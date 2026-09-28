#!/usr/bin/env python3
"""Append-only thoughttrail — reasoning entries linked to graph nodes.

Layout: .emperor/thoughttrail/trail.jsonl
Each line is one JSON object:
  id, ts, text, node_ids[], ledger, task

No embeddings. Stdlib only.
"""
from __future__ import annotations

import hashlib
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def default_trail_path(repo_root: Path) -> Path:
    return repo_root / ".emperor" / "thoughttrail" / "trail.jsonl"


def ensure_layout(repo_root: Path) -> dict[str, Path]:
    """Create inverted-workspace dirs (context/thoughttrail/sot/artifacts/sandbox)."""
    root = repo_root / ".emperor"
    paths = {
        "context": root / "context",
        "thoughttrail": root / "thoughttrail",
        "sot": root / "sot",
        "sot_plugins": root / "sot" / "plugins",
        "artifacts": root / "artifacts",
        "sandbox": root / "sandbox",
        "runtime": root / "sandbox" / "runtime",
        "runtime_compose": root / "sandbox" / "runtime" / "compose",
        "runtime_podman": root / "sandbox" / "runtime" / "podman",
        "runtime_k8s": root / "sandbox" / "runtime" / "k8s",
        "env": root / "env",
        "secrets": root / "secrets",
    }
    for p in paths.values():
        p.mkdir(parents=True, exist_ok=True)
    # SOT pointer stub (fetch-only mirror doctrine; multi-repo plugins)
    pointer = paths["sot"] / "POINTER.md"
    if not pointer.exists():
        pointer.write_text(
            "\n".join(
                [
                    "# SOT — source of truth (fetch-only mirrors)",
                    "",
                    "Emperor Time inverted workspace (virtual context = host-max):",
                    "- Workspace ≠ one repo. A task may bind multiple repos that",
                    "  work together; each bound repo is a *plugin* under",
                    "  `.emperor/sot/plugins/<repo>/` (fetch-only).",
                    "- Primary SOT = copy of `origin/main` kept current for",
                    "  context + regression reference. Do **not** mutate SOT.",
                    "- Regression runs from *copies* under `.emperor/artifacts/`,",
                    "  never by checking out over the SOT.",
                    "- Live checkout of main is not the only workspace; ET owns",
                    "  the workspace model.",
                    "",
                    "CLI: `emperor sot sync|add-plugin` (v1 stub).",
                    "",
                    "```yaml",
                    "remote: origin",
                    "ref: main",
                    "mirror_path:  # e.g. .emperor/sot/main-mirror (optional)",
                    "fetch_only: true",
                    "plugins: []  # filled by sot add-plugin",
                    "```",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    plugins_readme = paths["sot_plugins"] / "README.md"
    if not plugins_readme.exists():
        plugins_readme.write_text(
            "\n".join(
                [
                    "# SOT plugins — fetch-only bound repos",
                    "",
                    "Each subdirectory is a fetch-only mirror of a repo bound to",
                    "the workspace. The sandbox engine recognizes these as",
                    "plugins when composing stacks.",
                    "",
                    "Add via: `emperor sot add-plugin <name> <git-url>` (stub).",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    readme = paths["artifacts"] / "README.md"
    if not readme.exists():
        readme.write_text(
            "\n".join(
                [
                    "# Artifacts — parallel multi-repo PR workspaces",
                    "",
                    "Each `<id>/` holds workspace copies (multi-repo worktrees)",
                    "+ optional `compose.yml` generated so plugin repos fire",
                    "together. Job: fully SDLC-tested PRs. Not the SOT.",
                    "",
                    "CLI: `emperor context artifacts list|stub-create`",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    sandbox_readme = paths["sandbox"] / "README.md"
    if not sandbox_readme.exists():
        sandbox_readme.write_text(
            "\n".join(
                [
                    "# Sandbox — ports, mocks, sims, isolation",
                    "",
                    "Powers: sandboxing, mocking, simulating, isolating,",
                    "parallel testing. Ports allocated per artifact; stacks",
                    "raised per artifact. Simulator emits docker-compose (or",
                    "equivalent) wiring SOT plugins together.",
                    "",
                    "Files (v1 stubs):",
                    "- `ports.json` — allocated host ports per artifact",
                    "- `manifest.json` — mock/sim declarations",
                    "",
                    "CLI: `emperor sandbox plan|up|down|ports`",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    ports = paths["sandbox"] / "ports.json"
    if not ports.exists():
        ports.write_text('{"next_base": 18000, "allocations": {}}\n', encoding="utf-8")
    manifest = paths["sandbox"] / "manifest.json"
    if not manifest.exists():
        manifest.write_text(
            '{"mocks": [], "sims": [], "isolate": true}\n', encoding="utf-8"
        )

    # Pluggable runtimes (compose | podman | k8s)
    for rt_name, rt_path in (
        ("compose", paths["runtime_compose"]),
        ("podman", paths["runtime_podman"]),
        ("k8s", paths["runtime_k8s"]),
    ):
        readme = rt_path / "README.md"
        if not readme.exists():
            readme.write_text(
                f"# Runtime backend: {rt_name}\n\n"
                "Pluggable sandbox emitter. `emperor runtime use` selects active.\n"
                "Compose is not the only emitter — podman and k8s are peers.\n",
                encoding="utf-8",
            )
    active = paths["runtime"] / "active"
    if not active.exists():
        active.write_text("compose\n", encoding="utf-8")

    # Unified workspace env (repo≠workspace; ET merges across plugins)
    env_ex = paths["env"] / "workspace.env.example"
    if not env_ex.exists():
        env_ex.write_text(
            "\n".join(
                [
                    "# Workspace-level env example (NO secrets).",
                    "# ET owns merge/override across SOT plugins for an artifact.",
                    "# Classical per-repo dotenv is insufficient when workspace≠repo.",
                    "ET_WORKSPACE_ID=",
                    "ET_ARTIFACT_ID=",
                    "ET_RUNTIME=compose",
                    "# Plugin public config only — secrets via .emperor/secrets broker",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    overlays = paths["env"] / "overlays"
    overlays.mkdir(parents=True, exist_ok=True)
    og = overlays / "README.md"
    if not og.exists():
        og.write_text(
            "# Managed env overlays (no secrets in git)\n\n"
            "Per-artifact / per-plugin overlays merged by `emperor env sync`.\n"
            "Values that are secrets MUST come from the secrets broker, not here.\n",
            encoding="utf-8",
        )
    gitignore_env = paths["env"] / ".gitignore"
    if not gitignore_env.exists():
        gitignore_env.write_text(
            "workspace.env\n*.local.env\noverlays/*.env\n!.gitignore\n!workspace.env.example\n!overlays/README.md\n",
            encoding="utf-8",
        )

    # Blind credentials — names only in manifest; inject via broker
    sec_manifest = paths["secrets"] / "manifest.json"
    if not sec_manifest.exists():
        sec_manifest.write_text(
            '{\n  "broker": "env-file",\n  "names": [],\n'
            '  "note": "Agent sees names/status only — never plaintext values"\n}\n',
            encoding="utf-8",
        )
    sec_readme = paths["secrets"] / "README.md"
    if not sec_readme.exists():
        sec_readme.write_text(
            "\n".join(
                [
                    "# Blind credentials",
                    "",
                    "Unified way to obtain/inject secrets into workspace/stacks",
                    "WITHOUT the LLM seeing values (vault / 1Password / env-file",
                    "broker). Agent only sees names + status, never plaintext.",
                    "",
                    "CLI: `emperor secrets list|inject` — inject must not print values.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    gitignore_sec = paths["secrets"] / ".gitignore"
    if not gitignore_sec.exists():
        gitignore_sec.write_text(
            "*.env\n*.pem\n*.key\nvalues/\n!.gitignore\n!manifest.json\n!README.md\n",
            encoding="utf-8",
        )

    trail = default_trail_path(repo_root)
    if not trail.exists():
        trail.write_text("", encoding="utf-8")
    return paths


def append_entry(
    repo_root: Path,
    text: str,
    *,
    node_ids: Sequence[str] | None = None,
    ledger: str = "",
    task: str = "",
    trail_path: Path | None = None,
) -> dict:
    ensure_layout(repo_root)
    path = trail_path or default_trail_path(repo_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "id": uuid.uuid4().hex[:12],
        "ts": _utc(),
        "text": text.strip(),
        "node_ids": list(node_ids or []),
        "ledger": ledger,
        "task": task,
    }
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


def list_entries(
    repo_root: Path,
    *,
    limit: int = 20,
    trail_path: Path | None = None,
    node_id: str = "",
) -> list[dict]:
    path = trail_path or default_trail_path(repo_root)
    if not path.is_file():
        return []
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if node_id and node_id not in (obj.get("node_ids") or []):
            continue
        rows.append(obj)
    return rows[-limit:]


def link_nodes(
    repo_root: Path,
    entry_id: str,
    node_ids: Sequence[str],
    *,
    trail_path: Path | None = None,
) -> dict | None:
    """Rewrite trail.jsonl adding node_ids to an existing entry (append-safe copy)."""
    path = trail_path or default_trail_path(repo_root)
    if not path.is_file():
        return None
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    updated = None
    out_lines: list[str] = []
    for line in lines:
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            out_lines.append(line)
            continue
        if obj.get("id") == entry_id:
            ids = list(obj.get("node_ids") or [])
            for n in node_ids:
                if n not in ids:
                    ids.append(n)
            obj["node_ids"] = ids
            updated = obj
            out_lines.append(json.dumps(obj, ensure_ascii=False))
        else:
            out_lines.append(json.dumps(obj, ensure_ascii=False))
    if updated is None:
        return None
    path.write_text("\n".join(out_lines) + ("\n" if out_lines else ""), encoding="utf-8")
    return updated


__all__ = [
    "append_entry",
    "list_entries",
    "link_nodes",
    "ensure_layout",
    "default_trail_path",
]
