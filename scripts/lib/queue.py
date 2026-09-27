#!/usr/bin/env python3
"""Local / GitHub / Linear work picker (Python core).

Read-only unless mutating local .emperor/queue.md (add/done/next promote).
Kanban statuses (WIP=1): [ ] ready · [~] active · [x] done · [!] blocked

Thin twins: scripts/queue.sh / scripts/queue.ps1
CLI: queue.py list|next|add|done [args]

Env:
  EMPEROR_QUEUE_FILE   — override queue path (default: <repo>/.emperor/queue.md)
  EMPEROR_QUEUE_SOURCE — auto|gh|linear|local (default: auto)
  LINEAR_API_KEY       — presence only; script never ships tokens
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

_CHECKBOX_OPEN = re.compile(r"^- \[([ ~!])\]")
_READY = re.compile(r"^- \[ \]")
_ACTIVE = re.compile(r"^- \[~\]")
_ANY_OPEN = re.compile(r"^- \[[ ~!]\]")
_PLACEHOLDER_BARE = re.compile(r"^- \[[ ~!]\] *$")
_PLACEHOLDER_PARENS = re.compile(r"^- \[[ ~!]\] +\(.*\) *$")

_DEFAULT_HEADER = (
    "# Emperor queue\n"
    "# WIP=1 — one [~] active at a time. Statuses: [ ] ready · [~] active"
    " · [x] done · [!] blocked\n"
    "#\n"
    "# Empty — add: - [ ] <task>  (or connect gh/Linear)."
    " Placeholder/parentheses-empty lines are ignored.\n"
    "\n"
    "Local backlog when GitHub issues / Linear are not connected.\n"
)


def _repo_root() -> Path:
    # scripts/lib/queue.py → repo root
    return Path(__file__).resolve().parent.parent.parent


def _queue_path() -> Path:
    override = os.environ.get("EMPEROR_QUEUE_FILE")
    if override:
        return Path(override)
    return _repo_root() / ".emperor" / "queue.md"


def _ensure_queue(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.is_file():
        path.write_text(_DEFAULT_HEADER, encoding="utf-8")


def is_placeholder(line: str) -> bool:
    """True when a checkbox line is an empty-queue placeholder, not real work."""
    if "(empty" in line:
        return True
    if _PLACEHOLDER_BARE.match(line):
        return True
    if _PLACEHOLDER_PARENS.match(line):
        return True
    return False


def _lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def _write_lines(path: Path, lines: list[str]) -> None:
    """Write lines; always end with a trailing newline (markdown / twin parity)."""
    body = "\n".join(lines)
    if not body.endswith("\n"):
        body = body + "\n"
    path.write_text(body, encoding="utf-8")


def list_open(path: Path) -> list[str]:
    out: list[str] = []
    for line in _lines(path):
        if _CHECKBOX_OPEN.match(line) and not is_placeholder(line):
            out.append(line)
    return out


def list_ready(path: Path) -> list[str]:
    out: list[str] = []
    for line in _lines(path):
        if _READY.match(line) and not is_placeholder(line):
            out.append(line)
    return out


def list_active(path: Path) -> list[str]:
    out: list[str] = []
    for line in _lines(path):
        if _ACTIVE.match(line) and not is_placeholder(line):
            out.append(line)
    return out


def promote_first_ready(path: Path) -> str | None:
    """Promote first non-placeholder [ ] → [~]. Returns new active line or None."""
    lines = _lines(path)
    promoted: str | None = None
    new_lines: list[str] = []
    for line in lines:
        if promoted is None and _READY.match(line) and not is_placeholder(line):
            promoted = re.sub(r"^- \[ \]", "- [~]", line, count=1)
            new_lines.append(promoted)
        else:
            new_lines.append(line)
    if promoted is None:
        return None
    _write_lines(path, new_lines)
    return promoted


def _have_gh() -> bool:
    return shutil.which("gh") is not None


def _in_git_worktree(root: Path) -> bool:
    try:
        p = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return False
    return p.returncode == 0


def _gh_issue_list(limit: int = 10) -> tuple[int, str]:
    try:
        p = subprocess.run(
            ["gh", "issue", "list", "--state", "open", "--limit", str(limit)],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return 127, ""
    out = p.stdout or ""
    return p.returncode, out


def _gh_next_item() -> str | None:
    try:
        p = subprocess.run(
            [
                "gh",
                "issue",
                "list",
                "--state",
                "open",
                "--limit",
                "1",
                "--json",
                "number,title",
                "--jq",
                '.[] | "#\\(.number) \\(.title)"',
            ],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return None
    if p.returncode != 0:
        return None
    item = (p.stdout or "").strip()
    return item or None


def cmd_list(path: Path) -> int:
    root = _repo_root()
    print(f"== local {path} ==")
    for line in list_open(path):
        print(line)
    if _have_gh() and _in_git_worktree(root):
        print("== gh issues (open, limit 10) ==")
        rc, out = _gh_issue_list(10)
        if rc != 0:
            print("gh issue list failed (auth or no remote)")
        elif out:
            sys.stdout.write(out if out.endswith("\n") else out + "\n")
    if os.environ.get("LINEAR_API_KEY"):
        print(
            "== Linear key present (not listing unless EMPEROR_QUEUE_SOURCE=linear) =="
        )
    return 0


def cmd_next(path: Path) -> int:
    src = os.environ.get("EMPEROR_QUEUE_SOURCE", "auto")
    if src in ("gh", "auto") and _have_gh():
        item = _gh_next_item()
        if item:
            print(f"NEXT gh: {item}")
            return 0
    if src == "linear" or (src == "auto" and os.environ.get("LINEAR_API_KEY")):
        print(
            "NEXT linear: key present — agent must query Linear with client consent; "
            "script will not ship tokens."
        )
        return 0
    # WIP=1: if an active task exists, return it — refuse a second active.
    active = list_active(path)
    if active:
        print(f"NEXT local (active): {active[0]}")
        print(
            "WIP=1: refuse second active — finish current or: queue done <substring>"
        )
        return 0
    ready = list_ready(path)
    if ready:
        promoted = promote_first_ready(path)
        if promoted:
            print(f"NEXT local: {promoted}")
            return 0
    print(f"NEXT none: queue empty. Add a line to {path} or pass a task.")
    return 2


def cmd_add(path: Path, text: str) -> int:
    if not text:
        print("usage: queue.py add <text>", file=sys.stderr)
        return 2
    with path.open("a", encoding="utf-8") as f:
        f.write(f"- [ ] {text}\n")
    print(f"QUEUED: {text}")
    return 0


def cmd_done(path: Path, pat: str) -> int:
    if not pat:
        print("usage: queue.py done <substring>", file=sys.stderr)
        return 2
    lines = _lines(path)
    hit = False
    new_lines: list[str] = []
    for line in lines:
        if not hit and _ANY_OPEN.match(line) and pat in line:
            hit = True
            new_lines.append(re.sub(r"^- \[[ ~!]\]", "- [x]", line, count=1))
        else:
            new_lines.append(line)
    _write_lines(path, new_lines)
    print(f"CHECKED: {pat}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    cmd = args[0] if args else "next"
    rest = args[1:] if args else []

    path = _queue_path()
    _ensure_queue(path)

    if cmd == "list":
        return cmd_list(path)
    if cmd == "next":
        return cmd_next(path)
    if cmd == "add":
        return cmd_add(path, " ".join(rest))
    if cmd == "done":
        return cmd_done(path, rest[0] if rest else "")
    print("usage: queue.py list|next|add|done", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
