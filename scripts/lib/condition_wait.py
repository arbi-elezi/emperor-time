#!/usr/bin/env python3
"""Condition-based-waiting HARD-GATE card for emperor-heal (Python core).

Leaf adapted from obra/superpowers skills/systematic-debugging
condition-based-waiting.md (MIT) — Wait for the actual condition /
not a guess about timing. Emperor Time + Holy Chain stay the
orchestrator; do not announce the foreign skill name. Does not vendor
whole systematic-debugging (no pressure/academic packs).
condition-based-waiting is this Chain Jail leaf only;
find-polluter is a separate leaf (`emperor polluter`).

Prints WAIT / COND / MUST lines.
--reject-sleep and --reject-unguessed always fail (HARD-GATE helpers).
Optional --check-condition TEXT fails when no real condition-wait signal.
Phase-4 companion for flaky / timing waits (heal; after defense / trace).
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "skills/emperor-heal/condition-based-waiting.md"
SOURCE = (
    "obra/superpowers systematic-debugging → "
    "condition-based-waiting (Wait for the actual condition / "
    "not a guess about timing)"
)
IRON = "NO_ARBITRARY_SLEEP"

CONDS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "event",
        "name": "Wait for event",
        "need": "Poll until the named event appears (not a fixed delay)",
    },
    {
        "n": "2",
        "id": "state",
        "name": "Wait for state",
        "need": "Poll until machine/object reaches ready / target state",
    },
    {
        "n": "3",
        "id": "count",
        "name": "Wait for count",
        "need": "Poll until length / count meets the threshold",
    },
    {
        "n": "4",
        "id": "file",
        "name": "Wait for file",
        "need": "Poll until path exists / is readable",
    },
]

# Strong tokens for --check-condition (any one is enough)
STRONG_TOKENS = (
    "waitfor",
    "wait_for",
    "until",
    "condition",
    "poll",
    "exists",
    "ready",
    "event",
)
# waitFor / wait_for / WaitForEvent-style identifiers
WAITFOR_RE = re.compile(r"wait[_]?for\w*", re.IGNORECASE)


def format_card() -> str:
    lines = [
        "WAIT checklist=yes",
        f"WAIT leaf={LEAF}",
        f"WAIT source={SOURCE}",
        f"WAIT iron={IRON}",
        "WAIT companion=scripts/emperor heal (Phase 4 flaky-test / timing cure)",
        "WAIT companion=scripts/emperor defense (layers after source fix)",
        "WAIT companion=scripts/emperor trace (source fix first)",
    ]
    for cond in CONDS:
        lines.append(
            f"COND {cond['n']} id={cond['id']} name={cond['name']} "
            f"need={cond['need']}"
        )
    lines.append(
        "COND rule=poll_interval — poll about every 10ms (not 1ms busy-spin; "
        "not multi-second blind sleep)"
    )
    lines.append(
        "COND rule=always_timeout — every wait has a timeout + clear error; "
        "never loop forever"
    )
    lines.append(
        "COND rule=fresh_getter — call the getter inside the loop; "
        "do not cache stale state before polling"
    )
    lines.append(
        "COND rule=document_why — if an arbitrary timeout is truly needed "
        "(timed behavior), document WHY after waiting for the trigger condition"
    )
    lines.append("")
    lines.append(
        "MUST: Wait for the actual condition (event / state / count / file), "
        f"not a guess about timing. Open {LEAF}. Run "
        "scripts/emperor wait to reprint this card. Flaky/timing cure sits in "
        "heal Phase 4. Companions: scripts/emperor defense, "
        "scripts/emperor trace."
    )
    lines.append(
        "MUST-NOT: ship arbitrary setTimeout / sleep / time.sleep as the wait; "
        "wait without a named condition; poll with no timeout; cache getters "
        "outside the loop; load whole systematic-debugging "
        "(find-polluter, pressure tests). ET + Holy Chain remain the "
        "orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_sleep() -> str:
    return (
        "REJECT SLEEP: HARD-GATE — arbitrary setTimeout / sleep / time.sleep "
        "is not a wait. Wait for the actual condition (event / state / count / "
        f"file). Iron={IRON}. Open {LEAF}. "
        "Re-run scripts/emperor wait --check-condition \"...\".\n"
    )


def reject_unguessed() -> str:
    return (
        "REJECT UNGUESSED: HARD-GATE — no ship of a wait without a named "
        "condition. Guessing at timing creates flakes. "
        f"Iron={IRON}. Open {LEAF}. Run scripts/emperor heal (Phase 4), then "
        "scripts/emperor wait.\n"
    )


def check_condition(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when ≥1 strong token or waitFor pattern."""
    raw = text or ""
    low = raw.lower()
    # Normalize separators so wait-for / wait_for count
    compact = re.sub(r"[\s\-]+", "", low)
    found: set[str] = set()
    for tok in STRONG_TOKENS:
        needle = tok.replace("_", "")
        if tok in low or needle in compact:
            found.add(tok)
    if WAITFOR_RE.search(raw):
        found.add("waitfor")
    if found:
        shown = ", ".join(sorted(found))
        return (
            True,
            f"CONDITION OK: found condition-wait signal(s): {shown}\n",
        )
    return (
        False,
        "CONDITION FAIL: need a real condition wait "
        f"(tokens: {', '.join(STRONG_TOKENS)}) or waitFor-style pattern. "
        f"Iron={IRON}. Name the event/state/count/file. Open {LEAF}.\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time condition-based-waiting HARD-GATE card "
            "for emperor-heal (wait for the actual condition)."
        )
    )
    parser.add_argument(
        "--reject-sleep",
        action="store_true",
        help="Hard-gate: exit 1 when about to ship arbitrary sleep/setTimeout",
    )
    parser.add_argument(
        "--reject-unguessed",
        action="store_true",
        help="Hard-gate: exit 1 when about to wait without a named condition",
    )
    parser.add_argument(
        "--check-condition",
        metavar="TEXT",
        default=None,
        help=(
            "Exit 0 if TEXT shows a real condition wait "
            "(≥1 strong token or waitFor pattern); else exit 1"
        ),
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_sleep:
        sys.stdout.write(reject_sleep())
        return 1
    if args.reject_unguessed:
        sys.stdout.write(reject_unguessed())
        return 1
    if args.check_condition is not None:
        ok, msg = check_condition(args.check_condition)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
