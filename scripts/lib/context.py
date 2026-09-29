#!/usr/bin/env python3
"""Emperor Time thoughttrail + super-context CLI (Python core).

Clean-room virtual context: deterministic MD structural graph (no embeddings,
no Graphify vendor copy) under .emperor/context/, append-only reasoning index
under .emperor/thoughttrail/.

Commands:
  build [root]              extract MD → SQLite graph + L0 god-map
  query <term> [root]       L1 find nodes
  path <a> <b> [root]       L1 shortest path
  explain <term> [root]     L1 node explain (+ optional L2 cite slices)
  trail append <text> ...   append thoughttrail entry
  trail list [root]         list recent trail entries
  trail link <id> <nodes…>  attach graph node ids to an entry
  layout [root]             ensure inverted workspace dirs (SOT/artifacts/…)

Always-fail HARD-GATE helpers:
  --reject-no-graph         refuse CONTEXT READY without built graph
  --reject-no-trail         refuse thoughttrail claim without index

Check mode:
  --check-context PATH      task dir / repo root / .emperor/context
                            (exit 1 when activity claimed but graph soft/missing)
  --check-trail PATH        task dir / repo root / thoughttrail dir
                            (exit 1 when activity claimed but trail soft/missing)

Vacuous PASS when no super-context / thoughttrail activity is claimed.
Thin twins: scripts/context.sh / scripts/context.ps1
Doctrine: references/super-context.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Sequence
from check_report import report_check

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

import context_store as store
import thoughttrail as trail

LEAF = "references/super-context.md"

_CONTEXT_SIGNAL = re.compile(
    r"(?i)\b("
    r"super-?context"
    r"|thoughttrail"
    r"|CONTEXT\s+READY"
    r"|emperor\s+context"
    r"|L0\s+god[- ]?map"
    r"|context\s+build"
    r"|virtual\s+context"
    r"|\.emperor/context"
    r"|\.emperor/thoughttrail"
    r")\b"
)

_TRAIL_SIGNAL = re.compile(
    r"(?i)\b("
    r"thoughttrail"
    r"|trail\s+append"
    r"|reasoning\s+index"
    r"|\.emperor/thoughttrail"
    r")\b"
)

_GRAPH_SIGNAL = re.compile(
    r"(?i)\b("
    r"super-?context"
    r"|CONTEXT\s+READY"
    r"|emperor\s+context\s+build"
    r"|L0\s+god[- ]?map"
    r"|context\s+build"
    r"|virtual\s+context"
    r"|\.emperor/context"
    r")\b"
)


def _repo_of(path: Path) -> Path:
    """Resolve a repo root from task dir / .emperor/* / bare root."""
    p = path.resolve()
    if p.is_file():
        p = p.parent
    # If pointing at .emperor/context or thoughttrail, climb
    parts = list(p.parts)
    if ".emperor" in parts:
        idx = parts.index(".emperor")
        return Path(*parts[:idx]) if idx > 0 else p
    # task dir with ledger → parent parents until .emperor sibling or cwd marker
    if (p / ".emperor").is_dir() or (p / "SKILL.md").is_file():
        return p
    if (p / "ledger.md").is_file():
        # task dir — repo is often two up from .emperor/tasks/<id>
        for cand in (p.parent, p.parent.parent, p.parent.parent.parent):
            if (cand / ".emperor").is_dir() or (cand / "SKILL.md").is_file():
                return cand
        return p.parent
    return p


def _read_activity_text(path: Path) -> str:
    p = path.resolve()
    chunks: list[str] = []
    if p.is_file():
        chunks.append(p.read_text(encoding="utf-8", errors="replace"))
        return "\n".join(chunks)
    for name in (
        "ledger.md",
        "claims.md",
        "CLAIM.md",
        "work-order.md",
        "CONTEXT.md",
    ):
        f = p / name
        if f.is_file():
            chunks.append(f.read_text(encoding="utf-8", errors="replace"))
    # Root markdown claims (bounded)
    if p.is_dir():
        for f in sorted(p.glob("*.md")):
            if f.stat().st_size < 200_000:
                chunks.append(f.read_text(encoding="utf-8", errors="replace"))
    # also scan .emperor marker files under path
    emp = p / ".emperor"
    if emp.is_dir():
        for f in emp.rglob("*.md"):
            if f.stat().st_size < 200_000:
                chunks.append(f.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(chunks)


def format_card() -> str:
    lines = [
        "CONTEXT checklist=yes",
        f"CONTEXT leaf={LEAF}",
        "CONTEXT iron=GRAPH_THEN_TRAIL",
        "STEP 1 id=build name=Build deterministic MD graph "
        "et=headings/links/code/ADR → SQLite + L0",
        "STEP 1 key=No embeddings; EXTRACTED vs INFERRED tagged",
        "STEP 2 id=query name=L1 query|find|path|explain|l0|slice "
        "et=find / shortest path / degree neighbors",
        "STEP 2 key=L2 cite slices only when asked (path:line)",
        "STEP 3 id=trail name=Append thoughttrail "
        "et=.emperor/thoughttrail/trail.jsonl linked to node ids",
        "STEP 3 key=Append-only reasoning index; not a chat log dump",
        "STEP 4 id=sot name=Inverted workspace "
        "et=SOT fetch-only; RT from artifact copies",
        "STEP 4 key=Never mutate SOT; clones produce SDLC-tested PRs",
        "",
        "MUST: Before claiming CONTEXT READY / thoughttrail done, run "
        "scripts/emperor context build and ensure trail.jsonl exists. "
        f"Open {LEAF}; run scripts/emperor context --check-context <root>.",
        "MUST-NOT: claim super-context without graph.sqlite + l0.md; "
        "claim thoughttrail without trail.jsonl; copy Graphify vendor code; "
        "add embeddings.",
    ]
    return "\n".join(lines) + "\n"


def reject_no_graph() -> str:
    return (
        "REJECT NO GRAPH: HARD-GATE — super-context refuses CONTEXT READY "
        "without .emperor/context/graph.sqlite + l0.md. "
        f"Open {LEAF}; run scripts/emperor context build.\n"
    )


def reject_no_trail() -> str:
    return (
        "REJECT NO TRAIL: HARD-GATE — thoughttrail refuses 'done' without "
        "append-only .emperor/thoughttrail/trail.jsonl. "
        f"Open {LEAF}; run scripts/emperor context trail append ….\n"
    )


def _graph_errors(repo: Path) -> list[str]:
    db = store.default_db_path(repo)
    l0 = store.default_l0_path(repo)
    errs: list[str] = []
    if not db.is_file():
        errs.append("missing .emperor/context/graph.sqlite")
    else:
        try:
            conn = store.connect(db)
            try:
                n = conn.execute("SELECT COUNT(*) c FROM nodes").fetchone()["c"]
                if n < 1:
                    errs.append("graph.sqlite has zero nodes (empty theater)")
            finally:
                conn.close()
        except Exception as exc:  # noqa: BLE001
            errs.append(f"graph.sqlite unreadable: {exc}")
    if not l0.is_file():
        errs.append("missing .emperor/context/l0.md god-map")
    else:
        text = l0.read_text(encoding="utf-8", errors="replace")
        if "L0" not in text and "god" not in text.lower():
            errs.append("l0.md missing L0 / god-map markers")
        if len(text.strip()) < 40:
            errs.append("l0.md too short (theater)")
    return errs


def _trail_errors(repo: Path) -> list[str]:
    path = trail.default_trail_path(repo)
    errs: list[str] = []
    if not path.is_file():
        errs.append("missing .emperor/thoughttrail/trail.jsonl")
        return errs
    raw = path.read_text(encoding="utf-8", errors="replace")
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    if not lines:
        errs.append("trail.jsonl empty (no append-only entries)")
        return errs
    ok = 0
    for ln in lines:
        try:
            obj = json.loads(ln)
        except json.JSONDecodeError:
            errs.append("trail.jsonl has non-JSON line")
            continue
        if not obj.get("text") or not obj.get("id") or not obj.get("ts"):
            errs.append("trail entry missing id/ts/text")
        else:
            ok += 1
    if ok < 1:
        errs.append("trail.jsonl has no valid entries")
    return errs



def _context_vacuous(path: Path) -> bool:
    """True when --check-context would idle-skip (no graph activity claimed)."""
    if not path.exists():
        return False
    text = _read_activity_text(path)
    p = path.resolve()
    if p.name == "context" and p.parent.name == ".emperor":
        return False
    if p.name == "graph.sqlite" or (p.is_dir() and (p / "graph.sqlite").is_file()):
        return False
    if not _GRAPH_SIGNAL.search(text) and not _CONTEXT_SIGNAL.search(text):
        return True
    if _TRAIL_SIGNAL.search(text) and not _GRAPH_SIGNAL.search(text):
        if not re.search(
            r"(?i)super-?context|CONTEXT\s+READY|context\s+build|L0", text
        ):
            return True
    return False


def _trail_vacuous(path: Path) -> bool:
    """True when --check-trail would idle-skip (no trail activity claimed)."""
    if not path.exists():
        return False
    text = _read_activity_text(path)
    p = path.resolve()
    if p.name == "thoughttrail" and p.parent.name == ".emperor":
        return False
    if p.name == "trail.jsonl":
        return False
    if not _TRAIL_SIGNAL.search(text) and not _CONTEXT_SIGNAL.search(text):
        return True
    if _GRAPH_SIGNAL.search(text) and not _TRAIL_SIGNAL.search(text):
        return True
    return False

def validate_context(path: Path) -> list[str]:
    """SKIP (vacuous — no activity) when no graph activity claimed."""
    text = _read_activity_text(path)
    # Direct pointer at context dir / db → always validate
    p = path.resolve()
    forced = False
    if p.name == "context" and p.parent.name == ".emperor":
        forced = True
        repo = _repo_of(p)
    elif p.name == "graph.sqlite" or (p.is_dir() and (p / "graph.sqlite").is_file()):
        forced = True
        repo = _repo_of(p)
    else:
        repo = _repo_of(p)
        if not _GRAPH_SIGNAL.search(text) and not _CONTEXT_SIGNAL.search(text):
            return []
        # trail-only claim without graph claim → vacuous for graph check
        if _TRAIL_SIGNAL.search(text) and not _GRAPH_SIGNAL.search(text):
            if not _GRAPH_SIGNAL.search(text) and "CONTEXT READY" not in text.upper():
                # still run if super-context mentioned via CONTEXT_SIGNAL
                if not re.search(r"(?i)super-?context|CONTEXT\s+READY|context\s+build|L0", text):
                    return []
    return _graph_errors(repo)


def validate_trail(path: Path) -> list[str]:
    text = _read_activity_text(path)
    p = path.resolve()
    if p.name == "thoughttrail" and p.parent.name == ".emperor":
        repo = _repo_of(p)
        return _trail_errors(repo)
    if p.name == "trail.jsonl":
        repo = _repo_of(p)
        return _trail_errors(repo)
    repo = _repo_of(p)
    if not _TRAIL_SIGNAL.search(text) and not _CONTEXT_SIGNAL.search(text):
        return []
    # If only graph claimed without trail markers, vacuous for trail
    if _GRAPH_SIGNAL.search(text) and not _TRAIL_SIGNAL.search(text):
        return []
    return _trail_errors(repo)


def cmd_build(root: Path, *, force: bool = False) -> int:
    trail.ensure_layout(root)
    stats = store.build(root, force=force)
    l0 = store.write_l0(store.default_db_path(root), store.default_l0_path(root))
    print(
        f"context build PASS: scanned={stats['scanned']} updated={stats['updated']} "
        f"skipped={stats['skipped']} nodes={stats['nodes']} edges={stats['edges']}"
    )
    print(f"context L0: {l0}")
    print(f"context DB: {stats['db']}")
    return 0


def cmd_query(root: Path, term: str, *, limit: int = 20) -> int:
    db = store.default_db_path(root)
    if not db.is_file():
        print("context query FAIL: no graph — run context build", file=sys.stderr)
        return 1
    hits = store.find_nodes(db, term, limit=limit)
    if not hits:
        print(f"context query: no hits for {term!r}")
        return 0
    for h in hits:
        print(
            f"{h['id'][:12]}  [{h['kind']}] {h['label']}  "
            f"{h.get('source_path') or ''}:{h.get('line_start') or ''}"
        )
    return 0


def cmd_path(root: Path, a: str, b: str) -> int:
    db = store.default_db_path(root)
    if not db.is_file():
        print("context path FAIL: no graph — run context build", file=sys.stderr)
        return 1
    chain = store.shortest_path(db, a, b)
    if not chain:
        print(f"context path: no path between {a!r} and {b!r}", file=sys.stderr)
        return 1
    for i, n in enumerate(chain):
        print(f"{i}: [{n['kind']}] {n['label']} ({n.get('source_path') or n['id']})")
    return 0


def cmd_explain(root: Path, term: str, *, cite: bool = False) -> int:
    db = store.default_db_path(root)
    if not db.is_file():
        print("context explain FAIL: no graph — run context build", file=sys.stderr)
        return 1
    info = store.explain_node(db, term)
    if not info:
        print(f"context explain: no node for {term!r}", file=sys.stderr)
        return 1
    n = info["node"]
    print(f"node: [{n['kind']}] {n['label']} id={n['id']}")
    print(f"source: {n.get('source_path')}:{n.get('line_start')}-{n.get('line_end')}")
    print(f"degree: {info['degree']}")
    for e in info["edges"][:30]:
        print(
            f"  {e['relation']} ({e['confidence']}): "
            f"{e['src_label']} → {e['dst_label']}"
        )
    if cite:
        print("L2 cites:")
        for line in store.slice_cite(db, term):
            print(f"  {line}")
    return 0


def cmd_trail_append(root: Path, text: str, node_ids: list[str], ledger: str, task: str) -> int:
    entry = trail.append_entry(
        root, text, node_ids=node_ids, ledger=ledger, task=task
    )
    print(f"trail append PASS: id={entry['id']} ts={entry['ts']}")
    return 0


def cmd_trail_list(root: Path, *, limit: int = 20, node_id: str = "") -> int:
    rows = trail.list_entries(root, limit=limit, node_id=node_id)
    if not rows:
        print("trail list: (empty)")
        return 0
    for r in rows:
        nodes = ",".join(r.get("node_ids") or []) or "-"
        print(f"{r.get('ts')}  {r.get('id')}  nodes={nodes}  {r.get('text')}")
    return 0


def cmd_trail_link(root: Path, entry_id: str, node_ids: list[str]) -> int:
    updated = trail.link_nodes(root, entry_id, node_ids)
    if updated is None:
        print(f"trail link FAIL: entry {entry_id!r} not found", file=sys.stderr)
        return 1
    print(f"trail link PASS: id={entry_id} nodes={updated.get('node_ids')}")
    return 0


def cmd_layout(root: Path) -> int:
    paths = trail.ensure_layout(root)
    for k, p in paths.items():
        print(f"layout {k}: {p}")
    return 0



EXTENDED_CMDS = {
    "find", "l0", "slice", "sot", "sandbox", "artifacts",
    "runtime", "env", "secrets",
}


def _forward_super(argv: list[str]) -> int:
    """Delegate sot/sandbox/runtime/env/secrets (+find/l0/slice aliases) to super_context."""
    import super_context as sc

    # map find → find (same); context uses query, super uses find
    return sc.main(argv)


def main(argv: Sequence[str] | None = None) -> int:
    argv = list(argv) if argv is not None else sys.argv[1:]

    # Forward stub / extra tier commands before local argparse
    if argv and argv[0] in EXTENDED_CMDS:
        return _forward_super(argv)

    # Pre-parse hard-gates that may appear anywhere
    if "--reject-no-graph" in argv:
        sys.stdout.write(reject_no_graph())
        return 1
    if "--reject-no-trail" in argv:
        sys.stdout.write(reject_no_trail())
        return 1

    p = argparse.ArgumentParser(
        prog="context.py",
        description="Emperor Time thoughttrail + super-context (Python core)",
    )
    p.add_argument(
        "--check-context",
        type=Path,
        metavar="PATH",
        default=None,
        help="validate super-context graph when activity claimed",
    )
    p.add_argument(
        "--check-trail",
        type=Path,
        metavar="PATH",
        default=None,
        help="validate thoughttrail when activity claimed",
    )
    p.add_argument(
        "--reject-no-graph",
        action="store_true",
        help="Hard-gate: refuse missing graph (exit 1)",
    )
    p.add_argument(
        "--reject-no-trail",
        action="store_true",
        help="Hard-gate: refuse missing trail (exit 1)",
    )

    sub = p.add_subparsers(dest="cmd")

    b = sub.add_parser("build", help="build/update MD → SQLite graph + L0")
    b.add_argument("root", type=Path, nargs="?", default=Path("."))
    b.add_argument("--force", action="store_true")

    q = sub.add_parser("query", help="L1 find nodes")
    q.add_argument("term")
    q.add_argument("root", type=Path, nargs="?", default=Path("."))
    q.add_argument("--limit", type=int, default=20)

    pa = sub.add_parser("path", help="L1 shortest path")
    pa.add_argument("a")
    pa.add_argument("b")
    pa.add_argument("root", type=Path, nargs="?", default=Path("."))

    ex = sub.add_parser("explain", help="L1 explain node")
    ex.add_argument("term")
    ex.add_argument("root", type=Path, nargs="?", default=Path("."))
    ex.add_argument("--cite", action="store_true", help="include L2 path:line slices")

    tr = sub.add_parser("trail", help="thoughttrail append/list/link")
    tr_sub = tr.add_subparsers(dest="trail_cmd")
    ta = tr_sub.add_parser("append")
    ta.add_argument("text")
    ta.add_argument("root", type=Path, nargs="?", default=Path("."))
    ta.add_argument("--node", action="append", default=[], dest="nodes")
    ta.add_argument("--ledger", default="")
    ta.add_argument("--task", default="")
    tl = tr_sub.add_parser("list")
    tl.add_argument("root", type=Path, nargs="?", default=Path("."))
    tl.add_argument("--limit", type=int, default=20)
    tl.add_argument("--node", default="", dest="node_id")
    tk = tr_sub.add_parser("link")
    tk.add_argument("entry_id")
    tk.add_argument("nodes", nargs="+")
    tk.add_argument("root", type=Path, nargs="?", default=Path("."))

    ly = sub.add_parser("layout", help="ensure inverted workspace dirs")
    ly.add_argument("root", type=Path, nargs="?", default=Path("."))

    # No args → card
    if not argv:
        sys.stdout.write(format_card())
        return 0

    args = p.parse_args(argv)

    if args.reject_no_graph:
        sys.stdout.write(reject_no_graph())
        return 1
    if args.reject_no_trail:
        sys.stdout.write(reject_no_trail())
        return 1

    if args.check_context is not None:
        target = args.check_context
        errs = validate_context(target)
        vacuous = _context_vacuous(target)
        return report_check("context", target, errs, vacuous=vacuous)

    if args.check_trail is not None:
        target = args.check_trail
        errs = validate_trail(target)
        vacuous = _trail_vacuous(target)
        return report_check("trail", target, errs, vacuous=vacuous)

    if args.cmd is None:
        sys.stdout.write(format_card())
        return 0

    if args.cmd == "build":
        return cmd_build(args.root.resolve(), force=args.force)
    if args.cmd == "query":
        return cmd_query(args.root.resolve(), args.term, limit=args.limit)
    if args.cmd == "path":
        return cmd_path(args.root.resolve(), args.a, args.b)
    if args.cmd == "explain":
        return cmd_explain(args.root.resolve(), args.term, cite=args.cite)
    if args.cmd == "layout":
        return cmd_layout(args.root.resolve())
    if args.cmd == "trail":
        if args.trail_cmd == "append":
            return cmd_trail_append(
                args.root.resolve(),
                args.text,
                list(args.nodes or []),
                args.ledger,
                args.task,
            )
        if args.trail_cmd == "list":
            return cmd_trail_list(
                args.root.resolve(), limit=args.limit, node_id=args.node_id
            )
        if args.trail_cmd == "link":
            # root may be last positional overlapping nodes — handle path-like last
            nodes = list(args.nodes)
            root = args.root.resolve()
            if nodes and Path(nodes[-1]).exists() and (Path(nodes[-1]) / ".emperor").exists():
                root = Path(nodes.pop()).resolve()
            return cmd_trail_link(root, args.entry_id, nodes)
        print("usage: context trail append|list|link …", file=sys.stderr)
        return 2

    print(f"unknown command: {args.cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
