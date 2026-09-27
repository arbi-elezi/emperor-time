#!/usr/bin/env python3
"""Pressure/academic HARD-GATE card for emperor-heal (Python core).

Leaf adapted from obra/superpowers skills/systematic-debugging
test-pressure-1.md / test-pressure-2.md / test-pressure-3.md /
test-academic.md (MIT) — Resist process-skip under emergency, sunk-cost,
and authority pressure; academic four-phase self-check. Emperor Time +
Holy Chain stay the orchestrator; do not announce the foreign skill name.
Does not vendor whole systematic-debugging. pressure-academic is this
Chain Jail leaf only.

Prints PRESSURE / CASE / MUST / ACADEMIC lines.
--reject-shortcut and --reject-compromise always fail (HARD-GATE helpers).
Optional --check-academic TEXT fails when four-phase / root-cause-first
signals are missing.
Companion when time / money / exhaustion / seniority tempt skipping heal
phases (after find-polluter; before symptom fixes).
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "skills/emperor-heal/pressure-academic.md"
SOURCE = (
    "obra/superpowers systematic-debugging → "
    "test-pressure-*.md + test-academic.md "
    "(resist skip under pressure / academic four-phase check)"
)
IRON = "NO_SKIP_UNDER_PRESSURE"

CASES: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "emergency",
        "name": "Emergency production / revenue pressure",
        "need": (
            "Follow four phases even when a 2-minute retry looks cheaper; "
            "quick-fix-now is a symptom patch"
        ),
    },
    {
        "n": "2",
        "id": "sunk_cost",
        "name": "Sunk cost + exhaustion",
        "need": (
            "Delete arbitrary sleep / timeout guesses; return to Phase 1; "
            "good-enough TODO is not a root cause"
        ),
    },
    {
        "n": "3",
        "id": "authority",
        "name": "Authority + social pressure",
        "need": (
            "Insist on tracing the failing layer before shipping the "
            "senior's pattern; trust without evidence is skip"
        ),
    },
]

ACADEMIC: list[dict[str, str]] = [
    {
        "n": "1",
        "q": "four_phases",
        "a": "investigate → pattern-analyze → hypothesize → implement",
    },
    {
        "n": "2",
        "q": "before_any_fix",
        "a": "complete Phase 1 root-cause investigation (no fix yet)",
    },
    {
        "n": "3",
        "q": "first_hypothesis_fails",
        "a": "STOP and re-analyze; form a new single hypothesis",
    },
    {
        "n": "4",
        "q": "multiple_fixes",
        "a": "never fix multiple things at once (shotgun = fail)",
    },
    {
        "n": "5",
        "q": "do_not_understand",
        "a": "gather more evidence; do not guess",
    },
    {
        "n": "6",
        "q": "skip_for_simple",
        "a": "never acceptable — simple bugs still have root causes",
    },
]

# Strong tokens for --check-academic
PHASE_TOKENS = (
    "investigate",
    "investigation",
    "pattern",
    "hypothesis",
    "hypothesize",
    "implement",
    "implementation",
    "four phase",
    "four phases",
    "phase 1",
)
ROOT_TOKENS = (
    "root cause",
    "before",
    "no fix",
    "without root",
    "phase 1",
)
STOP_TOKENS = (
    "stop",
    "re-analyze",
    "reanalyze",
    "new hypothesis",
    "single hypothesis",
)
NEVER_SKIP_TOKENS = (
    "never skip",
    "not acceptable",
    "never acceptable",
    "do not skip",
    "don't skip",
    "no skip",
)


def format_card() -> str:
    lines = [
        "PRESSURE checklist=yes",
        f"PRESSURE leaf={LEAF}",
        f"PRESSURE source={SOURCE}",
        f"PRESSURE iron={IRON}",
        "PRESSURE companion=scripts/emperor heal (four phases — never skip)",
        "PRESSURE companion=scripts/emperor trace (source fix under pressure)",
        "PRESSURE companion=scripts/emperor wait (sunk-cost sleep is a different leaf)",
        "PRESSURE companion=scripts/emperor polluter (shared-state is a different leaf)",
    ]
    for case in CASES:
        lines.append(
            f"CASE {case['n']} id={case['id']} name={case['name']} "
            f"need={case['need']}"
        )
    lines.append(
        "CASE rule=choose_process — under pressure the only valid choice is "
        "follow four phases (Option A); B/C shortcuts and compromises fail"
    )
    lines.append(
        "CASE rule=no_emergency_exception — revenue / manager urgency does "
        "not waive Phase 1"
    )
    lines.append(
        "CASE rule=no_sunk_cost — hours of sleep/timeout thrash are deleted, "
        "not kept as 'good enough'"
    )
    lines.append(
        "CASE rule=no_authority_skip — seniority / call length does not "
        "replace tracing the failing layer"
    )
    for item in ACADEMIC:
        lines.append(
            f"ACADEMIC {item['n']} q={item['q']} a={item['a']}"
        )
    lines.append("")
    lines.append(
        "MUST: When emergency, sunk-cost, or authority pressure tempts a "
        "shortcut, refuse Options B/C. Stay on four phases. Open "
        f"{LEAF}. Run scripts/emperor pressure to reprint this card. "
        "Companions: scripts/emperor heal, scripts/emperor trace."
    )
    lines.append(
        "MUST-NOT: ship a quick retry / arbitrary sleep / senior's untraced "
        "pattern because of time, money, exhaustion, or social pressure; "
        "claim 'pragmatic compromise' while skipping Phase 1; load whole "
        "systematic-debugging. ET + Holy Chain remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_shortcut() -> str:
    return (
        "REJECT SHORTCUT: HARD-GATE — do not skip four phases for a quick "
        "fix, timeout, or go-along under emergency / exhaustion / "
        f"authority pressure. Iron={IRON}. Open {LEAF}. "
        "Re-run scripts/emperor pressure --check-academic \"...\".\n"
    )


def reject_compromise() -> str:
    return (
        "REJECT COMPROMISE: HARD-GATE — 'minimal investigation then shortcut' "
        "is still a skip. Complete Phase 1 root-cause investigation before "
        f"any fix. Iron={IRON}. Open {LEAF}. Run scripts/emperor heal, then "
        "scripts/emperor pressure.\n"
    )


def check_academic(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when academic/process signals appear."""
    raw = text or ""
    low = raw.lower()
    found: set[str] = set()

    phase_hits = [t for t in PHASE_TOKENS if t in low]
    if phase_hits:
        found.add("phases")
    if any(t in low for t in ROOT_TOKENS):
        found.add("root-first")
    if any(t in low for t in STOP_TOKENS):
        found.add("stop-reanalyze")
    if any(t in low for t in NEVER_SKIP_TOKENS):
        found.add("never-skip")
    # Option A / follow process choice
    if re.search(r"\boption\s*a\b", low) or "follow" in low and (
        "phase" in low or "process" in low or "systematic" in low
    ):
        found.add("choose-process")
    if "four" in low and "phase" in low:
        found.add("phases")

    # Need phases + root-first, plus one of stop / never-skip / choose-process
    has_core = "phases" in found and "root-first" in found
    has_resist = bool(found & {"stop-reanalyze", "never-skip", "choose-process"})
    if has_core and has_resist:
        shown = ", ".join(sorted(found))
        return (
            True,
            f"PRESSURE OK: academic/process signal(s): {shown}\n",
        )
    return (
        False,
        "PRESSURE FAIL: need academic four-phase + root-cause-first signals "
        "(and stop/never-skip/choose-process). "
        f"Iron={IRON}. Open {LEAF}.\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time pressure/academic HARD-GATE card "
            "for emperor-heal (resist skip under pressure)."
        )
    )
    parser.add_argument(
        "--reject-shortcut",
        action="store_true",
        help="Hard-gate: exit 1 when about to take a pressure shortcut",
    )
    parser.add_argument(
        "--reject-compromise",
        action="store_true",
        help="Hard-gate: exit 1 when about to 'compromise' then shortcut",
    )
    parser.add_argument(
        "--check-academic",
        metavar="TEXT",
        default=None,
        help=(
            "Exit 0 if TEXT shows four-phase + root-cause-first "
            "(and stop/never-skip/choose-process); else exit 1"
        ),
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_shortcut:
        sys.stdout.write(reject_shortcut())
        return 1
    if args.reject_compromise:
        sys.stdout.write(reject_compromise())
        return 1
    if args.check_academic is not None:
        ok, msg = check_academic(args.check_academic)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
