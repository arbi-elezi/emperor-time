#!/usr/bin/env python3
"""Deterministic Markdown → graph extract (stdlib only).

First-principles structural extract for Emperor Time super-context.
Produces nodes + edges tagged EXTRACTED (explicit in source) or INFERRED
(resolved locally, e.g. relative link → existing file). No embeddings,
no NetworkX, no third-party parsers.

Extracts: file nodes, AT1–H6 headings, markdown links, wiki-ish [[refs]],
fenced code spans, ADR/RFC-ish cites.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Iterator, Sequence

CONF_EXTRACTED = "EXTRACTED"
CONF_INFERRED = "INFERRED"

_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_MD_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_WIKI = re.compile(r"\[\[([^\]]+)\]\]")
_FENCE = re.compile(r"^```([\w+-]*)\s*$")
_ADR = re.compile(r"\b(ADR[- ]?\d{1,4}|RFC\s?\d{3,5})\b", re.I)
_SKIP_DIRS = {
    ".git",
    ".emperor",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    ".tox",
    "dist",
    "build",
    ".worktrees",
}


@dataclass
class Node:
    id: str
    kind: str
    label: str
    source_path: str = ""
    line_start: int = 0
    line_end: int = 0
    meta: dict = field(default_factory=dict)


@dataclass
class Edge:
    src: str
    dst: str
    relation: str
    confidence: str
    source_path: str = ""


@dataclass
class GraphSlice:
    nodes: list[Node] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
    content_hash: str = ""


def _slug(text: str) -> str:
    s = re.sub(r"[^\w]+", "-", text.strip().lower()).strip("-")
    return s or "x"


def _nid(*parts: str) -> str:
    raw = "|".join(parts)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def iter_md_files(root: Path) -> Iterator[Path]:
    root = root.resolve()
    if root.is_file() and root.suffix.lower() in {".md", ".markdown", ".mdx"}:
        yield root
        return
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix.lower() not in {".md", ".markdown", ".mdx"}:
            continue
        if any(part in _SKIP_DIRS for part in p.parts):
            continue
        yield p


def extract_file(path: Path, root: Path) -> GraphSlice:
    text = path.read_text(encoding="utf-8", errors="replace")
    content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    rel = _rel(path, root)
    nodes: list[Node] = []
    edges: list[Edge] = []

    file_id = _nid("file", rel)
    nodes.append(
        Node(
            id=file_id,
            kind="file",
            label=rel,
            source_path=rel,
            line_start=1,
            line_end=text.count("\n") + 1,
            meta={"hash": content_hash},
        )
    )

    heading_stack: list[tuple[int, str, str]] = []  # level, id, label
    in_fence = False
    fence_lang = ""
    fence_start = 0
    fence_lines: list[str] = []

    lines = text.splitlines()
    for i, line in enumerate(lines, start=1):
        fence_m = _FENCE.match(line)
        if fence_m:
            if not in_fence:
                in_fence = True
                fence_lang = fence_m.group(1) or ""
                fence_start = i
                fence_lines = []
            else:
                body = "\n".join(fence_lines)
                preview = body.strip().splitlines()[:1]
                label = (preview[0][:80] if preview else f"code:{fence_lang or 'plain'}")
                code_id = _nid("code", rel, str(fence_start), label)
                nodes.append(
                    Node(
                        id=code_id,
                        kind="code",
                        label=label,
                        source_path=rel,
                        line_start=fence_start,
                        line_end=i,
                        meta={"lang": fence_lang, "chars": len(body)},
                    )
                )
                parent = heading_stack[-1][1] if heading_stack else file_id
                edges.append(
                    Edge(parent, code_id, "contains", CONF_EXTRACTED, rel)
                )
                in_fence = False
            continue
        if in_fence:
            fence_lines.append(line)
            continue

        hm = _HEADING.match(line)
        if hm:
            level = len(hm.group(1))
            label = hm.group(2).strip()
            hid = _nid("heading", rel, str(level), _slug(label), str(i))
            nodes.append(
                Node(
                    id=hid,
                    kind="heading",
                    label=label,
                    source_path=rel,
                    line_start=i,
                    line_end=i,
                    meta={"level": level, "slug": _slug(label)},
                )
            )
            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()
            parent = heading_stack[-1][1] if heading_stack else file_id
            edges.append(Edge(parent, hid, "contains", CONF_EXTRACTED, rel))
            heading_stack.append((level, hid, label))

        for m in _MD_LINK.finditer(line):
            text_label, target = m.group(1).strip(), m.group(2).strip()
            link_id = _nid("link", rel, str(i), target)
            nodes.append(
                Node(
                    id=link_id,
                    kind="link",
                    label=text_label or target,
                    source_path=rel,
                    line_start=i,
                    line_end=i,
                    meta={"target": target},
                )
            )
            parent = heading_stack[-1][1] if heading_stack else file_id
            edges.append(Edge(parent, link_id, "contains", CONF_EXTRACTED, rel))
            edges.append(
                Edge(link_id, file_id, "mentions_target", CONF_EXTRACTED, rel)
            )

        for m in _WIKI.finditer(line):
            ref = m.group(1).strip()
            wid = _nid("wiki", rel, str(i), ref)
            nodes.append(
                Node(
                    id=wid,
                    kind="wiki",
                    label=ref,
                    source_path=rel,
                    line_start=i,
                    line_end=i,
                    meta={"ref": ref},
                )
            )
            parent = heading_stack[-1][1] if heading_stack else file_id
            edges.append(Edge(parent, wid, "contains", CONF_EXTRACTED, rel))

        for m in _ADR.finditer(line):
            cite = m.group(1).upper().replace(" ", "")
            if cite.startswith("RFC") and not cite.startswith("RFC"):
                cite = cite
            cid = _nid("cite", cite)
            # dedupe later in store; emit per occurrence edge
            nodes.append(
                Node(
                    id=cid,
                    kind="cite",
                    label=cite,
                    source_path=rel,
                    line_start=i,
                    line_end=i,
                    meta={"cite": cite},
                )
            )
            parent = heading_stack[-1][1] if heading_stack else file_id
            edges.append(Edge(parent, cid, "cites", CONF_EXTRACTED, rel))

    return GraphSlice(nodes=nodes, edges=edges, content_hash=content_hash)


def resolve_inferences(
    slices: Sequence[GraphSlice], root: Path
) -> list[Edge]:
    """INFERRED edges: relative markdown targets that resolve to known files."""
    file_by_rel: dict[str, str] = {}
    file_by_name: dict[str, list[str]] = {}
    for sl in slices:
        for n in sl.nodes:
            if n.kind == "file":
                file_by_rel[n.label] = n.id
                name = Path(n.label).name.lower()
                file_by_name.setdefault(name, []).append(n.id)

    inferred: list[Edge] = []
    for sl in slices:
        for n in sl.nodes:
            if n.kind != "link":
                continue
            target = (n.meta or {}).get("target", "")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0].strip()
            if not clean:
                continue
            # relative to source file
            src_dir = Path(n.source_path).parent
            cand = (root / src_dir / clean).resolve()
            try:
                rel = cand.relative_to(root.resolve()).as_posix()
            except ValueError:
                rel = clean.lstrip("./")
            dst = file_by_rel.get(rel)
            if not dst:
                hits = file_by_name.get(Path(clean).name.lower(), [])
                if len(hits) == 1:
                    dst = hits[0]
            if dst:
                inferred.append(
                    Edge(n.id, dst, "resolves_to", CONF_INFERRED, n.source_path)
                )
    return inferred


def extract_tree(root: Path) -> tuple[list[Node], list[Edge], dict[str, str]]:
    """Extract all MD under root. Returns nodes, edges, path→hash."""
    root = root.resolve()
    slices: list[GraphSlice] = []
    hashes: dict[str, str] = {}
    for path in iter_md_files(root):
        sl = extract_file(path, root)
        slices.append(sl)
        hashes[_rel(path, root)] = sl.content_hash

    nodes: list[Node] = []
    edges: list[Edge] = []
    seen_nodes: set[str] = set()
    for sl in slices:
        for n in sl.nodes:
            if n.id in seen_nodes and n.kind == "cite":
                continue
            if n.id not in seen_nodes:
                nodes.append(n)
                seen_nodes.add(n.id)
        edges.extend(sl.edges)
    edges.extend(resolve_inferences(slices, root))
    return nodes, edges, hashes


__all__ = [
    "Node",
    "Edge",
    "GraphSlice",
    "CONF_EXTRACTED",
    "CONF_INFERRED",
    "extract_file",
    "extract_tree",
    "iter_md_files",
    "resolve_inferences",
]
