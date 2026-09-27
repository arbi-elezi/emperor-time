#!/usr/bin/env python3
"""Deploy Emperor Time into a harness skill directory (Python core).

Closes bash↔ps1 twin drift: install.ps1 previewed chain destinations before
copy / dry-run; install.sh listed them only after copy. First-run tip also
diverged (dowse.sh vs dowse.ps1). One core owns harness map, copy set,
chain expose, activation tips, and dry-run.

Thin twins: scripts/install.sh / scripts/install.ps1
CLI: install.py <harness> [scope] [project-path] [--with-chain-skills] [--dry-run]

Harnesses: claude-code | kimi | codex | opencode | generic-agents
Scope: user (default) | project
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

HARNESSES: dict[str, tuple[str, str | None]] = {
    # (user_dir relative to home, project_dir relative to project root or None)
    "claude-code": (".claude/skills", ".claude/skills"),
    "kimi": (".kimi/skills", ".kimi/skills"),
    "codex": (".codex/skills", ".codex/skills"),
    "opencode": (".opencode/skills", None),
    "generic-agents": (".config/agents/skills", ".agents/skills"),
}

ITEMS: tuple[str, ...] = (
    "SKILL.md",
    "README.md",
    "chains",
    "references",
    "templates",
    "adapters",
    "scripts",
)

CHAINS: tuple[str, ...] = (
    "dowsing-chain",
    "chain-jail",
    "judgment-chain",
    "steal-chain",
    "holy-chain",
)

ACTIVATE: dict[str, str] = {
    "claude-code": (
        'Activate: say "emperor time" in Claude Code '
        "(or let the description auto-trigger)."
    ),
    "kimi": "Activate: /skill:emperor-time inside a kimi session.",
    "codex": "Activate: per Codex skill activation - verify with `codex --help`.",
    "opencode": (
        "Activate: opencode run --skill emperor-time "
        "(verify flag; see adapters/opencode/)."
    ),
    "generic-agents": (
        "Activate: any Agent-Skills-compatible harness reading "
        "~/.config/agents/skills/."
    ),
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _home() -> Path:
    return Path.home()


def resolve_dest(
    harness: str, scope: str, project: str
) -> tuple[Path, Path]:
    """Return (dest_root, dest) where dest is dest_root/emperor-time."""
    if harness not in HARNESSES:
        raise ValueError(f"unknown harness: {harness}")
    user_rel, proj_rel = HARNESSES[harness]
    if scope == "project":
        if proj_rel is None:
            raise ValueError(
                f"harness '{harness}' has no documented project-level "
                "skills dir - use scope 'user'"
            )
        project_root = Path(project).resolve()
        dest_root = project_root / proj_rel
    elif scope == "user":
        dest_root = _home() / user_rel
    else:
        raise ValueError(f"unknown scope: {scope} (want user|project)")
    return dest_root, dest_root / "emperor-time"


def _copy_tree(src: Path, dest: Path) -> None:
    if src.is_dir():
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)


def install(
    harness: str,
    *,
    scope: str = "user",
    project: str = ".",
    with_chains: bool = False,
    dry_run: bool = False,
    repo_root: Path | None = None,
) -> int:
    root = repo_root if repo_root is not None else _repo_root()
    try:
        dest_root, dest = resolve_dest(harness, scope, project)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print()
    print("=== EMPEROR TIME :: install ===")
    print(f"  source : {root}")
    print(f"  target : {dest}")
    if harness == "claude-code" and scope == "user":
        print(
            "  note   : Kimi CLI reads ~/.claude/skills/ too - "
            "this install covers both."
        )
    if dry_run:
        if with_chains:
            for c in CHAINS:
                print(f"  chain  : {dest_root / c} (planned)")
        print("  (dry run - nothing copied)")
        return 0

    dest.mkdir(parents=True, exist_ok=True)
    for item in ITEMS:
        src = root / item
        if src.exists():
            _copy_tree(src, dest / item)

    if with_chains:
        for c in CHAINS:
            src = root / "chains" / c
            if src.is_dir():
                _copy_tree(src, dest_root / c)
                print(f"  chain  : {dest_root / c}")

    print()
    print("Installed.")
    print(ACTIVATE[harness])
    print(
        "First run: execute `scripts/emperor dowse` "
        "(or scripts/dowse.sh / scripts/dowse.ps1) to build the agent roster."
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Deploy Emperor Time into a harness skill directory."
    )
    ap.add_argument(
        "harness",
        choices=sorted(HARNESSES.keys()),
        help="target harness",
    )
    ap.add_argument(
        "scope",
        nargs="?",
        default="user",
        choices=("user", "project"),
        help="user (default) or project",
    )
    ap.add_argument(
        "project",
        nargs="?",
        default=".",
        help="project path when scope=project (default: .)",
    )
    ap.add_argument(
        "--with-chain-skills",
        action="store_true",
        help="also expose each chain as its own top-level skill",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="print plan; copy nothing",
    )
    args = ap.parse_args(argv)
    # Positional flags after harness can be mistaken for scope/project when
    # callers pass only flags (bash loop previously remapped --* away).
    scope = args.scope
    project = args.project
    if scope.startswith("--"):
        scope = "user"
    if project.startswith("--"):
        project = "."
    return install(
        args.harness,
        scope=scope,
        project=project,
        with_chains=args.with_chain_skills,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    raise SystemExit(main())
