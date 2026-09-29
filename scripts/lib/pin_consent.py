#!/usr/bin/env python3
"""Validate Emperor Time Jail pin-and-consent HARD-GATE.

Doctrine: chains/chain-jail/pin-and-consent.md — Chain Jail may hunt; it may
not bind without pin (URL + hash + provenance) and a client consent line that
names **this captured skill**. Standing "you may hunt" is not standing
"you may fire". Adaptation never ends in use without this rite.

Always-fail HARD-GATE helpers:
  --reject-unpinned           refuse bind / fire without provenance pin
  --reject-no-skill-consent   refuse bind without named-skill client consent

Check mode:
  --check-pin-consent PATH    task dir / pin file / captured-skill / ledger
                              (exit 1 on soft / missing pin or consent)

Positional PATH runs the same check. No args prints the PIN-CONSENT card.
Thin twins: scripts/pin-and-consent.sh / scripts/pin-and-consent.ps1
Alias: jail-pin → same core.
G4 in gate.py calls --check-pin-consent when Jail pin activity is present
(activity-scoped; SKIP (vacuous — no activity) when no Jail pin markers).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence
from check_report import report_check

LEAF = "chains/chain-jail/pin-and-consent.md"

# Strong Jail pin / capture signals — weak "consent" alone is Steal's domain.
_JAIL_SIGNAL = re.compile(
    r"(?i)\b("
    r"pin-and-consent"
    r"|pin\s+and\s+consent"
    r"|chain[- ]jail"
    r"|captured[- ]skills?"
    r"|Captured\s+by\s+Chain\s+Jail"
    r"|source-url\s*:"
    r"|source-hash\s*:"
    r"|JAIL-CONSENT|JAIL\s+CONSENT"
    r"|jail[- ]pin"
    r"|bind\s+(?:this\s+)?captured"
    r"|fire\s+(?:this\s+)?captured"
    r"|adapt(?:ation|ed)?\s+(?:of\s+)?(?:a\s+)?captured"
    r"|provenance\s+header"
    r"|unpinned\s+(?:capture|skill|bind)"
    r")\b"
    r"|/\.emperor/captured-skills/"
    r"|\.emperor/captured-skills/"
)

_SOURCE_URL = re.compile(
    r"^\s{0,6}(?:[-*>]\s*)?(?:\*\*)?source-url(?:\*\*)?\s*:\s*\S+"
    r"|\bsource-url\s*:\s*https?://\S+"
    r"|Source:\s*https?://\S+",
    re.IGNORECASE | re.MULTILINE,
)

_SOURCE_HASH = re.compile(
    r"^\s{0,6}(?:[-*>]\s*)?(?:\*\*)?source-hash(?:\*\*)?\s*:\s*\S+"
    r"|\bsource-hash\s*:\s*(?:sha256:)?[0-9a-f]{7,}"
    r"|\b(?:sha256|git\s*SHA|commit)\s*[:=]\s*[0-9a-f]{7,}",
    re.IGNORECASE | re.MULTILINE,
)

# Optional provenance peers (soft theater if pin claimed without them).
_CAPTURED_AT = re.compile(
    r"\bcaptured-at\s*:\s*\S+"
    r"|Captured\s+by\s+Chain\s+Jail\s+on\s+\d{4}-\d{2}-\d{2}",
    re.IGNORECASE,
)
_LICENSE = re.compile(
    r"\blicense\s*:\s*\S+"
    r"|\(license:\s*[^)]+\)",
    re.IGNORECASE,
)
_ADAPTER = re.compile(
    r"\badapter\s*:\s*\S+"
    r"|\.emperor/captured-skills/[\w./-]+"
    r"|Adapted\s+for\s*:",
    re.IGNORECASE,
)

# Client consent naming THIS captured skill (not Steal enlistment CONSENT).
_SKILL_CONSENT = re.compile(
    r"("
    r"JAIL-CONSENT\s*:"
    r"|JAIL\s+CONSENT\s*:"
    r"|client\s+(?:said|wrote|quoted|approved|consented)[^\n]{0,120}"
    r"(?:captured|skill|pin|bind|fire|adapt)"
    r"|\"[^\"]{3,120}\"[^\n]{0,80}(?:consent|approved|yes)[^\n]{0,40}"
    r"(?:skill|capture|pin|bind|adapt)"
    r"|(?:consent|approved|yes)[^\n]{0,40}\"[^\"]{3,120}\""
    r"|named\s+(?:this\s+)?(?:captured\s+)?skill[^\n]{0,80}consent"
    r"|consent[^\n]{0,80}names?\s+(?:this\s+)?(?:captured\s+)?skill"
    r"|may\s+(?:bind|fire|adapt|use)\s+[^\n]{0,60}"
    r"(?:captured|\.emperor/captured-skills/)"
    r")",
    re.IGNORECASE,
)

_PIN_FILENAMES = {
    "pin-and-consent.md",
    "pin.md",
    "pin-consent.md",
    "jail-pin.md",
    "provenance.md",
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _iter_captured(root: Path) -> list[Path]:
    """Return captured-skill SKILL.md / provenance files under the task."""
    found: list[Path] = []
    for base_name in (".emperor/captured-skills", "captured-skills"):
        base = root / base_name
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".md", ".txt"}:
                found.append(path)
    return found


def _combined_text(task_or_file: Path) -> tuple[str, list[Path]]:
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    if not task_or_file.is_dir():
        return ("", [])
    parts: list[str] = []
    sources: list[Path] = []
    for name in (
        "pin-and-consent.md",
        "jail-consent.md",
        "pin.md",
        "pin-consent.md",
        "jail-pin.md",
        "provenance.md",
        "consent.md",
        "ledger.md",
        "claims.md",
        "claim-ledger.md",
        "DONE.md",
        "done.md",
        "admission.md",
        "adaptation.md",
        "capture.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
            sources.append(p)
    for cap in _iter_captured(task_or_file):
        parts.append(_read(cap))
        sources.append(cap)
    return ("\n".join(parts), sources)


def _has_jail_signal(path: Path, text: str) -> bool:
    root = path if path.is_dir() else path.parent
    if _iter_captured(root):
        return True
    if path.is_file() and path.name.lower() in _PIN_FILENAMES:
        return True
    if path.is_dir():
        for name in _PIN_FILENAMES:
            if (path / name).is_file():
                return True
        if (path / ".emperor" / "captured-skills").is_dir() or (
            path / "captured-skills"
        ).is_dir():
            return True
    return bool(_JAIL_SIGNAL.search(text))


def _pin_errors(text: str) -> list[str]:
    errors: list[str] = []
    has_url = bool(_SOURCE_URL.search(text))
    has_hash = bool(_SOURCE_HASH.search(text))
    if not has_url:
        errors.append(
            "missing pin source-url "
            f"(need source-url: <exact URL> — see {LEAF})"
        )
    if not has_hash:
        errors.append(
            "missing pin source-hash "
            f"(need source-hash: sha256… or git SHA — see {LEAF})"
        )
    # Soft theater: URL+hash present but provenance peers absent → still fail
    # when none of captured-at / license / adapter appear (incomplete pin).
    if has_url and has_hash:
        peers = (
            bool(_CAPTURED_AT.search(text)),
            bool(_LICENSE.search(text)),
            bool(_ADAPTER.search(text)),
        )
        if not any(peers):
            errors.append(
                "incomplete pin provenance "
                "(need captured-at: / license: / adapter: alongside "
                f"URL+hash — see {LEAF})"
            )
    return errors


def _consent_errors(text: str) -> list[str]:
    if _SKILL_CONSENT.search(text):
        return []
    return [
        "missing named-skill client consent "
        "(need JAIL-CONSENT: / client quote naming this captured skill — "
        f"standing 'you may hunt' is not 'you may fire' — see {LEAF})"
    ]


def validate(path: Path) -> list[str]:
    """Mechanical Jail pin+consent checks for a task dir / pin / ledger file."""
    if not path.exists():
        return [f"missing path: {path}"]

    text, _sources = _combined_text(path)
    active = _has_jail_signal(path, text)
    if not active:
        # Vacuous PASS — no Jail pin activity
        if path.is_file() and path.name.lower() in _PIN_FILENAMES:
            return _pin_errors(text) + _consent_errors(text)
        return []

    errors = _pin_errors(text) + _consent_errors(text)
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "PIN-CONSENT checklist=yes",
        f"PIN-CONSENT leaf={LEAF}",
        "PIN-CONSENT iron=PIN_THEN_CONSENT_BEFORE_ADAPT",
        "STEP 1 id=pin name=Pin provenance "
        "et=source-url + source-hash + captured-at + license + adapter",
        "STEP 1 key=No hash → no bind; re-fetch hash mismatch → quarantine",
        "STEP 2 id=consent name=Client names THIS captured skill "
        "et=JAIL-CONSENT: / quoted client yes on Task Ledger",
        "STEP 2 key=Standing you-may-hunt ≠ you-may-fire",
        "STEP 3 id=adapt name=Adapt only after pin+consent "
        "et=adaptation.md then trial-and-register — never direct use",
        "STEP 3 key=HARD-GATE --reject-unpinned / --reject-no-skill-consent",
        "STEP 4 id=injection name=Web text is CONJECTURE "
        "et=never paste hunted skill into always-on prompt / override vows",
        "STEP 4 key=Hostile until proven; Zetsu until pin+consent+trial",
        "",
        "MUST: Before binding / adapting / firing a captured skill, write the "
        f"provenance pin and named-skill consent. Open {LEAF}; run "
        "scripts/emperor pin-and-consent <task-dir>.",
        "MUST-NOT: fire unpinned capture; treat hunt standing as fire consent; "
        "adapt before pin+consent; paste web skill into always-on prompt.",
    ]
    return "\n".join(lines) + "\n"


def reject_unpinned() -> str:
    return (
        "REJECT UNPINNED: HARD-GATE — Chain Jail refuses bind / fire / adapt "
        "without provenance pin (source-url: + source-hash: + captured-at / "
        f"license / adapter). Open {LEAF}; re-run scripts/emperor "
        "pin-and-consent --check-pin-consent <task-dir>.\n"
    )


def reject_no_skill_consent() -> str:
    return (
        "REJECT NO SKILL CONSENT: HARD-GATE — Chain Jail refuses bind without "
        "a client consent line that names THIS captured skill (JAIL-CONSENT: / "
        "quoted yes). Standing 'you may hunt' is not 'you may fire'. "
        f"Open {LEAF}; re-run scripts/emperor pin-and-consent "
        "--check-pin-consent <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time Jail pin-and-consent "
            "(pin URL+hash + named-skill client consent before adaptation)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir / pin file / captured-skill / ledger (omit to print card)",
    )
    p.add_argument(
        "--check-pin-consent",
        type=Path,
        metavar="PATH",
        default=None,
        help="Jail pin+consent check (exit 1 on soft/missing pin or consent)",
    )
    p.add_argument(
        "--reject-unpinned",
        action="store_true",
        help="Hard-gate: refuse missing provenance pin (exit 1)",
    )
    p.add_argument(
        "--reject-no-skill-consent",
        action="store_true",
        help="Hard-gate: refuse missing named-skill client consent (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_unpinned:
        sys.stdout.write(reject_unpinned())
        return 1
    if args.reject_no_skill_consent:
        sys.stdout.write(reject_no_skill_consent())
        return 1

    target = (
        args.check_pin_consent
        if args.check_pin_consent is not None
        else args.path
    )
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    text_blob, _ = _combined_text(target) if target.exists() else ("", [])
    vacuous = target.exists() and not _has_jail_signal(target, text_blob)
    return report_check("pin-consent", target, errs, vacuous=vacuous)


if __name__ == "__main__":
    raise SystemExit(main())
