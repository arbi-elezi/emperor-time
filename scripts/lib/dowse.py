#!/usr/bin/env python3
"""Dowsing Chain Mode 2 — machine agent scan (Python core).

READ-ONLY (Vow of Consent): detects binaries on PATH and probes --version.
Never installs, never logs in, never reads credential/config files.
Auth probes run ONLY with --check-auth, using whitelisted harmless status cmds.

Closes bash↔ps1 twin drift: dowse.ps1 had -AsJson + richer roster metadata
(Binary, Headless, SignIn) while dowse.sh was table-only (no JSON).

Thin twins: scripts/dowse.sh / scripts/dowse.ps1
CLI: dowse.py [--check-auth] [--skip-versions] [--as-json]
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class AgentDef:
    name: str
    binary: str
    core: bool
    auth_cmd: tuple[str, ...] | None  # None => no safe status cmd
    headless: str
    login: str


# Roster mirrors references/agent-registry.md + prior ps1 metadata.
AGENTS: tuple[AgentDef, ...] = (
    AgentDef(
        "Claude Code",
        "claude",
        True,
        None,
        'claude -p "<prompt>" --output-format json',
        "run `claude` interactively (first-run login)",
    ),
    AgentDef(
        "Kimi CLI",
        "kimi",
        True,
        None,
        "no documented print flag - check `kimi --help`; kimi-agent-sdk; `kimi acp`",
        "run `kimi`, then /login",
    ),
    AgentDef(
        "Codex CLI",
        "codex",
        True,
        ("login", "status"),
        'codex exec "<prompt>"',
        "codex login  (headless: codex login --device-auth)",
    ),
    AgentDef(
        "Copilot CLI",
        "copilot",
        True,
        None,
        'copilot -p "<prompt>" -s --no-ask-user',
        "see `copilot --help` login flow",
    ),
    AgentDef(
        "opencode",
        "opencode",
        True,
        None,
        'opencode run "<prompt>"',
        "see `opencode --help` / auth subcommand",
    ),
    AgentDef(
        "Grok Build",
        "grok",
        True,
        None,
        'grok -p "<prompt>"  (verify; ACP: grok agent stdio — see adapters/grok/)',
        "grok login or XAI_API_KEY (client sets; orchestrator never logs in)",
    ),
    AgentDef(
        "Ollama",
        "ollama",
        True,
        ("list",),
        'ollama run <model> "<prompt>"',
        "none (local); daemon must be running",
    ),
    AgentDef(
        "GitHub CLI",
        "gh",
        False,
        ("auth", "status"),
        "(adjacent tooling, not an agent)",
        "gh auth login",
    ),
    AgentDef(
        "Aider",
        "aider",
        False,
        None,
        "verify at dowse: aider --help",
        "API key env vars (client sets)",
    ),
    AgentDef(
        "Gemini CLI",
        "gemini",
        False,
        None,
        "verify at dowse: gemini --help",
        "see `gemini --help`",
    ),
    AgentDef(
        "Goose",
        "goose",
        False,
        None,
        "verify at dowse: goose --help",
        "see `goose --help`",
    ),
    AgentDef(
        "Qwen Code",
        "qwen",
        False,
        None,
        "verify at dowse: qwen --help",
        "see `qwen --help`",
    ),
)


def _probe_timeout() -> float:
    raw = os.environ.get("EMPEROR_PROBE_TIMEOUT", "8")
    try:
        return float(raw)
    except ValueError:
        return 8.0


def _run_bounded(argv: list[str], timeout: float) -> tuple[int | None, str]:
    """Run argv; return (exit_code_or_None_on_timeout, first_line_combined)."""
    try:
        proc = subprocess.run(
            argv,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError:
        return 127, ""
    except subprocess.TimeoutExpired as exc:
        out = ""
        if exc.stdout:
            out = exc.stdout if isinstance(exc.stdout, str) else exc.stdout.decode(
                "utf-8", errors="replace"
            )
        elif exc.stderr:
            out = exc.stderr if isinstance(exc.stderr, str) else exc.stderr.decode(
                "utf-8", errors="replace"
            )
        first = out.splitlines()[0] if out else ""
        return None, first
    combined = (proc.stdout or "") + (proc.stderr or "")
    first = combined.splitlines()[0] if combined else ""
    return proc.returncode, first


def scan_agent(
    agent: AgentDef,
    *,
    check_auth: bool,
    skip_versions: bool,
    timeout: float,
) -> dict[str, Any]:
    entry: dict[str, Any] = {
        "Agent": agent.name,
        "Binary": agent.binary,
        "Status": "NOT INSTALLED",
        "Version": "",
        "Auth": "unchecked",
        "Headless": agent.headless,
        "SignIn": agent.login,
    }
    if shutil.which(agent.binary) is None:
        return entry

    entry["Status"] = "DETECTED"
    if not skip_versions:
        code, first = _run_bounded([agent.binary, "--version"], timeout)
        if code is None:
            entry["Version"] = f"(version probe hung >{int(timeout)}s)"
        elif first:
            entry["Version"] = first
        else:
            entry["Version"] = "(no version output)"

    if check_auth:
        if agent.auth_cmd is None:
            entry["Auth"] = (
                f"no safe status cmd known - verify via `{agent.binary} --help`"
            )
        else:
            code, first = _run_bounded(
                [agent.binary, *agent.auth_cmd], timeout
            )
            if code is None:
                entry["Auth"] = (
                    f"TIMEOUT after {int(timeout)}s (daemon down or cmd hung)"
                )
            elif code == 0:
                entry["Auth"] = f"OK: {first}" if first else "OK"
            else:
                entry["Auth"] = f"NEEDS SIGN-IN (status cmd exit {code})"

    return entry


def scan_roster(
    *,
    check_auth: bool = False,
    skip_versions: bool = False,
    timeout: float | None = None,
) -> list[dict[str, Any]]:
    t = _probe_timeout() if timeout is None else timeout
    return [
        scan_agent(
            a,
            check_auth=check_auth,
            skip_versions=skip_versions,
            timeout=t,
        )
        for a in AGENTS
    ]


def _format_table(roster: list[dict[str, Any]]) -> str:
    lines: list[str] = [
        "",
        "=== EMPEROR TIME :: DOWSING CHAIN :: machine scan ===",
        "(read-only: no installs, no logins, no credential access)",
        "",
        f"{'AGENT':<14} {'STATUS':<15} {'VERSION':<28} {'AUTH'}",
        f"{'-----':<14} {'------':<15} {'-------':<28} {'----'}",
    ]
    detected = 0
    for e in roster:
        if e["Status"] == "DETECTED":
            detected += 1
        ver = (e.get("Version") or "")[:28]
        lines.append(
            f"{e['Agent']:<14} {e['Status']:<15} {ver:<28} {e['Auth']}"
        )
    lines.extend(
        [
            "",
            f"Detected: {detected} agent(s).",
            "",
            "Next steps (Steal Chain protocol):",
            "  1. Verify each invocation syntax against reality:  <binary> --help",
            "  2. Agents needing sign-in: the CLIENT logs in, in a NEW terminal they",
            "     open themselves (never the orchestrator's shell).",
            "  3. Re-run with --check-auth to confirm via harmless status commands only.",
            "  4. Hand the roster to chains/steal-chain/SKILL.md for consent + dispatch.",
            "  Tip: --as-json emits Binary/Headless/SignIn for orchestrators.",
            "",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Dowsing Chain Mode 2 — read-only agent scan (Python core)",
    )
    ap.add_argument(
        "--check-auth",
        action="store_true",
        help="run whitelisted harmless auth status probes",
    )
    ap.add_argument(
        "--skip-versions",
        action="store_true",
        help="skip --version probes",
    )
    ap.add_argument(
        "--as-json",
        action="store_true",
        help="emit richer JSON roster (Agent/Binary/Status/Version/Auth/Headless/SignIn)",
    )
    args = ap.parse_args(list(sys.argv[1:] if argv is None else argv))

    roster = scan_roster(
        check_auth=args.check_auth,
        skip_versions=args.skip_versions,
    )
    if args.as_json:
        print(json.dumps(roster, indent=2, ensure_ascii=False))
    else:
        sys.stdout.write(_format_table(roster))
    return 0


if __name__ == "__main__":
    sys.exit(main())
