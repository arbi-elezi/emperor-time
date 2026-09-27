#!/usr/bin/env python3
"""Prove bakeoff.md / this-upgrade.md honesty against disk leaves.

Local mechanism paths must exist and be named in bakeoff.md.
Live defect-rate vs Superpowers must stay labeled UNVERIFIABLE in both
docs. No fake numbers — this helper only checks labels and presence.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# (short name, path relative to repo root, substrings bakeoff.md must contain)
LEAVES: list[tuple[str, str, tuple[str, ...]]] = [
    ("plans", "scripts/lib/work_order.py", ("plans", "work_order")),
    ("finish", "skills/emperor-forge/finish-menu.md", ("finish",)),
    ("finish-py", "scripts/lib/finish.py", ("finish.py", "finish menu")),
    ("activate", "scripts/lib/activate.py", ("activate", "must-route")),
    ("must-route", "skills/emperor-resume/must-route.md", ("must-route",)),
    ("grill", "skills/emperor-require-design/grill-checklist.md", ("grill",)),
    (
        "debug-phases",
        "skills/emperor-heal/debug-four-phases.md",
        ("debug", "four"),
    ),
    ("tdd", "skills/emperor-tdd/red-green-refactor.md", ("tdd",)),
    (
        "worktree-iso",
        "skills/emperor-worktree/isolation-checklist.md",
        ("worktree", "isolation"),
    ),
    (
        "review",
        "skills/emperor-verify/request-review-checklist.md",
        ("request-review",),
    ),
    (
        "author",
        "chains/chain-jail/authoring-checklist.md",
        ("authoring",),
    ),
    (
        "evidence",
        "skills/emperor-verify/verification-checklist.md",
        ("evidence", "verification"),
    ),
    ("arch-pas", "evals/fixtures/lost-pas/HELLO.PAS", ("lost-pas",)),
    ("arch-asm", "evals/fixtures/lost-asm/FOO.ASM", ("lost-asm",)),
    ("arch-cbl", "evals/fixtures/lost-cbl/HELLO.CBL", ("lost-cbl",)),
    ("arch-f90", "evals/fixtures/lost-f90/HELLO.F90", ("lost-f90",)),
    ("gate-py", "scripts/lib/gate.py", ("gate.py", "mechanical")),
    ("identify-py", "scripts/lib/identify.py", ("identify.py", "survey")),
    ("eval-py", "scripts/lib/eval.py", ("eval.py", "structural eval")),
    ("route-py", "scripts/lib/route.py", ("route", "fortran", ".f90")),
]

BAKEOFF = Path("evals/bakeoff.md")
UPGRADE = Path("evals/fixtures/this-upgrade.md")

# Both docs must keep live bake-off rate honestly unlabeled as measured.
LIVE_RATE_NEEDLES = (
    "UNVERIFIABLE",
    "defect-rate",
    "Superpowers",
)


def _fail(msg: str) -> int:
    print(f"BAKEOFF HONESTY FAIL: {msg}", file=sys.stderr)
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--cwd",
        type=Path,
        default=Path.cwd(),
        help="repo root (default: cwd)",
    )
    args = ap.parse_args()
    root: Path = args.cwd.resolve()

    bakeoff_path = root / BAKEOFF
    upgrade_path = root / UPGRADE
    if not bakeoff_path.is_file():
        return _fail(f"missing {BAKEOFF}")
    if not upgrade_path.is_file():
        return _fail(f"missing {UPGRADE}")

    bakeoff = bakeoff_path.read_text(encoding="utf-8")
    upgrade = upgrade_path.read_text(encoding="utf-8")
    bakeoff_l = bakeoff.lower()

    for name, rel, needles in LEAVES:
        path = root / rel
        if not path.is_file():
            return _fail(f"leaf {name}: missing path {rel}")
        for needle in needles:
            if needle.lower() not in bakeoff_l:
                return _fail(
                    f"leaf {name}: bakeoff.md missing mention {needle!r}"
                )

    for label, text in (("bakeoff.md", bakeoff), ("this-upgrade.md", upgrade)):
        for needle in LIVE_RATE_NEEDLES:
            if needle not in text:
                return _fail(f"{label} missing honesty needle {needle!r}")
        # Guard against inventing a measured win-rate.
        for bad in ("% better", "defect rate:", "wins N%", "N% lower"):
            if bad.lower() in text.lower():
                return _fail(f"{label} looks like a fake number phrase: {bad!r}")

    # Local mechanism must be labeled TESTED or VERIFIED somewhere in bakeoff.
    if "TESTED" not in bakeoff and "VERIFIED" not in bakeoff:
        return _fail("bakeoff.md missing TESTED/VERIFIED for local mechanism")

    print("BAKEOFF HONESTY OK")
    print(f"LEAVES checked={len(LEAVES)}")
    print("LIVE_DEFECT_RATE=UNVERIFIABLE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
