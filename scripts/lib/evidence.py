#!/usr/bin/env python3
"""Verification-before-completion checklist for emperor-verify (Python core).

Leaf adapted from obra/superpowers skills/verification-before-completion
The Iron Law + The Gate Function (MIT) — HARD-GATE only.
Emperor Time + emperor-verify stay the orchestrator; do not announce
the foreign skill name.

Prints EVIDENCE / STEP / MUST lines. Optional --step and --advance enforce
order. --reject-unverified always fails (hard gate when claiming completion
without fresh verification evidence). Does not mutate the tree.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

LEAF = "skills/emperor-verify/verification-checklist.md"
SOURCE = (
    "obra/superpowers verification-before-completion → "
    "The Iron Law / The Gate Function"
)

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "identify",
        "name": "IDENTIFY — Name the proving command",
        "et": "G4 / claim ledger / Vow of Evidence",
        "success": "One concrete command (or gate) that would prove the claim named",
        "key": "No vague 'tests' — exact argv / scripts/eval.sh / gate g4",
    },
    {
        "n": "2",
        "id": "run",
        "name": "RUN — Execute the FULL command fresh",
        "et": "this-message experiment; no prior-run reuse",
        "success": "Command executed in this turn; exit code captured",
        "key": "MANDATORY; previous green is rumor; agent 'success' is rumor",
    },
    {
        "n": "3",
        "id": "read",
        "name": "READ — Full output, exit, failure count",
        "et": "quoted evidence row",
        "success": "Exit code + failure count (or PASS tail) read end-to-end",
        "key": "No skimming; partial check proves nothing",
    },
    {
        "n": "4",
        "id": "verify",
        "name": "VERIFY — Output confirms the claim?",
        "et": "claim status VERIFIED or honest failure",
        "success": "YES with matching output OR NO with actual status stated",
        "key": "If NO: state actual status with evidence; do not claim",
    },
    {
        "n": "5",
        "id": "claim",
        "name": "CLAIM — Assert only with quoted evidence",
        "et": "ledger VERIFIED row + G4 / deliver",
        "success": "Claim text includes quoted command output or two independent sources",
        "key": "Skip any prior step = lying, not verifying",
    },
]


def _step_by_n(n: int) -> dict[str, str] | None:
    for s in STEPS:
        if int(s["n"]) == n:
            return s
    return None


def format_card(*, focus: int | None = None) -> str:
    lines = [
        "EVIDENCE checklist=yes",
        f"EVIDENCE leaf={LEAF}",
        f"EVIDENCE source={SOURCE}",
        "EVIDENCE iron=NO_COMPLETION_CLAIMS_WITHOUT_FRESH_VERIFICATION_EVIDENCE",
    ]
    selected = STEPS
    if focus is not None:
        s = _step_by_n(focus)
        if s is None:
            raise ValueError(f"step must be 1..5, got {focus}")
        selected = [s]
        lines.append(f"EVIDENCE focus={focus}")

    for s in selected:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} "
            f"et={s['et']}"
        )
        lines.append(f"STEP {s['n']} key={s['key']}")
        lines.append(f"STEP {s['n']} success={s['success']}")

    lines.append("")
    lines.append(
        "MUST: Complete each evidence step before the next. Identify the "
        "proving command before running. Run fresh in this turn. Read the "
        "full output. Verify the claim matches. Only then claim — with "
        f"quoted evidence. Open {LEAF} and run scripts/emperor evidence to "
        "reprint this card."
    )
    lines.append(
        "MUST-NOT: load whole verification-before-completion; claim with "
        "'should'/'probably'/'seems'; reuse a prior run; trust agent "
        "success reports; express satisfaction before Step 4 YES. "
        "ET + emperor-verify remain the orchestrator."
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


def reject_unverified() -> str:
    return (
        "REJECT UNVERIFIED: HARD-GATE — no completion / pass / fixed / done "
        "claim without fresh verification evidence from Steps 1–4. "
        f"Open {LEAF}; run scripts/emperor evidence. "
        "Identify → run → read → verify, then claim with a quote.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time verification-before-completion / evidence "
            "checklist for emperor-verify."
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
        "--reject-unverified",
        action="store_true",
        help="Hard-gate: refuse completion claim without fresh evidence (exit 1)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_unverified:
        sys.stdout.write(reject_unverified())
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
        print(f"evidence: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
