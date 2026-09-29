#!/usr/bin/env python3
"""Ask → scoped task spec HARD-GATE (Python core).

Translate a user ask into a minimal task spec *before* setup thrash:
  goal, done-when, out-of-scope, effort_class (tiny|small|medium|large).

Field failure (2026-09-29): agents burned whole token budgets on setup +
repeated verifications and never finished a small ask. Ask→spec forces a
scoped brief first; effort_class feeds proportionality caps.

Always-fail HARD-GATE helpers:
  --reject-no-spec          refuse without an ask→spec brief (card; exit 1)
  --require-spec PATH       always-on: missing/incomplete written spec FAILS
                            (never vacuous SKIP — thrash without a spec fails)
  --reject-over-ask-class   refuse when declared effort_class exceeds the
                            ask-text hint ceiling (tiny-hint ask → large)

Check / emit:
  --check-ask-spec PATH     activity-scoped idle check (SKIP vacuous when idle)
  --check-ask-hints PATH    activity-scoped: SKIP vacuous when no ask→spec;
                            FAIL when ask text has strong tiny hints but
                            declared effort_class is above tiny (ASK_HINT_BIND —
                            writing effort_class:large on a "fix typo" ask
                            can no longer unlock FORCE_TABLE[large] while
                            ASK_CLASS_BIND / CLASS_CAPS_BIND stay green)
  --reject-over-spec-class  refuse when declared effort_class exceeds the
                            hint ceiling of Ask(quoted)∪goal∪done-when
  --check-spec-hints PATH   activity-scoped: SKIP vacuous when no ask→spec;
                            FAIL when goal/done-when (or Ask quoted) has strong
                            tiny hints but declared effort_class is above tiny
                            (SPEC_HINT_BIND — park "fix typo" in goal while
                            Ask(quoted) stays clean can no longer unlock
                            FORCE_TABLE[large] while ASK_HINT_BIND stays green)
  --reject-over-scope-class refuse when declared effort_class exceeds the
                            hint ceiling of Ask∪goal∪done-when∪out-of-scope
  --check-scope-hints PATH  activity-scoped: SKIP vacuous when no ask→spec;
                            FAIL when out-of-scope (or Ask/goal/done-when) has
                            strong tiny hints but declared effort_class is
                            above tiny (SCOPE_HINT_BIND — park "fix typo" /
                            "one-line" in out-of-scope while Ask/goal/done-when
                            stay clean can no longer unlock FORCE_TABLE[large]
                            while SPEC_HINT_BIND stays green)
  --reject-over-body-class  refuse when declared effort_class exceeds the
                            hint ceiling of the full ask→spec file body
  --check-body-hints PATH   activity-scoped: SKIP vacuous when no ask→spec;
                            FAIL when any freeform section (## Notes /
                            ## Context / stray bullets) has strong tiny hints
                            but declared effort_class is above tiny
                            (BODY_HINT_BIND — park "fix typo" / "one-line" in
                            Notes while Ask/goal/done-when/out-of-scope stay
                            clean can no longer unlock FORCE_TABLE[large]
                            while SCOPE_HINT_BIND stays green)
  --reject-over-task-class  refuse when declared effort_class exceeds the
                            hint ceiling of the combined task-dir corpus
  --check-task-hints PATH   activity-scoped: SKIP vacuous when no ask→spec;
                            FAIL when ledger/work-order/brief/claims (or
                            ask-spec body) has strong tiny hints but declared
                            effort_class is above tiny
                            (TASK_HINT_BIND — park "fix typo" / "one-line" in
                            ledger.md / work-order.md while ask-spec.md body
                            stays clean can no longer unlock FORCE_TABLE[large]
                            while BODY_HINT_BIND stays green)
  --reject-over-notes-class refuse when declared effort_class exceeds the
                            hint ceiling of notes.md
  --check-notes-hints PATH  activity-scoped: SKIP vacuous when no ask→spec;
                            FAIL when notes.md has strong tiny hints but
                            declared effort_class is above tiny
                            (NOTES_HINT_BIND — park "fix typo" / "one-line" /
                            wording / trivial / nit / changelog only in
                            notes.md while ask-spec+ledger/work-order/brief/
                            claims stay clean can no longer unlock
                            FORCE_TABLE[large] while TASK_HINT_BIND stays green)
  --reject-over-plan-class  refuse when declared effort_class exceeds the
                            hint ceiling of PLAN.md / FINDINGS.md / PROGRESS.md
  --check-plan-hints PATH   activity-scoped: SKIP vacuous when no ask→spec;
                            FAIL when PLAN.md / FINDINGS.md / PROGRESS.md has
                            strong tiny hints but declared effort_class is
                            above tiny
                            (PLAN_HINT_BIND — park "fix typo" / "one-line" /
                            wording / trivial / nit / changelog only in
                            PLAN.md while ask-spec+ledger+notes stay clean
                            can no longer unlock FORCE_TABLE[large] while
                            NOTES_HINT_BIND stays green)
  --reject-over-state-class refuse when declared effort_class exceeds the
                            hint ceiling of STATE.md / state.md
  --check-state-hints PATH  activity-scoped: SKIP vacuous when no ask→spec;
                            FAIL when STATE.md / state.md has
                            strong tiny hints but declared effort_class is
                            above tiny
                            (STATE_HINT_BIND — park "fix typo" / "one-line" /
                            wording / trivial / nit / changelog only in
                            STATE.md while ask-spec+ledger+notes+plan stay clean
                            can no longer unlock FORCE_TABLE[large] while
                            PLAN_HINT_BIND stays green)
  --reject-over-done-class  refuse when declared effort_class exceeds the
                            hint ceiling of DONE.md / done.md
  --check-done-hints PATH   activity-scoped: SKIP vacuous when no ask→spec;
                            FAIL when DONE.md / done.md has
                            strong tiny hints but declared effort_class is
                            above tiny
                            (DONE_HINT_BIND — park "fix typo" / "one-line" /
                            wording / trivial / nit / changelog only in
                            DONE.md while ask-spec+ledger+notes+plan+state stay
                            clean can no longer unlock FORCE_TABLE[large] while
                            STATE_HINT_BIND stays green)
  --emit / --ask-file / stdin / positional ask → print or --write PATH

Positional PATH runs --check-ask-spec. No args prints the ASK-SPEC card.
Thin twins: scripts/ask-spec.sh / scripts/ask-spec.ps1
G0 calls --require-spec (setup without a written spec FAILS).
G4 calls --check-ask-hints after harness class-caps-bind.
G4 calls --check-spec-hints after --check-ask-hints.
G4 calls --check-scope-hints after --check-spec-hints.
G4 calls --check-body-hints after --check-scope-hints.
G4 calls --check-task-hints after --check-body-hints.
G4 calls --check-notes-hints after --check-task-hints.
G4 calls --check-plan-hints after --check-notes-hints.
G4 calls --check-state-hints after --check-plan-hints.
G4 calls --check-done-hints after --check-state-hints.
--check-ask-spec stays activity-scoped for idle honesty.
Length-only infer stays advisory; only strong _TINY_HINTS bind the ceiling.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence
from check_report import report_check

LEAF = "references/mechanical-gates.md"
EFFORT_CLASSES = ("tiny", "small", "medium", "large")

_ASK_SIGNAL = re.compile(
    r"(?i)\b("
    r"ask[- ]?spec"
    r"|ask\s*→\s*spec"
    r"|ask\s*-\s*>\s*spec"
    r"|effort[_ -]?class"
    r"|ASK_THEN_SPEC"
    r"|scoped\s+task\s+spec"
    r")\b"
    r"|ask-spec\.md"
)

_GOAL = re.compile(
    r"(?im)^\s{0,6}(?:[-*>]\s*)?(?:\*\*)?(?:goal|Goal):?(?:\*\*)?\s*:?\s*\S+"
    r"|^\s{0,6}#{1,6}\s+Goal\b"
)
_DONE_WHEN = re.compile(
    r"(?im)^\s{0,6}(?:[-*>]\s*)?(?:\*\*)?(?:done[- ]?when|Done[- ]?when|"
    r"acceptance\s+criteria):?(?:\*\*)?\s*:?\s*\S+"
    r"|^\s{0,6}#{1,6}\s+(?:Done[- ]?when|Acceptance\s+criteria)\b"
)
_OUT_OF_SCOPE = re.compile(
    r"(?im)^\s{0,6}(?:[-*>]\s*)?(?:\*\*)?(?:out[- ]?of[- ]?scope|"
    r"Out\s+of\s+scope):?(?:\*\*)?\s*:?\s*\S+"
    r"|^\s{0,6}#{1,6}\s+Out\s+of\s+scope\b"
)
_EFFORT = re.compile(
    r"(?im)(?:\*\*)?effort[_ -]?class:?\*?\*?\s*:?\s*(?:\*\*)?\s*"
    r"(tiny|small|medium|large)\b"
)

_TINY_HINTS = re.compile(
    r"(?i)\b("
    r"typo|rename|one[- ]line|1[- ]line|two[- ]line|2[- ]line|"
    r"bump\s+version|fix\s+typo|single[- ]file|one[- ]file|"
    r"trivial|nit|wording|changelog\s+only"
    r")\b"
)
_LARGE_HINTS = re.compile(
    r"(?i)\b("
    r"refactor|rewrite|migrate|migration|architecture|overhaul|"
    r"multi[- ]repo|platform|redesign|from\s+scratch"
    r")\b"
)
_SMALL_HINTS = re.compile(
    r"(?i)\b("
    r"add\s+flag|wire|thin\s+twin|alias|fixture|HARD-GATE|"
    r"lockstep|version\s+bump|small\s+fix|patch"
    r")\b"
)

_SPEC_FILENAMES = {
    "ask-spec.md",
    "ask_spec.md",
    "task-spec.md",
    "scoped-spec.md",
}

IRON_ASK_HINT = "ASK_HINT_BIND"
IRON_SPEC_HINT = "SPEC_HINT_BIND"
IRON_SCOPE_HINT = "SCOPE_HINT_BIND"
IRON_BODY_HINT = "BODY_HINT_BIND"
IRON_TASK_HINT = "TASK_HINT_BIND"
IRON_NOTES_HINT = "NOTES_HINT_BIND"
IRON_PLAN_HINT = "PLAN_HINT_BIND"
IRON_STATE_HINT = "STATE_HINT_BIND"
IRON_DONE_HINT = "DONE_HINT_BIND"
_CLASS_RANK = {"tiny": 0, "small": 1, "medium": 2, "large": 3}

_ASK_QUOTED = re.compile(
    r"(?ims)^#{1,6}\s+Ask\s*\(quoted\)\s*\n+(.*?)(?=^#{1,6}\s|\Z)"
)
_GOAL_VAL = re.compile(
    r"(?im)^\s{0,6}(?:[-*>]\s*)?(?:\*\*)?(?:goal|Goal):?(?:\*\*)?\s*:?\s*(.+)$"
)
_DONE_VAL = re.compile(
    r"(?im)^\s{0,6}(?:[-*>]\s*)?(?:\*\*)?(?:done[- ]?when|Done[- ]?when|"
    r"acceptance\s+criteria):?(?:\*\*)?\s*:?\s*(.+)$"
)
_OUT_OF_SCOPE_VAL = re.compile(
    r"(?im)^\s{0,6}(?:[-*>]\s*)?(?:\*\*)?(?:out[- ]?of[- ]?scope|"
    r"Out[- ]?of[- ]?scope|oos):?(?:\*\*)?\s*:?\s*(.+)$"
)


def _strip_md_noise(s: str) -> str:
    s = re.sub(r"^>\s?", "", s, flags=re.M)
    s = s.replace("**", "").replace("`", "")
    return s.strip()


def extract_ask_text(path: Path) -> str:
    """Ask body for hint binding: quoted Ask section, else goal (+ done-when)."""
    if not path.exists():
        return ""
    text_body, sources = _combined_text(path)
    # Prefer dedicated ask-spec file contents when present.
    root = path if path.is_dir() else path.parent
    for name in ("ask-spec.md", "ask_spec.md", "task-spec.md", "scoped-spec.md"):
        p = root / name
        if p.is_file():
            text_body = _read(p)
            break
    if path.is_file() and path.name.lower() in _SPEC_FILENAMES:
        text_body = _read(path)
    qm = _ASK_QUOTED.search(text_body)
    if qm:
        return _strip_md_noise(qm.group(1))
    parts: list[str] = []
    gm = _GOAL_VAL.search(text_body)
    if gm:
        parts.append(_strip_md_noise(gm.group(1)))
    dm = _DONE_VAL.search(text_body)
    if dm:
        parts.append(_strip_md_noise(dm.group(1)))
    return "\n".join(parts).strip()


def hint_ceiling(ask: str) -> str | None:
    """Max allowed effort_class from strong ask hints, or None (no bind).

    Only _TINY_HINTS bind (field-failure case: "fix typo" → large).
    _LARGE_HINTS lift the ceiling. Length-only infer stays advisory.
    """
    text_ask = (ask or "").strip()
    if not text_ask:
        return None
    if _LARGE_HINTS.search(text_ask):
        return None
    if _TINY_HINTS.search(text_ask):
        return "tiny"
    return None



def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _combined_text(task_or_file: Path) -> tuple[str, list[Path]]:
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    if not task_or_file.is_dir():
        return ("", [])
    parts: list[str] = []
    sources: list[Path] = []
    for name in (
        "ask-spec.md",
        "ask_spec.md",
        "task-spec.md",
        "scoped-spec.md",
        "ledger.md",
        "work-order.md",
        "brief.md",
        "claims.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
            sources.append(p)
    return ("\n".join(parts), sources)


def _has_ask_signal(path: Path, text: str) -> bool:
    if path.is_file() and path.name.lower() in _SPEC_FILENAMES:
        return True
    if path.is_dir():
        for name in _SPEC_FILENAMES:
            if (path / name).is_file():
                return True
    if _ASK_SIGNAL.search(text):
        return True
    if _EFFORT.search(text):
        return True
    return False


def infer_effort_class(ask: str) -> str:
    """Heuristic effort_class from ask text (overrideable in emitted spec)."""
    text = (ask or "").strip()
    n = len(text)
    if _LARGE_HINTS.search(text) or n >= 800:
        return "large"
    if _TINY_HINTS.search(text) or n <= 80:
        return "tiny"
    if _SMALL_HINTS.search(text) or n <= 240:
        return "small"
    if n <= 500:
        return "medium"
    return "large"


def emit_spec(
    ask: str,
    *,
    effort_class: str | None = None,
    goal: str | None = None,
    done_when: str | None = None,
    out_of_scope: str | None = None,
) -> str:
    """Emit a minimal ask→spec markdown block."""
    ask = (ask or "").strip()
    if not ask:
        raise ValueError("empty ask — cannot emit ask→spec")
    cls = (effort_class or infer_effort_class(ask)).lower().strip()
    if cls not in EFFORT_CLASSES:
        raise ValueError(f"effort_class must be one of {EFFORT_CLASSES}, got {cls}")
    # First sentence / line as default goal.
    first = re.split(r"[.\n]", ask, maxsplit=1)[0].strip() or ask[:120]
    g = (goal or first).strip()
    dw = (done_when or f"User ask satisfied: {first}").strip()
    oos = (
        out_of_scope
        or "Nen catalog growth; archaeology format museum; k8s emitter churn; "
        "unrelated drive-by refactors"
    ).strip()
    return (
        "# Ask → spec\n"
        f"\n"
        f"- **goal:** {g}\n"
        f"- **done-when:** {dw}\n"
        f"- **out-of-scope:** {oos}\n"
        f"- **effort_class:** {cls}\n"
        f"\n"
        f"## Ask (quoted)\n"
        f"\n"
        f"> {ask.replace(chr(10), chr(10) + '> ')}\n"
    )


def _field_errors(text: str) -> list[str]:
    errors: list[str] = []
    if not _GOAL.search(text):
        errors.append(
            f"missing goal: (need goal: <one sentence> — see {LEAF})"
        )
    if not _DONE_WHEN.search(text):
        errors.append(
            "missing done-when: / Acceptance criteria "
            f"(need done-when: <observable> — see {LEAF})"
        )
    if not _OUT_OF_SCOPE.search(text):
        errors.append(
            "missing out-of-scope: "
            f"(need out-of-scope: <what not to do> — see {LEAF})"
        )
    m = _EFFORT.search(text)
    if not m:
        errors.append(
            "missing effort_class: tiny|small|medium|large "
            f"(proportionality caps need a class — see {LEAF})"
        )
    return errors


def validate(path: Path) -> list[str]:
    """Mechanical ask→spec checks for a task dir / ask-spec / ledger file."""
    if not path.exists():
        return [f"missing path: {path}"]

    text, _sources = _combined_text(path)
    active = _has_ask_signal(path, text)
    if not active:
        # Vacuous PASS — no ask→spec activity on this task path.
        if path.is_file() and path.name.lower() in _SPEC_FILENAMES:
            return _field_errors(text)
        return []

    errors = _field_errors(text)
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def require_spec(path: Path) -> list[str]:
    """Always-on: missing or incomplete ask→spec fails (never vacuous).

    Used by G0 so SessionStart/skill/G0 holes cannot open setup
    without a written scoped brief.
    """
    if not path.exists():
        return [f"missing path: {path}"]

    text, _sources = _combined_text(path)
    active = _has_ask_signal(path, text)
    if not active:
        return [
            "missing ask→spec brief (need ask-spec.md with goal: / "
            "done-when: / out-of-scope: / effort_class: tiny|small|medium|large "
            f"— emit before setup thrash — see {LEAF})"
        ]

    errors = _field_errors(text)
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def parse_effort_class(path: Path) -> str | None:
    """Return effort_class from ask-spec / ledger, or None."""
    if not path.exists():
        return None
    text, _ = _combined_text(path)
    m = _EFFORT.search(text)
    if not m:
        return None
    for g in m.groups():
        if g:
            return g.lower()
    return None


def list_over_ask_class(path: Path) -> list[tuple[str, str]]:
    """Return (declared, ceiling) when declared exceeds hint ceiling; else []."""
    if not path.exists():
        return []
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return []
    ceiling = hint_ceiling(extract_ask_text(path))
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [(declared, ceiling)]
    return []


def validate_ask_hints(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no ask→spec (idle / vacuous).

    When ask→spec exists, FAIL if ask text has strong tiny hints but
    declared effort_class is above tiny. Closes ask-class inflate soft
    theater after CLASS_CAPS_BIND: writing effort_class:large on a
    "fix typo" ask can no longer unlock FORCE_TABLE[large] while
    ASK_CLASS_BIND / CLASS_TOOLS_BIND / CLASS_CAPS_BIND stay green.
    Tighter-than-hint class remains allowed. No tiny hints → no bind.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return [
            f"missing effort_class for ask-hint bind "
            f"({IRON_ASK_HINT}; see {LEAF})"
        ]
    ask = extract_ask_text(path)
    ceiling = hint_ceiling(ask)
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [
            f"ask→spec effort_class={declared} exceeds ask-hint ceiling="
            f"{ceiling} (tiny-hint ask cannot declare {declared} — "
            f"{IRON_ASK_HINT}; see {LEAF})"
        ]
    return []


def reject_over_ask_class() -> str:
    return (
        "REJECT OVER ASK CLASS: HARD-GATE — ask→spec effort_class must not "
        "exceed the ask-text hint ceiling. Agent cannot unlock "
        "FORCE_TABLE[large] / EFFORT_CAPS[large] by writing effort_class:large "
        "on a tiny-hint ask (fix typo / one-line / wording) while "
        "ASK_CLASS_BIND / CLASS_CAPS_BIND stay green. Tighter-than-hint class "
        f"remains allowed. Open {LEAF}; re-check with "
        f"--check-ask-hints <task-dir>. IRON={IRON_ASK_HINT}\n"
    )



def extract_hint_corpus(path: Path) -> str:
    """Hint corpus for SPEC_HINT_BIND: Ask(quoted) ∪ goal ∪ done-when.

    ASK_HINT_BIND binds Ask(quoted) alone (else goal+done-when). Parking
    tiny-hint language in goal/done-when while keeping Ask(quoted) clean
    bypassed ASK_HINT_BIND — this corpus closes that soft theater.
    """
    if not path.exists():
        return ""
    text_body, _sources = _combined_text(path)
    root = path if path.is_dir() else path.parent
    for name in ("ask-spec.md", "ask_spec.md", "task-spec.md", "scoped-spec.md"):
        candidate = root / name
        if candidate.is_file():
            text_body = _read(candidate)
            break
    if path.is_file() and path.name.lower() in _SPEC_FILENAMES:
        text_body = _read(path)
    parts: list[str] = []
    qm = _ASK_QUOTED.search(text_body)
    if qm:
        parts.append(_strip_md_noise(qm.group(1)))
    gm = _GOAL_VAL.search(text_body)
    if gm:
        parts.append(_strip_md_noise(gm.group(1)))
    dm = _DONE_VAL.search(text_body)
    if dm:
        parts.append(_strip_md_noise(dm.group(1)))
    return "\n".join(parts).strip()


def list_over_spec_class(path: Path) -> list[tuple[str, str]]:
    """Return (declared, ceiling) when declared exceeds spec-hint ceiling."""
    if not path.exists():
        return []
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return []
    ceiling = hint_ceiling(extract_hint_corpus(path))
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [(declared, ceiling)]
    return []


def validate_spec_hints(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no ask→spec (idle / vacuous).

    When ask→spec exists, FAIL if Ask(quoted)∪goal∪done-when has strong
    tiny hints but declared effort_class is above tiny. Closes goal-park
    soft theater after ASK_HINT_BIND: parking "fix typo" / "one-line" in
    goal/done-when while Ask(quoted) stays clean can no longer unlock
    FORCE_TABLE[large] while ASK_HINT_BIND stays green.
    Tighter-than-hint class remains allowed. No tiny hints → no bind.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return [
            f"missing effort_class for spec-hint bind "
            f"({IRON_SPEC_HINT}; see {LEAF})"
        ]
    corpus = extract_hint_corpus(path)
    ceiling = hint_ceiling(corpus)
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [
            f"ask→spec effort_class={declared} exceeds spec-hint ceiling="
            f"{ceiling} (goal/done-when/Ask tiny-hint cannot declare "
            f"{declared} — {IRON_SPEC_HINT}; see {LEAF})"
        ]
    return []


def reject_over_spec_class() -> str:
    return (
        "REJECT OVER SPEC CLASS: HARD-GATE — ask→spec effort_class must not "
        "exceed the hint ceiling of Ask(quoted)∪goal∪done-when. Agent cannot "
        "unlock FORCE_TABLE[large] / EFFORT_CAPS[large] by parking tiny-hint "
        "language in goal/done-when while Ask(quoted) stays clean and "
        "ASK_HINT_BIND stays green. Tighter-than-hint class remains allowed. "
        f"Open {LEAF}; re-check with --check-spec-hints <task-dir>. "
        f"IRON={IRON_SPEC_HINT}\n"
    )


def extract_scope_corpus(path: Path) -> str:
    """Hint corpus for SCOPE_HINT_BIND: Ask∪goal∪done-when∪out-of-scope.

    SPEC_HINT_BIND binds Ask∪goal∪done-when. Parking tiny-hint language in
    out-of-scope while keeping Ask/goal/done-when clean bypassed
    SPEC_HINT_BIND — this corpus closes that soft theater.
    """
    if not path.exists():
        return ""
    # Start from the spec-hint corpus, then append out-of-scope.
    parts: list[str] = []
    base = extract_hint_corpus(path)
    if base:
        parts.append(base)
    text_body, _sources = _combined_text(path)
    root = path if path.is_dir() else path.parent
    for name in ("ask-spec.md", "ask_spec.md", "task-spec.md", "scoped-spec.md"):
        candidate = root / name
        if candidate.is_file():
            text_body = _read(candidate)
            break
    if path.is_file() and path.name.lower() in _SPEC_FILENAMES:
        text_body = _read(path)
    om = _OUT_OF_SCOPE_VAL.search(text_body)
    if om:
        parts.append(_strip_md_noise(om.group(1)))
    return "\n".join(parts).strip()


def list_over_scope_class(path: Path) -> list[tuple[str, str]]:
    """Return (declared, ceiling) when declared exceeds scope-hint ceiling."""
    if not path.exists():
        return []
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return []
    ceiling = hint_ceiling(extract_scope_corpus(path))
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [(declared, ceiling)]
    return []


def validate_scope_hints(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no ask→spec (idle / vacuous).

    When ask→spec exists, FAIL if Ask∪goal∪done-when∪out-of-scope has strong
    tiny hints but declared effort_class is above tiny. Closes out-of-scope
    park soft theater after SPEC_HINT_BIND: parking "fix typo" / "one-line"
    in out-of-scope while Ask/goal/done-when stay clean can no longer unlock
    FORCE_TABLE[large] while SPEC_HINT_BIND stays green.
    Tighter-than-hint class remains allowed. No tiny hints → no bind.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return [
            f"missing effort_class for scope-hint bind "
            f"({IRON_SCOPE_HINT}; see {LEAF})"
        ]
    corpus = extract_scope_corpus(path)
    ceiling = hint_ceiling(corpus)
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [
            f"ask→spec effort_class={declared} exceeds scope-hint ceiling="
            f"{ceiling} (out-of-scope/Ask/goal/done-when tiny-hint cannot "
            f"declare {declared} — {IRON_SCOPE_HINT}; see {LEAF})"
        ]
    return []


def reject_over_scope_class() -> str:
    return (
        "REJECT OVER SCOPE CLASS: HARD-GATE — ask→spec effort_class must not "
        "exceed the hint ceiling of Ask(quoted)∪goal∪done-when∪out-of-scope. "
        "Agent cannot unlock FORCE_TABLE[large] / EFFORT_CAPS[large] by "
        "parking tiny-hint language in out-of-scope while Ask/goal/done-when "
        "stay clean and SPEC_HINT_BIND stays green. Tighter-than-hint class "
        f"remains allowed. Open {LEAF}; re-check with "
        f"--check-scope-hints <task-dir>. IRON={IRON_SCOPE_HINT}\n"
    )


def _ask_spec_file(path: Path) -> Path | None:
    """Resolve the ask→spec markdown file for body-hint corpus."""
    if path.is_file() and path.name.lower() in _SPEC_FILENAMES:
        return path
    root = path if path.is_dir() else path.parent
    for name in ("ask-spec.md", "ask_spec.md", "task-spec.md", "scoped-spec.md"):
        candidate = root / name
        if candidate.is_file():
            return candidate
    return None


def extract_body_corpus(path: Path) -> str:
    """Hint corpus for BODY_HINT_BIND: full ask→spec file prose.

    SCOPE_HINT_BIND binds Ask∪goal∪done-when∪out-of-scope only. Parking
    tiny-hint language in ## Notes / ## Context / stray bullets while those
    four fields stay clean bypassed SCOPE_HINT_BIND — this corpus closes
    that soft theater. effort_class declaration lines are stripped so the
    class token itself never feeds the ceiling.
    """
    if not path.exists():
        return ""
    spec = _ask_spec_file(path)
    if spec is None:
        return ""
    raw = _read(spec)
    # Drop effort_class lines so "effort_class: large" is not corpus noise.
    lines = []
    for line in raw.splitlines():
        if _EFFORT.search(line):
            continue
        lines.append(line)
    return _strip_md_noise("\n".join(lines))


def list_over_body_class(path: Path) -> list[tuple[str, str]]:
    """Return (declared, ceiling) when declared exceeds body-hint ceiling."""
    if not path.exists():
        return []
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return []
    ceiling = hint_ceiling(extract_body_corpus(path))
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [(declared, ceiling)]
    return []


def validate_body_hints(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no ask→spec (idle / vacuous).

    When ask→spec exists, FAIL if the full ask→spec file body has strong
    tiny hints but declared effort_class is above tiny. Closes Notes/freeform
    park soft theater after SCOPE_HINT_BIND: parking "fix typo" / "one-line"
    in ## Notes / ## Context / stray bullets while Ask/goal/done-when/
    out-of-scope stay clean can no longer unlock FORCE_TABLE[large] while
    SCOPE_HINT_BIND stays green.
    Tighter-than-hint class remains allowed. No tiny hints → no bind.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return [
            f"missing effort_class for body-hint bind "
            f"({IRON_BODY_HINT}; see {LEAF})"
        ]
    corpus = extract_body_corpus(path)
    ceiling = hint_ceiling(corpus)
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [
            f"ask→spec effort_class={declared} exceeds body-hint ceiling="
            f"{ceiling} (Notes/freeform/Ask/goal/done-when/out-of-scope "
            f"tiny-hint cannot declare {declared} — {IRON_BODY_HINT}; "
            f"see {LEAF})"
        ]
    return []


def reject_over_body_class() -> str:
    return (
        "REJECT OVER BODY CLASS: HARD-GATE — ask→spec effort_class must not "
        "exceed the hint ceiling of the full ask→spec file body. Agent cannot "
        "unlock FORCE_TABLE[large] / EFFORT_CAPS[large] by parking tiny-hint "
        "language in ## Notes / ## Context / stray bullets while "
        "Ask/goal/done-when/out-of-scope stay clean and SCOPE_HINT_BIND stays "
        "green. Tighter-than-hint class remains allowed. "
        f"Open {LEAF}; re-check with --check-body-hints <task-dir>. "
        f"IRON={IRON_BODY_HINT}\n"
    )



def extract_task_corpus(path: Path) -> str:
    """Hint corpus for TASK_HINT_BIND: combined task-dir prose.

    BODY_HINT_BIND binds the ask→spec file alone. Parking tiny-hint language
    in ledger.md / work-order.md / brief.md / claims.md while ask-spec.md
    (including ## Notes) stays clean bypassed BODY_HINT_BIND — this corpus
    closes that soft theater. effort_class declaration lines are stripped so
    the class token itself never feeds the ceiling.
    """
    if not path.exists():
        return ""
    raw, _sources = _combined_text(path)
    if not raw.strip():
        return ""
    lines = []
    for line in raw.splitlines():
        if _EFFORT.search(line):
            continue
        lines.append(line)
    return _strip_md_noise("\n".join(lines))


def list_over_task_class(path: Path) -> list[tuple[str, str]]:
    """Return (declared, ceiling) when declared exceeds task-hint ceiling."""
    if not path.exists():
        return []
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return []
    ceiling = hint_ceiling(extract_task_corpus(path))
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [(declared, ceiling)]
    return []


def validate_task_hints(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no ask→spec (idle / vacuous).

    When ask→spec exists, FAIL if the combined task-dir corpus (ask-spec +
    ledger / work-order / brief / claims) has strong tiny hints but declared
    effort_class is above tiny. Closes ledger-wide park soft theater after
    BODY_HINT_BIND: parking "fix typo" / "one-line" in ledger.md /
    work-order.md while ask-spec.md body stays clean can no longer unlock
    FORCE_TABLE[large] while BODY_HINT_BIND stays green.
    Tighter-than-hint class remains allowed. No tiny hints → no bind.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return [
            f"missing effort_class for task-hint bind "
            f"({IRON_TASK_HINT}; see {LEAF})"
        ]
    corpus = extract_task_corpus(path)
    ceiling = hint_ceiling(corpus)
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [
            f"ask→spec effort_class={declared} exceeds task-hint ceiling="
            f"{ceiling} (ledger/work-order/brief/claims/ask-spec "
            f"tiny-hint cannot declare {declared} — {IRON_TASK_HINT}; "
            f"see {LEAF})"
        ]
    return []


def reject_over_task_class() -> str:
    return (
        "REJECT OVER TASK CLASS: HARD-GATE — ask→spec effort_class must not "
        "exceed the hint ceiling of the combined task-dir corpus (ask-spec + "
        "ledger / work-order / brief / claims). Agent cannot "
        "unlock FORCE_TABLE[large] / EFFORT_CAPS[large] by parking tiny-hint "
        "language in ledger.md / work-order.md while ask-spec.md body stays "
        "clean and BODY_HINT_BIND stays "
        "green. Tighter-than-hint class remains allowed. "
        f"Open {LEAF}; re-check with --check-task-hints <task-dir>. "
        f"IRON={IRON_TASK_HINT}\n"
    )




def extract_notes_corpus(path: Path) -> str:
    """Hint corpus for NOTES_HINT_BIND: notes.md prose only.

    TASK_HINT_BIND binds ask-spec + ledger / work-order / brief / claims.
    Parking tiny-hint language in notes.md while that task corpus stays
    clean bypassed TASK_HINT_BIND — this corpus closes that soft theater.
    effort_class declaration lines are stripped so the class token itself
    never feeds the ceiling.
    """
    if not path.exists():
        return ""
    raw = ""
    if path.is_file():
        if path.name.lower() == "notes.md":
            raw = _read(path)
        else:
            sibling = path.parent / "notes.md"
            if sibling.is_file():
                raw = _read(sibling)
    elif path.is_dir():
        notes = path / "notes.md"
        if notes.is_file():
            raw = _read(notes)
    if not raw.strip():
        return ""
    lines = []
    for line in raw.splitlines():
        if _EFFORT.search(line):
            continue
        lines.append(line)
    return _strip_md_noise("\n".join(lines))


def list_over_notes_class(path: Path) -> list[tuple[str, str]]:
    """Return (declared, ceiling) when declared exceeds notes-hint ceiling."""
    if not path.exists():
        return []
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return []
    ceiling = hint_ceiling(extract_notes_corpus(path))
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [(declared, ceiling)]
    return []


def validate_notes_hints(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no ask→spec (idle / vacuous).

    When ask→spec exists, FAIL if notes.md has strong tiny hints but declared
    effort_class is above tiny. Closes notes.md park soft theater after
    TASK_HINT_BIND: parking "fix typo" / "one-line" / wording / trivial /
    nit / changelog only in notes.md while ask-spec+ledger/work-order/brief/
    claims stay clean can no longer unlock FORCE_TABLE[large] while
    TASK_HINT_BIND stays green.
    Tighter-than-hint class remains allowed. No tiny hints → no bind.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return [
            f"missing effort_class for notes-hint bind "
            f"({IRON_NOTES_HINT}; see {LEAF})"
        ]
    corpus = extract_notes_corpus(path)
    ceiling = hint_ceiling(corpus)
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [
            f"ask→spec effort_class={declared} exceeds notes-hint ceiling="
            f"{ceiling} (notes.md tiny-hint cannot declare {declared} — "
            f"{IRON_NOTES_HINT}; see {LEAF})"
        ]
    return []


def reject_over_notes_class() -> str:
    return (
        "REJECT OVER NOTES CLASS: HARD-GATE — ask→spec effort_class must not "
        "exceed the hint ceiling of notes.md. Agent cannot "
        "unlock FORCE_TABLE[large] / EFFORT_CAPS[large] by parking tiny-hint "
        "language in notes.md while ask-spec+ledger/work-order/brief/claims "
        "stay clean and TASK_HINT_BIND stays "
        "green. Tighter-than-hint class remains allowed. "
        f"Open {LEAF}; re-check with --check-notes-hints <task-dir>. "
        f"IRON={IRON_NOTES_HINT}\n"
    )




def _plan_file_names() -> tuple[str, ...]:
    """G2 resume plan artifacts (templates/plan-files.md)."""
    return ("PLAN.md", "FINDINGS.md", "PROGRESS.md", "plan.md", "findings.md", "progress.md")


def extract_plan_corpus(path: Path) -> str:
    """Hint corpus for PLAN_HINT_BIND: PLAN.md / FINDINGS.md / PROGRESS.md.

    NOTES_HINT_BIND binds notes.md alone. Parking tiny-hint language in
    PLAN.md / FINDINGS.md / PROGRESS.md while ask-spec+ledger+notes stay
    clean bypassed NOTES_HINT_BIND — this corpus closes that soft theater.
    effort_class declaration lines are stripped so the class token itself
    never feeds the ceiling.
    """
    if not path.exists():
        return ""
    parts: list[str] = []
    names = {n.lower() for n in _plan_file_names()}
    if path.is_file():
        if path.name.lower() in names:
            parts.append(_read(path))
        else:
            for name in _plan_file_names():
                sibling = path.parent / name
                if sibling.is_file():
                    parts.append(_read(sibling))
    elif path.is_dir():
        for name in _plan_file_names():
            p = path / name
            if p.is_file():
                parts.append(_read(p))
    raw = "\n".join(parts)
    if not raw.strip():
        return ""
    lines = []
    for line in raw.splitlines():
        if _EFFORT.search(line):
            continue
        lines.append(line)
    return _strip_md_noise("\n".join(lines))


def list_over_plan_class(path: Path) -> list[tuple[str, str]]:
    """Return (declared, ceiling) when declared exceeds plan-hint ceiling."""
    if not path.exists():
        return []
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return []
    ceiling = hint_ceiling(extract_plan_corpus(path))
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [(declared, ceiling)]
    return []


def validate_plan_hints(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no ask→spec (idle / vacuous).

    When ask→spec exists, FAIL if PLAN.md / FINDINGS.md / PROGRESS.md has
    strong tiny hints but declared effort_class is above tiny. Closes
    PLAN.md park soft theater after NOTES_HINT_BIND: parking "fix typo" /
    "one-line" / wording / trivial / nit / changelog only in PLAN.md while
    ask-spec+ledger+notes stay clean can no longer unlock FORCE_TABLE[large]
    while NOTES_HINT_BIND stays green.
    Tighter-than-hint class remains allowed. No tiny hints → no bind.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return [
            f"missing effort_class for plan-hint bind "
            f"({IRON_PLAN_HINT}; see {LEAF})"
        ]
    corpus = extract_plan_corpus(path)
    ceiling = hint_ceiling(corpus)
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [
            f"ask→spec effort_class={declared} exceeds plan-hint ceiling="
            f"{ceiling} (PLAN.md/FINDINGS.md/PROGRESS.md tiny-hint cannot "
            f"declare {declared} — {IRON_PLAN_HINT}; see {LEAF})"
        ]
    return []


def reject_over_plan_class() -> str:
    return (
        "REJECT OVER PLAN CLASS: HARD-GATE — ask→spec effort_class must not "
        "exceed the hint ceiling of PLAN.md / FINDINGS.md / PROGRESS.md. "
        "Agent cannot unlock FORCE_TABLE[large] / EFFORT_CAPS[large] by "
        "parking tiny-hint language in PLAN.md while ask-spec+ledger+notes "
        "stay clean and NOTES_HINT_BIND stays "
        "green. Tighter-than-hint class remains allowed. "
        f"Open {LEAF}; re-check with --check-plan-hints <task-dir>. "
        f"IRON={IRON_PLAN_HINT}\n"
    )






def _state_file_names() -> tuple[str, ...]:
    """Resume STATE disk (templates/STATE.md / templates/state.md)."""
    return ("STATE.md", "state.md")


def extract_state_corpus(path: Path) -> str:
    """Hint corpus for STATE_HINT_BIND: STATE.md / state.md.

    PLAN_HINT_BIND binds PLAN.md / FINDINGS.md / PROGRESS.md. Parking
    tiny-hint language in STATE.md while ask-spec+ledger+notes+plan stay
    clean bypassed PLAN_HINT_BIND — this corpus closes that soft theater.
    effort_class declaration lines are stripped so the class token itself
    never feeds the ceiling.
    """
    if not path.exists():
        return ""
    parts: list[str] = []
    names = {n.lower() for n in _state_file_names()}
    if path.is_file():
        if path.name.lower() in names:
            parts.append(_read(path))
        else:
            for name in _state_file_names():
                sibling = path.parent / name
                if sibling.is_file():
                    parts.append(_read(sibling))
                    break
    elif path.is_dir():
        for name in _state_file_names():
            sp = path / name
            if sp.is_file():
                parts.append(_read(sp))
                break
    raw = "\n".join(parts)
    if not raw.strip():
        return ""
    lines = []
    for line in raw.splitlines():
        if _EFFORT.search(line):
            continue
        lines.append(line)
    return _strip_md_noise("\n".join(lines))


def list_over_state_class(path: Path) -> list[tuple[str, str]]:
    """Return (declared, ceiling) when declared exceeds state-hint ceiling."""
    if not path.exists():
        return []
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return []
    ceiling = hint_ceiling(extract_state_corpus(path))
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [(declared, ceiling)]
    return []


def validate_state_hints(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no ask→spec (idle / vacuous).

    When ask→spec exists, FAIL if STATE.md / state.md has strong tiny hints
    but declared effort_class is above tiny. Closes STATE.md park soft
    theater after PLAN_HINT_BIND: parking "fix typo" / "one-line" /
    wording / trivial / nit / changelog only in STATE.md while
    ask-spec+ledger+notes+plan stay clean can no longer unlock
    FORCE_TABLE[large] while PLAN_HINT_BIND stays green.
    Tighter-than-hint class remains allowed. No tiny hints → no bind.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return [
            f"missing effort_class for state-hint bind "
            f"({IRON_STATE_HINT}; see {LEAF})"
        ]
    corpus = extract_state_corpus(path)
    ceiling = hint_ceiling(corpus)
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [
            f"ask→spec effort_class={declared} exceeds state-hint ceiling="
            f"{ceiling} (STATE.md/state.md tiny-hint cannot "
            f"declare {declared} — {IRON_STATE_HINT}; see {LEAF})"
        ]
    return []


def reject_over_state_class() -> str:
    return (
        "REJECT OVER STATE CLASS: HARD-GATE — ask→spec effort_class must not "
        "exceed the hint ceiling of STATE.md / state.md. "
        "Agent cannot unlock FORCE_TABLE[large] / EFFORT_CAPS[large] by "
        "parking tiny-hint language in STATE.md while ask-spec+ledger+notes+plan "
        "stay clean and PLAN_HINT_BIND stays "
        "green. Tighter-than-hint class remains allowed. "
        f"Open {LEAF}; re-check with --check-state-hints <task-dir>. "
        f"IRON={IRON_STATE_HINT}\n"
    )




def _done_file_names() -> tuple[str, ...]:
    """G1 DONE probes disk (templates/DONE.md / done.md)."""
    return ("DONE.md", "done.md")


def extract_done_corpus(path: Path) -> str:
    """Hint corpus for DONE_HINT_BIND: DONE.md / done.md.

    STATE_HINT_BIND binds STATE.md / state.md. Parking tiny-hint language
    in DONE.md while ask-spec+ledger+notes+plan+state stay clean bypassed
    STATE_HINT_BIND — this corpus closes that soft theater.
    effort_class declaration lines are stripped so the class token itself
    never feeds the ceiling.
    """
    if not path.exists():
        return ""
    parts: list[str] = []
    names = {n.lower() for n in _done_file_names()}
    if path.is_file():
        if path.name.lower() in names:
            parts.append(_read(path))
        else:
            for name in _done_file_names():
                sibling = path.parent / name
                if sibling.is_file():
                    parts.append(_read(sibling))
                    break
    elif path.is_dir():
        for name in _done_file_names():
            sp = path / name
            if sp.is_file():
                parts.append(_read(sp))
                break
    raw = "\n".join(parts)
    if not raw.strip():
        return ""
    lines = []
    for line in raw.splitlines():
        if _EFFORT.search(line):
            continue
        lines.append(line)
    return _strip_md_noise("\n".join(lines))


def list_over_done_class(path: Path) -> list[tuple[str, str]]:
    """Return (declared, ceiling) when declared exceeds done-hint ceiling."""
    if not path.exists():
        return []
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return []
    ceiling = hint_ceiling(extract_done_corpus(path))
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [(declared, ceiling)]
    return []


def validate_done_hints(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no ask→spec (idle / vacuous).

    When ask→spec exists, FAIL if DONE.md / done.md has strong tiny hints
    but declared effort_class is above tiny. Closes DONE.md park soft
    theater after STATE_HINT_BIND: parking "fix typo" / "one-line" /
    wording / trivial / nit / changelog only in DONE.md while
    ask-spec+ledger+notes+plan+state stay clean can no longer unlock
    FORCE_TABLE[large] while STATE_HINT_BIND stays green.
    Tighter-than-hint class remains allowed. No tiny hints → no bind.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    text_body, _ = _combined_text(path)
    if not _has_ask_signal(path, text_body):
        return []
    declared = parse_effort_class(path)
    if declared is None:
        return [
            f"missing effort_class for done-hint bind "
            f"({IRON_DONE_HINT}; see {LEAF})"
        ]
    corpus = extract_done_corpus(path)
    ceiling = hint_ceiling(corpus)
    if ceiling is None:
        return []
    if _CLASS_RANK[declared] > _CLASS_RANK[ceiling]:
        return [
            f"ask→spec effort_class={declared} exceeds done-hint ceiling="
            f"{ceiling} (DONE.md/done.md tiny-hint cannot "
            f"declare {declared} — {IRON_DONE_HINT}; see {LEAF})"
        ]
    return []


def reject_over_done_class() -> str:
    return (
        "REJECT OVER DONE CLASS: HARD-GATE — ask→spec effort_class must not "
        "exceed the hint ceiling of DONE.md / done.md. "
        "Agent cannot unlock FORCE_TABLE[large] / EFFORT_CAPS[large] by "
        "parking tiny-hint language in DONE.md while "
        "ask-spec+ledger+notes+plan+state "
        "stay clean and STATE_HINT_BIND stays "
        "green. Tighter-than-hint class remains allowed. "
        f"Open {LEAF}; re-check with --check-done-hints <task-dir>. "
        f"IRON={IRON_DONE_HINT}\n"
    )



def format_card() -> str:
    lines = [
        "ASK-SPEC checklist=yes",
        f"ASK-SPEC leaf={LEAF}",
        "ASK-SPEC iron=ASK_THEN_SPEC_BEFORE_SETUP",
        "STEP 1 id=quote name=Quote the user ask "
        "et=verbatim client ask (no paraphrase theater)",
        "STEP 1 key=Empty ask → refuse emit",
        "STEP 2 id=scope name=Write goal / done-when / out-of-scope "
        "et=ask-spec.md or ledger fields",
        "STEP 2 key=HARD-GATE --reject-no-spec / --require-spec / --check-ask-spec",
        "STEP 3 id=class name=Declare effort_class "
        "et=tiny|small|medium|large (feeds proportionality caps)",
        "STEP 3 key=tiny ≈ 1–5 lines / single-file; large = rewrite/migrate; "
        "tiny-hint ask cannot declare medium/large (ASK_HINT_BIND); goal/done-when tiny hints also bind (SPEC_HINT_BIND); out-of-scope tiny hints also bind (SCOPE_HINT_BIND); freeform Notes/body tiny hints also bind (BODY_HINT_BIND); ledger/work-order/brief/claims tiny hints also bind (TASK_HINT_BIND); notes.md tiny hints also bind (NOTES_HINT_BIND); PLAN.md/FINDINGS.md/PROGRESS.md tiny hints also bind (PLAN_HINT_BIND); STATE.md tiny hints also bind (STATE_HINT_BIND); DONE.md tiny hints also bind (DONE_HINT_BIND)",
        "STEP 4 id=drive name=Do-once at proportional scale "
        "et=verify/critique cycles capped by class — see proportionality.py",
        "STEP 4 key=No museum of gates for a 2-line change",
        "",
        "MUST: Before heavy setup / repeated verify, emit ask→spec "
        f"(goal, done-when, out-of-scope, effort_class). Open {LEAF}; run "
        "scripts/emperor ask-spec --emit \"<ask>\" --write <task>/ask-spec.md.",
        "MUST-NOT: burn token budget on setup+verify loops without a scoped "
        "spec; run ~20 verifications for a tiny ask; declare effort_class:large "
        "on a fix-typo / one-line ask (ASK_HINT_BIND); park tiny language in goal while Ask(quoted) stays clean (SPEC_HINT_BIND); park tiny language in out-of-scope while Ask/goal/done-when stay clean (SCOPE_HINT_BIND); park tiny language in ## Notes / freeform body while Ask/goal/done-when/out-of-scope stay clean (BODY_HINT_BIND); park tiny language in ledger.md / work-order.md while ask-spec.md body stays clean (TASK_HINT_BIND); park tiny language in notes.md while ask-spec+ledger stay clean (NOTES_HINT_BIND); park tiny language in PLAN.md / FINDINGS.md / PROGRESS.md while ask-spec+ledger+notes stay clean (PLAN_HINT_BIND); park tiny language in STATE.md while ask-spec+ledger+notes+plan stay clean (STATE_HINT_BIND); park tiny language in DONE.md while ask-spec+ledger+notes+plan+state stay clean (DONE_HINT_BIND).",
        "HONESTY: --check-ask-spec / --check-ask-hints idle SKIP; "
        "G0 --require-spec never vacuous — setup without a written spec FAILS; "
        f"G4 --check-ask-hints FAILS on tiny-hint inflate (IRON={IRON_ASK_HINT}); G4 --check-spec-hints FAILS on goal-park inflate (IRON={IRON_SPEC_HINT}); G4 --check-scope-hints FAILS on out-of-scope-park inflate (IRON={IRON_SCOPE_HINT}); G4 --check-body-hints FAILS on Notes/freeform-park inflate (IRON={IRON_BODY_HINT}); G4 --check-task-hints FAILS on ledger-park inflate (IRON={IRON_TASK_HINT}); G4 --check-notes-hints FAILS on notes.md-park inflate (IRON={IRON_NOTES_HINT}); G4 --check-plan-hints FAILS on PLAN.md-park inflate (IRON={IRON_PLAN_HINT}); G4 --check-state-hints FAILS on STATE.md-park inflate (IRON={IRON_STATE_HINT}); G4 --check-done-hints FAILS on DONE.md-park inflate (IRON={IRON_DONE_HINT}).",
    ]
    return "\n".join(lines) + "\n"


def reject_no_spec() -> str:
    return (
        "REJECT NO SPEC: HARD-GATE — task path refuses heavy setup without "
        "ask→spec (goal: + done-when: + out-of-scope: + effort_class: "
        "tiny|small|medium|large). Translate the ask first; then do-once at "
        f"proportional scale. Open {LEAF}; re-run scripts/emperor ask-spec "
        "--check-ask-spec <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Emperor Time ask→spec: emit/validate scoped task brief "
            "(goal / done-when / out-of-scope / effort_class) before setup thrash"
        )
    )
    p.add_argument(
        "path_or_ask",
        nargs="?",
        default=None,
        help="task dir / ask-spec file (check) OR ask text (with --emit)",
    )
    p.add_argument(
        "--check-ask-spec",
        type=Path,
        metavar="PATH",
        default=None,
        help="ask→spec check (exit 1 on soft/missing fields when active)",
    )
    p.add_argument(
        "--reject-no-spec",
        action="store_true",
        help="Hard-gate: refuse missing ask→spec (always exit 1)",
    )
    p.add_argument(
        "--require-spec",
        type=Path,
        metavar="PATH",
        default=None,
        help="Always-on: missing/incomplete written ask→spec FAILS (never vacuous)",
    )
    p.add_argument(
        "--check-ask-hints",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Ask-hint bind: FAIL when ask text has strong tiny hints but "
            "declared effort_class is above tiny; SKIP vacuous when no ask→spec"
        ),
    )
    p.add_argument(
        "--reject-over-ask-class",
        action="store_true",
        help=(
            "Hard-gate card: refuse when declared effort_class exceeds "
            "ask-text hint ceiling (tiny-hint → large)"
        ),
    )
    p.add_argument(
        "--check-spec-hints",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Spec-hint bind: FAIL when Ask(quoted)∪goal∪done-when has strong "
            "tiny hints but declared effort_class is above tiny; SKIP vacuous "
            "when no ask→spec"
        ),
    )
    p.add_argument(
        "--reject-over-spec-class",
        action="store_true",
        help=(
            "Hard-gate card: refuse when declared effort_class exceeds "
            "spec-hint corpus ceiling (goal-park tiny → large)"
        ),
    )
    p.add_argument(
        "--check-scope-hints",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Scope-hint bind: FAIL when Ask∪goal∪done-when∪out-of-scope has "
            "strong tiny hints but declared effort_class is above tiny; SKIP "
            "vacuous when no ask→spec"
        ),
    )
    p.add_argument(
        "--reject-over-scope-class",
        action="store_true",
        help=(
            "Hard-gate card: refuse when declared effort_class exceeds "
            "scope-hint corpus ceiling (out-of-scope-park tiny → large)"
        ),
    )
    p.add_argument(
        "--check-body-hints",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Body-hint bind: FAIL when full ask→spec file body has strong "
            "tiny hints but declared effort_class is above tiny; SKIP "
            "vacuous when no ask→spec"
        ),
    )
    p.add_argument(
        "--reject-over-body-class",
        action="store_true",
        help=(
            "Hard-gate card: refuse when declared effort_class exceeds "
            "body-hint corpus ceiling (Notes/freeform-park tiny → large)"
        ),
    )
    p.add_argument(
        "--check-task-hints",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Task-hint bind: FAIL when combined task-dir corpus (ask-spec + "
            "ledger / work-order / brief / claims) has strong tiny hints but "
            "declared effort_class is above tiny; SKIP vacuous when no ask→spec"
        ),
    )
    p.add_argument(
        "--reject-over-task-class",
        action="store_true",
        help=(
            "Hard-gate card: refuse when declared effort_class exceeds "
            "task-hint corpus ceiling (ledger-park tiny → large)"
        ),
    )
    p.add_argument(
        "--check-notes-hints",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Notes-hint bind: FAIL when notes.md has strong tiny hints but "
            "declared effort_class is above tiny; SKIP vacuous when no ask→spec"
        ),
    )
    p.add_argument(
        "--reject-over-notes-class",
        action="store_true",
        help=(
            "Hard-gate card: refuse when declared effort_class exceeds "
            "notes-hint corpus ceiling (notes.md-park tiny → large)"
        ),
    )
    p.add_argument(
        "--check-plan-hints",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Plan-hint bind: FAIL when PLAN.md / FINDINGS.md / PROGRESS.md "
            "has strong tiny hints but declared effort_class is above tiny; "
            "SKIP vacuous when no ask→spec"
        ),
    )
    p.add_argument(
        "--reject-over-plan-class",
        action="store_true",
        help=(
            "Hard-gate card: refuse when declared effort_class exceeds "
            "plan-hint corpus ceiling (PLAN.md-park tiny → large)"
        ),
    )
    p.add_argument(
        "--check-state-hints",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "State-hint bind: FAIL when STATE.md / state.md "
            "has strong tiny hints but declared effort_class is above tiny; "
            "SKIP vacuous when no ask→spec"
        ),
    )
    p.add_argument(
        "--reject-over-state-class",
        action="store_true",
        help=(
            "Hard-gate card: refuse when declared effort_class exceeds "
            "state-hint corpus ceiling (STATE.md-park tiny → large)"
        ),
    )
    p.add_argument(
        "--check-done-hints",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Done-hint bind: FAIL when DONE.md / done.md "
            "has strong tiny hints but declared effort_class is above tiny; "
            "SKIP vacuous when no ask→spec"
        ),
    )
    p.add_argument(
        "--reject-over-done-class",
        action="store_true",
        help=(
            "Hard-gate card: refuse when declared effort_class exceeds "
            "done-hint corpus ceiling (DONE.md-park tiny → large)"
        ),
    )
    p.add_argument(
        "--emit",
        action="store_true",
        help="Emit ask→spec from ask text / stdin / --ask-file",
    )
    p.add_argument(
        "--ask-file",
        type=Path,
        default=None,
        help="Read ask text from file (with --emit)",
    )
    p.add_argument(
        "--write",
        type=Path,
        default=None,
        help="Write emitted spec to PATH (implies --emit)",
    )
    p.add_argument(
        "--effort-class",
        choices=list(EFFORT_CLASSES),
        default=None,
        help="Override inferred effort_class on emit",
    )
    p.add_argument(
        "--goal",
        default=None,
        help="Override goal on emit",
    )
    p.add_argument(
        "--done-when",
        default=None,
        help="Override done-when on emit",
    )
    p.add_argument(
        "--out-of-scope",
        default=None,
        help="Override out-of-scope on emit",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_no_spec:
        sys.stdout.write(reject_no_spec())
        return 1

    if args.reject_over_ask_class:
        sys.stdout.write(reject_over_ask_class())
        return 1

    if args.reject_over_spec_class:
        sys.stdout.write(reject_over_spec_class())
        return 1

    if args.reject_over_scope_class:
        sys.stdout.write(reject_over_scope_class())
        return 1

    if args.reject_over_body_class:
        sys.stdout.write(reject_over_body_class())
        return 1

    if args.reject_over_task_class:
        sys.stdout.write(reject_over_task_class())
        return 1

    if args.reject_over_notes_class:
        sys.stdout.write(reject_over_notes_class())
        return 1

    if args.reject_over_done_class:
        sys.stdout.write(reject_over_done_class())
        return 1

    if args.check_done_hints is not None:
        target = args.check_done_hints
        errs = validate_done_hints(target)
        text_body, _ = _combined_text(target) if target.exists() else ("", [])
        vacuous = target.exists() and not _has_ask_signal(target, text_body)
        return report_check("done-hints", target, errs, vacuous=vacuous)

    if args.reject_over_state_class:
        sys.stdout.write(reject_over_state_class())
        return 1

    if args.check_state_hints is not None:
        target = args.check_state_hints
        errs = validate_state_hints(target)
        text_body, _ = _combined_text(target) if target.exists() else ("", [])
        vacuous = target.exists() and not _has_ask_signal(target, text_body)
        return report_check("state-hints", target, errs, vacuous=vacuous)

    if args.reject_over_plan_class:
        sys.stdout.write(reject_over_plan_class())
        return 1

    if args.check_plan_hints is not None:
        target = args.check_plan_hints
        errs = validate_plan_hints(target)
        text_body, _ = _combined_text(target) if target.exists() else ("", [])
        vacuous = target.exists() and not _has_ask_signal(target, text_body)
        return report_check("plan-hints", target, errs, vacuous=vacuous)

    if args.check_notes_hints is not None:
        target = args.check_notes_hints
        errs = validate_notes_hints(target)
        text_body, _ = _combined_text(target) if target.exists() else ("", [])
        vacuous = target.exists() and not _has_ask_signal(target, text_body)
        return report_check("notes-hints", target, errs, vacuous=vacuous)

    if args.check_task_hints is not None:
        target = args.check_task_hints
        errs = validate_task_hints(target)
        text_body, _ = _combined_text(target) if target.exists() else ("", [])
        vacuous = target.exists() and not _has_ask_signal(target, text_body)
        return report_check("task-hints", target, errs, vacuous=vacuous)

    if args.check_body_hints is not None:
        target = args.check_body_hints
        errs = validate_body_hints(target)
        text_body, _ = _combined_text(target) if target.exists() else ("", [])
        vacuous = target.exists() and not _has_ask_signal(target, text_body)
        return report_check("body-hints", target, errs, vacuous=vacuous)

    if args.check_scope_hints is not None:
        target = args.check_scope_hints
        errs = validate_scope_hints(target)
        text_body, _ = _combined_text(target) if target.exists() else ("", [])
        vacuous = target.exists() and not _has_ask_signal(target, text_body)
        return report_check("scope-hints", target, errs, vacuous=vacuous)

    if args.check_spec_hints is not None:
        target = args.check_spec_hints
        errs = validate_spec_hints(target)
        text_body, _ = _combined_text(target) if target.exists() else ("", [])
        vacuous = target.exists() and not _has_ask_signal(target, text_body)
        return report_check("spec-hints", target, errs, vacuous=vacuous)

    if args.check_ask_hints is not None:
        target = args.check_ask_hints
        errs = validate_ask_hints(target)
        text_body, _ = _combined_text(target) if target.exists() else ("", [])
        vacuous = target.exists() and not _has_ask_signal(target, text_body)
        return report_check("ask-hints", target, errs, vacuous=vacuous)

    if args.require_spec is not None:
        errs = require_spec(args.require_spec)
        # Always-on: never vacuous — missing brief is FAIL.
        return report_check(
            "ask-spec", args.require_spec, errs, vacuous=False
        )

    if args.emit or args.write is not None or args.ask_file is not None:
        ask = ""
        if args.ask_file is not None:
            if not args.ask_file.is_file():
                print(f"ask-spec FAIL: no such ask file: {args.ask_file}", file=sys.stderr)
                return 2
            ask = _read(args.ask_file)
        elif args.path_or_ask and not Path(args.path_or_ask).exists():
            ask = args.path_or_ask
        elif args.path_or_ask and Path(args.path_or_ask).is_file() and (
            Path(args.path_or_ask).suffix.lower() in {".txt", ".md"}
            and Path(args.path_or_ask).name.lower() not in _SPEC_FILENAMES
        ):
            # Treat as ask file when --emit and path looks like ask text file.
            ask = _read(Path(args.path_or_ask))
        elif args.path_or_ask:
            ask = args.path_or_ask
        else:
            if not sys.stdin.isatty():
                ask = sys.stdin.read()
        try:
            spec = emit_spec(
                ask,
                effort_class=args.effort_class,
                goal=args.goal,
                done_when=args.done_when,
                out_of_scope=args.out_of_scope,
            )
        except ValueError as exc:
            print(f"ask-spec FAIL: {exc}", file=sys.stderr)
            return 2
        if args.write is not None:
            args.write.parent.mkdir(parents=True, exist_ok=True)
            args.write.write_text(spec, encoding="utf-8")
            print(f"ask-spec: {args.write.resolve()}")
            # Also print effort_class for callers.
            cls = parse_effort_class(args.write) or args.effort_class or infer_effort_class(ask)
            print(f"effort_class: {cls}")
            return 0
        sys.stdout.write(spec)
        return 0

    target = (
        args.check_ask_spec
        if args.check_ask_spec is not None
        else (Path(args.path_or_ask) if args.path_or_ask else None)
    )
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    text, _sources = _combined_text(target) if target.exists() else ("", [])
    vacuous = target.exists() and not _has_ask_signal(target, text)
    return report_check("ask-spec", target, errs, vacuous=vacuous)


if __name__ == "__main__":
    raise SystemExit(main())
