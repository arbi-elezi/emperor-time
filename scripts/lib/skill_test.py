#!/usr/bin/env python3
"""Testing-skills HARD-GATE card for Chain Jail authoring (Python core).

Leaf adapted from obra/superpowers skills/writing-skills
testing-skills-with-subagents.md (MIT) — Combined Pressure / Watch Baseline
Fail / Verbatim Rationalizations / Explicit Negation / Stay Green.
Emperor Time + Chain Jail authoring.md stay the orchestrator; do not
announce the foreign skill name.
Does not vendor whole writing-skills. testing-skills is this Chain Jail
leaf only.

Prints SKILLTEST / PRIN / GATE / MUST lines.
--reject-academic-only and --reject-skip-red always fail (HARD-GATE helpers).
Optional --check-pressure-baseline TEXT fails when combined-pressure +
watch-baseline signals are missing.
Companion when pressure-testing a skill after the authoring RGR cycle
(emperor author).
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "chains/chain-jail/testing-skills.md"
SOURCE = (
    "obra/superpowers writing-skills → testing-skills-with-subagents.md "
    "(Combined Pressure / Watch Baseline Fail / Explicit Negation)"
)
IRON = "EVERY_SKILL_FACES_COMBINED_PRESSURE"

PRINCIPLES: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "combined_pressure",
        "name": "Combined pressure (3+)",
        "need": (
            "Pressure scenarios stack three or more pressures "
            "(time + sunk cost + exhaustion / authority / economic); "
            "single-pressure and academic quizzes do not count"
        ),
    },
    {
        "n": "2",
        "id": "watch_baseline",
        "name": "Watch baseline FAIL without skill",
        "need": (
            "Run the scenario WITHOUT the skill first; quote the FAIL / "
            "violation; if you did not watch it fail you do not know what "
            "to prevent"
        ),
    },
    {
        "n": "3",
        "id": "verbatim_rationalizations",
        "name": "Capture rationalizations verbatim",
        "need": (
            "Document exact excuses word-for-word "
            "(\"tests after achieve same goals\"); "
            "\"agent was wrong\" is not a baseline"
        ),
    },
    {
        "n": "4",
        "id": "explicit_negation",
        "name": "Explicit negation per loophole",
        "need": (
            "Each new rationalization gets an explicit counter "
            "(\"Don't keep as reference\" not \"Don't cheat\"); "
            "update rationalization table + red flags"
        ),
    },
    {
        "n": "5",
        "id": "stay_green",
        "name": "Stay green under max pressure",
        "need": (
            "Re-test after each REFACTOR; meta-test clarity; "
            "one green pass ≠ bulletproof; continue until no new "
            "rationalizations under maximum pressure"
        ),
    },
]

PRESSURE_TOKENS = (
    "combined pressure",
    "3+ pressure",
    "three pressure",
    "multiple pressure",
    "time + sunk",
    "sunk cost",
    "exhaustion",
    "authority pressure",
    "pressure scenario",
    "pressure scenarios",
)
BASELINE_TOKENS = (
    "without the skill",
    "without skill",
    "baseline fail",
    "watch it fail",
    "watched it fail",
    "run without",
    "baseline test",
    "red phase",
    "verify red",
)
VERBATIM_TOKENS = (
    "verbatim",
    "word-for-word",
    "word for word",
    "exact rationalization",
    "exact wording",
    "quoted rationalization",
    "document rationalization",
)
NEGATION_TOKENS = (
    "explicit negation",
    "explicit counter",
    "rationalization table",
    "red flag",
    "close loophole",
    "plug the hole",
    "don't keep as reference",
)
STAY_TOKENS = (
    "stay green",
    "re-test",
    "retest",
    "meta-test",
    "meta test",
    "maximum pressure",
    "still complies",
    "bulletproof",
)


def format_card() -> str:
    lines = [
        "SKILLTEST checklist=yes",
        f"SKILLTEST leaf={LEAF}",
        f"SKILLTEST source={SOURCE}",
        f"SKILLTEST iron={IRON}",
        "SKILLTEST companion=scripts/emperor author (skill RGR — failing baseline first)",
        "SKILLTEST companion=chains/chain-jail/authoring-checklist.md",
    ]
    for prin in PRINCIPLES:
        lines.append(
            f"PRIN {prin['n']} id={prin['id']} name={prin['name']} "
            f"need={prin['need']}"
        )
    lines.append(
        "GATE rule=before_deploy — create 3+ combined-pressure scenarios; "
        "run WITHOUT skill and quote FAIL + rationalizations; write minimal "
        "skill; re-run WITH skill; plug each new loophole with explicit "
        "negation; re-verify under max pressure before trial/register"
    )
    lines.append(
        "GATE rule=no_academic_only — \"what does the skill say?\" quizzes "
        "and single-pressure prompts are not skill tests; force A/B/C under "
        "real constraints"
    )
    lines.append("")
    lines.append(
        "MUST: Before deploying or registering a discipline skill, face it "
        f"with combined pressure and watch the baseline fail. Open {LEAF}. "
        "Run scripts/emperor skill-test to reprint this card. Companion: "
        "scripts/emperor author."
    )
    lines.append(
        "MUST-NOT: ship skills tested only academically; skip RED baseline; "
        "summarize failures as \"agent was wrong\"; add vague counters "
        "(\"don't cheat\"); stop after first green; load whole "
        "writing-skills. ET + Chain Jail remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_academic_only() -> str:
    return (
        "REJECT ACADEMIC-ONLY: HARD-GATE — academic quizzes and single-pressure "
        "prompts do not prove a skill holds. Stack 3+ pressures (time + sunk "
        "cost + exhaustion/authority) with concrete A/B/C choices. "
        f"Iron={IRON}. Open {LEAF}. Re-run scripts/emperor "
        "skill-test --check-pressure-baseline \"...\".\n"
    )


def reject_skip_red() -> str:
    return (
        "REJECT SKIP-RED: HARD-GATE — writing the skill before watching a "
        "baseline FAIL reveals what YOU think needs preventing, not what "
        "agents actually do. Run WITHOUT the skill first; quote FAIL + "
        f"rationalizations verbatim. Iron={IRON}. Open {LEAF}.\n"
    )


def check_pressure_baseline(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when combined-pressure + baseline signals appear."""
    raw = text or ""
    low = raw.lower()
    found: set[str] = set()

    if any(t in low for t in PRESSURE_TOKENS):
        found.add("combined-pressure")
    if any(t in low for t in BASELINE_TOKENS):
        found.add("watch-baseline")
    if any(t in low for t in VERBATIM_TOKENS):
        found.add("verbatim")
    if any(t in low for t in NEGATION_TOKENS):
        found.add("explicit-negation")
    if any(t in low for t in STAY_TOKENS):
        found.add("stay-green")
    # Numeric 3+ pressure hint
    if re.search(r"\b3\s*\+\b", low) and "pressure" in low:
        found.add("combined-pressure")
    if "without" in low and "skill" in low and (
        "fail" in low or "baseline" in low or "ran" in low or "run" in low
    ):
        found.add("watch-baseline")

    has_core = "combined-pressure" in found and "watch-baseline" in found
    has_quality = bool(
        found & {"verbatim", "explicit-negation", "stay-green"}
    )
    if has_core and has_quality:
        shown = ", ".join(sorted(found))
        return (
            True,
            f"SKILLTEST OK: pressure-baseline signal(s): {shown}\n",
        )
    return (
        False,
        "SKILLTEST FAIL: need combined-pressure + watch-baseline plus "
        "verbatim / explicit-negation / stay-green. "
        f"Iron={IRON}. Open {LEAF}.\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time testing-skills HARD-GATE card "
            "for Chain Jail authoring (combined pressure / watch baseline)."
        )
    )
    parser.add_argument(
        "--reject-academic-only",
        action="store_true",
        help="Hard-gate: exit 1 when about to ship on academic-only tests",
    )
    parser.add_argument(
        "--reject-skip-red",
        action="store_true",
        help="Hard-gate: exit 1 when writing skill before watching baseline FAIL",
    )
    parser.add_argument(
        "--check-pressure-baseline",
        metavar="TEXT",
        default=None,
        help=(
            "Exit 0 if TEXT has combined-pressure + watch-baseline plus "
            "verbatim/explicit-negation/stay-green; else exit 1"
        ),
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_academic_only:
        sys.stdout.write(reject_academic_only())
        return 1
    if args.reject_skip_red:
        sys.stdout.write(reject_skip_red())
        return 1
    if args.check_pressure_baseline is not None:
        ok, msg = check_pressure_baseline(args.check_pressure_baseline)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
