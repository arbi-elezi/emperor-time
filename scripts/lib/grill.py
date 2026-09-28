#!/usr/bin/env python3
"""Grill / brainstorm checklist for emperor require-design (Python core).

Leaf adapted from obra/superpowers skills/brainstorming
"HARD-GATE" (MIT) — questions before code / reject jumping to impl.
Path taxonomy vertical depth: spike | bounded | architectural must be
announced; stage approval must match the path; impl before stage approval
fails. Emperor Time + require-design stay the orchestrator; do not announce
the foreign skill name.

Prints GRILL / STEP / MUST lines. Optional --step and --advance enforce
order. Always-fail HARD-GATE helpers:
  --reject-impl                 refuse jumping to impl (legacy)
  --reject-no-path              refuse missing path type
  --reject-stage-skip           refuse skipped stage
  --reject-impl-before-approval refuse impl before stage approval

Check mode:
  --check-path PATH   task dir or ledger/grill file (exit 1 when path
                      type missing, stage skipped, or impl before approval)

Does not mutate the tree. Thin twins: scripts/grill.sh / scripts/grill.ps1.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence

LEAF = "skills/emperor-require-design/grill-checklist.md"
SOURCE = "obra/superpowers brainstorming → HARD-GATE"

PATH_TYPES = ("spike", "bounded", "architectural")

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "classify",
        "name": "Classify the path",
        "et": "ledger / Size notes",
        "success": "spike | bounded | architectural announced; partner may override",
        "key": "Announce path out loud; heavier when unsure; ratchet upgrades only",
    },
    {
        "n": "2",
        "id": "grill-intent",
        "name": "Grill intent (Socratic)",
        "et": "scope / Dowsing gaps",
        "success": "Purpose, constraints, success criteria clear",
        "key": "One focused question at a time; no features/approach until intent clear",
    },
    {
        "n": "3",
        "id": "write-back",
        "name": "Write-back understanding",
        "et": "G1 match",
        "success": "Partner corrects or confirms the brief",
        "key": "Summarize outcome/constraints/success; separate said vs assumptions",
    },
    {
        "n": "4",
        "id": "present-design",
        "name": "Present design (path-scaled)",
        "et": "work-order / chat",
        "success": "Design artifact exists to approve (no product code yet)",
        "key": "Spike probe / bounded chat design / architectural work-order (G2)",
    },
    {
        "n": "5",
        "id": "get-approval",
        "name": "Get approval — then STOP",
        "et": "G2 → BUILD",
        "success": "Explicit yes on the artifact presented; gate open for BUILD",
        "key": "STOP until yes; presenting and coding in one breath skips the gate",
    },
]

# Path: spike | bounded | architectural  (also Grill path / Path type)
_PATH_LINE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:\*\*)?(?:Grill\s+)?Path(?:\s+type)?(?:\*\*)?\s*:\s*"
    r"(?P<body>.+\S)\s*$"
)

_STAGE_LINE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:\*\*)?Stage\s+approval(?:\*\*)?\s*:\s*"
    r"(?P<body>.+\S)\s*$"
)

_PATH_THEATER = re.compile(
    r"(?i)^\s*(?:tbd|todo|pending|placeholder|\?+|n/?a|none|unclassified|"
    r"too\s+simple|skip|unset|missing)\s*$"
)

_STAGE_EMPTYISH = re.compile(
    r"(?i)^\s*(?:tbd|todo|pending|placeholder|\?+|n/?a|none|empty|"
    r"skipped?|not\s+yet|-|\.\.\.|…)\s*$"
)

# Idea/feature approval is not stage approval (Superpowers HARD-GATE).
_IDEA_ONLY = re.compile(
    r"(?i)^\s*(?:idea|feature(?:\s+scope)?|concept|scope)\s+approved\b"
)

_PROBE_OK = re.compile(
    r"(?i)\b(?:probe|question\s*\+?\s*probe|question\s+and\s+probe)\s+approved\b"
)
_DESIGN_OK = re.compile(
    r"(?i)\b(?:short\s+)?(?:in-chat\s+)?design\s+approved\b"
)
_WO_OK = re.compile(
    r"(?i)\b(?:work[- ]?order|written\s+spec|spec(?:\s+file)?)\s+approved\b"
)

# Evidence that implementation / BUILD already happened.
_IMPL_EVIDENCE = re.compile(
    r"(?im)^#{1,6}\s*G3\b.*$|"
    r"^\s*(?:[-*]\s*)?(?:\*\*)?Change\s+summary(?:\*\*)?\s*:\s*\S|"
    r"^\s*(?:[-*]\s*)?(?:\*\*)?Build(?:\*\*)?\s*:\s*\S|"
    r"\b(?:impl(?:ementation)?\s+started|product\s+code\s+written|"
    r"scaffolding\s+landed|BUILD\s+invoked)\b"
)


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "GRILL checklist=yes",
        f"GRILL leaf={LEAF}",
        f"GRILL source={SOURCE}",
        "GRILL iron=NO_IMPL_WITHOUT_DESIGN_APPROVAL",
        "GRILL paths=spike|bounded|architectural",
        "GRILL iron=PATH_AND_STAGE_BEFORE_IMPL",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..5, got {focus}")
        selected = [s]
        lines.append(f"GRILL focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Complete each grill step before the next. Announce path "
        "(spike|bounded|architectural); record Stage approval for the "
        "artifact presented. No product code, scaffolding, or BUILD before "
        f"stage approval. Open {LEAF}; run scripts/emperor grill "
        "--check-path <task-dir>."
    )
    lines.append(
        "MUST-NOT: load whole brainstorming; jump to impl; skip path "
        "classification; treat idea-approval as stage approval; announce a "
        "foreign master router. ET + require-design remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def check_advance(frm: int, to: int) -> tuple[bool, str]:
    """Enforce sequential advancement. Same step or +1 only."""
    if frm < 1 or frm > 5 or to < 1 or to > 5:
        return False, f"ADVANCE FAIL: steps must be 1..5 (from={frm} to={to})"
    if to < frm:
        return (
            False,
            f"ADVANCE FAIL: cannot go backward ({frm} → {to}); "
            f"re-enter Step {to} explicitly via --step",
        )
    if to > frm + 1:
        return (
            False,
            f"ADVANCE FAIL: cannot skip ({frm} → {to}); next allowed is {frm + 1}",
        )
    if to == frm:
        return True, f"ADVANCE OK: stay on Step {frm}"
    nxt = _step_by_n(to)
    assert nxt is not None
    return True, f"ADVANCE OK: Step {frm} → {to} ({nxt['name']})"


def reject_impl() -> str:
    return (
        "REJECT IMPL: HARD-GATE — no implementation action before grill "
        "checklist Step 5 approval. "
        f"Open {LEAF}; run scripts/emperor grill. "
        "Do not scaffold, write product code, or invoke BUILD yet.\n"
    )


def reject_no_path() -> str:
    return (
        "REJECT NO PATH: HARD-GATE — grill refuses without an announced path "
        "type (spike | bounded | architectural). Classify out loud; record "
        f"`Path: …` in the ledger. Open {LEAF}; run scripts/emperor grill "
        "--check-path <task-dir>.\n"
    )


def reject_stage_skip() -> str:
    return (
        "REJECT STAGE SKIP: HARD-GATE — a reply approves the stage actually "
        "presented; idea/feature approval does not approve missing artifacts. "
        "Resume at the earliest incomplete stage. "
        f"Open {LEAF}; run scripts/emperor grill --check-path <task-dir>.\n"
    )


def reject_impl_before_approval() -> str:
    return (
        "REJECT IMPL BEFORE APPROVAL: HARD-GATE — no product code, scaffolding, "
        "or BUILD before path-scaled stage approval (spike: probe; bounded: "
        "short design; architectural: work-order/spec). "
        f"Open {LEAF}; run scripts/emperor grill --check-path <task-dir>.\n"
    )


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _combined_text(task_or_file: Path) -> tuple[str, list[Path]]:
    """Return combined text + source paths.

    PATH may be a task directory (ledger.md / grill.md / path.md) or a
    single markdown file.
    """
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    if not task_or_file.is_dir():
        return ("", [])

    parts: list[str] = []
    sources: list[Path] = []
    for name in ("ledger.md", "grill.md", "path.md", "notes.md"):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
            sources.append(p)
    return ("\n".join(parts), sources)


def _strip_md(s: str) -> str:
    """Strip light markdown emphasis / bullets from a captured body."""
    t = s.strip()
    t = re.sub(r"^\*+\s*", "", t)
    t = re.sub(r"\s*\*+$", "", t)
    t = t.strip().strip("*").strip()
    return t


def _normalize_path(body: str) -> str | None:
    """Return canonical path type or None if not a known type."""
    token = _strip_md(body).lower()
    # Allow trailing notes: "bounded — small flag"
    first = re.split(r"[\s,;/|—–-]+", token, maxsplit=1)[0]
    if first in PATH_TYPES:
        return first
    for p in PATH_TYPES:
        if re.search(rf"\b{p}\b", token):
            return p
    return None


def _stage_body_ok(path_type: str, body: str) -> tuple[bool, str]:
    """Return (ok, reason). reason is failure code when not ok."""
    text = body.strip()
    if _STAGE_EMPTYISH.match(text):
        return False, "stage skipped"
    if _IDEA_ONLY.match(text):
        return False, "stage skipped"  # idea ≠ design artifact

    if path_type == "spike":
        if _PROBE_OK.search(text) or re.search(
            r"(?i)\bapproved\b.*\bprobe\b|\bprobe\b.*\bapproved\b", text
        ):
            return True, ""
        # Explicit "Stage approval: yes — probe" style
        if re.search(r"(?i)\bprobe\b", text) and re.search(
            r"(?i)\b(?:yes|approved|ok|nod)\b", text
        ):
            return True, ""
        return False, "stage skipped"

    if path_type == "bounded":
        if _DESIGN_OK.search(text):
            return True, ""
        if re.search(r"(?i)\bdesign\b", text) and re.search(
            r"(?i)\b(?:yes|approved|ok)\b", text
        ):
            return True, ""
        # work-order approval is heavier — allowed (ratchet up)
        if _WO_OK.search(text):
            return True, ""
        return False, "stage skipped"

    # architectural
    if _WO_OK.search(text):
        return True, ""
    if re.search(r"(?i)\b(?:work[- ]?order|spec)\b", text) and re.search(
        r"(?i)\b(?:yes|approved|ok)\b", text
    ):
        return True, ""
    # Chat/design-only is a stage skip for architectural
    if _DESIGN_OK.search(text) or (
        re.search(r"(?i)\bdesign\b", text)
        and not re.search(r"(?i)\b(?:work[- ]?order|spec)\b", text)
    ):
        return False, "stage skipped"
    return False, "stage skipped"


def check_path(path: Path) -> list[str]:
    """Mechanical path-taxonomy checks. Empty list = PASS.

    Fails when:
      - path type missing / theater / unknown
      - stage skipped (missing, idea-only, or wrong stage for path)
      - impl evidence present before stage approval
    """
    errors: list[str] = []
    if not path.exists():
        return [f"missing path: {path}"]

    text, sources = _combined_text(path)
    if not text.strip():
        return [
            f"no ledger/grill notes under {path} — cannot prove path type "
            "(record Path: spike|bounded|architectural)"
        ]

    path_m = _PATH_LINE.search(text)
    if path_m is None:
        errors.append(
            "path type missing — announce Path: spike|bounded|architectural "
            f"(open {LEAF})"
        )
        # Still check impl: missing path + impl = also impl-before-approval
        if _IMPL_EVIDENCE.search(text):
            errors.append(
                "impl before stage approval — G3/Build evidence without path "
                "+ stage approval"
            )
        return errors

    body = _strip_md(path_m.group("body") or "")
    if _PATH_THEATER.match(body):
        errors.append(
            f"path type missing (theater `{body}`) — must be "
            "spike|bounded|architectural"
        )
        return errors

    path_type = _normalize_path(body)
    if path_type is None:
        errors.append(
            f"path type missing (unknown `{body}`) — must be "
            "spike|bounded|architectural"
        )
        return errors

    stage_m = _STAGE_LINE.search(text)
    stage_ok = False
    if stage_m is None:
        errors.append(
            f"stage skipped — Path={path_type} but no Stage approval line "
            "(approve the artifact presented for this path)"
        )
    else:
        stage_body = _strip_md(stage_m.group("body") or "")
        ok, reason = _stage_body_ok(path_type, stage_body)
        if not ok:
            if _IDEA_ONLY.match(stage_body):
                errors.append(
                    "stage skipped — idea/feature approval ≠ design artifact "
                    f"approval (Path={path_type}; resume earliest incomplete stage)"
                )
            elif path_type == "architectural" and (
                _DESIGN_OK.search(stage_body)
                or (
                    re.search(r"(?i)\bdesign\b", stage_body)
                    and not re.search(
                        r"(?i)\b(?:work[- ]?order|spec)\b", stage_body
                    )
                )
            ):
                errors.append(
                    "stage skipped — architectural Path needs work-order/spec "
                    "approval; conversational design only permits writing the "
                    "work order"
                )
            else:
                errors.append(
                    f"stage skipped — Stage approval `{stage_body}` does not "
                    f"match Path={path_type} prerequisites"
                )
        else:
            stage_ok = True

    if _IMPL_EVIDENCE.search(text) and not stage_ok:
        errors.append(
            "impl before stage approval — Build/G3 evidence present without "
            f"valid Path={path_type} stage approval"
        )

    # sources unused except for future diagnostics; silence lint
    _ = sources
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time grill/brainstorm checklist for require-design; "
            "enforce path taxonomy + stage approval HARD-GATE."
        )
    )
    parser.add_argument(
        "--step",
        type=int,
        choices=(1, 2, 3, 4, 5),
        default=None,
        help="Print only one step detail (still emits MUST lines)",
    )
    parser.add_argument(
        "--advance",
        nargs=2,
        type=int,
        metavar=("FROM", "TO"),
        help="Validate sequential step advance (exit 1 on skip)",
    )
    parser.add_argument(
        "--reject-impl",
        action="store_true",
        help="Hard-gate: refuse jumping to implementation (exit 1)",
    )
    parser.add_argument(
        "--reject-no-path",
        action="store_true",
        help="Hard-gate: refuse missing path type (exit 1)",
    )
    parser.add_argument(
        "--reject-stage-skip",
        action="store_true",
        help="Hard-gate: refuse skipped stage (exit 1)",
    )
    parser.add_argument(
        "--reject-impl-before-approval",
        action="store_true",
        help="Hard-gate: refuse impl before stage approval (exit 1)",
    )
    parser.add_argument(
        "--check-path",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "path taxonomy check (exit 1 when path missing, stage skipped, "
            "or impl before approval)"
        ),
    )
    parser.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="optional task dir / ledger (same as --check-path)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_impl:
        sys.stdout.write(reject_impl())
        return 1
    if args.reject_no_path:
        sys.stdout.write(reject_no_path())
        return 1
    if args.reject_stage_skip:
        sys.stdout.write(reject_stage_skip())
        return 1
    if args.reject_impl_before_approval:
        sys.stdout.write(reject_impl_before_approval())
        return 1

    if args.advance is not None:
        frm, to = args.advance
        ok, msg = check_advance(frm, to)
        sys.stdout.write(msg + "\n")
        if not ok:
            return 1
        sys.stdout.write(format_card(focus=to))
        return 0

    target = args.check_path if args.check_path is not None else args.path
    if target is not None:
        errs = check_path(target)
        if errs:
            for e in errs:
                print(f"grill FAIL: {e}", file=sys.stderr)
            return 1
        print(f"grill PASS: path taxonomy ok ({target})")
        return 0

    try:
        sys.stdout.write(format_card(focus=args.step))
    except ValueError as exc:
        print(f"grill: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
