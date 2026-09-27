#!/usr/bin/env python3
"""Receive-review checklist for emperor-verify (Python core).

Leaf adapted from obra/superpowers skills/receiving-code-review
The Response Pattern + Forbidden Responses + When To Push Back (MIT) — HARD-GATE only.
Emperor Time + emperor-verify stay the orchestrator; do not announce
the foreign skill name.

Prints RECEIVE / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-blind-implement always fails (hard gate when implementing
review feedback before verify/evaluate). Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-verify/receive-review-checklist.md"
SOURCE = (
    "obra/superpowers receiving-code-review → "
    "The Response Pattern / Forbidden Responses / When To Push Back"
)

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "read",
        "name": "READ — Complete feedback without reacting",
        "et": "emperor-verify / ledger receive:read",
        "success": "Every review item read end-to-end; item count ledgered",
        "key": "No coding mid-read; no performative agreement",
    },
    {
        "n": "2",
        "id": "understand",
        "name": "UNDERSTAND — Restate or ask",
        "et": "G1 restatement / clarifying questions",
        "success": "Each item restated in own words OR clarifying ask; unclear items block implement",
        "key": "Partial understanding of a multi-item batch = wrong implementation",
    },
    {
        "n": "3",
        "id": "verify",
        "name": "VERIFY — Check against codebase reality",
        "et": "Vow of Evidence / quoted paths or commands",
        "success": "At least one quoted path, test, or command confirms feedback against THIS tree",
        "key": "Memory is rumor; verify on disk before evaluate",
    },
    {
        "n": "4",
        "id": "evaluate",
        "name": "EVALUATE — Sound for THIS codebase?",
        "et": "Judgment claim-audit",
        "success": "Correctness / breakage / missing context / YAGNI / stack fit decided per item",
        "key": "Wrong or unverifiable → prepare pushback; do not silent-implement",
    },
    {
        "n": "5",
        "id": "respond",
        "name": "RESPOND — Technical acknowledgment or pushback",
        "et": "hetero-critique ACT / pushback with evidence",
        "success": "Technical restatement, ask, or evidenced pushback (no performative praise)",
        "key": "Forbidden: You're absolutely right / Great point / implement-now before verify",
    },
    {
        "n": "6",
        "id": "implement",
        "name": "IMPLEMENT — One item at a time, test each",
        "et": "emperor-build + tdd + evidence",
        "success": "Only verified items; blocking→simple→complex; each fix tested",
        "key": "No batch blind apply; unclear items still open = STOP",
    },
]


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "RECEIVE checklist=yes",
        f"RECEIVE leaf={LEAF}",
        f"RECEIVE source={SOURCE}",
        "RECEIVE iron=NO_IMPLEMENT_WITHOUT_VERIFYING_REVIEW_FEEDBACK",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..6, got {focus}")
        selected = [s]
        lines.append(f"RECEIVE focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Complete each receive step before the next. Read fully. "
        "Restate or ask. Verify against this codebase. Evaluate soundness. "
        "Respond technically (or push back with evidence). Only then "
        f"implement one item at a time with tests. Open {LEAF} and run "
        "scripts/emperor receive to reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole receiving-code-review; performative agreement "
        "('You're absolutely right!'); implement before VERIFY/EVALUATE; "
        "batch-apply with unclear items still open. "
        "ET + emperor-verify remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def check_advance(frm: int, to: int) -> tuple[bool, str]:
    """Enforce sequential advancement. Same step or +1 only."""
    if frm < 1 or frm > 6 or to < 1 or to > 6:
        return False, f"ADVANCE FAIL: steps must be 1..6 (from={frm} to={to})"
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


def reject_blind_implement() -> str:
    return (
        "REJECT BLIND-IMPLEMENT: HARD-GATE — no implementing review feedback "
        "without READ→UNDERSTAND→VERIFY→EVALUATE→RESPOND first. "
        f"Open {LEAF}; run scripts/emperor receive. "
        "Verify against this codebase, then implement one tested item at a time.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time receiving-code-review / receive checklist "
            "for emperor-verify."
        )
    )
    parser.add_argument(
        "--step",
        type=int,
        choices=(1, 2, 3, 4, 5, 6),
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
        "--reject-blind-implement",
        action="store_true",
        help="Hard-gate: refuse implement-before-verify (exit 1)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_blind_implement:
        sys.stdout.write(reject_blind_implement())
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
        print(f"receive: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
