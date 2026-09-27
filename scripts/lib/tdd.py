#!/usr/bin/env python3
"""TDD iron-law / red-green-refactor checklist for emperor-tdd (Python core).

Leaf adapted from obra/superpowers skills/test-driven-development
"The Iron Law" + "Red-Green-Refactor" (MIT) — HARD-GATE only.
Emperor Time + emperor-tdd stay the orchestrator; do not announce
the foreign skill name.

Prints TDD / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-prod always fails (hard gate when jumping to production
code before a failing probe was observed). Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-tdd/red-green-refactor.md"
SOURCE = "obra/superpowers test-driven-development → The Iron Law / Red-Green-Refactor"

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "red",
        "name": "RED — Write failing probe",
        "et": "work-order Expected: FAIL / ledger HYPOTHESIS",
        "success": "Probe written; predicted FAIL signal ledgered before run",
        "key": "One behavior; clear name; real code; predict FAIL first",
    },
    {
        "n": "2",
        "id": "verify-red",
        "name": "Verify RED — Watch it FAIL",
        "et": "scientific-method claim / quote FAIL tail",
        "success": "FAIL observed and quoted; proves absence (not typo)",
        "key": "MANDATORY; if pass → fix probe; if error → fix harness then re-fail",
    },
    {
        "n": "3",
        "id": "green",
        "name": "GREEN — Minimal production code",
        "et": "BUILD / G3",
        "success": "Smallest change that would make that probe pass",
        "key": "Nothing else; no riders; no sibling refactors",
    },
    {
        "n": "4",
        "id": "verify-green",
        "name": "Verify GREEN — Watch it PASS",
        "et": "G3 / G4 evidence",
        "success": "PASS quoted; project suite run; reds named",
        "key": "MANDATORY; single-probe green ≠ suite green",
    },
    {
        "n": "5",
        "id": "refactor",
        "name": "REFACTOR — Clean while green",
        "et": "stay on G3",
        "success": "Cleanup done; probes still green; no new behavior",
        "key": "After green only; re-run after each cleanup",
    },
]


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "TDD checklist=yes",
        f"TDD leaf={LEAF}",
        f"TDD source={SOURCE}",
        "TDD iron=NO_PRODUCTION_CODE_WITHOUT_FAILING_PROBE_FIRST",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..5, got {focus}")
        selected = [s]
        lines.append(f"TDD focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Complete each RGR step before the next. No production code "
        "before Step 2 FAIL was observed and quoted. Delete impl written "
        f"earlier. Open {LEAF} and run scripts/emperor tdd to reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole test-driven-development; skip verify-red; "
        "keep pre-probe code as reference; call green from one probe without "
        "the project suite. ET + emperor-tdd remain the orchestrator."
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


def reject_prod() -> str:
    return (
        "REJECT PROD: HARD-GATE — no production code before TDD "
        "checklist Step 2 FAIL was observed and quoted. "
        f"Open {LEAF}; run scripts/emperor tdd. "
        "Delete impl written earlier; replay RED → verify-red first.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print Emperor Time TDD iron-law / RGR checklist for emperor-tdd."
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
        "--reject-prod",
        action="store_true",
        help="Hard-gate: refuse production code before failing probe (exit 1)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_prod:
        sys.stdout.write(reject_prod())
        return 1

    if args.advance is not None:
        frm, to = args.advance
        ok, msg = check_advance(frm, to)
        sys.stdout.write(msg + "\n")
        if not ok:
            return 1
        sys.stdout.write(format_card(focus=to))
        return 0

    try:
        sys.stdout.write(format_card(focus=args.step))
    except ValueError as exc:
        print(f"tdd: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
