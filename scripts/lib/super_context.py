#!/usr/bin/env python3
"""Emperor Time super-context CLI — graph-over-grep + thoughttrail + stubs.

Commands:
  build | find | path | explain | trail | l0 | slice
  sot sync|add-plugin|status
  sandbox plan|up|down|ports
  artifacts list|stub-create
  runtime use|status (compose|podman|k8s)
  env show|sync (redacted)
  secrets list|inject|declare (no plaintext)
  layout   (ensure .emperor inverted dirs)

Tiers:
  L0 — highest-degree nodes + file communities (load before mass-grep)
  L1 — find / path / explain on edges (EXTRACTED|INFERRED)
  L2 — optional path:line slice cites when asked

No embeddings. No Graphify code. Stdlib + sqlite3.
Thin twins: scripts/context.sh / context.ps1 (+ thoughttrail / super-context / sandbox / sot aliases).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

import context_store as store
import thoughttrail as trail


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
                "STUBS: sot|sandbox|runtime|env|secrets (blind creds; no plaintext)",
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
    print("LAYOUT ok")
    for k, p in paths.items():
        print(f"  {k}={p}")
    return 0


def cmd_sot(args: argparse.Namespace) -> int:
    """v1 stubs: sync | add-plugin | status — doctrine real, clone engine thin."""
    root = Path(args.root).resolve() if args.root else _repo_root()
    paths = trail.ensure_layout(root)
    action = args.sot_action
    plugins_dir = paths["sot_plugins"]
    if action == "status":
        plugins = [
            p.name
            for p in sorted(plugins_dir.iterdir())
            if p.is_dir() and p.name != "__pycache__"
        ]
        print(f"SOT status fetch_only=true plugins={len(plugins)}")
        print(f"  pointer={paths['sot'] / 'POINTER.md'}")
        for name in plugins:
            print(f"  plugin={name}")
        if not plugins:
            print("  (no plugins — emperor sot add-plugin <name> <url>)")
        return 0
    if action == "add-plugin":
        if not args.name:
            print("SOT FAIL: add-plugin needs <name>", file=sys.stderr)
            return 1
        dest = plugins_dir / args.name
        dest.mkdir(parents=True, exist_ok=True)
        meta = {
            "name": args.name,
            "url": args.url or "",
            "fetch_only": True,
            "ref": args.ref or "main",
            "stub": True,
        }
        (dest / "plugin.json").write_text(
            json.dumps(meta, indent=2) + "\n", encoding="utf-8"
        )
        # thin compose service hint
        (dest / "compose.fragment.yml").write_text(
            "\n".join(
                [
                    f"# fragment for plugin {args.name} — sandbox plan merges these",
                    f"  {args.name}:",
                    f"    image: ${{{args.name.upper()}_IMAGE:-alpine:3.20}}",
                    "    profiles: [\"et-plugin\"]",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        print(f"SOT add-plugin stub name={args.name} path={dest}")
        print("NOTE: fetch/clone not executed in v1 stub — doctrine only")
        return 0
    if action == "sync":
        # stub: touch POINTER + report
        pointer = paths["sot"] / "POINTER.md"
        print(f"SOT sync stub pointer={pointer}")
        print("NOTE: git fetch of mirrors not executed in v1 stub")
        plugins = [p.name for p in plugins_dir.iterdir() if p.is_dir()]
        print(f"SOT sync would refresh plugins={plugins or '[]'}")
        return 0
    print(f"SOT FAIL: unknown action {action}", file=sys.stderr)
    return 1


def _allocate_ports(sandbox_dir: Path, artifact_id: str, n: int = 3) -> dict:
    ports_path = sandbox_dir / "ports.json"
    data = json.loads(ports_path.read_text(encoding="utf-8"))
    if artifact_id in data.get("allocations", {}):
        return data["allocations"][artifact_id]
    base = int(data.get("next_base", 18000))
    alloc = {"http": base, "db": base + 1, "aux": base + 2}
    data.setdefault("allocations", {})[artifact_id] = alloc
    data["next_base"] = base + max(n, 3)
    ports_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return alloc


def _compose_from_plugins(root: Path, artifact_id: str, alloc: dict) -> str:
    plugins_dir = root / ".emperor" / "sot" / "plugins"
    frags: list[str] = []
    if plugins_dir.is_dir():
        for p in sorted(plugins_dir.iterdir()):
            frag = p / "compose.fragment.yml"
            if frag.is_file():
                # strip comment-only lead lines; keep service body
                frags.append(frag.read_text(encoding="utf-8").rstrip() + "\n")
    if not frags:
        body = (
            f"  et-stub:\n"
            f"    image: alpine:3.20\n"
            f"    command: [\"sleep\", \"infinity\"]\n"
            f"    ports: [\"{alloc.get('http', 18000)}:80\"]\n"
        )
    else:
        body = "".join(frags)
        if not body.lstrip().startswith("services:"):
            pass
    header = (
        f"# ET sandbox compose for artifact={artifact_id}\n"
        f"# ports http={alloc.get('http')} db={alloc.get('db')} "
        f"aux={alloc.get('aux')}\n"
        "# stub generator — full engine later; doctrine: plugins fire together\n"
        "\n"
        "services:\n"
    )
    networks = (
        "\nnetworks:\n"
        "  default:\n"
        f"    name: et-{artifact_id}\n"
    )
    # avoid double 'services:' if fragment already includes it
    if body.lstrip().startswith("services:"):
        return (
            f"# ET sandbox compose for artifact={artifact_id}\n"
            f"# ports http={alloc.get('http')} db={alloc.get('db')} "
            f"aux={alloc.get('aux')}\n"
            "# stub generator — full engine later\n\n"
            + body
            + networks
        )
    return header + body + networks


def cmd_sandbox(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else _repo_root()
    paths = trail.ensure_layout(root)
    action = args.sandbox_action
    artifact_id = args.artifact or "default"
    art_dir = paths["artifacts"] / artifact_id
    if action == "ports":
        data = json.loads((paths["sandbox"] / "ports.json").read_text(encoding="utf-8"))
        print(json.dumps(data, indent=2))
        return 0
    if action == "plan":
        art_dir.mkdir(parents=True, exist_ok=True)
        alloc = _allocate_ports(paths["sandbox"], artifact_id)
        compose = _compose_from_plugins(root, artifact_id, alloc)
        out = art_dir / "compose.yml"
        out.write_text(compose, encoding="utf-8")
        print(f"SANDBOX plan artifact={artifact_id} compose={out}")
        print(f"PORTS {json.dumps(alloc)}")
        return 0
    if action == "up":
        compose = art_dir / "compose.yml"
        if not compose.is_file():
            print("SANDBOX FAIL: no compose — run: emperor sandbox plan", file=sys.stderr)
            return 1
        print(f"SANDBOX up stub artifact={artifact_id} compose={compose}")
        print("NOTE: docker compose up not executed in v1 stub")
        return 0
    if action == "down":
        print(f"SANDBOX down stub artifact={artifact_id}")
        print("NOTE: docker compose down not executed in v1 stub")
        return 0
    print(f"SANDBOX FAIL: unknown action {action}", file=sys.stderr)
    return 1


def cmd_artifacts(args: argparse.Namespace) -> int:
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
            print(f"  {a}")
        return 0
    if action == "stub-create":
        aid = args.artifact or "task-stub"
        dest = paths["artifacts"] / aid
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "README.md").write_text(
            f"# Artifact `{aid}`\n\nMulti-repo worktrees + compose live here.\n",
            encoding="utf-8",
        )
        print(f"ARTIFACTS stub-create id={aid} path={dest}")
        return 0
    print(f"ARTIFACTS FAIL: unknown action {action}", file=sys.stderr)
    return 1



def cmd_runtime(args: argparse.Namespace) -> int:
    """Pluggable runtime: use compose|podman|k8s."""
    root = Path(args.root).resolve() if args.root else _repo_root()
    paths = trail.ensure_layout(root)
    action = args.runtime_action
    active_path = paths["runtime"] / "active"
    if action == "use":
        choice = (args.backend or "").strip()
        if choice not in ("compose", "podman", "k8s"):
            print("RUNTIME FAIL: use compose|podman|k8s", file=sys.stderr)
            return 1
        active_path.write_text(choice + "\n", encoding="utf-8")
        print(f"RUNTIME use backend={choice}")
        print(f"EMITTER dir={paths['runtime'] / choice}")
        return 0
    if action == "status":
        cur = active_path.read_text(encoding="utf-8").strip() if active_path.is_file() else "compose"
        print(f"RUNTIME status backend={cur}")
        for name in ("compose", "podman", "k8s"):
            mark = "*" if name == cur else " "
            print(f"  [{mark}] {name} -> {paths['runtime'] / name}")
        return 0
    print(f"RUNTIME FAIL: unknown action {action}", file=sys.stderr)
    return 1


def _redact_env_lines(raw: str) -> list[str]:
    out = []
    for line in raw.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            out.append(line)
            continue
        if "=" in line:
            k, _, _v = line.partition("=")
            out.append(f"{k}=***REDACTED***")
        else:
            out.append(line)
    return out


def cmd_env(args: argparse.Namespace) -> int:
    """Unified workspace env — show (redacted) | sync stub."""
    root = Path(args.root).resolve() if args.root else _repo_root()
    paths = trail.ensure_layout(root)
    action = args.env_action
    env_dir = paths["env"]
    example = env_dir / "workspace.env.example"
    managed = env_dir / "workspace.env"
    if action == "show":
        print("ENV show scope=workspace (redacted; repo≠workspace)")
        print(f"  example={example}")
        if managed.is_file():
            print("  --- workspace.env (redacted) ---")
            for line in _redact_env_lines(managed.read_text(encoding="utf-8", errors="replace")):
                print(f"  {line}")
        else:
            print("  workspace.env=(absent — copy from example; secrets via broker)")
        overlays = env_dir / "overlays"
        if overlays.is_dir():
            for ov in sorted(overlays.glob("*.env")):
                print(f"  overlay={ov.name} (redacted)")
                for line in _redact_env_lines(ov.read_text(encoding="utf-8", errors="replace"))[:20]:
                    print(f"    {line}")
        return 0
    if action == "sync":
        # merge example keys into managed without copying secret-looking values
        if not managed.exists() and example.exists():
            managed.write_text(example.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"ENV sync created {managed} from example (no secrets)")
        else:
            print(f"ENV sync stub managed={managed}")
        print("NOTE: plugin overlay merge is stub — ET owns workspace env merge")
        return 0
    print(f"ENV FAIL: unknown action {action}", file=sys.stderr)
    return 1


def cmd_secrets(args: argparse.Namespace) -> int:
    """Blind credentials — list names / inject without plaintext to stdout."""
    root = Path(args.root).resolve() if args.root else _repo_root()
    paths = trail.ensure_layout(root)
    action = args.secrets_action
    man_path = paths["secrets"] / "manifest.json"
    data = json.loads(man_path.read_text(encoding="utf-8"))
    if action == "list":
        names = data.get("names") or []
        print(f"SECRETS list broker={data.get('broker', '?')} n={len(names)}")
        for n in names:
            # status only — never values
            print(f"  name={n} status=declared")
        if not names:
            print("  (none — register names in .emperor/secrets/manifest.json)")
        print("IRON: agent must never read plaintext secret values")
        return 0
    if action == "inject":
        names = data.get("names") or []
        target = args.artifact or "default"
        # Honest stub: write a broker receipt WITHOUT values
        receipt = paths["secrets"] / f"inject-{target}.receipt.json"
        receipt.write_text(
            json.dumps(
                {
                    "artifact": target,
                    "broker": data.get("broker", "env-file"),
                    "injected_names": names,
                    "plaintext_to_stdout": False,
                    "stub": True,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"SECRETS inject artifact={target} names={len(names)} receipt={receipt}")
        print("NOTE: broker stub — values not fetched; plaintext withheld from agent")
        return 0
    if action == "declare":
        # register a name only
        name = (args.name or "").strip()
        if not name:
            print("SECRETS FAIL: declare needs --name", file=sys.stderr)
            return 1
        names = list(data.get("names") or [])
        if name not in names:
            names.append(name)
        data["names"] = names
        man_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        print(f"SECRETS declare name={name} (value never accepted on CLI)")
        return 0
    print(f"SECRETS FAIL: unknown action {action}", file=sys.stderr)
    return 1



def build_parser() -> argparse.ArgumentParser:
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument("--root", default="", help="repo root (default: detect)")
    parent.add_argument("--db", default="", help="graph.sqlite path")

    p = argparse.ArgumentParser(
        prog="super_context",
        description="Emperor Time super-context / thoughttrail / sandbox stubs",
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

    sb = sub.add_parser("sandbox", help="sandbox plan|up|down|ports stubs", parents=[parent])
    sb.add_argument(
        "sandbox_action",
        choices=["plan", "up", "down", "ports"],
    )
    sb.add_argument("--artifact", default="default")

    ar = sub.add_parser("artifacts", help="artifacts list|stub-create", parents=[parent])
    ar.add_argument(
        "artifacts_action",
        choices=["list", "stub-create"],
    )
    ar.add_argument("--artifact", default="")

    rt = sub.add_parser("runtime", help="runtime use|status (compose|podman|k8s)", parents=[parent])
    rt.add_argument("runtime_action", choices=["use", "status"])
    rt.add_argument("backend", nargs="?", default="", help="compose|podman|k8s for use")

    ev = sub.add_parser("env", help="workspace env show|sync (redacted)", parents=[parent])
    ev.add_argument("env_action", choices=["show", "sync"])

    sec = sub.add_parser("secrets", help="blind creds list|inject|declare", parents=[parent])
    sec.add_argument("secrets_action", choices=["list", "inject", "declare"])
    sec.add_argument("--name", default="", help="declare name only (no value)")
    sec.add_argument("--artifact", default="default")

    return p



def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        return _print_card()
    parser = build_parser()
    args = parser.parse_args(argv)
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
