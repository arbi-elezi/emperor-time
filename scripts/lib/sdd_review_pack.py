#!/usr/bin/env python3
"""Plan-scoped BASE..HEAD review package into the SDD workspace (Python core).

Writes commit list + diffstat + full diff into
`.emperor/sdd/<slug>/review-<base>..<head>.diff`.

Guards (exit 3): BASE must be an ancestor of HEAD; range must be non-empty.
Use the BASE recorded by task-start — never HEAD~1 for multi-commit tasks.

Aspect adapted from obra/superpowers review-package (MIT) — range guards +
file emit only. Layout is ET: `.emperor/sdd/`. Companion to review_pack.py
(task-dir packs); this one is plan-scoped.

Thin twins: scripts/sdd-review-pack.sh / scripts/sdd-review-pack.ps1
CLI: sdd_review_pack.py <plan-file> <base> <head> [outfile]
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


def _run(cmd: list[str], *, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd, cwd=cwd, capture_output=True, text=True, check=False
    )


def _verify_ref(ref: str, cwd: Path | None = None) -> bool:
    p = _run(["git", "rev-parse", "--verify", "--quiet", ref], cwd=cwd)
    return p.returncode == 0


def _short(ref: str, cwd: Path | None = None) -> str:
    p = _run(["git", "rev-parse", "--short", ref], cwd=cwd)
    return p.stdout.strip() if p.returncode == 0 else ref[:12]


def emit_pack(
    plan: Path,
    base: str,
    head: str,
    outfile: Path | None = None,
) -> tuple[Path, int]:
    if not plan.is_file():
        raise FileNotFoundError(f"no such plan file: {plan}")
    plan_repo = plan.resolve().parent
    if not _verify_ref(base, cwd=plan_repo):
        raise ValueError(f"bad BASE: {base}")
    if not _verify_ref(head, cwd=plan_repo):
        raise ValueError(f"bad HEAD: {head}")

    anc = _run(
        ["git", "merge-base", "--is-ancestor", base, head], cwd=plan_repo
    )
    if anc.returncode != 0:
        raise RuntimeError(
            f"HEAD is not a descendant of BASE: {base}..{head}"
        )
    count_p = _run(
        ["git", "rev-list", "--count", f"{base}..{head}"], cwd=plan_repo
    )
    try:
        count = int(count_p.stdout.strip() or "0")
    except ValueError:
        count = 0
    if count <= 0:
        raise RuntimeError(f"empty commit range: {base}..{head}")

    if outfile is None:
        ws = resolve_workspace(plan)
        outfile = ws / (
            f"review-{_short(base, cwd=plan_repo)}.."
            f"{_short(head, cwd=plan_repo)}.diff"
        )
    else:
        outfile = Path(outfile)
        outfile.parent.mkdir(parents=True, exist_ok=True)

    log = _run(
        ["git", "log", "--oneline", f"{base}..{head}"], cwd=plan_repo
    ).stdout
    stat = _run(
        ["git", "diff", "--stat", f"{base}..{head}"], cwd=plan_repo
    ).stdout
    diff = _run(
        ["git", "diff", "-U10", f"{base}..{head}"], cwd=plan_repo
    ).stdout

    body = (
        f"# Review package: {base}..{head}\n"
        f"\n"
        f"## Commits\n"
        f"{log}"
        f"\n"
        f"## Files changed\n"
        f"{stat}"
        f"\n"
        f"## Diff\n"
        f"{diff}"
    )
    outfile.write_text(body, encoding="utf-8")
    return outfile.resolve(), count


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Plan-scoped BASE..HEAD review package into .emperor/sdd/"
    )
    ap.add_argument("plan_file", type=Path)
    ap.add_argument("base")
    ap.add_argument("head")
    ap.add_argument("outfile", type=Path, nargs="?", default=None)
    args = ap.parse_args(argv)
    try:
        path, count = emit_pack(
            args.plan_file, args.base, args.head, args.outfile
        )
    except FileNotFoundError as exc:
        print(f"sdd_review_pack FAIL: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(f"sdd_review_pack FAIL: {exc}", file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(f"sdd_review_pack FAIL: {exc}", file=sys.stderr)
        return 3
    size = path.stat().st_size
    print(f"wrote {path}: {count} commit(s), {size} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
