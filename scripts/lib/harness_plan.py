#!/usr/bin/env python3
"""Harness tool+force planner (Python core).

The harness/orchestrator owns tool selection and proportionality of force —
not more agent-facing CLI the model must recall. Flow:

  1. User ask → ask→spec (goal / done-when / out-of-scope / effort_class)
  2. From effort_class (tiny|small|medium|large), the harness **selects**
     which tools/gates to run and **caps** (verify/critique/gate cycles)
  3. Drive do-once / verify-at-scale — the LLM does not choose 20
     verifications for a 2-line change

Always-fail HARD-GATE helpers:
  --reject-no-plan          refuse without a harness plan (card; exit 1)

Check / require / emit:
  --check-harness-plan PATH activity-scoped idle check (SKIP vacuous when idle)
  --require-plan PATH       always-on when task active: missing/invalid plan FAILS
                            (never vacuous — G0 calls this after ask→spec)
  --emit / --from / --effort-class / --write PATH

Positional PATH runs --check-harness-plan. No args prints the HARNESS-PLAN card.
Thin twins: scripts/harness-plan.sh / scripts/harness-plan.ps1
Alias: tool-force → same core.
G0 calls --require-plan after ask→spec.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Sequence

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from ask_spec import parse_effort_class  # noqa: E402
from check_report import report_check  # noqa: E402
from proportionality import EFFORT_CAPS  # noqa: E402

LEAF = "references/mechanical-gates.md"
IRON = "HARNESS_OWNS_TOOL_AND_FORCE"
PLAN_FILENAMES = {
    "harness-plan.md",
    "harness_plan.md",
    "tool-force.md",
    "tool_force.md",
}
PLAN_JSON = "harness-plan.json"
EFFORT_CLASSES = ("tiny", "small", "medium", "large")

# Harness-owned tool+force table. Caps mirror proportionality.EFFORT_CAPS.
# Forbidden heavy paths shrink as class grows — tiny forbids the museum.
FORCE_TABLE: dict[str, dict[str, Any]] = {
    "tiny": {
        "tools": [
            "ask-spec",
            "harness-plan",
            "activate",
            "route",
            "gate",
            "done",
        ],
        "optional": ["finish", "proportionality"],
        "forbidden": [
            "excavate",
            "sandbox",
            "sot",
            "steal-flow",
            "heal",
            "critique",
            "grill",
            "parallel",
            "subagent",
            "forge",
            "context-build",
            "triage",
            "reproduce",
            "process-heal",
            "pin-and-consent",
            "quarantine",
            "swarm-emulate",
            "review-pack",
        ],
        "notes": (
            "do-once; verify-at-scale for tiny ≈ 1–2 checks; "
            "no museum of gates for a 2-line change"
        ),
    },
    "small": {
        "tools": [
            "ask-spec",
            "harness-plan",
            "activate",
            "route",
            "gate",
            "work-order",
            "tdd",
            "proportionality",
            "done",
            "finish",
        ],
        "optional": ["critique", "claim-audit"],
        "forbidden": [
            "excavate",
            "sandbox",
            "sot",
            "steal-flow",
            "swarm-emulate",
            "parallel",
            "heal",
            "triage",
            "reproduce",
            "process-heal",
        ],
        "notes": "bounded patch; one critique pass max when optional",
    },
    "medium": {
        "tools": [
            "ask-spec",
            "harness-plan",
            "activate",
            "route",
            "gate",
            "work-order",
            "tdd",
            "proportionality",
            "critique",
            "claim-audit",
            "grill",
            "review-pack",
            "forge",
            "context",
            "done",
            "finish",
        ],
        "optional": ["heal", "iso"],
        "forbidden": [
            "excavate",
            "swarm-emulate",
            "unbounded-steal",
        ],
        "notes": "feature-scale; harness caps cycles — agent does not invent force",
    },
    "large": {
        "tools": [
            "ask-spec",
            "harness-plan",
            "activate",
            "route",
            "gate",
            "work-order",
            "tdd",
            "proportionality",
            "critique",
            "claim-audit",
            "grill",
            "review-pack",
            "forge",
            "context",
            "heal",
            "iso",
            "sandbox",
            "sot",
            "excavate",
            "steal-flow",
            "triage",
            "reproduce",
            "process-heal",
            "done",
            "finish",
        ],
        "optional": ["parallel", "subagent", "pin-and-consent", "quarantine"],
        "forbidden": [
            "unbounded-swarm",
        ],
        "notes": "full factory; still capped by effort_class totals",
    },
}

_PLAN_SIGNAL = re.compile(
    r"(?i)\b("
    r"harness[- ]?plan"
    r"|tool[- ]?force"
    r"|HARNESS_OWNS_TOOL_AND_FORCE"
    r"|harness\s+owns\s+tool"
    r")\b"
    r"|harness-plan\.md"
    r"|harness-plan\.json"
)

_EFFORT = re.compile(
    r"(?im)(?:\*\*)?effort[_ -]?class:?\*?\*?\s*:?\s*(?:\*\*)?\s*"
    r"(tiny|small|medium|large)\b"
)
_TOOLS_HDR = re.compile(r"(?im)^\s{0,6}#{1,6}\s+Tools\b|^\s{0,6}(?:\*\*)?tools:?\*?\*?\s*$")
_CAPS_HDR = re.compile(r"(?im)^\s{0,6}#{1,6}\s+Caps\b|^\s{0,6}(?:\*\*)?caps:?\*?\*?\s*$")
_FORBID_HDR = re.compile(
    r"(?im)^\s{0,6}#{1,6}\s+Forbidden\b|^\s{0,6}(?:\*\*)?forbidden:?\*?\*?\s*$"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _task_root(path: Path) -> Path:
    if path.is_dir():
        return path
    if path.is_file():
        return path.parent
    return path


def caps_for(effort_class: str) -> dict[str, int]:
    cls = effort_class.lower().strip()
    if cls not in EFFORT_CAPS:
        raise ValueError(f"effort_class must be one of {EFFORT_CLASSES}, got {effort_class}")
    return dict(EFFORT_CAPS[cls])


def select_force(effort_class: str) -> dict[str, Any]:
    """Return harness-owned tools / caps / forbidden for effort_class."""
    cls = effort_class.lower().strip()
    if cls not in FORCE_TABLE:
        raise ValueError(f"effort_class must be one of {EFFORT_CLASSES}, got {effort_class}")
    row = FORCE_TABLE[cls]
    return {
        "effort_class": cls,
        "owner": "harness",
        "tools": list(row["tools"]),
        "optional": list(row["optional"]),
        "forbidden": list(row["forbidden"]),
        "caps": caps_for(cls),
        "notes": row["notes"],
        "iron": IRON,
    }


def plan_to_markdown(plan: dict[str, Any]) -> str:
    caps = plan["caps"]
    lines = [
        "# Harness plan",
        "",
        f"effort_class: {plan['effort_class']}",
        f"owner: {plan['owner']}",
        f"iron: {plan['iron']}",
        "",
        "## Tools",
    ]
    for t in plan["tools"]:
        lines.append(f"- {t}")
    if plan.get("optional"):
        lines.append("")
        lines.append("## Optional")
        for t in plan["optional"]:
            lines.append(f"- {t}")
    lines.append("")
    lines.append("## Caps")
    for k in ("verify", "critique", "gate", "total"):
        lines.append(f"- {k}: {caps[k]}")
    lines.append("")
    lines.append("## Forbidden")
    for t in plan["forbidden"]:
        lines.append(f"- {t}")
    lines.append("")
    lines.append("## Force")
    lines.append(
        f"- proportionality: {plan['notes']}"
    )
    lines.append(
        "- harness selects tools + caps from effort_class; "
        "agent does not invent 20 verifications for a tiny ask"
    )
    lines.append("")
    return "\n".join(lines)


def plan_to_json(plan: dict[str, Any]) -> str:
    return json.dumps(plan, indent=2) + "\n"


def resolve_effort_class(
    path: Path | None = None,
    *,
    override: str | None = None,
) -> str:
    if override:
        cls = override.lower().strip()
        if cls not in EFFORT_CLASSES:
            raise ValueError(f"effort_class must be one of {EFFORT_CLASSES}, got {override}")
        return cls
    if path is not None and path.exists():
        cls = parse_effort_class(path)
        if cls:
            return cls
        # Also peek plan file / json for declared class
        text, _ = _combined_text(path)
        m = _EFFORT.search(text)
        if m:
            for g in m.groups():
                if g:
                    return g.lower()
        jp = _task_root(path) / PLAN_JSON
        if jp.is_file():
            try:
                data = json.loads(_read(jp))
                raw = data.get("effort_class")
                if isinstance(raw, str) and raw.lower() in EFFORT_CLASSES:
                    return raw.lower()
            except (OSError, json.JSONDecodeError):
                pass
    return "tiny"  # missing class → tiny (same as proportionality default)


def emit_plan(
    *,
    effort_class: str | None = None,
    from_path: Path | None = None,
) -> dict[str, Any]:
    cls = resolve_effort_class(from_path, override=effort_class)
    return select_force(cls)


def _combined_text(task_or_file: Path) -> tuple[str, list[Path]]:
    if task_or_file.is_file():
        return (_read(task_or_file), [task_or_file])
    if not task_or_file.is_dir():
        return ("", [])
    parts: list[str] = []
    sources: list[Path] = []
    for name in (
        "harness-plan.md",
        "harness_plan.md",
        "tool-force.md",
        "tool_force.md",
        "harness-plan.json",
        "ask-spec.md",
        "ask_spec.md",
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


def _has_plan_file(task: Path) -> Path | None:
    root = _task_root(task)
    if root.is_file():
        if root.name.lower() in PLAN_FILENAMES or root.name == PLAN_JSON:
            return root
        root = root.parent
    for name in (*PLAN_FILENAMES, PLAN_JSON):
        p = root / name
        if p.is_file():
            return p
    return None


def _has_plan_signal(path: Path, text: str) -> bool:
    if _PLAN_SIGNAL.search(text or ""):
        return True
    if _has_plan_file(path) is not None:
        return True
    # Task with ask-spec is "active" — plan required under --require-plan;
    # for activity-scoped check, ask-spec alone is enough to claim activity.
    if path.is_dir() or path.is_file():
        root = _task_root(path)
        for name in ("ask-spec.md", "ask_spec.md"):
            if (root / name).is_file():
                return True
    return False


def _has_activity(path: Path) -> bool:
    if not path.exists():
        return False
    text, _ = _combined_text(path)
    return _has_plan_signal(path, text)


def _parse_plan_markdown(text: str) -> dict[str, Any]:
    """Best-effort parse of harness-plan.md fields."""
    cls_m = _EFFORT.search(text)
    cls = None
    if cls_m:
        for g in cls_m.groups():
            if g:
                cls = g.lower()
                break
    tools: list[str] = []
    forbidden: list[str] = []
    caps: dict[str, int] = {}
    section = None
    for line in text.splitlines():
        if _TOOLS_HDR.search(line):
            section = "tools"
            continue
        if _CAPS_HDR.search(line):
            section = "caps"
            continue
        if _FORBID_HDR.search(line):
            section = "forbidden"
            continue
        if re.match(r"(?im)^\s{0,6}#{1,6}\s+\S", line) and section:
            # new unrelated header
            if not (_TOOLS_HDR.search(line) or _CAPS_HDR.search(line) or _FORBID_HDR.search(line)):
                section = None
            continue
        m = re.match(r"^\s*[-*]\s+(\S.+?)\s*$", line)
        if not m or section is None:
            # caps may be "verify: 2"
            cm = re.match(
                r"(?im)^\s*[-*]?\s*(verify|critique|gate|total)\s*[:=]\s*(\d+)\s*$",
                line,
            )
            if cm and section == "caps":
                caps[cm.group(1).lower()] = int(cm.group(2))
            continue
        item = m.group(1).strip().strip("*").strip("`")
        if section == "tools":
            tools.append(item.split()[0].lower())
        elif section == "forbidden":
            forbidden.append(item.split()[0].lower())
        elif section == "caps":
            cm = re.match(r"(?i)(verify|critique|gate|total)\s*[:=]\s*(\d+)", item)
            if cm:
                caps[cm.group(1).lower()] = int(cm.group(2))
    return {"effort_class": cls, "tools": tools, "forbidden": forbidden, "caps": caps}


def _load_plan(path: Path) -> dict[str, Any] | None:
    root = _task_root(path)
    jp = root / PLAN_JSON
    if jp.is_file():
        try:
            data = json.loads(_read(jp))
            if isinstance(data, dict) and data.get("effort_class"):
                return data
        except (OSError, json.JSONDecodeError):
            pass
    for name in PLAN_FILENAMES:
        p = root / name
        if p.is_file():
            return _parse_plan_markdown(_read(p))
    if path.is_file() and (
        path.name.lower() in PLAN_FILENAMES or path.name == PLAN_JSON
    ):
        if path.suffix.lower() == ".json":
            try:
                data = json.loads(_read(path))
                return data if isinstance(data, dict) else None
            except (OSError, json.JSONDecodeError):
                return None
        return _parse_plan_markdown(_read(path))
    return None


def _field_errors(plan: dict[str, Any] | None, expected_class: str | None) -> list[str]:
    if plan is None:
        return [
            "missing harness plan (need harness-plan.md / harness-plan.json "
            f"with tools / caps / forbidden — harness owns tool+force — see {LEAF})"
        ]
    errs: list[str] = []
    cls = plan.get("effort_class")
    if not isinstance(cls, str) or cls.lower() not in EFFORT_CLASSES:
        errs.append("harness plan missing effort_class: tiny|small|medium|large")
        cls = None
    else:
        cls = cls.lower()
    if expected_class and cls and cls != expected_class:
        errs.append(
            f"harness plan effort_class={cls} mismatches ask→spec "
            f"effort_class={expected_class}"
        )
    tools = plan.get("tools") or []
    if not isinstance(tools, list) or len(tools) < 2:
        errs.append("harness plan missing tools list (harness must select tools)")
    caps = plan.get("caps") or {}
    if not isinstance(caps, dict):
        errs.append("harness plan missing caps")
    else:
        for k in ("verify", "critique", "gate", "total"):
            if k not in caps:
                errs.append(f"harness plan caps missing {k}")
    forbidden = plan.get("forbidden")
    if forbidden is None or (isinstance(forbidden, list) and len(forbidden) == 0 and cls == "tiny"):
        # tiny must forbid heavy paths
        if cls == "tiny":
            errs.append(
                "harness plan tiny must list forbidden heavy paths "
                "(excavate/sandbox/critique/…)"
            )
    # Cap honesty: declared caps must not exceed class table
    if cls and isinstance(caps, dict) and cls in EFFORT_CAPS:
        table = EFFORT_CAPS[cls]
        for k in ("verify", "critique", "gate", "total"):
            try:
                n = int(caps.get(k, -1))
            except (TypeError, ValueError):
                continue
            if n > table[k]:
                errs.append(
                    f"harness plan caps.{k}={n} exceeds {cls} table cap={table[k]}"
                )
    # Tiny must not include forbidden heavy tools in tools list
    if cls == "tiny" and isinstance(tools, list):
        heavy = set(FORCE_TABLE["tiny"]["forbidden"])
        for t in tools:
            name = str(t).split()[0].lower()
            if name in heavy:
                errs.append(f"harness plan tiny must not select heavy tool: {name}")
    return errs


def validate(path: Path) -> list[str]:
    """Activity-scoped: empty errs when idle (no plan/ask-spec signal)."""
    if not path.exists():
        return [f"missing path: {path}"]
    text, _ = _combined_text(path)
    if not _has_plan_signal(path, text):
        return []
    plan = _load_plan(path)
    expected = parse_effort_class(_task_root(path))
    return _field_errors(plan, expected)


def require_plan(path: Path) -> list[str]:
    """Always-on: missing/invalid plan FAILS (never vacuous).

    Used by G0 after ask→spec — active task without harness plan FAILS.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    plan = _load_plan(path)
    expected = parse_effort_class(_task_root(path)) or resolve_effort_class(path)
    return _field_errors(plan, expected if parse_effort_class(_task_root(path)) else None)


def format_card() -> str:
    lines = [
        "HARNESS-PLAN checklist=yes",
        f"HARNESS-PLAN leaf={LEAF}",
        f"HARNESS-PLAN iron={IRON}",
        "STEP 1 id=ask name=Require ask→spec "
        "et=goal / done-when / out-of-scope / effort_class",
        "STEP 1 key=ask_spec.py --require-spec before plan",
        "STEP 2 id=select name=Harness selects tools + caps from effort_class "
        "et=tiny|small|medium|large → FORCE_TABLE",
        "STEP 2 key=Not agent recall — harness owns tool+force",
        "STEP 3 id=emit name=Write harness-plan.md (+ json) "
        "et=tools / caps / forbidden / notes",
        "STEP 3 key=HARD-GATE --reject-no-plan / --require-plan / --check-harness-plan",
        "STEP 4 id=drive name=Do-once at proportional scale "
        "et=tiny → few tools + low caps; forbid excavate/sandbox/critique museum",
        "STEP 4 key=LLM does not choose 20 verifications for a 2-line change",
        "",
        "MUST: After ask→spec, emit harness plan "
        "(scripts/emperor harness-plan --emit --from <task> --write "
        "<task>/harness-plan.md). G0 --require-plan FAILS without a plan.",
        "MUST-NOT: treat tool selection as agent-facing CLI trivia; run heavy "
        "paths (excavate/sandbox/critique/steal) on tiny asks; omit plan so "
        "the model invents force.",
        "HONESTY: --check-harness-plan idle SKIP; G0 --require-plan never "
        "vacuous when a task dir is checked.",
    ]
    return "\n".join(lines) + "\n"


def reject_no_plan() -> str:
    return (
        "REJECT NO PLAN: HARD-GATE — task path refuses work without a harness "
        "plan (tools + caps + forbidden from effort_class). Harness owns "
        "tool+force selection; agent does not invent verification count. "
        f"Open {LEAF}; run scripts/emperor harness-plan --emit --from <task> "
        "--write <task>/harness-plan.md; re-check with "
        "--check-harness-plan <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Emperor Time harness tool+force planner: select tools/caps/"
            "forbidden from ask→spec effort_class (HARD-GATE)"
        )
    )
    p.add_argument(
        "path",
        nargs="?",
        default=None,
        help="task dir / plan file (check) OR omitted for card",
    )
    p.add_argument(
        "--check-harness-plan",
        type=Path,
        metavar="PATH",
        default=None,
        help="harness-plan check (exit 1 on soft/missing when active)",
    )
    p.add_argument(
        "--reject-no-plan",
        action="store_true",
        help="Hard-gate: refuse missing harness plan (always exit 1)",
    )
    p.add_argument(
        "--require-plan",
        type=Path,
        metavar="PATH",
        default=None,
        help="Always-on: missing/invalid harness plan FAILS (never vacuous)",
    )
    p.add_argument(
        "--emit",
        action="store_true",
        help="Emit harness plan from effort_class / --from ask-spec task",
    )
    p.add_argument(
        "--from",
        dest="from_path",
        type=Path,
        default=None,
        help="Task dir / ask-spec to read effort_class from",
    )
    p.add_argument(
        "--effort-class",
        choices=list(EFFORT_CLASSES),
        default=None,
        help="Override effort_class on emit",
    )
    p.add_argument(
        "--write",
        type=Path,
        default=None,
        help="Write harness-plan.md to PATH (implies --emit); also writes .json sibling",
    )
    p.add_argument(
        "--json-only",
        action="store_true",
        help="With --emit / stdout: print JSON instead of markdown",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_no_plan:
        sys.stdout.write(reject_no_plan())
        return 1

    if args.require_plan is not None:
        errs = require_plan(args.require_plan)
        return report_check(
            "harness-plan", args.require_plan, errs, vacuous=False
        )

    if args.emit or args.write is not None or args.from_path is not None:
        try:
            plan = emit_plan(
                effort_class=args.effort_class,
                from_path=args.from_path,
            )
        except ValueError as exc:
            print(f"harness-plan FAIL: {exc}", file=sys.stderr)
            return 2
        if args.write is not None:
            out = args.write
            out.parent.mkdir(parents=True, exist_ok=True)
            if out.suffix.lower() == ".json":
                out.write_text(plan_to_json(plan), encoding="utf-8")
                md = out.with_suffix(".md")
                if md.name == "harness-plan.md" or True:
                    # also write md sibling when writing json named harness-plan.json
                    if out.name == PLAN_JSON:
                        (out.parent / "harness-plan.md").write_text(
                            plan_to_markdown(plan), encoding="utf-8"
                        )
            else:
                out.write_text(plan_to_markdown(plan), encoding="utf-8")
                jp = out.with_name(PLAN_JSON) if out.suffix.lower() == ".md" else out.parent / PLAN_JSON
                # Prefer same-dir harness-plan.json
                if out.name.lower() in PLAN_FILENAMES or out.suffix.lower() == ".md":
                    jp = out.parent / PLAN_JSON
                jp.write_text(plan_to_json(plan), encoding="utf-8")
            print(f"harness-plan: {out.resolve()}")
            print(f"effort_class: {plan['effort_class']}")
            print(f"tools: {', '.join(plan['tools'])}")
            print(
                "caps: "
                + ", ".join(f"{k}≤{v}" for k, v in plan["caps"].items())
            )
            return 0
        if args.json_only:
            sys.stdout.write(plan_to_json(plan))
        else:
            sys.stdout.write(plan_to_markdown(plan))
        return 0

    target = (
        args.check_harness_plan
        if args.check_harness_plan is not None
        else (Path(args.path) if args.path else None)
    )
    if target is None:
        sys.stdout.write(format_card())
        return 0

    errs = validate(target)
    vacuous = target.exists() and not _has_activity(target)
    return report_check("harness-plan", target, errs, vacuous=vacuous)


if __name__ == "__main__":
    raise SystemExit(main())
