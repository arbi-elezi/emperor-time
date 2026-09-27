#!/usr/bin/env python3
"""Git finish environment + integration menu (Python core).

Does not merge, push, or delete. Agent + client choose; forge still needs consent.

Thin twins: scripts/finish.sh / scripts/finish.ps1 — same CLI:
  finish.py

Preserves finish.sh semantics (origin/HEAD base_guess fallback, worktree
kind, cleanup_owned, standard vs detached MENU) so bash/ps1 cannot drift.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


def _run(args: list[str]) -> tuple[int, str]:
    try:
        p = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return 127, ""
    out = (p.stdout or "").strip()
    return p.returncode, out


def _pwd_p(path: str) -> str:
    """Resolve like `cd … && pwd -P` (physical path)."""
    try:
        return str(Path(path).resolve())
    except OSError:
        return path


def detect() -> tuple[dict[str, str], str]:
    """Return (env_map, menu_kind) or exit 1 if not a git repo."""
    rc, _ = _run(["git", "rev-parse", "--is-inside-work-tree"])
    if rc != 0:
        print("FINISH FAIL: not a git repo", file=sys.stderr)
        raise SystemExit(1)

    _, git_dir_raw = _run(["git", "rev-parse", "--git-dir"])
    _, git_common_raw = _run(["git", "rev-parse", "--git-common-dir"])
    git_dir = _pwd_p(git_dir_raw)
    git_common = _pwd_p(git_common_raw)

    _, worktree_path = _run(["git", "rev-parse", "--show-toplevel"])
    rc_b, branch = _run(["git", "branch", "--show-current"])
    if rc_b != 0:
        branch = ""
    _, head_short = _run(["git", "rev-parse", "--short", "HEAD"])
    _, super_path = _run(["git", "rev-parse", "--show-superproject-working-tree"])

    kind = "normal"
    if super_path:
        kind = "normal"
    elif git_dir != git_common:
        kind = "worktree-named" if branch else "worktree-detached"

    base_guess = ""
    rc_m, _ = _run(["git", "rev-parse", "--verify", "origin/main"])
    if rc_m == 0:
        base_guess = "main"
    else:
        rc_s, _ = _run(["git", "rev-parse", "--verify", "origin/master"])
        if rc_s == 0:
            base_guess = "master"
        else:
            rc_h, href = _run(
                ["git", "symbolic-ref", "-q", "refs/remotes/origin/HEAD"]
            )
            if rc_h == 0 and href:
                base_guess = re.sub(r"^refs/remotes/origin/", "", href).strip()
    if not base_guess:
        base_guess = "main"

    # bash: [[ path == */.worktrees/* || path == */worktrees/* ]]
    wt = worktree_path.replace("\\", "/")
    if kind.startswith("worktree-") and (
        "/.worktrees/" in wt or "/worktrees/" in wt
    ):
        cleanup = "yes"
    else:
        cleanup = "no"

    env = {
        "kind": kind,
        "branch": branch if branch else "DETACHED",
        "head": head_short,
        "worktree": worktree_path,
        "base_guess": base_guess,
        "cleanup_owned": cleanup,
    }
    menu = "detached" if kind == "worktree-detached" else "standard"
    return env, menu


def render(env: dict[str, str], menu: str) -> list[str]:
    lines = [
        f"ENV kind={env['kind']}",
        f"ENV branch={env['branch']}",
        f"ENV head={env['head']}",
        f"ENV worktree={env['worktree']}",
        f"ENV base_guess={env['base_guess']}",
        f"ENV cleanup_owned={env['cleanup_owned']}",
        "",
    ]
    if menu == "detached":
        lines.append("MENU detached")
        lines.append(
            "Implementation complete. You're on a detached HEAD "
            "(externally managed workspace).\n"
            "\n"
            "1. Push as new branch and create a Pull Request\n"
            "2. Keep as-is (I'll handle it later)\n"
            "\n"
            "Which option?"
        )
    else:
        base = env["base_guess"]
        lines.append("MENU standard")
        lines.append(
            "Implementation complete. What would you like to do?\n"
            "\n"
            f"1. Merge back to {base} locally\n"
            "2. Push and create a Pull Request\n"
            "3. Keep the branch as-is (I'll handle it later)\n"
            "\n"
            "Which option?"
        )
    return lines


def main() -> int:
    env, menu = detect()
    for line in render(env, menu):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
