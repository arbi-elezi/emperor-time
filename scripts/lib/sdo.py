#!/usr/bin/env python3
"""Skill Discovery Optimization (SDO) HARD-GATE card for Chain Jail authoring.

Leaf adapted from obra/superpowers skills/writing-skills SKILL.md
heading "Skill Discovery Optimization (SDO)" — CRITICAL: Description =
When to Use, NOT What the Skill Does (MIT). Emperor Time + Chain Jail
authoring.md stay the orchestrator; do not announce the foreign skill
name. Does not vendor whole writing-skills. SDO is this Chain Jail leaf
only (not keyword-coverage essay, not token-efficiency dump, not
graphviz / anthropic-best-practices).

Prints SDO / PRIN / GATE / MUST lines.
--reject-workflow-summary and --reject-no-trigger always fail (HARD-GATE
helpers). Optional --check-description TEXT fails when "Use when" /
trigger signals are missing, or when workflow-summary tokens appear.
Companion when writing skill frontmatter description after authoring
RGR (emperor author), alongside persuasion wording and skill-test
pressure.
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "chains/chain-jail/skill-discovery.md"
SOURCE = (
    "obra/superpowers writing-skills → Skill Discovery Optimization "
    "(SDO) / Description = When to Use, NOT What the Skill Does"
)
IRON = "DESCRIPTION_TRIGGERS_NOT_WORKFLOW"

PRINCIPLES: list[dict[str, str]] = [
    {
        "n": "1",
        "id": "trigger_only",
        "name": "Trigger-only description",
        "need": (
            "Description answers Should I read this skill right now? "
            "with when-to-use conditions only; never summarize the "
            "skill body process"
        ),
    },
    {
        "n": "2",
        "id": "no_workflow",
        "name": "No workflow summary",
        "need": (
            "NEVER summarize the skill process or workflow in "
            "description (dispatches X then Y / write test first "
            "watch it fail) — agents follow the shortcut and skip "
            "the body"
        ),
    },
    {
        "n": "3",
        "id": "use_when",
        "name": "Use when",
        "need": (
            "Start with Use when... focusing on triggering conditions, "
            "symptoms, and situations"
        ),
    },
    {
        "n": "4",
        "id": "symptoms",
        "name": "Concrete symptoms",
        "need": (
            "Name the problem (race conditions, missing capability) "
            "not a step list; keep tech-agnostic unless the skill "
            "itself is technology-specific"
        ),
    },
    {
        "n": "5",
        "id": "third_person",
        "name": "Third person",
        "need": (
            "Write in third person (harness injects into system "
            "prompt); avoid I can help you..."
        ),
    },
]

# Tokens that mark a description as summarizing workflow/process.
WORKFLOW_TOKENS = (
    "dispatches",
    "dispatch subagent",
    "code review between",
    "write test first",
    "watch it fail",
    "write minimal code",
    "red-green-refactor",
    "red green refactor",
    "then write",
    "then run",
    "then refactor",
    "step 1",
    "step 2",
    "workflow:",
    "process:",
    "followed by",
    "after which",
)

TRIGGER_TOKENS = (
    "use when",
    "use before",
    "use after",
    "use during",
    "use if",
    "when the",
    "when you",
    "when tests",
    "when implementing",
    "when creating",
    "when editing",
    "when verifying",
    "when a",
    "before writing",
    "before implementing",
)


def format_card() -> str:
    lines = [
        "SDO checklist=yes",
        f"SDO leaf={LEAF}",
        f"SDO source={SOURCE}",
        f"SDO iron={IRON}",
        "SDO companion=scripts/emperor author (skill RGR — failing baseline first)",
        "SDO companion=scripts/emperor persuasion (critical-practice wording)",
        "SDO companion=scripts/emperor skill-test (combined pressure after wording)",
        "SDO companion=chains/chain-jail/authoring-checklist.md",
    ]
    for prin in PRINCIPLES:
        lines.append(
            f"PRIN {prin['n']} id={prin['id']} name={prin['name']} "
            f"need={prin['need']}"
        )
    lines.append(
        "GATE rule=before_description — write Use when... trigger "
        "conditions / symptoms only; never put the skill's step list "
        "or workflow into the YAML description field"
    )
    lines.append(
        "GATE rule=no_workflow_shortcut — dispatches X then Y / write "
        "test first watch it fail / numbered process in description "
        "are HARD-GATE failures (agents skip the body)"
    )
    lines.append("")
    lines.append(
        "MUST: When authoring skill frontmatter, description = when to "
        f"use (triggers), not what the skill does as a process. Open "
        f"{LEAF}. Run scripts/emperor sdo to reprint this card. "
        "Companions: scripts/emperor author, persuasion, skill-test."
    )
    lines.append(
        "MUST-NOT: summarize workflow in description; omit Use when / "
        "trigger signals; first-person I can help; dump whole "
        "writing-skills / keyword essay / graphviz / "
        "anthropic-best-practices. ET + Chain Jail remain the "
        "orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_workflow_summary() -> str:
    return (
        "REJECT WORKFLOW-SUMMARY: HARD-GATE — description that "
        "summarizes the skill process (dispatches X then Y / write "
        "test first / watch it fail / step lists) creates a shortcut "
        "agents follow instead of reading the skill body. Rewrite "
        "with Use when... triggers only. "
        f"Iron={IRON}. Open {LEAF}. Re-run scripts/emperor "
        "sdo --check-description \"...\".\n"
    )


def reject_no_trigger() -> str:
    return (
        "REJECT NO-TRIGGER: HARD-GATE — description without Use when "
        "/ trigger conditions does not answer Should I load this "
        "skill right now?. Start with Use when... and name symptoms "
        f"/ situations. Iron={IRON}. Open {LEAF}.\n"
    )


def check_description(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok when trigger signal present and no workflow summary."""
    raw = (text or "").strip()
    low = raw.lower()
    found: set[str] = set()

    if any(t in low for t in TRIGGER_TOKENS):
        found.add("trigger")
    if re.search(r"\buse when\b", low):
        found.add("trigger")
        found.add("use-when")

    workflow_hits = [t for t in WORKFLOW_TOKENS if t in low]
    if workflow_hits:
        shown = ", ".join(workflow_hits[:4])
        return (
            False,
            "SDO FAIL: workflow-summary token(s) in description: "
            f"{shown}. Iron={IRON}. Open {LEAF}.\n",
        )

    if "trigger" not in found:
        return (
            False,
            "SDO FAIL: need Use when / trigger conditions "
            f"(symptoms/situations). Iron={IRON}. Open {LEAF}.\n",
        )

    shown = ", ".join(sorted(found))
    return (
        True,
        f"SDO OK: description signal(s): {shown}\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time skill-discovery (SDO) HARD-GATE card "
            "for Chain Jail authoring (description = when, not workflow)."
        )
    )
    parser.add_argument(
        "--reject-workflow-summary",
        action="store_true",
        help="Hard-gate: exit 1 when description summarizes skill workflow",
    )
    parser.add_argument(
        "--reject-no-trigger",
        action="store_true",
        help="Hard-gate: exit 1 when description lacks Use when / triggers",
    )
    parser.add_argument(
        "--check-description",
        metavar="TEXT",
        default=None,
        help=(
            "Exit 0 if TEXT has Use when / trigger signals and no "
            "workflow-summary tokens; else exit 1"
        ),
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_workflow_summary:
        sys.stdout.write(reject_workflow_summary())
        return 1
    if args.reject_no_trigger:
        sys.stdout.write(reject_no_trigger())
        return 1
    if args.check_description is not None:
        ok, msg = check_description(args.check_description)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
