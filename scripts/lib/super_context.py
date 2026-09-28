#!/usr/bin/env python3
"""Emperor Time super-context CLI — graph-over-grep + thoughttrail + sandbox.

Commands:
  build | find | path | explain | trail | l0 | slice
  sot sync|add-plugin|status
  sandbox plan|up|down|ports   (engine: scripts/lib/sandbox_engine.py)
  artifacts list|stub-create|sync
  runtime use|status (compose|podman|k8s)
  env show|sync (redacted; workspace_env merges overlays)
  secrets list|inject|declare (blind broker; HARD-GATE leak checks)
  layout   (ensure .emperor inverted dirs)

Tiers:
  L0 — highest-degree nodes + file communities (load before mass-grep)
  L1 — find / path / explain on edges (EXTRACTED|INFERRED)
  L2 — optional path:line slice cites when asked

Sandbox engine (v0.4.135+): real port allocator (no collisions), compose /
podman / k8s emitters, loadable isolate|mock|simulate profiles.
Blind secrets broker + unified workspace env (v0.4.136+): names+status
only; inject via env-file/vault hook; env sync merges plugin overlays.
No embeddings. No Graphify code. Stdlib + sqlite3.
Thin twins: scripts/context.sh / context.ps1 (+ thoughttrail / super-context / sandbox / sot aliases).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

import context_store as store
import thoughttrail as trail
import sandbox_engine as sbox
import secrets_broker as secrets
import workspace_env as wenv


LEAF = "references/super-context.md"
IRON = "GRAPH_BEFORE_GREP"


def _repo_root(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for p in [cur, *cur.parents]:
        if (p / ".git").exists() or (p / "SKILL.md").exists():
            return p
    return cur


def _print_card() -> int:
    print(
        "\n".join(
            [
                f"CONTEXT checklist=yes leaf={LEAF}",
                "TIER L0: god/degree map + communities (.emperor/context/l0.md)",
                "TIER L1: find | path | explain on EXTRACTED|INFERRED edges",
                "TIER L2: slice path:line cites (only when asked)",
                "LAYOUT: context/ thoughttrail/ sot/plugins/ artifacts/ sandbox/runtime/{compose,podman,k8s}/ env/ secrets/",
                "ENGINE: sandbox plan|up|down|ports + runtime use compose|podman|k8s; env|secrets blind",
                f"MUST: load L0 before mass-grep  IRON={IRON}",
                "GATE rule=graph-over-grep; no embeddings; no Graphify ports",
            ]
        )
    )
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else _repo_root()
    trail.ensure_layout(root)
    db = Path(args.db) if args.db else store.default_db_path(root)
    stats = store.build(root, db, force=args.force)
    l0 = store.write_l0(db, store.default_l0_path(root))
    print(f"BUILD ok db={stats['db']}")
    print(
        f"SCANNED={stats['scanned']} UPDATED={stats['updated']} "
        f"SKIPPED={stats['skipped']} NODES={stats['nodes']} EDGES={stats['edges']}"
    )
    print(f"L0 {l0}")
    return 0


def cmd_find(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else _repo_root()
    db = Path(args.db) if args.db else store.default_db_path(root)
    if not db.is_file():
        print("FIND FAIL: no graph — run: emperor context build", file=sys.stderr)
        return 1
    hits = store.find_nodes(db, args.query, limit=args.limit)
    if not hits:
        print(f"FIND none query={args.query!r}")
        return 0
    print(f"FIND n={len(hits)} query={args.query!r}")
    for h in hits:
        loc = ""
        if h.get("source_path") and h.get("line_start"):
            loc = f" {h['source_path']}:{h['line_start']}"
        print(f"  [{h['kind']}] {h['label']} id={h['id']}{loc}")
    return 0


def cmd_path(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else _repo_root()
    db = Path(args.db) if args.db else store.default_db_path(root)
    if not db.is_file():
        print("PATH FAIL: no graph — run: emperor context build", file=sys.stderr)
        return 1
    chain = store.shortest_path(db, args.a, args.b, max_depth=args.depth)
    if not chain:
        print(f"PATH none {args.a!r} → {args.b!r}")
        return 0
    print(f"PATH hops={len(chain) - 1}")
    for i, n in enumerate(chain):
        print(f"  {i}. [{n['kind']}] {n['label']} id={n['id']}")
    return 0


def cmd_explain(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else _repo_root()
    db = Path(args.db) if args.db else store.default_db_path(root)
    if not db.is_file():
        print("EXPLAIN FAIL: no graph — run: emperor context build", file=sys.stderr)
        return 1
    info = store.explain_node(db, args.query)
    if not info:
        print(f"EXPLAIN none query={args.query!r}")
        return 0
    n = info["node"]
    print(
        f"EXPLAIN [{n['kind']}] {n['label']} id={n['id']} "
        f"degree={info['degree']} path={n.get('source_path','')}"
    )
    for e in info["edges"][:30]:
        print(
            f"  {e['src_label']} -[{e['relation']}/{e['confidence']}]-> "
            f"{e['dst_label']}"
        )
    return 0


def cmd_l0(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else _repo_root()
    db = Path(args.db) if args.db else store.default_db_path(root)
    l0_path = store.default_l0_path(root)
    if not db.is_file():
        print("L0 FAIL: no graph — run: emperor context build", file=sys.stderr)
        return 1
    store.write_l0(db, l0_path, top=args.top)
    print(l0_path.read_text(encoding="utf-8"), end="")
    return 0


def cmd_slice(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else _repo_root()
    db = Path(args.db) if args.db else store.default_db_path(root)
    if not db.is_file():
        print("SLICE FAIL: no graph — run: emperor context build", file=sys.stderr)
        return 1
    cites = store.slice_cite(db, args.query)
    print(f"SLICE n={len(cites)} query={args.query!r}")
    for c in cites:
        print(f"  {c}")
    return 0


def cmd_trail(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else _repo_root()
    trail.ensure_layout(root)
    action = args.trail_action
    if action == "append":
        if not args.text:
            print("TRAIL FAIL: --text required for append", file=sys.stderr)
            return 1
        node_ids = [x for x in (args.nodes or "").split(",") if x.strip()]
        entry = trail.append_entry(
            root,
            args.text,
            node_ids=node_ids,
            ledger=args.ledger or "",
            task=args.task or "",
        )
        print(f"TRAIL append id={entry['id']} nodes={entry['node_ids']}")
        return 0
    if action == "link":
        if not args.entry or not args.nodes:
            print("TRAIL FAIL: link needs --entry and --nodes", file=sys.stderr)
            return 1
        node_ids = [x for x in args.nodes.split(",") if x.strip()]
        updated = trail.link_nodes(root, args.entry, node_ids)
        if not updated:
            print(f"TRAIL FAIL: entry not found id={args.entry}", file=sys.stderr)
            return 1
        print(f"TRAIL link id={updated['id']} nodes={updated['node_ids']}")
        return 0
    # list
    rows = trail.list_entries(root, limit=args.limit, node_id=args.node or "")
    print(f"TRAIL n={len(rows)}")
    for r in rows:
        print(
            f"  {r.get('ts','')} id={r.get('id')} "
            f"nodes={r.get('node_ids')} :: {r.get('text','')[:120]}"
        )
    return 0


def cmd_layout(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else _repo_root()
    paths = trail.ensure_layout(root)
    profs = sbox.ensure_profiles(root)
    print("LAYOUT ok")
    for k, p in paths.items():
        print(f"  {k}={p}")
    for k, p in profs.items():
        print(f"  profile_{k}={p}")
    return 0



def _run_git(args: list[str], *, cwd: Path | None = None) -> tuple[int, str]:
    try:
        r = subprocess.run(
            ["git", *args],
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return 127, "git not found"
    out = (r.stdout or "") + (r.stderr or "")
    return r.returncode, out.strip()


def _plugin_mirror(plugin_dir: Path) -> Path:
    return plugin_dir / "mirror"


def _load_plugin_meta(plugin_dir: Path) -> dict:
    meta_path = plugin_dir / "plugin.json"
    if meta_path.is_file():
        return json.loads(meta_path.read_text(encoding="utf-8"))
    return {}


def _save_plugin_meta(plugin_dir: Path, meta: dict) -> None:
    (plugin_dir / "plugin.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )


def cmd_sot(args: argparse.Namespace) -> int:
    """SOT sync|add-plugin|status — real git fetch-only mirrors under sot/plugins."""
    root = Path(args.root).resolve() if args.root else _repo_root()
    paths = trail.ensure_layout(root)
    action = args.sot_action
    plugins_dir = paths["sot_plugins"]
    if action == "status":
        plugins = [
            p.name
            for p in sorted(plugins_dir.iterdir())
            if p.is_dir() and p.name not in {"__pycache__"} and (p / "plugin.json").is_file()
        ]
        print(f"SOT status fetch_only=true plugins={len(plugins)}")
        print(f"  pointer={paths['sot'] / 'POINTER.md'}")
        for name in plugins:
            meta = _load_plugin_meta(plugins_dir / name)
            mirror = _plugin_mirror(plugins_dir / name)
            ready = "ready" if mirror.is_dir() else "meta-only"
            print(
                f"  plugin={name} state={ready} "
                f"ref={meta.get('ref', 'main')} url={meta.get('url', '')}"
            )
        if not plugins:
            print("  (no plugins — emperor sot add-plugin <name> <url>)")
        return 0
    if action == "add-plugin":
        if not args.name:
            print("SOT FAIL: add-plugin needs <name>", file=sys.stderr)
            return 1
        if not args.url:
            print("SOT FAIL: add-plugin needs <url> (git URL or local path)", file=sys.stderr)
            return 1
        dest = plugins_dir / args.name
        dest.mkdir(parents=True, exist_ok=True)
        ref = args.ref or "main"
        mirror = _plugin_mirror(dest)
        meta = {
            "name": args.name,
            "url": args.url,
            "fetch_only": True,
            "ref": ref,
            "mirror": "mirror",
            "stub": False,
        }
        # Real clone --mirror (fetch-only SOT). Never checkout a working tree here.
        if mirror.exists():
            print(f"SOT add-plugin exists name={args.name} — use sot sync to refresh")
        else:
            rc, out = _run_git(
                ["clone", "--mirror", args.url, str(mirror)]
            )
            if rc != 0:
                print(f"SOT FAIL: git clone --mirror rc={rc}", file=sys.stderr)
                print(out, file=sys.stderr)
                return 1
            # pin ref availability (fetch-only; no checkout)
            rc2, out2 = _run_git(["-C", str(mirror), "rev-parse", f"refs/heads/{ref}"])
            if rc2 != 0:
                # try tags or remote HEAD
                rc2, out2 = _run_git(["-C", str(mirror), "rev-parse", "HEAD"])
            meta["tip"] = out2.strip() if rc2 == 0 else ""
            print(f"SOT add-plugin cloned name={args.name} mirror={mirror}")
            if meta.get("tip"):
                print(f"SOT tip={meta['tip']}")
        _save_plugin_meta(dest, meta)
        frag = dest / "compose.fragment.yml"
        if not frag.exists():
            frag.write_text(
                "\n".join(
                    [
                        f"# fragment for plugin {args.name} — sandbox plan merges these",
                        f"  {args.name}:",
                        f"    image: ${{{args.name.upper()}_IMAGE:-alpine:3.20}}",
                        '    profiles: ["et-plugin"]',
                        "",
                    ]
                ),
                encoding="utf-8",
            )
        print(f"SOT add-plugin ok name={args.name} path={dest} fetch_only=true")
        return 0
    if action == "sync":
        pointer = paths["sot"] / "POINTER.md"
        print(f"SOT sync pointer={pointer}")
        plugins = [
            p
            for p in sorted(plugins_dir.iterdir())
            if p.is_dir() and (p / "plugin.json").is_file()
        ]
        if not plugins:
            print("SOT sync none (no plugins)")
            return 0
        failed = 0
        for pdir in plugins:
            meta = _load_plugin_meta(pdir)
            mirror = _plugin_mirror(pdir)
            if not mirror.is_dir():
                url = meta.get("url") or ""
                if not url:
                    print(f"SOT sync SKIP {pdir.name}: no mirror and no url")
                    failed += 1
                    continue
                rc, out = _run_git(["clone", "--mirror", url, str(mirror)])
                if rc != 0:
                    print(f"SOT sync FAIL {pdir.name}: clone {out}", file=sys.stderr)
                    failed += 1
                    continue
            rc, out = _run_git(["-C", str(mirror), "fetch", "--all", "--prune"])
            if rc != 0:
                print(f"SOT sync FAIL {pdir.name}: fetch {out}", file=sys.stderr)
                failed += 1
                continue
            ref = meta.get("ref") or "main"
            rc2, tip = _run_git(["-C", str(mirror), "rev-parse", f"refs/heads/{ref}"])
            if rc2 != 0:
                rc2, tip = _run_git(["-C", str(mirror), "rev-parse", "HEAD"])
            if rc2 == 0:
                meta["tip"] = tip.strip()
                meta["last_sync"] = __import__("datetime").datetime.now(
                    __import__("datetime").timezone.utc
                ).strftime("%Y-%m-%dT%H:%M:%SZ")
                _save_plugin_meta(pdir, meta)
                print(f"SOT sync ok plugin={pdir.name} tip={meta['tip']}")
            else:
                print(f"SOT sync ok plugin={pdir.name} (tip unresolved)")
        if failed:
            print(f"SOT sync DONE with failures={failed}", file=sys.stderr)
            return 1
        print(f"SOT sync DONE plugins={len(plugins)}")
        return 0
    print(f"SOT FAIL: unknown action {action}", file=sys.stderr)
    return 1


def _allocate_ports(sandbox_dir: Path, artifact_id: str, n: int = 3) -> dict:
    """Delegate to sandbox_engine PortAllocator (persist; no collisions)."""
    # sandbox_dir is .emperor/sandbox; root is its parent.parent
    root = sandbox_dir.parent.parent if sandbox_dir.name == "sandbox" else sandbox_dir
    # walk up if needed
    if not (root / ".emperor").is_dir():
        root = sandbox_dir.parent
    _ = n  # stride handled inside engine
    return sbox.allocate_ports(root, artifact_id)


def _compose_from_plugins(root: Path, artifact_id: str, alloc: dict) -> str:
    """Delegate to sandbox_engine compose emitter."""
    return sbox.emit_compose(root, artifact_id, alloc)


def cmd_sandbox(args: argparse.Namespace) -> int:
    """sandbox plan|up|down|ports — real engine (ports/emitters/profiles)."""
    return sbox.cmd_sandbox_cli(args)


def cmd_artifacts(args: argparse.Namespace) -> int:
    """Artifacts list|stub-create|sync — multi-repo copies from SOT plugins."""
    root = Path(args.root).resolve() if args.root else _repo_root()
    paths = trail.ensure_layout(root)
    action = args.artifacts_action
    if action == "list":
        arts = [
            p.name
            for p in sorted(paths["artifacts"].iterdir())
            if p.is_dir()
        ]
        print(f"ARTIFACTS n={len(arts)}")
        for a in arts:
            repos = paths["artifacts"] / a / "repos"
            n = len(list(repos.iterdir())) if repos.is_dir() else 0
            print(f"  {a} repos={n}")
        return 0
    if action == "stub-create":
        aid = args.artifact or "task-stub"
        dest = paths["artifacts"] / aid
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "repos").mkdir(exist_ok=True)
        (dest / "README.md").write_text(
            f"# Artifact `{aid}`\n\n"
            "Multi-repo worktrees live under `repos/<plugin>/`.\n"
            "Synced from fetch-only SOT mirrors — never mutate SOT.\n"
            "Run: `emperor context artifacts sync --artifact "
            f"{aid}`\n",
            encoding="utf-8",
        )
        meta = {"id": aid, "plugins": [], "synced": False}
        (dest / "artifact.json").write_text(
            json.dumps(meta, indent=2) + "\n", encoding="utf-8"
        )
        print(f"ARTIFACTS stub-create id={aid} path={dest}")
        return 0
    if action == "sync":
        aid = args.artifact or "default"
        dest = paths["artifacts"] / aid
        dest.mkdir(parents=True, exist_ok=True)
        repos_dir = dest / "repos"
        repos_dir.mkdir(exist_ok=True)
        plugins_dir = paths["sot_plugins"]
        plugins = [
            p
            for p in sorted(plugins_dir.iterdir())
            if p.is_dir() and (p / "plugin.json").is_file()
        ]
        if not plugins:
            print("ARTIFACTS sync FAIL: no SOT plugins — sot add-plugin first", file=sys.stderr)
            return 1
        synced = []
        failed = 0
        for pdir in plugins:
            meta = _load_plugin_meta(pdir)
            mirror = _plugin_mirror(pdir)
            if not mirror.is_dir():
                print(f"ARTIFACTS sync SKIP {pdir.name}: no mirror (sot sync first)")
                failed += 1
                continue
            target = repos_dir / pdir.name
            ref = meta.get("ref") or "main"
            tip = meta.get("tip") or ""
            if not tip:
                rc, tip = _run_git(["-C", str(mirror), "rev-parse", f"refs/heads/{ref}"])
                if rc != 0:
                    rc, tip = _run_git(["-C", str(mirror), "rev-parse", "HEAD"])
                tip = tip.strip() if rc == 0 else ""
            if not tip:
                print(f"ARTIFACTS sync FAIL {pdir.name}: no tip", file=sys.stderr)
                failed += 1
                continue
            if target.exists():
                # refresh existing clone from mirror
                rc, out = _run_git(["-C", str(target), "fetch", str(mirror), ref])
                if rc != 0:
                    rc, out = _run_git(["-C", str(target), "fetch", str(mirror)])
                if rc == 0:
                    _run_git(["-C", str(target), "checkout", "-B", ref, "FETCH_HEAD"])
                else:
                    print(f"ARTIFACTS sync FAIL {pdir.name}: {out}", file=sys.stderr)
                    failed += 1
                    continue
            else:
                rc, out = _run_git(
                    ["clone", "--no-hardlinks", f"--branch={ref}", str(mirror), str(target)]
                )
                if rc != 0:
                    # mirror may be bare without branch name — clone then checkout tip
                    rc, out = _run_git(["clone", str(mirror), str(target)])
                    if rc != 0:
                        print(f"ARTIFACTS sync FAIL {pdir.name}: clone {out}", file=sys.stderr)
                        failed += 1
                        continue
                    if tip:
                        _run_git(["-C", str(target), "checkout", "-B", ref, tip])
            synced.append(pdir.name)
            print(f"ARTIFACTS sync ok plugin={pdir.name} path={target} tip={tip[:12]}")
        art_meta = {
            "id": aid,
            "plugins": synced,
            "synced": failed == 0 and bool(synced),
        }
        (dest / "artifact.json").write_text(
            json.dumps(art_meta, indent=2) + "\n", encoding="utf-8"
        )
        # generate compose into artifact
        alloc = _allocate_ports(paths["sandbox"], aid)
        compose = _compose_from_plugins(root, aid, alloc)
        (dest / "compose.yml").write_text(compose, encoding="utf-8")
        if failed:
            print(f"ARTIFACTS sync DONE with failures={failed}", file=sys.stderr)
            return 1
        print(f"ARTIFACTS sync DONE id={aid} plugins={len(synced)}")
        return 0
    print(f"ARTIFACTS FAIL: unknown action {action}", file=sys.stderr)
    return 1


def cmd_runtime(args: argparse.Namespace) -> int:
    """Pluggable runtime: use compose|podman|k8s (persisted; emitters real)."""
    return sbox.cmd_runtime_cli(args)


def cmd_env(args: argparse.Namespace) -> int:
    """Unified workspace env — show (redacted) | sync (merge overlays)."""
    return wenv.cmd_env_cli(args)


def cmd_secrets(args: argparse.Namespace) -> int:
    """Blind credentials broker — list/declare/inject; HARD-GATE leak checks."""
    return secrets.cmd_secrets_cli(args)


def build_parser() -> argparse.ArgumentParser:
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument("--root", default="", help="repo root (default: detect)")
    parent.add_argument("--db", default="", help="graph.sqlite path")

    p = argparse.ArgumentParser(
        prog="super_context",
        description="Emperor Time super-context / thoughttrail / sandbox engine",
        parents=[parent],
    )
    sub = p.add_subparsers(dest="cmd")

    b = sub.add_parser("build", help="extract MD → graph.sqlite + L0", parents=[parent])
    b.add_argument("--force", action="store_true")

    f = sub.add_parser("find", help="L1 substring find over nodes", parents=[parent])
    f.add_argument("query")
    f.add_argument("--limit", type=int, default=20)

    pa = sub.add_parser("path", help="L1 shortest path between two nodes", parents=[parent])
    pa.add_argument("a")
    pa.add_argument("b")
    pa.add_argument("--depth", type=int, default=8)

    e = sub.add_parser("explain", help="L1 explain node + edges", parents=[parent])
    e.add_argument("query")

    l0 = sub.add_parser("l0", help="print/refresh L0 god map", parents=[parent])
    l0.add_argument("--top", type=int, default=15)

    sl = sub.add_parser("slice", help="L2 path:line cites", parents=[parent])
    sl.add_argument("query")

    tr = sub.add_parser("trail", help="thoughttrail append|list|link", parents=[parent])
    tr.add_argument(
        "trail_action",
        nargs="?",
        default="list",
        choices=["append", "list", "link"],
    )
    tr.add_argument("--text", default="")
    tr.add_argument("--nodes", default="", help="comma-separated node ids")
    tr.add_argument("--entry", default="", help="entry id for link")
    tr.add_argument("--ledger", default="")
    tr.add_argument("--task", default="")
    tr.add_argument("--node", default="", help="filter list by node id")
    tr.add_argument("--limit", type=int, default=20)

    sub.add_parser("layout", help="ensure .emperor inverted dirs", parents=[parent])

    sot = sub.add_parser("sot", help="SOT sync|add-plugin|status stubs", parents=[parent])
    sot.add_argument(
        "sot_action",
        choices=["sync", "add-plugin", "status"],
    )
    sot.add_argument("name", nargs="?", default="")
    sot.add_argument("url", nargs="?", default="")
    sot.add_argument("--ref", default="main")

    sb = sub.add_parser("sandbox", help="sandbox plan|up|down|ports (engine)", parents=[parent])
    sb.add_argument(
        "sandbox_action",
        choices=["plan", "up", "down", "ports"],
    )
    sb.add_argument("--artifact", default="default")

    ar = sub.add_parser("artifacts", help="artifacts list|stub-create", parents=[parent])
    ar.add_argument(
        "artifacts_action",
        choices=["list", "stub-create", "sync"],
    )
    ar.add_argument("--artifact", default="")

    rt = sub.add_parser("runtime", help="runtime use|status (compose|podman|k8s)", parents=[parent])
    rt.add_argument("runtime_action", choices=["use", "status"])
    rt.add_argument("backend", nargs="?", default="", help="compose|podman|k8s for use")

    ev = sub.add_parser("env", help="workspace env show|sync (redacted merge)", parents=[parent])
    ev.add_argument("env_action", choices=["show", "sync"])
    ev.add_argument("--artifact", default="", help="artifact id for sync/show scope")

    sec = sub.add_parser("secrets", help="blind creds list|inject|declare", parents=[parent])
    sec.add_argument("secrets_action", choices=["list", "inject", "declare"])
    sec.add_argument("--name", default="", help="declare name only (no value)")
    sec.add_argument("--artifact", default="default")
    sec.add_argument("--from-file", default="", help="bind value from file (never echoed)")
    sec.add_argument("--broker", default="", help="env-file|vault|1password")
    sec.add_argument("--names", default="", help="comma-separated inject subset")
    sec.add_argument("--target", default="", help="override inject env-file path")
    sec.add_argument(
        "--reject-secret-leak",
        action="store_true",
        help="HARD-GATE: refuse secret-leaking dumps",
    )
    sec.add_argument(
        "--check-env-redacted",
        default="",
        help="HARD-GATE: fail when dump would expose values",
    )

    return p



def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        return _print_card()
    # HARD-GATE shortcuts (work with or without secrets subcommand)
    if "--reject-secret-leak" in argv:
        sys.stdout.write(secrets.reject_secret_leak())
        return 1
    if "--check-env-redacted" in argv:
        # allow: secrets --check-env-redacted PATH  OR  --check-env-redacted PATH
        try:
            idx = argv.index("--check-env-redacted")
            target = argv[idx + 1] if idx + 1 < len(argv) else ""
        except ValueError:
            target = ""
        if not target or target.startswith("-"):
            print("SECRETS FAIL: --check-env-redacted needs PATH", file=sys.stderr)
            return 1
        ok, msg = secrets.check_env_redacted(Path(target))
        print(msg)
        return 0 if ok else 1
    parser = build_parser()
    args = parser.parse_args(argv)
    # normalize check-env-redacted empty → None for broker adapter
    if getattr(args, "check_env_redacted", "") in ("", None):
        if hasattr(args, "check_env_redacted"):
            args.check_env_redacted = None
    # normalize empty root/db
    if not getattr(args, "root", ""):
        args.root = ""
    if not getattr(args, "db", ""):
        args.db = ""
    dispatch = {
        "build": cmd_build,
        "find": cmd_find,
        "path": cmd_path,
        "explain": cmd_explain,
        "l0": cmd_l0,
        "slice": cmd_slice,
        "trail": cmd_trail,
        "layout": cmd_layout,
        "sot": cmd_sot,
        "sandbox": cmd_sandbox,
        "artifacts": cmd_artifacts,
        "runtime": cmd_runtime,
        "env": cmd_env,
        "secrets": cmd_secrets,
    }
    fn = dispatch.get(args.cmd)
    if not fn:
        return _print_card()
    return fn(args)


if __name__ == "__main__":
    sys.exit(main())
