#!/usr/bin/env python3
"""Isolated git worktree create helper (Python core).

Closes bash↔ps1 twin drift on the mutate path used after the isolation
HARD-GATE (`emperor iso` / worktree_iso.py). One core owns id/base resolve,
.worktrees layout, emperor/<id> branch, EXISTS short-circuit, and create.

Thin twins: scripts/worktree.sh / scripts/worktree.ps1
CLI: worktree.py <id> [base]

Does not replace the isolation checklist — run `emperor iso` first.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def _git(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
    )


def _inside_work_tree(cwd: Path | None = None) -> bool:
    cp = _git("rev-parse", "--is-inside-work-tree", cwd=cwd)
    return cp.returncode == 0 and cp.stdout.strip() == "true"


def create_worktree(
    task_id: str,
    base: str = "HEAD",
    *,
    cwd: Path | None = None,
) -> tuple[int, str, str]:
    """Create .worktrees/<id> on branch emperor/<id>.

    Returns (exit_code, stdout_body, stderr_body).
    """
    root = cwd if cwd is not None else Path.cwd()
    if not task_id:
        return 2, "", "usage: worktree.py <id> [base]\n"
    if not root.is_dir():
        return 1, "", "WORKTREE FAIL: not a git repo\n"
    if not _inside_work_tree(root):
        return 1, "", "WORKTREE FAIL: not a git repo\n"

    directory = root / ".worktrees" / task_id
    branch = f"emperor/{task_id}"
    (root / ".worktrees").mkdir(parents=True, exist_ok=True)

    if directory.is_dir():
        rel = f".worktrees/{task_id}"
        body = f"WORKTREE EXISTS: {rel}\n{rel}\n"
        return 0, body, ""

    cp = _git("worktree", "add", "-B", branch, str(directory), base, cwd=root)
    if cp.returncode != 0:
        err = (cp.stderr or cp.stdout or "git worktree add failed").rstrip() + "\n"
        return cp.returncode or 1, "", err

    rel = f".worktrees/{task_id}"
    return 0, f"WORKTREE: {rel}\n", ""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="worktree.py",
        description="Isolated git worktree for one swarm worker.",
    )
    ap.add_argument("id", nargs="?", default="", help="task / worker id")
    ap.add_argument("base", nargs="?", default="HEAD", help="git base (default HEAD)")
    ap.add_argument(
        "--cwd",
        default="",
        help="operate in this git root (eval / tests; default: process cwd)",
    )
    args = ap.parse_args(argv)

    cwd = Path(args.cwd) if args.cwd else None
    code, out, err = create_worktree(args.id, args.base, cwd=cwd)
    if out:
        sys.stdout.write(out)
    if err:
        sys.stderr.write(err)
    return code


if __name__ == "__main__":
    sys.exit(main())
