#!/usr/bin/env python3
"""Proportionality / anti-loop HARD-GATE (Python core).

Effort caps tied to effort_class from ask→spec. Detect verify / critique /
gate thrash via a cycle ledger under the task dir so loops are visible across
invocations. Tiny asks (≈1–5 lines / single-file) get low caps — forbid
re-running a museum of gates.

Always-fail HARD-GATE helpers:
  --reject-over-verify         refuse when cycles exceed class cap

Check / record:
  --check-proportionality PATH
  --record-cycle KIND PATH     KIND=verify|critique|gate|total

Positional PATH runs the same check. No args prints the PROPORTIONALITY card.
Thin twins: scripts/proportionality.sh / scripts/proportionality.ps1
Alias: anti-loop → same core.
G4 in gate.py records a gate cycle then calls --check-proportionality.
Vacuous PASS when no effort_class and no cycle ledger (idle paths).
Steal/Jail/Holy vacuous PASS is separate — this is task-path thrash.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Sequence

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from ask_spec import parse_effort_class  # noqa: E402

LEAF = "references/mechanical-gates.md"
CYCLE_FILE = "effort-cycles.json"
KINDS = ("verify", "critique", "gate", "total")

# Caps per effort_class. tiny forbids museum-scale re-verify.
EFFORT_CAPS: dict[str, dict[str, int]] = {
    "tiny": {"verify": 2, "critique": 2, "gate": 3, "total": 4},
    "small": {"verify": 4, "critique": 4, "gate": 6, "total": 10},
    "medium": {"verify": 8, "critique": 8, "gate": 12, "total": 20},
    "large": {"verify": 16, "critique": 16, "gate": 24, "total": 40},
}

_EFFORT = re.compile(
    r"(?im)\beffort[_ -]?class\s*[:=]\s*(tiny|small|medium|large)\b"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _task_root(path: Path) -> Path:
    if path.is_dir():
        return path
    # If the file is ask-spec / ledger inside a task dir, use parent.
    if path.is_file():
        return path.parent
    return path


def _cycle_path(task: Path) -> Path:
    return _task_root(task) / CYCLE_FILE


def _load_cycles(task: Path) -> dict[str, int]:
    p = _cycle_path(task)
    base = {"verify": 0, "critique": 0, "gate": 0, "total": 0}
    if not p.is_file():
        return base
    try:
        data = json.loads(_read(p))
    except (OSError, json.JSONDecodeError):
        return base
    if not isinstance(data, dict):
        return base
    out = dict(base)
    for k in KINDS:
        try:
            out[k] = int(data.get(k, 0) or 0)
        except (TypeError, ValueError):
            out[k] = 0
    if "effort_class" in data and isinstance(data["effort_class"], str):
        # stash separately via return? keep counts only here
        pass
    return out


def _load_meta(task: Path) -> dict:
    p = _cycle_path(task)
    if not p.is_file():
        return {}
    try:
        data = json.loads(_read(p))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def save_cycles(
    task: Path,
    counts: dict[str, int],
    *,
    effort_class: str | None = None,
) -> Path:
    root = _task_root(task)
    root.mkdir(parents=True, exist_ok=True)
    meta = _load_meta(task)
    payload = {
        "effort_class": effort_class
        or meta.get("effort_class")
        or parse_effort_class(root)
        or "",
        "verify": int(counts.get("verify", 0)),
        "critique": int(counts.get("critique", 0)),
        "gate": int(counts.get("gate", 0)),
        "total": int(counts.get("total", 0)),
    }
    path = _cycle_path(task)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def record_cycle(task: Path, kind: str) -> dict[str, int]:
    """Increment KIND (+ total) and persist. Returns new counts."""
    kind = kind.lower().strip()
    if kind not in KINDS:
        raise ValueError(f"kind must be one of {KINDS}, got {kind}")
    counts = _load_cycles(task)
    if kind == "total":
        counts["total"] = counts.get("total", 0) + 1
    else:
        counts[kind] = counts.get(kind, 0) + 1
        counts["total"] = counts.get("total", 0) + 1
    cls = parse_effort_class(_task_root(task))
    save_cycles(task, counts, effort_class=cls)
    return counts


def resolve_effort_class(task: Path) -> str | None:
    """effort_class from ask-spec/ledger or cycle meta."""
    root = _task_root(task)
    cls = parse_effort_class(root)
    if cls:
        return cls
    meta = _load_meta(task)
    raw = meta.get("effort_class")
    if isinstance(raw, str) and raw.lower() in EFFORT_CAPS:
        return raw.lower()
    # Also scan ledger text directly.
    ledger = root / "ledger.md"
    if ledger.is_file():
        m = _EFFORT.search(_read(ledger))
        if m:
            return m.group(1).lower()
    return None


def _has_activity(task: Path) -> bool:
    root = _task_root(task)
    if _cycle_path(task).is_file():
        return True
    if resolve_effort_class(root) is not None:
        return True
    for name in ("ask-spec.md", "ask_spec.md"):
        if (root / name).is_file():
            return True
    return False


def validate(path: Path, *, bump_gate: bool = False) -> list[str]:
    """Check cycles against effort_class caps.

    bump_gate=True records a gate cycle before checking (G4 wiring).
    """
    if not path.exists():
        return [f"missing path: {path}"]

    root = _task_root(path)
    cls = resolve_effort_class(root)
    # Only bump when a class is declared — do not create orphan cycle ledgers
    # on vacuous paths (would force a false "missing effort_class" fail).
    if bump_gate and cls is not None:
        record_cycle(root, "gate")

    if cls is None and not _cycle_path(root).is_file():
        # Vacuous PASS — no effort_class / cycle ledger.
        return []

    if cls is None:
        return [
            "effort activity without effort_class "
            f"(need effort_class: tiny|small|medium|large from ask→spec — "
            f"see {LEAF})"
        ]

    caps = EFFORT_CAPS[cls]
    counts = _load_cycles(root)
    errors: list[str] = []
    for kind in ("verify", "critique", "gate", "total"):
        n = int(counts.get(kind, 0))
        cap = caps[kind]
        if n > cap:
            errors.append(
                f"over-verify: {kind}={n} exceeds {cls} cap={cap} "
                f"(ask→spec effort_class={cls}; stop thrash — do-once / "
                f"ship or shrink — see {LEAF})"
            )
    return errors


def format_card() -> str:
    lines = [
        "PROPORTIONALITY checklist=yes",
        f"PROPORTIONALITY leaf={LEAF}",
        "PROPORTIONALITY iron=EFFORT_CAP_BY_CLASS",
        "STEP 1 id=class name=Read effort_class from ask→spec "
        "et=tiny|small|medium|large",
        "STEP 1 key=No class → emit ask-spec first",
        "STEP 2 id=caps name=Honor class caps "
        "et="
        + "; ".join(
            f"{k}: total≤{v['total']}/verify≤{v['verify']}/critique≤{v['critique']}/gate≤{v['gate']}"
            for k, v in EFFORT_CAPS.items()
        ),
        "STEP 2 key=tiny ≈ 1–5 line change → max 1–2 verify/critique",
        "STEP 3 id=ledger name=Record cycles in effort-cycles.json "
        "et=--record-cycle verify|critique|gate <task-dir>",
        "STEP 3 key=Loops across invocations are detectable",
        "STEP 4 id=gate name=HARD-GATE on over-cap "
        "et=--reject-over-verify / --check-proportionality; G4 records+checks",
        "STEP 4 key=Nonzero exit when thrash exceeds class",
        "",
        "MUST: Scale verify/critique/gate effort to effort_class. Tiny asks "
        "do not re-run the museum of gates. Open "
        f"{LEAF}; run scripts/emperor proportionality --check-proportionality "
        "<task-dir>.",
        "MUST-NOT: ~20 verifications for a 2-line change; endless "
        "critique/gate loops that burn tokens without shipping.",
        "HONESTY: Idle Steal/Jail/Holy vacuous PASS is separate; this HARD-GATE "
        "is task-path thrash only.",
    ]
    return "\n".join(lines) + "\n"


def reject_over_verify() -> str:
    return (
        "REJECT OVER-VERIFY: HARD-GATE — verify/critique/gate cycles exceed "
        "the effort_class cap from ask→spec. Stop thrash: ship, shrink scope, "
        "or raise effort_class with client yes. "
        f"Open {LEAF}; re-run scripts/emperor proportionality "
        "--check-proportionality <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Emperor Time proportionality / anti-loop: effort caps by "
            "effort_class + cycle ledger (HARD-GATE)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir (omit to print card)",
    )
    p.add_argument(
        "--check-proportionality",
        type=Path,
        metavar="PATH",
        default=None,
        help="proportionality check (exit 1 when over cap)",
    )
    p.add_argument(
        "--reject-over-verify",
        action="store_true",
        help="Hard-gate: refuse over-cap thrash (always exit 1)",
    )
    p.add_argument(
        "--record-cycle",
        nargs=2,
        metavar=("KIND", "PATH"),
        default=None,
        help="Increment KIND (verify|critique|gate|total) on PATH",
    )
    p.add_argument(
        "--bump-gate",
        action="store_true",
        help="With --check-proportionality / PATH: record a gate cycle first",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_over_verify:
        sys.stdout.write(reject_over_verify())
        return 1

    if args.record_cycle is not None:
        kind, raw = args.record_cycle
        target = Path(raw)
        try:
            counts = record_cycle(target, kind)
        except (ValueError, OSError) as exc:
            print(f"proportionality FAIL: {exc}", file=sys.stderr)
            return 2
        print(
            f"proportionality RECORD: kind={kind.lower()} "
            f"verify={counts['verify']} critique={counts['critique']} "
            f"gate={counts['gate']} total={counts['total']} path={target}"
        )
        return 0

    target = (
        args.check_proportionality
        if args.check_proportionality is not None
        else args.path
    )
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target, bump_gate=args.bump_gate)
    if errs:
        for e in errs:
            print(f"proportionality FAIL: {e}", file=sys.stderr)
        return 1
    cls = resolve_effort_class(target) or "vacuous"
    counts = _load_cycles(target)
    print(
        f"proportionality PASS: {target} effort_class={cls} "
        f"total={counts.get('total', 0)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
