#!/usr/bin/env python3
"""Validate Emperor Time Steal consent-protocol records.

Doctrine: chains/steal-chain/consent-protocol.md — nothing dispatches without
a consent line (per-task ask, standing policy quote, CI EMPEROR_CONSENT_AGENTS,
or honest solo self-grant).

Always-fail HARD-GATE helpers:
  --reject-no-consent   refuse dispatch / enlistment without consent record

Check mode:
  --check-consent PATH  task dir or consent/ledger file
                        (exit 1 on soft / missing consent)

Positional PATH runs the same check. No args prints the CONSENT card.
Thin twins: scripts/consent.sh / scripts/consent.ps1
Alias: steal-consent → same core.
G4 in gate.py calls --check-consent when steal activity is present
(activity-scoped; SKIP (vacuous — no activity) when no steal markers).
CI: EMPEROR_CONSENT_AGENTS=codex,claude (or "none") replaces chat consent.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Sequence
from check_report import report_check

LEAF = "chains/steal-chain/consent-protocol.md"

# Positive CONSENT header — ignore "no CONSENT" / "without consent" prose.
_CONSENT_HEADER = re.compile(
    r"(?i)(?<![\w-])(?<!no\s)(?<!without\s)(?<!missing\s)"
    r"CONSENT\s*:\s*"
)
# Assignment: agent → role  (arrow unicode or ASCII)
_ASSIGNMENT = re.compile(
    r"(?im)^\s{0,6}([A-Za-z][\w./-]*)\s*(?:→|->)\s*\S"
)
# Solo self-grant (consent-protocol.md Step 2 autonomous path)
_SOLO = re.compile(
    r"(?i)\b("
    r"proceeded\s+solo"
    r"|client\s+unreachable[^\n]{0,80}solo"
    r"|CONSENT\s*:\s*[^\n]*\bsolo\b"
    r"|solo\s*=\s*self-?grant"
    r")\b"
)
_STANDING = re.compile(r"(?i)\bSTANDING\s+POLICY\b")
# Strong steal signals — weak "enlisted" alone is not enough (normal ledgers).
_STEAL_SIGNAL = re.compile(
    r"(?i)\b(STEAL|\.emperor/runs|worker\s+done|dispatch(?:ed|ing)?\s+worker)\b"
    r"|\bconsent\s+(record|protocol|ask)\b"
    r"|\bEMPEROR_CONSENT_AGENTS\b"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _iter_run_agents(root: Path) -> list[Path]:
    """Return agent run dirs that look like steal capture layout."""
    candidates: list[Path] = []
    for base_name in (".emperor/runs", "runs"):
        base = root / base_name
        if not base.is_dir():
            continue
        for path in base.rglob("out.txt"):
            agent_dir = path.parent
            if agent_dir not in candidates:
                candidates.append(agent_dir)
    if (root / "out.txt").is_file():
        candidates.append(root)
    if root.is_dir() and not candidates:
        for child in root.iterdir():
            if child.is_dir() and (child / "out.txt").is_file():
                candidates.append(child)
    return candidates


def _combined_text(task_or_file: Path) -> tuple[str, list[Path]]:
    """Text that may carry CONSENT / standing / steal markers."""
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    if not task_or_file.is_dir():
        return ("", [])
    parts: list[str] = []
    sources: list[Path] = []
    for name in (
        "consent.md",
        "ledger.md",
        "admission.md",
        "quarantine.md",
        "claims.md",
        "claim-ledger.md",
        "DONE.md",
        "done.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
            sources.append(p)
    return ("\n".join(parts), sources)


def _env_agents() -> list[str] | None:
    """Return CI standing agent list, or None if unset. Empty/'none' → []."""
    raw = os.environ.get("EMPEROR_CONSENT_AGENTS")
    if raw is None:
        return None
    raw = raw.strip()
    if not raw or raw.lower() == "none":
        return []
    return [a.strip().lower() for a in raw.split(",") if a.strip()]


def _has_steal_signal(path: Path, text: str) -> bool:
    root = path if path.is_dir() else path.parent
    if _iter_run_agents(root):
        return True
    if path.is_dir():
        for name in ("consent.md", "admission.md", "quarantine.md"):
            if (path / name).is_file():
                return True
    if path.is_file() and path.name.lower() in {
        "consent.md",
        "admission.md",
        "quarantine.md",
    }:
        return True
    return bool(_STEAL_SIGNAL.search(text))


def _assignments(text: str) -> list[str]:
    return [m.group(1).lower() for m in _ASSIGNMENT.finditer(text)]


def _consent_structure_errors(text: str) -> list[str]:
    """Structural consent checks (header + assignment or solo/standing+assign)."""
    errors: list[str] = []
    has_header = bool(_CONSENT_HEADER.search(text))
    has_solo = bool(_SOLO.search(text))
    has_standing = bool(_STANDING.search(text))
    agents = _assignments(text)

    if has_solo and not agents:
        # Honest solo self-grant — no enlisted agents required.
        return []

    if not has_header and not has_standing:
        errors.append(
            "missing CONSENT record "
            f"(need 'CONSENT: task …' with agent → role lines — see {LEAF})"
        )
        return errors

    if not agents:
        errors.append(
            "CONSENT header/standing without assignment "
            "(need at least one 'agent → role' line, or honest 'proceeded solo' "
            f"— see {LEAF})"
        )
        return errors

    # Soft theater: CONSENT present but no per-task/standing provenance hint
    # (quote, approval, standing policy, or client msg). Assignment alone OK
    # if header present — provenance is recommended but not regex-theater.
    return errors


def _agent_coverage_errors(text: str, agent_dirs: list[Path], env: list[str] | None) -> list[str]:
    """When runs/<agent> exist, each enlisted agent must be named in consent or env."""
    if not agent_dirs:
        return []
    named = set(_assignments(text))
    # Also allow bare agent tokens after CONSENT: (codex on its own line)
    named |= {
        m.group(1).lower()
        for m in re.finditer(
            r"(?im)^\s{0,6}([A-Za-z][\w./-]*)\s*(?:→|->|\bapproved\b|\benlisted\b)",
            text,
        )
    }
    text_l = text.lower()
    env_set = set(env) if env is not None else None
    missing: list[str] = []
    for d in agent_dirs:
        agent = d.name.lower()
        if agent in {"demo", "task", "runs"}:
            continue
        covered = agent in named or agent in text_l
        if env_set is not None and agent in env_set:
            covered = True
        if not covered:
            missing.append(agent)
    if missing:
        return [
            "enlisted agent(s) missing from consent: "
            + ", ".join(sorted(set(missing)))
            + " (name them under CONSENT: or set EMPEROR_CONSENT_AGENTS)"
        ]
    return []


def validate(path: Path) -> list[str]:
    """Mechanical steal-consent checks for a task dir / consent / ledger file."""
    errors: list[str] = []
    if not path.exists():
        return [f"missing path: {path}"]

    text, _sources = _combined_text(path)
    root = path if path.is_dir() else path.parent
    agents = _iter_run_agents(root)
    if path.is_file():
        agents = agents or _iter_run_agents(path.parent)

    steal = _has_steal_signal(path if path.is_dir() else root, text)
    env = _env_agents()

    # CI standing: EMPEROR_CONSENT_AGENTS set
    if env is not None:
        if env == [] and (steal or agents):
            # "none" with steal activity → dark / refuse
            return [
                "EMPEROR_CONSENT_AGENTS=none (or empty) but steal activity present "
                f"— Steal Chain is dark (see {LEAF} / ci-mode.md)"
            ]
        if env and agents:
            errors.extend(_agent_coverage_errors(text, agents, env))
            return errors
        if env and steal and not agents:
            # Env standing covers dispatch without runs yet
            return []
        if env and not steal and not agents:
            return []
        # env set but no steal — vacuous / env-OK
        if not steal:
            return []

    if not steal:
        # Vacuous PASS — no steal activity to consent
        # Exception: explicit consent file check still validates structure
        # when the file *claims* to be a consent record (has CONSENT:).
        if path.is_file() and _CONSENT_HEADER.search(text):
            return _consent_structure_errors(text)
        if path.is_file() and path.name.lower() in {"consent.md"}:
            return _consent_structure_errors(text) or [
                "missing CONSENT record "
                f"(need 'CONSENT: task …' — see {LEAF})"
            ]
        return []

    # Steal activity: need ledger/file consent (or already handled via env)
    errors.extend(_consent_structure_errors(text))
    if not errors:
        errors.extend(_agent_coverage_errors(text, agents, env))

    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "CONSENT checklist=yes",
        f"CONSENT leaf={LEAF}",
        "CONSENT iron=NO_DISPATCH_WITHOUT_CONSENT_RECORD",
        "STEP 1 id=roster name=Present dowsed roster "
        "et=agent / state / version / one-line strength",
        "STEP 1 key=Include NEEDS SIGN-IN; NOT INSTALLED only if relevant",
        "STEP 2 id=ask name=Concrete ask with recommendation "
        "et=routing.md reason + cost/privacy in the ask",
        "STEP 2 key=Never open-ended 'which agents?'; solo if client unreachable",
        "STEP 3 id=standing name=Standing policy when granted "
        "et=quote client words; read narrowly; re-confirm stale",
        "STEP 3 key=CI uses EMPEROR_CONSENT_AGENTS instead of chat",
        "STEP 4 id=record name=Write CONSENT: task … agent → role "
        "et=per-task approval quote or standing policy cite",
        "STEP 4 key=Declined stays declined; no consent-shopping",
        "",
        "MUST: Before dispatching enlisted agents, write CONSENT: with "
        f"agent → role lines (or EMPEROR_CONSENT_AGENTS / honest solo). Open "
        f"{LEAF}; run scripts/emperor consent <task-dir>. G4 calls this "
        "module when steal activity is present.",
        "MUST-NOT: dispatch without a CONSENT line; CONSENT-header theater "
        "without assignment; treat forge EMPEROR_CONSENT_PR as Steal "
        "enlistment consent; re-ask declined agents this task.",
    ]
    return "\n".join(lines) + "\n"


def reject_no_consent() -> str:
    return (
        "REJECT NO CONSENT: HARD-GATE — Steal refuses dispatch / enlistment "
        "without a CONSENT: record (agent → role), standing policy quote, "
        "EMPEROR_CONSENT_AGENTS, or honest 'proceeded solo'. "
        f"Open {LEAF}; re-run scripts/emperor consent <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time Steal consent-protocol "
            "(CONSENT record + agent → role / CI env / solo)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir / consent file / ledger (omit to print CONSENT card)",
    )
    p.add_argument(
        "--check-consent",
        type=Path,
        metavar="PATH",
        default=None,
        help="consent-protocol check (exit 1 on soft/missing consent)",
    )
    p.add_argument(
        "--reject-no-consent",
        action="store_true",
        help="Hard-gate: refuse missing consent record (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_no_consent:
        sys.stdout.write(reject_no_consent())
        return 1

    target = args.check_consent if args.check_consent is not None else args.path
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    if not target.exists():
        return report_check("consent", target, errs, vacuous=False)
    text_blob, _ = _combined_text(target)
    root = target if target.is_dir() else target.parent
    agents = _iter_run_agents(root)
    if target.is_file():
        agents = agents or _iter_run_agents(target.parent)
    steal = _has_steal_signal(target if target.is_dir() else root, text_blob)
    forced = target.is_file() and (
        bool(_CONSENT_HEADER.search(text_blob))
        or target.name.lower() in {"consent.md"}
    )
    vacuous = (not steal) and (not forced) and (not agents)
    return report_check("consent", target, errs, vacuous=vacuous)


if __name__ == "__main__":
    raise SystemExit(main())
