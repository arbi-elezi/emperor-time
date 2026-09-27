#!/usr/bin/env python3
"""Writing-good-tests HARD-GATE card for emperor-tdd (Python core).

Leaf adapted from obra/superpowers skills/test-driven-development
writing-good-tests.md (MIT) — Name the Break / Exercise the Real Thing /
Gate Function / Mutation Check. Emperor Time + emperor-tdd stay the
orchestrator; do not announce the foreign skill name.
Does not vendor whole test-driven-development. writing-good-tests is this
Chain Jail leaf only.

Prints GOOD / PRIN / GATE / MUST lines.
--reject-mirror and --reject-change-detector always fail (HARD-GATE helpers).
Optional --check-named-break TEXT fails when name-the-break + real-thing
signals are missing.
Companion when writing or changing tests after the RGR cycle (emperor tdd).
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "skills/emperor-tdd/writing-good-tests.md"
SOURCE = (
    "obra/superpowers test-driven-development → writing-good-tests.md "
    "(Name the Break / Exercise the Real Thing)"
)
IRON = "EVERY_TEST_NAMES_THE_BREAK"

PRINCIPLES: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "name_break",
        "name": "Name the Break",
        "need": (
            "Every test names the production change that would make it fail "
            "(a bug, not a redesign decision)"
        ),
    },
    {
        "n": "2",
        "id": "exercise_real",
        "name": "Exercise the Real Thing",
        "need": (
            "Mock earns no assertions; assert real component behavior; "
            "unmock or delete mock-existence checks"
        ),
    },
    {
        "n": "3",
        "id": "hand_derived",
        "name": "Hand-derived expectations",
        "need": (
            "Literals / hand-checked fixtures; never reuse code-under-test "
            "helpers to build want"
        ),
    },
    {
        "n": "4",
        "id": "mutation",
        "name": "Mutation check",
        "need": (
            "Before finish: at least one test fails for each realistic "
            "production mutation (wrong arg, branch, side effect, empty)"
        ),
    },
]

# Strong tokens for --check-named-break
BREAK_TOKENS = (
    "name the break",
    "names the break",
    "production change",
    "would make this test fail",
    "would make the test fail",
    "catch a bug",
    "catches a bug",
    "break it catches",
    "observable behavior",
    "wrong branch",
    "missing side effect",
    "broken contract",
)
REAL_TOKENS = (
    "real thing",
    "real component",
    "exercise the real",
    "mock earns no",
    "assert the real",
    "unmock",
    "not the mock",
    "integration test",
    "real behavior",
)
HAND_TOKENS = (
    "hand-derived",
    "hand derived",
    "literal",
    "hand-checked",
    "hand checked",
    "without the code under test",
    "not mirror",
    "no mirror",
)
MUTATION_TOKENS = (
    "mutation check",
    "mutation",
    "mutate the production",
    "wrong constant",
    "wrong argument",
    "missing validation",
)


def format_card() -> str:
    lines = [
        "GOOD checklist=yes",
        f"GOOD leaf={LEAF}",
        f"GOOD source={SOURCE}",
        f"GOOD iron={IRON}",
        "GOOD companion=scripts/emperor tdd (RGR — failing probe first)",
        "GOOD companion=skills/emperor-tdd/red-green-refactor.md",
    ]
    for prin in PRINCIPLES:
        lines.append(
            f"PRIN {prin['n']} id={prin['id']} name={prin['name']} "
            f"need={prin['need']}"
        )
    lines.append(
        "GATE rule=before_body — name the break before writing the test body; "
        "cannot name one → redesign; source-text-only → run the artifact; "
        "change-detector → test the behavior that depends on the decision"
    )
    lines.append(
        "GATE rule=before_mock — list real side effects; keep depended-on "
        "behavior real; mock only slow/external; never assert on the mock itself"
    )
    lines.append(
        "GATE rule=no_mirror — expected values are literals or hand-checked "
        "fixtures; builders shared with the code under test fail the gate"
    )
    lines.append("")
    lines.append(
        "MUST: Before writing or changing a test, name the production break "
        f"it catches and exercise the real thing. Open {LEAF}. Run "
        "scripts/emperor good-tests to reprint this card. Companion: "
        "scripts/emperor tdd."
    )
    lines.append(
        "MUST-NOT: ship mirror assertions, change detectors, mock-existence "
        "checks, or source-text greps as tests; claim coverage while no "
        "mutation fails; load whole test-driven-development. ET + emperor-tdd "
        "remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_mirror() -> str:
    return (
        "REJECT MIRROR: HARD-GATE — do not build expected values with the "
        "code under test (or its helpers). Use a literal or hand-checked "
        f"fixture. Iron={IRON}. Open {LEAF}. Re-run scripts/emperor "
        "good-tests --check-named-break \"...\".\n"
    )


def reject_change_detector() -> str:
    return (
        "REJECT CHANGE-DETECTOR: HARD-GATE — a test that fails only on "
        "intentional redesign (constants, message wording, private structure) "
        "sleeps through bugs. Name a bug-shaped break and assert the behavior "
        f"that depends on the decision. Iron={IRON}. Open {LEAF}.\n"
    )


def check_named_break(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when name-break + real/hand signals appear."""
    raw = text or ""
    low = raw.lower()
    found: set[str] = set()

    if any(t in low for t in BREAK_TOKENS):
        found.add("name-break")
    if any(t in low for t in REAL_TOKENS):
        found.add("real-thing")
    if any(t in low for t in HAND_TOKENS):
        found.add("hand-derived")
    if any(t in low for t in MUTATION_TOKENS):
        found.add("mutation")
    # Gate-function phrasing
    if "before writing" in low and ("test" in low or "body" in low):
        found.add("gate-before")
    if re.search(r"\bbug\b", low) and (
        "fail" in low or "catch" in low or "break" in low
    ):
        found.add("name-break")

    has_core = "name-break" in found
    has_quality = bool(
        found & {"real-thing", "hand-derived", "mutation", "gate-before"}
    )
    if has_core and has_quality:
        shown = ", ".join(sorted(found))
        return (
            True,
            f"GOOD OK: named-break/quality signal(s): {shown}\n",
        )
    return (
        False,
        "GOOD FAIL: need name-the-break signal plus real-thing / "
        "hand-derived / mutation / gate-before. "
        f"Iron={IRON}. Open {LEAF}.\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time writing-good-tests HARD-GATE card "
            "for emperor-tdd (name the break / exercise the real thing)."
        )
    )
    parser.add_argument(
        "--reject-mirror",
        action="store_true",
        help="Hard-gate: exit 1 when about to ship a mirror assertion",
    )
    parser.add_argument(
        "--reject-change-detector",
        action="store_true",
        help="Hard-gate: exit 1 when about to ship a change-detector test",
    )
    parser.add_argument(
        "--check-named-break",
        metavar="TEXT",
        default=None,
        help=(
            "Exit 0 if TEXT names the break plus real-thing/hand-derived/"
            "mutation/gate-before; else exit 1"
        ),
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_mirror:
        sys.stdout.write(reject_mirror())
        return 1
    if args.reject_change_detector:
        sys.stdout.write(reject_change_detector())
        return 1
    if args.check_named_break is not None:
        ok, msg = check_named_break(args.check_named_break)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
