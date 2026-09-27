#!/usr/bin/env python3
"""Diagnosing HARD-GATE card for emperor-heal (Python core).

Leaf adapted from obra/superpowers skills/diagnosing-superpowers
SKILL.md (MIT) — Core principle (citation iron law) + Intake before
analysis Hard rule only. Emperor Time + emperor-heal stay the
orchestrator; do not announce the foreign skill name. Does not vendor
diagnosing-superpowers (no analyst prompts, case/report templates,
bundles, or GitHub-issue workflow).

Prints DIAGNOSE / INTAKE / CITE / MUST lines.
--reject-uncited and --reject-skip-intake always fail (HARD-GATE helpers).
Optional --check-citation TEXT fails when no path:line citation is present.
Locate of transcript paths stays with session-discovery; this leaf gates
intake + citation honesty after locate.
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

LEAF = "skills/emperor-heal/diagnosing.md"
SOURCE = (
    "obra/superpowers diagnosing-superpowers → "
    "Core principle + Intake before analysis"
)
IRON_CITE = "NO_FINDING_WITHOUT_PATH_LINE_CITATION"
IRON_INTAKE = "INTAKE_BEFORE_ANALYSIS"

# path:line — absolute or relative path, then colon, then digits
CITATION_RE = re.compile(r"(?:^|[\s`\"'(])([A-Za-z0-9_./\\~-]+\.[A-Za-z0-9_]+):(\d+)\b")

INTAKE_FIELDS: list[dict[str, str]] = [
    {
        "id": "sessions",
        "name": "Session(s)",
        "need": "Named session id(s) and/or VERIFIED path(s) via session-discovery",
    },
    {
        "id": "expected",
        "name": "Expected",
        "need": "What the human partner expected to happen",
    },
    {
        "id": "happened",
        "name": "Happened",
        "need": "What was observed instead (not a reconstructed guess)",
    },
    {
        "id": "observable",
        "name": "Observable",
        "need": "Concrete care-about: wall-clock, tokens, repeated actions, one specific action",
    },
]


def format_card() -> str:
    lines = [
        "DIAGNOSE checklist=yes",
        f"DIAGNOSE leaf={LEAF}",
        f"DIAGNOSE source={SOURCE}",
        f"DIAGNOSE iron={IRON_CITE}",
        f"DIAGNOSE iron={IRON_INTAKE}",
        "DIAGNOSE locate=scripts/emperor session-discovery (VERIFIED path first)",
    ]
    for f in INTAKE_FIELDS:
        lines.append(
            f"INTAKE field={f['id']} name={f['name']} status=REQUIRED need={f['need']}"
        )
    lines.append(
        "INTAKE rule=one_question_at_a_time until a problem statement can be written"
    )
    lines.append(
        "INTAKE rule=complaint_is_not_statement "
        "('it took too long' needs an observable)"
    )
    lines.append(
        "INTAKE rule=partner_away → write questions and STOP; "
        "do not reconstruct their answer"
    )
    lines.append(
        "CITE rule=every_finding_needs_path_line (path:line); no citation → drop finding"
    )
    lines.append(
        "CITE rule=numbers_from_transcript_or_command_only; never from memory"
    )
    lines.append(
        "CITE rule=discard_returned_finding_without_path_line"
    )
    lines.append("")
    lines.append(
        "MUST: Finish intake (partner-answered problem statement) before "
        "locate/triage/report. Locate via session-discovery to VERIFIED paths. "
        f"Every finding cites path:line. Open {LEAF}. Run scripts/emperor diagnose "
        "to reprint this card."
    )
    lines.append(
        "MUST-NOT: invent numbers or findings; skip intake because 'obvious'; "
        "start analysis while partner is away; load whole diagnosing-superpowers "
        "(analyst prompts, templates, bundles, issue workflow). "
        "ET + emperor-heal remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_uncited() -> str:
    return (
        "REJECT UNCITED: HARD-GATE — no finding without a path:line citation. "
        "Every number must come from a transcript or a command you ran. "
        f"Open {LEAF}. Re-run scripts/emperor diagnose --check-citation \"...\".\n"
    )


def reject_skip_intake() -> str:
    return (
        "REJECT SKIP INTAKE: HARD-GATE — intake before analysis. "
        "Nothing in locate/triage/report starts until the human partner has "
        "answered. If they are away, write the questions and stop. "
        f"Open {LEAF}.\n"
    )


def check_citation(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when at least one path:line is present."""
    hits = CITATION_RE.findall(text or "")
    if hits:
        shown = ", ".join(f"{p}:{n}" for p, n in hits[:5])
        more = f" (+{len(hits) - 5} more)" if len(hits) > 5 else ""
        return True, f"CITE OK: found {len(hits)} citation(s): {shown}{more}\n"
    return (
        False,
        "CITE FAIL: no path:line citation in text. "
        f"Iron={IRON_CITE}. Drop the finding or add evidence. Open {LEAF}.\n",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time diagnosing HARD-GATE card "
            "for emperor-heal (intake + citation)."
        )
    )
    parser.add_argument(
        "--reject-uncited",
        action="store_true",
        help="Hard-gate: exit 1 when about to emit a finding without path:line",
    )
    parser.add_argument(
        "--reject-skip-intake",
        action="store_true",
        help="Hard-gate: exit 1 when about to analyze before partner intake",
    )
    parser.add_argument(
        "--check-citation",
        metavar="TEXT",
        default=None,
        help="Exit 0 if TEXT contains path:line; else exit 1 with CITE FAIL",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_uncited:
        sys.stdout.write(reject_uncited())
        return 1
    if args.reject_skip_intake:
        sys.stdout.write(reject_skip_intake())
        return 1
    if args.check_citation is not None:
        ok, msg = check_citation(args.check_citation)
        sys.stdout.write(msg)
        return 0 if ok else 1

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
