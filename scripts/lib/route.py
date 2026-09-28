#!/usr/bin/env python3
"""Trigger→skill router MVP (no embeddings). Reads evals/triggers.json routes.

CLI: utterance arg(s), or EMPEROR_ROUTE_UTTERANCE, or stdin.
Prints: <target> — <reason>
Exit: 0 match / 1 no match / 2 usage or error.

Extracted from the inlined Python formerly in route.sh / route.ps1.
Thin twins: scripts/route.sh / scripts/route.ps1. Excavate patterns include
Fortran (.f90 / gfortran), VHDL (.vhd / ghdl), Ada (.adb / gnat), Forth (.fs / pforth), Common Lisp (.lisp / clisp), Prolog (.pro / swipl), Tcl (.tcl / tclsh), Erlang (.erl / escript), REXX (.rex / regina), Modula-2 (.mod / gm2), Algol 68 (.a68 / a68g), ALGOL 60 (.a60 / marst), Algol W (.alw / awe), and Icon (.icn / icont) alongside Pascal / ASM / COBOL.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import select
import sys
from pathlib import Path


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def matches(pattern: str, text: str) -> bool:
    p = pattern.casefold().strip()
    if not p:
        return False
    # Short tokens / tags: word-boundary to avoid "rom" in "from"
    compact = re.sub(r"[^a-z0-9]+", "", p)
    if len(compact) <= 3 or p.startswith("."):
        # escape and allow flexible non-alnum edges for extensions
        if p.startswith("."):
            return p in text
        return re.search(r"(?<![a-z0-9])" + re.escape(p) + r"(?![a-z0-9])", text) is not None
    return p in text


def route(utterance: str, triggers_path: Path) -> tuple[str | None, str | None]:
    """Return (target, reason) on first match, else (None, None)."""
    text = utterance.casefold()
    with open(triggers_path, encoding="utf-8") as f:
        data = json.load(f)
    routes = data.get("routes") or []
    for item in routes:
        pats = list(item.get("patterns") or [])
        tags = list(item.get("tags") or [])
        hit = None
        for p in pats:
            if matches(p, text):
                hit = p
                break
        if hit is None:
            for t in tags:
                if matches(t, text):
                    hit = t
                    break
        if hit is None:
            continue
        target = item.get("target") or ""
        reason = item.get("reason") or item.get("id") or "match"
        if not target:
            continue
        return str(target), str(reason)
    return None, None


def _read_stdin() -> str:
    """Read stdin when piped. Avoid hang when non-tty has no data ready."""
    if sys.stdin.isatty():
        return ""
    try:
        ready, _, _ = select.select([sys.stdin], [], [], 0)
    except (OSError, ValueError):
        ready = [sys.stdin]
    if not ready:
        return ""
    return sys.stdin.read()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="route.py",
        description="Emperor Time trigger→skill router MVP",
        add_help=True,
    )
    parser.add_argument(
        "utterance",
        nargs="*",
        help="utterance to route (or EMPEROR_ROUTE_UTTERANCE / stdin)",
    )
    parser.add_argument(
        "--triggers",
        default=None,
        help="path to triggers.json (default: EMPEROR_TRIGGERS or <root>/evals/triggers.json)",
    )
    args = parser.parse_args(argv)

    if args.utterance:
        utterance = " ".join(args.utterance)
    elif os.environ.get("EMPEROR_ROUTE_UTTERANCE"):
        utterance = os.environ["EMPEROR_ROUTE_UTTERANCE"]
    else:
        utterance = _read_stdin()

    utterance = re.sub(r"\s+", " ", utterance).strip()
    if not utterance:
        print("usage: route.py <utterance>   or pipe stdin", file=sys.stderr)
        return 2

    if args.triggers:
        triggers = Path(args.triggers)
    elif os.environ.get("EMPEROR_ROUTE_TRIGGERS"):
        triggers = Path(os.environ["EMPEROR_ROUTE_TRIGGERS"])
    elif os.environ.get("EMPEROR_TRIGGERS"):
        triggers = Path(os.environ["EMPEROR_TRIGGERS"])
    else:
        triggers = _root() / "evals" / "triggers.json"

    if not triggers.is_file():
        print(f"route: missing {triggers}", file=sys.stderr)
        return 2

    try:
        target, reason = route(utterance, triggers)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"route: {exc}", file=sys.stderr)
        return 2

    if not target:
        print("route: no match", file=sys.stderr)
        return 1
    print(f"{target} — {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
