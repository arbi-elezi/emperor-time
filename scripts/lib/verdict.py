#!/usr/bin/env python3
"""Validate Emperor Time Judgment verdict + Breach Register (G5).

Doctrine: chains/judgment-chain/verdicts-and-breaches.md — one ruling with
required citations; Breach Register honest (empty OK) or filled (no theater).

Harness-driven citations (HARNESS_DRIVES_G4_CHECKS):
  ask→spec effort_class → FORCE_TABLE Tools/Optional/Forbidden drives which
  verdict citation fields are required. Forbidden/unlisted → cite not required
  (tiny bare Verdict: PASS OK — no museum parenthetical). Tools → cite required
  and value must name an artifact (critique: absent FAILS). Optional unused →
  cite not required; Optional used → require non-absent. No plan → legacy
  always-on (all three fields; hetero: absent still OK).

Always-fail HARD-GATE helpers:
  --reject-hidden-breach   refuse empty/theater breach rows / soft verdict

Check mode:
  --check-verdict PATH   task dir or ledger file (exit 1 on soft verdict/breach)

Positional PATH runs the same check. No args prints the VERDICT card.
Thin twins: scripts/verdict.sh / scripts/verdict.ps1
Alias: breach → same core.
G5 in gate.py calls --check-verdict on the task dir.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence

LEAF = "chains/judgment-chain/verdicts-and-breaches.md"
TEMPLATE = "templates/task-ledger.md"

# Verdict: PASS | PASS-WITH-CONDITIONS (…) | FAIL → G2 (…)
_VERDICT_LINE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:\*\*)?Verdict(?:\*\*)?\s*:\s*(?P<body>.+\S)\s*$"
    r"|^\s*VERDICT\s*:\s*(?P<body2>.+\S)\s*$"
)

_DELIVERABLE = re.compile(
    r"(?is)^\s*(?:PASS-WITH-CONDITIONS\b(?P<cond>.*)|PASS\b(?!\s*-WITH))"
)

_FAIL_VERDICT = re.compile(r"(?is)^\s*FAIL\b")

# Citation fields on the verdict (doctrine hygiene).
# Harness drives which are required (HARNESS_DRIVES_G4_CHECKS).
_CITE_CLAIM = re.compile(r"(?i)claim\s*audit")
_CITE_CRITIQUE = re.compile(r"(?i)\bcritique\b")
_CITE_HETERO = re.compile(r"(?i)\bhetero(?:-?\s*critique)?\b")
_CITE_ABSENT = re.compile(
    r"(?i)^\s*(?:absent|n/?a|skipped?|none|unused|unlisted|forbidden|"
    r"not\s+run|vacuous|—|-|\.\.\.|…)\s*$"
)
# (label, harness tool name, field presence regex)
_CITE_SPECS: tuple[tuple[str, str, re.Pattern[str]], ...] = (
    ("claim audit", "claim-audit", _CITE_CLAIM),
    ("critique", "critique", _CITE_CRITIQUE),
    ("hetero", "review-pack", _CITE_HETERO),
)
IRON_G4 = "HARNESS_DRIVES_G4_CHECKS"

_BREACH_HEADER = re.compile(
    r"(?im)^#{1,6}\s+Breach\s+Register\b|^Breach\s+Register\s*$"
)

_HONEST_EMPTY = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:\*\*)?(?:empty|none|no\s+breaches?|n/?a|"
    r"\(none\)|\(empty\))(?:\*\*)?\s*$"
)

_EMPTYISH = re.compile(
    r"(?i)^\s*(?:[-–—.*]|\.\.\.|…)?\s*$"
)

_THEATER_CELL = re.compile(
    r"(?i)^\s*(?:tbd|todo|pending|placeholder|lorem|xxx|\.\.\.|…|-+|n/?a|"
    r"none|empty|\?+)\s*$"
)

_HEADERISH = re.compile(
    r"(?i)^\s*\|\s*Vow\b|^\s*\|\s*-{3,}|^\s*\|\s*#\s*\|"
)

_SECTION_END = re.compile(r"(?m)^#{1,6}\s+")


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _combined_text(task_or_file: Path) -> tuple[str, list[Path]]:
    """Return ledger text + source paths.

    PATH may be a task directory (ledger.md) or a single ledger / verdict file.
    """
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    if not task_or_file.is_dir():
        return ("", [])

    parts: list[str] = []
    sources: list[Path] = []
    for name in ("ledger.md", "verdict.md", "breaches.md"):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
            sources.append(p)
    return ("\n".join(parts), sources)


def _cells(line: str) -> list[str]:
    if not line.strip().startswith("|"):
        return []
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _breach_section(text: str) -> str | None:
    m = _BREACH_HEADER.search(text)
    if not m:
        return None
    start = m.end()
    rest = text[start:]
    # Cut at next same-or-higher section heading
    end_m = _SECTION_END.search(rest)
    if end_m:
        return rest[: end_m.start()]
    return rest


def _is_separator(cells: list[str]) -> bool:
    # Markdown separator row: |---|---| — not blank data rows.
    if not cells:
        return False
    dashed = [c for c in cells if re.fullmatch(r":?-{3,}:?", c)]
    return bool(dashed) and all(
        re.fullmatch(r":?-{3,}:?", c) or c == "" for c in cells
    )


def _cell_emptyish(cell: str) -> bool:
    return bool(_EMPTYISH.match(cell))


def _cell_theater(cell: str) -> bool:
    if _cell_emptyish(cell):
        return True
    return bool(_THEATER_CELL.match(cell.strip()))


def _iter_breach_rows(section: str) -> list[list[str]]:
    """Return data rows (list of cells) under Breach Register."""
    rows: list[list[str]] = []
    for line in section.splitlines():
        if not line.strip().startswith("|"):
            continue
        if _HEADERISH.search(line):
            cells = _cells(line)
            if _is_separator(cells):
                continue
            # Header row with "Vow" — skip
            if any(c.lower() in {"vow", "what happened", "discovered"} for c in cells):
                continue
        cells = _cells(line)
        if not cells or _is_separator(cells):
            continue
        rows.append(cells)
    return rows


def _row_all_theater(cells: list[str]) -> bool:
    # Doctrine row: Vow | what happened | discovered | remediation | lesson
    # Require at least 4 cells; pad short rows.
    if len(cells) < 4:
        return True
    # Check first five (or all if fewer)
    check = cells[:5] if len(cells) >= 5 else cells
    return all(_cell_theater(c) for c in check)


def _row_has_empty_required(cells: list[str]) -> bool:
    """True when a row pretends to be data but required cells are blank."""
    if len(cells) < 4:
        return True
    check = cells[:5] if len(cells) >= 5 else cells
    # Partially filled with blanks = empty breach row theater
    any_real = any(not _cell_theater(c) for c in check)
    any_empty = any(_cell_emptyish(c) for c in check)
    return any_real and any_empty or all(_cell_emptyish(c) for c in check)


def _check_breach_register(section: str) -> list[str]:
    errors: list[str] = []
    rows = _iter_breach_rows(section)

    # Explicit honest-empty marker outside the table
    honest = False
    for line in section.splitlines():
        if line.strip().startswith("|"):
            continue
        if _HONEST_EMPTY.match(line):
            honest = True
            break

    if not rows:
        # Header-only or "- empty" — honest empty is allowed.
        return errors

    empty_rows = 0
    theater_rows = 0
    real_rows = 0
    for cells in rows:
        if all(_cell_emptyish(c) for c in (cells[:5] if len(cells) >= 5 else cells)):
            empty_rows += 1
            continue
        if _row_all_theater(cells) or _row_has_empty_required(cells):
            theater_rows += 1
            continue
        real_rows += 1

    if empty_rows:
        errors.append(
            f"empty breach row(s) ({empty_rows}) — blank register lines are "
            "hidden-breach theater; delete them or fill Vow/what/discovered/"
            "remediation/lesson, or mark the register honestly empty"
        )
    if theater_rows and real_rows == 0:
        errors.append(
            "theater-only Breach Register — TBD/TODO/placeholder rows are not "
            "Stake of Retribution entries; fill real cells or mark empty"
        )
    elif theater_rows:
        errors.append(
            f"theater breach row(s) ({theater_rows}) — placeholder cells "
            "(TBD/TODO/empty) fail the Stake; fill or remove"
        )
    # If we had rows but somehow none classified and not honest — shouldn't happen
    if empty_rows == 0 and theater_rows == 0 and real_rows == 0 and not honest:
        errors.append("Breach Register has no usable rows")
    return errors


def _verdict_body(text: str) -> str | None:
    for line in text.splitlines():
        m = _VERDICT_LINE.match(line)
        if not m:
            continue
        body = m.group("body") or m.group("body2") or ""
        return body.strip()
    return None



def _cite_value(clean: str, label: str) -> str | None:
    """Extract value after 'label:' inside a verdict citation parenthetical."""
    pat = re.compile(
        rf"(?i){re.escape(label)}\s*:\s*([^;)]+)"
    )
    m = pat.search(clean)
    if not m:
        return None
    return m.group(1).strip()


def _citation_required(path: Path, tool: str) -> bool:
    """Whether harness requires a non-absent citation for *tool*.

    skip → False (forbidden/unlisted — no cite museum)
    activity + unused → False
    activity + used / require / always → True
    Import failure → True (legacy fail-closed on cites)
    """
    try:
        from harness_plan import g4_check_mode, tool_was_used
    except Exception:
        return True
    mode = g4_check_mode(path, tool)
    if mode == "skip":
        return False
    if mode == "activity":
        root = path if path.is_dir() else path.parent
        return tool_was_used(root, tool)
    return True  # require | always


def _check_verdict(text: str, path: Path | None = None) -> list[str]:
    errors: list[str] = []
    body = _verdict_body(text)
    if body is None:
        errors.append(
            "missing Verdict line "
            "(need 'Verdict: PASS|PASS-WITH-CONDITIONS|FAIL → <phase>' "
            f"— open {TEMPLATE})"
        )
        return errors

    # Strip markdown bold markers for matching
    clean = re.sub(r"\*+", "", body).strip()

    if _FAIL_VERDICT.match(clean):
        errors.append(
            "verdict is FAIL — G5 requires PASS or PASS-WITH-CONDITIONS "
            "(re-enter at the named phase; do not deliver)"
        )
        return errors

    dm = _DELIVERABLE.match(clean)
    if not dm:
        errors.append(
            f"verdict body not a deliverable ruling: {body!r} "
            "(need PASS or PASS-WITH-CONDITIONS; 'PASS, mostly' is not a verdict)"
        )
        return errors

    # PASS-WITH-CONDITIONS must name at least one condition
    if re.match(r"(?i)^\s*PASS-WITH-CONDITIONS\b", clean):
        cond = (dm.group("cond") or "").strip()
        # Drop citation parenthetical for condition check
        cond_wo_cite = re.sub(
            r"\(claim\s*audit:.*$", "", cond, flags=re.I
        ).strip()
        cond_wo_cite = cond_wo_cite.strip(" :—–-()")
        if not cond_wo_cite or _EMPTYISH.match(cond_wo_cite):
            # Allow conditions listed after colon on same line with real words
            if not re.search(
                r"(?i)PASS-WITH-CONDITIONS\s*[:(\[]\s*\S+", clean
            ):
                errors.append(
                    "PASS-WITH-CONDITIONS missing named conditions "
                    "(a silent condition is a hidden defect)"
                )

    # Harness-driven citation fields (HARNESS_DRIVES_G4_CHECKS).
    # No plan / bare file → legacy always-on (all three fields; absent OK).
    # Plan skip → field not required. Plan require → field + non-absent value.
    missing_cite: list[str] = []
    for label, tool, pat in _CITE_SPECS:
        required = True if path is None else _citation_required(path, tool)
        if not required:
            continue
        if not pat.search(clean):
            missing_cite.append(label)
            continue
        # require/always with a present field: refuse absent theater when
        # harness selected the tool (require/activity-used). Legacy always
        # still allows hetero: absent (field present is enough).
        if path is not None:
            try:
                from harness_plan import g4_check_mode

                mode = g4_check_mode(path, tool)
            except Exception:
                mode = "always"
            if mode in ("require", "activity"):
                val = _cite_value(clean, label)
                if val is not None and _CITE_ABSENT.match(val):
                    errors.append(
                        f"verdict cites {label}: {val!r} but harness requires "
                        f"{tool} ({IRON_G4} — name the artifact, not absent)"
                    )
    if missing_cite:
        errors.append(
            "verdict missing required citation fields: "
            + ", ".join(missing_cite)
            + " — need (claim audit: …; critique: …; hetero: <file|absent>) "
            + f"when harness selects those tools ({IRON_G4})"
        )
    return errors


def validate(path: Path) -> list[str]:
    """Mechanical verdict + Breach Register checks for a task dir or ledger."""
    errors: list[str] = []
    if not path.exists():
        return [f"missing path: {path}"]

    text, _sources = _combined_text(path)
    if not text.strip():
        return [
            f"no ledger.md under {path} "
            f"(verdict + Breach Register need a ledger — open {TEMPLATE})"
        ]

    section = _breach_section(text)
    if section is None:
        errors.append(
            "Breach Register missing (must exist even if honestly empty)"
        )
    else:
        errors.extend(_check_breach_register(section))

    errors.extend(_check_verdict(text, path))

    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "VERDICT checklist=yes",
        f"VERDICT leaf={LEAF}",
        f"VERDICT template={TEMPLATE}",
        "VERDICT iron=NO_G5_WITHOUT_VERDICT_AND_HONEST_BREACH_REGISTER",
        "STEP 1 id=ruling name=One deliverable ruling "
        "et=Verdict: PASS | PASS-WITH-CONDITIONS (<named>) | FAIL → phase",
        "STEP 1 key='PASS, mostly' is not a verdict; FAIL does not open G5",
        "STEP 2 id=citations name=Verdict cites trial record "
        "et=(claim audit: …; critique: <file>; hetero: <file|absent>) "
        "when harness selects those tools",
        f"STEP 2 key={IRON_G4} — tiny SKIP → bare Verdict: PASS OK; "
        "Tools → refuse *: absent",
        "STEP 3 id=breach-register name=Breach Register present "
        "et=header + honest empty OR filled Stake rows",
        "STEP 3 key=Header-only / '- empty' OK; blank/TBD rows = hidden breach",
        "STEP 4 id=stake-rows name=No empty/theater rows "
        "et=Vow | what happened | discovered | remediation | lesson — all filled",
        "STEP 4 key=Theater-only register fails; real rows must not have blanks",
        "",
        "MUST: Before G5, ledger carries a deliverable Verdict and an honest "
        f"Breach Register. Citations follow harness plan ({IRON_G4}): skip → "
        "no cite museum; Tools → name artifacts (not absent). Open {LEAF}; "
        "run scripts/emperor verdict <task-dir>. G5 calls this module.",
        "MUST-NOT: PASS-substring theater; empty breach rows; TBD-only register; "
        "silent PASS-WITH-CONDITIONS; FAIL delivered as G5; critique: absent "
        "while harness Tools require critique.",
    ]
    return "\n".join(lines) + "\n"


def reject_hidden_breach() -> str:
    return (
        "REJECT HIDDEN BREACH: HARD-GATE — G5 refuses empty/theater Breach "
        "Register rows and missing Verdict citations. Breach Register header "
        "alone with blank/TBD rows is hidden-breach theater. "
        f"Open {LEAF}; fill {TEMPLATE} Verdict + Breach Register; "
        "re-run scripts/emperor verdict <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time Judgment verdict + Breach Register "
            "(deliverable ruling + honest Stake rows)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir or ledger file (omit to print VERDICT card)",
    )
    p.add_argument(
        "--check-verdict",
        type=Path,
        metavar="PATH",
        default=None,
        help="verdict + breach structure check (exit 1 on soft/hidden breach)",
    )
    p.add_argument(
        "--reject-hidden-breach",
        action="store_true",
        help="Hard-gate: refuse empty/theater breach + soft verdict (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_hidden_breach:
        sys.stdout.write(reject_hidden_breach())
        return 1

    target = args.check_verdict if args.check_verdict is not None else args.path
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    if errs:
        for e in errs:
            print(f"verdict FAIL: {e}", file=sys.stderr)
        return 1
    print(f"verdict PASS: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
