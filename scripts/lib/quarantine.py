#!/usr/bin/env python3
"""Validate Emperor Time Steal quarantine admission.

Doctrine: chains/steal-chain/quarantine.md — worker output is CONJECTURE;
nothing crosses from .emperor/runs/ into real artifacts without an admission
record (ADMITTED / REJECTED + verification quote).

Always-fail HARD-GATE helpers:
  --reject-unquarantined   refuse missing quarantine / CONJECTURE / admission

Check mode:
  --check-quarantine PATH  task dir, admission file, or runs tree
                           (exit 1 on soft / missing admission)

Positional PATH runs the same check. No args prints the QUARANTINE card.
Thin twins: scripts/quarantine.sh / scripts/quarantine.ps1
Alias: steal-quarantine → same core.
G4 in gate.py calls --check-quarantine when steal activity is present
(vacuous PASS when no worker runs / no steal markers).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence

LEAF = "chains/steal-chain/quarantine.md"
RUN_LAYOUT = ".emperor/runs/<task>/<agent>/{prompt.md,out.txt,meta.md}"

# Positive ruling tokens — ignore "No ADMITTED" / "without REJECTED" prose.
_ADMISSION = re.compile(
    r"(?i)(?<![\w-])(?<!no\s)(?<!without\s)(?<!missing\s)"
    r"(ADMITTED|REJECTED)(?![\w-])"
)
_ADMISSION_VERIFIED = re.compile(
    r"(?i)(?<![\w-])(?<!no\s)(?<!without\s)(?<!missing\s)"
    r"(ADMITTED|REJECTED)(?![\w-])[\s\S]{0,200}?"
    r"\b(verified|reason|probe)\b"
    r"|\b(verified|reason)\s*:\s*\S"
)
# CONJECTURE *start* — status cell / carried label / explicit start phrase.
# Do NOT treat "CONJECTURE-labeled" audit tallies alone as admission start.
_CONJECTURE_START = re.compile(
    r"(?i)"
    # Table status cell containing CONJECTURE (not prose mentioning the word).
    r"(?:^\|[^\n]*\|\s*CONJECTURE\b"
    r"|\bCONJECTURE\s*\(carried\)"
    r"|\bCONJECTURE\s+start\s*:"
    r"|\bstarts?\s+at\s+CONJECTURE\b"
    r"|\bentered\s+(?:the\s+)?(?:claim\s+)?ledger\s+as\s+CONJECTURE\b"
    r"|\bas\s+CONJECTURE\s+(?:before|with|then)\b)"
)
# Strong steal signals only — weak words like "enlisted" appear in normal ledgers.
_STEAL_SIGNAL = re.compile(
    r"(?i)\b(STEAL|\.emperor/runs|worker\s+done)\b"
    r"|\bquarantine\s+(admission|dir|record)\b"
    r"|\b(ADMITTED|REJECTED)\b"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _iter_run_agents(root: Path) -> list[Path]:
    """Return agent run dirs that look like steal capture layout."""
    candidates: list[Path] = []
    for base_name in (".emperor/runs", "runs"):
        base = root / base_name
        if not base.is_dir():
            # Also allow task dir itself to BE a runs/<task> tree
            continue
        # layout: runs/<task>/<agent>/out.txt  OR  runs/<agent>/out.txt
        for path in base.rglob("out.txt"):
            agent_dir = path.parent
            if agent_dir not in candidates:
                candidates.append(agent_dir)
    # PATH may itself be an agent run dir
    if (root / "out.txt").is_file():
        candidates.append(root)
    # PATH may be runs/<task> with agent children
    if root.is_dir() and not candidates:
        for child in root.iterdir():
            if child.is_dir() and (child / "out.txt").is_file():
                candidates.append(child)
    return candidates


def _combined_text(task_or_file: Path) -> tuple[str, list[Path]]:
    """Text that may carry admission / CONJECTURE / steal markers."""
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    if not task_or_file.is_dir():
        return ("", [])
    parts: list[str] = []
    sources: list[Path] = []
    for name in (
        "admission.md",
        "quarantine.md",
        "ledger.md",
        "claims.md",
        "claim-ledger.md",
        "DONE.md",
        "done.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
            sources.append(p)
    # Also fold short out.txt tails (worker "done" testimony)
    for agent in _iter_run_agents(task_or_file):
        out = agent / "out.txt"
        if out.is_file() and out not in sources:
            parts.append(_read(out)[:4000])
            sources.append(out)
    return ("\n".join(parts), sources)


def _has_steal_signal(path: Path, text: str) -> bool:
    root = path if path.is_dir() else path.parent
    if _iter_run_agents(root):
        return True
    if path.is_dir():
        for name in ("admission.md", "quarantine.md"):
            if (path / name).is_file():
                return True
    # File named admission/quarantine is itself a steal signal
    if path.is_file() and path.name.lower() in {"admission.md", "quarantine.md"}:
        return True
    return bool(_STEAL_SIGNAL.search(text))


def _layout_errors(agent_dir: Path) -> list[str]:
    errs: list[str] = []
    for req in ("prompt.md", "out.txt", "meta.md"):
        if not (agent_dir / req).is_file():
            errs.append(
                f"run layout incomplete under {agent_dir}: missing {req} "
                f"(need {RUN_LAYOUT})"
            )
    return errs


def _admission_ok(text: str) -> list[str]:
    errors: list[str] = []
    if not _ADMISSION.search(text):
        errors.append(
            "missing admission marker "
            "(need ADMITTED or REJECTED per contribution — see "
            f"{LEAF})"
        )
        return errors
    # At least one admission should carry verified:/reason:
    if not _ADMISSION_VERIFIED.search(text):
        errors.append(
            "admission lacks verification quote "
            "(need 'verified:' / 'reason:' / probe on ADMITTED|REJECTED row)"
        )
    return errors


def _conjecture_ok(text: str, _agents: list[Path]) -> list[str]:
    """Worker-sourced claims must start as CONJECTURE."""
    if _CONJECTURE_START.search(text):
        return []
    return [
        "missing CONJECTURE start "
        "(enlisted output enters Claim Ledger as CONJECTURE — "
        f"open {LEAF})"
    ]


def validate(path: Path) -> list[str]:
    """Mechanical steal-quarantine checks for a task dir / admission / runs."""
    errors: list[str] = []
    if not path.exists():
        return [f"missing path: {path}"]

    text, _sources = _combined_text(path)
    root = path if path.is_dir() else path.parent
    agents = _iter_run_agents(root)
    # If PATH is a file, also scan that file's directory for runs
    if path.is_file():
        agents = agents or _iter_run_agents(path.parent)

    steal = _has_steal_signal(path if path.is_dir() else root, text)
    if not steal:
        # Vacuous PASS — no steal activity to quarantine
        return []

    file_only = path.is_file()
    if not agents and not file_only:
        errors.append(
            "missing quarantine dir "
            f"(need {RUN_LAYOUT} with out.txt — worker output must land "
            "under .emperor/runs/ before admission)"
        )
    elif not agents and file_only:
        # File-level check: require the admission text to *name* the runs layout.
        if ".emperor/runs" not in text and "runs/" not in text:
            errors.append(
                "admission file missing quarantine dir reference "
                f"(name {RUN_LAYOUT})"
            )
    else:
        for agent in agents:
            errors.extend(_layout_errors(agent))

    errors.extend(_admission_ok(text))
    errors.extend(_conjecture_ok(text, agents))

    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "QUARANTINE checklist=yes",
        f"QUARANTINE leaf={LEAF}",
        f"QUARANTINE layout={RUN_LAYOUT}",
        "QUARANTINE iron=NO_MERGE_WITHOUT_ADMISSION_RECORD",
        "STEP 1 id=capture name=Land worker output in runs/ "
        "et=prompt.md + out.txt + meta.md per agent",
        "STEP 1 key=No silent paste from chat into the tree",
        "STEP 2 id=conjecture name=Enter claims as CONJECTURE "
        "et=worker fluency is testimony, not evidence",
        "STEP 2 key=Empty VERIFIED list from worker → reject without further reading",
        "STEP 3 id=admit name=ADMITTED or REJECTED with your probe "
        "et=verified: quote from YOUR terminal, not the worker's",
        "STEP 3 key=Partial admission is normal; record rejected hunks",
        "STEP 4 id=gate name=Hand to Judgment only after admission "
        "et=scripts/emperor quarantine <task-dir>; G4 calls this module",
        "STEP 4 key=Beautiful-looking diffs still quarantine",
        "",
        "MUST: Before merging enlisted-agent output, capture under "
        f".emperor/runs/, start Claim Ledger rows as CONJECTURE, write "
        f"ADMITTED|REJECTED with verified quote. Open {LEAF}; run "
        "scripts/emperor quarantine <task-dir>. G4 calls this module when "
        "steal activity is present.",
        "MUST-NOT: merge out.txt without admission; promote worker "
        "'done'/'tests pass' above CONJECTURE on testimony; skip meta.md; "
        "quarantine-file-present theater without ADMITTED|REJECTED + verified.",
    ]
    return "\n".join(lines) + "\n"


def reject_unquarantined() -> str:
    return (
        "REJECT UNQUARANTINED: HARD-GATE — Steal refuses worker 'done' without "
        "quarantine dir (.emperor/runs/<task>/<agent>/), CONJECTURE start, and "
        "ADMITTED|REJECTED admission markers with verified quote. "
        f"Open {LEAF}; re-run scripts/emperor quarantine <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time Steal quarantine admission "
            "(runs layout + CONJECTURE + ADMITTED|REJECTED)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir / admission file / runs tree (omit to print QUARANTINE card)",
    )
    p.add_argument(
        "--check-quarantine",
        type=Path,
        metavar="PATH",
        default=None,
        help="quarantine admission check (exit 1 on soft/missing admission)",
    )
    p.add_argument(
        "--reject-unquarantined",
        action="store_true",
        help="Hard-gate: refuse missing quarantine/CONJECTURE/admission (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_unquarantined:
        sys.stdout.write(reject_unquarantined())
        return 1

    target = args.check_quarantine if args.check_quarantine is not None else args.path
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    if errs:
        for e in errs:
            print(f"quarantine FAIL: {e}", file=sys.stderr)
        return 1
    print(f"quarantine PASS: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
