#!/usr/bin/env python3
"""Session transcript locate card for emperor-heal (Python core).

Leaf adapted from obra/superpowers skills/diagnosing-superpowers
references/session-discovery.md (MIT) — locate / verify-path aspect only.
Emperor Time + emperor-heal stay the orchestrator; do not announce
the foreign skill name. Does not vendor diagnosing-superpowers.

Prints SESSION / PATH / STATUS / MUST lines. Probes known harness
transcript locations when present. Marks VERIFIED only when the path
exists on disk. Read-only: never modifies session files.
--reject-guess exits non-zero when no verified path is available
(HARD-GATE helper for a future diagnosing leaf).
"""
from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

LEAF = "skills/emperor-heal/session-discovery.md"
SOURCE = (
    "obra/superpowers diagnosing-superpowers → "
    "references/session-discovery.md (locate aspect)"
)
IRON = "NO_SESSION_CLAIM_WITHOUT_VERIFIED_PATH"


@dataclass(frozen=True)
class Probe:
    kind: str
    path: Path | None
    status: str  # VERIFIED | ABSENT | UNVERIFIABLE
    reason: str


def _expand(raw: str) -> Path:
    return Path(os.path.expanduser(os.path.expandvars(raw))).resolve()


def _status_for(path: Path | None, *, expected: str) -> Probe:
    if path is None:
        return Probe(expected, None, "UNVERIFIABLE", "no candidate path constructed")
    if path.exists():
        kind = "dir" if path.is_dir() else "file"
        return Probe(expected, path, "VERIFIED", f"exists ({kind})")
    return Probe(expected, path, "ABSENT", "path does not exist on this host")


def _claude_project_dir(cwd: Path) -> Path:
    # Claude Code encodes absolute cwd as ~/.claude/projects/<dash-path>
    encoded = str(cwd).replace("/", "-")
    if not encoded.startswith("-"):
        encoded = "-" + encoded
    return Path.home() / ".claude" / "projects" / encoded


def _cursor_agent_roots(cwd: Path) -> list[tuple[str, Path]]:
    roots: list[tuple[str, Path]] = []
    env = os.environ.get("AGENT_TRANSCRIPTS", "").strip()
    if env:
        roots.append(("cursor-agent-env", _expand(env)))
    # Common Cursor / box layouts (probe; mark ABSENT if missing)
    roots.append(
        (
            "cursor-agent-cwd",
            Path.home() / ".cursor" / "projects" / cwd.name / "agent-transcripts",
        )
    )
    roots.append(
        ("cursor-sand-data", Path.home() / "sand-data" / "agent-transcripts")
    )
    # Dedupe by resolved path string while preserving order
    seen: set[str] = set()
    out: list[tuple[str, Path]] = []
    for kind, p in roots:
        key = str(p)
        if key in seen:
            continue
        seen.add(key)
        out.append((kind, p))
    return out


def collect_probes(
    *,
    session_id: str | None,
    explicit_path: str | None,
    cwd: Path,
) -> list[Probe]:
    probes: list[Probe] = []

    if explicit_path:
        p = _expand(explicit_path)
        if session_id and p.is_dir():
            # Prefer session-id child when dir + id given
            child = p / session_id
            if child.exists():
                probes.append(
                    Probe(
                        "explicit",
                        child.resolve(),
                        "VERIFIED",
                        f"exists under --path with session-id={session_id}",
                    )
                )
            else:
                base = _status_for(p, expected="explicit")
                probes.append(base)
                probes.append(
                    Probe(
                        "explicit-session",
                        child,
                        "ABSENT",
                        f"no child named {session_id} under --path",
                    )
                )
        else:
            probes.append(_status_for(p, expected="explicit"))

    # Claude Code projects root + cwd-encoded project
    claude_root = Path.home() / ".claude" / "projects"
    probes.append(_status_for(claude_root, expected="claude-projects-root"))
    probes.append(_status_for(_claude_project_dir(cwd), expected="claude-project-cwd"))

    if session_id and claude_root.is_dir():
        # Best-effort: look for *session_id* under projects (no content parse)
        hits = sorted(claude_root.rglob(f"*{session_id}*"))
        if hits:
            probes.append(
                Probe(
                    "claude-session-id",
                    hits[0].resolve(),
                    "VERIFIED",
                    f"name match under ~/.claude/projects ({len(hits)} hit(s); first shown)",
                )
            )
        else:
            probes.append(
                Probe(
                    "claude-session-id",
                    None,
                    "ABSENT",
                    f"no path name containing session-id under {claude_root}",
                )
            )

    for kind, root in _cursor_agent_roots(cwd):
        base = _status_for(root, expected=kind)
        probes.append(base)
        if session_id and root.is_dir():
            child = root / session_id
            jsonl = child / f"{session_id}.jsonl"
            if jsonl.exists():
                probes.append(
                    Probe(
                        f"{kind}-session",
                        jsonl.resolve(),
                        "VERIFIED",
                        "session jsonl exists",
                    )
                )
            elif child.exists():
                probes.append(
                    Probe(
                        f"{kind}-session",
                        child.resolve(),
                        "VERIFIED",
                        "session directory exists",
                    )
                )
            else:
                probes.append(
                    Probe(
                        f"{kind}-session",
                        child,
                        "ABSENT",
                        f"no session dir/file named {session_id}",
                    )
                )

    return probes


def format_card(
    *,
    session_id: str | None,
    cwd: Path,
    probes: list[Probe],
) -> str:
    verified = [p for p in probes if p.status == "VERIFIED"]
    lines = [
        "SESSION checklist=yes",
        f"SESSION leaf={LEAF}",
        f"SESSION source={SOURCE}",
        f"SESSION iron={IRON}",
        f"SESSION id={session_id if session_id else 'ABSENT (not supplied)'}",
        f"SESSION cwd={cwd}",
    ]
    for p in probes:
        path_s = str(p.path) if p.path is not None else "NONE"
        lines.append(
            f"PATH kind={p.kind} status={p.status} path={path_s} reason={p.reason}"
        )

    if verified:
        lines.append(
            f"STATUS summary=VERIFIED_PATHS count={len(verified)} "
            f"first={verified[0].path}"
        )
    else:
        lines.append(
            "STATUS summary=NO_VERIFIED_PATH "
            "reason=no probed harness location exists for this host/args"
        )

    lines.append("")
    lines.append(
        "MUST: Resolve sessions to absolute filesystem paths before citing "
        "history. Expand ~ and env vars. Confirm identity with session id, "
        "cwd, timestamps, or matching content — recency alone is not "
        f"confirmation. Open {LEAF} and run scripts/emperor session-discovery "
        "to reprint this card. Record rejected candidates."
    )
    lines.append(
        "MUST-NOT: invent transcript contents or numbers; claim a session "
        "without a VERIFIED path; modify/move/delete session files; load "
        "whole diagnosing-superpowers. ET + emperor-heal remain the "
        "orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_guess() -> str:
    return (
        "REJECT GUESS: HARD-GATE — no session claim without a VERIFIED "
        "filesystem path. Supply --path and/or --session-id, or re-run "
        "scripts/emperor session-discovery until STATUS summary=VERIFIED_PATHS. "
        f"Open {LEAF}.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time session-discovery locate card "
            "for emperor-heal (read-only probes)."
        )
    )
    parser.add_argument(
        "--session-id",
        "-i",
        default=None,
        help="Session id to match under known harness roots",
    )
    parser.add_argument(
        "--path",
        "-p",
        default=None,
        help="Explicit transcript file or directory (verified if exists)",
    )
    parser.add_argument(
        "--cwd",
        default=None,
        help="Working directory hint for harness project encoding (default: pwd)",
    )
    parser.add_argument(
        "--reject-guess",
        action="store_true",
        help="Hard-gate: exit 1 when no VERIFIED path is available",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_guess:
        # House pattern (receive/evidence): reject-* is an always-fail HARD-GATE
        # the caller invokes when about to claim a session without a verified path.
        sys.stdout.write(reject_guess())
        return 1

    cwd = _expand(args.cwd) if args.cwd else Path.cwd().resolve()
    probes = collect_probes(
        session_id=args.session_id,
        explicit_path=args.path,
        cwd=cwd,
    )
    sys.stdout.write(
        format_card(session_id=args.session_id, cwd=cwd, probes=probes)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
