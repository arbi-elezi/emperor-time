#!/usr/bin/env python3
"""Emperor Time adjustable-rigor config — schema v1 (stdlib YAML subset).

Thin extension of effort_class — no parallel ladder. Load/merge:

  1. Built-in defaults (default_effort_class=tiny, auto_detect_little=true)
  2. Project `.emperor/config.yaml` (if present)
  3. User overlay `~/.config/emperor-time/config.yaml` (wins on keys it sets)

Aliases (resolved on read/set of rigor.default_effort_class):
  standard → small, full → large

Iron gates in gates.always_hard NEVER soft — forge PR-consent, pin-consent,
quarantine/steal consent, secrets-no-leak, enlist/credentials. Documented in
schema comments; scale_with_effort may soften *other* gates only.

CLI: `emperor config show|get|set|edit` (host-agnostic thin twins).
Missing file → defaults (tiny). Freeze *-hint-bind; no museum/Nen/k8s growth.

Stdlib only — hand-rolled YAML subset (no PyYAML).
"""
from __future__ import annotations

import argparse
import copy
import os
import re
import sys
from pathlib import Path
from typing import Any, Sequence

LEAF = "references/mechanical-gates.md"
SCHEMA_VERSION = 1

# Canonical effort ladder (no parallel rigor ladder).
EFFORT_CLASSES = ("tiny", "small", "medium", "large")

# User-facing aliases → canonical class (thin extension of effort_class).
EFFORT_ALIASES: dict[str, str] = {
    "standard": "small",
    "full": "large",
}

# Iron gates — NEVER soft regardless of effort_class / scale_with_effort.
# forge-pr-consent, pin-and-consent, quarantine, steal-consent, secrets-no-leak;
# enlist/credentials covered by steal-consent + secrets-no-leak.
ALWAYS_HARD_GATES: tuple[str, ...] = (
    "forge-pr-consent",
    "pin-and-consent",
    "quarantine",
    "steal-consent",
    "secrets-no-leak",
)

DEFAULT_CONFIG: dict[str, Any] = {
    "version": SCHEMA_VERSION,
    "rigor": {
        "default_effort_class": "tiny",
        "aliases": {"standard": "small", "full": "large"},
        "auto_detect_little": True,
    },
    "gates": {
        # Iron — never soft (see ALWAYS_HARD_GATES / schema comments).
        "always_hard": list(ALWAYS_HARD_GATES),
        "scale_with_effort": True,
    },
    "harness": {
        "force_table_source": "builtin",
        "require_plan": True,
        "require_spec": True,
    },
}

# Minimal default file body shipped / created-on-set.
DEFAULT_YAML = """\
# Emperor Time adjustable rigor — schema v1
# Thin extension of effort_class (no parallel ladder).
# Aliases: standard→small, full→large. Missing file → defaults (tiny).
# Iron gates (always_hard) NEVER soft: forge-pr-consent, pin-and-consent,
# quarantine, steal-consent, secrets-no-leak (+ enlist/credentials via those).
version: 1
rigor:
  default_effort_class: tiny
  aliases:
    standard: small
    full: large
  auto_detect_little: true
gates:
  always_hard:
    - forge-pr-consent
    - pin-and-consent
    - quarantine
    - steal-consent
    - secrets-no-leak
  scale_with_effort: true
harness:
  force_table_source: builtin
  require_plan: true
  require_spec: true
"""


# ---------------------------------------------------------------------------
# Minimal YAML subset (load + dump) — maps/lists/scalars/bools/null/int/float
# ---------------------------------------------------------------------------

_BOOLS = {"true": True, "false": False, "yes": True, "no": False, "on": True, "off": False}
_NULL = {"null", "~", ""}


def _parse_scalar(raw: str) -> Any:
    s = raw.strip()
    if not s or s in _NULL:
        return None
    low = s.lower()
    if low in _BOOLS:
        return _BOOLS[low]
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    # int / float
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s):
        return float(s)
    # inline flow list [a, b]
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(p.strip()) for p in _split_flow(inner)]
    # inline flow map {a: b}
    if s.startswith("{") and s.endswith("}"):
        inner = s[1:-1].strip()
        out: dict[str, Any] = {}
        if not inner:
            return out
        for part in _split_flow(inner):
            if ":" not in part:
                continue
            k, _, v = part.partition(":")
            out[k.strip()] = _parse_scalar(v.strip())
        return out
    return s


def _split_flow(inner: str) -> list[str]:
    parts: list[str] = []
    buf: list[str] = []
    depth = 0
    in_q: str | None = None
    for ch in inner:
        if in_q:
            buf.append(ch)
            if ch == in_q:
                in_q = None
            continue
        if ch in ('"', "'"):
            in_q = ch
            buf.append(ch)
            continue
        if ch in "[{":
            depth += 1
            buf.append(ch)
            continue
        if ch in "]}":
            depth -= 1
            buf.append(ch)
            continue
        if ch == "," and depth == 0:
            parts.append("".join(buf).strip())
            buf = []
            continue
        buf.append(ch)
    if buf:
        parts.append("".join(buf).strip())
    return [p for p in parts if p]


def load_yaml(text: str) -> Any:
    """Parse a minimal YAML subset into Python objects."""
    lines = text.splitlines()
    # Drop full-line comments / blanks up front via indexer.
    idx = 0

    def peek() -> tuple[int, str] | None:
        nonlocal idx
        while idx < len(lines):
            raw = lines[idx]
            # strip inline comments only when not inside quotes (best-effort)
            stripped = raw.split("#", 1)[0].rstrip() if "#" in raw and not _in_quote_hash(raw) else raw.rstrip()
            if not stripped.strip():
                idx += 1
                continue
            indent = len(stripped) - len(stripped.lstrip(" "))
            return indent, stripped.lstrip(" ")
        return None

    def _in_quote_hash(raw: str) -> bool:
        # crude: if odd number of quotes before #, treat # as inside string
        before = raw.split("#", 1)[0]
        return before.count('"') % 2 == 1 or before.count("'") % 2 == 1

    def parse_block(min_indent: int) -> Any:
        nonlocal idx
        cur = peek()
        if cur is None:
            return None
        indent, content = cur
        if indent < min_indent:
            return None
        if content.startswith("- "):
            return parse_list(min_indent)
        if ":" in content:
            return parse_map(min_indent)
        # bare scalar
        idx += 1
        return _parse_scalar(content)

    def parse_map(min_indent: int) -> dict[str, Any]:
        nonlocal idx
        out: dict[str, Any] = {}
        while True:
            cur = peek()
            if cur is None:
                break
            indent, content = cur
            if indent < min_indent:
                break
            if content.startswith("- "):
                break
            if indent > min_indent and out:
                # nested continuation without key — shouldn't happen at map level
                break
            if ":" not in content:
                break
            key, _, rest = content.partition(":")
            key = key.strip()
            rest = rest.strip()
            idx += 1
            if rest:
                out[key] = _parse_scalar(rest)
            else:
                nxt = peek()
                if nxt is None:
                    out[key] = None
                else:
                    nindent, ncontent = nxt
                    if nindent <= indent:
                        out[key] = None
                    elif ncontent.startswith("- "):
                        out[key] = parse_list(nindent)
                    else:
                        out[key] = parse_map(nindent)
        return out

    def parse_list(min_indent: int) -> list[Any]:
        nonlocal idx
        out: list[Any] = []
        while True:
            cur = peek()
            if cur is None:
                break
            indent, content = cur
            if indent < min_indent:
                break
            if not content.startswith("- "):
                break
            if indent > min_indent and out and indent != min_indent:
                # nested list item at deeper indent belongs to previous value
                break
            item_raw = content[2:].strip()
            idx += 1
            if not item_raw:
                nxt = peek()
                if nxt is None:
                    out.append(None)
                else:
                    nindent, ncontent = nxt
                    if nindent <= indent:
                        out.append(None)
                    elif ncontent.startswith("- "):
                        out.append(parse_list(nindent))
                    else:
                        out.append(parse_map(nindent))
            elif item_raw.endswith(":") or (
                ":" in item_raw and not item_raw.startswith("{")
                and _parse_scalar(item_raw.split(":", 1)[1].strip() if ":" in item_raw else "") is not None
                and item_raw.split(":", 1)[1].strip() == ""
            ):
                # "- key:" → map starting at this indent+2
                # Actually "- key: value" inline map entry
                if item_raw.endswith(":"):
                    k = item_raw[:-1].strip()
                    nxt = peek()
                    if nxt is None or nxt[0] <= indent:
                        out.append({k: None})
                    else:
                        nindent, ncontent = nxt
                        if ncontent.startswith("- "):
                            out.append({k: parse_list(nindent)})
                        else:
                            nested = parse_map(nindent)
                            out.append({k: nested} if k not in nested else {k: nested})
                            # Better: map with key k whose value is nested map OR
                            # the list item IS a map beginning with k
                            # Re-parse as map starting with this key
                else:
                    # "- key: value" single-entry map
                    k, _, v = item_raw.partition(":")
                    entry: dict[str, Any] = {k.strip(): _parse_scalar(v.strip())}
                    # may continue with more keys at indent+2
                    nxt = peek()
                    if nxt is not None and nxt[0] > indent and not nxt[1].startswith("- "):
                        more = parse_map(nxt[0])
                        entry.update(more)
                    out.append(entry)
            elif ":" in item_raw and not item_raw.startswith("[") and not item_raw.startswith("{"):
                # "- key: value" possibly followed by more map keys
                k, _, v = item_raw.partition(":")
                entry = {k.strip(): _parse_scalar(v.strip())}
                nxt = peek()
                if nxt is not None and nxt[0] > indent and not nxt[1].startswith("- "):
                    more = parse_map(nxt[0])
                    entry.update(more)
                out.append(entry)
            else:
                out.append(_parse_scalar(item_raw))
        return out

    result = parse_block(0)
    return result if result is not None else {}


def dump_yaml(data: Any, *, indent: int = 0) -> str:
    """Serialize a restricted object tree to YAML subset text."""
    sp = "  " * indent

    def dump(obj: Any, level: int) -> list[str]:
        pad = "  " * level
        lines_out: list[str] = []
        if isinstance(obj, dict):
            if not obj:
                lines_out.append(pad + "{}")
                return lines_out
            for k, v in obj.items():
                if isinstance(v, dict):
                    if not v:
                        lines_out.append(f"{pad}{k}: {{}}")
                    else:
                        lines_out.append(f"{pad}{k}:")
                        lines_out.extend(dump(v, level + 1))
                elif isinstance(v, list):
                    if not v:
                        lines_out.append(f"{pad}{k}: []")
                    else:
                        lines_out.append(f"{pad}{k}:")
                        lines_out.extend(dump(v, level + 1))
                else:
                    lines_out.append(f"{pad}{k}: {_fmt_scalar(v)}")
            return lines_out
        if isinstance(obj, list):
            if not obj:
                lines_out.append(pad + "[]")
                return lines_out
            for item in obj:
                if isinstance(item, dict):
                    if not item:
                        lines_out.append(f"{pad}- {{}}")
                    else:
                        keys = list(item.keys())
                        first_k = keys[0]
                        first_v = item[first_k]
                        if isinstance(first_v, (dict, list)):
                            lines_out.append(f"{pad}- {first_k}:")
                            lines_out.extend(dump(first_v, level + 2))
                            rest = {k: item[k] for k in keys[1:]}
                            if rest:
                                lines_out.extend(dump(rest, level + 1))
                        else:
                            lines_out.append(f"{pad}- {first_k}: {_fmt_scalar(first_v)}")
                            rest = {k: item[k] for k in keys[1:]}
                            if rest:
                                lines_out.extend(dump(rest, level + 1))
                elif isinstance(item, list):
                    lines_out.append(f"{pad}-")
                    lines_out.extend(dump(item, level + 1))
                else:
                    lines_out.append(f"{pad}- {_fmt_scalar(item)}")
            return lines_out
        lines_out.append(pad + _fmt_scalar(obj))
        return lines_out

    return "\n".join(dump(data, indent)) + "\n"


def _fmt_scalar(v: Any) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if s == "" or any(c in s for c in ":#{}[]&*!|>%@`") or s.strip() != s:
        return '"' + s.replace('"', '\\"') + '"'
    return s


# ---------------------------------------------------------------------------
# Merge / resolve / paths
# ---------------------------------------------------------------------------


def deep_merge(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    """Overlay wins on keys it sets; nested dicts merge; lists replace."""
    out = copy.deepcopy(base)
    for k, v in overlay.items():
        if k in out and isinstance(out[k], dict) and isinstance(v, dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def resolve_effort_alias(value: str) -> str:
    """Map alias → canonical effort_class; pass through known classes."""
    v = (value or "").lower().strip()
    if v in EFFORT_ALIASES:
        return EFFORT_ALIASES[v]
    return v


def normalize_effort_class(value: str) -> str:
    """Resolve alias and validate against EFFORT_CLASSES."""
    cls = resolve_effort_alias(value)
    if cls not in EFFORT_CLASSES:
        raise ValueError(
            f"effort_class must be one of {EFFORT_CLASSES} "
            f"(aliases: {dict(EFFORT_ALIASES)}), got {value!r}"
        )
    return cls


def project_config_path(root: Path) -> Path:
    return root / ".emperor" / "config.yaml"


def user_config_path() -> Path:
    explicit = os.environ.get("EMPEROR_CONFIG", "").strip()
    if explicit:
        return Path(explicit).expanduser().resolve()
    xdg = os.environ.get("XDG_CONFIG_HOME", "").strip()
    if xdg:
        return Path(xdg).expanduser().resolve() / "emperor-time" / "config.yaml"
    return Path.home() / ".config" / "emperor-time" / "config.yaml"


def _resolve_root(explicit: str | Path | None = None) -> Path:
    """Prefer git / SKILL.md / .emperor/config.yaml walk from explicit or cwd."""
    start = Path(explicit).resolve() if explicit else Path.cwd().resolve()
    for p in [start, *start.parents]:
        if (p / ".git").exists() or (p / "SKILL.md").exists():
            return p
        if (p / ".emperor" / "config.yaml").is_file():
            return p
    return start


def _read_yaml_file(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    data = load_yaml(text)
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError(f"config root must be a mapping: {path}")
    return data


def _normalize_loaded(data: dict[str, Any]) -> dict[str, Any]:
    """Apply alias resolution on rigor.default_effort_class; fill aliases map."""
    out = copy.deepcopy(data)
    rigor = out.setdefault("rigor", {})
    if not isinstance(rigor, dict):
        raise ValueError("rigor must be a mapping")
    aliases = rigor.get("aliases")
    merged = dict(EFFORT_ALIASES)
    if isinstance(aliases, dict):
        for k, v in aliases.items():
            mv = str(v).lower().strip()
            # Allow alias→alias once via known map, else canonical.
            if mv in EFFORT_ALIASES:
                mv = EFFORT_ALIASES[mv]
            merged[str(k).lower().strip()] = mv
    rigor["aliases"] = merged
    raw = rigor.get("default_effort_class", "tiny")
    v = str(raw).lower().strip()
    if v in merged:
        v = merged[v]
    if v not in EFFORT_CLASSES:
        raise ValueError(
            f"rigor.default_effort_class must be one of {EFFORT_CLASSES} "
            f"(or alias), got {raw!r}"
        )
    rigor["default_effort_class"] = v
    if "auto_detect_little" not in rigor:
        rigor["auto_detect_little"] = True
    gates = out.setdefault("gates", {})
    if isinstance(gates, dict):
        # Iron gates always present / never soft — enforce union with defaults.
        hard = gates.get("always_hard")
        if isinstance(hard, list):
            seen = []
            for g in list(ALWAYS_HARD_GATES) + [str(x) for x in hard]:
                if g not in seen:
                    seen.append(g)
            gates["always_hard"] = seen
        else:
            gates["always_hard"] = list(ALWAYS_HARD_GATES)
        if "scale_with_effort" not in gates:
            gates["scale_with_effort"] = True
    out.setdefault("version", SCHEMA_VERSION)
    return out


def load_config(root: Path | None = None) -> dict[str, Any]:
    """Load merged config: defaults ← project ← user overlay (user wins)."""
    root = _resolve_root(root)
    merged = copy.deepcopy(DEFAULT_CONFIG)
    project = _read_yaml_file(project_config_path(root))
    if project:
        merged = deep_merge(merged, project)
    user = _read_yaml_file(user_config_path())
    if user:
        merged = deep_merge(merged, user)
    return _normalize_loaded(merged)


def default_effort_class(root: Path | None = None) -> str:
    """Resolved default effort_class from config (aliases already applied)."""
    cfg = load_config(root)
    return str(cfg["rigor"]["default_effort_class"])


def auto_detect_little(root: Path | None = None) -> bool:
    cfg = load_config(root)
    return bool(cfg.get("rigor", {}).get("auto_detect_little", True))


def get_path(cfg: dict[str, Any], dotted: str) -> Any:
    cur: Any = cfg
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(dotted)
        cur = cur[part]
    return cur


def set_path(cfg: dict[str, Any], dotted: str, value: Any) -> dict[str, Any]:
    parts = dotted.split(".")
    out = copy.deepcopy(cfg)
    cur: Any = out
    for part in parts[:-1]:
        if part not in cur or not isinstance(cur[part], dict):
            cur[part] = {}
        cur = cur[part]
    key = parts[-1]
    # Resolve aliases when setting rigor.default_effort_class
    if dotted == "rigor.default_effort_class" or (
        dotted.endswith("default_effort_class") and isinstance(value, str)
    ):
        value = normalize_effort_class(str(value))
    # Coerce common scalar strings from CLI
    if isinstance(value, str):
        low = value.lower().strip()
        if low in _BOOLS:
            value = _BOOLS[low]
        elif re.fullmatch(r"-?\d+", value):
            value = int(value)
    cur[key] = value
    return out


def ensure_project_config(root: Path | None = None) -> Path:
    """Create `.emperor/config.yaml` from defaults if missing; return path."""
    root = _resolve_root(root)
    path = project_config_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.is_file():
        path.write_text(DEFAULT_YAML, encoding="utf-8")
    return path


def write_project_config(cfg: dict[str, Any], root: Path | None = None) -> Path:
    root = _resolve_root(root)
    path = project_config_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Write normalized schema-shaped view (not full merge with comments).
    body = dump_yaml(
        {
            "version": int(cfg.get("version", SCHEMA_VERSION)),
            "rigor": cfg.get("rigor", DEFAULT_CONFIG["rigor"]),
            "gates": cfg.get("gates", DEFAULT_CONFIG["gates"]),
            "harness": cfg.get("harness", DEFAULT_CONFIG["harness"]),
        }
    )
    # Prepend iron-gate comment header.
    header = (
        "# Emperor Time adjustable rigor — schema v1\n"
        "# Iron gates (always_hard) NEVER soft.\n"
        "# Aliases: standard→small, full→large.\n"
    )
    path.write_text(header + body, encoding="utf-8")
    return path


def format_show(cfg: dict[str, Any]) -> str:
    return dump_yaml(cfg)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _cli_show(args: argparse.Namespace) -> int:
    root = _resolve_root(args.root)
    cfg = load_config(root)
    sys.stdout.write(format_show(cfg))
    return 0


def _cli_get(args: argparse.Namespace) -> int:
    root = _resolve_root(args.root)
    cfg = load_config(root)
    try:
        val = get_path(cfg, args.key)
    except KeyError:
        print(f"config FAIL: unknown key {args.key!r}", file=sys.stderr)
        return 2
    if isinstance(val, (dict, list)):
        sys.stdout.write(dump_yaml(val))
    elif isinstance(val, bool):
        print("true" if val else "false")
    elif val is None:
        print("null")
    else:
        print(val)
    return 0


def _cli_set(args: argparse.Namespace) -> int:
    root = _resolve_root(args.root)
    path = ensure_project_config(root)
    # Load project-only (not user overlay) so set writes project file.
    project = _read_yaml_file(path)
    base = deep_merge(copy.deepcopy(DEFAULT_CONFIG), project) if project else copy.deepcopy(DEFAULT_CONFIG)
    try:
        updated = set_path(base, args.key, args.value)
        updated = _normalize_loaded(updated)
    except (ValueError, KeyError) as exc:
        print(f"config FAIL: {exc}", file=sys.stderr)
        return 2
    write_project_config(updated, root)
    # Print resolved value for the key.
    try:
        resolved = get_path(updated, args.key)
    except KeyError:
        resolved = args.value
    print(f"config: set {args.key}={_fmt_scalar(resolved)} ({path})")
    return 0


def _cli_edit(args: argparse.Namespace) -> int:
    root = _resolve_root(args.root)
    path = ensure_project_config(root)
    editor = os.environ.get("EDITOR", "").strip()
    if not sys.stdin.isatty() or not editor:
        print(path.resolve())
        return 0
    import subprocess

    rc = subprocess.call([editor, str(path)])
    return rc


def format_card() -> str:
    return (
        "CONFIG — adjustable rigor (schema v1)\n"
        "  emperor config show              # merged defaults+project+user\n"
        "  emperor config get <dotted.key>  # e.g. rigor.default_effort_class\n"
        "  emperor config set <key> <value> # writes .emperor/config.yaml\n"
        "  emperor config edit              # $EDITOR or print path if no TTY\n"
        f"  aliases: standard→small, full→large; default tiny; see {LEAF}\n"
        "  iron always_hard NEVER soft (forge-pr-consent, pin-and-consent,\n"
        "  quarantine, steal-consent, secrets-no-leak)\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="emperor-config",
        description="Emperor Time adjustable-rigor config (schema v1)",
    )
    p.add_argument(
        "--root",
        default=None,
        help="Project root (default: cwd / git / SKILL.md walk)",
    )
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("show", help="Print merged config (YAML)")
    g = sub.add_parser("get", help="Get a dotted key")
    g.add_argument("key")
    s = sub.add_parser("set", help="Set a dotted key in project config")
    s.add_argument("key")
    s.add_argument("value")
    sub.add_parser("edit", help="Open project config in $EDITOR (or print path)")

    args = p.parse_args(list(argv) if argv is not None else None)
    if not args.cmd:
        sys.stdout.write(format_card())
        return 0
    if args.cmd == "show":
        return _cli_show(args)
    if args.cmd == "get":
        return _cli_get(args)
    if args.cmd == "set":
        return _cli_set(args)
    if args.cmd == "edit":
        return _cli_edit(args)
    sys.stdout.write(format_card())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
