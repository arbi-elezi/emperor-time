#!/usr/bin/env python3
"""Executing-plans checklist for emperor-build (Python core).

Leaf adapted from obra/superpowers skills/executing-plans
Continuous execution + Four stops + Rulings not stalls + Task Loop +
Completion contract (MIT) — HARD-GATE only.
Emperor Time + emperor-build stay the orchestrator; do not announce
the foreign skill name.

Prints EXECUTE / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-checkin always fails (hard gate when pausing between tasks
for permission theater). Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-build/executing-plans-checklist.md"
SOURCE = (
    "obra/superpowers executing-plans → "
    "Continuous execution / Four stops / Rulings not stalls / "
    "Task Loop / Completion contract"
)

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "setup",
        "name": "SETUP — Worktree, ledger, plan, TDD, pre-flight",
        "et": "emperor-worktree iso + ledger + tdd",
        "success": "Isolated workspace; ledger on disk; plan+spec read; TDD loaded; pre-flight rows ledgered",
        "key": "No implement on main without consent; ledger survives compaction",
    },
    {
        "n": "2",
        "id": "task",
        "name": "TASK — Brief + BASE; read the brief",
        "et": "emperor-build current work-order task",
        "success": "Brief read (exact values); BASE set; task marked in progress",
        "key": "Memory of setup is a summary — read the brief every task",
    },
    {
        "n": "3",
        "id": "work",
        "name": "WORK — TDD steps; compare every Expected",
        "et": "emperor-tdd + emperor-heal",
        "success": "Failing probe watched; every Expected compared to real output",
        "key": "Code wrong → heal; never symptom-patch to match Expected",
    },
    {
        "n": "4",
        "id": "rule",
        "name": "RULE — Ledger rulings; do not stall",
        "et": "ledger Ruling lines",
        "success": "Every plan conflict has Ruling: what — why — cost if wrong",
        "key": "Unledgered deviation is a decision made in secret",
    },
    {
        "n": "5",
        "id": "complete",
        "name": "COMPLETE — Contract + task-done line; next task",
        "et": "emperor-verify evidence",
        "success": "Contract met with quoted evidence; ledger task-done; continue without check-in",
        "key": "Missing contract item = task not complete; no permission theater",
    },
    {
        "n": "6",
        "id": "final",
        "name": "FINAL — Whole-branch review then finish menu",
        "et": "emperor-verify review + emperor-forge finish",
        "success": "Review done; Critical/Important fixed RED→GREEN; rulings listed; finish menu presented",
        "key": "Do not assume PR; minors deferred; no skip of whole-branch review",
    },
]


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "EXECUTE checklist=yes",
        f"EXECUTE leaf={LEAF}",
        f"EXECUTE source={SOURCE}",
        "EXECUTE iron=NO_CHECKIN_THEATER_FOUR_STOPS_ONLY",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..6, got {focus}")
        selected = [s]
        lines.append(f"EXECUTE focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Setup once (iso + ledger + plan/spec + TDD + pre-flight). "
        "Per task: read brief, work TDD steps, compare Expected, ledger "
        "rulings, meet completion contract. Between tasks: no check-in "
        "theater. Stop only for the four stops (destructive, security, "
        "out-of-worktree side effect, plan unworkable). After all tasks: "
        f"whole-branch review then emperor finish. Open {LEAF} and run "
        "scripts/emperor execute to reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole executing-plans or subagent-driven-development; "
        "pause between tasks for 'should I continue?'; deviate from the "
        "plan without a ledgered Ruling; claim task complete without the "
        "completion contract; skip whole-branch review. "
        "ET + emperor-build remain the orchestrator."
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


def reject_checkin() -> str:
    return (
        "REJECT CHECKIN: HARD-GATE — no pause-between-tasks permission "
        "theater after inline execution was chosen. "
        f"Open {LEAF}; run scripts/emperor execute. "
        "Only the four stops halt you: destructive, security, "
        "out-of-worktree side effect, or plan unworkable. "
        "Ledger rulings and continue.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time executing-plans / execute checklist "
            "for emperor-build."
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
        "--reject-checkin",
        action="store_true",
        help="Hard-gate: refuse check-in theater between tasks (exit 1)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_checkin:
        sys.stdout.write(reject_checkin())
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
        print(f"execute: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
