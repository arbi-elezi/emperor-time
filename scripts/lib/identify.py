#!/usr/bin/env python3
"""Language-agnostic artifact survey (Python core).

No preferred stack. Always exits 0.

Thin twins: scripts/identify.sh / scripts/identify.ps1 — same CLI:
  identify.py [root]

Excavate thin aliases (scripts/excavate.sh / excavate.ps1) call this core
directly (no hop through identify twins).

Preserves identify.sh semantics (extensions + named fossils + shebangs)
so bash/ps1 cannot drift. excavate/boot consume this survey.
"""
from __future__ import annotations

import argparse
import fnmatch
import re
import sys
from collections import Counter
from pathlib import Path

# Ordered fossil patterns — match identify.sh (find -iname semantics).
FOSSIL_PATTERNS: tuple[str, ...] = (
    "*.pas",
    "*.pp",
    "*.dpr",
    "*.lpr",
    "*.asm",
    "*.s",
    "*.inc",
    "*.cbl",
    "*.cob",
    "*.for",
    "*.f",
    "*.f90",
    "*.vhd",
    "*.vhdl",
    "*.adb",
    "*.ads",
    "*.ada",
    "*.fs",
    "*.fth",
    "*.4th",
    "*.lisp",
    "*.lsp",
    "*.cl",
    "*.pro",
    "*.prolog",
    "*.tcl",
    "*.tk",
    "*.erl",
    "*.hrl",
    "*.rex",
    "*.rexx",
    "*.mod",
    "*.def",
    "*.a68",
    "*.alg",
    "*.a60",
    "*.alw",
    "*.icn",
    "*.obn",
    "*.sno",
    "*.sim",
    "*.apl",
    "*.b",
    "*.bcpl",
    "*.pli",
    "*.pl1",
    "*.st",
    "*.ps",
    "*.eps",
    "*.bas",
    "*.scm",
    "*.awk",
    "*.sed",
    "*.m4",
    "*.ed",
    "*.dc",
    "*.bc",
    "*.exp",
    "*.lua",
    "*.rb",
    "*.go",
    "*.rs",
    "*.c",
    "*.js",
    "*.py",
    "*.ts",
    "*.sh",
    "*.php",
    "*.sql",
    "*.jq",
    "*.xsl",
    "*.xslt",
    "*.xml",
    "*.yaml",
    "*.yml",
    "*.toml",
    "*.html",
    "*.htm",
    "*.csv",
    "*.json",
    "*.ini",
    "*.plist",
    "*.eml",
    "*.zip",
    "*.tar",
    "*.l",
    "*.lex",
    "*.y",
    "*.roff",
    "*.pl",
    "*.pm",
    "*.rel",
    "*.hex",
    "*.bin",
    "*.rom",
    "Makefile",
    "makefile",
    "*.mak",
    "*.mk",
)

SKIP_PARTS = frozenset({".git", ".emperor", "node_modules"})
EXT_RE = re.compile(r"^[A-Za-z0-9]+$")
SHEBANG_BYTES = 200 * 1024
SHEBANG_SCAN_CAP = 200
SHEBANG_PRINT_CAP = 30
EXT_TOP = 40


def _skip(rel: Path) -> bool:
    return any(part in SKIP_PARTS for part in rel.parts)


def _find_style(root: Path, rel: Path) -> str:
    """Path string shaped like GNU find \"$ROOT\" output."""
    if str(root) == ".":
        return "./" + rel.as_posix()
    return f"{root.as_posix().rstrip('/')}/{rel.as_posix()}"


def _iter_files(root: Path) -> list[tuple[Path, Path, str]]:
    out: list[tuple[Path, Path, str]] = []
    try:
        for p in sorted(root.rglob("*")):
            if not p.is_file():
                continue
            try:
                rel = p.relative_to(root)
            except ValueError:
                continue
            if _skip(rel):
                continue
            out.append((p, rel, _find_style(root, rel)))
    except OSError:
        return []
    return out


def _extension_token(find_path: str) -> str | None:
    # Mirror bash: sed 's/.*\.//' on the find path, then alphanumeric-only.
    if "." not in find_path:
        token = find_path
    else:
        token = find_path.rsplit(".", 1)[-1]
    if EXT_RE.fullmatch(token):
        return token.lower()
    return None


def _matches_fossil(name: str, pat: str) -> bool:
    # find -iname "$pat" — case-insensitive glob / literal.
    return fnmatch.fnmatch(name.lower(), pat.lower())


def survey(root: Path) -> list[str]:
    lines: list[str] = [f"== identify {root} =="]
    files = _iter_files(root)

    lines.append("-- extensions --")
    ext_counts: Counter[str] = Counter()
    for _abs, _rel, fpath in files:
        tok = _extension_token(fpath)
        if tok is not None:
            ext_counts[tok] += 1
    # sort -nr: count desc, then name desc (GNU uniq -c | sort -nr)
    ranked = sorted(ext_counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for tok, n in ranked[:EXT_TOP]:
        lines.append(f"{n:7d} {tok}")

    lines.append("-- named fossils --")
    for pat in FOSSIL_PATTERNS:
        n = sum(1 for _a, rel, _f in files if _matches_fossil(rel.name, pat))
        if n:
            lines.append(f"{n} {pat}")

    lines.append("-- shebangs --")
    printed = 0
    scanned = 0
    for abs_path, _rel, fpath in files:
        if scanned >= SHEBANG_SCAN_CAP or printed >= SHEBANG_PRINT_CAP:
            break
        try:
            size = abs_path.stat().st_size
        except OSError:
            continue
        if size >= SHEBANG_BYTES:
            continue
        scanned += 1
        try:
            with abs_path.open("rb") as fh:
                first = fh.readline(4096)
        except OSError:
            continue
        if not first.startswith(b"#!"):
            continue
        text = first.decode("utf-8", errors="replace").rstrip("\r\n")
        lines.append(f"{fpath}: {text}")
        printed += 1

    lines.append("identify: done (read-only)")
    return lines


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Language-agnostic artifact survey (read-only)."
    )
    ap.add_argument(
        "root",
        nargs="?",
        default=".",
        help="tree to survey (default: .)",
    )
    args = ap.parse_args(argv)
    root = Path(args.root)
    if not root.exists():
        print(f"== identify {args.root} ==")
        print("-- extensions --")
        print("-- named fossils --")
        print("-- shebangs --")
        print("identify: done (read-only)")
        return 0
    for line in survey(root):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
