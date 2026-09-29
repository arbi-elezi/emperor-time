#!/usr/bin/env python3
"""Validate Emperor Time reproduce-and-bisect fingerprint + combat ledger.

Doctrine: chains/holy-chain/reproduce-and-bisect.md — fail on demand with a
quoted fingerprint, then one-hypothesis combat ledger lines before healing.
Hands off to heal-and-verify once cause + mechanism + repro are in hand.

Always-fail HARD-GATE helpers:
  --reject-no-repro           refuse cause-isolated without repro fingerprint
  --reject-no-combat-ledger   refuse bisect claims without combat ledger line

Check mode:
  --check-reproduce PATH      task dir or reproduce/ledger file
                              (exit 1 on soft / missing fingerprint or ledger)

Positional PATH runs the same check. No args prints the REPRODUCE card.
Thin twins: scripts/reproduce.sh / scripts/reproduce.ps1
Alias: reproduce-and-bisect → same core.
Activity-scoped: SKIP (vacuous — no activity) when no reproduce/bisect claimed.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence
from check_report import report_check

LEAF = "chains/holy-chain/reproduce-and-bisect.md"

# Strong reproduce/bisect signals — weak "fail" alone is not enough.
_REPRO_SIGNAL = re.compile(
    r"(?i)\b("
    r"reproduce-and-bisect"
    r"|combat\s+ledger"
    r"|holy\s+reproduce"
    r"|cause\s+isolated"
    r"|isolated\s+(?:the\s+)?cause"
    r"|REPRO\s*:"
    r"|fails?\s+on\s+demand"
    r"|failure\s+fingerprint"
    r"|fingerprint\s*:"
    r"|git\s+bisect"
    r"|minimal\s+repro(?:duction)?"
    r"|bisection\s+discipline"
    r"|one\s+hypothesis\s+per\s+(?:step|probe)"
    r")\b"
)

_REPRO_FINGERPRINT = re.compile(
    r"(?i)(?<!\w)("
    r"REPRO\s*:"
    r"|fingerprint\s*:"
    r"|fails?\s+on\s+demand"
    r"|minimal\s+repro(?:duction)?"
    r"|reproduction\s*:"
    r"|repro(?:duction)?\s+(?:cmd|command|invocation)\s*:"
    r"|failure\s+(?:text|output|fingerprint)\s*:"
    r"|quoted\s+failure"
    r"|fail(?:ure|s)?\s+quoted"
    r")"
)

# H3: ... | predict: ... | ran: ... | saw: ... | REFUTED/VERIFIED/...
_COMBAT_LEDGER = re.compile(
    r"(?im)^\s*H\d+\s*:\s*\S.+?"
    r"\|\s*predict\s*:\s*\S.+?"
    r"\|\s*ran\s*:\s*\S.+?"
    r"\|\s*saw\s*:\s*\S.+?"
    r"\|\s*\S"
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
        "reproduce.md",
        "bisect.md",
        "combat-ledger.md",
        "repro.md",
        "ledger.md",
        "claims.md",
        "claim-ledger.md",
        "DONE.md",
        "done.md",
        "heal.md",
        "admission.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
    return "\n".join(parts)


def _has_repro_signal(path: Path, text: str) -> bool:
    if path.is_file() and path.name.lower() in {
        "reproduce.md",
        "bisect.md",
        "combat-ledger.md",
        "repro.md",
    }:
        return True
    if path.is_dir():
        for name in ("reproduce.md", "bisect.md", "combat-ledger.md", "repro.md"):
            if (path / name).is_file():
                return True
    return bool(_REPRO_SIGNAL.search(text))


def _fingerprint_errors(text: str) -> list[str]:
    if _REPRO_FINGERPRINT.search(text):
        return []
    return [
        "missing reproduction fingerprint "
        "(need REPRO:/fingerprint:/fails on demand / quoted failure — see "
        f"{LEAF})"
    ]


def _combat_errors(text: str) -> list[str]:
    if _COMBAT_LEDGER.search(text):
        return []
    return [
        "missing combat ledger line "
        "(need H#: ... | predict: ... | ran: ... | saw: ... | "
        f"REFUTED|VERIFIED — see {LEAF})"
    ]


def validate(path: Path) -> list[str]:
    """Mechanical reproduce-and-bisect checks for a task dir / file."""
    if not path.exists():
        return [f"missing path: {path}"]

    text = _combined_text(path)
    active = _has_repro_signal(path, text)
    if not active:
        # Vacuous PASS — no reproduce/bisect activity to close
        if path.is_file() and path.name.lower() in {
            "reproduce.md",
            "bisect.md",
            "combat-ledger.md",
            "repro.md",
        }:
            return _fingerprint_errors(text) + _combat_errors(text)
        return []

    errors = _fingerprint_errors(text) + _combat_errors(text)
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "REPRODUCE checklist=yes",
        f"REPRODUCE leaf={LEAF}",
        "REPRODUCE iron=FINGERPRINT_THEN_COMBAT",
        "STEP 1 id=repro name=Fail on demand "
        "et=minimal invocation; quote failure fingerprint",
        "STEP 1 key=No reproduction → no healing claims (mitigation only)",
        "STEP 2 id=minimize name=Strip to smallest failing case "
        "et=each removal is a micro-probe",
        "STEP 2 key=Determinism 3/3 or measured flake rate",
        "STEP 3 id=combat name=Combat ledger before each probe "
        "et=H#: cause | predict: | ran: | saw: | REFUTED|VERIFIED",
        "STEP 3 key=One variable per probe; prediction stops motivated reading",
        "STEP 4 id=exit name=Cause + mechanism + repro in hand "
        "et=hand to heal-and-verify.md",
        "STEP 4 key=HARD-GATE --reject-no-repro / --reject-no-combat-ledger",
        "",
        "MUST: Before claiming cause isolated, quote the reproduction fingerprint "
        f"and at least one combat ledger line. Open {LEAF}; run "
        "scripts/emperor reproduce <task-dir>.",
        "MUST-NOT: guess a fix for an irreproducible failure; skip combat ledger; "
        "change two variables per probe; claim bisect without mechanism.",
    ]
    return "\n".join(lines) + "\n"


def reject_no_repro() -> str:
    return (
        "REJECT NO REPRO: HARD-GATE — reproduce-and-bisect refuses "
        "'cause isolated' without a quoted reproduction fingerprint. "
        f"Open {LEAF}; re-run scripts/emperor reproduce <task-dir>.\n"
    )


def reject_no_combat_ledger() -> str:
    return (
        "REJECT NO COMBAT LEDGER: HARD-GATE — reproduce-and-bisect refuses "
        "bisect claims without H#: | predict: | ran: | saw: | line. "
        f"Open {LEAF}; re-run scripts/emperor reproduce <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time reproduce-and-bisect "
            "(fingerprint + combat ledger)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir / reproduce file / ledger (omit to print REPRODUCE card)",
    )
    p.add_argument(
        "--check-reproduce",
        type=Path,
        metavar="PATH",
        default=None,
        help="reproduce-and-bisect check (exit 1 on soft/missing fingerprint or ledger)",
    )
    p.add_argument(
        "--reject-no-repro",
        action="store_true",
        help="Hard-gate: refuse missing reproduction fingerprint (exit 1)",
    )
    p.add_argument(
        "--reject-no-combat-ledger",
        action="store_true",
        help="Hard-gate: refuse missing combat ledger line (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_no_repro:
        sys.stdout.write(reject_no_repro())
        return 1
    if args.reject_no_combat_ledger:
        sys.stdout.write(reject_no_combat_ledger())
        return 1

    target = args.check_reproduce if args.check_reproduce is not None else args.path
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    text_blob = _combined_text(target) if target.exists() else ""
    vacuous = target.exists() and not _has_repro_signal(target, text_blob)
    return report_check("reproduce", target, errs, vacuous=vacuous)


if __name__ == "__main__":
    raise SystemExit(main())
