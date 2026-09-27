#!/usr/bin/env python3
"""Defense-in-depth HARD-GATE card for emperor-heal (Python core).

Leaf adapted from obra/superpowers skills/systematic-debugging
defense-in-depth.md (MIT) — Validate at every layer / Four layers only.
Emperor Time + Holy Chain stay the orchestrator; do not announce the
foreign skill name. Does not vendor whole systematic-debugging (no
find-polluter.sh, condition-based-waiting, or pressure tests).

Prints DEFENSE / LAYER / MUST lines.
--reject-single-layer and --reject-unlayered always fail (HARD-GATE helpers).
Optional --check-layers TEXT fails when fewer than two distinct layer ids appear.
Phase-4 companion after scripts/emperor trace (source fix first, then layers).
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "skills/emperor-heal/defense-in-depth.md"
SOURCE = (
    "obra/superpowers systematic-debugging → "
    "defense-in-depth (Validate at every layer / Four layers)"
)
IRON = "NO_SINGLE_LAYER_VALIDATION"

LAYERS: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "entry",
        "name": "Entry Point Validation",
        "need": "Reject obviously invalid input at the API / CLI boundary",
    },
    {
        "n": "2",
        "id": "business",
        "name": "Business Logic Validation",
        "need": "Ensure data makes sense for this operation (domain rules)",
    },
    {
        "n": "3",
        "id": "environment",
        "name": "Environment Guards",
        "need": "Refuse dangerous ops in test / CI / wrong-cwd contexts",
    },
    {
        "n": "4",
        "id": "debug",
        "name": "Debug Instrumentation",
        "need": "Capture stack/context at the dangerous op for forensics",
    },
]

LAYER_IDS = [layer["id"] for layer in LAYERS]
# Match whole layer ids as tokens (word-ish boundaries)
LAYER_RE = re.compile(
    r"(?:^|[\s,;|/])(" + "|".join(LAYER_IDS) + r")(?:$|[\s,;|/])",
    re.IGNORECASE,
)


def format_card() -> str:
    lines = [
        "DEFENSE checklist=yes",
        f"DEFENSE leaf={LEAF}",
        f"DEFENSE source={SOURCE}",
        f"DEFENSE iron={IRON}",
        "DEFENSE companion=scripts/emperor trace (source fix first; layers additive)",
        "DEFENSE companion=scripts/emperor heal (Phase 4 Implementation)",
    ]
    for layer in LAYERS:
        lines.append(
            f"LAYER {layer['n']} id={layer['id']} name={layer['name']} "
            f"need={layer['need']}"
        )
    lines.append(
        "LAYER rule=source_fix_first — defense-in-depth is additive after "
        "root-cause source fix (emperor trace); never a substitute"
    )
    lines.append(
        "LAYER rule=map_checkpoints — list every point bad data passes through "
        "before adding checks"
    )
    lines.append(
        "LAYER rule=test_bypass — try to bypass layer 1; verify layer 2+ catches it"
    )
    lines.append("")
    lines.append(
        "MUST: After the source fix, validate at every layer data passes through "
        f"(entry / business / environment / debug). Open {LEAF}. Run "
        "scripts/emperor defense to reprint this card. Trace companion: "
        "scripts/emperor trace. Phase order: scripts/emperor heal."
    )
    lines.append(
        "MUST-NOT: ship a single-layer guard as the whole fix; skip layers "
        "because 'entry validation is enough'; use layered checks instead of "
        "tracing to the source; load whole systematic-debugging "
        "(find-polluter, condition-based-waiting, pressure tests). "
        "ET + Holy Chain remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_single_layer() -> str:
    return (
        "REJECT SINGLE LAYER: HARD-GATE — one validation site is not enough. "
        "Validate at every layer data passes through (entry / business / "
        f"environment / debug). Iron={IRON}. Open {LEAF}. "
        "Re-run scripts/emperor defense --check-layers \"...\".\n"
    )


def reject_unlayered() -> str:
    return (
        "REJECT UNLAYERED: HARD-GATE — no ship of a source fix for invalid data "
        "without a multi-layer validation plan. "
        f"Iron={IRON}. Open {LEAF}. Run scripts/emperor trace first, then "
        "scripts/emperor defense.\n"
    )


def check_layers(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when ≥2 distinct layer ids appear."""
    found = {m.group(1).lower() for m in LAYER_RE.finditer(f" {text or ''} ")}
    # Also accept bare tokens at string edges via simple split scan
    tokens = re.findall(r"[A-Za-z]+", text or "")
    for tok in tokens:
        low = tok.lower()
        if low in LAYER_IDS:
            found.add(low)
    if len(found) >= 2:
        shown = ", ".join(sorted(found))
        return (
            True,
            f"LAYERS OK: found {len(found)} distinct layer id(s): {shown}\n",
        )
    return (
        False,
        "LAYERS FAIL: need ≥2 distinct layer ids "
        f"({', '.join(LAYER_IDS)}) showing multi-layer validation. "
        f"Iron={IRON}. Map checkpoints; add layers. Open {LEAF}.\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time defense-in-depth HARD-GATE card "
            "for emperor-heal (validate at every layer)."
        )
    )
    parser.add_argument(
        "--reject-single-layer",
        action="store_true",
        help="Hard-gate: exit 1 when about to ship with only one validation layer",
    )
    parser.add_argument(
        "--reject-unlayered",
        action="store_true",
        help="Hard-gate: exit 1 when about to ship without a layered validation plan",
    )
    parser.add_argument(
        "--check-layers",
        metavar="TEXT",
        default=None,
        help="Exit 0 if TEXT names ≥2 distinct layer ids; else exit 1 with LAYERS FAIL",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_single_layer:
        sys.stdout.write(reject_single_layer())
        return 1
    if args.reject_unlayered:
        sys.stdout.write(reject_unlayered())
        return 1
    if args.check_layers is not None:
        ok, msg = check_layers(args.check_layers)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
