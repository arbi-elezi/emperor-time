#!/usr/bin/env python3
"""Validate Emperor Time Judgment claim-audit (G4 scientific-method sweep).

Doctrine: chains/judgment-chain/claim-audit.md — every Claim Ledger row
terminates; CLAIM AUDIT line written; HYPOTHESIS/TESTED are unfinished.

Harness-driven G4 (HARNESS_DRIVES_G4_CHECKS):
  When a harness plan exists, --check-audit SKIPs if claim-audit is
  forbidden/unlisted; Optional → SKIP when unused; Tools → require
  CLAIM AUDIT line. No plan → legacy always-on.

Always-fail HARD-GATE helpers:
  --reject-unaudited   refuse missing CLAIM AUDIT / unfinished rows

Check mode:
  --check-audit PATH   task dir or claims/ledger file (exit 1 on soft audit)

Positional PATH runs the same check. No args prints the CLAIM-AUDIT card.
Thin twins: scripts/claim-audit.sh / scripts/claim-audit.ps1
G4 in gate.py calls --check-audit on the task dir.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from check_report import report_check
from typing import Sequence

LEAF = "chains/judgment-chain/claim-audit.md"
TEMPLATE = "templates/claim-ledger.md"

# Doctrine audit line:
# CLAIM AUDIT: n rows — v VERIFIED / r REFUTED / c CONJECTURE-labeled /
# u UNVERIFIABLE-labeled; spot-checks: …
_AUDIT_LINE = re.compile(
    r"(?im)^\s*CLAIM\s+AUDIT\s*:\s*.+\S"
)

_AUDIT_SECTION = re.compile(
    r"(?im)^#{1,6}\s+Claim\s+Audit\b|^##\s+CLAIM\s+AUDIT\b"
)

# Table row with a status cell (pipe-delimited Claim Ledger).
_ROW = re.compile(
    r"^\|(?P<body>(?:[^|\n]+\|)+)\s*$"
)

_STATUS_TOKEN = re.compile(
    r"(?i)\b(VERIFIED|REFUTED|UNVERIFIABLE|CONJECTURE|HYPOTHESIS|TESTED)\b"
)

_TERMINAL = frozenset({"VERIFIED", "REFUTED", "UNVERIFIABLE"})
_UNFINISHED = frozenset({"HYPOTHESIS", "TESTED"})

_CONJECTURE_LABELED = re.compile(
    r"(?i)UNVERIFIABLE|carried|labeled|assumption|explicit"
)

_HEADERISH = re.compile(
    r"(?i)\bClaim\b.*\bStatus\b|\bStatus\b.*\bClaim\b|^\s*#{1,6}\s|"
    r"^\s*\|\s*-+\s*\||^\s*\|\s*#\s*\|"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _combined_text(task_or_file: Path) -> tuple[str, list[Path]]:
    """Return text to audit + source paths.

    PATH may be a task directory (ledger.md + claims.md) or a single file.
    """
    if task_or_file.is_dir():
        parts: list[str] = []
        sources: list[Path] = []
        for name in ("ledger.md", "claims.md", "claim-ledger.md"):
            p = task_or_file / name
            if p.is_file():
                parts.append(_read(p))
                sources.append(p)
        return ("\n".join(parts), sources)
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    return ("", [])


def _has_audit_line(text: str) -> bool:
    return bool(_AUDIT_LINE.search(text) or _AUDIT_SECTION.search(text))


def _status_cells(line: str) -> list[str]:
    """Extract status tokens from a markdown table row."""
    if not line.strip().startswith("|"):
        return []
    # Skip separator / header rows
    if re.match(r"^\|\s*-+", line) or _HEADERISH.search(line):
        # Header may contain the word Status — not a data row
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if any(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            return []
        if any(c.lower() in {"status", "claim", "#", "prediction"} for c in cells):
            return []
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    found: list[str] = []
    for cell in cells:
        m = _STATUS_TOKEN.fullmatch(cell.strip())
        if m:
            found.append(m.group(1).upper())
            continue
        # Status may share a cell with labels: "CONJECTURE (carried)"
        m2 = _STATUS_TOKEN.search(cell)
        if m2 and len(cell) < 80:
            found.append(m2.group(1).upper())
    return found


def _iter_claim_rows(text: str) -> list[tuple[str, str]]:
    """Return [(status, raw_line), ...] for claim-table data rows."""
    rows: list[tuple[str, str]] = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        statuses = _status_cells(line)
        if not statuses:
            continue
        # Prefer the first status-looking cell
        rows.append((statuses[0], line))
    return rows


def _audit_structure_ok(text: str) -> list[str]:
    """Required structure per claim-audit.md doctrine."""
    errors: list[str] = []
    if not _has_audit_line(text):
        errors.append(
            "missing CLAIM AUDIT line "
            "(need 'CLAIM AUDIT: n rows — v VERIFIED / r REFUTED / …')"
        )
        return errors

    audit_m = _AUDIT_LINE.search(text)
    audit_body = audit_m.group(0) if audit_m else ""
    # Zero-row audit is valid structure (trivial / no claims).
    if re.search(r"(?i)\b0\s+rows?\b", audit_body):
        return errors

    # Non-zero audit needs a claim table with Status vocabulary.
    rows = _iter_claim_rows(text)
    if not rows:
        errors.append(
            "CLAIM AUDIT cites rows but no claim-table Status rows found "
            f"(open {TEMPLATE})"
        )
        return errors

    # Audit line should mention at least one terminal / labeled class.
    if not re.search(
        r"(?i)VERIFIED|REFUTED|CONJECTURE|UNVERIFIABLE|spot-check",
        audit_body,
    ):
        errors.append(
            "CLAIM AUDIT line missing status tallies "
            "(VERIFIED/REFUTED/CONJECTURE-labeled/UNVERIFIABLE)"
        )
    return errors


def validate(path: Path) -> list[str]:
    """Mechanical claim-audit checks for a task dir or claims/ledger file."""
    errors: list[str] = []
    if not path.exists():
        return [f"missing path: {path}"]

    text, sources = _combined_text(path)
    if not text.strip():
        return [
            f"no ledger.md / claims.md under {path} "
            "(claim audit needs a Claim Ledger artifact)"
        ]

    errors.extend(_audit_structure_ok(text))

    for status, line in _iter_claim_rows(text):
        if status in _UNFINISHED:
            errors.append(
                f"unfinished {status} row (finish experiment or demote to "
                f"UNVERIFIABLE): {line.strip()[:100]}"
            )
        elif status == "CONJECTURE":
            if not _CONJECTURE_LABELED.search(line):
                errors.append(
                    "unterminated CONJECTURE row "
                    "(must be carried/labeled assumption): "
                    f"{line.strip()[:100]}"
                )
        elif status == "VERIFIED":
            if '"' not in line and "`" not in line:
                errors.append(
                    f"VERIFIED row without quoted evidence: {line.strip()[:100]}"
                )

    # De-dupe while preserving order
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "CLAIM-AUDIT checklist=yes",
        f"CLAIM-AUDIT leaf={LEAF}",
        f"CLAIM-AUDIT template={TEMPLATE}",
        "CLAIM-AUDIT iron=NO_G4_WITHOUT_CLAIM_AUDIT_LINE",
        "CLAIM-AUDIT iron=HARNESS_DRIVES_G4_CHECKS",
        "STEP 1 id=completeness name=Claims in the ledger "
        "et=every assertion is a row; no smuggled obviously/always claims",
        "STEP 1 key=Scan deliverable; unrowed claims → CONJECTURE then continue",
        "STEP 2 id=termination name=No unfinished states "
        "et=VERIFIED/REFUTED/UNVERIFIABLE terminal; CONJECTURE only if labeled",
        "STEP 2 key=HYPOTHESIS/TESTED are unfinished — finish or demote",
        "STEP 3 id=spot-check name=VERIFIED teeth "
        "et=prediction-before-run / evidence-supports / freshness / two-source",
        "STEP 3 key=Quote evidence; near-evidence demotes the row",
        "STEP 4 id=audit-line name=Write CLAIM AUDIT line "
        "et=CLAIM AUDIT: n rows — v VERIFIED / r REFUTED / c labeled / u labeled",
        "STEP 4 key=Hand to self-critique only after the audit line exists",
        "",
        "MUST: Before G4, when harness plan selects claim-audit (Tools) or "
        "optional claim-audit shows activity, Claim Ledger rows are "
        "terminal and ledger carries CLAIM AUDIT line. Tiny/unlisted → "
        f"SKIP (HARNESS_DRIVES_G4_CHECKS). Open {LEAF}; run "
        "scripts/emperor claim-audit <task-dir>. G4 calls this.",
        "MUST-NOT: missing CLAIM AUDIT; HYPOTHESIS/TESTED left open; "
        "critique-file-present theater without the audit sweep; "
        "unlabeled CONJECTURE in delivery.",
    ]
    return "\n".join(lines) + "\n"


def reject_unaudited() -> str:
    return (
        "REJECT UNAUDITED: HARD-GATE — G4 refuses without a CLAIM AUDIT line "
        "and terminal Claim Ledger rows. HYPOTHESIS/TESTED are unfinished; "
        "CONJECTURE must be carried/labeled. "
        f"Open {LEAF}; fill {TEMPLATE}; "
        "re-run scripts/emperor claim-audit <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time Judgment claim-audit "
            "(CLAIM AUDIT line + terminal rows)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir or claims/ledger file (omit to print CLAIM-AUDIT card)",
    )
    p.add_argument(
        "--check-audit",
        type=Path,
        metavar="PATH",
        default=None,
        help="claim-audit structure check (exit 1 on soft/missing audit)",
    )
    p.add_argument(
        "--reject-unaudited",
        action="store_true",
        help="Hard-gate: refuse missing CLAIM AUDIT / unfinished rows (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_unaudited:
        sys.stdout.write(reject_unaudited())
        return 1

    target = args.check_audit if args.check_audit is not None else args.path
    if target is None:
        sys.stdout.write(format_card())
        return 0

    # Harness drives which G4 checks run. Tiny does not select claim-audit
    # → SKIP (no museum CLAIM AUDIT for a 2-line change). No plan → always-on.
    if target.is_dir() or target.exists():
        try:
            from harness_plan import g4_check_mode, tool_was_used

            mode = g4_check_mode(target, "claim-audit")
            if mode == "skip":
                return report_check(
                    "claim_audit", target, [], vacuous=True
                )
            root = target if target.is_dir() else target.parent
            if mode == "activity" and not tool_was_used(root, "claim-audit"):
                return report_check(
                    "claim_audit", target, [], vacuous=True
                )
        except Exception:
            pass

    errs = validate(target)
    return report_check("claim_audit", target, errs, vacuous=False)


if __name__ == "__main__":
    raise SystemExit(main())
