#!/usr/bin/env python3
"""Consent-gated PR forge (Python core).

Opens a PR only with explicit consent. Refuses if DONE probes fail.
Closes bash↔ps1 twin drift: forge.ps1 hardcoded title 'emperor-time change'
and dumped the entire ledger into PR.md; forge.sh extracted title + G1..G2.

Thin twins: scripts/forge.sh / scripts/forge.ps1
CLI: forge.py <task-dir>

Env:
  EMPEROR_CONSENT_PR=1  — consent without ledger quote
  EMPEROR_FORGE_DRY=1   — force dry-run (print gh command; never create)
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

_CONSENT_RE = re.compile(r"consent.*pr|open a pr|yes.*pr", re.IGNORECASE)
_TITLE_LINE_RE = re.compile(r"^# |Task:")


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def has_consent(task: Path) -> bool:
    if os.environ.get("EMPEROR_CONSENT_PR") == "1":
        return True
    ledger = task / "ledger.md"
    if not ledger.is_file():
        return False
    text = ledger.read_text(encoding="utf-8", errors="replace")
    return bool(_CONSENT_RE.search(text))


def extract_title(ledger_text: str) -> str:
    """Match forge.sh: first '^# ' or 'Task:' line, strip '# ' then '.*Task: '."""
    for line in ledger_text.splitlines():
        if _TITLE_LINE_RE.search(line):
            t = re.sub(r"^# ", "", line, count=1)
            t = re.sub(r"^.*Task:\s*", "", t, count=1)
            t = t.strip()
            return t or "emperor-time change"
    return "emperor-time change"


def extract_g1_section(ledger_text: str) -> str:
    """Match sed -n '/G1/,/G2/p' — inclusive range."""
    lines = ledger_text.splitlines()
    out: list[str] = []
    started = False
    for line in lines:
        if not started:
            if re.search(r"G1", line):
                started = True
                out.append(line)
                if re.search(r"G2", line):
                    break
        else:
            out.append(line)
            if re.search(r"G2", line):
                break
    return "\n".join(out)


def _run_done(task: Path) -> int:
    py = _root() / "scripts" / "lib" / "done.py"
    proc = subprocess.run(
        [sys.executable, str(py), str(task)],
        check=False,
    )
    return proc.returncode


def write_pr_body(task: Path) -> tuple[str, Path]:
    """Write PR.md from G1 section + DONE probes. Returns (title, body_path)."""
    ledger = task / "ledger.md"
    ledger_text = (
        ledger.read_text(encoding="utf-8", errors="replace")
        if ledger.is_file()
        else ""
    )
    title = extract_title(ledger_text) if ledger_text else "emperor-time change"
    g1 = extract_g1_section(ledger_text) if ledger_text else ""
    done_path = task / "DONE.md"
    done_text = (
        done_path.read_text(encoding="utf-8", errors="replace")
        if done_path.is_file()
        else ""
    )
    parts = ["## G1"]
    if g1:
        parts.append(g1)
    parts.append("")
    parts.append("## DONE probes")
    if done_text:
        parts.append(done_text.rstrip("\n"))
    parts.append("")
    body = task / "PR.md"
    body.write_text("\n".join(parts), encoding="utf-8")
    return title, body


def _shell_quote(s: str) -> str:
    """Bash-style single-quote (parity with printf %q for simple paths/titles)."""
    return "'" + s.replace("'", "'\\''") + "'"


def forge(task: Path) -> int:
    if not task.is_dir():
        print("usage: forge.py <task-dir>", file=sys.stderr)
        return 2
    if not has_consent(task):
        print(
            "FORGE REFUSED: no EMPEROR_CONSENT_PR=1 and no quoted PR consent "
            "in ledger.md",
            file=sys.stderr,
        )
        return 3
    rc = _run_done(task)
    if rc != 0:
        return rc
    title, body = write_pr_body(task)
    force_dry = os.environ.get("EMPEROR_FORGE_DRY") == "1"
    no_gh = shutil.which("gh") is None
    if force_dry or no_gh:
        why = "EMPEROR_FORGE_DRY=1" if force_dry else "gh not installed"
        print(f"FORGE DRY: {why}. Client runs:")
        print(
            f"  gh pr create --title {_shell_quote(title)} "
            f"--body-file {_shell_quote(str(body))}"
        )
        return 0
    proc = subprocess.run(
        ["gh", "pr", "create", "--title", title, "--body-file", str(body)],
        check=False,
    )
    return proc.returncode


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("usage: forge.py <task-dir>", file=sys.stderr)
        return 2
    return forge(Path(args[0]))


if __name__ == "__main__":
    sys.exit(main())
