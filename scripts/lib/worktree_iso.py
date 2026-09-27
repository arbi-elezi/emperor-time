#!/usr/bin/env python3
"""Worktree isolation checklist for emperor-worktree (Python core).

Leaf adapted from obra/superpowers skills/using-git-worktrees
detect → native/git → ignore-safety → baseline (MIT) — HARD-GATE only.
Emperor Time + emperor-worktree stay the orchestrator; do not announce
the foreign skill name.

Prints WORKTREE / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-blind-create always fails (hard gate when creating without
detect). Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-worktree/isolation-checklist.md"
SOURCE = "obra/superpowers using-git-worktrees → detect/create/setup/baseline"

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "detect",
        "name": "DETECT — Existing isolation",
        "et": "ledger isolation=linked|normal|submodule",
        "success": "Linked worktree (non-submodule) reported, or normal/submodule named",
        "key": "Compare git-dir vs git-common-dir; submodule guard before nesting",
    },
    {
        "n": "2",
        "id": "prefer-native",
        "name": "PREFER-NATIVE — Harness tool or consent",
        "et": "consent / host tool",
        "success": "Native tool chosen, git fallback chosen, stay-in-place, or already isolated",
        "key": "Never fight the harness; honor standing preference; ask once if undeclared",
    },
    {
        "n": "3",
        "id": "dir-safety",
        "name": "DIR-SAFETY — Location + check-ignore",
        "et": ".gitignore + Vow of Evidence",
        "success": "Location chosen; git check-ignore passes (or ignore committed)",
        "key": "Preference > .worktrees > worktrees > default .worktrees; MUST verify ignore",
    },
    {
        "n": "4",
        "id": "create-enter",
        "name": "CREATE-ENTER — Isolated workspace",
        "et": "scripts/emperor worktree <id>",
        "success": "Inside target path on branch (or honest sandbox fallback in place)",
        "key": "Native first; else git worktree add; permission fail → work in place",
    },
    {
        "n": "5",
        "id": "setup-baseline",
        "name": "SETUP-BASELINE — Deps + green suite",
        "et": "BUILD entry / scientific-method",
        "success": "Deps installed as needed; suite green quoted or failures escalated",
        "key": "Dirty baseline makes later failures ambiguous; do not silent-BUILD",
    },
]


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "WORKTREE checklist=yes",
        f"WORKTREE leaf={LEAF}",
        f"WORKTREE source={SOURCE}",
        "WORKTREE iron=NO_MUTATE_WITHOUT_ISOLATION_DETECT",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..5, got {focus}")
        selected = [s]
        lines.append(f"WORKTREE focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Complete each isolation step before the next. Detect before "
        "create. Verify check-ignore before git worktree add. Prove baseline "
        f"before BUILD. Open {LEAF} and run scripts/emperor iso to reprint "
        "this card."
    )
    lines.append(
        "MUST-NOT: load whole using-git-worktrees; nest worktrees; create under "
        "unignored dirs; skip baseline; announce a foreign master router. "
        "ET + emperor-worktree remain the orchestrator."
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


def reject_blind_create() -> str:
    return (
        "REJECT BLIND-CREATE: HARD-GATE — no git worktree add / native create "
        "before isolation checklist Step 1 detect. "
        f"Open {LEAF}; run scripts/emperor iso. "
        "Detect linked vs normal vs submodule first.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print Emperor Time worktree isolation checklist."
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
        "--reject-blind-create",
        action="store_true",
        help="Hard-gate: refuse creating without detect (exit 1)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_blind_create:
        sys.stdout.write(reject_blind_create())
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
        print(f"iso: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
