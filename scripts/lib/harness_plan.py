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
  --reject-forbidden-used   refuse when a plan-forbidden tool was actually used
  --reject-extra-tools      refuse when a tool outside Tools∪Optional was used
  --reject-over-plan-caps   refuse when effort-cycles exceed plan Caps
  --reject-over-class-tools refuse when plan Tools/Optional/Forbidden
                            diverge from FORCE_TABLE[effort_class]
  --reject-class-mismatch   refuse when plan effort_class mismatches
                            ask→spec effort_class
  --reject-over-class-caps  refuse when plan Caps exceed EFFORT_CAPS[class]

Check / require / emit:
  --check-harness-plan PATH activity-scoped idle check (SKIP vacuous when idle)
  --check-forbidden PATH    activity-scoped: SKIP vacuous when no plan / idle;
                            FAIL when plan forbids a tool and task markers show
                            that tool was used; PASS when clean
  --check-allowed PATH      activity-scoped: SKIP vacuous when no plan / idle;
                            FAIL when a watched tool outside Tools∪Optional shows
                            use markers (forbid owns named bans; allowlist owns
                            unlisted thrash like tdd/work-order on tiny)
  --check-caps PATH         activity-scoped: SKIP vacuous when no plan / idle;
                            FAIL when effort-cycles.json exceeds plan Caps
                            (plan Caps bind even when tighter than class table;
                            proportionality still owns EFFORT_CAPS[class])
  --check-class-tools PATH  activity-scoped: SKIP vacuous when no plan / idle;
                            FAIL when plan Tools∪Optional exceed FORCE_TABLE
                            for effort_class, or Forbidden omits a class ban
  --check-ask-class PATH    activity-scoped: SKIP vacuous when no plan / idle;
                            FAIL when plan effort_class mismatches ask→spec
                            (ASK_CLASS_BIND — tiny→large rewrite cannot dodge
                            CLASS_TOOLS_BIND by upgrading the plan class)
                            (agent cannot upgrade tiny→tdd by rewriting the plan)
  --check-class-caps PATH   activity-scoped: SKIP vacuous when no plan / idle;
                            FAIL when plan Caps exceed EFFORT_CAPS[effort_class]
                            (CLASS_CAPS_BIND — inflate verify:16 on tiny plan
                            cannot finish green; tighter-than-class Caps OK)
  --require-plan PATH       always-on when task active: missing/invalid plan FAILS
                            (never vacuous — G0 calls this after ask→spec)
  --emit / --from / --effort-class / --write PATH

Positional PATH runs --check-harness-plan. No args prints the HARNESS-PLAN card.
Thin twins: scripts/harness-plan.sh / scripts/harness-plan.ps1
Alias: tool-force → same core.
G0 calls --require-plan after ask→spec.
G4 calls --check-forbidden then --check-allowed then --check-caps then
--check-class-tools then --check-ask-class then --check-class-caps after
proportionality.
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
from proportionality import EFFORT_CAPS, _load_cycles  # noqa: E402

LEAF = "references/mechanical-gates.md"
IRON = "HARNESS_OWNS_TOOL_AND_FORCE"
IRON_FORBID = "FORBIDDEN_TOOLS_NEVER_RUN"
IRON_ALLOW = "ALLOWED_TOOLS_ONLY"
IRON_CAPS = "PLAN_CAPS_BIND"
IRON_CLASS = "CLASS_TOOLS_BIND"
IRON_ASK_CLASS = "ASK_CLASS_BIND"
IRON_CLASS_CAPS = "CLASS_CAPS_BIND"
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
_OPTIONAL_HDR = re.compile(
    r"(?im)^\s{0,6}#{1,6}\s+Optional\b|^\s{0,6}(?:\*\*)?optional:?\*?\*?\s*$"
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
    optional: list[str] = []
    forbidden: list[str] = []
    caps: dict[str, int] = {}
    section = None
    for line in text.splitlines():
        if _TOOLS_HDR.search(line):
            section = "tools"
            continue
        if _OPTIONAL_HDR.search(line):
            section = "optional"
            continue
        if _CAPS_HDR.search(line):
            section = "caps"
            continue
        if _FORBID_HDR.search(line):
            section = "forbidden"
            continue
        if re.match(r"(?im)^\s{0,6}#{1,6}\s+\S", line) and section:
            # new unrelated header
            if not (
                _TOOLS_HDR.search(line)
                or _OPTIONAL_HDR.search(line)
                or _CAPS_HDR.search(line)
                or _FORBID_HDR.search(line)
            ):
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
        elif section == "optional":
            optional.append(item.split()[0].lower())
        elif section == "forbidden":
            forbidden.append(item.split()[0].lower())
        elif section == "caps":
            cm = re.match(r"(?i)(verify|critique|gate|total)\s*[:=]\s*(\d+)", item)
            if cm:
                caps[cm.group(1).lower()] = int(cm.group(2))
    return {
        "effort_class": cls,
        "tools": tools,
        "optional": optional,
        "forbidden": forbidden,
        "caps": caps,
    }


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
    # Cap honesty: declared caps must not exceed class table (CLASS_CAPS_BIND)
    errs.extend(_class_caps_errors(plan))
    # Class tools bind: Tools∪Optional ⊆ FORCE_TABLE; Forbidden ⊇ class bans
    errs.extend(_class_tools_errors(plan))
    return errs


# ---------------------------------------------------------------------------
# Forbidden-tool enforcement (plan-without-run theater → HARD-GATE)
# ---------------------------------------------------------------------------
# Detect "used" via peer-style activity markers. Plan files themselves list
# forbidden tool *names* — those mentions must NOT trip (false positive).

_PLAN_EXCLUDE_NAMES = frozenset(
    {
        "harness-plan.md",
        "harness_plan.md",
        "tool-force.md",
        "tool_force.md",
        "harness-plan.json",
        "ask-spec.md",
        "ask_spec.md",
        "README.md",
    }
)

# Per-tool activity: files / relative paths / cycle keys / text signals.
# Keep proportional — prefer concrete artifacts over loose word matches.
TOOL_ACTIVITY: dict[str, dict[str, Any]] = {
    "critique": {
        "files": ("critique.md", "self-critique.md"),
        "cycle_key": "critique",
        "signals": (
            r"(?i)\bCRITIQUE\s+(PASS|FAIL|COMPLETE|EIGHT)",
            r"(?i)\beight[- ]count\b",
            r"(?i)--check-critique\b",
            r"(?i)--reject-incomplete-critique\b",
        ),
    },
    "grill": {
        "files": ("grill.md", "path.md"),
        "signals": (
            r"(?i)\bgrill\s+(path|advance|PASS|FAIL)\b",
            r"(?i)PATH_AND_STAGE_BEFORE_IMPL",
            r"(?i)--check-path\b",
            r"(?i)--reject-no-path\b",
        ),
    },
    "sandbox": {
        "files": ("sandbox.md",),
        "paths": (
            ".emperor/sandbox/ports.json",
            ".emperor/sandbox/runtime/active",
        ),
        "signals": (
            r"(?i)\bSANDBOX\s+(READY|UP|PLAN)\b",
            r"(?i)\bsandbox\s+(plan|up|down|ports)\b",
            r"(?i)PLAN_BEFORE_SANDBOX_UP",
        ),
    },
    "excavate": {
        "files": ("excavate.md", "survey.md", "identify.md"),
        "signals": (
            r"(?i)\bexcavated\s+(from|as|language)\b",
            r"(?i)\bIDENTIFY\s+(PASS|FAIL)\b",
            r"(?i)\bemperor\s+excavate\b",
            r"(?i)--excavate\b",
            r"(?i)\bSURVEY\s+(PASS|READY)\b",
        ),
    },
    "sot": {
        "files": ("sot.md",),
        "paths": (".emperor/sot/",),
        "signals": (
            r"(?i)\bSOT\s+(READY|SYNC|FETCH)\b",
            r"(?i)FETCH_ONLY_NEVER_MUTATE_SOT",
            r"(?i)\bsot\s+(add-plugin|sync)\b",
        ),
    },
    "steal-flow": {
        "files": (
            "steal-flow.md",
            "sign-in.md",
            "signin.md",
            "dispatch.md",
            "steal-dispatch.md",
            "swarm.md",
        ),
        "signals": (
            r"(?i)SIGN-IN\s+HANDOFF",
            r"(?i)\bemperor\s+steal-flow\b",
            r"(?i)--check-signin\b",
            r"(?i)--check-dispatch\b",
            r"(?i)unbounded[- ]swarm",
        ),
    },
    "heal": {
        "files": ("heal.md", "heal-verify.md", "postmortem.md"),
        "signals": (
            r"(?i)\bheal[- ]?verify\b",
            r"(?i)TRIAD_THEN_POSTMORTEM",
            r"(?i)--check-heal\b",
            r"(?i)--reject-no-triad\b",
        ),
    },
    "parallel": {
        "files": ("parallel.md", "dispatch-parallel.md"),
        "signals": (
            r"(?i)\bparallel[- ]dispatch\b",
            r"(?i)--check-parallel\b",
            r"(?i)\bPARALLEL\s+(PASS|READY)\b",
        ),
    },
    "subagent": {
        "files": ("subagent.md", "subagents.md"),
        "signals": (
            r"(?i)\bsubagent[- ]driven\b",
            r"(?i)\bSUBAGENT\s+(PASS|READY)\b",
        ),
    },
    "forge": {
        "files": ("forge.md", "pr-consent.md"),
        "signals": (
            r"(?i)EMPEROR_CONSENT_PR",
            r"(?i)PR_CONSENT_BEFORE_PUBLIC",
            r"(?i)--check-pr-consent\b",
            r"(?i)\bforge\s+(PASS|READY|PR)\b",
        ),
    },
    "context-build": {
        "files": ("context.md", "thoughttrail.md", "super-context.md"),
        "signals": (
            r"(?i)GRAPH_THEN_TRAIL",
            r"(?i)--check-context\b",
            r"(?i)--check-trail\b",
            r"(?i)\bcontext[- ]build\b",
        ),
    },
    "triage": {
        "files": ("triage.md", "holy-triage.md"),
        "signals": (
            r"(?i)STOP_SNAPSHOT_BRACKET",
            r"(?i)--check-triage\b",
            r"(?i)--reject-no-triage\b",
            r"(?i)\bTRIAGE\s+(PASS|BLOCK)\b",
        ),
    },
    "reproduce": {
        "files": ("reproduce.md", "combat-ledger.md", "fingerprint.md"),
        "signals": (
            r"(?i)FINGERPRINT_THEN_COMBAT",
            r"(?i)--check-reproduce\b",
            r"(?i)--reject-no-repro\b",
        ),
    },
    "process-heal": {
        "files": ("process-heal.md", "process-healing.md"),
        "signals": (
            r"(?i)REGISTER_THEN_REENTER",
            r"(?i)--check-process-heal\b",
            r"(?i)--reject-no-register\b",
        ),
    },
    "pin-and-consent": {
        "files": ("pin-and-consent.md", "pin-consent.md", "jail-pin.md"),
        "signals": (
            r"(?i)PIN_THEN_CONSENT_BEFORE_ADAPT",
            r"(?i)--check-pin-consent\b",
            r"(?i)--reject-unpinned\b",
        ),
    },
    "quarantine": {
        "files": ("quarantine.md", "steal-quarantine.md"),
        "signals": (
            r"(?i)--check-quarantine\b",
            r"(?i)--reject-unquarantined\b",
            r"(?i)\bADMITTED\b.*\bREJECTED\b|\bQUARANTINE\s+(PASS|ADMIT)",
        ),
    },
    "swarm-emulate": {
        "files": ("swarm.md", "swarm-emulate.md"),
        "signals": (
            r"(?i)\bswarm[- ]emulate\b",
            r"(?i)--check-swarm\b",
            r"(?i)--reject-unbounded-swarm\b",
        ),
    },
    "review-pack": {
        "files": ("review-pack.md", "review_pack.md", "hetero.md"),
        "signals": (
            r"(?i)--check-isolation\b",
            r"(?i)--reject-unisolated\b",
            r"(?i)--reject-author-diary\b",
            r"(?i)\bemperor\s+review-pack\b",
            r"(?i)\bREVIEW[- ]PACK\s+(PASS|READY|EMIT)\b",
        ),
    },
    "tdd": {
        "files": ("tdd.md", "red-green.md", "rgr.md"),
        "signals": (
            r"(?i)\bTDD\s+(PASS|FAIL|RED|GREEN)\b",
            r"(?i)\bred[- ]green[- ]refactor\b",
            r"(?i)--reject-prod\b",
            r"(?i)\bemperor\s+tdd\b",
        ),
    },
    "work-order": {
        "files": ("work-order.md", "work_order.md"),
        "signals": (
            r"(?i)\bwork[- ]order\b.*\b(PASS|READY|EMIT)\b",
            r"(?i)--reject-tbd\b",
            r"(?i)--reject-no-tasks\b",
            r"(?i)\bemperor\s+work-order\b",
        ),
    },
    "claim-audit": {
        "files": ("claim-audit.md", "claims.md"),
        "signals": (
            r"(?i)CLAIM\s+AUDIT",
            r"(?i)--check-audit\b",
            r"(?i)--reject-unaudited\b",
            r"(?i)\bemperor\s+claim-audit\b",
        ),
    },
    "diagnose": {
        "files": ("diagnose.md", "diagnosis.md"),
        "signals": (
            r"(?i)CITE_OR_FAIL_REPORT",
            r"(?i)--check-report\b",
            r"(?i)--reject-no-report\b",
            r"(?i)\bemperor\s+diagnose\b",
        ),
    },
    "evidence": {
        "files": ("evidence.md", "verification.md"),
        "signals": (
            r"(?i)\bevidence\s+(PASS|READY|COMPLETE)\b",
            r"(?i)\bemperor\s+evidence\b",
            r"(?i)verification[- ]before[- ]completion",
        ),
    },
    "iso": {
        "files": ("iso.md", "worktree.md", "isolation.md"),
        "signals": (
            r"(?i)--reject-blind-create\b",
            r"(?i)\bemperor\s+iso\b",
            r"(?i)\bWORKTREE\s+(PASS|READY)\b",
        ),
    },
    "author": {
        "files": ("author.md", "skill-rgr.md"),
        "signals": (
            r"(?i)\bemperor\s+author\b",
            r"(?i)\bAUTHOR\s+(PASS|READY)\b",
            r"(?i)skill[- ]RGR",
        ),
    },
    "secrets": {
        "files": ("secrets.md",),
        "signals": (
            r"(?i)--reject-secret-leak\b",
            r"(?i)--check-env-redacted\b",
            r"(?i)\bemperor\s+secrets\b",
            r"(?i)\bSECRETS\s+(PASS|READY|LIST)\b",
        ),
    },
    "queue": {
        "files": ("queue.md",),
        "signals": (
            r"(?i)--reject-multi-wip\b",
            r"(?i)--check-wip\b",
            r"(?i)\bemperor\s+queue\b",
            r"(?i)REJECT\s+MULTI\s+WIP",
        ),
    },
    "unbounded-steal": {
        "files": ("steal-flow.md", "swarm.md"),
        "signals": (
            r"(?i)unbounded[- ](steal|swarm)",
            r"(?i)--reject-unbounded-swarm\b",
        ),
    },
    "unbounded-swarm": {
        "files": ("swarm.md", "swarm-emulate.md"),
        "signals": (
            r"(?i)unbounded[- ]swarm",
            r"(?i)--reject-unbounded-swarm\b",
        ),
    },
}


def _normalize_tool(name: str) -> str:
    return str(name).split()[0].lower().strip().strip("*").strip("`")


def _activity_text_excluding_plan(root: Path) -> str:
    """Scan task dir for activity text, excluding plan/spec files.

    Mentions of forbidden tool names inside harness-plan.md must not trip.
    """
    if root.is_file():
        if root.name.lower() in {n.lower() for n in _PLAN_EXCLUDE_NAMES}:
            return ""
        try:
            return _read(root)
        except OSError:
            return ""
    if not root.is_dir():
        return ""
    parts: list[str] = []
    for name in (
        "ledger.md",
        "claims.md",
        "brief.md",
        "work-order.md",
        "critique.md",
        "self-critique.md",
        "grill.md",
        "path.md",
        "sandbox.md",
        "sot.md",
        "heal.md",
        "heal-verify.md",
        "postmortem.md",
        "excavate.md",
        "survey.md",
        "identify.md",
        "triage.md",
        "reproduce.md",
        "process-heal.md",
        "forge.md",
        "context.md",
        "thoughttrail.md",
        "review-pack.md",
        "quarantine.md",
        "steal-flow.md",
        "dispatch.md",
        "sign-in.md",
        "swarm.md",
        "parallel.md",
        "subagent.md",
        "pin-and-consent.md",
        "notes.md",
    ):
        p = root / name
        if p.is_file():
            try:
                parts.append(_read(p)[:12000])
            except OSError:
                pass
    # Shallow extra .md (still skip plan/spec/README)
    try:
        for child in sorted(root.iterdir()):
            if not child.is_file() or child.suffix.lower() != ".md":
                continue
            if child.name.lower() in {n.lower() for n in _PLAN_EXCLUDE_NAMES}:
                continue
            if child.name in {
                "ledger.md",
                "claims.md",
                "brief.md",
                "work-order.md",
                "critique.md",
                "self-critique.md",
                "grill.md",
                "path.md",
            }:
                continue  # already read
            try:
                parts.append(_read(child)[:4000])
            except OSError:
                pass
    except OSError:
        pass
    return "\n".join(parts)


def _cycle_count(root: Path, key: str) -> int:
    p = root / "effort-cycles.json"
    if not p.is_file():
        return 0
    try:
        data = json.loads(_read(p))
    except (OSError, json.JSONDecodeError):
        return 0
    if not isinstance(data, dict):
        return 0
    try:
        return int(data.get(key, 0) or 0)
    except (TypeError, ValueError):
        return 0


def tool_was_used(root: Path, tool: str) -> bool:
    """True when task markers show *tool* actually ran (not plan theater)."""
    name = _normalize_tool(tool)
    spec = TOOL_ACTIVITY.get(name)
    if spec is None:
        # Unknown forbidden name: only trip on a dedicated marker file
        # `<tool>.md` or `<tool>_ran.md` — avoid false positives on words.
        for cand in (f"{name}.md", f"{name.replace('-', '_')}.md", f"{name}-ran.md"):
            if (root / cand).is_file():
                return True
        return False

    for fname in spec.get("files") or ():
        if (root / fname).is_file():
            return True
    for rel in spec.get("paths") or ():
        p = root / rel
        if p.exists():
            return True
    cycle_key = spec.get("cycle_key")
    if isinstance(cycle_key, str) and _cycle_count(root, cycle_key) > 0:
        return True
    text = _activity_text_excluding_plan(root)
    for pat in spec.get("signals") or ():
        if re.search(pat, text or ""):
            return True
    return False


def list_forbidden_used(path: Path) -> list[str]:
    """Return forbidden tools that show activity markers under task."""
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    forbidden = plan.get("forbidden") or []
    if not isinstance(forbidden, list):
        return []
    used: list[str] = []
    for raw in forbidden:
        name = _normalize_tool(raw)
        if not name:
            continue
        if tool_was_used(root, name):
            used.append(name)
    return used


def validate_forbidden(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no plan (idle / vacuous).

    When a harness plan exists, FAIL if any forbidden tool shows use markers.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    used = list_forbidden_used(root)
    if not used:
        return []
    return [
        f"forbidden tool used: {name} "
        f"(plan forbids it — {IRON_FORBID}; see {LEAF})"
        for name in used
    ]


def reject_forbidden_used() -> str:
    return (
        "REJECT FORBIDDEN USED: HARD-GATE — harness plan listed a tool as "
        "forbidden, but task markers show that tool actually ran (critique.md / "
        "effort-cycles critique stamps / sandbox plan emits / excavate markers / "
        "…). Plan-without-enforcement is soft theater. Open "
        f"{LEAF}; re-check with --check-forbidden <task-dir>. "
        f"IRON={IRON_FORBID}\n"
    )


def _allowed_set(plan: dict[str, Any]) -> set[str]:
    allowed: set[str] = set()
    for key in ("tools", "optional"):
        raw = plan.get(key) or []
        if not isinstance(raw, list):
            continue
        for item in raw:
            name = _normalize_tool(item)
            if name:
                allowed.add(name)
    return allowed


def _forbidden_set(plan: dict[str, Any]) -> set[str]:
    raw = plan.get("forbidden") or []
    if not isinstance(raw, list):
        return set()
    out: set[str] = set()
    for item in raw:
        name = _normalize_tool(item)
        if name:
            out.add(name)
    return out


def list_extra_used(path: Path) -> list[str]:
    """Return watched tools used outside plan Tools∪Optional.

    Named Forbidden tools are owned by --check-forbidden (sharper card);
    this list only reports unlisted extras (the allowlist gap).
    """
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    allowed = _allowed_set(plan)
    forbidden = _forbidden_set(plan)
    extras: list[str] = []
    for name in sorted(TOOL_ACTIVITY.keys()):
        if name in allowed or name in forbidden:
            continue
        if tool_was_used(root, name):
            extras.append(name)
    return extras


def validate_allowed(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no plan (idle / vacuous).

    When a harness plan exists, FAIL if a watched tool outside Tools∪Optional
    shows use markers (and is not already named Forbidden).
    """
    if not path.exists():
        return [f"missing path: {path}"]
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    extras = list_extra_used(root)
    if not extras:
        return []
    return [
        f"extra tool used: {name} "
        f"(not in plan Tools/Optional — {IRON_ALLOW}; see {LEAF})"
        for name in extras
    ]


def reject_extra_tools() -> str:
    return (
        "REJECT EXTRA TOOLS: HARD-GATE — harness plan Tools∪Optional is the "
        "allowlist, but task markers show an unlisted tool ran (tdd.md / "
        "work-order.md / diagnose.md / …). Forbid-enforce owns named bans; "
        "allowlist owns unlisted thrash. Open "
        f"{LEAF}; re-check with --check-allowed <task-dir>. "
        f"IRON={IRON_ALLOW}\n"
    )


def list_over_plan_caps(path: Path) -> list[tuple[str, int, int]]:
    """Return (kind, count, cap) triples where cycles exceed plan Caps.

    Plan Caps are the harness-owned force budget written into harness-plan.
    They may be tighter than EFFORT_CAPS[effort_class]; when tighter, they win.
    Proportionality still enforces the class table separately.
    """
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    caps = plan.get("caps") or {}
    if not isinstance(caps, dict):
        return []
    counts = _load_cycles(root)
    over: list[tuple[str, int, int]] = []
    for kind in ("verify", "critique", "gate", "total"):
        if kind not in caps:
            continue
        try:
            cap = int(caps[kind])
        except (TypeError, ValueError):
            continue
        n = int(counts.get(kind, 0) or 0)
        if n > cap:
            over.append((kind, n, cap))
    return over


def validate_caps(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no plan (idle / vacuous).

    When a harness plan exists, FAIL if effort-cycles exceed plan Caps.
    Missing cycle ledger counts as zeros (under any non-negative cap → PASS).
    Incomplete Caps (missing verify/critique/gate/total) FAIL so plan theater
    cannot dodge by omitting the budget lines.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    caps = plan.get("caps") or {}
    errs: list[str] = []
    if not isinstance(caps, dict):
        return [
            f"harness plan missing caps "
            f"(plan Caps bind force — {IRON_CAPS}; see {LEAF})"
        ]
    for k in ("verify", "critique", "gate", "total"):
        if k not in caps:
            errs.append(
                f"harness plan caps missing {k} "
                f"({IRON_CAPS}; see {LEAF})"
            )
    if errs:
        return errs
    over = list_over_plan_caps(root)
    for kind, n, cap in over:
        errs.append(
            f"plan cap exceeded: {kind}={n} > plan.caps.{kind}={cap} "
            f"({IRON_CAPS}; see {LEAF})"
        )
    return errs


def reject_over_plan_caps() -> str:
    return (
        "REJECT OVER PLAN CAPS: HARD-GATE — harness plan Caps are the force "
        "budget, but effort-cycles.json exceeds them (verify/critique/gate/"
        "total). Class-table proportionality is a separate ceiling; plan Caps "
        "bind even when tighter (tiny plan verify:1 still FAILS at 2). Open "
        f"{LEAF}; re-check with --check-caps <task-dir>. "
        f"IRON={IRON_CAPS}\n"
    )



def _norm_tool(name: Any) -> str:
    return str(name).split()[0].lower().strip()


def _class_tools_errors(plan: dict[str, Any]) -> list[str]:
    """Plan Tools/Optional/Forbidden must honor FORCE_TABLE[effort_class].

    Closes force-upgrade soft theater: a tiny plan that lists tdd/work-order
    under Tools (or omits excavate from Forbidden) can no longer finish green.
    Returns [] when effort_class is missing/invalid — other validators own that.
    """
    cls = plan.get("effort_class")
    if not isinstance(cls, str) or cls.lower() not in FORCE_TABLE:
        return []
    cls = cls.lower()
    row = FORCE_TABLE[cls]
    allowed = {
        _norm_tool(x)
        for x in list(row.get("tools") or []) + list(row.get("optional") or [])
        if _norm_tool(x)
    }
    errs: list[str] = []
    for section in ("tools", "optional"):
        for t in plan.get(section) or []:
            n = _norm_tool(t)
            if n and n not in allowed:
                errs.append(
                    f"harness plan {cls} must not select over-class tool: {n} "
                    f"(not in FORCE_TABLE[{cls}] tools∪optional — "
                    f"{IRON_CLASS}; see {LEAF})"
                )
    have = {_norm_tool(x) for x in (plan.get("forbidden") or []) if _norm_tool(x)}
    for f in row.get("forbidden") or []:
        fn = _norm_tool(f)
        if fn and fn not in have:
            errs.append(
                f"harness plan {cls} missing forbidden tool: {fn} "
                f"(FORCE_TABLE[{cls}] forbid must bind — {IRON_CLASS}; see {LEAF})"
            )
    return errs


def list_class_tools_violations(path: Path) -> list[tuple[str, str]]:
    """Return (kind, name) for over-class Tools/Optional or missing Forbidden."""
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    cls = plan.get("effort_class")
    if not isinstance(cls, str) or cls.lower() not in FORCE_TABLE:
        return []
    cls = cls.lower()
    row = FORCE_TABLE[cls]
    allowed = {
        _norm_tool(x)
        for x in list(row.get("tools") or []) + list(row.get("optional") or [])
        if _norm_tool(x)
    }
    out: list[tuple[str, str]] = []
    for section in ("tools", "optional"):
        for t in plan.get(section) or []:
            n = _norm_tool(t)
            if n and n not in allowed:
                out.append(("extra-tool", n))
    have = {_norm_tool(x) for x in (plan.get("forbidden") or []) if _norm_tool(x)}
    for f in row.get("forbidden") or []:
        fn = _norm_tool(f)
        if fn and fn not in have:
            out.append(("missing-forbid", fn))
    return out


def validate_class_tools(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no plan (idle / vacuous).

    When a harness plan exists, FAIL if Tools∪Optional exceed FORCE_TABLE
    for the plan's effort_class, or Forbidden omits a class-table ban.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    cls = plan.get("effort_class")
    if not isinstance(cls, str) or cls.lower() not in FORCE_TABLE:
        return [
            f"harness plan missing effort_class for FORCE_TABLE bind "
            f"({IRON_CLASS}; see {LEAF})"
        ]
    return _class_tools_errors(plan)


def reject_over_class_tools() -> str:
    return (
        "REJECT OVER CLASS TOOLS: HARD-GATE — harness plan Tools∪Optional/"
        "Forbidden must honor FORCE_TABLE[effort_class]. Agent cannot upgrade "
        "force by writing tdd/work-order into a tiny plan or un-forbidding "
        f"excavate. Open {LEAF}; re-check with --check-class-tools <task-dir>. "
        f"IRON={IRON_CLASS}\n"
    )


def list_ask_class_mismatch(path: Path) -> list[tuple[str, str]]:
    """Return (plan_class, ask_class) when they diverge; else []."""
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    plan_cls = plan.get("effort_class")
    if not isinstance(plan_cls, str) or plan_cls.lower() not in EFFORT_CLASSES:
        return []
    plan_cls = plan_cls.lower()
    ask_cls = parse_effort_class(root)
    if ask_cls is None:
        return []
    ask_cls = ask_cls.lower()
    if plan_cls != ask_cls:
        return [(plan_cls, ask_cls)]
    return []


def validate_ask_class(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no plan (idle / vacuous).

    When a harness plan exists, FAIL if plan.effort_class mismatches
    ask→spec effort_class, or ask→spec class is missing while a plan exists.
    Closes the tiny→large rewrite bypass of CLASS_TOOLS_BIND: upgrading the
    plan class makes FORCE_TABLE[large] green while ask→spec stayed tiny.
    """
    if not path.exists():
        return [f"missing path: {path}"]
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    plan_cls = plan.get("effort_class")
    if not isinstance(plan_cls, str) or plan_cls.lower() not in EFFORT_CLASSES:
        return [
            f"harness plan missing effort_class for ask→spec bind "
            f"({IRON_ASK_CLASS}; see {LEAF})"
        ]
    plan_cls = plan_cls.lower()
    ask_cls = parse_effort_class(root)
    if ask_cls is None:
        return [
            f"missing ask→spec effort_class to bind plan effort_class={plan_cls} "
            f"({IRON_ASK_CLASS}; see {LEAF})"
        ]
    ask_cls = ask_cls.lower()
    if plan_cls != ask_cls:
        return [
            f"harness plan effort_class={plan_cls} mismatches ask→spec "
            f"effort_class={ask_cls} ({IRON_ASK_CLASS}; see {LEAF})"
        ]
    return []


def reject_class_mismatch() -> str:
    return (
        "REJECT CLASS MISMATCH: HARD-GATE — harness plan effort_class must "
        "match ask→spec effort_class. Agent cannot upgrade force by rewriting "
        "a tiny plan to large (which would make CLASS_TOOLS_BIND green against "
        f"FORCE_TABLE[large]). Open {LEAF}; re-check with "
        f"--check-ask-class <task-dir>. IRON={IRON_ASK_CLASS}\n"
    )


def _class_caps_errors(plan: dict[str, Any]) -> list[str]:
    """Plan Caps must not exceed EFFORT_CAPS[effort_class].

    Closes cap-inflate soft theater: a tiny plan that keeps Tools inside
    FORCE_TABLE[tiny] but rewrites Caps to large (verify:16) can no longer
    finish green. Tighter-than-class Caps remain allowed (PLAN_CAPS_BIND).
    Returns [] when effort_class is missing/invalid — other validators own that.
    """
    cls = plan.get("effort_class")
    if not isinstance(cls, str) or cls.lower() not in EFFORT_CAPS:
        return []
    cls = cls.lower()
    caps = plan.get("caps") or {}
    if not isinstance(caps, dict):
        return []
    table = EFFORT_CAPS[cls]
    errs: list[str] = []
    for k in ("verify", "critique", "gate", "total"):
        if k not in caps:
            continue
        try:
            n = int(caps[k])
        except (TypeError, ValueError):
            continue
        if n > table[k]:
            errs.append(
                f"harness plan caps.{k}={n} exceeds {cls} table cap={table[k]} "
                f"({IRON_CLASS_CAPS}; see {LEAF})"
            )
    return errs


def list_over_class_caps(path: Path) -> list[tuple[str, int, int]]:
    """Return (kind, plan_cap, table_cap) where plan Caps exceed class table."""
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    cls = plan.get("effort_class")
    if not isinstance(cls, str) or cls.lower() not in EFFORT_CAPS:
        return []
    cls = cls.lower()
    caps = plan.get("caps") or {}
    if not isinstance(caps, dict):
        return []
    table = EFFORT_CAPS[cls]
    over: list[tuple[str, int, int]] = []
    for k in ("verify", "critique", "gate", "total"):
        if k not in caps:
            continue
        try:
            n = int(caps[k])
        except (TypeError, ValueError):
            continue
        if n > table[k]:
            over.append((k, n, table[k]))
    return over


def validate_class_caps(path: Path) -> list[str]:
    """Activity-scoped: empty errs when no plan (idle / vacuous).

    When a harness plan exists, FAIL if plan Caps exceed EFFORT_CAPS for the
    plan's effort_class. Incomplete Caps (missing verify/critique/gate/total)
    FAIL so plan theater cannot dodge by omitting the budget lines.
    Tighter-than-class Caps PASS (PLAN_CAPS_BIND owns that force).
    """
    if not path.exists():
        return [f"missing path: {path}"]
    root = _task_root(path)
    plan = _load_plan(root)
    if plan is None:
        return []
    cls = plan.get("effort_class")
    if not isinstance(cls, str) or cls.lower() not in EFFORT_CAPS:
        return [
            f"harness plan missing effort_class for EFFORT_CAPS bind "
            f"({IRON_CLASS_CAPS}; see {LEAF})"
        ]
    caps = plan.get("caps") or {}
    errs: list[str] = []
    if not isinstance(caps, dict):
        return [
            f"harness plan missing caps "
            f"(class Caps bind force — {IRON_CLASS_CAPS}; see {LEAF})"
        ]
    for k in ("verify", "critique", "gate", "total"):
        if k not in caps:
            errs.append(
                f"harness plan caps missing {k} "
                f"({IRON_CLASS_CAPS}; see {LEAF})"
            )
    if errs:
        return errs
    return _class_caps_errors(plan)


def reject_over_class_caps() -> str:
    return (
        "REJECT OVER CLASS CAPS: HARD-GATE — harness plan Caps must not exceed "
        "EFFORT_CAPS[effort_class]. Agent cannot inflate force by rewriting a "
        "tiny plan's Caps to large (verify:16) while CLASS_TOOLS_BIND and "
        "ASK_CLASS_BIND stay green. Tighter-than-class Caps remain allowed "
        f"(PLAN_CAPS_BIND). Open {LEAF}; re-check with "
        f"--check-class-caps <task-dir>. IRON={IRON_CLASS_CAPS}\n"
    )


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
        "STEP 3 key=HARD-GATE --reject-no-plan / --require-plan / --check-harness-plan / --check-forbidden / --reject-forbidden-used / --check-class-tools / --reject-over-class-tools / --check-ask-class / --reject-class-mismatch / --check-class-caps / --reject-over-class-caps",
        "STEP 4 id=drive name=Do-once at proportional scale "
        "et=tiny → few tools + low caps; forbid excavate/sandbox/critique museum",
        "STEP 4 key=LLM does not choose 20 verifications for a 2-line change",
        "",
        "MUST: After ask→spec, emit harness plan "
        "(scripts/emperor harness-plan --emit --from <task> --write "
        "<task>/harness-plan.md). G0 --require-plan FAILS without a plan. "
        "G4 --check-forbidden FAILS when a forbidden tool was actually used. "
        "G4 --check-allowed FAILS when an unlisted tool outside Tools/Optional "
        "ran. G4 --check-caps FAILS when effort-cycles exceed plan Caps. "
        "G4 --check-class-tools FAILS when plan Tools/Optional/Forbidden "
        "diverge from FORCE_TABLE[effort_class]. "
        "G4 --check-ask-class FAILS when plan effort_class mismatches "
        "ask→spec (tiny→large rewrite cannot dodge CLASS_TOOLS_BIND). "
        "G4 --check-class-caps FAILS when plan Caps exceed EFFORT_CAPS"
        "[effort_class] (inflate verify:16 on tiny cannot finish green).",
        "MUST-NOT: treat tool selection as agent-facing CLI trivia; run heavy "
        "paths (excavate/sandbox/critique/steal) on tiny asks; omit plan so "
        "the model invents force; write a tiny plan then thrash forbidden "
        "tools; rewrite a tiny plan to list tdd/work-order or un-forbid excavate; "
        "rewrite plan effort_class tiny→large to dodge CLASS_TOOLS_BIND; "
        "inflate plan Caps past EFFORT_CAPS[class] while keeping class+tools green.",
        "HONESTY: --check-harness-plan / --check-forbidden / --check-allowed / "
        "--check-caps / --check-class-tools / --check-ask-class / "
        "--check-class-caps idle SKIP; "
        "G0 --require-plan never vacuous; plan file listing a tool under "
        "Forbidden is not itself 'use' of that tool; tighter-than-class Caps OK.",
        f"IRON forbid={IRON_FORBID}",
        f"IRON allow={IRON_ALLOW}",
        f"IRON caps={IRON_CAPS}",
        f"IRON class={IRON_CLASS}",
        f"IRON ask-class={IRON_ASK_CLASS}",
        f"IRON class-caps={IRON_CLASS_CAPS}",
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
        "--check-forbidden",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Forbidden-tool enforce: FAIL when plan forbids a tool that was "
            "used; SKIP vacuous when no plan / idle"
        ),
    )
    p.add_argument(
        "--reject-forbidden-used",
        action="store_true",
        help="Hard-gate card: refuse when forbidden tools were used (always exit 1)",
    )
    p.add_argument(
        "--check-allowed",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Allowlist enforce: FAIL when a watched tool outside Tools∪Optional "
            "was used; SKIP vacuous when no plan / idle"
        ),
    )
    p.add_argument(
        "--reject-extra-tools",
        action="store_true",
        help="Hard-gate card: refuse when extra (unlisted) tools were used (always exit 1)",
    )
    p.add_argument(
        "--check-caps",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Plan-caps enforce: FAIL when effort-cycles exceed plan Caps; "
            "SKIP vacuous when no plan / idle"
        ),
    )
    p.add_argument(
        "--reject-over-plan-caps",
        action="store_true",
        help="Hard-gate card: refuse when cycles exceed plan Caps (always exit 1)",
    )
    p.add_argument(
        "--check-class-tools",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Class-tools bind: FAIL when plan Tools∪Optional/Forbidden diverge "
            "from FORCE_TABLE[effort_class]; SKIP vacuous when no plan / idle"
        ),
    )
    p.add_argument(
        "--reject-over-class-tools",
        action="store_true",
        help=(
            "Hard-gate card: refuse when plan upgrades force past FORCE_TABLE "
            "(always exit 1)"
        ),
    )
    p.add_argument(
        "--check-ask-class",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Ask-class bind: FAIL when plan effort_class mismatches ask→spec; "
            "SKIP vacuous when no plan / idle"
        ),
    )
    p.add_argument(
        "--reject-class-mismatch",
        action="store_true",
        help=(
            "Hard-gate card: refuse when plan effort_class mismatches ask→spec "
            "(always exit 1)"
        ),
    )
    p.add_argument(
        "--check-class-caps",
        type=Path,
        metavar="PATH",
        default=None,
        help=(
            "Class-caps bind: FAIL when plan Caps exceed EFFORT_CAPS[effort_class]; "
            "SKIP vacuous when no plan / idle"
        ),
    )
    p.add_argument(
        "--reject-over-class-caps",
        action="store_true",
        help=(
            "Hard-gate card: refuse when plan Caps exceed class table "
            "(always exit 1)"
        ),
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

    if args.reject_forbidden_used:
        sys.stdout.write(reject_forbidden_used())
        return 1

    if args.reject_extra_tools:
        sys.stdout.write(reject_extra_tools())
        return 1

    if args.reject_over_plan_caps:
        sys.stdout.write(reject_over_plan_caps())
        return 1

    if args.reject_over_class_tools:
        sys.stdout.write(reject_over_class_tools())
        return 1

    if args.reject_class_mismatch:
        sys.stdout.write(reject_class_mismatch())
        return 1

    if args.reject_over_class_caps:
        sys.stdout.write(reject_over_class_caps())
        return 1

    if args.check_class_caps is not None:
        target = args.check_class_caps
        errs = validate_class_caps(target)
        plan = _load_plan(target) if target.exists() else None
        vacuous = target.exists() and plan is None and not errs
        return report_check("harness-class-caps", target, errs, vacuous=vacuous)

    if args.check_ask_class is not None:
        target = args.check_ask_class
        errs = validate_ask_class(target)
        plan = _load_plan(target) if target.exists() else None
        vacuous = target.exists() and plan is None and not errs
        return report_check("harness-ask-class", target, errs, vacuous=vacuous)

    if args.check_class_tools is not None:
        target = args.check_class_tools
        errs = validate_class_tools(target)
        plan = _load_plan(target) if target.exists() else None
        vacuous = target.exists() and plan is None and not errs
        return report_check("harness-class-tools", target, errs, vacuous=vacuous)

    if args.check_caps is not None:
        target = args.check_caps
        errs = validate_caps(target)
        plan = _load_plan(target) if target.exists() else None
        vacuous = target.exists() and plan is None and not errs
        return report_check("harness-caps", target, errs, vacuous=vacuous)

    if args.check_forbidden is not None:
        target = args.check_forbidden
        errs = validate_forbidden(target)
        plan = _load_plan(target) if target.exists() else None
        vacuous = target.exists() and plan is None and not errs
        return report_check("harness-forbid", target, errs, vacuous=vacuous)

    if args.check_allowed is not None:
        target = args.check_allowed
        errs = validate_allowed(target)
        plan = _load_plan(target) if target.exists() else None
        vacuous = target.exists() and plan is None and not errs
        return report_check("harness-allow", target, errs, vacuous=vacuous)

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
