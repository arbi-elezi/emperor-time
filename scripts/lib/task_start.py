#!/usr/bin/env python3
"""Record task BASE SHA + ensure brief (Python core).

Plan-scoped SDD task-start: extract/write the brief, record BASE
(`git rev-parse HEAD`) into the plan workspace, print `brief:` + `base:`.
Deepens execute/subagent from print-cards into mutating mechanics.

Does not vendor whole Superpowers prompts. Layout: `.emperor/sdd/<slug>/`.

Thin twins: scripts/task-start.sh / scripts/task-start.ps1
CLI: task_start.py <plan-file> <N>
Prints:
  brief: <path>
  base: <sha>
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from sdd_workspace import resolve as resolve_workspace
from task_brief import write_brief


def _git_rev(ref: str = "HEAD", cwd: Path | None = None) -> str | None:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", ref],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout.strip()
    except OSError:
        return None
    return None


def start_task(plan: Path, n: int) -> tuple[Path, str]:
    """Ensure brief + record BASE. Returns (brief_path, base_sha)."""
    if not plan.is_file():
        raise FileNotFoundError(f"no such plan file: {plan}")
    if n < 1:
        raise ValueError(f"task number must be >= 1, got {n}")

    ws = resolve_workspace(plan)
    brief = write_brief(plan, n)

    plan_repo = plan.resolve().parent
    base = _git_rev("HEAD", cwd=plan_repo)
    if not base:
        raise RuntimeError("not a git repo (cannot record BASE SHA)")

    base_path = ws / f"task-{n}-base"
    base_path.write_text(base + "\n", encoding="utf-8")

    # Mark in-progress in the progress ledger (create if needed).
    progress = ws / "progress.md"
    if not progress.is_file():
        plan_id = (ws / "plan-path").read_text(encoding="utf-8").strip()
        progress.write_text(
            f"# SDD progress\n"
            f"- plan: {plan_id}\n"
            f"\n",
            encoding="utf-8",
        )
    line = f"Task {n}: started base={base} brief={brief.name}\n"
    # Avoid duplicate started lines for the same task+base.
    existing = progress.read_text(encoding="utf-8")
    if line not in existing:
        with progress.open("a", encoding="utf-8") as fh:
            fh.write(line)

    return brief, base


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="SDD task-start: write brief + record BASE SHA"
    )
    ap.add_argument("plan_file", type=Path, help="path to work-order / plan")
    ap.add_argument("task_number", type=int, help="Task N (1-based)")
    args = ap.parse_args(argv)
    try:
        brief, base = start_task(args.plan_file, args.task_number)
    except (FileNotFoundError, ValueError, RuntimeError, OSError) as exc:
        print(f"task_start FAIL: {exc}", file=sys.stderr)
        return 2
    print(f"brief: {brief}")
    print(f"base: {base}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
