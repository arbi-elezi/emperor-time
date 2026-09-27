#!/usr/bin/env python3
"""Request-review checklist for emperor-verify (Python core).

Leaf adapted from obra/superpowers skills/requesting-code-review
When / How / Act-on-feedback (MIT) — HARD-GATE only.
Emperor Time + emperor-verify stay the orchestrator; do not announce
the foreign skill name.

Prints REVIEW / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-self-review always fails (hard gate when author skips
dispatch to self-review the diff). Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-verify/request-review-checklist.md"
SOURCE = (
    "obra/superpowers requesting-code-review → When / How / Act-on-feedback"
)

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "when",
        "name": "WHEN — Confirm mandatory trigger",
        "et": "G4 / finish / major feature / subagent task done",
        "success": "Trigger named: task-done | major-feature | before-merge | stuck | pre-refactor",
        "key": "Mandatory after each subagent task, major feature, before merge to main",
    },
    {
        "n": "2",
        "id": "shas",
        "name": "SHAS — Resolve BASE and HEAD",
        "et": "git merge-base / rev-parse; ledger SHAs",
        "success": "BASE_SHA and HEAD_SHA resolved and ledgered (merge-base origin/main HEAD preferred)",
        "key": "Never hand the reviewer session history; SHAs bound the product",
    },
    {
        "n": "3",
        "id": "pack",
        "name": "PACK — Emit isolated review pack",
        "et": "scripts/emperor review-pack <task-dir> <base> <head>",
        "success": "review-pack/ has meta.md + diff + criteria; no author CoT",
        "key": "Isolated pack only — SHAs + diff + acceptance criteria",
    },
    {
        "n": "4",
        "id": "dispatch",
        "name": "DISPATCH — Fresh reviewer context",
        "et": "hetero-critique / Steal Chain worker / fresh subagent",
        "success": "Reviewer dispatched with DESCRIPTION + PLAN + SHAs; builder does not write verdict",
        "key": "Crafted context only; never session history; read-only reviewer",
    },
    {
        "n": "5",
        "id": "act",
        "name": "ACT — Severity-gated response",
        "et": "claim ledger + G4 ruling",
        "success": "Critical fixed; Important fixed before proceed; Minor noted; pushback only with evidence",
        "key": "No proceed with unfixed Critical/Important; verify critic findings before acting",
    },
]


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "REVIEW checklist=yes",
        f"REVIEW leaf={LEAF}",
        f"REVIEW source={SOURCE}",
        "REVIEW iron=NO_PROCEED_WITHOUT_REQUESTED_REVIEW",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..5, got {focus}")
        selected = [s]
        lines.append(f"REVIEW focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Complete each request-review step before the next. Confirm "
        "WHEN before SHAs. Emit pack before dispatch. Dispatch a fresh "
        "reviewer — do not self-review the diff inline. Act on Critical and "
        f"Important before merge/proceed. Open {LEAF} and run "
        "scripts/emperor review to reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole requesting-code-review; skip review because "
        "'it is simple'; ignore Critical; proceed with unfixed Important; "
        "hand the reviewer session history; announce a foreign master "
        "router. ET + emperor-verify remain the orchestrator."
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


def reject_self_review() -> str:
    return (
        "REJECT SELF-REVIEW: HARD-GATE — no author self-review of the diff "
        "in place of dispatching a fresh reviewer. "
        f"Open {LEAF}; run scripts/emperor review. "
        "Emit the pack (Step 3), dispatch (Step 4), then act (Step 5).\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print Emperor Time request-review checklist."
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
        "--reject-self-review",
        action="store_true",
        help="Hard-gate: refuse author self-review instead of dispatch (exit 1)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_self_review:
        sys.stdout.write(reject_self_review())
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
        print(f"review: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
