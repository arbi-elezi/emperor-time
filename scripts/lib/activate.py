#!/usr/bin/env python3
"""SessionStart MUST-route activation card (Python core).

Leaf adapted from obra/superpowers skills/using-superpowers
"if even a 1% chance a skill applies → MUST invoke" (MIT).
Emperor Time stays the orchestrator; do not announce a foreign skill name.

Detects disk state and optional utterance; prints ACTIVATION / MUST lines.
Does not mutate the tree. Route still owns utterance→skill matching.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_NEXT = "skills/emperor-resume/SKILL.md"
LEAF = "skills/emperor-resume/must-route.md"


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _state_next(cwd: Path) -> str:
    """Pick default skill from on-disk factory state (no model)."""
    state = cwd / ".emperor" / "state.md"
    body = _read_text(state).casefold()
    if body:
        if re.search(r"\b(red|derail|heal|failing)\b", body):
            return "skills/emperor-heal/SKILL.md"
        if re.search(r"\b(g4|verify|critique)\b", body):
            return "skills/emperor-verify/SKILL.md"
        if re.search(r"\b(forge|pr|ship|finish)\b", body):
            return "skills/emperor-forge/SKILL.md"
        if re.search(r"\b(g3|build|implement)\b", body):
            return "skills/emperor-build/SKILL.md"
        if re.search(r"\b(g2|work-?order|design)\b", body):
            return "skills/emperor-require-design/SKILL.md"
        if re.search(r"\b(g0|dowse|scope|intake)\b", body):
            return "skills/emperor-scope/SKILL.md"
        return DEFAULT_NEXT

    queue = cwd / ".emperor" / "queue.md"
    q = _read_text(queue)
    if re.search(r"^- \[~\]", q, re.M):
        return "skills/emperor-queue/SKILL.md"
    if re.search(r"^- \[ \] .\S", q, re.M) and "(empty" not in q.casefold():
        return "skills/emperor-queue/SKILL.md"

    survey = _read_text(cwd / ".emperor" / "survey.md").casefold()
    if re.search(r"\b(pascal|\.pas|assembly|\.asm|cobol|rom)\b", survey):
        return "skills/emperor-excavate/SKILL.md"

    return DEFAULT_NEXT


def _route_utterance(utterance: str, triggers_path: Path) -> str | None:
    """Mirror route.sh first-match; return target path or None."""
    if not utterance.strip() or not triggers_path.is_file():
        return None
    try:
        data = json.loads(triggers_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    text = utterance.casefold()
    for route in data.get("routes") or []:
        patterns = list(route.get("patterns") or []) + list(route.get("tags") or [])
        for pattern in patterns:
            p = str(pattern).casefold().strip()
            if not p:
                continue
            if len(p) <= 3 or p.startswith(".") or p.endswith(" "):
                if re.search(rf"(?<!\w){re.escape(p.strip())}(?!\w)", text):
                    return str(route.get("target") or "") or None
            elif p in text:
                return str(route.get("target") or "") or None
    return None


def format_card(*, next_skill: str, source: str, utterance: str | None) -> str:
    lines = [
        "ACTIVATION must_route=yes",
        "ACTIVATION rule=skill_applies_must_invoke",
        f"ACTIVATION leaf={LEAF}",
        f"ACTIVATION default={DEFAULT_NEXT}",
        f"ACTIVATION next={next_skill}",
        f"ACTIVATION source={source}",
    ]
    if utterance:
        lines.append(f"ACTIVATION utterance={utterance.strip()[:120]}")
    lines.append("")
    lines.append(
        "MUST: Before clarifying questions or exploring the tree, open "
        f"{next_skill} (or run scripts/emperor route \"<utterance>\"). "
        "If even a small chance a phase skill applies, invoke it. "
        "Do not wait for the client to say 'emperor time'."
    )
    lines.append(
        "MUST: Before setup thrash, emit ask→spec "
        "(scripts/emperor ask-spec --emit \"<ask>\" --write "
        ".emperor/tasks/<id>/ask-spec.md). G0 "
        "calls --require-spec — setup without a written spec FAILS."
    )
    lines.append(
        "MUST: After ask→spec, emit harness plan "
        "(scripts/emperor harness-plan --emit --from "
        ".emperor/tasks/<id> --write "
        ".emperor/tasks/<id>/harness-plan.md). Harness owns "
        "tool+force from effort_class. G0 --require-plan FAILS without a plan."
    )
    lines.append(
        "MUST-NOT: load using-superpowers or another master router; "
        "ET remains the orchestrator (see must-route.md)."
    )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print Emperor Time SessionStart MUST-route activation card."
    )
    parser.add_argument(
        "--cwd",
        default=".",
        help="Repo root to inspect for .emperor state (default: .)",
    )
    parser.add_argument(
        "--utterance",
        "-u",
        default="",
        help="Optional user utterance to route before disk defaults",
    )
    parser.add_argument(
        "--triggers",
        default=str(ROOT / "evals" / "triggers.json"),
        help="triggers.json path for utterance routing",
    )
    args = parser.parse_args(argv)
    cwd = Path(args.cwd).resolve()

    source = "disk"
    next_skill = _state_next(cwd)
    if args.utterance.strip():
        routed = _route_utterance(args.utterance, Path(args.triggers))
        if routed:
            next_skill = routed
            source = "utterance"

    sys.stdout.write(
        format_card(next_skill=next_skill, source=source, utterance=args.utterance or None)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
