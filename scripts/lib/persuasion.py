#!/usr/bin/env python3
"""Persuasion-principles HARD-GATE card for Chain Jail authoring (Python core).

Leaf adapted from obra/superpowers skills/writing-skills
persuasion-principles.md (MIT) — Authority / Commitment / Scarcity /
Social Proof / Unity / Reciprocity / Liking for critical skill practices.
Emperor Time + Chain Jail authoring.md stay the orchestrator; do not
announce the foreign skill name.
Does not vendor whole writing-skills. persuasion-principles is this
Chain Jail leaf only.

Prints PERSUADE / PRIN / GATE / MUST lines.
--reject-hedge and --reject-optional always fail (HARD-GATE helpers).
Optional --check-persuasion TEXT fails when authority + commitment
signals are missing, or when none of scarcity/social-proof/unity appear.
Companion when wording critical practices after the authoring RGR cycle
(emperor author) and before skill-test pressure.
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "chains/chain-jail/persuasion-principles.md"
SOURCE = (
    "obra/superpowers writing-skills → persuasion-principles.md "
    "(Authority / Commitment / Scarcity / Social Proof / Unity)"
)
IRON = "CRITICAL_PRACTICE_USES_PERSUASION"

PRINCIPLES: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "authority",
        "name": "Authority",
        "need": (
            "Imperative language (YOU MUST / Never / Always / No exceptions) "
            "for discipline and safety-critical practices; soft consider "
            "does not bind"
        ),
    },
    {
        "n": "2",
        "id": "commitment",
        "name": "Commitment",
        "need": (
            "Require announcements, force explicit A/B/C choices, or use "
            "tracking (todos) so the agent commits before acting"
        ),
    },
    {
        "n": "3",
        "id": "scarcity",
        "name": "Scarcity",
        "need": (
            "Time-bound or sequential gates (Before proceeding / Immediately "
            "after X) that block deferral"
        ),
    },
    {
        "n": "4",
        "id": "social_proof",
        "name": "Social Proof",
        "need": (
            "Universal norms (Every time / Always) and failure modes "
            "(X without Y = failure) that establish what everyone does"
        ),
    },
    {
        "n": "5",
        "id": "unity",
        "name": "Unity",
        "need": (
            "Shared-identity language (our codebase / we both want quality) "
            "for collaborative judgment without hierarchy theater"
        ),
    },
    {
        "n": "6",
        "id": "reciprocity",
        "name": "Reciprocity",
        "need": (
            "Use sparingly or avoid in skills; can feel manipulative; "
            "other principles are usually enough"
        ),
    },
    {
        "n": "7",
        "id": "liking",
        "name": "Liking",
        "need": (
            "Do NOT use for compliance; conflicts with honest feedback; "
            "creates sycophancy"
        ),
    },
]

AUTHORITY_TOKENS = (
    "you must",
    "must ",
    "never",
    "always",
    "no exceptions",
    "no exception",
    "imperative",
    "hard-gate",
    "hard gate",
    "iron law",
)
COMMITMENT_TOKENS = (
    "announce",
    "announcement",
    "choose a",
    "choose a, b, or c",
    "a/b/c",
    "a, b, or c",
    "tracking",
    "todo",
    "todos",
    "checklist",
    "commit to",
    "explicit choice",
)
SCARCITY_TOKENS = (
    "before proceeding",
    "immediately",
    "immediately after",
    "time-bound",
    "right now",
    "do not defer",
    "no later",
    "sequential",
)
SOCIAL_TOKENS = (
    "every time",
    "everyone",
    "without y = failure",
    "without = failure",
    "= failure",
    "social proof",
    "universal",
    "norm",
)
UNITY_TOKENS = (
    "our codebase",
    "we're colleagues",
    "we are colleagues",
    "we both",
    "shared",
    "unity",
    "colleagues",
)


def format_card() -> str:
    lines = [
        "PERSUADE checklist=yes",
        f"PERSUADE leaf={LEAF}",
        f"PERSUADE source={SOURCE}",
        f"PERSUADE iron={IRON}",
        "PERSUADE companion=scripts/emperor author (skill RGR — failing baseline first)",
        "PERSUADE companion=scripts/emperor skill-test (combined pressure after wording)",
        "PERSUADE companion=chains/chain-jail/authoring-checklist.md",
    ]
    for prin in PRINCIPLES:
        lines.append(
            f"PRIN {prin['n']} id={prin['id']} name={prin['name']} "
            f"need={prin['need']}"
        )
    lines.append(
        "GATE rule=before_wording — for critical / discipline practices write "
        "Authority (MUST/Never/Always/No exceptions) + Commitment (announce / "
        "choose A|B|C / tracking) plus at least one of Scarcity / Social Proof "
        "/ Unity; never rely on hedge language"
    )
    lines.append(
        "GATE rule=no_hedge_optional — consider / when feasible / "
        "optional for mandatory practices are HARD-GATE failures; "
        "Reciprocity sparingly; Liking never for compliance"
    )
    lines.append("")
    lines.append(
        "MUST: When authoring critical skill practices, use persuasion "
        f"principles so agents comply under pressure. Open {LEAF}. "
        "Run scripts/emperor persuasion to reprint this card. Companions: "
        "scripts/emperor author, scripts/emperor skill-test."
    )
    lines.append(
        "MUST-NOT: hedge critical practices (consider / when feasible); "
        "frame mandatory steps as optional; use Liking for compliance; dump "
        "whole writing-skills / graphviz / anthropic-best-practices. "
        "ET + Chain Jail remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_hedge() -> str:
    return (
        "REJECT HEDGE: HARD-GATE — soft consider / when feasible / "
        "you might want to language for critical practices does not bind. "
        "Rewrite with Authority (YOU MUST / Never / Always / No exceptions). "
        f"Iron={IRON}. Open {LEAF}. Re-run scripts/emperor "
        "persuasion --check-persuasion \"...\".\n"
    )


def reject_optional() -> str:
    return (
        "REJECT OPTIONAL: HARD-GATE — framing a mandatory practice as "
        "optional / nice-to-have / if you have time invites skip under "
        "pressure. Make it Authority + Commitment. "
        f"Iron={IRON}. Open {LEAF}.\n"
    )


def check_persuasion(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when authority + commitment + one of scarcity/social/unity."""
    raw = text or ""
    low = raw.lower()
    found: set[str] = set()

    if any(t in low for t in AUTHORITY_TOKENS):
        found.add("authority")
    if re.search(r"\b(must|never|always)\b", low):
        found.add("authority")
    if any(t in low for t in COMMITMENT_TOKENS):
        found.add("commitment")
    if re.search(r"\bchoose\b", low) and re.search(r"\b[abc]\b", low):
        found.add("commitment")
    if any(t in low for t in SCARCITY_TOKENS):
        found.add("scarcity")
    if any(t in low for t in SOCIAL_TOKENS):
        found.add("social-proof")
    if any(t in low for t in UNITY_TOKENS):
        found.add("unity")

    has_core = "authority" in found and "commitment" in found
    has_boost = bool(found & {"scarcity", "social-proof", "unity"})
    if has_core and has_boost:
        shown = ", ".join(sorted(found))
        return (
            True,
            f"PERSUADE OK: persuasion signal(s): {shown}\n",
        )
    return (
        False,
        "PERSUADE FAIL: need authority + commitment plus "
        "scarcity / social-proof / unity. "
        f"Iron={IRON}. Open {LEAF}.\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time persuasion-principles HARD-GATE card "
            "for Chain Jail authoring (authority / commitment / scarcity)."
        )
    )
    parser.add_argument(
        "--reject-hedge",
        action="store_true",
        help="Hard-gate: exit 1 when critical practice uses hedge language",
    )
    parser.add_argument(
        "--reject-optional",
        action="store_true",
        help="Hard-gate: exit 1 when mandatory practice is framed optional",
    )
    parser.add_argument(
        "--check-persuasion",
        metavar="TEXT",
        default=None,
        help=(
            "Exit 0 if TEXT has authority + commitment plus "
            "scarcity/social-proof/unity; else exit 1"
        ),
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_hedge:
        sys.stdout.write(reject_hedge())
        return 1
    if args.reject_optional:
        sys.stdout.write(reject_optional())
        return 1
    if args.check_persuasion is not None:
        ok, msg = check_persuasion(args.check_persuasion)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
