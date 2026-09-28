#!/usr/bin/env python3
"""Emperor Time unified workspace env — merge overlays; redacted show.

Real in v0.4.136+ (deepens stubs from super_context v0.4.133):

1. `env show` — merge view across workspace.env + overlays + SOT plugin
   fragments; values ALWAYS redacted on stdout.
2. `env sync [--artifact ID]` — write managed overlay
   `.emperor/env/overlays/<artifact>.managed.env` without echoing secrets.
   Secret keys stay as placeholders; values come from secrets broker inject.
3. Repo ≠ workspace — ET owns merge/override across plugins for an artifact.

No embeddings. No Graphify. Stdlib only.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

import thoughttrail as trail

LEAF = "references/super-context.md"
IRON = "ENV_REDACTED"

_SECRET_KEY = re.compile(
    r"(?i)(SECRET|PASSWORD|TOKEN|API[_-]?KEY|PRIVATE[_-]?KEY|CREDENTIAL|PASSWD|AUTH)"
)
_REDACT = "***REDACTED***"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resolve_root(args: Any) -> Path:
    root = getattr(args, "root", None) or ""
    if root:
        return Path(root).resolve()
    cur = Path.cwd().resolve()
    for p in [cur, *cur.parents]:
        if (p / ".git").exists() or (p / "SKILL.md").exists():
            return p
    return cur


def env_dir(root: Path) -> Path:
    return root / ".emperor" / "env"


def parse_env_text(raw: str) -> list[tuple[str, str, str]]:
    """Return list of (kind, key, value) where kind is 'kv'|'comment'|'blank'."""
    rows: list[tuple[str, str, str]] = []
    for line in raw.splitlines():
        s = line.strip()
        if not s:
            rows.append(("blank", "", ""))
            continue
        if s.startswith("#"):
            rows.append(("comment", "", line))
            continue
        if "=" in line:
            k, _, v = line.partition("=")
            rows.append(("kv", k.strip(), v))
        else:
            rows.append(("comment", "", line))
    return rows


def is_secret_key(key: str) -> bool:
    return bool(_SECRET_KEY.search(key))


def redact_value(key: str, value: str) -> str:
    if is_secret_key(key):
        return _REDACT
    # Also redact non-empty values that look like they might be secrets
    # when key is ET_*_SECRET etc. — already covered. For public keys,
    # show value (workspace public config).
    return value


def redact_env_lines(raw: str) -> list[str]:
    out: list[str] = []
    for kind, key, val in parse_env_text(raw):
        if kind == "blank":
            out.append("")
        elif kind == "comment":
            out.append(val if val else "")
        else:
            out.append(f"{key}={redact_value(key, val)}")
    return out


def load_kv_file(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    out: dict[str, str] = {}
    for kind, key, val in parse_env_text(path.read_text(encoding="utf-8", errors="replace")):
        if kind == "kv" and key:
            out[key] = val
    return out


def plugin_env_fragments(root: Path) -> list[tuple[str, Path]]:
    """SOT plugin public env fragments (env.fragment / env.example)."""
    plugins = root / ".emperor" / "sot" / "plugins"
    found: list[tuple[str, Path]] = []
    if not plugins.is_dir():
        return found
    for pdir in sorted(plugins.iterdir()):
        if not pdir.is_dir():
            continue
        for name in ("env.fragment", "env.example", "workspace.env.example"):
            cand = pdir / name
            if cand.is_file():
                found.append((pdir.name, cand))
                break
    return found


def collect_layers(root: Path, artifact_id: str = "") -> list[tuple[str, Path, dict[str, str]]]:
    """Ordered layers (low → high precedence) for merge."""
    trail.ensure_layout(root)
    ed = env_dir(root)
    layers: list[tuple[str, Path, dict[str, str]]] = []
    example = ed / "workspace.env.example"
    if example.is_file():
        layers.append(("example", example, load_kv_file(example)))
    managed_ws = ed / "workspace.env"
    if managed_ws.is_file():
        layers.append(("workspace", managed_ws, load_kv_file(managed_ws)))
    overlays = ed / "overlays"
    if overlays.is_dir():
        for ov in sorted(overlays.glob("*.env")):
            # skip writing target mid-sync if present
            layers.append((f"overlay:{ov.name}", ov, load_kv_file(ov)))
    for pname, frag in plugin_env_fragments(root):
        layers.append((f"plugin:{pname}", frag, load_kv_file(frag)))
    if artifact_id:
        art_env = root / ".emperor" / "artifacts" / artifact_id / "env.public"
        if art_env.is_file():
            layers.append((f"artifact:{artifact_id}", art_env, load_kv_file(art_env)))
    return layers


def merge_layers(layers: list[tuple[str, Path, dict[str, str]]]) -> dict[str, str]:
    merged: dict[str, str] = {}
    for _label, _path, kv in layers:
        merged.update(kv)
    return merged


def show_env(root: Path, *, artifact_id: str = "") -> list[str]:
    """Return redacted display lines for env show."""
    layers = collect_layers(root, artifact_id)
    lines: list[str] = [
        f"ENV show scope=workspace artifact={artifact_id or '(none)'} (redacted; repo≠workspace)",
        f"  dir={env_dir(root)}",
    ]
    for label, path, kv in layers:
        lines.append(f"  layer={label} path={path.name} keys={len(kv)}")
    merged = merge_layers(layers)
    lines.append("  --- merged (redacted) ---")
    if not merged:
        lines.append("  (empty — emperor env sync; secrets via broker)")
    else:
        for k in sorted(merged.keys()):
            lines.append(f"  {k}={redact_value(k, merged[k])}")
    return lines


def sync_env(
    root: Path,
    *,
    artifact_id: str = "default",
) -> dict[str, Any]:
    """Merge overlays → write managed overlay WITHOUT echoing secrets.

    Secret-looking keys are written as empty or ${NAME} placeholders;
    plaintext secret values are stripped (broker inject owns those).
    """
    trail.ensure_layout(root)
    ed = env_dir(root)
    overlays = ed / "overlays"
    overlays.mkdir(parents=True, exist_ok=True)
    layers = collect_layers(root, artifact_id)
    # Exclude the target managed file from layers to avoid feedback
    target = overlays / f"{artifact_id}.managed.env"
    layers = [(a, b, c) for a, b, c in layers if b.resolve() != target.resolve()]
    merged = merge_layers(layers)

    # Seed from example if nothing else
    example = ed / "workspace.env.example"
    managed_ws = ed / "workspace.env"
    created_ws = False
    if not managed_ws.exists() and example.exists():
        # copy public keys only
        kv = load_kv_file(example)
        lines = [
            f"# Managed workspace.env — generated {_utc()} (no secrets)",
            "# Secret values MUST come from `emperor secrets inject`",
        ]
        for k, v in kv.items():
            if is_secret_key(k):
                lines.append(f"{k}=")  # placeholder
            else:
                lines.append(f"{k}={v}")
        managed_ws.write_text("\n".join(lines) + "\n", encoding="utf-8")
        created_ws = True
        # re-merge including new workspace
        layers = collect_layers(root, artifact_id)
        layers = [(a, b, c) for a, b, c in layers if b.resolve() != target.resolve()]
        merged = merge_layers(layers)

    out_lines = [
        f"# Emperor Time managed overlay — artifact={artifact_id} @ {_utc()}",
        "# Generated by `emperor env sync`. DO NOT put secrets here.",
        "# Blind inject: `emperor secrets inject --artifact "
        + artifact_id
        + "`",
        f"# Layers: {', '.join(a for a, _, _ in layers) or '(none)'}",
    ]
    secret_keys = []
    public_keys = []
    for k in sorted(merged.keys()):
        v = merged[k]
        if is_secret_key(k):
            # never write plaintext secret into managed overlay
            out_lines.append(f"{k}=${{{k}}}")
            secret_keys.append(k)
        else:
            out_lines.append(f"{k}={v}")
            public_keys.append(k)
    target.write_text("\n".join(out_lines) + "\n", encoding="utf-8")

    # Also drop a public artifact pointer (no secrets)
    art_dir = root / ".emperor" / "artifacts" / artifact_id
    art_dir.mkdir(parents=True, exist_ok=True)
    pointer = art_dir / "env.managed.path"
    pointer.write_text(str(target) + "\n", encoding="utf-8")

    return {
        "artifact": artifact_id,
        "managed": str(target),
        "workspace_created": created_ws,
        "public_keys": public_keys,
        "secret_placeholders": secret_keys,
        "layers": [a for a, _, _ in layers],
        "plaintext_to_stdout": False,
    }


def cmd_show(args: argparse.Namespace) -> int:
    root = _resolve_root(args)
    artifact = getattr(args, "artifact", "") or ""
    for line in show_env(root, artifact_id=artifact):
        print(line)
    print(f"IRON: values redacted on stdout  IRON={IRON}")
    return 0


def cmd_sync(args: argparse.Namespace) -> int:
    root = _resolve_root(args)
    artifact = getattr(args, "artifact", "") or "default"
    result = sync_env(root, artifact_id=artifact)
    print(
        f"ENV sync artifact={result['artifact']} managed={result['managed']} "
        f"public={len(result['public_keys'])} "
        f"secret_placeholders={len(result['secret_placeholders'])}"
    )
    if result["workspace_created"]:
        print("ENV sync created workspace.env from example (no secrets)")
    if result["layers"]:
        print(f"ENV sync layers={','.join(result['layers'])}")
    if result["secret_placeholders"]:
        print(
            "ENV sync secret keys kept as ${NAME} placeholders — "
            "use `emperor secrets inject`"
        )
    print("NOTE: managed overlay written; secrets not echoed")
    return 0


def _print_card() -> int:
    print(
        "\n".join(
            [
                f"ENV checklist=yes leaf={LEAF}",
                "UNIFIED: workspace env merges overlays across SOT plugins",
                "CMDS: show (redacted) | sync [--artifact ID]",
                "WRITE: .emperor/env/overlays/<artifact>.managed.env (no secret plaintext)",
                f"IRON={IRON} — never echo secrets; broker owns inject",
                "GATE rule=repo-ne-workspace; no embeddings; no Graphify ports",
            ]
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument("--root", default="", help="repo root (default: detect)")
    p = argparse.ArgumentParser(
        prog="workspace_env",
        description="Emperor Time unified workspace env (redacted show / sync)",
        parents=[parent],
    )
    sub = p.add_subparsers(dest="cmd")
    sh = sub.add_parser("show", help="redacted merge view", parents=[parent])
    sh.add_argument("--artifact", default="")
    sy = sub.add_parser("sync", help="write managed overlay (no secret echo)", parents=[parent])
    sy.add_argument("--artifact", default="default")
    return p


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        return _print_card()
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.cmd:
        return _print_card()
    if args.cmd == "show":
        return cmd_show(args)
    if args.cmd == "sync":
        return cmd_sync(args)
    return _print_card()


def cmd_env_cli(args: Any) -> int:
    """Adapter from super_context argparse Namespace."""
    root = Path(args.root).resolve() if getattr(args, "root", "") else _resolve_root(args)
    action = getattr(args, "env_action", None) or getattr(args, "cmd", None)
    ns = argparse.Namespace(
        root=str(root),
        artifact=getattr(args, "artifact", "") or "",
    )
    if action == "show":
        if not ns.artifact:
            ns.artifact = ""
        return cmd_show(ns)
    if action == "sync":
        if not ns.artifact:
            ns.artifact = "default"
        return cmd_sync(ns)
    print(f"ENV FAIL: unknown action {action}", file=sys.stderr)
    return 1


__all__ = [
    "show_env",
    "sync_env",
    "redact_env_lines",
    "redact_value",
    "is_secret_key",
    "collect_layers",
    "merge_layers",
    "cmd_env_cli",
    "main",
]


if __name__ == "__main__":
    sys.exit(main())
