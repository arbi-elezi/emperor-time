#!/usr/bin/env python3
"""Find-polluter HARD-GATE card for emperor-heal (Python core).

Leaf adapted from obra/superpowers skills/systematic-debugging
find-polluter.sh (MIT) — Find which test creates unwanted files/state /
do not guess the polluter. Emperor Time + Holy Chain stay the
orchestrator; do not announce the foreign skill name. Does not vendor
whole systematic-debugging (pressure/academic is a sibling leaf). find-polluter
is this Chain Jail leaf only.

Prints POLLUTER / STEP / MUST lines.
--reject-guess and --reject-unbisected always fail (HARD-GATE helpers).
Optional --check-found TEXT fails when no polluter-identity signal appears.
Phase-1/2 companion when shared-state / leftover files break later tests
(heal; after reproduce, before symptom fixes).
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "skills/emperor-heal/find-polluter.md"
SOURCE = (
    "obra/superpowers systematic-debugging → "
    "find-polluter.sh (Find which test creates unwanted files/state)"
)
IRON = "NO_GUESS_THE_POLLUTER"

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "marker",
        "name": "Name the pollution marker",
        "need": "Path / file / dir that should not exist after a clean run",
    },
    {
        "n": "2",
        "id": "candidates",
        "name": "List candidate tests",
        "need": "Enumerate test files matching the suite pattern (sorted)",
    },
    {
        "n": "3",
        "id": "sequential",
        "name": "Run one test at a time",
        "need": "Before each run confirm marker absent; run only that test",
    },
    {
        "n": "4",
        "id": "stop",
        "name": "Stop at first creator",
        "need": "First test that creates the marker is the polluter — stop",
    },
    {
        "n": "5",
        "id": "investigate",
        "name": "Investigate that test only",
        "need": "Open the polluter; fix cleanup / isolation there (not elsewhere)",
    },
]

# Strong tokens for --check-found (any one is enough with a path-ish signal)
STRONG_TOKENS = (
    "found polluter",
    "polluter",
    "pollution",
    "created:",
    "bisect",
    "test:",
)
# path-ish: something.test.* or *test* file path
PATHISH_RE = re.compile(
    r"(?:^|[\s`\"'])("
    r"[^\s`\"']+\.(?:test|spec)\.[A-Za-z0-9]+"
    r"|[^\s`\"']*test[^\s`\"']*\.[A-Za-z0-9]+"
    r")",
    re.IGNORECASE,
)


def format_card() -> str:
    lines = [
        "POLLUTER checklist=yes",
        f"POLLUTER leaf={LEAF}",
        f"POLLUTER source={SOURCE}",
        f"POLLUTER iron={IRON}",
        "POLLUTER companion=scripts/emperor heal (Phase 1–2 shared-state / leftover files)",
        "POLLUTER companion=scripts/emperor trace (source fix after polluter known)",
        "POLLUTER companion=scripts/emperor wait (flaky timing is a different leaf)",
    ]
    for step in STEPS:
        lines.append(
            f"STEP {step['n']} id={step['id']} name={step['name']} "
            f"need={step['need']}"
        )
    lines.append(
        "STEP rule=marker_absent_before — skip a candidate when pollution "
        "already exists; clean or pick a fresh marker first"
    )
    lines.append(
        "STEP rule=runner_agnostic — invoke the project test runner for one "
        "file (pytest / npm test / go test / …); do not hardcode one ecosystem"
    )
    lines.append(
        "STEP rule=stop_at_first — do not keep running after FOUND POLLUTER; "
        "the first creator is enough evidence"
    )
    lines.append(
        "STEP rule=fix_cleanup_at_polluter — isolate teardown / temp dirs in "
        "the polluter test; do not paper over with later deletes"
    )
    lines.append("")
    lines.append(
        "MUST: When leftover files or shared state break later tests, find "
        "which test creates the pollution by running candidates one-by-one "
        f"(or bisecting). Open {LEAF}. Run scripts/emperor polluter to reprint "
        "this card. Companions: scripts/emperor heal, scripts/emperor trace."
    )
    lines.append(
        "MUST-NOT: guess which test polluted; ship a cleanup elsewhere while "
        "the polluter stays dirty; keep running the whole suite hoping order "
        "changes; load whole systematic-debugging (pressure/academic is a sibling leaf). "
        "ET + Holy Chain remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_guess() -> str:
    return (
        "REJECT GUESS: HARD-GATE — do not guess which test created the "
        "pollution. Name the marker; run candidates one-by-one until FOUND "
        f"POLLUTER. Iron={IRON}. Open {LEAF}. "
        "Re-run scripts/emperor polluter --check-found \"...\".\n"
    )


def reject_unbisected() -> str:
    return (
        "REJECT UNBISECTED: HARD-GATE — no ship of a shared-state / leftover "
        "fix without identifying the polluter test. "
        f"Iron={IRON}. Open {LEAF}. Run scripts/emperor heal (Phase 1–2), then "
        "scripts/emperor polluter.\n"
    )


def check_found(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when polluter identity signals appear."""
    raw = text or ""
    low = raw.lower()
    found: set[str] = set()
    for tok in STRONG_TOKENS:
        if tok in low:
            found.add(tok)
    path_hits = PATHISH_RE.findall(raw)
    if path_hits:
        found.add("test-path")
    # Need at least one strong token AND (path or 'found polluter' / created:)
    strong_core = found & {
        "found polluter",
        "polluter",
        "pollution",
        "created:",
        "bisect",
        "test:",
        "test-path",
    }
    has_identity = (
        "found polluter" in found
        or ("polluter" in found and ("test-path" in found or "created:" in found or "test:" in found))
        or ("pollution" in found and "test-path" in found)
        or ("bisect" in found and "test-path" in found)
    )
    if has_identity and strong_core:
        shown = ", ".join(sorted(found))
        return (
            True,
            f"POLLUTER OK: found polluter-identity signal(s): {shown}\n",
        )
    return (
        False,
        "POLLUTER FAIL: need polluter identity "
        "(e.g. 'FOUND POLLUTER' + test path, or polluter + created: + path). "
        f"Iron={IRON}. Run candidates one-by-one. Open {LEAF}.\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time find-polluter HARD-GATE card "
            "for emperor-heal (find which test creates unwanted state)."
        )
    )
    parser.add_argument(
        "--reject-guess",
        action="store_true",
        help="Hard-gate: exit 1 when about to guess which test polluted",
    )
    parser.add_argument(
        "--reject-unbisected",
        action="store_true",
        help="Hard-gate: exit 1 when about to ship without finding the polluter",
    )
    parser.add_argument(
        "--check-found",
        metavar="TEXT",
        default=None,
        help=(
            "Exit 0 if TEXT shows polluter identity "
            "(FOUND POLLUTER + path, or polluter/created/path signals); else exit 1"
        ),
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_guess:
        sys.stdout.write(reject_guess())
        return 1
    if args.reject_unbisected:
        sys.stdout.write(reject_unbisected())
        return 1
    if args.check_found is not None:
        ok, msg = check_found(args.check_found)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
