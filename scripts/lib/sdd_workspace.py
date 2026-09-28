#!/usr/bin/env python3
"""Plan-scoped SDD workspace resolver (Python core).

Resolves/creates `.emperor/sdd/<plan-slug>/` for one plan's short-lived
artifacts: task briefs, BASE markers, progress ledger, review packages.
Two plans → two dirs. Basename collisions disambiguate via parent dir then
counter. Each workspace records its owning plan in a `plan-path` marker.
Writes `.emperor/sdd/.gitignore` with `*` so the workspace is self-ignoring
(even if a host un-ignores `.emperor/`).

Aspect adapted from obra/superpowers sdd-workspace (MIT) — plan-scoping +
marker + self-ignore only. Layout is ET: `.emperor/sdd/` (NOT `.superpowers/`).
Never vendors whole Superpowers prompts/templates.

Thin twins: scripts/sdd-workspace.sh / scripts/sdd-workspace.ps1
CLI: sdd_workspace.py <plan-file>
Prints the absolute workspace path.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def _git_root(cwd: Path | None = None) -> Path | None:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0 and proc.stdout.strip():
            return Path(proc.stdout.strip()).resolve()
    except OSError:
        return None
    return None


def _plan_id(plan: Path, root: Path) -> str:
    plan_abs = plan.resolve()
    try:
        return str(plan_abs.relative_to(root))
    except ValueError:
        return str(plan_abs)


def _owns(workspace: Path, plan_id: str) -> bool:
    """True when workspace is (or becomes) this plan's."""
    marker = workspace / "plan-path"
    if marker.is_file():
        return marker.read_text(encoding="utf-8").strip() == plan_id
    workspace.mkdir(parents=True, exist_ok=True)
    marker.write_text(plan_id + "\n", encoding="utf-8")
    return True


def resolve(plan: Path, *, cwd: Path | None = None) -> Path:
    """Resolve/create plan-scoped SDD workspace. Returns absolute path."""
    if not plan.is_file():
        raise FileNotFoundError(f"no such plan file: {plan}")

    # Prefer the plan's own git root so evals / worktrees resolve correctly
    # even when process cwd is a different repo.
    root = (
        _git_root(plan.resolve().parent)
        or _git_root(cwd)
        or (cwd or Path.cwd()).resolve()
    )
    base = root / ".emperor" / "sdd"
    base.mkdir(parents=True, exist_ok=True)
    # Self-ignore: keep every plan workspace out of accidental commits.
    gi = base / ".gitignore"
    if not gi.is_file() or gi.read_text(encoding="utf-8").strip() != "*":
        gi.write_text("*\n", encoding="utf-8")

    plan_abs = plan.resolve()
    slug = plan_abs.stem
    if not slug or slug in (".", ".."):
        raise ValueError(f"cannot derive a workspace name from: {plan}")

    plan_id = _plan_id(plan_abs, root)
    candidate = base / slug
    if not _owns(candidate, plan_id):
        parent = plan_abs.parent.name or "plan"
        candidate = base / f"{slug}-{parent}"
        if not _owns(candidate, plan_id):
            n = 2
            while True:
                candidate = base / f"{slug}-{parent}-{n}"
                if _owns(candidate, plan_id):
                    break
                n += 1

    return candidate.resolve()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Resolve/create plan-scoped .emperor/sdd/<slug>/ workspace"
    )
    ap.add_argument("plan_file", type=Path, help="path to work-order / plan file")
    args = ap.parse_args(argv)
    try:
        ws = resolve(args.plan_file)
    except (FileNotFoundError, ValueError, OSError) as exc:
        print(f"sdd_workspace FAIL: {exc}", file=sys.stderr)
        return 2
    print(ws)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
