#!/usr/bin/env python3
"""Agent-defined DONE probes (Python core).

Exit 0 only if every probe:/expect: pair in <task-dir>/DONE.md matches.
A probe runs via bash -lc (same as done.sh). expect: is a substring match
on combined stdout+stderr. Empty expect always passes (parity with bash/ps1).

Thin twins: scripts/done.sh / scripts/done.ps1
CLI: done.py <task-dir>
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def _run_probe(cmd: str) -> str:
    """Run probe the way done.sh does: bash -lc, never raise on nonzero."""
    try:
        p = subprocess.run(
            ["bash", "-lc", cmd],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        # No bash: last-resort shell (should be rare on supported hosts).
        p = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=False,
        )
    out = (p.stdout or "") + (p.stderr or "")
    return out


def _tail(text: str, n: int = 8) -> str:
    lines = text.splitlines()
    return "\n".join(lines[-n:])


def evaluate(done_path: Path) -> int:
    """Parse DONE.md and run probes. Prints DONE PASS/FAIL/OK. Returns exit code."""
    text = done_path.read_text(encoding="utf-8", errors="replace")
    if not any(line.startswith("probe:") for line in text.splitlines()):
        print(f"DONE FAIL: no probes in DONE.md", file=sys.stderr)
        return 1

    fail = 0
    cmd: str | None = None
    expect = ""

    def flush() -> None:
        nonlocal fail, cmd, expect
        if not cmd:
            return
        out = _run_probe(cmd)
        # Empty expect: always pass (grep -F '' / PowerShell -and short-circuit).
        if expect == "" or expect in out:
            print(f"DONE PASS: {cmd}")
        else:
            print(f"DONE FAIL: {cmd}")
            print(f"  expected substring: {expect}")
            print(f"  got tail: {_tail(out)}")
            fail = 1
        cmd = None
        expect = ""

    for raw in text.splitlines():
        if raw.startswith("probe:"):
            flush()
            cmd = raw[len("probe:") :].lstrip()
            expect = ""
        elif raw.startswith("expect:"):
            expect = raw[len("expect:") :].lstrip()

    flush()
    if fail != 0:
        return 1
    print("DONE OK")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Agent-defined DONE. Exit 0 only if every probe matches."
    )
    ap.add_argument("task_dir", help="task directory containing DONE.md")
    args = ap.parse_args(argv)
    task = Path(args.task_dir)
    if not task.is_dir():
        print(f"usage: done.py <task-dir>", file=sys.stderr)
        return 2
    done = task / "DONE.md"
    if not done.is_file():
        print(
            f"DONE FAIL: no {done} (agent must define DONE)",
            file=sys.stderr,
        )
        return 1
    return evaluate(done)


if __name__ == "__main__":
    sys.exit(main())
