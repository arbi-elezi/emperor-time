#!/usr/bin/env python3
"""Isolated review-pack emitter + hetero-critique isolation HARD-GATE.

Emits SHAs + diff + acceptance criteria. No author CoT.
Closes bash↔ps1 twin drift: review-pack.ps1 copied the entire work-order
into criteria.md while review-pack.sh extracted only the
## Acceptance criteria section.

Always-fail HARD-GATE helpers:
  --reject-unisolated      refuse non-isolated examiner handoff
  --reject-author-diary    refuse author CoT / self-critique / diary in pack

Check mode:
  --check-isolation PATH   review-pack dir or task dir
                           (exit 1 on forbidden files / author-diary content;
                            SKIP vacuous when no pack / no hetero signal)

Emit mode (unchanged):
  review_pack.py <task-dir> [base] [head]

No args prints the ISOLATION card.
Thin twins: scripts/review-pack.sh / scripts/review-pack.ps1
G4 in gate.py calls --check-isolation when review-pack / hetero activity
is present.
Activity-scoped: SKIP (vacuous — no activity) when no pack / no hetero signal.

Doctrine: chains/judgment-chain/hetero-critique.md + iron law 9
(Reviewer isolation) + templates/review-pack.md.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence
from check_report import report_check

LEAF = "chains/judgment-chain/hetero-critique.md"
IRON = "references/iron-laws.md"

# Files the emitter may place (and the examiner may receive).
ALLOWED_PACK_NAMES = frozenset(
    {
        "meta.md",
        "criteria.md",
        "diff.patch",
        "diffstat.txt",
        "claims.md",
        "readme.md",  # optional examiner brief
    }
)

# Explicit contamination filenames — never in an isolated pack.
FORBIDDEN_PACK_NAMES = frozenset(
    {
        "self-critique.md",
        "critique.md",
        "diary.md",
        "author-diary.md",
        "author.md",
        "cot.md",
        "chain-of-thought.md",
        "rationalization.md",
        "out.txt",
        "design.md",
        "approach.md",
        "notes.md",
        "prompt.md",  # critic prompt lives under runs/, not the pack
    }
)

# Author diary / self-critique leakage inside otherwise-allowed files.
_AUTHOR_DIARY = re.compile(
    r"(?i)(?:"
    r"self-critique\s+conclusions?"
    r"|##\s*self-critique\b"
    r"|role:\s*self-prosecution"
    r"|prosecution\s+opens\s*:"
    r"|author'?s?\s+(?:chain\s+of\s+thought|diary|cot)\b"
    r"|chain\s+of\s+thought\s*:"
    r"|author\s+diary\s*:"
    r"|i\s+decided\s+to\s+(?:implement|skip|defer|ship)"
    r"|here\s+is\s+my\s+(?:reasoning|rationale)\s+for\s+the\s+patch"
    r")"
)

# Strong hetero / pack signals — weak "review" alone is not enough.
_HETERO_SIGNAL = re.compile(
    r"(?i)("
    # Positive hetero record / pack emit — not "out of scope: live hetero-critique".
    r"hetero-critique\s*:\s*\S"
    r"|isolated\s+review\s+pack"
    r"|review-pack/"
    r"|\breview_pack\.py\b"
    r"|\bscripts/(?:emperor\s+)?review-pack\b"
    r"|examiner\s+receives?\s+only"
    r"|\breject-unisolated\b"
    r"|\breject-author-diary\b"
    r"|\bcheck-isolation\b"
    r")"
)


def _in_git(cwd: Path | None = None) -> bool:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        return proc.returncode == 0 and proc.stdout.strip() == "true"
    except OSError:
        return False


def _git_rev(ref: str, cwd: Path | None = None) -> str | None:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", ref],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0:
            return proc.stdout.strip()
    except OSError:
        return None
    return None


def _git_diff(base: str, head: str, *, stat: bool = False, cwd: Path | None = None) -> str:
    args = ["git", "diff"]
    if stat:
        args.append("--stat")
    args.append(f"{base}..{head}")
    try:
        proc = subprocess.run(
            args,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        return proc.stdout
    except OSError:
        return ""


def extract_acceptance_criteria(work_order_text: str) -> str:
    """Match bash awk: from '^## Acceptance criteria' until next '^## ' heading.

    Inclusive of the Acceptance criteria heading; exclusive of the next ##.
    Returns empty string when the section is absent (bash awk empty output).
    """
    lines = work_order_text.splitlines()
    out: list[str] = []
    started = False
    for line in lines:
        if not started:
            if line.startswith("## Acceptance criteria"):
                started = True
                out.append(line)
            continue
        if line.startswith("## ") and not line.startswith("## Acceptance"):
            break
        out.append(line)
    return "\n".join(out) + ("\n" if out else "")


def emit_pack(task: Path, base: str = "HEAD~1", head: str = "HEAD") -> int:
    if not task.is_dir():
        print(f"missing {task}", file=sys.stderr)
        return 1
    out = task / "review-pack"
    out.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    meta_lines = [
        "# Isolated review pack",
        f"- task: {task}",
        f"- generated: {now}",
    ]
    if _in_git():
        base_sha = _git_rev(base) or base
        head_sha = _git_rev(head) or head
        meta_lines.append(f"- base: {base_sha}")
        meta_lines.append(f"- head: {head_sha}")
    else:
        meta_lines.append("- base/head: not a git repo")
    (out / "meta.md").write_text("\n".join(meta_lines) + "\n", encoding="utf-8")

    order = task / "work-order.md"
    if order.is_file():
        text = order.read_text(encoding="utf-8", errors="replace")
        criteria = extract_acceptance_criteria(text)
        (out / "criteria.md").write_text(criteria, encoding="utf-8")

    if _in_git():
        (out / "diff.patch").write_text(
            _git_diff(base, head), encoding="utf-8", errors="replace"
        )
        (out / "diffstat.txt").write_text(
            _git_diff(base, head, stat=True), encoding="utf-8", errors="replace"
        )

    claims = task / "claims.md"
    if claims.is_file():
        (out / "claims.md").write_text(
            claims.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    print(f"REVIEW PACK: {out}")
    for p in sorted(out.iterdir()):
        try:
            size = p.stat().st_size
        except OSError:
            size = 0
        print(f"{size:>8}  {p.name}")
    return 0


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _looks_like_pack(path: Path) -> bool:
    """A pack dir has meta.md (emitter always writes it) or classic name."""
    if not path.is_dir():
        return False
    if path.name == "review-pack":
        return True
    return (path / "meta.md").is_file()


def _pack_dir(path: Path) -> Path | None:
    """Resolve PATH to a review-pack directory if one exists."""
    if path.is_dir() and _looks_like_pack(path):
        # Prefer nested review-pack/ when both exist (task dir with meta elsewhere).
        nested = path / "review-pack"
        if nested.is_dir() and path.name != "review-pack":
            return nested
        return path
    if path.is_dir() and (path / "review-pack").is_dir():
        return path / "review-pack"
    if path.is_file() and (
        path.parent.name == "review-pack" or (path.parent / "meta.md").is_file()
    ):
        return path.parent
    return None


def _combined_signal_text(path: Path) -> str:
    if path.is_file():
        return _read(path)
    if not path.is_dir():
        return ""
    parts: list[str] = []
    for name in (
        "ledger.md",
        "claims.md",
        "claim-ledger.md",
        "DONE.md",
        "done.md",
        "hetero-critique.md",
        "work-order.md",
    ):
        p = path / name
        if p.is_file():
            parts.append(_read(p))
    return "\n".join(parts)


def _has_hetero_signal(path: Path, text: str) -> bool:
    pack = _pack_dir(path)
    if pack is not None:
        return True
    if path.is_dir() and (path / "review-pack").is_dir():
        return True
    if path.is_file() and path.parent.name == "review-pack":
        return True
    return bool(_HETERO_SIGNAL.search(text))


def _pack_file_errors(pack: Path) -> list[str]:
    errors: list[str] = []
    if not pack.is_dir():
        return [f"missing review-pack dir: {pack}"]
    for child in sorted(pack.iterdir()):
        if not child.is_file():
            errors.append(
                f"unisolated entry in review-pack/ (non-file): {child.name} — "
                f"examiner receives the pack only (see {LEAF})"
            )
            continue
        name = child.name
        lower = name.lower()
        if lower in FORBIDDEN_PACK_NAMES:
            errors.append(
                f"author-diary / forbidden file in review-pack/: {name} — "
                "examiner must not receive self-critique, diary, CoT, "
                f"worker out.txt, or design rationalizations (see {LEAF})"
            )
            continue
        if lower not in ALLOWED_PACK_NAMES:
            errors.append(
                f"unisolated file in review-pack/: {name} — "
                "allowed: meta.md, criteria.md, diff.patch, diffstat.txt, "
                f"claims.md (see {LEAF} / iron law 9)"
            )
            continue
        body = _read(child)
        if _AUTHOR_DIARY.search(body):
            errors.append(
                f"author-diary content in review-pack/{name} — "
                "self-critique conclusions / author CoT / diary markers "
                f"break reviewer isolation (see {LEAF})"
            )
    return errors


def validate_isolation(path: Path) -> list[str]:
    """Mechanical hetero-critique isolation checks for pack / task dir."""
    if not path.exists():
        return [f"missing path: {path}"]

    text = _combined_signal_text(path)
    pack = _pack_dir(path)
    hetero = _has_hetero_signal(path, text)

    if not hetero and pack is None:
        # Vacuous PASS — no pack / no hetero activity to isolate
        return []

    errors: list[str] = []
    if pack is None:
        # Hetero claimed (signal in ledger/work-order) but no pack on disk
        errors.append(
            "missing isolated review-pack/ "
            "(hetero-critique / isolation claimed but examiner pack absent — "
            f"run scripts/emperor review-pack <task-dir>; see {LEAF})"
        )
        return errors

    errors.extend(_pack_file_errors(pack))
    # Direct file check: when PATH is a contaminated file inside the pack,
    # _pack_file_errors already covers siblings; also re-check the file itself
    # when it is the only signal (already covered via pack walk).
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def format_card() -> str:
    lines = [
        "ISOLATION checklist=yes",
        f"ISOLATION leaf={LEAF}",
        f"ISOLATION iron=REVIEWER_ISOLATION ({IRON} #9)",
        "STEP 1 id=pack name=Emit isolated review pack "
        "et=scripts/emperor review-pack <task-dir> <base> <head>",
        "STEP 1 key=meta + criteria + diff + VERIFIED claims only",
        "STEP 2 id=forbid name=Keep author diary out "
        "et=no self-critique / CoT / out.txt / design rationalization in pack",
        "STEP 2 key=Forbidden names fail --check-isolation",
        "STEP 3 id=dispatch name=Hand pack only to hetero-critic "
        "et=fresh context; builder does not write hetero verdict",
        "STEP 3 key=Iron law 9 — examiner receives the review pack only",
        "STEP 4 id=gate name=G4 calls --check-isolation "
        "et=SKIP (vacuous) when no pack / no hetero signal",
        "STEP 4 key=Pack-present theater with diary still fails",
        "",
        "MUST: Before hetero-critique dispatch, emit an isolated pack and keep "
        f"author diary out of it. Open {LEAF}; run "
        "scripts/emperor review-pack --check-isolation <task-dir>. "
        "G4 calls this module when review-pack / hetero activity is present.",
        "MUST-NOT: hand the full task dir; pack self-critique.md / critique.md / "
        "diary / CoT / worker out.txt; claim isolation without "
        "--check-isolation exit 0.",
    ]
    return "\n".join(lines) + "\n"


def reject_unisolated() -> str:
    return (
        "REJECT UNISOLATED: HARD-GATE — hetero-critique refuses an examiner "
        "handoff that is not the isolated review pack (pack missing, or "
        "pack contains files outside meta/criteria/diff/claims). "
        f"Open {LEAF}; re-run scripts/emperor review-pack --check-isolation "
        "<task-dir>.\n"
    )


def reject_author_diary() -> str:
    return (
        "REJECT AUTHOR DIARY: HARD-GATE — hetero-critique refuses author "
        "self-critique conclusions, chain-of-thought, diary, or design "
        "rationalizations inside the review pack. "
        f"Open {LEAF}; strip diary files/content; re-run "
        "scripts/emperor review-pack --check-isolation <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    raw = list(sys.argv[1:] if argv is None else argv)
    p = argparse.ArgumentParser(
        description=(
            "Emit isolated Emperor Time review pack and/or validate "
            "hetero-critique isolation (no author diary)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir for emit, or pack/task for isolation check",
    )
    p.add_argument(
        "base",
        nargs="?",
        default="HEAD~1",
        help="git base ref for emit (default HEAD~1)",
    )
    p.add_argument(
        "head",
        nargs="?",
        default="HEAD",
        help="git head ref for emit (default HEAD)",
    )
    p.add_argument(
        "--check-isolation",
        type=Path,
        metavar="PATH",
        default=None,
        help="isolation check (exit 1 on unisolated / author-diary pack)",
    )
    p.add_argument(
        "--reject-unisolated",
        action="store_true",
        help="Hard-gate: refuse non-isolated examiner handoff (exit 1)",
    )
    p.add_argument(
        "--reject-author-diary",
        action="store_true",
        help="Hard-gate: refuse author diary/CoT in review pack (exit 1)",
    )
    args = p.parse_args(raw)

    if args.reject_unisolated:
        sys.stdout.write(reject_unisolated())
        return 1
    if args.reject_author_diary:
        sys.stdout.write(reject_author_diary())
        return 1

    if args.check_isolation is not None:
        target = args.check_isolation
        errs = validate_isolation(target)
        text = _combined_signal_text(target) if target.exists() else ""
        pack = _pack_dir(target) if target.exists() else None
        hetero = _has_hetero_signal(target, text) if target.exists() else False
        vacuous = target.exists() and (not hetero) and pack is None
        return report_check("isolation", target, errs, vacuous=vacuous)

    if args.path is None:
        sys.stdout.write(format_card())
        return 0

    # Emit mode (legacy positional CLI).
    return emit_pack(args.path, args.base, args.head)


if __name__ == "__main__":
    raise SystemExit(main())
