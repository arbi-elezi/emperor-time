#!/usr/bin/env python3
"""Diagnosing HARD-GATE card for emperor-heal (Python core).

Leaf adapted from obra/superpowers skills/diagnosing-superpowers
SKILL.md (MIT) — Core principle (citation iron law) + Intake before
analysis Hard rule + Report step (write a cite-or-fail report path).
Emperor Time + emperor-heal stay the orchestrator; do not announce the
foreign skill name. Does not vendor diagnosing-superpowers (no analyst
prompts, 7-dimension case/report templates, bundles, or GitHub-issue
workflow).

Prints DIAGNOSE / INTAKE / CITE / REPORT / MUST lines.
Always-fail HARD-GATE helpers:
  --reject-uncited       refuse finding without path:line
  --reject-skip-intake   refuse analysis before partner intake
  --reject-no-report     refuse claiming done without a report path

Check modes:
  --check-citation TEXT  exit 0 when TEXT contains path:line
  --check-report PATH    exit 0 when report skeleton is cite-or-fail OK
                         (problem statement + session(s) + findings with
                         path:line, or honest none-found)

Locate of transcript paths stays with session-discovery; this leaf gates
intake + citation honesty + report skeleton after locate.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence

LEAF = "skills/emperor-heal/diagnosing.md"
SOURCE = (
    "obra/superpowers diagnosing-superpowers → "
    "Core principle + Intake before analysis + Report (path only)"
)
IRON_CITE = "NO_FINDING_WITHOUT_PATH_LINE_CITATION"
IRON_INTAKE = "INTAKE_BEFORE_ANALYSIS"
IRON_REPORT = "CITE_OR_FAIL_REPORT"

# path:line — absolute or relative path, then colon, then digits
CITATION_RE = re.compile(r"(?:^|[\s`\"'(])([A-Za-z0-9_./\\~-]+\.[A-Za-z0-9_]+):(\d+)\b")

INTAKE_FIELDS: list[dict[str, str]] = [
    {
        "id": "sessions",
        "name": "Session(s)",
        "need": "Named session id(s) and/or VERIFIED path(s) via session-discovery",
    },
    {
        "id": "expected",
        "name": "Expected",
        "need": "What the human partner expected to happen",
    },
    {
        "id": "happened",
        "name": "Happened",
        "need": "What was observed instead (not a reconstructed guess)",
    },
    {
        "id": "observable",
        "name": "Observable",
        "need": "Concrete care-about: wall-clock, tokens, repeated actions, one specific action",
    },
]

# Mechanical report skeleton sections (ET-owned; not SP 7-analyst templates).
REPORT_SECTIONS: list[dict[str, str]] = [
    {
        "id": "problem",
        "name": "Problem statement",
        "need": "Partner-answered statement (sessions + expected + happened + observable)",
    },
    {
        "id": "sessions",
        "name": "Session(s)",
        "need": "VERIFIED path(s) and/or session id(s) examined",
    },
    {
        "id": "findings",
        "name": "Findings",
        "need": "Each finding cites path:line, or honest none-found with checked note",
    },
]

_PROBLEM_LINE = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Problem\s+statement)(?:\*\*)?\s*:\s*"
    r"(?P<body>.+\S)\s*$|"
    r"^#{1,6}\s*(?:\d+\.\s*)?Problem\s+statement\b(?P<header>.*)$",
    re.I | re.M,
)

_SESSION_LINE = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Session(?:\(s\))?s?(?:\s+examined)?|"
    r"Sessions\s+examined)(?:\*\*)?\s*:\s*(?P<body>.+\S)\s*$|"
    r"^#{1,6}\s*(?:\d+\.\s*)?Sessions?\s+examined\b(?P<header>.*)$",
    re.I | re.M,
)

_FINDINGS_HEADER = re.compile(
    r"^#{1,6}\s*(?:\d+\.\s*)?Findings\b|"
    r"^\s*(?:[-*]\s*)?(?:\*\*)?Findings(?:\*\*)?\s*:",
    re.I | re.M,
)

_NONE_FOUND = re.compile(
    r"(?i)\bnone\s+found\b(?:\s*[—–-]\s*|\s+)?(?:checked\b)?"
)

_THEATER = re.compile(
    r"(?i)^\s*(?:tbd|todo|pending|placeholder|\?+|n/?a|none|empty|"
    r"skipped?|not\s+yet|-|\.\.\.|…|lorem\s+ipsum)\s*$"
)

_FINDING_BULLET = re.compile(
    r"(?im)^\s*(?:[-*]\s+|finding\s*:\s*|#{2,6}\s*\d+(?:\.\d+)?\s+)"
    r"(?P<body>.+\S)\s*$"
)


def format_card() -> str:
    lines = [
        "DIAGNOSE checklist=yes",
        f"DIAGNOSE leaf={LEAF}",
        f"DIAGNOSE source={SOURCE}",
        f"DIAGNOSE iron={IRON_CITE}",
        f"DIAGNOSE iron={IRON_INTAKE}",
        f"DIAGNOSE iron={IRON_REPORT}",
        "DIAGNOSE locate=scripts/emperor session-discovery (VERIFIED path first)",
    ]
    for f in INTAKE_FIELDS:
        lines.append(
            f"INTAKE field={f['id']} name={f['name']} status=REQUIRED need={f['need']}"
        )
    lines.append(
        "INTAKE rule=one_question_at_a_time until a problem statement can be written"
    )
    lines.append(
        "INTAKE rule=complaint_is_not_statement "
        "('it took too long' needs an observable)"
    )
    lines.append(
        "INTAKE rule=partner_away → write questions and STOP; "
        "do not reconstruct their answer"
    )
    lines.append(
        "CITE rule=every_finding_needs_path_line (path:line); no citation → drop finding"
    )
    lines.append(
        "CITE rule=numbers_from_transcript_or_command_only; never from memory"
    )
    lines.append(
        "CITE rule=discard_returned_finding_without_path_line"
    )
    lines.append(
        "REPORT skeleton=problem_statement+sessions+findings "
        "(cite-or-fail; not SP 7-analyst templates)"
    )
    for s in REPORT_SECTIONS:
        lines.append(
            f"REPORT section={s['id']} name={s['name']} status=REQUIRED need={s['need']}"
        )
    lines.append(
        "REPORT rule=write_report_to_workspace_path_before_claiming_done"
    )
    lines.append(
        "REPORT rule=findings_cite_path_line_or_none_found_checked"
    )
    lines.append("")
    lines.append(
        "MUST: Finish intake (partner-answered problem statement) before "
        "locate/triage/report. Locate via session-discovery to VERIFIED paths. "
        "Every finding cites path:line. Write a cite-or-fail report file "
        f"(problem statement + session(s) + findings) and give the path. "
        f"Open {LEAF}. Run scripts/emperor diagnose --check-report <path>."
    )
    lines.append(
        "MUST-NOT: invent numbers or findings; skip intake because 'obvious'; "
        "start analysis while partner is away; claim diagnosis done without a "
        "report path; load whole diagnosing-superpowers (analyst prompts, "
        "7-dimension templates, bundles, issue workflow). "
        "ET + emperor-heal remain the orchestrator."
    )
    return "\n".join(lines) + "\n"


def reject_uncited() -> str:
    return (
        "REJECT UNCITED: HARD-GATE — no finding without a path:line citation. "
        "Every number must come from a transcript or a command you ran. "
        f"Open {LEAF}. Re-run scripts/emperor diagnose --check-citation \"...\".\n"
    )


def reject_skip_intake() -> str:
    return (
        "REJECT SKIP INTAKE: HARD-GATE — intake before analysis. "
        "Nothing in locate/triage/report starts until the human partner has "
        "answered. If they are away, write the questions and stop. "
        f"Open {LEAF}.\n"
    )


def reject_no_report() -> str:
    return (
        "REJECT NO REPORT: HARD-GATE — diagnose refuses without a written "
        "cite-or-fail report path (problem statement + session(s) + findings "
        "with path:line, or honest none-found). Do not claim diagnosis done "
        "from intake+cite theater alone. "
        f"Open {LEAF}; run scripts/emperor diagnose --check-report <path>.\n"
    )


def check_citation(text: str) -> tuple[bool, str]:
    """Return (ok, message). ok True when at least one path:line is present."""
    hits = CITATION_RE.findall(text or "")
    if hits:
        shown = ", ".join(f"{p}:{n}" for p, n in hits[:5])
        more = f" (+{len(hits) - 5} more)" if len(hits) > 5 else ""
        return True, f"CITE OK: found {len(hits)} citation(s): {shown}{more}\n"
    return (
        False,
        "CITE FAIL: no path:line citation in text. "
        f"Iron={IRON_CITE}. Drop the finding or add evidence. Open {LEAF}.\n",
    )


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _combined_report(task_or_file: Path) -> tuple[str, list[Path]]:
    """Return report text + source paths.

    PATH may be a report file or a directory containing report.md /
    diagnose-report.md / diagnosis.md / diagnosing.md.
    """
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    if not task_or_file.is_dir():
        return ("", [])

    parts: list[str] = []
    sources: list[Path] = []
    for name in (
        "report.md",
        "diagnose-report.md",
        "diagnosis.md",
        "diagnosing.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
            sources.append(p)
    return ("\n".join(parts), sources)


def _strip_md(s: str) -> str:
    t = s.strip()
    t = re.sub(r"^\*+\s*", "", t)
    t = re.sub(r"\s*\*+$", "", t)
    return t.strip().strip("*").strip()


def _section_body_after_header(text: str, header_re: re.Pattern[str]) -> str | None:
    """Return text from a matching header to the next same-level heading."""
    m = header_re.search(text)
    if m is None:
        return None
    start = m.end()
    rest = text[start:]
    # Stop at next markdown heading
    nxt = re.search(r"(?m)^#{1,6}\s+\S", rest)
    if nxt:
        rest = rest[: nxt.start()]
    return rest


def _problem_ok(text: str) -> tuple[bool, str]:
    m = _PROBLEM_LINE.search(text)
    if m is None:
        return False, "problem statement missing"
    if m.groupdict().get("body") is not None:
        body = _strip_md(m.group("body") or "")
        if not body or _THEATER.match(body):
            return False, "problem statement missing (theater)"
        return True, ""
    # Heading form — need non-theater body after header
    body = _section_body_after_header(text, re.compile(
        r"^#{1,6}\s*(?:\d+\.\s*)?Problem\s+statement\b",
        re.I | re.M,
    ))
    if body is None:
        return False, "problem statement missing"
    cleaned = re.sub(r"\s+", " ", body).strip()
    if not cleaned or _THEATER.match(cleaned):
        return False, "problem statement missing (theater)"
    # Reject tiny placeholders
    if len(cleaned) < 12:
        return False, "problem statement missing (too thin)"
    return True, ""


def _sessions_ok(text: str) -> tuple[bool, str]:
    matches = list(_SESSION_LINE.finditer(text))
    if not matches:
        return False, "session(s) missing"
    # Prefer field-line captures (body=) over heading-only matches
    body_m = next((m for m in matches if m.groupdict().get("body") is not None), None)
    if body_m is not None:
        body = _strip_md(body_m.group("body") or "")
        if not body or _THEATER.match(body):
            return False, "session(s) missing (theater)"
        return True, ""
    body = _section_body_after_header(text, re.compile(
        r"^#{1,6}\s*(?:\d+\.\s*)?Sessions?\s+examined\b",
        re.I | re.M,
    ))
    if body is None:
        return False, "session(s) missing"
    cleaned = re.sub(r"\s+", " ", body).strip()
    if not cleaned or _THEATER.match(cleaned):
        return False, "session(s) missing (theater)"
    if len(cleaned) < 3:
        return False, "session(s) missing (too thin)"
    return True, ""


def _findings_region(text: str) -> str | None:
    m = _FINDINGS_HEADER.search(text)
    if m is None:
        return None
    rest = text[m.end() :]
    nxt = re.search(r"(?m)^#{1,6}\s+\S", rest)
    if nxt:
        rest = rest[: nxt.start()]
    return rest


def _findings_ok(text: str) -> tuple[bool, str]:
    region = _findings_region(text)
    if region is None:
        return False, "findings section missing"

    region_stripped = region.strip()
    if not region_stripped or _THEATER.match(region_stripped):
        return False, "findings section missing (theater)"

    if _NONE_FOUND.search(region):
        # Honest empty is OK when "none found" (optionally with checked note)
        return True, ""

    cites = CITATION_RE.findall(region)
    if cites:
        return True, ""

    # Has finding-looking content but no path:line → cite-or-fail
    bullets = [
        b for b in _FINDING_BULLET.finditer(region)
        if not re.match(r"(?i)^\s*(?:#|\|\s*-)", b.group("body") or "")
    ]
    if bullets or len(region_stripped) >= 8:
        return False, "uncited findings (cite-or-fail — every finding needs path:line)"

    return False, "findings section missing (theater)"


def check_report(path: Path) -> list[str]:
    """Mechanical cite-or-fail report skeleton. Empty list = PASS.

    Fails when:
      - report path missing / empty
      - problem statement missing / theater
      - session(s) missing / theater
      - findings section missing / theater / uncited
    """
    errors: list[str] = []
    if not path.exists():
        return [f"report missing: {path}"]

    text, sources = _combined_report(path)
    if not text.strip():
        return [
            f"report missing under {path} — write report.md with problem "
            "statement + session(s) + findings (cite-or-fail)"
        ]

    ok, reason = _problem_ok(text)
    if not ok:
        errors.append(
            f"{reason} — record Problem statement: … "
            f"(partner-answered; open {LEAF})"
        )

    ok, reason = _sessions_ok(text)
    if not ok:
        errors.append(
            f"{reason} — record Session(s): … "
            f"(VERIFIED path via session-discovery; open {LEAF})"
        )

    ok, reason = _findings_ok(text)
    if not ok:
        errors.append(
            f"{reason} — Findings must cite path:line or say "
            f"`none found — checked: …` (iron={IRON_REPORT}; open {LEAF})"
        )

    _ = sources
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print Emperor Time diagnosing HARD-GATE card "
            "for emperor-heal (intake + citation + cite-or-fail report)."
        )
    )
    parser.add_argument(
        "--reject-uncited",
        action="store_true",
        help="Hard-gate: exit 1 when about to emit a finding without path:line",
    )
    parser.add_argument(
        "--reject-skip-intake",
        action="store_true",
        help="Hard-gate: exit 1 when about to analyze before partner intake",
    )
    parser.add_argument(
        "--reject-no-report",
        action="store_true",
        help="Hard-gate: exit 1 when about to claim done without a report path",
    )
    parser.add_argument(
        "--check-citation",
        metavar="TEXT",
        default=None,
        help="Exit 0 if TEXT contains path:line; else exit 1 with CITE FAIL",
    )
    parser.add_argument(
        "--check-report",
        metavar="PATH",
        default=None,
        help=(
            "Exit 0 if PATH is a cite-or-fail report skeleton "
            "(problem + sessions + findings); else exit 1"
        ),
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=None,
        help="Optional report path (same as --check-report)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.reject_uncited:
        sys.stdout.write(reject_uncited())
        return 1
    if args.reject_skip_intake:
        sys.stdout.write(reject_skip_intake())
        return 1
    if args.reject_no_report:
        sys.stdout.write(reject_no_report())
        return 1
    if args.check_citation is not None:
        ok, msg = check_citation(args.check_citation)
        sys.stdout.write(msg)
        return 0 if ok else 1

    target = args.check_report if args.check_report is not None else args.path
    if target is not None:
        errors = check_report(Path(target))
        if errors:
            for e in errors:
                sys.stdout.write(f"REPORT FAIL: {e}\n")
            sys.stdout.write(
                f"REPORT FAIL: iron={IRON_REPORT}. "
                f"Open {LEAF}; fix skeleton or drop uncited findings.\n"
            )
            return 1
        sys.stdout.write(
            f"REPORT PASS: cite-or-fail report skeleton ok ({target})\n"
        )
        return 0

    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    sys.exit(main())
