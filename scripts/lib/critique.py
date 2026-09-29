#!/usr/bin/env python3
"""Validate Emperor Time Judgment self-critique eight-count (G4).

Doctrine: chains/judgment-chain/self-critique.md — eight counts, each showing
what was examined. Critique *file presence* is not eight-count completeness.

Harness-driven G4 (HARNESS_DRIVES_G4_CHECKS):
  When a harness plan exists, --check-critique SKIPs if critique is
  forbidden/unlisted; Optional → SKIP when unused; Tools → require
  eight-count. No plan → legacy always-on. Closes tiny catch-22 where
  FORCE_TABLE forbids critique but G4 demanded eight-count.

Always-fail HARD-GATE helpers:
  --reject-incomplete-critique   refuse missing/partial/unexamined counts

Check mode:
  --check-critique PATH   task dir or critique file (exit 1 on soft critique)

Positional PATH runs the same check. No args prints the CRITIQUE card.
Thin twins: scripts/critique.sh / scripts/critique.ps1
Alias: self-critique → same core.
G4 in gate.py calls --check-critique on the task dir.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence
from check_report import report_check

LEAF = "chains/judgment-chain/self-critique.md"
TEMPLATE = "templates/critique.md"

# Eight axes — name + matcher (table Count cell, heading, or prose label).
_AXES: tuple[tuple[int, str, re.Pattern[str]], ...] = (
    (
        1,
        "Requirements coverage",
        re.compile(r"(?i)requirements\s+coverage"),
    ),
    (
        2,
        "Correctness at the edges",
        re.compile(r"(?i)correctness\s+at\s+the\s+edges"),
    ),
    (
        3,
        "Hidden assumptions",
        re.compile(r"(?i)hidden\s+assumptions"),
    ),
    (
        4,
        "Evidence quality",
        re.compile(r"(?i)evidence\s+quality"),
    ),
    (
        5,
        "Regression surface",
        re.compile(r"(?i)regression\s+surface"),
    ),
    (
        6,
        "Security and safety",
        re.compile(r"(?i)security\s*(?:&|and)\s*safety"),
    ),
    (
        7,
        "Simpler alternative",
        re.compile(r"(?i)simpler\s+alternative"),
    ),
    (
        8,
        "Honesty of the report",
        re.compile(r"(?i)honesty\s+of\s+the\s+report"),
    ),
)

_EMPTYISH = re.compile(
    r"(?i)^\s*(?:[-–—.]|n/?a|todo|tbd|none\s+checked|unexamined|"
    r"pending|\.\.\.|…)?\s*$"
)

_HEADERISH = re.compile(
    r"(?i)^\s*\|\s*#\s*\|\s*Count\b|^\s*\|\s*-{3,}"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _combined_text(task_or_file: Path) -> tuple[str, list[Path]]:
    """Return critique text + source paths.

    PATH may be a task directory (critique.md / self-critique.md / ledger
    Self-critique section) or a single critique file.
    """
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    if not task_or_file.is_dir():
        return ("", [])

    parts: list[str] = []
    sources: list[Path] = []
    for name in ("critique.md", "self-critique.md"):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
            sources.append(p)
    ledger = task_or_file / "ledger.md"
    if ledger.is_file():
        text = _read(ledger)
        # Prefer dedicated files; still fold Self-critique / eight-counts
        # sections when those files are absent.
        if not parts and re.search(
            r"(?im)(?:^#{1,6}\s+.*(?:Self-critique|eight counts)\b|"
            r"Self-critique\s*:)",
            text,
        ):
            parts.append(text)
            sources.append(ledger)
        elif not parts:
            # Ledger alone with no critique section — not enough.
            pass
    return ("\n".join(parts), sources)


def _cells(line: str) -> list[str]:
    if not line.strip().startswith("|"):
        return []
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _table_axis_rows(text: str) -> dict[int, tuple[str, str]]:
    """Map axis number → (count_label, checked_cell) from markdown tables."""
    found: dict[int, tuple[str, str]] = {}
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        if _HEADERISH.search(line):
            continue
        cells = _cells(line)
        if len(cells) < 3:
            continue
        # Expect: # | Count | Checked | ...
        num_m = re.match(r"^\s*(\d+)\s*$", cells[0])
        if not num_m:
            # Sometimes Count is first data-ish cell without leading #
            continue
        num = int(num_m.group(1))
        if num < 1 or num > 8:
            continue
        count_label = cells[1]
        checked = cells[2] if len(cells) > 2 else ""
        # Confirm label matches expected axis when possible
        axis = next((a for a in _AXES if a[0] == num), None)
        if axis is not None and not axis[2].search(count_label):
            # Number present but wrong label — still record; validate later
            pass
        found[num] = (count_label, checked)
    return found


def _prose_axis_hits(text: str) -> dict[int, str]:
    """Map axis number → evidence snippet from headings / numbered prose.

    Table rows are preferred (see _table_axis_rows). This path covers
    `### 1. Requirements coverage` / `1. Requirements coverage — checked…`
    forms when no table is used.
    """
    found: dict[int, str] = {}
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # Skip table rows — handled elsewhere
        if line.strip().startswith("|"):
            continue
        structured = bool(
            re.match(r"^\s*#{1,6}\s+", line)
            or re.match(r"^\s*\d+[.)]\s+", line)
        )
        if not structured:
            continue
        for num, name, pat in _AXES:
            if num in found:
                continue
            if not pat.search(line):
                continue
            # Prefer matching count number when present
            num_m = re.match(r"^\s*(?:#{1,6}\s*)?(\d+)[.)]?\s+", line)
            if num_m and int(num_m.group(1)) != num:
                continue
            body: list[str] = []
            # Inline after em-dash / colon once the axis name is stripped
            after = pat.split(line, maxsplit=1)
            if len(after) > 1:
                tail = after[1].strip(" 	-—–:()[]")
                # Drop parenthetical template hints; keep real checked prose
                if tail and not re.match(
                    r"(?i)^(all of G1|empty/huge|environment|do tests|"
                    r"what else|injection|could half|does the summary)",
                    tail,
                ):
                    body.append(tail)
            for j in range(i + 1, min(i + 12, len(lines))):
                nxt = lines[j]
                if re.match(r"^\s*#{1,6}\s+", nxt):
                    break
                if re.match(r"^\s*\d+[.)]\s+", nxt):
                    break
                if nxt.strip().startswith("|"):
                    break
                if nxt.strip():
                    body.append(nxt.strip())
                    break
            found[num] = " ".join(body).strip()
    return found


def _checked_ok(checked: str) -> bool:
    if not checked or _EMPTYISH.match(checked):
        return False
    # Refuse pure "none" / "no findings" as Checked evidence of examination
    if re.fullmatch(r"(?i)none|no findings|n/?a", checked.strip()):
        return False
    return len(checked.strip()) >= 3


def validate(path: Path) -> list[str]:
    """Mechanical eight-count checks for a task dir or critique file."""
    errors: list[str] = []
    if not path.exists():
        return [f"missing path: {path}"]

    text, sources = _combined_text(path)
    if not text.strip():
        return [
            f"no critique.md / self-critique.md under {path} "
            "(eight-count needs a critique artifact; file presence theater "
            f"without axes fails — open {TEMPLATE})"
        ]

    table = _table_axis_rows(text)
    prose = _prose_axis_hits(text)

    missing: list[str] = []
    unexamined: list[str] = []
    mislabeled: list[str] = []

    for num, name, pat in _AXES:
        label_checked: tuple[str, str] | None = None
        if num in table:
            label_checked = table[num]
            if not pat.search(label_checked[0]):
                mislabeled.append(
                    f"count {num} label {label_checked[0]!r} "
                    f"does not match {name!r}"
                )
        elif num in prose:
            label_checked = (name, prose[num])
        else:
            # Last resort: axis name anywhere with nearby evidence is weak —
            # require structured table or numbered/heading form.
            if pat.search(text):
                # Name dropped in prose without structure → still incomplete
                missing.append(f"{num}. {name} (mentioned but not structured)")
            else:
                missing.append(f"{num}. {name}")
            continue

        _label, checked = label_checked
        if not _checked_ok(checked):
            unexamined.append(
                f"{num}. {name} (Checked empty/unexamined — "
                "'no findings' without naming what was checked is not a pass)"
            )

    if missing:
        errors.append(
            "incomplete eight-count — missing axes: " + "; ".join(missing)
        )
    if unexamined:
        errors.append(
            "unexamined counts (empty Checked): " + "; ".join(unexamined)
        )
    if mislabeled:
        for m in mislabeled:
            errors.append(m)

    # De-dupe
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "CRITIQUE checklist=yes",
        f"CRITIQUE leaf={LEAF}",
        f"CRITIQUE template={TEMPLATE}",
        "CRITIQUE iron=NO_G4_WITHOUT_EIGHT_COUNT_CRITIQUE",
        "CRITIQUE iron=HARNESS_DRIVES_G4_CHECKS",
        "STEP 1 id=presence name=Critique artifact "
        "et=critique.md or self-critique section exists",
        "STEP 1 key=File presence alone is theater — continue to eight-count",
        "STEP 2 id=eight-axes name=All eight axes present "
        "et=Requirements / Edges / Assumptions / Evidence / Regression / "
        "Security / Simpler / Honesty",
        "STEP 2 key=Open templates/critique.md; fill every Count row",
        "STEP 3 id=examined name=Checked cell names examination "
        "et=commands run / paths read per count; empty Checked = FAIL",
        "STEP 3 key='No findings' without Checked evidence is unexamined",
        "STEP 4 id=disposition name=Findings disposition + Verdict "
        "et=blocker/should-fix/note; PASS|PASS-WITH-CONDITIONS|FAIL",
        "STEP 4 key=Hand to hetero-critique or verdicts-and-breaches",
        "",
        "MUST: Before G4, when harness plan selects critique (Tools) or optional "
        "critique shows activity, critique carries all eight counts with "
        f"Checked evidence. Tiny/unlisted → SKIP (HARNESS_DRIVES_G4_CHECKS). "
        f"Open {LEAF}; run scripts/emperor critique <task-dir>. G4 calls this.",
        "MUST-NOT: critique-file-present theater; empty Checked cells; "
        "batching 'criteria 1–4 look fine'; skipping an axis.",
    ]
    return "\n".join(lines) + "\n"


def reject_incomplete_critique() -> str:
    return (
        "REJECT INCOMPLETE CRITIQUE: HARD-GATE — G4 refuses without all eight "
        "self-critique counts and non-empty Checked evidence per axis. "
        "Critique file presence ≠ eight-count completeness. "
        f"Open {LEAF}; fill {TEMPLATE}; "
        "re-run scripts/emperor critique <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time Judgment self-critique eight-count "
            "(all eight axes + Checked evidence)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir or critique file (omit to print CRITIQUE card)",
    )
    p.add_argument(
        "--check-critique",
        type=Path,
        metavar="PATH",
        default=None,
        help="eight-count structure check (exit 1 on soft/incomplete critique)",
    )
    p.add_argument(
        "--reject-incomplete-critique",
        action="store_true",
        help="Hard-gate: refuse incomplete/unexamined eight-count (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_incomplete_critique:
        sys.stdout.write(reject_incomplete_critique())
        return 1

    target = args.check_critique if args.check_critique is not None else args.path
    if target is None:
        sys.stdout.write(format_card())
        return 0

    # Harness drives which G4 checks run (ask→spec → effort_class → tools).
    # Tiny forbids critique → SKIP eight-count (closes catch-22 vs
    # FORBIDDEN_TOOLS_NEVER_RUN). No plan → legacy always-on.
    mode = "always"
    if target.is_dir() or target.exists():
        try:
            from harness_plan import g4_check_mode, tool_was_used

            mode = g4_check_mode(target, "critique")
            if mode == "skip":
                return report_check(
                    "critique", target, [], vacuous=True
                )
            if mode == "activity" and not tool_was_used(
                target if target.is_dir() else target.parent, "critique"
            ):
                return report_check(
                    "critique", target, [], vacuous=True
                )
        except Exception:
            mode = "always"

    # Proportionality: count critique only when the check actually runs.
    # Missing effort_class stamps DEFAULT_EFFORT_CLASS=tiny.
    if target.is_dir() and mode in ("require", "activity", "always"):
        try:
            from proportionality import bump_and_check

            prop_errs = bump_and_check(target, "critique")
            if prop_errs:
                for e in prop_errs:
                    print(f"critique FAIL: {e}", file=sys.stderr)
                return 1
        except Exception:
            pass

    errs = validate(target)
    return report_check("critique", target, errs, vacuous=False)


if __name__ == "__main__":
    raise SystemExit(main())
