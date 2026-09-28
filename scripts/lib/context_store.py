#!/usr/bin/env python3
"""SQLite graph store for Emperor Time super-context.

Build/update/query a local graph DB under .emperor/context/graph.sqlite.
Content-hash cache skips unchanged Markdown files. Stdlib + sqlite3 only.
No embeddings. No NetworkX.
"""
from __future__ import annotations

import json
import sqlite3
from collections import defaultdict, deque
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in __import__('sys').path:
    __import__('sys').path.insert(0, str(_LIB))

from md_graph import (
    CONF_EXTRACTED,
    CONF_INFERRED,
    Edge,
    Node,
    extract_file,
    extract_tree,
    iter_md_files,
    resolve_inferences,
)

SCHEMA = """
CREATE TABLE IF NOT EXISTS files (
  path TEXT PRIMARY KEY,
  content_hash TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS nodes (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  label TEXT NOT NULL,
  source_path TEXT,
  line_start INTEGER,
  line_end INTEGER,
  meta TEXT
);
CREATE TABLE IF NOT EXISTS edges (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  src TEXT NOT NULL,
  dst TEXT NOT NULL,
  relation TEXT NOT NULL,
  confidence TEXT NOT NULL,
  source_path TEXT,
  UNIQUE(src, dst, relation)
);
CREATE TABLE IF NOT EXISTS meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_nodes_label ON nodes(label);
CREATE INDEX IF NOT EXISTS idx_nodes_kind ON nodes(kind);
CREATE INDEX IF NOT EXISTS idx_edges_src ON edges(src);
CREATE INDEX IF NOT EXISTS idx_edges_dst ON edges(dst);
"""


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def default_db_path(repo_root: Path) -> Path:
    return repo_root / ".emperor" / "context" / "graph.sqlite"


def default_l0_path(repo_root: Path) -> Path:
    return repo_root / ".emperor" / "context" / "l0.md"


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def _upsert_node(conn: sqlite3.Connection, n: Node) -> None:
    conn.execute(
        """
        INSERT INTO nodes(id, kind, label, source_path, line_start, line_end, meta)
        VALUES(?,?,?,?,?,?,?)
        ON CONFLICT(id) DO UPDATE SET
          kind=excluded.kind,
          label=excluded.label,
          source_path=excluded.source_path,
          line_start=excluded.line_start,
          line_end=excluded.line_end,
          meta=excluded.meta
        """,
        (
            n.id,
            n.kind,
            n.label,
            n.source_path,
            n.line_start,
            n.line_end,
            json.dumps(n.meta or {}, sort_keys=True),
        ),
    )


def _upsert_edge(conn: sqlite3.Connection, e: Edge) -> None:
    conn.execute(
        """
        INSERT INTO edges(src, dst, relation, confidence, source_path)
        VALUES(?,?,?,?,?)
        ON CONFLICT(src, dst, relation) DO UPDATE SET
          confidence=excluded.confidence,
          source_path=excluded.source_path
        """,
        (e.src, e.dst, e.relation, e.confidence, e.source_path),
    )


def _clear_file_graph(conn: sqlite3.Connection, rel: str) -> None:
    """Remove nodes/edges owned by a file path (except shared cite nodes)."""
    rows = conn.execute(
        "SELECT id, kind FROM nodes WHERE source_path = ?", (rel,)
    ).fetchall()
    for row in rows:
        if row["kind"] == "cite":
            continue
        nid = row["id"]
        conn.execute("DELETE FROM edges WHERE src = ? OR dst = ?", (nid, nid))
        conn.execute("DELETE FROM nodes WHERE id = ?", (nid,))
    # drop dangling contains/cites edges from this file
    conn.execute("DELETE FROM edges WHERE source_path = ?", (rel,))


def build(
    repo_root: Path,
    db_path: Path | None = None,
    *,
    force: bool = False,
) -> dict:
    """Build or incrementally update the graph. Returns build stats."""
    repo_root = repo_root.resolve()
    db_path = db_path or default_db_path(repo_root)
    conn = connect(db_path)
    scanned = 0
    updated = 0
    skipped = 0
    try:
        for path in iter_md_files(repo_root):
            scanned += 1
            rel = path.resolve().relative_to(repo_root).as_posix()
            sl = extract_file(path, repo_root)
            row = conn.execute(
                "SELECT content_hash FROM files WHERE path = ?", (rel,)
            ).fetchone()
            if (
                not force
                and row
                and row["content_hash"] == sl.content_hash
            ):
                skipped += 1
                continue
            _clear_file_graph(conn, rel)
            for n in sl.nodes:
                _upsert_node(conn, n)
            for e in sl.edges:
                _upsert_edge(conn, e)
            conn.execute(
                """
                INSERT INTO files(path, content_hash, updated_at)
                VALUES(?,?,?)
                ON CONFLICT(path) DO UPDATE SET
                  content_hash=excluded.content_hash,
                  updated_at=excluded.updated_at
                """,
                (rel, sl.content_hash, _utc()),
            )
            updated += 1

        # Recompute INFERRED resolve edges across current link+file nodes
        conn.execute("DELETE FROM edges WHERE confidence = ? AND relation = ?",
                     (CONF_INFERRED, "resolves_to"))
        # Lightweight re-extract for inference only from DB state is hard;
        # re-run resolve over fresh slices for updated corpus.
        nodes, edges, _hashes = extract_tree(repo_root)
        # Sync any missing inferred
        for e in edges:
            if e.confidence == CONF_INFERRED:
                _upsert_edge(conn, e)
        # Ensure all EXTRACTED from full tree exist (first build / force)
        if force or updated == scanned:
            for n in nodes:
                _upsert_node(conn, n)
            for e in edges:
                _upsert_edge(conn, e)

        conn.execute(
            "INSERT INTO meta(key, value) VALUES('built_at', ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (_utc(),),
        )
        conn.commit()
        n_nodes = conn.execute("SELECT COUNT(*) c FROM nodes").fetchone()["c"]
        n_edges = conn.execute("SELECT COUNT(*) c FROM edges").fetchone()["c"]
    finally:
        conn.close()
    return {
        "db": str(db_path),
        "scanned": scanned,
        "updated": updated,
        "skipped": skipped,
        "nodes": n_nodes,
        "edges": n_edges,
    }


def find_nodes(
    db_path: Path, query: str, *, limit: int = 20
) -> list[dict]:
    conn = connect(db_path)
    try:
        q = f"%{query}%"
        rows = conn.execute(
            """
            SELECT id, kind, label, source_path, line_start, line_end, meta
            FROM nodes
            WHERE label LIKE ? OR id LIKE ? OR source_path LIKE ?
            ORDER BY
              CASE kind WHEN 'heading' THEN 0 WHEN 'file' THEN 1
                        WHEN 'cite' THEN 2 ELSE 3 END,
              length(label)
            LIMIT ?
            """,
            (q, q, q, limit),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def _neighbors(conn: sqlite3.Connection, nid: str) -> list[sqlite3.Row]:
    return conn.execute(
        """
        SELECT e.src, e.dst, e.relation, e.confidence, e.source_path,
               ns.label AS src_label, nd.label AS dst_label,
               ns.kind AS src_kind, nd.kind AS dst_kind
        FROM edges e
        JOIN nodes ns ON ns.id = e.src
        JOIN nodes nd ON nd.id = e.dst
        WHERE e.src = ? OR e.dst = ?
        """,
        (nid, nid),
    ).fetchall()


def explain_node(db_path: Path, query: str) -> dict | None:
    hits = find_nodes(db_path, query, limit=1)
    if not hits:
        # exact id
        conn = connect(db_path)
        try:
            row = conn.execute(
                "SELECT id, kind, label, source_path, line_start, line_end, meta "
                "FROM nodes WHERE id = ?",
                (query,),
            ).fetchone()
            if not row:
                return None
            hit = dict(row)
        finally:
            conn.close()
    else:
        hit = hits[0]
    conn = connect(db_path)
    try:
        deg = conn.execute(
            "SELECT COUNT(*) c FROM edges WHERE src = ? OR dst = ?",
            (hit["id"], hit["id"]),
        ).fetchone()["c"]
        neigh = [dict(r) for r in _neighbors(conn, hit["id"])]
        return {"node": hit, "degree": deg, "edges": neigh}
    finally:
        conn.close()


def shortest_path(
    db_path: Path, a: str, b: str, *, max_depth: int = 8
) -> list[dict] | None:
    """BFS undirected path between two node queries/ids."""
    ha = find_nodes(db_path, a, limit=1)
    hb = find_nodes(db_path, b, limit=1)
    conn = connect(db_path)
    try:
        def resolve(q: str, hits: list[dict]) -> str | None:
            if hits:
                return hits[0]["id"]
            row = conn.execute(
                "SELECT id FROM nodes WHERE id = ?", (q,)
            ).fetchone()
            return row["id"] if row else None

        sa = resolve(a, ha)
        sb = resolve(b, hb)
        if not sa or not sb:
            return None
        if sa == sb:
            n = conn.execute(
                "SELECT id, kind, label FROM nodes WHERE id = ?", (sa,)
            ).fetchone()
            return [dict(n)] if n else None

        adj: dict[str, list[str]] = defaultdict(list)
        for row in conn.execute("SELECT src, dst FROM edges"):
            adj[row["src"]].append(row["dst"])
            adj[row["dst"]].append(row["src"])

        prev: dict[str, str | None] = {sa: None}
        q: deque[str] = deque([sa])
        found = False
        while q:
            cur = q.popleft()
            if cur == sb:
                found = True
                break
            depth = 0
            # compute depth via chain
            t = cur
            while prev[t] is not None:
                depth += 1
                t = prev[t]  # type: ignore[assignment]
                if depth > max_depth:
                    break
            if depth >= max_depth:
                continue
            for nxt in adj.get(cur, []):
                if nxt not in prev:
                    prev[nxt] = cur
                    q.append(nxt)
        if not found and sb not in prev:
            return None
        # reconstruct
        chain = [sb]
        while chain[-1] != sa:
            p = prev.get(chain[-1])
            if p is None:
                return None
            chain.append(p)
        chain.reverse()
        out = []
        for nid in chain:
            row = conn.execute(
                "SELECT id, kind, label, source_path FROM nodes WHERE id = ?",
                (nid,),
            ).fetchone()
            if row:
                out.append(dict(row))
        return out
    finally:
        conn.close()


def degree_summary(db_path: Path, *, top: int = 15) -> list[dict]:
    conn = connect(db_path)
    try:
        rows = conn.execute(
            """
            SELECT n.id, n.kind, n.label, n.source_path,
                   (SELECT COUNT(*) FROM edges e
                    WHERE e.src = n.id OR e.dst = n.id) AS degree
            FROM nodes n
            ORDER BY degree DESC, n.label
            LIMIT ?
            """,
            (top,),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def connected_components(db_path: Path) -> list[dict]:
    """Simple Union-Find components over undirected edges (file-centric labels)."""
    conn = connect(db_path)
    try:
        parent: dict[str, str] = {}

        def find(x: str) -> str:
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: str, b: str) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        ids = [r["id"] for r in conn.execute("SELECT id FROM nodes")]
        for i in ids:
            parent[i] = i
        for row in conn.execute("SELECT src, dst FROM edges"):
            union(row["src"], row["dst"])

        groups: dict[str, list[str]] = defaultdict(list)
        for i in ids:
            groups[find(i)].append(i)

        # label each community by highest-degree member label
        deg = {
            r["id"]: r["degree"]
            for r in degree_summary(db_path, top=10_000)
        }
        communities = []
        for root_id, members in groups.items():
            if len(members) < 2:
                continue
            best = max(members, key=lambda m: (deg.get(m, 0), m))
            row = conn.execute(
                "SELECT label, kind, source_path FROM nodes WHERE id = ?",
                (best,),
            ).fetchone()
            communities.append(
                {
                    "root": best,
                    "label": row["label"] if row else best,
                    "kind": row["kind"] if row else "?",
                    "size": len(members),
                    "sample_path": row["source_path"] if row else "",
                }
            )
        communities.sort(key=lambda c: (-c["size"], c["label"]))
        return communities
    finally:
        conn.close()


def write_l0(db_path: Path, out_path: Path, *, top: int = 15) -> Path:
    gods = degree_summary(db_path, top=top)
    communities = connected_components(db_path)[:20]
    lines = [
        "# L0 — super-context god map",
        "",
        f"Built: {_utc()}",
        "",
        "## Highest-degree nodes",
        "",
    ]
    for g in gods:
        lines.append(
            f"- deg={g['degree']} [{g['kind']}] {g['label']}"
            f" (`{g['source_path'] or g['id']}`)"
        )
    lines += ["", "## File communities (connected components)", ""]
    if not communities:
        lines.append("- (none — build the graph first)")
    for c in communities:
        lines.append(
            f"- size={c['size']} [{c['kind']}] {c['label']}"
            f" (`{c['sample_path'] or c['root']}`)"
        )
    lines.append("")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def slice_cite(db_path: Path, query: str) -> list[str]:
    """L2: path:line ranges for matching nodes (only when asked)."""
    hits = find_nodes(db_path, query, limit=30)
    out = []
    for h in hits:
        sp = h.get("source_path") or ""
        ls = h.get("line_start") or 0
        le = h.get("line_end") or ls
        if sp and ls:
            if le and le != ls:
                out.append(f"{sp}:{ls}-{le}  [{h['kind']}] {h['label']}")
            else:
                out.append(f"{sp}:{ls}  [{h['kind']}] {h['label']}")
    return out


__all__ = [
    "build",
    "connect",
    "default_db_path",
    "default_l0_path",
    "find_nodes",
    "explain_node",
    "shortest_path",
    "degree_summary",
    "connected_components",
    "write_l0",
    "slice_cite",
    "CONF_EXTRACTED",
    "CONF_INFERRED",
]
