#!/usr/bin/env python3
"""Grill / brainstorm checklist for emperor require-design (Python core).

Leaf adapted from obra/superpowers skills/brainstorming
"HARD-GATE" (MIT) — questions before code / reject jumping to impl.
Emperor Time + require-design stay the orchestrator; do not announce
the foreign skill name.

Prints GRILL / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-impl always fails (hard gate when jumping to code).
Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-require-design/grill-checklist.md"
SOURCE = "obra/superpowers brainstorming → HARD-GATE"

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
        "MUST: Complete each grill step before the next. No product code, "
        "scaffolding, or BUILD before Step 5 approval. "
        f"Open {LEAF} and run scripts/emperor grill to reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole brainstorming; jump to impl; turn idea-approval "
        "into code permission; announce a foreign master router. "
        "ET + require-design remain the orchestrator."
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


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print Emperor Time grill/brainstorm checklist for require-design."
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
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_impl:
        sys.stdout.write(reject_impl())
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
        print(f"grill: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
