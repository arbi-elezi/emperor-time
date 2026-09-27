#!/usr/bin/env python3
"""Root-cause tracing HARD-GATE card for emperor-heal (Python core).

Leaf adapted from obra/superpowers skills/systematic-debugging
root-cause-tracing.md (MIT) — Trace backward / Fix at source / Never fix
just the symptom only. Emperor Time + Holy Chain stay the orchestrator;
do not announce the foreign skill name. Does not vendor whole
systematic-debugging (no pressure/academic packs). Sibling leaves
cover defense-in-depth, condition-based-waiting, and find-polluter.

Prints TRACE / STEP / MUST lines.
--reject-symptom-fix and --reject-untraced always fail (HARD-GATE helpers).
Optional --check-chain TEXT fails when fewer than two backward links appear.
Phase-1 companion to scripts/emperor heal (four-phase card).
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "skills/emperor-heal/root-cause-tracing.md"
SOURCE = (
    "obra/superpowers systematic-debugging → "
    "root-cause-tracing (Trace backward / Fix at source)"
)
IRON = "NO_SYMPTOM_FIX_WITHOUT_SOURCE_TRACE"

# One backward hop: "called by", unicode/ascii arrows used in stack traces
CHAIN_LINK_RE = re.compile(
    r"(?:called\s+by|\u2192|\u2190|->|<-)",
    re.IGNORECASE,
)

STEPS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "observe",
        "name": "Observe the Symptom",
        "need": "Quote the error / wrong path / bad value where it appears",
    },
    {
        "n": "2",
        "id": "immediate",
        "name": "Find Immediate Cause",
        "need": "Name the code that directly causes the symptom (file/fn)",
    },
    {
        "n": "3",
        "id": "caller",
        "name": "Ask: What Called This?",
        "need": "One level up the call chain with the value that was passed",
    },
    {
        "n": "4",
        "id": "upward",
        "name": "Keep Tracing Up",
        "need": "Repeat until the bad value / wrong cwd / empty arg originates",
    },
    {
        "n": "5",
        "id": "trigger",
        "name": "Find Original Trigger",
        "need": "Name the source; fix THERE — not at the symptom site",
    },
]


def format_card() -> str:
    lines = [
        "TRACE checklist=yes",
        f"TRACE leaf={LEAF}",
        f"TRACE source={SOURCE}",
        f"TRACE iron={IRON}",
        "TRACE companion=scripts/emperor heal (Phase 1 Root Cause Investigation)",
    ]
    for s in STEPS:
        lines.append(
            f"STEP {s['n']} id={s['id']} name={s['name']} need={s['need']}"
        )
    lines.append(
        "STEP rule=dead_end → fix at last reachable layer only after "
        "recording the dead end; prefer source when reachable"
    )
    lines.append(
        "STEP rule=instrument_when_stuck — add stack/log at the failing op, "
        "re-run, read the captured chain"
    )
    lines.append(
        "STEP rule=fix_at_source_then_optional_defense_in_depth "
        "(validation at layers is additive, not a substitute for source fix)"
    )
    lines.append("")
    lines.append(
        "MUST: Trace backward through the call chain to the original trigger "
        f"before proposing a fix. Open {LEAF}. Run scripts/emperor trace "
        "to reprint this card. Phase-1 companion: scripts/emperor heal."
    )
    lines.append(
        "MUST-NOT: fix only where the error appears; stack symptom patches; "
        "load whole systematic-debugging (find-polluter, defense-in-depth "
        "essay, condition-based-waiting, pressure tests). "
        "ET + Holy Chain remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_symptom_fix() -> str:
    return (
        "REJECT SYMPTOM FIX: HARD-GATE — no fix at the symptom site alone. "
        "Trace backward to the original trigger; fix at the source. "
        f"Iron={IRON}. Open {LEAF}. "
        "Re-run scripts/emperor trace --check-chain \"...\".\n"
    )


def reject_untraced() -> str:
    return (
        "REJECT UNTRACED: HARD-GATE — no implementation without a backward "
        "trace (symptom → immediate → caller → … → trigger). "
        f"Iron={IRON}. Open {LEAF}. Run scripts/emperor heal for phase order.\n"
    )


def check_chain(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when ≥2 backward links are present."""
    hits = CHAIN_LINK_RE.findall(text or "")
    if len(hits) >= 2:
        shown = ", ".join(hits[:5])
        more = f" (+{len(hits) - 5} more)" if len(hits) > 5 else ""
        return (
            True,
            f"CHAIN OK: found {len(hits)} backward link(s): {shown}{more}\n",
        )
    return (
        False,
        "CHAIN FAIL: need ≥2 backward links "
        "('called by', →, ←, ->, or <-) showing a multi-hop trace. "
        f"Iron={IRON}. Keep tracing up. Open {LEAF}.\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time root-cause tracing HARD-GATE card "
            "for emperor-heal (trace backward / fix at source)."
        )
    )
    parser.add_argument(
        "--reject-symptom-fix",
        action="store_true",
        help="Hard-gate: exit 1 when about to fix only at the symptom site",
    )
    parser.add_argument(
        "--reject-untraced",
        action="store_true",
        help="Hard-gate: exit 1 when about to implement without a backward trace",
    )
    parser.add_argument(
        "--check-chain",
        metavar="TEXT",
        default=None,
        help="Exit 0 if TEXT has ≥2 backward links; else exit 1 with CHAIN FAIL",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_symptom_fix:
        sys.stdout.write(reject_symptom_fix())
        return 1
    if args.reject_untraced:
        sys.stdout.write(reject_untraced())
        return 1
    if args.check_chain is not None:
        ok, msg = check_chain(args.check_chain)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
