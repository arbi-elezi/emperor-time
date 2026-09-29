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
  --emit / --ask-file / stdin / positional ask → print or --write PATH

Positional PATH runs --check-ask-spec. No args prints the ASK-SPEC card.
Thin twins: scripts/ask-spec.sh / scripts/ask-spec.ps1
G0 calls --require-spec (setup without a written spec FAILS).
G4 calls --check-ask-hints after harness class-caps-bind.
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
        "tiny-hint ask cannot declare medium/large (ASK_HINT_BIND)",
        "STEP 4 id=drive name=Do-once at proportional scale "
        "et=verify/critique cycles capped by class — see proportionality.py",
        "STEP 4 key=No museum of gates for a 2-line change",
        "",
        "MUST: Before heavy setup / repeated verify, emit ask→spec "
        f"(goal, done-when, out-of-scope, effort_class). Open {LEAF}; run "
        "scripts/emperor ask-spec --emit \"<ask>\" --write <task>/ask-spec.md.",
        "MUST-NOT: burn token budget on setup+verify loops without a scoped "
        "spec; run ~20 verifications for a tiny ask; declare effort_class:large "
        "on a fix-typo / one-line ask (ASK_HINT_BIND).",
        "HONESTY: --check-ask-spec / --check-ask-hints idle SKIP; "
        "G0 --require-spec never vacuous — setup without a written spec FAILS; "
        f"G4 --check-ask-hints FAILS on tiny-hint inflate (IRON={IRON_ASK_HINT}).",
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
