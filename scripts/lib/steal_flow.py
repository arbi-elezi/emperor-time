#!/usr/bin/env python3
"""Validate Emperor Time Steal sign-in / dispatch / swarm HARD-GATEs.

Doctrine leaves:
  chains/steal-chain/sign-in-handoff.md
  chains/steal-chain/dispatch.md
  chains/steal-chain/swarm-emulate.md

Already hard elsewhere: consent.py, quarantine.py. parallel.py covers
independent-domain checklist only — not these three leaves.

Always-fail HARD-GATE helpers:
  --reject-no-signin            refuse missing SIGN-IN HANDOFF
  --reject-no-dispatch-layout   refuse missing runs layout / prompt anatomy
  --reject-unbounded-swarm      refuse unbounded / overlapping swarm

Check modes (vacuous PASS when no matching activity):
  --check-signin PATH
  --check-dispatch PATH
  --check-swarm PATH

Positional PATH runs all three checks. No args prints the STEAL-FLOW card.
Thin twins: scripts/steal-flow.sh / scripts/steal-flow.ps1
Aliases: sign-in-handoff, steal-dispatch, swarm-emulate → same core.
G4 in gate.py calls the three checks when steal activity is present.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Sequence

LEAF_SIGNIN = "chains/steal-chain/sign-in-handoff.md"
LEAF_DISPATCH = "chains/steal-chain/dispatch.md"
LEAF_SWARM = "chains/steal-chain/swarm-emulate.md"

DEFAULT_SWARM_N = 4

_SIGNIN_SIGNAL = re.compile(
    r"(?i)\b("
    r"NEEDS[- ]SIGN[- ]IN"
    r"|SIGN[- ]IN\s+HANDOFF"
    r"|sign[- ]in\s+handoff"
    r"|auth(?:entication)?\s+handoff"
    r"|needs\s+(?:sign[- ]in|auth)\b"
    r"|client\s+(?:must|should)\s+(?:sign\s*in|log\s*in|authenticate)"
    r")\b"
)

_HANDOFF = re.compile(
    r"(?i)(?<![\w-])(?<!no\s)(?<!without\s)(?<!missing\s)"
    r"SIGN[- ]IN\s+HANDOFF\s*:"
)

_AGENT_IN_HANDOFF = re.compile(
    r"(?i)SIGN[- ]IN\s+HANDOFF\s*:\s*([A-Za-z][\w./-]*)"
)

_CLIENT_DONE = re.compile(
    r"(?i)\b("
    r"client\s+completed"
    r"|client\s+ran"
    r"|client\s+performed"
    r"|client\s+finished"
    r"|in\s+their\s+(?:own\s+)?(?:new\s+)?terminal"
    r"|client\s+terminal"
    r")\b"
)

_VERIFIED = re.compile(
    r"(?i)\b("
    r"verified\s*:"
    r"|AVAILABLE\s*\(\s*verified"
    r"|status\s+(?:cmd|command)"
    r"|login\s+status"
    r"|auth\s+status"
    r"|exit\s*0"
    r"|exit\s+code\s*0"
    r")\b"
)

_CREDENTIAL_SHAPE = re.compile(
    r"(?i)("
    r"\b(?:sk|pk|api)[-_][A-Za-z0-9]{16,}"
    r"|\bBearer\s+[A-Za-z0-9._\-]{20,}"
    r"|\b(?:password|passwd|secret|api[_-]?key|access[_-]?token)\s*[=:]\s*\S+"
    r"|\bghp_[A-Za-z0-9]{20,}"
    r"|\bxox[baprs]-[A-Za-z0-9-]{10,}"
    r")"
)

_DISPATCH_SIGNAL = re.compile(
    r"(?i)(?<!no\s)(?<!without\s)(?<!missing\s)\b("
    r"STEAL\s+(?:dispatch|worker|chain|enlist)"
    r"|\.emperor/runs"
    r"|dispatch(?:ed|ing)?\s+(?:worker|agent|to)"
    r"|worker\s+(?:done|dispatched|prompt)"
    r"|steal[- ]dispatch"
    r"|prompt\.md"
    r")\b"
)

_OBJECTIVE = re.compile(r"(?im)^\s*OBJECTIVE\s*:")
_SCOPE = re.compile(r"(?im)^\s*SCOPE\s*:")
_EXIT_OR_TIMEOUT = re.compile(
    r"(?i)\b("
    r"exit(?:\s+code)?\s*[:=]?\s*-?\d+"
    r"|timeout\s*[:=]?\s*\S+"
    r"|timed?\s*out"
    r"|wall\s*time"
    r")\b"
)

_SWARM_SIGNAL = re.compile(
    r"(?i)\b("
    r"swarm[- ]emulate"
    r"|swarm\s+emulat"
    r"|EMPEROR_SWARM_N"
    r"|swarm-\d+"
    r"|fan[- ]out"
    r"|AgentSwarm"
    r"|/swarm\b"
    r"|N\s*=\s*\d+\s*(?:workers?|agents?|items?)?"
    r"|bound\s+N\b"
    r")\b"
)

_BOUND_N = re.compile(
    r"(?i)\b("
    r"EMPEROR_SWARM_N\s*=\s*(\d+)"
    r"|bound\s+N\s*=\s*(\d+)"
    r"|N\s*=\s*(\d+)\s*(?:workers?|agents?|items?)?"
    r"|swarm\s+N\s*=\s*(\d+)"
    r"|cap\s+(\d+)"
    r")\b"
)

_DISJOINT = re.compile(
    r"(?i)\b("
    r"disjoint\s+SCOPE"
    r"|SCOPE\s+(?:lists?\s+)?(?:are\s+)?disjoint"
    r"|no\s+shared\s+writ(?:eable|able)\s+file"
    r"|scopes?\s+do\s+not\s+overlap"
    r"|non[- ]overlapping\s+SCOPE"
    r")\b"
)

_SYNTHESIS = re.compile(
    r"(?i)\b("
    r"synthesiz(?:e|ed|ing)\s+(?:myself|yourself|self)?"
    r"|synthesis\s*(?:note)?\s*:"
    r"|I\s+(?:merged|synthesized)\s+(?:the\s+)?(?:swarm|siblings?|workers?)"
    r"|orchestrator\s+synthes"
    r")\b"
)

_SIGNIN_NAMES = {
    "sign-in-handoff.md",
    "signin-handoff.md",
    "handoff.md",
    "signin.md",
}
_DISPATCH_NAMES = {
    "dispatch.md",
    "steal-dispatch.md",
    "prompt.md",
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _combined_text(task_or_file: Path) -> str:
    if task_or_file.is_file():
        return _read(task_or_file)
    if not task_or_file.is_dir():
        return ""
    parts: list[str] = []
    for name in (
        "sign-in-handoff.md",
        "signin-handoff.md",
        "handoff.md",
        "signin.md",
        "dispatch.md",
        "steal-dispatch.md",
        "swarm.md",
        "swarm-emulate.md",
        "roster.md",
        "consent.md",
        "ledger.md",
        "claims.md",
        "claim-ledger.md",
        "DONE.md",
        "done.md",
        "admission.md",
        "quarantine.md",
        "synthesis.md",
        "meta.md",
    ):
        p = task_or_file / name
        if p.is_file():
            parts.append(_read(p))
    return "\n".join(parts)


def _iter_run_agents(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for base_name in (".emperor/runs", "runs"):
        base = root / base_name
        if not base.is_dir():
            continue
        for path in base.rglob("out.txt"):
            agent_dir = path.parent
            if agent_dir not in candidates:
                candidates.append(agent_dir)
        for path in base.rglob("prompt.md"):
            agent_dir = path.parent
            if agent_dir not in candidates:
                candidates.append(agent_dir)
    if (root / "out.txt").is_file() or (root / "prompt.md").is_file():
        candidates.append(root)
    if root.is_dir() and not candidates:
        for child in root.iterdir():
            if child.is_dir() and (
                (child / "out.txt").is_file() or (child / "prompt.md").is_file()
            ):
                candidates.append(child)
    return candidates


def _swarm_dirs(root: Path) -> list[Path]:
    found: list[Path] = []
    swarm_re = re.compile(r"(?i)^swarm-(\d+)$")
    for base_name in (".emperor/runs", "runs"):
        base = root / base_name
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if path.is_dir() and swarm_re.match(path.name):
                found.append(path)
    if root.is_dir():
        for child in root.iterdir():
            if child.is_dir() and swarm_re.match(child.name):
                found.append(child)
    seen: set[Path] = set()
    out: list[Path] = []
    for p in found:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def _swarm_cap(text: str) -> int:
    """Hard cap from env or default — claimed N never widens the gate."""
    env = os.environ.get("EMPEROR_SWARM_N")
    if env is not None and env.strip().isdigit():
        return int(env.strip())
    return DEFAULT_SWARM_N


def _dedupe(errors: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def _has_signin_signal(path: Path, text: str) -> bool:
    if path.is_file() and path.name.lower() in _SIGNIN_NAMES:
        return True
    if path.is_dir():
        for n in _SIGNIN_NAMES:
            if (path / n).is_file():
                return True
    return bool(_SIGNIN_SIGNAL.search(text))


def _signin_errors(text: str) -> list[str]:
    errors: list[str] = []
    if not _HANDOFF.search(text):
        errors.append(
            "missing SIGN-IN HANDOFF record "
            f"(need 'SIGN-IN HANDOFF: <agent> — client completed …; "
            f"verified: …' — see {LEAF_SIGNIN})"
        )
        return errors
    if not _AGENT_IN_HANDOFF.search(text):
        errors.append(
            "SIGN-IN HANDOFF missing agent name "
            f"(need agent after SIGN-IN HANDOFF: — see {LEAF_SIGNIN})"
        )
    if not _CLIENT_DONE.search(text):
        errors.append(
            "SIGN-IN HANDOFF missing client-completed "
            "(need 'client completed' / client ran / their terminal — "
            f"see {LEAF_SIGNIN})"
        )
    if not _VERIFIED.search(text):
        errors.append(
            "SIGN-IN HANDOFF missing status verification "
            "(need verified: / status cmd / exit 0 / AVAILABLE (verified — "
            f"see {LEAF_SIGNIN})"
        )
    for m in re.finditer(r"(?is)SIGN[- ]IN\s+HANDOFF\s*:.{0,800}", text):
        if _CREDENTIAL_SHAPE.search(m.group(0)):
            errors.append(
                "SIGN-IN HANDOFF contains credential/token-shaped material "
                "(summary only — never API keys / bearer / password= — "
                f"see {LEAF_SIGNIN})"
            )
            break
    return errors


def validate_signin(path: Path) -> list[str]:
    if not path.exists():
        return [f"missing path: {path}"]
    text = _combined_text(path)
    active = _has_signin_signal(path, text)
    if not active:
        if path.is_file() and path.name.lower() in _SIGNIN_NAMES:
            return _signin_errors(text)
        return []
    return _dedupe(_signin_errors(text))


def _has_dispatch_signal(path: Path, text: str, agents: list[Path]) -> bool:
    if path.is_file() and path.name.lower() in _DISPATCH_NAMES:
        return True
    if path.is_dir():
        for n in ("dispatch.md", "steal-dispatch.md"):
            if (path / n).is_file():
                return True
        if (path / ".emperor" / "runs").is_dir() or (path / "runs").is_dir():
            return True
    if agents:
        return True
    return bool(_DISPATCH_SIGNAL.search(text))


def _layout_errors_for_agent(agent: Path) -> list[str]:
    errors: list[str] = []
    for req in ("prompt.md", "out.txt", "meta.md"):
        if not (agent / req).is_file():
            errors.append(
                f"missing {req} under {agent} "
                f"(need .emperor/runs/<task>/<agent>/{{prompt,out,meta}} — "
                f"see {LEAF_DISPATCH})"
            )
    prompt = agent / "prompt.md"
    if prompt.is_file():
        ptxt = _read(prompt)
        if not _OBJECTIVE.search(ptxt):
            errors.append(
                f"prompt.md missing OBJECTIVE: in {agent} "
                f"(soft theater — see {LEAF_DISPATCH})"
            )
        if not _SCOPE.search(ptxt):
            errors.append(
                f"prompt.md missing SCOPE: in {agent} "
                f"(soft theater — see {LEAF_DISPATCH})"
            )
    meta = agent / "meta.md"
    if meta.is_file():
        mtxt = _read(meta)
        if not _EXIT_OR_TIMEOUT.search(mtxt):
            errors.append(
                f"meta.md missing exit/timeout signal in {agent} "
                f"(see {LEAF_DISPATCH})"
            )
    return errors


def _dispatch_text_layout_errors(text: str) -> list[str]:
    errors: list[str] = []
    # Require positive layout claim — "No .emperor/runs" prose is not evidence.
    has_layout = bool(
        re.search(
            r"(?i)(?:Runs\s+layout\s*:|\.emperor/runs/[\w./\-]+|runs/[\w./\-]+/prompt\.md)",
            text,
        )
    )
    if not has_layout:
        errors.append(
            "missing runs layout mention "
            f"(.emperor/runs/<task>/<agent>/{{prompt.md,out.txt,meta.md}} — "
            f"see {LEAF_DISPATCH})"
        )
    if not _OBJECTIVE.search(text):
        errors.append(
            f"dispatch claim missing OBJECTIVE evidence — see {LEAF_DISPATCH}"
        )
    if not _SCOPE.search(text):
        errors.append(
            f"dispatch claim missing SCOPE evidence — see {LEAF_DISPATCH}"
        )
    return errors


def validate_dispatch(path: Path) -> list[str]:
    if not path.exists():
        return [f"missing path: {path}"]
    text = _combined_text(path)
    # File fixtures: text-only (do not inherit sibling task runs under fixtures/).
    agents = _iter_run_agents(path) if path.is_dir() else []
    active = _has_dispatch_signal(path, text, agents)
    if not active:
        if path.is_file() and path.name.lower() in _DISPATCH_NAMES:
            return _dispatch_text_layout_errors(text)
        return []
    errors: list[str] = []
    if agents:
        for a in agents:
            errors.extend(_layout_errors_for_agent(a))
    else:
        errors.extend(_dispatch_text_layout_errors(text))
    return _dedupe(errors)


def _has_swarm_signal(path: Path, text: str, swarm_dirs: list[Path]) -> bool:
    if path.is_file() and path.name.lower() in {"swarm.md", "swarm-emulate.md"}:
        return True
    if path.is_dir():
        for n in ("swarm.md", "swarm-emulate.md"):
            if (path / n).is_file():
                return True
    if swarm_dirs:
        return True
    return bool(_SWARM_SIGNAL.search(text))


def _swarm_errors(path: Path, text: str, swarm_dirs: list[Path]) -> list[str]:
    errors: list[str] = []
    cap = _swarm_cap(text)
    n_claimed = None
    m = _BOUND_N.search(text)
    if m:
        for g in m.groups():
            if g is not None and str(g).isdigit():
                n_claimed = int(g)
                break
    n_dirs = len(swarm_dirs)
    n = n_claimed if n_claimed is not None else (n_dirs if n_dirs else None)

    if n is not None and n > cap:
        errors.append(
            f"unbounded swarm N={n} exceeds cap {cap} "
            f"(default 4 / EMPEROR_SWARM_N — see {LEAF_SWARM})"
        )
    if n_dirs > cap:
        errors.append(
            f"swarm run dirs ({n_dirs}) exceed cap {cap} "
            f"(see {LEAF_SWARM})"
        )
    if n is None and n_dirs == 0:
        if "EMPEROR_SWARM_N" not in text and not re.search(
            r"(?i)\bbound\s+N\b|\bN\s*=\s*\d+", text
        ):
            errors.append(
                "swarm activity missing bound N (default 4 / EMPEROR_SWARM_N — "
                f"see {LEAF_SWARM})"
            )
    if not _DISJOINT.search(text):
        scopes: list[str] = []
        for d in swarm_dirs:
            prompt = d / "prompt.md"
            if prompt.is_file():
                for line in _read(prompt).splitlines():
                    if re.match(r"(?i)^\s*SCOPE\s*:", line):
                        scopes.append(line.strip().lower())
        if len(scopes) >= 2 and len(set(scopes)) == len(scopes):
            pass
        elif len(scopes) >= 2 and len(set(scopes)) < len(scopes):
            errors.append(
                f"swarm SCOPE lists overlap (not disjoint — see {LEAF_SWARM})"
            )
        else:
            errors.append(
                "missing disjoint SCOPE evidence "
                f"(disjoint SCOPE / non-overlapping scopes — see {LEAF_SWARM})"
            )
    if n_dirs == 0 and not re.search(r"(?i)swarm-\d+", text):
        errors.append(
            "missing swarm-<n> run dirs / numbered collect layout "
            f"(see {LEAF_SWARM})"
        )
    if not _SYNTHESIS.search(text):
        syn = False
        if path.is_dir() and (path / "synthesis.md").is_file():
            syn = True
        if path.is_file() and path.name.lower() == "synthesis.md":
            syn = True
        if not syn:
            errors.append(
                "missing synthesis note "
                f"(orchestrator synthesizes; workers do not merge — "
                f"see {LEAF_SWARM})"
            )
    return errors


def validate_swarm(path: Path) -> list[str]:
    if not path.exists():
        return [f"missing path: {path}"]
    text = _combined_text(path)
    # File fixtures: text-only (do not inherit sibling swarm-* dirs).
    swarm_dirs = _swarm_dirs(path) if path.is_dir() else []
    active = _has_swarm_signal(path, text, swarm_dirs)
    if not active:
        if path.is_file() and path.name.lower() in {
            "swarm.md",
            "swarm-emulate.md",
        }:
            return _swarm_errors(path, text, swarm_dirs)
        return []
    return _dedupe(_swarm_errors(path, text, swarm_dirs))


def validate_all(path: Path) -> list[str]:
    return _dedupe(
        validate_signin(path) + validate_dispatch(path) + validate_swarm(path)
    )


def format_card() -> str:
    lines = [
        "STEAL-FLOW checklist=yes",
        f"STEAL-FLOW leaf-signin={LEAF_SIGNIN}",
        f"STEAL-FLOW leaf-dispatch={LEAF_DISPATCH}",
        f"STEAL-FLOW leaf-swarm={LEAF_SWARM}",
        "STEAL-FLOW iron=SIGNIN_THEN_DISPATCH_THEN_BOUNDED_SWARM",
        "STEP 1 id=signin name=Client login handoff "
        "et=SIGN-IN HANDOFF: agent — client completed; verified status",
        "STEP 1 key=Never credentials/tokens; summary only",
        "STEP 2 id=dispatch name=Runs layout + prompt anatomy "
        "et=.emperor/runs/<task>/<agent>/{prompt.md,out.txt,meta.md}",
        "STEP 2 key=OBJECTIVE + SCOPE required; timeout in meta",
        "STEP 3 id=swarm name=Bound N + disjoint SCOPE + synthesize "
        "et=default N=4 / EMPEROR_SWARM_N; collect swarm-<n>/; one retry",
        "STEP 3 key=HARD-GATE --reject-no-signin / "
        "--reject-no-dispatch-layout / --reject-unbounded-swarm",
        "",
        "MUST: Before claiming steal sign-in/dispatch/swarm done, satisfy the "
        "matching HARD-GATE. Open the leaf; run scripts/emperor steal-flow "
        "<task-dir> (aliases: sign-in-handoff, steal-dispatch, swarm-emulate).",
        "MUST-NOT: silent agent login; credential material in handoff; "
        "dispatch without runs layout / OBJECTIVE+SCOPE; unbounded swarm; "
        "overlapping writable SCOPE; worker merges siblings.",
    ]
    return "\n".join(lines) + "\n"


def reject_no_signin() -> str:
    return (
        "REJECT NO SIGNIN: HARD-GATE — Steal refuses NEEDS-SIGN-IN → AVAILABLE "
        "without SIGN-IN HANDOFF (agent + client completed + verified status; "
        f"no credential/token material). Open {LEAF_SIGNIN}; re-run "
        "scripts/emperor steal-flow --check-signin <task-dir>.\n"
    )


def reject_no_dispatch_layout() -> str:
    return (
        "REJECT NO DISPATCH LAYOUT: HARD-GATE — Steal refuses worker dispatch "
        "without .emperor/runs/<task>/<agent>/{prompt.md,out.txt,meta.md} "
        f"(OBJECTIVE + SCOPE in prompt; exit/timeout in meta). Open "
        f"{LEAF_DISPATCH}; re-run scripts/emperor steal-flow "
        "--check-dispatch <task-dir>.\n"
    )


def reject_unbounded_swarm() -> str:
    return (
        "REJECT UNBOUNDED SWARM: HARD-GATE — Steal refuses swarm without "
        f"bound N≤{DEFAULT_SWARM_N} (or EMPEROR_SWARM_N), disjoint SCOPE, and "
        f"swarm-<n> collect / synthesis. Open {LEAF_SWARM}; re-run "
        "scripts/emperor steal-flow --check-swarm <task-dir>.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Validate Emperor Time Steal sign-in / dispatch / swarm "
            "(HARD-GATE card + check modes)"
        )
    )
    p.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=None,
        help="task dir / ledger (omit to print STEAL-FLOW card; runs all checks)",
    )
    p.add_argument(
        "--check-signin",
        type=Path,
        metavar="PATH",
        default=None,
        help="sign-in handoff check (exit 1 on soft/missing handoff)",
    )
    p.add_argument(
        "--check-dispatch",
        type=Path,
        metavar="PATH",
        default=None,
        help="dispatch layout check (exit 1 on soft/missing layout)",
    )
    p.add_argument(
        "--check-swarm",
        type=Path,
        metavar="PATH",
        default=None,
        help="swarm bound/disjoint/synthesis check (exit 1 on soft/unbounded)",
    )
    p.add_argument(
        "--reject-no-signin",
        action="store_true",
        help="Hard-gate: refuse missing SIGN-IN HANDOFF (exit 1)",
    )
    p.add_argument(
        "--reject-no-dispatch-layout",
        action="store_true",
        help="Hard-gate: refuse missing dispatch runs layout (exit 1)",
    )
    p.add_argument(
        "--reject-unbounded-swarm",
        action="store_true",
        help="Hard-gate: refuse unbounded / overlapping swarm (exit 1)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    if args.reject_no_signin:
        sys.stdout.write(reject_no_signin())
        return 1
    if args.reject_no_dispatch_layout:
        sys.stdout.write(reject_no_dispatch_layout())
        return 1
    if args.reject_unbounded_swarm:
        sys.stdout.write(reject_unbounded_swarm())
        return 1

    if args.check_signin is not None:
        errs = validate_signin(args.check_signin)
        label = "signin"
        target = args.check_signin
    elif args.check_dispatch is not None:
        errs = validate_dispatch(args.check_dispatch)
        label = "dispatch"
        target = args.check_dispatch
    elif args.check_swarm is not None:
        errs = validate_swarm(args.check_swarm)
        label = "swarm"
        target = args.check_swarm
    elif args.path is not None:
        errs = validate_all(args.path)
        label = "steal-flow"
        target = args.path
    else:
        sys.stdout.write(format_card())
        return 0

    if errs:
        for e in errs:
            print(f"{label} FAIL: {e}", file=sys.stderr)
        return 1
    print(f"{label} PASS: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
