#!/usr/bin/env python3
"""Isolated review-pack emitter (Python core).

Emits SHAs + diff + acceptance criteria. No author CoT.
Closes bash↔ps1 twin drift: review-pack.ps1 copied the entire work-order
into criteria.md while review-pack.sh extracted only the
## Acceptance criteria section.

Thin twins: scripts/review-pack.sh / scripts/review-pack.ps1
CLI: review_pack.py <task-dir> [base] [head]
"""
from __future__ import annotations

import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def _in_git(cwd: Path | None = None) -> bool:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        return proc.returncode == 0 and proc.stdout.strip() == "true"
    except OSError:
        return False


def _git_rev(ref: str, cwd: Path | None = None) -> str | None:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", ref],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0:
            return proc.stdout.strip()
    except OSError:
        return None
    return None


def _git_diff(base: str, head: str, *, stat: bool = False, cwd: Path | None = None) -> str:
    args = ["git", "diff"]
    if stat:
        args.append("--stat")
    args.append(f"{base}..{head}")
    try:
        proc = subprocess.run(
            args,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        return proc.stdout
    except OSError:
        return ""


def extract_acceptance_criteria(work_order_text: str) -> str:
    """Match bash awk: from '^## Acceptance criteria' until next '^## ' heading.

    Inclusive of the Acceptance criteria heading; exclusive of the next ##.
    Returns empty string when the section is absent (bash awk empty output).
    """
    lines = work_order_text.splitlines()
    out: list[str] = []
    started = False
    for line in lines:
        if not started:
            if line.startswith("## Acceptance criteria"):
                started = True
                out.append(line)
            continue
        if line.startswith("## ") and not line.startswith("## Acceptance"):
            break
        out.append(line)
    return "\n".join(out) + ("\n" if out else "")


def emit_pack(task: Path, base: str = "HEAD~1", head: str = "HEAD") -> int:
    if not task.is_dir():
        print(f"missing {task}", file=sys.stderr)
        return 1
    out = task / "review-pack"
    out.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    meta_lines = [
        "# Isolated review pack",
        f"- task: {task}",
        f"- generated: {now}",
    ]
    if _in_git():
        base_sha = _git_rev(base) or base
        head_sha = _git_rev(head) or head
        meta_lines.append(f"- base: {base_sha}")
        meta_lines.append(f"- head: {head_sha}")
    else:
        meta_lines.append("- base/head: not a git repo")
    (out / "meta.md").write_text("\n".join(meta_lines) + "\n", encoding="utf-8")

    order = task / "work-order.md"
    if order.is_file():
        text = order.read_text(encoding="utf-8", errors="replace")
        criteria = extract_acceptance_criteria(text)
        (out / "criteria.md").write_text(criteria, encoding="utf-8")

    if _in_git():
        (out / "diff.patch").write_text(
            _git_diff(base, head), encoding="utf-8", errors="replace"
        )
        (out / "diffstat.txt").write_text(
            _git_diff(base, head, stat=True), encoding="utf-8", errors="replace"
        )

    claims = task / "claims.md"
    if claims.is_file():
        (out / "claims.md").write_text(
            claims.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    print(f"REVIEW PACK: {out}")
    for p in sorted(out.iterdir()):
        try:
            size = p.stat().st_size
        except OSError:
            size = 0
        print(f"{size:>8}  {p.name}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print(
            "usage: review_pack.py <task-dir> [base] [head]",
            file=sys.stderr,
        )
        return 2
    task = Path(args[0])
    base = args[1] if len(args) > 1 else "HEAD~1"
    head = args[2] if len(args) > 2 else "HEAD"
    return emit_pack(task, base, head)


if __name__ == "__main__":
    sys.exit(main())
