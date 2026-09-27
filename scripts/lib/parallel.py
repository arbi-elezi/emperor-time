#!/usr/bin/env python3
"""Parallel-dispatch checklist for emperor-dispatch (Python core).

Leaf adapted from obra/superpowers skills/dispatching-parallel-agents
Identify Independent Domains + Focused Agent Tasks + Parallel Dispatch +
Review and Integrate (MIT) — HARD-GATE only.
Emperor Time + emperor-dispatch stay the orchestrator; do not announce
the foreign skill name.

Prints PARALLEL / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-shared-scope always fails (hard gate when launching parallel
agents whose scopes share writable files or related root causes). Does not
mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-dispatch/parallel-dispatch-checklist.md"
SOURCE = (
    "obra/superpowers dispatching-parallel-agents → "
    "Identify Independent Domains / Focused Agent Tasks / "
    "Parallel Dispatch / Review and Integrate"
)

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "gate",
        "name": "GATE — When-to-use vs sequential / related",
        "et": "ledger When-to-use; steal-chain consent if external CLIs",
        "success": "2+ independent domains confirmed; related/shared-state path rejected; path chosen (parallel vs sequential vs single)",
        "key": "Related failures or shared writable state → do NOT parallelize; investigate together or use emperor subagent sequentially",
    },
    {
        "n": "2",
        "id": "domains",
        "name": "DOMAINS — Group by independent problem domain",
        "et": "ledger domain table (file/subsystem → root-cause guess)",
        "success": "Each domain has disjoint writable SCOPE; read-only shared context listed; no overlapping edit targets",
        "key": "Fixing A must not be expected to fix B; scopes checked before launch, not after",
    },
    {
        "n": "3",
        "id": "briefs",
        "name": "BRIEFS — Focused self-contained agent prompts",
        "et": ".emperor/runs/<task>/<agent>/prompt.md per domain",
        "success": "One objective per agent; specific scope; constraints; expected output; no session-history paste",
        "key": "Too broad / no context / no constraints / vague output = reject and rewrite before dispatch",
    },
    {
        "n": "4",
        "id": "dispatch",
        "name": "DISPATCH — Issue all agents in one response",
        "et": "harness subagents same turn and/or steal-chain dispatch.md",
        "success": "All independent agents launched concurrently; BASE recorded; agent ids ledgered; no staggered sequential launch pretending to be parallel",
        "key": "Multiple dispatch calls in one response = parallel; one per response = sequential",
    },
    {
        "n": "5",
        "id": "integrate",
        "name": "INTEGRATE — Review summaries, conflicts, full suite",
        "et": "emperor-verify + quarantine + gate g4; full suite on this tree",
        "success": "Each summary read; no conflicting edits; full suite green; spot-check for systematic agent errors",
        "key": "Output stays CONJECTURE until Judgment; beautiful-looking diffs still quarantine",
    },
    {
        "n": "6",
        "id": "complete",
        "name": "COMPLETE — Ledger, next, or finish",
        "et": "ledger + emperor finish when branch work done",
        "success": "Domains closed or parked-with-ruling; conflicts resolved; finish menu only after green suite",
        "key": "Do not claim done with open domain conflicts or red suite",
    },
]


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "PARALLEL checklist=yes",
        f"PARALLEL leaf={LEAF}",
        f"PARALLEL source={SOURCE}",
        "PARALLEL iron=ONE_AGENT_PER_INDEPENDENT_DOMAIN_NO_SHARED_WRITABLE",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..6, got {focus}")
        selected = [s]
        lines.append(f"PARALLEL focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Confirm When-to-use (2+ independent domains; "
        "else sequential emperor subagent / emperor execute / single agent). "
        "Group failures by domain; check writable SCOPE lists are disjoint. "
        "Write focused self-contained briefs (one objective, constraints, "
        "expected output). Dispatch all agents in the same response for "
        "true parallelism. Review summaries, check conflicts, run full suite, "
        f"then Judgment. Open {LEAF} and run scripts/emperor parallel to "
        "reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole dispatching-parallel-agents as always-on; "
        "parallelize related failures or shared writable scopes; paste "
        "session history into briefs; launch one agent per turn and call it "
        "parallel; merge agent output without quarantine/Judgment; claim "
        "done with conflicting edits or red suite. "
        "ET + emperor-dispatch remain the orchestrator. "
        "Sequential plan tasks with one implementer at a time stay "
        "emperor subagent (no parallel implementers on the same plan)."
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


def reject_shared_scope() -> str:
    return (
        "REJECT SHARED-SCOPE: HARD-GATE — do not dispatch parallel agents "
        "whose writable SCOPE lists share a file, or whose failures share a "
        "root cause. Parallelize only independent domains. Related work: "
        "investigate together or run emperor subagent sequentially. "
        f"Open {LEAF}; run scripts/emperor parallel. "
        "Disjoint writable scopes checked before launch, not after.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time dispatching-parallel-agents / parallel "
            "checklist for emperor-dispatch."
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
        "--reject-shared-scope",
        action="store_true",
        help="Hard-gate: refuse parallel with shared writable scope (exit 1)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_shared_scope:
        sys.stdout.write(reject_shared_scope())
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
        print(f"parallel: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
