#!/usr/bin/env python3
"""Validate Emperor Time Holy process-healing register + re-entry.

Doctrine: chains/holy-chain/process-healing.md — repair breakage in the
discipline (skipped gates, bad admissions, delivered falsehoods, derailed
waterfalls). Output: breach processed (register + remediation + disclosure
where owed) and the loop re-entered at the earliest sound gate.

Always-fail HARD-GATE helpers:
  --reject-no-register    refuse process-heal without register entry
  --reject-no-reentry     refuse process-heal without RE-ENTERED seam

Check mode:
  --check-process-heal PATH   task dir or process-heal/ledger file
                              (exit 1 on soft / missing register or re-entry)

Positional PATH runs the same check. No args prints the PROCESS-HEAL card.
Thin twins: scripts/process-heal.sh / scripts/process-heal.ps1
Alias: process-healing → same core.
Vacuous PASS when no process-healing activity is claimed.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence

LEAF = "chains/holy-chain/process-healing.md"

# Strong process-healing signals — weak "breach" alone is not enough.
_PROCESS_SIGNAL = re.compile(
    r"(?i)\b("
    r"holy\s+process(?:-healing)?"
    r"|process-healing"
    r"|process\s+healing"
    r"|skipped\s+gate"
    r"|gate\s+was\s+skipped"
    r"|waterfall\s+derailed"
    r"|bad\s+admission"
    r"|delivered\s+falsehood"
    r"|systemic\s+drift"
    r"|RE-ENTERED\s+G[0-5]"
    r"|re-enter(?:ed)?\s+at\s+G[0-5]"
    r")\b"
)

# Register entry: Breach Register row or explicit register fields.
_REGISTER = re.compile(
    r"(?i)(?<!\w)("
    r"Breach\s+Register\s*:"
    r"|Register\s*(?:entry)?\s*:"
    r"|register\s+entry\s*:"
    r"|\|\s*Vow\s*\|[^\n]{0,200}\|\s*\S"
    r"|Vow\s*[1-6]\s*:\s*\S.+?(?:remediat|lesson|discovered)"
    r"|Stake\s*:\s*\S"
    r"|what\s+happened\s*:\s*\S.+?remediat"
    r")"
)

# Re-entry seam: RE-ENTERED Gn <date> (breach #N) or equivalent.
_REENTRY = re.compile(
    r"(?i)(?<!\w)("
    r"RE-ENTERED\s+G[0-5]\b"
    r"|re-entered\s+G[0-5]\b"
    r"|re-enter(?:ed)?\s+at\s+G[0-5]\b"
    r"|re-enter(?:ed)?\s+at\s+(?:the\s+)?earliest\s+(?:sound\s+)?gate"
    r"|ledger\s+seam\s*:\s*RE-ENTERED"
    r"|re-entry\s*:\s*G[0-5]\b"
    r")"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _combined_text(task_or_file: Path) -> str:
    if task_or_file.is_file():
        return _read(task_or_file)
    if not task_or_file.is_dir():
        return ""
    parts: list[str] = []
    for name in (
        "process-heal.md",
        "process-healing.md",
        "breach.md",
        "register.md",
        "ledger.md",
        "claims.md",
        "claim-ledger.md",
        "DONE.md",
        "done.md",
        "admission.md",
        "heal.md",
        "triage.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
    return "\n".join(parts)


def _has_process_signal(path: Path, text: str) -> bool:
    if path.is_file() and path.name.lower() in {
        "process-heal.md",
        "process-healing.md",
    }:
        return True
    if path.is_dir() and (
        (path / "process-heal.md").is_file()
        or (path / "process-healing.md").is_file()
    ):
        return True
    return bool(_PROCESS_SIGNAL.search(text))


def _register_errors(text: str) -> list[str]:
    if _REGISTER.search(text):
        return []
    return [
        "missing register entry "
        f"(need Breach Register:/Register:/| Vow | row — see {LEAF})"
    ]


def _reentry_errors(text: str) -> list[str]:
    if _REENTRY.search(text):
        return []
    return [
        "missing RE-ENTERED seam "
        "(need RE-ENTERED G[0-5] / re-enter at G[0-5] / earliest sound gate "
        f"— see {LEAF})"
    ]


def validate(path: Path) -> list[str]:
    """Mechanical process-healing checks for a task dir / ledger file."""
    if not path.exists():
        return [f"missing path: {path}"]

    text = _combined_text(path)
    active = _has_process_signal(path, text)
    if not active:
        # Vacuous PASS — no process-healing activity to close
        if path.is_file() and path.name.lower() in {
            "process-heal.md",
            "process-healing.md",
        }:
            return _register_errors(text) + _reentry_errors(text)
        return []

    errors = _register_errors(text) + _reentry_errors(text)
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "PROCESS-HEAL checklist=yes",
        f"PROCESS-HEAL leaf={LEAF}",
        "PROCESS-HEAL iron=REGISTER_THEN_REENTER",
        "STEP 1 id=declare name=Register the wound "
        "et=Stake register entry — no narrative padding",
        "STEP 1 key=Breach Register: Vow | what happened | remediation",
        "STEP 2 id=earliest name=Find earliest unsound gate "
        "et=walk gatekeeping backward; evidence not memory",
        "STEP 2 key=Work above unopened gate is re-judged not grandfathered",
        "STEP 3 id=reenter name=Re-enter with ledger seam "
        "et=RE-ENTERED G2 <date> (breach #N)",
        "STEP 3 key=Gates from re-entry forward re-run in order",
        "STEP 4 id=disclose name=Disclose if delivered "
        "et=client hears it before the quiet fix — cover-up shape banned",
        "STEP 4 key=Delivered falsehood: disclose first, fix second",
        "STEP 5 id=remediate name=Remediate + loop back to code sequence "
        "et=code damage left behind → triage → reproduce → heal-verify",
        "STEP 5 key=HARD-GATE --reject-no-register / --reject-no-reentry",
        "",
        "MUST: Before claiming process healed, write the register entry and "
        f"RE-ENTERED seam. Open {LEAF}; run scripts/emperor process-heal "
        "<task-dir>.",
        "MUST-NOT: declare and keep output unjudged; fix quietly before "
        "disclose on delivered falsehood; skip earliest-gate re-entry; claim "
        "process-heal without register + RE-ENTERED.",
    ]
    return "\n".join(lines) + "\n"


def reject_no_register() -> str:
    return (
        "REJECT NO REGISTER: HARD-GATE — holy process-healing refuses close "
        "without Breach Register / Register entry (Vow | what happened | "
        f"remediation). Open {LEAF}; re-run scripts/emperor process-heal "
        "<task-dir>.\n"
    )


def reject_no_reentry() -> str:
    return (
        "REJECT NO REENTRY: HARD-GATE — holy process-healing refuses close "
        "without RE-ENTERED G[0-5] ledger seam (earliest sound gate). "
        f"Open {LEAF}; re-run scripts/emperor process-heal <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time holy process-healing "
            "(register entry + RE-ENTERED seam)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir / process-heal file / ledger (omit to print card)",
    )
    p.add_argument(
        "--check-process-heal",
        type=Path,
        metavar="PATH",
        default=None,
        help="holy process-heal check (exit 1 on soft/missing register or re-entry)",
    )
    p.add_argument(
        "--reject-no-register",
        action="store_true",
        help="Hard-gate: refuse missing register entry (exit 1)",
    )
    p.add_argument(
        "--reject-no-reentry",
        action="store_true",
        help="Hard-gate: refuse missing RE-ENTERED seam (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_no_register:
        sys.stdout.write(reject_no_register())
        return 1
    if args.reject_no_reentry:
        sys.stdout.write(reject_no_reentry())
        return 1

    target = (
        args.check_process_heal
        if args.check_process_heal is not None
        else args.path
    )
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    if errs:
        for e in errs:
            print(f"process-heal FAIL: {e}", file=sys.stderr)
        return 1
    print(f"process-heal PASS: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
