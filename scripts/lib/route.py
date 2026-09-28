#!/usr/bin/env python3
"""Trigger→skill router MVP (no embeddings). Reads evals/triggers.json routes.

CLI: utterance arg(s), or EMPEROR_ROUTE_UTTERANCE, or stdin.
Prints: <target> — <reason>
Exit: 0 match / 1 no match / 2 usage or error.

Extracted from the inlined Python formerly in route.sh / route.ps1.
Thin twins: scripts/route.sh / scripts/route.ps1. Excavate patterns include
Fortran (.f90 / gfortran), VHDL (.vhd / ghdl), Ada (.adb / gnat), Forth (.fs / pforth), Common Lisp (.lisp / clisp), Prolog (.pro / swipl), Tcl (.tcl / tclsh), Erlang (.erl / escript), REXX (.rex / regina), Modula-2 (.mod / gm2), Algol 68 (.a68 / a68g), ALGOL 60 (.a60 / marst), Algol W (.alw / awe), Icon (.icn / icont), Oberon (.obn / voc), SNOBOL4 (.sno / snobol4), Simula (.sim / cim), APL (.apl / apl), BCPL (.b / bcpl / cintsys), PL/I (.pli / plic), Smalltalk (gst / smalltalk), PostScript (ghostscript / postscript), BASIC (bwbasic / bywater / .bas), Scheme (csi / chicken / chicken-scheme / .scm), AWK (gawk / awk / nawk / .awk), sed (sed / gsed / .sed), m4 (m4 / gm4 / .m4), ed (ed / gnu-ed / .ed), Make (gmake / gnu-make / .mk / .mak / makefile; bare make refused), dc (dc / gnu-dc / .dc), lex (lex / flex / gnu-flex / .lex; bare .l refused), yacc (yacc / bison / gnu-bison / .y), roff (roff / nroff / groff / gnu-groff / .roff), Perl (perl / perl5 / .pm; bare .pl refused for PL/I .pli/.pl1 collision), bc (bc / gnu-bc; bare .bc refused for BCPL .bcpl collision), Expect (expect / tcl-expect / .exp), Lua (lua / lua5.4 / .lua), Ruby (ruby / ruby3.3 / .rb), Go (golang / go1.24 / .go; bare go refused), Rust (rust / rustc / rust1.85 / .rs), C (gcc / gcc14 / c11 / .c; bare c refused; extension-boundary for .c), JavaScript (nodejs / node20 / javascript / .js; bare node refused like bare go; bare js allowed; extension-boundary so .js does not prefix-hit .json/.jsx), Python (python3 / python3.13 / cpython / .py; bare python refused for ET meta / house-tooling discourse collision; bare py allowed; extension-boundary so .py does not prefix-hit .pyc/.pyo/.pyw/.pyx/.pyi), TypeScript (typescript / typescript5 / tsc / ts5 / .ts; bare ts allowed; extension-boundary so .ts does not prefix-hit .tsx/.tsbuildinfo/.mts/.cts; not bun), Bash (bash / bash5 / bash5.2 / gnu-bash / .sh; bare bash allowed; bare sh refused for POSIX/dash ambiguity; extension-boundary so .sh does not prefix-hit .sha/.shar/.shtml), and PHP (php / php8 / php8.4 / php-cli / .php; bare php allowed; extension-boundary so .php does not prefix-hit .php3/.php4/.php5/.phps; not hhvm / web SAPI) alongside Pascal / ASM / COBOL.
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
            # Require non-alnum/end after suffix so ".c" does not prefix-hit ".cbl"/".cl".
            return re.search(re.escape(p) + r"(?![a-z0-9])", text) is not None
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
