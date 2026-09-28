#!/usr/bin/env python3
"""Consent-gated PR forge (Python core).

Opens a PR only with explicit consent. Refuses if DONE probes fail.
Closes bash↔ps1 twin drift: forge.ps1 hardcoded title 'emperor-time change'
and dumped the entire ledger into PR.md; forge.sh extracted title + G1..G2.

Always-fail HARD-GATE helpers (forge-PR-specific; Steal owns --reject-no-consent):
  --reject-no-pr-consent   refuse public PR without PR consent
  --check-pr-consent PATH  exit 1 when forge/PR activity lacks consent
                           (vacuous PASS when no forge/PR activity)

Positional <task-dir> still forges. No args prints the FORGE card.
Thin twins: scripts/forge.sh / scripts/forge.ps1
G5 in gate.py calls --check-pr-consent (vacuous PASS when no forge markers).

Env:
  EMPEROR_CONSENT_PR=1  — consent without ledger quote
  EMPEROR_FORGE_DRY=1   — force dry-run (print gh command; never create)
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Sequence

LEAF = "skills/emperor-forge/SKILL.md"

_CONSENT_RE = re.compile(r"consent.*pr|open a pr|yes.*pr", re.IGNORECASE)
_TITLE_LINE_RE = re.compile(r"^# |Task:")

# Strong forge/PR signals — bare "forge" / "PR" alone is not enough.
# Note: EMPEROR_CONSENT_PR in prose also matches _CONSENT_RE (consent.*pr);
# that is intentional for positive consent files, so negative fixtures must
# not name the env var.
_FORGE_SIGNAL = re.compile(
    r"(?im)(?:"
    r"\bEMPEROR_CONSENT_PR\b"
    r"|\bscripts/emperor\s+forge\b"
    r"|\bscripts/lib/forge\.py\b"
    r"|\bscripts/forge\.sh\b"
    r"|\bopen(?:ing)?\s+a\s+PR\b"
    r"|\bpublic\s+PR\b"
    r"|\bcreate\s+(?:a\s+)?pull\s+request\b"
    r"|\bpull\s+request\b"
    r"|\bPR\s+consent\b"
    r"|\bconsent\s+(?:to\s+)?(?:a\s+)?PR\b"
    r"|\bPR\.md\b"
    r"|^#+\s*Forge\b"
    r"|\bDelivered as:\s*forge\b"
    r"|\bForge:\s*"
    r")"
)


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _combined_text(task_or_file: Path) -> str:
    if task_or_file.is_file():
        return _read(task_or_file)
    if not task_or_file.is_dir():
        return ""
    parts: list[str] = []
    for name in (
        "forge.md",
        "consent-pr.md",
        "pr-consent.md",
        "ledger.md",
        "PR.md",
        "DONE.md",
        "done.md",
        "claims.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
    return "\n".join(parts)


def _has_forge_signal(path: Path, text: str) -> bool:
    if path.is_file() and path.name.lower() in {
        "forge.md",
        "consent-pr.md",
        "pr-consent.md",
        "pr.md",
    }:
        return True
    if path.is_dir():
        for name in ("forge.md", "consent-pr.md", "pr-consent.md", "PR.md"):
            if (path / name).is_file():
                return True
    return bool(_FORGE_SIGNAL.search(text))


def has_consent(task: Path) -> bool:
    """True when EMPEROR_CONSENT_PR=1 or ledger quotes PR consent."""
    if os.environ.get("EMPEROR_CONSENT_PR") == "1":
        return True
    if task.is_file():
        return bool(_CONSENT_RE.search(_read(task)))
    ledger = task / "ledger.md" if task.is_dir() else None
    if ledger is not None and ledger.is_file():
        if _CONSENT_RE.search(_read(ledger)):
            return True
    # Also accept dedicated forge consent files
    if task.is_dir():
        for name in ("forge.md", "consent-pr.md", "pr-consent.md"):
            p = task / name
            if p.is_file() and _CONSENT_RE.search(_read(p)):
                return True
        text = _combined_text(task)
        return bool(_CONSENT_RE.search(text))
    return False


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


def validate_pr_consent(path: Path) -> list[str]:
    """Mechanical forge PR-consent checks. Vacuous PASS when no forge activity."""
    if not path.exists():
        return [f"missing path: {path}"]

    text = _combined_text(path)
    forge = _has_forge_signal(path, text)
    if not forge:
        # Vacuous PASS — no forge/PR activity claimed
        return []

    if has_consent(path):
        return []

    return [
        "missing PR consent "
        "(need EMPEROR_CONSENT_PR=1 or ledger quote matching "
        f"consent.*pr / open a pr / yes.*pr — see {LEAF})"
    ]


def format_card() -> str:
    lines = [
        "FORGE checklist=yes",
        f"FORGE leaf={LEAF}",
        "FORGE iron=PR_CONSENT_BEFORE_PUBLIC",
        "STEP 1 id=done name=DONE probes green "
        "et=scripts/emperor done <task-dir> exit 0",
        "STEP 1 key=Red or missing probes refuse forge",
        "STEP 2 id=g5 name=G5 verdict + breach honest "
        "et=scripts/emperor gate g5 <task-dir>",
        "STEP 2 key=FAIL is re-entry, not deliver",
        "STEP 3 id=consent name=PR consent quoted or EMPEROR_CONSENT_PR=1 "
        "et=client yes to public PR (not Steal enlistment CONSENT:)",
        "STEP 3 key=No consent → stop and ask; never invent a public PR",
        "STEP 4 id=forge name=scripts/emperor forge <task-dir> "
        "et=title + G1 + DONE body; DRY if gh missing",
        "STEP 4 key=HARD-GATE --reject-no-pr-consent / --check-pr-consent",
        "",
        "MUST: Before opening a public PR, quote client yes or set "
        f"EMPEROR_CONSENT_PR=1. Open {LEAF}; run "
        "scripts/emperor forge --check-pr-consent <task-dir>. "
        "Steal --reject-no-consent is a different gate (enlistment).",
        "MUST-NOT: open PR without consent; dump full ledger into PR body; "
        "treat Steal CONSENT: as PR consent; pretend gh succeeded when DRY.",
    ]
    return "\n".join(lines) + "\n"


def reject_no_pr_consent() -> str:
    return (
        "REJECT NO PR CONSENT: HARD-GATE — forge refuses public PR without "
        "EMPEROR_CONSENT_PR=1 or a quoted PR consent in the ledger "
        "(consent.*pr / open a pr / yes.*pr). "
        f"Open {LEAF}; re-run scripts/emperor forge --check-pr-consent "
        "<task-dir>. Steal enlistment uses consent.py --reject-no-consent "
        "(different gate).\n"
    )


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


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Consent-gated PR forge + forge PR-consent HARD-GATE "
            "(--reject-no-pr-consent / --check-pr-consent)"
        )
    )
    p.add_argument(
        "task_dir",
        type=Path,
        nargs="?",
        default=None,
        help="task directory to forge (omit with flags / for FORGE card)",
    )
    p.add_argument(
        "--check-pr-consent",
        type=Path,
        metavar="PATH",
        default=None,
        help="forge PR-consent check (exit 1 on soft/missing; vacuous OK)",
    )
    p.add_argument(
        "--reject-no-pr-consent",
        action="store_true",
        help="Hard-gate: refuse missing PR consent (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_no_pr_consent:
        sys.stdout.write(reject_no_pr_consent())
        return 1

    if args.check_pr_consent is not None:
        errs = validate_pr_consent(args.check_pr_consent)
        if errs:
            for e in errs:
                print(f"forge FAIL: {e}", file=sys.stderr)
            return 1
        print(f"forge PASS: {args.check_pr_consent}")
        return 0

    if args.task_dir is None:
        sys.stdout.write(format_card())
        return 0

    return forge(args.task_dir)


if __name__ == "__main__":
    raise SystemExit(main())
