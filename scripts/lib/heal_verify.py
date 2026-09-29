#!/usr/bin/env python3
"""Validate Emperor Time heal-and-verify triad + postmortem.

Doctrine: chains/holy-chain/heal-and-verify.md — cure + no-new-wounds +
mechanism triad, then the structured postmortem line. Entry still runs
four-phase via debug_phases / emperor heal; this module locks the close.

Always-fail HARD-GATE helpers:
  --reject-no-triad        refuse heal-done without verification triad
  --reject-no-postmortem   refuse heal-done without postmortem line

Check mode:
  --check-heal PATH        task dir or heal/ledger file
                           (exit 1 on soft / missing triad or postmortem)

Positional PATH runs the same check. No args prints the HEAL-VERIFY card.
Thin twins: scripts/heal-verify.sh / scripts/heal-verify.ps1
Alias: heal-and-verify → same core.
Activity-scoped: SKIP (vacuous — no activity) when no heal activity claimed.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence
from check_report import report_check

LEAF = "chains/holy-chain/heal-and-verify.md"

# Strong heal signals — weak "fix" alone is not enough (normal ledgers).
_HEAL_SIGNAL = re.compile(
    r"(?i)\b("
    r"heal-and-verify"
    r"|verification\s+triad"
    r"|BROKE\s*:"
    r"|WOULD-HAVE-CAUGHT-SOONER"
    r"|no\s+new\s+wounds"
    r"|holy\s+heal"
    r"|root-cause\s+heal"
    r"|symptom-?patch"
    r"|HEAL\s*:"
    r")\b"
)

_CURE = re.compile(
    r"(?i)(?<!\w)("
    r"cure\s*:"
    r"|cure\s*[—\-]\s*"
    r"|reproduction\s+now\s+pass(?:es|ed)?"
    r"|repro(?:duction)?\s+now\s+pass(?:es|ed)?"
    r"|repro(?:duction)?\s+pass(?:es|ed)?"
    r"|original\s+repro[^\n]{0,80}pass"
    r"|triage-captured\s+reproduction[^\n]{0,80}pass"
    r")"
)

_NO_WOUNDS = re.compile(
    r"(?i)(?<!\w)("
    r"no\s+new\s+wounds"
    r"|surrounding\s+(suite|build)\s+pass"
    r"|suite\s+pass(?:es|ed)?\s+at\s+pre-breakage"
    r"|full\s+suite\s+pass"
    r")"
)

_MECHANISM = re.compile(
    r"(?i)(?<!\w)("
    r"mechanism\s*:"
    r"|mechanism\s+suppressed,?\s*not\s+removed"
    r"|root-?cause\s+claim\s+.*VERIFIED"
    r"|VERIFIED[^\n]{0,120}root-?cause"
    r"|why\s+it\s+broke[^\n]{0,80}why\s+this\s+change"
    r")"
)

# BROKE: ... | CAUSE: ... | HEAL: ... | CAUGHT-BY: ... | WOULD-HAVE-CAUGHT-SOONER: ...
_POSTMORTEM = re.compile(
    r"(?is)BROKE\s*:\s*\S.+?"
    r"\|\s*CAUSE\s*:\s*\S.+?"
    r"\|\s*HEAL\s*:\s*\S.+?"
    r"\|\s*CAUGHT-BY\s*:\s*\S.+?"
    r"\|\s*WOULD-HAVE-CAUGHT-SOONER\s*:\s*\S"
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
        "heal.md",
        "heal-verify.md",
        "postmortem.md",
        "ledger.md",
        "claims.md",
        "claim-ledger.md",
        "DONE.md",
        "done.md",
        "admission.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
    return "\n".join(parts)


def _has_heal_signal(path: Path, text: str) -> bool:
    if path.is_file() and path.name.lower() in {
        "heal.md",
        "heal-verify.md",
        "postmortem.md",
    }:
        return True
    if path.is_dir():
        for name in ("heal.md", "heal-verify.md", "postmortem.md"):
            if (path / name).is_file():
                return True
    return bool(_HEAL_SIGNAL.search(text))


def _triad_errors(text: str) -> list[str]:
    errors: list[str] = []
    if not _CURE.search(text):
        errors.append(
            "missing Cure triad leg "
            "(need cure:/repro pass quote — see "
            f"{LEAF})"
        )
    if not _NO_WOUNDS.search(text):
        errors.append(
            "missing No-new-wounds triad leg "
            "(need 'no new wounds' / suite pass at pre-breakage scope — see "
            f"{LEAF})"
        )
    if not _MECHANISM.search(text):
        errors.append(
            "missing Mechanism triad leg "
            "(need mechanism:/VERIFIED root-cause or "
            "'mechanism suppressed, not removed' — see "
            f"{LEAF})"
        )
    return errors


def _postmortem_errors(text: str) -> list[str]:
    if _POSTMORTEM.search(text):
        return []
    return [
        "missing postmortem line "
        "(need BROKE: | CAUSE: | HEAL: | CAUGHT-BY: | "
        f"WOULD-HAVE-CAUGHT-SOONER: — see {LEAF})"
    ]


def validate(path: Path) -> list[str]:
    """Mechanical heal-and-verify checks for a task dir / heal / ledger file."""
    if not path.exists():
        return [f"missing path: {path}"]

    text = _combined_text(path)
    heal = _has_heal_signal(path, text)
    if not heal:
        # Vacuous PASS — no heal activity to close
        # Explicit heal/postmortem file still validates structure.
        if path.is_file() and path.name.lower() in {
            "heal.md",
            "heal-verify.md",
            "postmortem.md",
        }:
            return _triad_errors(text) + _postmortem_errors(text)
        return []

    errors = _triad_errors(text) + _postmortem_errors(text)
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "HEAL-VERIFY checklist=yes",
        f"HEAL-VERIFY leaf={LEAF}",
        "HEAL-VERIFY iron=TRIAD_THEN_POSTMORTEM",
        "STEP 1 id=shape name=Choose root-cause heal or labeled symptom-patch "
        "et=mislabeling is the crime",
        "STEP 1 key=Unlabeled symptom-patch is a delayed lie",
        "STEP 2 id=minimal name=Keep scope minimal "
        "et=no riders; adjacent bugs → own task",
        "STEP 2 key=Smallest scope ≠ hackiest thought",
        "STEP 3 id=triad name=Verification triad quoted "
        "et=Cure + No new wounds + Mechanism",
        "STEP 3 key=Unverified until each triad leg holds",
        "STEP 4 id=postmortem name=BROKE|CAUSE|HEAL|CAUGHT-BY|WOULD-HAVE-CAUGHT-SOONER "
        "et=one structured ledger line",
        "STEP 4 key=Forward-looking field names a cheap check or honest nothing",
        "",
        "MUST: Before claiming heal done, quote Cure + No-new-wounds + Mechanism "
        f"and append the postmortem line. Open {LEAF}; run "
        "scripts/emperor heal-verify <task-dir>. Entry still runs "
        "scripts/emperor heal (four-phase) before proposing fixes.",
        "MUST-NOT: claim heal without triad; skip postmortem; discard "
        ".holy- snapshot before triad; unlabeled symptom-patch as 'fixed'.",
    ]
    return "\n".join(lines) + "\n"


def reject_no_triad() -> str:
    return (
        "REJECT NO TRIAD: HARD-GATE — heal-and-verify refuses 'done' without "
        "Cure + No-new-wounds + Mechanism quoted. "
        f"Open {LEAF}; re-run scripts/emperor heal-verify <task-dir>.\n"
    )


def reject_no_postmortem() -> str:
    return (
        "REJECT NO POSTMORTEM: HARD-GATE — heal-and-verify refuses 'done' "
        "without BROKE: | CAUSE: | HEAL: | CAUGHT-BY: | "
        "WOULD-HAVE-CAUGHT-SOONER: line. "
        f"Open {LEAF}; re-run scripts/emperor heal-verify <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time heal-and-verify "
            "(verification triad + postmortem line)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir / heal file / ledger (omit to print HEAL-VERIFY card)",
    )
    p.add_argument(
        "--check-heal",
        type=Path,
        metavar="PATH",
        default=None,
        help="heal-and-verify check (exit 1 on soft/missing triad or postmortem)",
    )
    p.add_argument(
        "--reject-no-triad",
        action="store_true",
        help="Hard-gate: refuse missing verification triad (exit 1)",
    )
    p.add_argument(
        "--reject-no-postmortem",
        action="store_true",
        help="Hard-gate: refuse missing postmortem line (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_no_triad:
        sys.stdout.write(reject_no_triad())
        return 1
    if args.reject_no_postmortem:
        sys.stdout.write(reject_no_postmortem())
        return 1

    target = args.check_heal if args.check_heal is not None else args.path
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    text_blob = _combined_text(target) if target.exists() else ""
    vacuous = target.exists() and not _has_heal_signal(target, text_blob)
    return report_check("heal-verify", target, errs, vacuous=vacuous)


if __name__ == "__main__":
    raise SystemExit(main())
