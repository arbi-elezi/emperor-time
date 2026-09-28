#!/usr/bin/env python3
"""Emperor Time blind secrets broker — names+status only; NEVER plaintext.

Real in v0.4.136+ (deepens stubs from super_context v0.4.133):

1. Manifest `.emperor/secrets/manifest.json` — names, status, broker kind.
2. Values live under `.emperor/secrets/values/<NAME>` (gitignored) OR via
   vault / 1Password hook placeholders — never echoed to agent/LLM stdout.
3. CLI: `secrets list|declare|inject`
4. HARD-GATE: `--reject-secret-leak` / `--check-env-redacted PATH`

Inject writes an env-file outside git (artifact path) or a vault-hook
placeholder receipt. Agent sees receipt + names only.

No embeddings. No Graphify. Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import os
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
IRON = "BLIND_SECRETS"
BROKERS = ("env-file", "vault", "1password")
STATUSES = ("declared", "bound", "missing", "injected")

# Patterns that look like secret values being dumped (not mere KEY= names).
_LEAK_LINE = re.compile(
    r"(?i)^\s*(?:export\s+)?([A-Z][A-Z0-9_]*(?:SECRET|PASSWORD|TOKEN|API[_-]?KEY|PRIVATE[_-]?KEY|CREDENTIAL)[A-Z0-9_]*)\s*=\s*(.+)$"
)
_REDACTED = re.compile(r"(?i)^\*+$|^<*REDACTED>*$|^\[REDACTED\]$|^\*REDACTED\*$|^\$\{.+\}$|^<.*>$")


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


def secrets_dir(root: Path) -> Path:
    return root / ".emperor" / "secrets"


def manifest_path(root: Path) -> Path:
    return secrets_dir(root) / "manifest.json"


def values_dir(root: Path) -> Path:
    return secrets_dir(root) / "values"


def default_manifest() -> dict[str, Any]:
    return {
        "broker": "env-file",
        "names": [],
        "entries": {},
        "note": "Agent sees names/status only — never plaintext values",
    }


def load_manifest(root: Path) -> dict[str, Any]:
    trail.ensure_layout(root)
    path = manifest_path(root)
    if not path.is_file():
        data = default_manifest()
        save_manifest(root, data)
        return data
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("broker", "env-file")
    data.setdefault("names", [])
    data.setdefault("entries", {})
    # migrate flat names → entries
    entries = data["entries"]
    for n in list(data["names"]):
        if n not in entries:
            entries[n] = {"status": "declared", "bound": False}
    return data


def save_manifest(root: Path, data: dict[str, Any]) -> None:
    path = manifest_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    # keep names list in sync with entries for back-compat
    entries = data.get("entries") or {}
    data["names"] = sorted(entries.keys()) if entries else list(data.get("names") or [])
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _value_path(root: Path, name: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", name)
    return values_dir(root) / safe


def _has_bound_value(root: Path, name: str) -> bool:
    """True if a value exists on disk or via EMPEROR_SECRET_<NAME> env.

    Does NOT return or print the value.
    """
    vp = _value_path(root, name)
    if vp.is_file() and vp.stat().st_size > 0:
        return True
    env_key = f"EMPEROR_SECRET_{name}"
    if os.environ.get(env_key):
        return True
    return False


def _read_value_blind(root: Path, name: str) -> str | None:
    """Read secret value for inject only — callers MUST NOT print it."""
    vp = _value_path(root, name)
    if vp.is_file():
        return vp.read_text(encoding="utf-8").rstrip("\n")
    env_key = f"EMPEROR_SECRET_{name}"
    val = os.environ.get(env_key)
    if val is not None and val != "":
        return val
    return None


def declare(
    root: Path,
    name: str,
    *,
    status: str = "declared",
    broker: str | None = None,
) -> dict[str, Any]:
    """Register a secret name only. Values are never accepted on this path."""
    name = name.strip()
    if not name:
        raise ValueError("empty secret name")
    if re.search(r"[\s=]", name):
        raise ValueError("secret name must be a single token (no spaces/=)")
    data = load_manifest(root)
    if broker and broker in BROKERS:
        data["broker"] = broker
    entries = data.setdefault("entries", {})
    prev = entries.get(name) or {}
    bound = _has_bound_value(root, name)
    st = status if status in STATUSES else "declared"
    if bound and st == "declared":
        st = "bound"
    entries[name] = {
        "status": st,
        "bound": bound,
        "declared_at": prev.get("declared_at") or _utc(),
        "updated_at": _utc(),
    }
    save_manifest(root, data)
    return entries[name]


def bind_from_file(root: Path, name: str, source: Path) -> dict[str, Any]:
    """Bind a value from a file into gitignored values/ without echoing it.

    The file contents are copied; source may be deleted by caller. Never
    prints the value. Status becomes bound.
    """
    name = name.strip()
    if not name:
        raise ValueError("empty secret name")
    if not source.is_file():
        raise FileNotFoundError(str(source))
    raw = source.read_text(encoding="utf-8")
    # strip single trailing newline only; keep content opaque
    if raw.endswith("\n"):
        raw = raw[:-1]
    if not raw:
        raise ValueError("source file empty — refuse bind")
    vdir = values_dir(root)
    vdir.mkdir(parents=True, exist_ok=True)
    # ensure values/.gitignore
    gi = vdir / ".gitignore"
    if not gi.exists():
        gi.write_text("*\n!.gitignore\n", encoding="utf-8")
    _value_path(root, name).write_text(raw + "\n", encoding="utf-8")
    return declare(root, name, status="bound")


def list_secrets(root: Path) -> list[dict[str, Any]]:
    """Return name+status rows only (no values)."""
    data = load_manifest(root)
    rows = []
    for name in sorted(data.get("entries") or data.get("names") or []):
        entry = (data.get("entries") or {}).get(name) or {}
        bound = bool(entry.get("bound")) or _has_bound_value(root, name)
        status = entry.get("status") or ("bound" if bound else "declared")
        if bound and status == "declared":
            status = "bound"
        rows.append({"name": name, "status": status, "bound": bound})
    return rows


def inject(
    root: Path,
    artifact_id: str,
    *,
    names: list[str] | None = None,
    target: Path | None = None,
) -> dict[str, Any]:
    """Inject secrets into artifact env-file via broker. Never print values.

    env-file broker: write `.emperor/artifacts/<id>/.env.secrets` (gitignored
    via secrets + artifact conventions) with KEY=value lines, then a public
    receipt with names only.

    vault / 1password: write a placeholder receipt describing the hook;
    values are not fetched in-process (honest stub for external CLI).
    """
    data = load_manifest(root)
    broker = data.get("broker") or "env-file"
    all_names = list((data.get("entries") or {}).keys()) or list(data.get("names") or [])
    wanted = names if names else all_names
    trail.ensure_layout(root)
    art_dir = root / ".emperor" / "artifacts" / artifact_id
    art_dir.mkdir(parents=True, exist_ok=True)
    # ensure artifact ignores secret env files
    art_gi = art_dir / ".gitignore"
    if not art_gi.exists():
        art_gi.write_text(".env\n.env.*\n*.secrets\n!.gitignore\n", encoding="utf-8")

    receipt: dict[str, Any] = {
        "artifact": artifact_id,
        "broker": broker,
        "injected_names": [],
        "skipped": [],
        "plaintext_to_stdout": False,
        "stub": False,
        "ts": _utc(),
    }

    if broker in ("vault", "1password"):
        # Placeholder hook — external CLI would fill; we never print values.
        hook_path = secrets_dir(root) / f"hook-{broker}-{artifact_id}.json"
        hook = {
            "broker": broker,
            "artifact": artifact_id,
            "names": wanted,
            "op": "inject",
            "note": (
                f"Placeholder for {broker} CLI hook. "
                "Run external broker to materialize; ET never echoes values."
            ),
            "plaintext_to_stdout": False,
        }
        hook_path.write_text(json.dumps(hook, indent=2) + "\n", encoding="utf-8")
        receipt["hook"] = str(hook_path)
        receipt["injected_names"] = list(wanted)
        receipt["stub"] = True  # hook placeholder, not a live vault call
        for n in wanted:
            declare(root, n, status="injected")
    else:
        # env-file broker
        out_path = target or (art_dir / ".env.secrets")
        lines: list[str] = [
            f"# Emperor Time blind inject — {artifact_id} @ {_utc()}",
            "# DO NOT commit. Agent/LLM must never cat this file into chat.",
        ]
        injected = []
        skipped = []
        for n in wanted:
            val = _read_value_blind(root, n)
            if val is None:
                skipped.append({"name": n, "reason": "unbound"})
                declare(root, n, status="missing")
                continue
            # write value to file only — never to stdout
            lines.append(f"{n}={val}")
            injected.append(n)
            declare(root, n, status="injected")
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        # chmod best-effort
        try:
            out_path.chmod(0o600)
        except OSError:
            pass
        receipt["env_file"] = str(out_path)
        receipt["injected_names"] = injected
        receipt["skipped"] = skipped

    receipt_path = secrets_dir(root) / f"inject-{artifact_id}.receipt.json"
    # Public receipt — names only, never values
    public = {
        "artifact": receipt["artifact"],
        "broker": receipt["broker"],
        "injected_names": receipt["injected_names"],
        "skipped_names": [s["name"] if isinstance(s, dict) else s for s in receipt.get("skipped") or []],
        "plaintext_to_stdout": False,
        "stub": receipt.get("stub", False),
        "env_file": receipt.get("env_file"),
        "hook": receipt.get("hook"),
        "ts": receipt["ts"],
    }
    receipt_path.write_text(json.dumps(public, indent=2) + "\n", encoding="utf-8")
    receipt["receipt"] = str(receipt_path)
    return receipt


# ---------------------------------------------------------------------------
# HARD-GATE
# ---------------------------------------------------------------------------


def reject_secret_leak() -> str:
    return (
        "REJECT SECRET LEAK: HARD-GATE — blind secrets broker refuses dumps "
        "that would expose plaintext values to the agent/LLM. "
        f"Use `emperor secrets list` (names+status only) + `inject` (receipt). "
        f"IRON={IRON} leaf={LEAF}\n"
    )


def _looks_redacted(value: str) -> bool:
    v = value.strip().strip("\"'")
    if not v:
        return True
    if _REDACTED.match(v):
        return True
    if v in ("***", "***REDACTED***", "[redacted]", "REDACTED"):
        return True
    return False


def check_env_redacted(path: Path) -> tuple[bool, str]:
    """Fail if PATH (file or dir dump) would expose secret-looking values.

    Vacuous PASS when no secrets activity / no leaky lines.
    Scans for KEY=VALUE where KEY looks secret-ish and VALUE is not redacted.
    Also fails if a known bound value from values/ appears as substring
    (without printing the value).
    """
    p = path.resolve()
    texts: list[tuple[str, str]] = []
    if p.is_file():
        texts.append((str(p), p.read_text(encoding="utf-8", errors="replace")))
    elif p.is_dir():
        # scan common dump / env paths
        candidates = list(p.rglob("*.env")) + list(p.rglob("*.dump")) + list(p.rglob("*.log"))
        # also CLAIM / ledger style
        for name in ("DUMP.md", "dump.txt", "env-show.txt", "CLAIM.md", "ledger.md"):
            f = p / name
            if f.is_file():
                candidates.append(f)
        # if pointing at a fixture root with env-leaky.txt
        for f in p.rglob("env-leaky*"):
            if f.is_file():
                candidates.append(f)
        for f in p.rglob("env-redacted*"):
            if f.is_file():
                candidates.append(f)
        seen = set()
        for f in candidates:
            if f in seen:
                continue
            seen.add(f)
            # skip gitignored values/ store itself — those are allowed on disk
            if "secrets/values" in str(f).replace("\\", "/"):
                continue
            if f.name.endswith(".secrets") and ".emperor/artifacts" in str(f).replace("\\", "/"):
                continue
            try:
                texts.append((str(f), f.read_text(encoding="utf-8", errors="replace")))
            except OSError:
                continue
    else:
        return False, f"SECRETS FAIL: path not found {p}"

    # Collect known plaintext values (for substring check) without logging them
    known_values: list[str] = []
    # Walk up to find repo root for values/
    root = p if p.is_dir() else p.parent
    for cand in [root, *root.parents]:
        if (cand / ".emperor" / "secrets").is_dir() or (cand / "SKILL.md").is_file():
            root = cand
            break
    vdir = values_dir(root)
    if vdir.is_dir():
        for vf in vdir.iterdir():
            if vf.is_file() and vf.name != ".gitignore":
                raw = vf.read_text(encoding="utf-8").rstrip("\n")
                if raw and len(raw) >= 4:
                    known_values.append(raw)

    leaks: list[str] = []
    secret_activity = False
    for fpath, text in texts:
        if re.search(r"(?i)\b(secret|password|token|api[_-]?key|credential|inject)\b", text):
            secret_activity = True
        for i, line in enumerate(text.splitlines(), 1):
            m = _LEAK_LINE.match(line)
            if m:
                secret_activity = True
                val = m.group(2).strip()
                if not _looks_redacted(val):
                    leaks.append(f"{fpath}:{i} key={m.group(1)} (unredacted value)")
            # known value substring (do not echo the value)
            for kv in known_values:
                if kv in line and not line.strip().startswith("#"):
                    # allow the private values/ files themselves (already skipped)
                    leaks.append(f"{fpath}:{i} (known secret value echoed)")
                    break

    if leaks:
        detail = "; ".join(leaks[:8])
        return False, (
            f"SECRETS FAIL: --check-env-redacted — dump would expose values "
            f"({len(leaks)} leak(s)): {detail}"
        )
    if not texts:
        return True, "SECRETS OK: --check-env-redacted vacuous (no dump files)"
    if not secret_activity:
        return True, "SECRETS OK: --check-env-redacted vacuous (no secrets activity)"
    return True, "SECRETS OK: --check-env-redacted (names/status only; values redacted)"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def cmd_list(args: argparse.Namespace) -> int:
    root = _resolve_root(args)
    data = load_manifest(root)
    rows = list_secrets(root)
    print(f"SECRETS list broker={data.get('broker', '?')} n={len(rows)}")
    for r in rows:
        print(f"  name={r['name']} status={r['status']} bound={str(r['bound']).lower()}")
    if not rows:
        print("  (none — emperor secrets declare --name NAME)")
    print(f"IRON: agent must never read plaintext secret values  IRON={IRON}")
    return 0


def cmd_declare(args: argparse.Namespace) -> int:
    root = _resolve_root(args)
    name = (args.name or "").strip()
    if not name:
        print("SECRETS FAIL: declare needs --name", file=sys.stderr)
        return 1
    # HARD refuse value on CLI
    if getattr(args, "value", None):
        print(
            "SECRETS FAIL: value never accepted on CLI — use --from-file "
            "(gitignored bind) or EMPEROR_SECRET_<NAME>",
            file=sys.stderr,
        )
        return 1
    try:
        if args.from_file:
            entry = bind_from_file(root, name, Path(args.from_file))
            print(f"SECRETS declare name={name} status={entry['status']} (bound from file; value withheld)")
        else:
            entry = declare(root, name, status=args.status or "declared", broker=args.broker or None)
            print(f"SECRETS declare name={name} status={entry['status']} (value never accepted on CLI)")
    except (ValueError, FileNotFoundError) as e:
        print(f"SECRETS FAIL: {e}", file=sys.stderr)
        return 1
    return 0


def cmd_inject(args: argparse.Namespace) -> int:
    root = _resolve_root(args)
    artifact = args.artifact or "default"
    names = [x for x in (args.names or "").split(",") if x.strip()] or None
    target = Path(args.target) if args.target else None
    # Optional broker override for this inject
    if args.broker:
        data = load_manifest(root)
        if args.broker not in BROKERS:
            print(f"SECRETS FAIL: broker must be one of {BROKERS}", file=sys.stderr)
            return 1
        data["broker"] = args.broker
        save_manifest(root, data)
    try:
        receipt = inject(root, artifact, names=names, target=target)
    except Exception as e:  # noqa: BLE001 — surface as SECRETS FAIL
        print(f"SECRETS FAIL: inject {e}", file=sys.stderr)
        return 1
    print(
        f"SECRETS inject artifact={artifact} broker={receipt['broker']} "
        f"names={len(receipt['injected_names'])} receipt={receipt.get('receipt')}"
    )
    if receipt.get("skipped"):
        skipped = receipt["skipped"]
        labels = [s["name"] if isinstance(s, dict) else str(s) for s in skipped]
        print(f"SECRETS inject skipped={','.join(labels)} (unbound — declare+bind first)")
    if receipt.get("env_file"):
        print(f"SECRETS inject env_file={receipt['env_file']} (outside git; do not cat)")
    if receipt.get("hook"):
        print(f"SECRETS inject hook={receipt['hook']} (vault/1password placeholder)")
    print("NOTE: plaintext withheld from agent/LLM stdout")
    return 0


def _print_card() -> int:
    print(
        "\n".join(
            [
                f"SECRETS checklist=yes leaf={LEAF}",
                "BLIND: list names+status only — NEVER plaintext values",
                "CMDS: list | declare --name | inject --artifact",
                "BIND: declare --name X --from-file PATH (gitignored values/)",
                "BROKERS: env-file | vault | 1password (hook placeholder)",
                f"HARD-GATE: --reject-secret-leak / --check-env-redacted PATH  IRON={IRON}",
                "GATE rule=blind-secrets; no embeddings; no Graphify ports",
            ]
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument("--root", default="", help="repo root (default: detect)")

    p = argparse.ArgumentParser(
        prog="secrets_broker",
        description="Emperor Time blind secrets broker (names+status only)",
        parents=[parent],
    )
    p.add_argument(
        "--reject-secret-leak",
        action="store_true",
        help="always-fail HARD-GATE: refuse secret-leaking dumps",
    )
    p.add_argument(
        "--check-env-redacted",
        type=Path,
        metavar="PATH",
        default=None,
        help="fail when dump/env would expose unredacted secret values",
    )
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("list", help="list names+status (never values)", parents=[parent])

    d = sub.add_parser("declare", help="register name only (no CLI value)", parents=[parent])
    d.add_argument("--name", default="", help="secret name")
    d.add_argument("--status", default="declared", choices=list(STATUSES))
    d.add_argument("--broker", default="", choices=[""] + list(BROKERS))
    d.add_argument("--from-file", default="", help="bind value from file (never echoed)")
    d.add_argument("--value", default="", help=argparse.SUPPRESS)  # trap & refuse

    inj = sub.add_parser("inject", help="inject into artifact env via broker", parents=[parent])
    inj.add_argument("--artifact", default="default")
    inj.add_argument("--names", default="", help="comma-separated subset")
    inj.add_argument("--target", default="", help="override env-file path")
    inj.add_argument("--broker", default="", choices=[""] + list(BROKERS))

    return p


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        return _print_card()
    # Pre-parse hard-gates that may appear anywhere
    if "--reject-secret-leak" in argv:
        sys.stdout.write(reject_secret_leak())
        return 1
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.check_env_redacted is not None:
        ok, msg = check_env_redacted(args.check_env_redacted)
        print(msg)
        return 0 if ok else 1
    if not args.cmd:
        return _print_card()
    dispatch = {
        "list": cmd_list,
        "declare": cmd_declare,
        "inject": cmd_inject,
    }
    return dispatch[args.cmd](args)


# Helpers used by super_context / workspace_env
def cmd_secrets_cli(args: Any) -> int:
    """Adapter from super_context argparse Namespace."""
    root = Path(args.root).resolve() if getattr(args, "root", "") else _resolve_root(args)
    # Harden: reject-secret-leak / check-env-redacted may be on args
    if getattr(args, "reject_secret_leak", False):
        sys.stdout.write(reject_secret_leak())
        return 1
    if getattr(args, "check_env_redacted", None):
        ok, msg = check_env_redacted(Path(args.check_env_redacted))
        print(msg)
        return 0 if ok else 1
    action = getattr(args, "secrets_action", None) or getattr(args, "cmd", None)
    # Build a synthetic namespace
    ns = argparse.Namespace(
        root=str(root),
        name=getattr(args, "name", "") or "",
        artifact=getattr(args, "artifact", "default") or "default",
        status=getattr(args, "status", "declared") or "declared",
        broker=getattr(args, "broker", "") or "",
        from_file=getattr(args, "from_file", "") or "",
        value=getattr(args, "value", "") or "",
        names=getattr(args, "names", "") or "",
        target=getattr(args, "target", "") or "",
    )
    if action == "list":
        return cmd_list(ns)
    if action == "declare":
        return cmd_declare(ns)
    if action == "inject":
        return cmd_inject(ns)
    print(f"SECRETS FAIL: unknown action {action}", file=sys.stderr)
    return 1


__all__ = [
    "declare",
    "bind_from_file",
    "list_secrets",
    "inject",
    "load_manifest",
    "save_manifest",
    "reject_secret_leak",
    "check_env_redacted",
    "cmd_secrets_cli",
    "main",
]


if __name__ == "__main__":
    sys.exit(main())
