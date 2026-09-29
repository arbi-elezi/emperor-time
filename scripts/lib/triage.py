#!/usr/bin/env python3
"""Validate Emperor Time Holy triage block + snapshot.

Doctrine: chains/holy-chain/triage.md — freeze the scene before investigation.
Output: triage block in the ledger + stabilized workspace. Hands off to
reproduce-and-bisect once the scene is secured.

Always-fail HARD-GATE helpers:
  --reject-no-triage      refuse proceeding without triage block
  --reject-no-snapshot    refuse proceeding without snapshot field

Check mode:
  --check-triage PATH     task dir or triage/ledger file
                          (exit 1 on soft / missing triage block or snapshot)

Positional PATH runs the same check. No args prints the TRIAGE card.
Thin twins: scripts/triage.sh / scripts/triage.ps1
Alias: holy-triage → same core.
Activity-scoped: SKIP (vacuous — no activity) when no triage activity claimed.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence
from check_report import report_check

LEAF = "chains/holy-chain/triage.md"

# Strong triage signals — weak "broke" alone is not enough.
_TRIAGE_SIGNAL = re.compile(
    r"(?i)\b("
    r"holy\s+triage"
    r"|triage\s+block"
    r"|securing\s+the\s+scene"
    r"|TRIAGE\s+\S"
    r"|last-?known-?good"
    r"|last-good\s*:"
    r"|first-bad\s*:"
    r"|agents?\s+halted"
    r"|holy-chain\s+triage"
    r"|snapshot\s*:\s*\S"
    r")\b"
)

_BROKE = re.compile(
    r"(?i)(?<!\w)("
    r"Broke\s*:"
    r"|symptom\s*:"
    r"|what\s+broke\s*:"
    r")"
)

_NOTICED = re.compile(
    r"(?i)(?<!\w)("
    r"Noticed\s+by\s*:"
    r"|Noticed\s*:"
    r"|trigger\s*:"
    r"|trigger\s+verbatim"
    r")"
)

_LAST_GOOD = re.compile(
    r"(?i)(?<!\w)("
    r"Last-good\s*:"
    r"|Last[- ]known[- ]good\s*:"
    r"|last\s+demonstrably\s+worked"
    r")"
)

_FIRST_BAD = re.compile(
    r"(?i)(?<!\w)("
    r"First-bad\s*:"
    r"|first\s+observed\s+broken"
    r"|first[- ]bad\s*:"
    r")"
)

_SNAPSHOT = re.compile(
    r"(?i)(?<!\w)(?<!no\s)(?<!without\s)("
    r"Snapshot\s*:\s*\S"
    r"|stash\s+ref\s*:\s*\S"
    r"|rescue\s+branch\s*:\s*\S"
    r"|holy-\d{4}"
    r"|git\s+stash\s+push[^\n]{0,40}holy-chain"
    r"|cp\s+-R[^\n]{0,40}\.holy-"
    r")"
)

_CLASS = re.compile(
    r"(?i)(?<!\w)("
    r"Class\s*:\s*(?:local|shared|shipped)"
    r"|severity\s*:\s*(?:local|shared|shipped)"
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
        "triage.md",
        "ledger.md",
        "claims.md",
        "claim-ledger.md",
        "DONE.md",
        "done.md",
        "admission.md",
        "reproduce.md",
        "heal.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
    return "\n".join(parts)


def _has_triage_signal(path: Path, text: str) -> bool:
    if path.is_file() and path.name.lower() in {"triage.md"}:
        return True
    if path.is_dir() and (path / "triage.md").is_file():
        return True
    return bool(_TRIAGE_SIGNAL.search(text))


def _block_errors(text: str) -> list[str]:
    errors: list[str] = []
    if not _BROKE.search(text):
        errors.append(
            "missing Broke field "
            f"(need Broke:/symptom: — see {LEAF})"
        )
    if not _NOTICED.search(text):
        errors.append(
            "missing Noticed-by field "
            f"(need Noticed by:/trigger: — see {LEAF})"
        )
    if not _LAST_GOOD.search(text):
        errors.append(
            "missing Last-good bracket "
            f"(need Last-good:/last-known-good — see {LEAF})"
        )
    if not _FIRST_BAD.search(text):
        errors.append(
            "missing First-bad bracket "
            f"(need First-bad:/first observed broken — see {LEAF})"
        )
    if not _CLASS.search(text):
        errors.append(
            "missing Class field "
            f"(need Class: local|shared|shipped — see {LEAF})"
        )
    return errors


def _snapshot_errors(text: str) -> list[str]:
    if _SNAPSHOT.search(text):
        return []
    return [
        "missing Snapshot field "
        "(need Snapshot:/stash ref / rescue branch / copy path / HEAD — see "
        f"{LEAF})"
    ]


def validate(path: Path) -> list[str]:
    """Mechanical triage checks for a task dir / triage / ledger file."""
    if not path.exists():
        return [f"missing path: {path}"]

    text = _combined_text(path)
    active = _has_triage_signal(path, text)
    if not active:
        # Vacuous PASS — no triage activity to close
        if path.is_file() and path.name.lower() == "triage.md":
            return _block_errors(text) + _snapshot_errors(text)
        return []

    errors = _block_errors(text) + _snapshot_errors(text)
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "TRIAGE checklist=yes",
        f"TRIAGE leaf={LEAF}",
        "TRIAGE iron=STOP_SNAPSHOT_BRACKET",
        "STEP 1 id=stop name=Halt in-flight edits and touching agents "
        "et=urge to fix before understanding is digging",
        "STEP 1 key=Note exact trigger verbatim",
        "STEP 2 id=snapshot name=Freeze the workspace "
        "et=stash / rescue branch / copy / HEAD — reversibility concrete",
        "STEP 2 key=Every investigative action must have an undo after this",
        "STEP 3 id=bracket name=Last-good / First-bad interval "
        "et=demonstrably worked → first observed broken",
        "STEP 3 key=No demonstrable last-good → record honestly",
        "STEP 4 id=class name=Classify severity "
        "et=local|shared|shipped — changes who you tell",
        "STEP 4 key=Shared/shipped: tell client before investigating further",
        "STEP 5 id=block name=Write TRIAGE block "
        "et=Broke|Noticed|Last-good|First-bad|Snapshot|Class|Agents halted",
        "STEP 5 key=HARD-GATE --reject-no-triage / --reject-no-snapshot",
        "",
        "MUST: Before investigating further, write the triage block and record "
        f"the snapshot. Open {LEAF}; run scripts/emperor triage <task-dir>.",
        "MUST-NOT: dig before snapshot; skip last-good bracket; claim triage "
        "without Class; hand off to reproduce without a triage block.",
    ]
    return "\n".join(lines) + "\n"


def reject_no_triage() -> str:
    return (
        "REJECT NO TRIAGE: HARD-GATE — holy triage refuses investigation "
        "without Broke|Noticed|Last-good|First-bad|Class triage block. "
        f"Open {LEAF}; re-run scripts/emperor triage <task-dir>.\n"
    )


def reject_no_snapshot() -> str:
    return (
        "REJECT NO SNAPSHOT: HARD-GATE — holy triage refuses proceeding "
        "without Snapshot: (stash / rescue branch / copy / HEAD). "
        f"Open {LEAF}; re-run scripts/emperor triage <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time holy triage "
            "(triage block + snapshot)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir / triage file / ledger (omit to print TRIAGE card)",
    )
    p.add_argument(
        "--check-triage",
        type=Path,
        metavar="PATH",
        default=None,
        help="holy triage check (exit 1 on soft/missing block or snapshot)",
    )
    p.add_argument(
        "--reject-no-triage",
        action="store_true",
        help="Hard-gate: refuse missing triage block (exit 1)",
    )
    p.add_argument(
        "--reject-no-snapshot",
        action="store_true",
        help="Hard-gate: refuse missing snapshot field (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_no_triage:
        sys.stdout.write(reject_no_triage())
        return 1
    if args.reject_no_snapshot:
        sys.stdout.write(reject_no_snapshot())
        return 1

    target = args.check_triage if args.check_triage is not None else args.path
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    text_blob = _combined_text(target) if target.exists() else ""
    vacuous = target.exists() and not _has_triage_signal(target, text_blob)
    return report_check("triage", target, errs, vacuous=vacuous)


if __name__ == "__main__":
    raise SystemExit(main())
