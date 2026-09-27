#!/usr/bin/env python3
"""Four-phase debug checklist for emperor heal (Python core).

Leaf adapted from obra/superpowers skills/systematic-debugging
"The Four Phases" (MIT) — list only. Emperor Time + Holy Chain stay
the orchestrator; do not announce the foreign skill name.

Prints PHASE / MUST lines. Optional --phase and --advance enforce order.
Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-heal/debug-four-phases.md"
SOURCE = "obra/superpowers systematic-debugging → The Four Phases"

PHASES: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "root-cause-investigation",
        "name": "Root Cause Investigation",
        "holy": "triage.md → reproduce-and-bisect.md",
        "success": "Understand WHAT and WHY before any fix",
        "key": "Read errors; reproduce; check recent changes; instrument boundaries; trace to source",
    },
    {
        "n": "2",
        "id": "pattern-analysis",
        "name": "Pattern Analysis",
        "holy": "reproduce-and-bisect.md",
        "success": "Identify differences vs working examples",
        "key": "Find working examples; compare references completely; list every difference; map deps",
    },
    {
        "n": "3",
        "id": "hypothesis-and-testing",
        "name": "Hypothesis and Testing",
        "holy": "reproduce-and-bisect.md (combat ledger)",
        "success": "One hypothesis confirmed or replaced — not stacked",
        "key": "Single hypothesis; minimal one-variable test; prediction before probe",
    },
    {
        "n": "4",
        "id": "implementation",
        "name": "Implementation",
        "holy": "heal-and-verify.md",
        "success": "Root-cause fix; cure + no-new-wounds + mechanism",
        "key": "Failing test first; single fix; verify triad; ≥3 fails → question architecture",
    },
]


def _phase_by_n(n: int) -> dict[str, str] | None:
    for p in PHASES:
        if int(p["n"]) == n:
            return p
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "DEBUG four_phases=yes",
        f"DEBUG leaf={LEAF}",
        f"DEBUG source={SOURCE}",
        "DEBUG iron=NO_FIXES_WITHOUT_ROOT_CAUSE_INVESTIGATION_FIRST",
    ]
    selected = PHASES
    if focus is not None:
        p = _phase_by_n(focus)
        if p is None:
            raise ValueError(f"phase must be 1..4, got {focus}")
        selected = [p]
        lines.append(f"DEBUG focus={focus}")

    for p in selected:
        lines.append(
            f"PHASE {p['n']} id={p['id']} name={p['name']} "
            f"holy={p['holy']}"
        )
        lines.append(f"PHASE {p['n']} key={p['key']}")
        lines.append(f"PHASE {p['n']} success={p['success']}")

    lines.append("")
    lines.append(
        "MUST: Complete each phase before the next. No fixes before Phase 1. "
        f"Open {LEAF} and the Holy aspect for the current phase. "
        "Run scripts/emperor heal to reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole systematic-debugging; skip phases under pressure; "
        "stack fixes; propose solutions before tracing root cause. "
        "ET + Holy Chain remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def check_advance(frm: int, to: int) -> tuple[bool, str]:
    """Enforce sequential advancement. Same phase or +1 only (or stay)."""
    if frm < 1 or frm > 4 or to < 1 or to > 4:
        return False, f"ADVANCE FAIL: phases must be 1..4 (from={frm} to={to})"
    if to < frm:
        return False, f"ADVANCE FAIL: cannot go backward ({frm} → {to}); re-enter Phase {to} explicitly via --phase"
    if to > frm + 1:
        return False, f"ADVANCE FAIL: cannot skip ({frm} → {to}); next allowed is {frm + 1}"
    if to == frm:
        return True, f"ADVANCE OK: stay on Phase {frm}"
    # to == frm + 1
    nxt = _phase_by_n(to)
    assert nxt is not None
    return True, f"ADVANCE OK: Phase {frm} → {to} ({nxt['name']})"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print Emperor Time four-phase debug checklist for heal."
    )
    parser.add_argument(
        "--phase",
        type=int,
        choices=(1, 2, 3, 4),
        default=None,
        help="Print only one phase detail (still emits MUST lines)",
    )
    parser.add_argument(
        "--advance",
        nargs=2,
        type=int,
        metavar=("FROM", "TO"),
        help="Validate sequential phase advance (exit 1 on skip)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.advance is not None:
        frm, to = args.advance
        ok, msg = check_advance(frm, to)
        sys.stdout.write(msg + "\n")
        if not ok:
            return 1
        # Also print the destination phase card for convenience
        sys.stdout.write(format_card(focus=to))
        return 0

    try:
        sys.stdout.write(format_card(focus=args.phase))
    except ValueError as exc:
        print(f"debug_phases: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
