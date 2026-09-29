#!/usr/bin/env python3
"""Honest check-mode reporting for activity-scoped HARD-GATEs.

Activity-scoped gates (Steal / Jail / Holy / peers) must not print bare
``PASS`` when no matching activity was claimed — that lets agents quote
``signin PASS`` as if the gate were exercised. Vacuous paths print:

    {label} SKIP (vacuous — no activity): {target}

Exercised green paths still print:

    {label} PASS: {target}

Exit 0 for both SKIP and PASS; exit 1 for FAIL. Legacy always-on gates
(verdict, …) may still avoid this helper. Critique eight-count and
claim-audit use report_check when harness plan selects skip/activity
(HARNESS_DRIVES_G4_CHECKS); no-plan paths stay require-or-fail.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


def report_check(
    label: str,
    target: Path | str,
    errors: Sequence[str],
    *,
    vacuous: bool,
) -> int:
    """Print FAIL / SKIP (vacuous) / PASS and return exit code 1 / 0 / 0."""
    if errors:
        for e in errors:
            print(f"{label} FAIL: {e}", file=sys.stderr)
        return 1
    if vacuous:
        print(f"{label} SKIP (vacuous — no activity): {target}")
        return 0
    print(f"{label} PASS: {target}")
    return 0


if __name__ == "__main__":
    # Tiny self-check so the module is importable as a script too.
    raise SystemExit(
        report_check("demo", Path("."), [], vacuous=True)
    )
