#!/usr/bin/env python3
"""Git finish environment + integration menu (Python core).

Does not merge, push, or delete. Agent + client choose; forge still needs consent.

Superpowers finishing Step 1 runs the full suite BEFORE options. Menu-only
finish without a green suite is soft theater. HARD-GATE helpers close that:

  --reject-red-suite          always fail (refuse red-suite menu advance)
  --require-green [task-dir]  run done.py probes (and/or eval if present);
                              print ENV/MENU only when green; else refuse
  --check-suite PATH          suite check only (no menu)

Prefer integrating with done.py probes / eval.py when present — do not invent
a parallel suite runner.

Thin twins: scripts/finish.sh / scripts/finish.ps1 — same CLI.
Preserves finish.sh semantics (origin/HEAD base_guess fallback, worktree
kind, cleanup_owned, standard vs detached MENU) so bash/ps1 cannot drift.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Sequence

LEAF = "skills/emperor-forge/finish-menu.md"
SOURCE = (
    "obra/superpowers finishing-a-development-branch → Step 1 Verify Tests"
)


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def _run(args: list[str], *, cwd: str | Path | None = None) -> tuple[int, str]:
    try:
        p = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=False,
            cwd=str(cwd) if cwd else None,
        )
    except FileNotFoundError:
        return 127, ""
    out = (p.stdout or "") + (p.stderr or "")
    return p.returncode, out.strip() if isinstance(out, str) else out


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


def format_card() -> str:
    lines = [
        "FINISH checklist=yes",
        f"FINISH leaf={LEAF}",
        f"FINISH source={SOURCE}",
        "FINISH iron=NO_MENU_WITHOUT_GREEN_SUITE",
        "STEP 1 id=suite name=Fresh suite on this tree "
        "et=done.py probes and/or eval.py — quote the tail",
        "STEP 1 key=Prior green is rumor; red suite → stop; no menu",
        "STEP 2 id=detect name=Detect environment "
        "et=ENV kind/branch/head/worktree/base_guess/cleanup_owned",
        "STEP 2 key=Capture before any cd that leaves the worktree",
        "STEP 3 id=menu name=Present exactly one menu "
        "et=standard 3 options or detached 2 options",
        "STEP 3 key=Wait; do not assume PR; discard only on typed discard",
        "",
        "MUST: Before menu advance / claiming done, suite is green on this "
        f"tree. Open {LEAF}; run scripts/emperor finish --require-green "
        "<task-dir>. Done probes via done.py; eval.py when present.",
        "MUST-NOT: Menu-only finish on a red suite; skip Step 1; reuse an "
        "earlier green run as proof.",
    ]
    return "\n".join(lines) + "\n"


def reject_red_suite() -> str:
    return (
        "REJECT RED SUITE: HARD-GATE — finish refuses menu advance / done "
        "without a green suite on this tree. Menu-only finish is soft theater; "
        "Superpowers finishing Step 1 runs the full suite before options. "
        f"Open {LEAF}; run scripts/emperor finish --require-green <task-dir> "
        "(DONE probes via done.py) or with eval present; re-run until green.\n"
    )


def _run_done(task: Path) -> tuple[int, str]:
    py = _root() / "scripts" / "lib" / "done.py"
    return _run([sys.executable, str(py), str(task)])


def _run_eval() -> tuple[int, str]:
    """Run structural eval suite once. Skip if already inside eval (re-entry)."""
    if os.environ.get("EMPEROR_EVAL_RUNNING") == "1":
        return 0, "EVAL SKIP: already inside eval (re-entry guard)"
    py = _root() / "scripts" / "lib" / "eval.py"
    if not py.is_file():
        return 127, "eval.py missing"
    env = os.environ.copy()
    env["EMPEROR_EVAL_RUNNING"] = "1"
    try:
        p = subprocess.run(
            [sys.executable, str(py)],
            capture_output=True,
            text=True,
            check=False,
            env=env,
        )
    except FileNotFoundError:
        return 127, ""
    out = (p.stdout or "") + (p.stderr or "")
    return p.returncode, out


def check_suite(path: Path | None, *, use_eval: bool = False) -> list[str]:
    """Mechanical suite-green checks. Prefer done.py; eval when asked/present.

    PATH is a task directory (DONE.md) or a DONE.md file. When PATH is None
    and use_eval is True (or eval.py is the only available suite), run eval.
    """
    errors: list[str] = []
    root = _root()
    done_py = root / "scripts" / "lib" / "done.py"
    eval_py = root / "scripts" / "lib" / "eval.py"

    task: Path | None = None
    if path is not None:
        if path.is_file() and path.name == "DONE.md":
            task = path.parent
        elif path.is_dir():
            task = path
        else:
            return [f"missing task dir or DONE.md: {path}"]

    ran_something = False

    if task is not None:
        done_md = task / "DONE.md"
        if not done_md.is_file():
            errors.append(
                f"no DONE.md under {task} — cannot prove suite green "
                "(agent must define DONE probes; open done.py)"
            )
        elif not done_py.is_file():
            errors.append(f"done.py missing at {done_py}")
        else:
            ran_something = True
            rc, out = _run_done(task)
            if rc != 0:
                tail = "\n".join(out.splitlines()[-12:])
                errors.append(
                    f"DONE probes red (exit {rc}) — no menu until green"
                    + (f"\n{tail}" if tail else "")
                )

    # Prefer done probes; also run eval when explicitly requested or when
    # no task-dir was given and eval.py is present (project suite).
    want_eval = use_eval or (task is None and eval_py.is_file())
    if want_eval:
        if not eval_py.is_file():
            errors.append(f"eval.py missing at {eval_py}")
        else:
            ran_something = True
            rc, out = _run_eval()
            if rc != 0:
                # Keep message short — full eval log is noisy for finish.
                if "EVAL SKIP:" in out:
                    pass  # re-entry: treat as vacuous green for nested call
                else:
                    errors.append(
                        f"eval suite red (exit {rc}) — no menu until green"
                    )

    if not ran_something and not errors:
        errors.append(
            "no suite evidence — pass a task-dir with DONE.md (done.py) "
            "or ensure eval.py is present; refuse menu without a green proof"
        )
    return errors


def _print_menu() -> int:
    env, menu = detect()
    for line in render(env, menu):
        print(line)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Git finish ENV/MENU. HARD-GATE: refuse menu without green suite "
            "(Superpowers finishing Step 1)."
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="optional task dir (with --require-green / --check-suite)",
    )
    p.add_argument(
        "--reject-red-suite",
        action="store_true",
        help="Hard-gate: refuse red-suite menu advance (always exit 1)",
    )
    p.add_argument(
        "--require-green",
        action="store_true",
        help=(
            "Run done.py probes (and/or eval if present); print MENU only "
            "when green; else refuse"
        ),
    )
    p.add_argument(
        "--check-suite",
        type=Path,
        metavar="PATH",
        default=None,
        help="suite-green check only (exit 1 on red; no menu)",
    )
    p.add_argument(
        "--with-eval",
        action="store_true",
        help="also run eval.py when requiring/checking green",
    )
    p.add_argument(
        "--card",
        action="store_true",
        help="print FINISH checklist card (no menu)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_red_suite:
        sys.stdout.write(reject_red_suite())
        return 1

    if args.card:
        sys.stdout.write(format_card())
        return 0

    def _bump_verify(task: Path | None) -> list[str]:
        """Record verify cycle on real finish attempts; missing class → tiny.

        --check-suite is read-only (no ledger write) so probes / eval re-runs
        stay idempotent. --require-green still bumps (menu advance thrash).
        """
        if task is None or not task.is_dir():
            return []
        try:
            from proportionality import bump_and_check

            return bump_and_check(task, "verify")
        except Exception:
            return []

    if args.check_suite is not None:
        # Read-only probe — do not stamp effort-cycles.json.
        errs = check_suite(args.check_suite, use_eval=args.with_eval)
        if errs:
            for e in errs:
                print(f"finish FAIL: {e}", file=sys.stderr)
            return 1
        print(f"finish PASS: suite green ({args.check_suite})")
        return 0

    if args.require_green:
        target = args.path
        prop_errs = _bump_verify(target)
        if prop_errs:
            for e in prop_errs:
                print(f"finish FAIL: {e}", file=sys.stderr)
            return 1
        errs = check_suite(target, use_eval=args.with_eval)
        if errs:
            for e in errs:
                print(f"finish FAIL: {e}", file=sys.stderr)
            sys.stdout.write(reject_red_suite())
            return 1
        print("SUITE green=yes")
        if target is not None:
            print(f"SUITE via=done.py path={target}")
        elif args.with_eval or (_root() / "scripts/lib/eval.py").is_file():
            print("SUITE via=eval.py")
        return _print_menu()

    # Default: detect + menu (Step 2). Doctrine requires --require-green
    # before claiming done / menu advance; default stays usable for ENV probe.
    return _print_menu()


if __name__ == "__main__":
    raise SystemExit(main())
