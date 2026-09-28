#!/usr/bin/env python3
"""Validate Emperor Time work-order plan header + Task-N structure (G2).

Leaf adapted from obra/superpowers skills/writing-plans
"Plan Document Header" (MIT) — Goal / Architecture / Tech Stack / Spec /
Global Constraints / Review Focus — plus Task-N bite-sized structure
(Files / Expected FAIL+PASS / Commit; no bare TBD). Emperor Time keeps
the orchestrator; this module locks the shapes.

Always-fail HARD-GATE helpers:
  --reject-tbd        refuse TBD / placeholder plans
  --reject-no-tasks   refuse work-orders with no Task N headings

Check mode:
  --check-tasks PATH  Task-N structure only (exit 1 on soft skeleton)

Positional PATH runs full validate (header + Task-N). No args prints the
TASKS card. Thin twins: scripts/work-order.sh / scripts/work-order.ps1
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence

LEAF = "references/work-order.md"
TEMPLATE = "templates/work-order.md"

REQUIRED_INLINE = (
    ("**Goal:**", re.compile(r"(?im)^\*\*Goal:\*\*\s+\S")),
    ("**Architecture:**", re.compile(r"(?im)^\*\*Architecture:\*\*\s+\S")),
    ("**Tech Stack:**", re.compile(r"(?im)^\*\*Tech Stack:\*\*\s+\S")),
    ("**Spec:**", re.compile(r"(?im)^\*\*Spec:\*\*\s+\S")),
)

REQUIRED_SECTIONS = (
    ("## Global Constraints", re.compile(r"(?im)^##\s+Global Constraints\s*$")),
    ("## Review Focus", re.compile(r"(?im)^##\s+Review Focus\s*$")),
)

PLACEHOLDER = re.compile(
    r"(?i)<[^>]+>|\[(?:one sentence|2-3 sentences|key technologies|"
    r"path to|the five|TODO|TBD)[^\]]*\]|\bTBD\b|\.\.\.\s*$"
)

_TASK_HEAD = re.compile(
    r"^(#{1,6})[ \t]+Task[ \t]+(\d+)\b(.*)$",
    re.MULTILINE,
)

_TRIVIAL = re.compile(
    r"(?im)^\s*-\s*\*\*Size:\*\*\s*trivial\b|^\*\*Size:\*\*\s*trivial\b|"
    r"Size:\s*trivial\b"
)

_TBD_BARE = re.compile(r"(?i)\bTBD\b|\bTODO\b|<name>|<path>|<exact ")

_FILES_HEAD = re.compile(r"(?im)^\*\*Files:\*\*|^\s*Files:\s*$")
_COMMIT = re.compile(r"(?im)^\*\*Commit:\*\*\s+\S|^Commit:\s+\S")
_EXPECTED_FAIL = re.compile(r"(?im)^Expected:\s*FAIL\b")
_EXPECTED_PASS = re.compile(r"(?im)^Expected:\s*PASS\b")
_PATHISH = re.compile(
    r"(?im)^\s*-\s*(?:Create|Modify|Delete|Touch):\s*\S|"
    r"`[^`]+`|\b[\w./-]+\.\w{1,8}\b"
)


def _section_body(text: str, heading_re: re.Pattern[str]) -> str | None:
    m = heading_re.search(text)
    if not m:
        return None
    rest = text[m.end() :]
    nxt = re.search(r"(?m)^##\s+", rest)
    body = rest if nxt is None else rest[: nxt.start()]
    return body


def _body_ok(body: str) -> bool:
    lines = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("<!--"):
            continue
        if PLACEHOLDER.search(line) and len(re.sub(r"\W+", "", line)) < 12:
            continue
        lines.append(line)
    if not lines:
        return False
    joined = "\n".join(lines)
    if re.search(r"(?i)\bnone\b.*\bchecked\b|\bchecked\b.*\bnone\b|^none\s*$", joined):
        return True
    for line in lines:
        if PLACEHOLDER.search(line) and len(line) < 40:
            continue
        if line.startswith(("-", "*", "|")) or len(line) >= 8:
            return True
    return False


def _is_trivial(text: str) -> bool:
    return bool(_TRIVIAL.search(text))


def _iter_tasks(text: str) -> list[tuple[int, str]]:
    """Return [(n, body_including_heading), ...] in document order."""
    matches = list(_TASK_HEAD.finditer(text))
    out: list[tuple[int, str]] = []
    for i, m in enumerate(matches):
        n = int(m.group(2))
        start = m.start()
        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)
        # Fence-aware end: do not let a fenced ### Task example truncate,
        # but sibling Task headings outside fences always end the slice
        # (matches list already ignores nothing — headings are real).
        body = text[start:end]
        # If next match was inside a fence relative to this task, still OK:
        # real work-orders do not nest Task headings in fences as siblings.
        out.append((n, body))
    return out


def validate_header(text: str) -> list[str]:
    errors: list[str] = []
    for label, rx in REQUIRED_INLINE:
        if not rx.search(text):
            errors.append(f"missing filled {label} line")
    for label, rx in REQUIRED_SECTIONS:
        body = _section_body(text, rx)
        if body is None:
            errors.append(f"missing section {label}")
        elif not _body_ok(body):
            errors.append(f"empty or placeholder-only {label}")
    return errors


def validate_tasks(text: str) -> list[str]:
    """Mechanical Task-N structure (non-trivial work orders)."""
    errors: list[str] = []
    tasks = _iter_tasks(text)
    if not tasks:
        errors.append(
            "no Task N headings (need '### Task 1 — …' bite-sized units)"
        )
        return errors

    contract = _section_body(
        text, re.compile(r"(?im)^##\s+Contract\b.*$")
    )
    if contract is not None and _TBD_BARE.search(contract):
        # Allow explicit none; fail bare TBD/TODO/<path> placeholders
        if not re.search(r"(?i)\bnone\b.*\bchecked\b", contract):
            errors.append("Contract section has TBD/TODO/placeholder")

    return _validate_tasks_bodies(tasks, errors)


def _validate_tasks_bodies(
    tasks: list[tuple[int, str]], errors: list[str]
) -> list[str]:
    seen: set[int] = set()
    for n, body in tasks:
        if n in seen:
            errors.append(f"duplicate Task {n} heading")
        seen.add(n)
        lines = body.splitlines()
        title = ""
        if lines:
            tm = _TASK_HEAD.match(lines[0])
            if tm:
                title = (tm.group(3) or "").strip().lstrip("—-").strip()
        if (
            not title
            or title.lower() in {"<name>", "…", "..."}
            or (PLACEHOLDER.search(title) and len(title) < 20)
        ):
            errors.append(f"Task {n} missing real title (not <name>/TBD)")

        if not _FILES_HEAD.search(body):
            errors.append(f"Task {n} missing **Files:** section")
        elif not _PATHISH.search(body):
            errors.append(f"Task {n} Files: has no real Create/Modify path")

        if not _EXPECTED_FAIL.search(body):
            errors.append(f"Task {n} missing 'Expected: FAIL' (probe first)")
        if not _EXPECTED_PASS.search(body):
            errors.append(f"Task {n} missing 'Expected: PASS'")

        if not _COMMIT.search(body):
            errors.append(f"Task {n} missing filled **Commit:** line")
        else:
            cm = None
            for line in lines:
                if re.match(r"(?im)^\*\*Commit:\*\*|^Commit:", line):
                    cm = line
                    break
            if cm and (
                PLACEHOLDER.search(cm)
                or re.search(r"(?i)<type>|<message>", cm)
            ):
                errors.append(f"Task {n} Commit: is placeholder")

    return errors


def validate(path: Path, *, tasks_only: bool = False) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"missing work-order: {path}"]
    text = path.read_text(encoding="utf-8", errors="replace")
    # trivial tasks skip header + Task-N lock (gate.sh already short-circuits)
    if _is_trivial(text):
        return []

    if not tasks_only:
        errors.extend(validate_header(text))
    errors.extend(validate_tasks(text))
    return errors


def format_card() -> str:
    lines = [
        "WORK-ORDER-TASKS checklist=yes",
        f"WORK-ORDER-TASKS leaf={LEAF}",
        f"WORK-ORDER-TASKS template={TEMPLATE}",
        "WORK-ORDER-TASKS iron=NO_BUILD_WITHOUT_TASK_N_STRUCTURE",
        "STEP 1 id=header name=Plan Document Header "
        "et=Goal/Architecture/Tech Stack/Spec + Global Constraints + Review Focus",
        "STEP 1 key=Filled lines; Review Focus or none (checked); no TBD",
        "STEP 2 id=tasks name=Bite-sized Task N units "
        "et=### Task N — title / Files / Expected FAIL then PASS / Commit",
        "STEP 2 key=Zero-context worker can execute Task N alone; probe first",
        "STEP 3 id=contract name=Contract between tasks "
        "et=Inputs/Outputs/Forbidden on disk; no TBD",
        "STEP 3 key=Interface assumptions written before BUILD",
        "",
        "MUST: Non-trivial work orders include plan header AND at least one "
        f"Task N with Files + Expected: FAIL + Expected: PASS + Commit. "
        f"Open {LEAF}; run scripts/emperor work-order <path>. "
        "G2 calls this module.",
        "MUST-NOT: skeleton Task headings; TBD in Contract; Expected: lines "
        "only at file level without Task N; jump to BUILD on soft markdown.",
    ]
    return "\n".join(lines) + "\n"


def reject_tbd() -> str:
    return (
        "REJECT TBD: HARD-GATE — work-order must not ship TBD/TODO/"
        f"placeholder Task N or Contract. Open {LEAF}; fill real paths, "
        "Expected: FAIL/PASS, and Commit. "
        "Re-run scripts/emperor work-order <path>.\n"
    )


def reject_no_tasks() -> str:
    return (
        "REJECT NO-TASKS: HARD-GATE — non-trivial work-order needs "
        "'### Task N — <name>' bite-sized units before BUILD. "
        f"Open {TEMPLATE}; run scripts/emperor work-order --check-tasks "
        "<path>. Zero-context workers cannot execute a vibe.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time work-order plan header + Task-N structure"
        )
    )
    p.add_argument(
        "work_order",
        type=Path,
        nargs="?",
        default=None,
        help="path to work-order.md (omit to print TASKS card)",
    )
    p.add_argument(
        "--check-tasks",
        type=Path,
        metavar="PATH",
        default=None,
        help="Task-N structure only (exit 1 on soft skeleton)",
    )
    p.add_argument(
        "--reject-tbd",
        action="store_true",
        help="Hard-gate: refuse TBD/placeholder plans (exit 1)",
    )
    p.add_argument(
        "--reject-no-tasks",
        action="store_true",
        help="Hard-gate: refuse missing Task N headings (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_tbd:
        sys.stdout.write(reject_tbd())
        return 1
    if args.reject_no_tasks:
        sys.stdout.write(reject_no_tasks())
        return 1

    if args.check_tasks is not None:
        errs = validate(args.check_tasks, tasks_only=True)
        if errs:
            for e in errs:
                print(f"work_order FAIL: {e}", file=sys.stderr)
            return 1
        print(f"work_order PASS tasks: {args.check_tasks}")
        return 0

    if args.work_order is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(args.work_order)
    if errs:
        for e in errs:
            print(f"work_order FAIL: {e}", file=sys.stderr)
        return 1
    print(f"work_order PASS: {args.work_order}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
