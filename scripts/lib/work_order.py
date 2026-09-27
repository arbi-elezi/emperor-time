#!/usr/bin/env python3
"""Validate Emperor Time work-order plan header (G2).

Leaf adapted from obra/superpowers skills/writing-plans
"Plan Document Header" (MIT) — Goal / Architecture / Tech Stack / Spec /
Global Constraints / Review Focus. Emperor Time keeps the orchestrator;
this module only locks the header shape.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_INLINE = (
    ("**Goal:**", re.compile(r"(?im)^\*\*Goal:\*\*\s+\S")),
    ("**Architecture:**", re.compile(r"(?im)^\*\*Architecture:\*\*\s+\S")),
    ("**Tech Stack:**", re.compile(r"(?im)^\*\*Tech Stack:\*\*\s+\S")),
    ("**Spec:**", re.compile(r"(?im)^\*\*Spec:\*\*\s+\S")),
)

REQUIRED_SECTIONS = (
    ("## Global Constraints", re.compile(r"(?im)^##\s+Global Constraints\s*$")),
    ("## Review Focus", re.compile(r"(?im)^##\s+Review Focus\s*$")),
)

PLACEHOLDER = re.compile(
    r"(?i)<[^>]+>|\[(?:one sentence|2-3 sentences|key technologies|"
    r"path to|the five|TODO|TBD)[^\]]*\]|\bTBD\b|\.\.\.\s*$"
)


def _section_body(text: str, heading_re: re.Pattern[str]) -> str | None:
    m = heading_re.search(text)
    if not m:
        return None
    rest = text[m.end() :]
    nxt = re.search(r"(?m)^##\s+", rest)
    body = rest if nxt is None else rest[: nxt.start()]
    return body


def _body_ok(body: str) -> bool:
    lines = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("<!--"):
            continue
        if PLACEHOLDER.search(line) and len(re.sub(r"\W+", "", line)) < 12:
            continue
        # explicit none / checked is allowed (Superpowers: empty means checked)
        lines.append(line)
    if not lines:
        return False
    joined = "\n".join(lines)
    if re.search(r"(?i)\bnone\b.*\bchecked\b|\bchecked\b.*\bnone\b|^none\s*$", joined):
        return True
    # at least one non-placeholder bullet or sentence
    for line in lines:
        if PLACEHOLDER.search(line) and len(line) < 40:
            continue
        if line.startswith(("-", "*", "|")) or len(line) >= 8:
            return True
    return False


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"missing work-order: {path}"]
    text = path.read_text(encoding="utf-8", errors="replace")
    # trivial tasks skip header lock (gate.sh already short-circuits)
    if re.search(r"(?im)^\s*-\s*\*\*Size:\*\*\s*trivial\b|^\*\*Size:\*\*\s*trivial\b|Size:\s*trivial\b", text):
        return []

    for label, rx in REQUIRED_INLINE:
        if not rx.search(text):
            errors.append(f"missing filled {label} line")

    for label, rx in REQUIRED_SECTIONS:
        body = _section_body(text, rx)
        if body is None:
            errors.append(f"missing section {label}")
        elif not _body_ok(body):
            errors.append(f"empty or placeholder-only {label}")

    return errors


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Validate work-order plan header")
    p.add_argument("work_order", type=Path, help="path to work-order.md")
    args = p.parse_args(argv)
    errs = validate(args.work_order)
    if errs:
        for e in errs:
            print(f"work_order FAIL: {e}", file=sys.stderr)
        return 1
    print(f"work_order PASS: {args.work_order}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
