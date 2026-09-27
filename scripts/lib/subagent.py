#!/usr/bin/env python3
"""Subagent-driven-development checklist for emperor-build (Python core).

Leaf adapted from obra/superpowers skills/subagent-driven-development
Fresh subagent per task + Task review after each + Fix loop (R of 5) +
Final whole-branch review (MIT) — HARD-GATE only.
Emperor Time + emperor-build stay the orchestrator; do not announce
the foreign skill name.

Prints SUBAGENT / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-skip-review always fails (hard gate when advancing without
a clean or parked task review). Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-build/subagent-driven-checklist.md"
SOURCE = (
    "obra/superpowers subagent-driven-development → "
    "Fresh subagent per task / Task review after each / "
    "Fix loop R of 5 / Final whole-branch review"
)

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "setup",
        "name": "SETUP — When-to-use, worktree, ledger, plan, pre-flight",
        "et": "emperor-worktree iso + ledger + When-to-use gate",
        "success": "Subagent path chosen (not inline); workspace+ledger ready; plan/spec read; pre-flight rows ledgered",
        "key": "Tight coupling or no subagent tool → emperor execute instead; no Task 1 in controller",
    },
    {
        "n": "2",
        "id": "dispatch",
        "name": "DISPATCH — Fresh implementer; brief as a file",
        "et": "harness subagent + .emperor/runs brief/report",
        "success": "BASE recorded; brief file path in dispatch; report path set; agent id recorded; no parallel implementers",
        "key": "No session-history paste; implementer never spawns reviewers",
    },
    {
        "n": "3",
        "id": "report",
        "name": "REPORT — Status triage",
        "et": "read report file statuses",
        "success": "DONE/CONCERNS/NEEDS_CONTEXT/BLOCKED handled; no unchanged retry on BLOCKED",
        "key": "Escalations change context, model, split, or ledgered ruling — never ignore",
    },
    {
        "n": "4",
        "id": "review",
        "name": "REVIEW — Spec + quality; never skip",
        "et": "emperor-verify review + review-pack",
        "success": "Diff file BASE..HEAD; both verdicts present; no pre-judge; ⚠️ items resolved by controller",
        "key": "Implementer self-review never replaces task review",
    },
    {
        "n": "5",
        "id": "fix",
        "name": "FIX — Loop R of 5; controller never fixes",
        "et": "resume/fresh implementer + scoped re-review",
        "success": "Rounds ledgered; minors deferred; breaker adjudicates only at R=5 with rulings",
        "key": "Controller does not patch findings; parallel implementers forbidden",
    },
    {
        "n": "6",
        "id": "complete",
        "name": "COMPLETE — Task-done, next task, final review, finish",
        "et": "emperor-verify review + emperor-forge finish",
        "success": "Complete line only when clean or parked-at-cap; final review + ONE fix wave; rulings listed; finish menu",
        "key": "No check-in theater; do not assume PR; no skip of whole-branch review",
    },
]


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "SUBAGENT checklist=yes",
        f"SUBAGENT leaf={LEAF}",
        f"SUBAGENT source={SOURCE}",
        "SUBAGENT iron=FRESH_SUBAGENT_PER_TASK_REVIEW_AFTER_EACH",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..6, got {focus}")
        selected = [s]
        lines.append(f"SUBAGENT focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Confirm When-to-use (independent tasks + subagent tool; "
        "else emperor execute). Setup once (iso + ledger + plan/spec + "
        "pre-flight). Per task: extract brief file, record BASE, dispatch "
        "fresh implementer, triage report, task-review (spec+quality) with "
        "diff file, fix loop R of 5 if needed, ledger complete only when "
        "clean or parked-at-cap. Between tasks: no check-in theater. After "
        f"all tasks: whole-branch review then emperor finish. Open {LEAF} "
        "and run scripts/emperor subagent to reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole subagent-driven-development or its prompt "
        "templates as always-on; implement the next task in the controller; "
        "skip task review; paste session history into dispatches; dispatch "
        "parallel implementers; fix findings in the controller; pause "
        "between tasks for 'should I continue?'; claim task complete with "
        "open Critical/Important unparked. "
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


def reject_skip_review() -> str:
    return (
        "REJECT SKIP-REVIEW: HARD-GATE — no next-task without a clean "
        "task review (spec + quality) or parked-with-ruling at the fix "
        f"cap. Open {LEAF}; run scripts/emperor subagent. "
        "Implementer self-review never replaces the task review. "
        "Fresh subagent per task; controller coordinates only.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time subagent-driven-development / subagent "
            "checklist for emperor-build."
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
        "--reject-skip-review",
        action="store_true",
        help="Hard-gate: refuse skipping per-task review (exit 1)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_skip_review:
        sys.stdout.write(reject_skip_review())
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
        print(f"subagent: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
