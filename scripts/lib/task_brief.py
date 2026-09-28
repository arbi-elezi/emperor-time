#!/usr/bin/env python3
"""Extract one plan task brief to a file (Python core).

Extracts `### Task N` / `## Task N` (any heading level matching Task N)
from a work-order/plan into a uniquely named brief file under the
plan-scoped SDD workspace. Exit ≠0 if the task is missing or empty.

Aspect adapted from obra/superpowers task-brief (MIT) — extract-to-file
only. Layout is ET: `.emperor/sdd/<slug>/`. Never vendors whole SP prompts.

Thin twins: scripts/task-brief.sh / scripts/task-brief.ps1
CLI: task_brief.py <plan-file> <N> [outfile]
Prints: brief: <path>
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in __import__('sys').path:
    __import__('sys').path.insert(0, str(_LIB))

from sdd_workspace import resolve as resolve_workspace

# Match AT any heading depth: "# Task 1", "### Task 2 — title", etc.
_TASK_HEAD = re.compile(
    r"^(#{1,6})[ \t]+Task[ \t]+(\d+)\b(.*)$",
    re.MULTILINE,
)


def extract_task(text: str, n: int) -> str:
    """Return the full text of Task N including its heading, or ''."""
    matches = list(_TASK_HEAD.finditer(text))
    target = None
    for i, m in enumerate(matches):
        if int(m.group(2)) == n:
            target = i
            break
    if target is None:
        return ""
    start = matches[target].start()
    # End at next Task heading of any depth (or EOF). Fence-aware: ignore
    # headings inside ``` fences so fenced examples do not truncate.
    rest = text[start:]
    # Walk line-by-line from just after the start heading.
    lines = rest.splitlines(keepends=True)
    out: list[str] = []
    in_fence = False
    for i, line in enumerate(lines):
        if i == 0:
            out.append(line)
            continue
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence:
            m = _TASK_HEAD.match(line.rstrip("\n"))
            if m is not None:
                break
        out.append(line)
    body = "".join(out).strip()
    return body + ("\n" if body else "")


def write_brief(
    plan: Path,
    n: int,
    outfile: Path | None = None,
) -> Path:
    """Extract Task N and write brief. Raises ValueError if missing/empty."""
    if not plan.is_file():
        raise FileNotFoundError(f"no such plan file: {plan}")
    if n < 1:
        raise ValueError(f"task number must be >= 1, got {n}")
    text = plan.read_text(encoding="utf-8", errors="replace")
    brief = extract_task(text, n)
    if not brief.strip():
        raise ValueError(
            f"task {n} not found in {plan} (no heading matching 'Task {n}')"
        )
    if outfile is None:
        ws = resolve_workspace(plan)
        outfile = ws / f"task-{n}-brief.md"
    else:
        outfile = Path(outfile)
        outfile.parent.mkdir(parents=True, exist_ok=True)
    outfile.write_text(brief, encoding="utf-8")
    if outfile.stat().st_size == 0:
        raise ValueError(f"task {n} brief is empty")
    return outfile.resolve()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Extract Task N from work-order/plan into a brief file"
    )
    ap.add_argument("plan_file", type=Path, help="path to work-order / plan")
    ap.add_argument("task_number", type=int, help="Task N (1-based)")
    ap.add_argument(
        "outfile",
        type=Path,
        nargs="?",
        default=None,
        help="optional outfile (default: .emperor/sdd/<slug>/task-N-brief.md)",
    )
    args = ap.parse_args(argv)
    try:
        path = write_brief(args.plan_file, args.task_number, args.outfile)
    except (FileNotFoundError, ValueError, OSError) as exc:
        print(f"task_brief FAIL: {exc}", file=sys.stderr)
        return 3 if "not found" in str(exc) or "empty" in str(exc) else 2
    print(f"brief: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
