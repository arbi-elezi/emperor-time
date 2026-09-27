#!/usr/bin/env python3
"""Authoring iron-law / skill RGR checklist for Chain Jail (Python core).

Leaf adapted from obra/superpowers skills/writing-skills
"The Iron Law (Same as TDD)" + RED-GREEN-REFACTOR for Skills (MIT) —
HARD-GATE only. Emperor Time + Chain Jail authoring.md stay the
orchestrator; do not announce the foreign skill name.

Prints AUTHOR / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-untested always fails (hard gate when jumping to skill
prose before a failing baseline was observed). Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "chains/chain-jail/authoring-checklist.md"
SOURCE = "obra/superpowers writing-skills → The Iron Law (Same as TDD) / skill RGR"

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "red",
        "name": "RED — Design failing baseline",
        "et": "claim HYPOTHESIS / pressure scenario",
        "success": "Probe written; predicted FAIL signal ledgered before run",
        "key": "One pressure scenario or structural probe; name the expected violation",
    },
    {
        "n": "2",
        "id": "verify-red",
        "name": "Verify RED — Watch baseline FAIL",
        "et": "Vow of Evidence / quote FAIL tail",
        "success": "FAIL / violation quoted without the new skill (or with old text)",
        "key": "MANDATORY; capture rationalizations; if pass → fix probe",
    },
    {
        "n": "3",
        "id": "green",
        "name": "GREEN — Minimal skill addressing those violations",
        "et": "authoring.md Steps 1–4 / Zetsu stage",
        "success": "Smallest skill text that would make that baseline pass",
        "key": "Description FIRST; procedure body; provenance; no riders",
    },
    {
        "n": "4",
        "id": "verify-green",
        "name": "Verify GREEN — Watch it PASS",
        "et": "pre-trial evidence",
        "success": "Compliance quoted with skill present; still hand to trial",
        "key": "MANDATORY; one green ≠ registered",
    },
    {
        "n": "5",
        "id": "refactor",
        "name": "REFACTOR — Close loopholes while green",
        "et": "trial-and-register.md",
        "success": "Loopholes plugged; still green; no new capabilities",
        "key": "After green only; re-run; then hand to trial",
    },
]


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "AUTHOR checklist=yes",
        f"AUTHOR leaf={LEAF}",
        f"AUTHOR source={SOURCE}",
        "AUTHOR iron=NO_SKILL_WITHOUT_FAILING_BASELINE_FIRST",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..5, got {focus}")
        selected = [s]
        lines.append(f"AUTHOR focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Complete each skill-RGR step before the next. No skill body "
        "before Step 2 FAIL was observed and quoted. Delete skill prose "
        f"written earlier. Open {LEAF} and run scripts/emperor author to "
        "reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole writing-skills; skip verify-red; keep "
        "pre-baseline drafts as reference; bind before trial-and-register. "
        "ET + Chain Jail authoring remain the orchestrator."
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


def reject_untested() -> str:
    return (
        "REJECT UNTESTED: HARD-GATE — no skill body before authoring "
        "checklist Step 2 FAIL was observed and quoted. "
        f"Open {LEAF}; run scripts/emperor author. "
        "Delete skill prose written earlier; replay RED → verify-red first.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time authoring iron-law / skill RGR checklist "
            "for Chain Jail."
        )
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
        "--reject-untested",
        action="store_true",
        help="Hard-gate: refuse skill write before failing baseline (exit 1)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_untested:
        sys.stdout.write(reject_untested())
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
        print(f"author: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
