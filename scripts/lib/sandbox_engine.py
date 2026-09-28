#!/usr/bin/env python3
"""Emperor Time sandbox engine — ports, emitters, profiles, plan|up|down.

Real in v0.4.135+ (deepens stubs from super_context v0.4.133/134):

1. PortAllocator — persist `.emperor/sandbox/ports.json`; no collisions
   across parallel artifacts (scans all allocations before assigning).
2. ComposeEmitter — wire SOT plugin fragments + artifact workspace into
   `docker-compose.yml` / `compose.yml`.
3. PodmanEmitter — `podman-compose.yml` (compose-compat) + optional
   `podman-play.yaml` for `podman play kube`.
4. K8sEmitter — basic Deployment + Service manifests from plugin list.
5. `sandbox plan|up|down|ports` honor active runtime (compose|podman|k8s).
6. Loadable profiles: isolate (network), mock (placeholder svc), simulate.

No embeddings. No Graphify. Stdlib only. Blind secrets stay names-only.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

import thoughttrail as trail

DEFAULT_BASE = 18000
DEFAULT_STRIDE = 10  # ports reserved per artifact block
DEFAULT_KEYS = ("http", "db", "aux")
RUNTIMES = ("compose", "podman", "k8s")
PROFILES = ("isolate", "mock", "simulate")


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _safe_name(s: str) -> str:
    out = []
    for ch in s.lower():
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        else:
            out.append("-")
    name = "".join(out).strip("-") or "et"
    return name[:63]


# ---------------------------------------------------------------------------
# Port allocator
# ---------------------------------------------------------------------------


def ports_path(root: Path) -> Path:
    return root / ".emperor" / "sandbox" / "ports.json"


def load_ports(root: Path) -> dict[str, Any]:
    path = ports_path(root)
    if not path.is_file():
        trail.ensure_layout(root)
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("next_base", DEFAULT_BASE)
    data.setdefault("allocations", {})
    return data


def save_ports(root: Path, data: dict[str, Any]) -> None:
    path = ports_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _used_ports(data: dict[str, Any]) -> set[int]:
    used: set[int] = set()
    for alloc in (data.get("allocations") or {}).values():
        if isinstance(alloc, dict):
            for v in alloc.values():
                if isinstance(v, int):
                    used.add(v)
                elif isinstance(v, dict) and "port" in v:
                    used.add(int(v["port"]))
    return used


def allocate_ports(
    root: Path,
    artifact_id: str,
    *,
    keys: tuple[str, ...] | list[str] | None = None,
    force: bool = False,
) -> dict[str, int]:
    """Allocate host ports for an artifact. Persist; never collide.

    Returns mapping service_key -> host_port. Reuses existing allocation
    unless force=True.
    """
    trail.ensure_layout(root)
    data = load_ports(root)
    keys = tuple(keys) if keys else DEFAULT_KEYS
    existing = (data.get("allocations") or {}).get(artifact_id)
    if existing and not force:
        # normalize to flat int map
        out: dict[str, int] = {}
        for k, v in existing.items():
            if isinstance(v, int):
                out[k] = v
            elif isinstance(v, dict) and "port" in v:
                out[k] = int(v["port"])
        # ensure all requested keys present
        if all(k in out for k in keys):
            return {k: out[k] for k in keys}

    used = _used_ports(data)
    # Prefer advancing next_base, but skip any collision
    base = int(data.get("next_base", DEFAULT_BASE))
    while any(base + i in used for i in range(max(len(keys), DEFAULT_STRIDE))):
        base += DEFAULT_STRIDE

    alloc: dict[str, int] = {}
    cursor = base
    for k in keys:
        while cursor in used or cursor in alloc.values():
            cursor += 1
        alloc[k] = cursor
        used.add(cursor)
        cursor += 1

    data.setdefault("allocations", {})[artifact_id] = alloc
    # advance next_base past this block
    data["next_base"] = max(int(data.get("next_base", DEFAULT_BASE)), cursor)
    # also ensure stride gap for parallel friends
    if data["next_base"] < base + DEFAULT_STRIDE:
        data["next_base"] = base + DEFAULT_STRIDE
    save_ports(root, data)
    return alloc


def release_ports(root: Path, artifact_id: str) -> bool:
    data = load_ports(root)
    allocs = data.get("allocations") or {}
    if artifact_id not in allocs:
        return False
    del allocs[artifact_id]
    data["allocations"] = allocs
    save_ports(root, data)
    return True


# ---------------------------------------------------------------------------
# Plugin discovery
# ---------------------------------------------------------------------------


def list_plugins(root: Path, artifact_id: str = "") -> list[dict[str, Any]]:
    """Return plugin descriptors from SOT (+ optional artifact.json filter)."""
    plugins_dir = root / ".emperor" / "sot" / "plugins"
    names_filter: set[str] | None = None
    if artifact_id:
        meta_path = (
            root / ".emperor" / "artifacts" / artifact_id / "artifact.json"
        )
        if meta_path.is_file():
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            plugged = meta.get("plugins") or []
            if plugged:
                names_filter = set(plugged)

    out: list[dict[str, Any]] = []
    if not plugins_dir.is_dir():
        return out
    for p in sorted(plugins_dir.iterdir()):
        if not p.is_dir() or p.name.startswith("."):
            continue
        meta_path = p / "plugin.json"
        if not meta_path.is_file():
            continue
        if names_filter is not None and p.name not in names_filter:
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        frag = p / "compose.fragment.yml"
        out.append(
            {
                "name": p.name,
                "meta": meta,
                "dir": p,
                "fragment": frag if frag.is_file() else None,
                "image": meta.get("image")
                or f"${{{p.name.upper().replace('-', '_')}_IMAGE:-alpine:3.20}}",
            }
        )
    return out


# ---------------------------------------------------------------------------
# Profiles (loadable stubs)
# ---------------------------------------------------------------------------


def profiles_dir(root: Path) -> Path:
    return root / ".emperor" / "sandbox" / "profiles"


def ensure_profiles(root: Path) -> dict[str, Path]:
    """Write loadable isolate/mock/simulate profile stubs if missing."""
    trail.ensure_layout(root)
    pdir = profiles_dir(root)
    pdir.mkdir(parents=True, exist_ok=True)
    specs = {
        "isolate": {
            "name": "isolate",
            "kind": "network",
            "description": "Isolate artifact stack on an internal network (no host publish except allocated ports).",
            "compose": {
                "networks": {
                    "et-isolate": {
                        "driver": "bridge",
                        "internal": True,
                    }
                },
                "service_defaults": {
                    "networks": ["et-isolate", "default"],
                },
            },
            "k8s": {"networkPolicy": "default-deny-egress-optional"},
            "loadable": True,
        },
        "mock": {
            "name": "mock",
            "kind": "service",
            "description": "Placeholder mock service (alpine sleep) for dependent plugins.",
            "compose": {
                "services": {
                    "et-mock": {
                        "image": "alpine:3.20",
                        "command": ["sleep", "infinity"],
                        "profiles": ["et-mock"],
                        "labels": {"et.profile": "mock"},
                    }
                }
            },
            "k8s": {
                "deployment": "et-mock",
                "image": "alpine:3.20",
                "command": ["sleep", "infinity"],
            },
            "loadable": True,
        },
        "simulate": {
            "name": "simulate",
            "kind": "sim",
            "description": "Simulate profile stub — marks stack as sim-only (no external side effects).",
            "compose": {
                "x-et-simulate": True,
                "service_defaults": {
                    "labels": {"et.profile": "simulate", "et.simulate": "true"}
                },
            },
            "k8s": {"annotations": {"et.profile": "simulate"}},
            "loadable": True,
        },
    }
    paths: dict[str, Path] = {}
    for name, spec in specs.items():
        path = pdir / f"{name}.json"
        if not path.exists():
            path.write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
        paths[name] = path
    readme = pdir / "README.md"
    if not readme.exists():
        readme.write_text(
            "# Sandbox profiles (loadable)\n\n"
            "- `isolate` — internal network isolation\n"
            "- `mock` — placeholder mock service\n"
            "- `simulate` — sim-only labels / no external side effects\n\n"
            "Loaded by `emperor sandbox plan` from this directory.\n",
            encoding="utf-8",
        )
    return paths


def load_profile(root: Path, name: str) -> dict[str, Any] | None:
    ensure_profiles(root)
    path = profiles_dir(root) / f"{name}.json"
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def active_profiles(root: Path) -> list[str]:
    """Profiles enabled in sandbox/manifest.json (default: isolate + mock)."""
    ensure_profiles(root)
    man = root / ".emperor" / "sandbox" / "manifest.json"
    if not man.is_file():
        return ["isolate", "mock"]
    data = json.loads(man.read_text(encoding="utf-8"))
    enabled = []
    if data.get("isolate", True):
        enabled.append("isolate")
    mocks = data.get("mocks") or []
    if mocks or data.get("mock", True):
        # default mock on unless explicitly disabled
        if data.get("mock", True) or mocks:
            enabled.append("mock")
    sims = data.get("sims") or []
    if sims or data.get("simulate"):
        enabled.append("simulate")
    # de-dupe preserve order
    seen: set[str] = set()
    out: list[str] = []
    for p in enabled:
        if p not in seen and p in PROFILES:
            seen.add(p)
            out.append(p)
    return out or ["isolate"]


# ---------------------------------------------------------------------------
# Runtime selection
# ---------------------------------------------------------------------------


def active_runtime(root: Path) -> str:
    trail.ensure_layout(root)
    path = root / ".emperor" / "sandbox" / "runtime" / "active"
    if path.is_file():
        cur = path.read_text(encoding="utf-8").strip()
        if cur in RUNTIMES:
            return cur
    return "compose"


def set_runtime(root: Path, backend: str) -> str:
    if backend not in RUNTIMES:
        raise ValueError(f"backend must be one of {RUNTIMES}")
    trail.ensure_layout(root)
    path = root / ".emperor" / "sandbox" / "runtime" / "active"
    path.write_text(backend + "\n", encoding="utf-8")
    return backend


# ---------------------------------------------------------------------------
# Emitters
# ---------------------------------------------------------------------------


def _fragment_body(frag_path: Path) -> str:
    text = frag_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    # drop leading pure-comment / blank lines for merge under services:
    while lines and (not lines[0].strip() or lines[0].lstrip().startswith("#")):
        lines.pop(0)
    body = "\n".join(lines).rstrip() + "\n"
    if body.lstrip().startswith("services:"):
        # strip the services: header; keep indented services
        rest = body.split("\n", 1)[1] if "\n" in body else ""
        return rest if rest.endswith("\n") else rest + "\n"
    return body


def _default_service_yaml(name: str, image: str, host_port: int) -> str:
    return (
        f"  {name}:\n"
        f"    image: {image}\n"
        f'    command: ["sleep", "infinity"]\n'
        f'    ports: ["{host_port}:80"]\n'
        f"    labels:\n"
        f"      et.plugin: \"{name}\"\n"
    )


def emit_compose(
    root: Path,
    artifact_id: str,
    alloc: dict[str, int],
    *,
    profiles: list[str] | None = None,
) -> str:
    """Emit docker-compose.yml content wiring SOT plugins + profiles."""
    plugins = list_plugins(root, artifact_id)
    profiles = profiles if profiles is not None else active_profiles(root)
    http = alloc.get("http", DEFAULT_BASE)

    parts: list[str] = []
    if plugins:
        for i, plug in enumerate(plugins):
            port = alloc.get(plug["name"]) or alloc.get(
                DEFAULT_KEYS[min(i, len(DEFAULT_KEYS) - 1)], http + i
            )
            if plug["fragment"]:
                parts.append(_fragment_body(plug["fragment"]))
            else:
                parts.append(
                    _default_service_yaml(plug["name"], plug["image"], int(port))
                )
    else:
        parts.append(
            _default_service_yaml("et-stub", "alpine:3.20", http)
        )

    # mock profile → placeholder service
    if "mock" in profiles:
        mock = load_profile(root, "mock") or {}
        svc = (mock.get("compose") or {}).get("services") or {}
        if "et-mock" in svc:
            parts.append(
                "  et-mock:\n"
                "    image: alpine:3.20\n"
                '    command: ["sleep", "infinity"]\n'
                '    profiles: ["et-mock"]\n'
                "    labels:\n"
                '      et.profile: "mock"\n'
            )

    body = "".join(parts)
    header = (
        f"# ET sandbox compose for artifact={artifact_id}\n"
        f"# runtime=compose ports={json.dumps(alloc)}\n"
        f"# profiles={','.join(profiles)}\n"
        f"# generated={_utc()}\n"
        "# emitters: compose|podman|k8s — selected via `emperor runtime use`\n"
        "\n"
        "services:\n"
    )
    networks = "\nnetworks:\n  default:\n" f"    name: et-{_safe_name(artifact_id)}\n"
    if "isolate" in profiles:
        networks += (
            "  et-isolate:\n"
            "    driver: bridge\n"
            "    internal: true\n"
            f"    name: et-{_safe_name(artifact_id)}-iso\n"
        )
    return header + body + networks


def emit_podman(
    root: Path,
    artifact_id: str,
    alloc: dict[str, int],
    *,
    profiles: list[str] | None = None,
) -> tuple[str, str]:
    """Return (podman-compose.yml text, podman-play.yaml text)."""
    # compose-compat file for podman-compose
    compose_txt = emit_compose(root, artifact_id, alloc, profiles=profiles)
    compose_txt = compose_txt.replace(
        "runtime=compose", "runtime=podman (compose-compat)"
    )

    plugins = list_plugins(root, artifact_id)
    profiles = profiles if profiles is not None else active_profiles(root)
    http = alloc.get("http", DEFAULT_BASE)
    ns = f"et-{_safe_name(artifact_id)}"

    docs: list[str] = [
        f"# ET podman play kube for artifact={artifact_id}\n"
        f"# ports={json.dumps(alloc)} profiles={','.join(profiles)}\n"
        f"# invoke: podman play kube <this-file>\n"
    ]
    # Pod
    containers = []
    if plugins:
        for i, plug in enumerate(plugins):
            port = alloc.get(plug["name"]) or alloc.get(
                DEFAULT_KEYS[min(i, len(DEFAULT_KEYS) - 1)], http + i
            )
            containers.append(
                {
                    "name": plug["name"],
                    "image": "alpine:3.20",
                    "command": ["sleep", "infinity"],
                    "ports": [{"hostPort": int(port), "containerPort": 80}],
                }
            )
    else:
        containers.append(
            {
                "name": "et-stub",
                "image": "alpine:3.20",
                "command": ["sleep", "infinity"],
                "ports": [{"hostPort": http, "containerPort": 80}],
            }
        )
    if "mock" in profiles:
        containers.append(
            {
                "name": "et-mock",
                "image": "alpine:3.20",
                "command": ["sleep", "infinity"],
            }
        )

    # Emit as multi-doc YAML (hand-rolled, no PyYAML dep)
    play_lines = [
        "apiVersion: v1",
        "kind: Pod",
        "metadata:",
        f"  name: {ns}",
        f"  namespace: {ns}",
        "  labels:",
        f"    et.artifact: {artifact_id}",
        "    et.runtime: podman",
        "spec:",
        "  containers:",
    ]
    for c in containers:
        play_lines.append(f"  - name: {c['name']}")
        play_lines.append(f"    image: {c['image']}")
        play_lines.append("    command:")
        for arg in c["command"]:
            play_lines.append(f'    - "{arg}"')
        if c.get("ports"):
            play_lines.append("    ports:")
            for p in c["ports"]:
                play_lines.append(f"    - hostPort: {p['hostPort']}")
                play_lines.append(f"      containerPort: {p['containerPort']}")
    docs.append("\n".join(play_lines) + "\n")
    return compose_txt, "".join(docs) if len(docs) == 1 else docs[0] + docs[1]


def emit_k8s(
    root: Path,
    artifact_id: str,
    alloc: dict[str, int],
    *,
    profiles: list[str] | None = None,
) -> str:
    """Emit basic Namespace + Deployment + Service manifests."""
    plugins = list_plugins(root, artifact_id)
    profiles = profiles if profiles is not None else active_profiles(root)
    http = alloc.get("http", DEFAULT_BASE)
    ns = f"et-{_safe_name(artifact_id)}"

    lines: list[str] = [
        f"# ET k8s manifests for artifact={artifact_id}",
        f"# ports={json.dumps(alloc)} profiles={','.join(profiles)}",
        f"# generated={_utc()}",
        f"# invoke: kubectl apply -f <this-file>",
        "---",
        "apiVersion: v1",
        "kind: Namespace",
        "metadata:",
        f"  name: {ns}",
        f"  labels:",
        f"    et.artifact: \"{artifact_id}\"",
    ]

    services = plugins or [
        {"name": "et-stub", "image": "alpine:3.20", "meta": {}}
    ]
    if "mock" in profiles:
        services = list(services) + [
            {"name": "et-mock", "image": "alpine:3.20", "meta": {}}
        ]

    for i, plug in enumerate(services):
        name = plug["name"] if isinstance(plug, dict) else str(plug)
        image = (
            plug.get("image", "alpine:3.20")
            if isinstance(plug, dict)
            else "alpine:3.20"
        )
        # strip ${VAR:-default} → default for k8s (no compose interpolation)
        if isinstance(image, str) and image.startswith("${"):
            # ${FOO:-alpine:3.20} → alpine:3.20
            if ":-" in image:
                image = image.split(":-", 1)[1].rstrip("}")
            else:
                image = "alpine:3.20"
        port = alloc.get(name) or alloc.get(
            DEFAULT_KEYS[min(i, len(DEFAULT_KEYS) - 1)], http + i
        )
        lines += [
            "---",
            "apiVersion: apps/v1",
            "kind: Deployment",
            "metadata:",
            f"  name: {name}",
            f"  namespace: {ns}",
            "  labels:",
            f"    et.plugin: \"{name}\"",
            "spec:",
            "  replicas: 1",
            "  selector:",
            "    matchLabels:",
            f"      app: {name}",
            "  template:",
            "    metadata:",
            "      labels:",
            f"        app: {name}",
            "        et.runtime: k8s",
            "    spec:",
            "      containers:",
            f"      - name: {name}",
            f"        image: {image}",
            '        command: ["sleep", "infinity"]',
            "        ports:",
            "        - containerPort: 80",
            "---",
            "apiVersion: v1",
            "kind: Service",
            "metadata:",
            f"  name: {name}",
            f"  namespace: {ns}",
            "spec:",
            "  type: NodePort",
            "  selector:",
            f"    app: {name}",
            "  ports:",
            "  - port: 80",
            "    targetPort: 80",
            f"    # host hint (NodePort assigned by cluster; ET alloc={port})",
            f"    nodePort: {30000 + (int(port) % 2768)}",
        ]
    if "isolate" in profiles:
        lines += [
            "---",
            "apiVersion: networking.k8s.io/v1",
            "kind: NetworkPolicy",
            "metadata:",
            f"  name: et-isolate",
            f"  namespace: {ns}",
            "spec:",
            "  podSelector: {}",
            "  policyTypes: [\"Ingress\", \"Egress\"]",
            "  ingress:",
            "  - from:",
            "    - podSelector: {}",
            "  egress:",
            "  - to:",
            "    - podSelector: {}",
        ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Plan / up / down / ports
# ---------------------------------------------------------------------------


def artifact_dir(root: Path, artifact_id: str) -> Path:
    return root / ".emperor" / "artifacts" / artifact_id


def state_path(root: Path, artifact_id: str) -> Path:
    return artifact_dir(root, artifact_id) / "sandbox.state.json"


def write_state(root: Path, artifact_id: str, state: dict[str, Any]) -> Path:
    path = state_path(root, artifact_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    state = dict(state)
    state["updated"] = _utc()
    path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    return path


def plan(
    root: Path,
    artifact_id: str = "default",
    *,
    profiles: list[str] | None = None,
    runtime: str | None = None,
) -> dict[str, Any]:
    """Allocate ports + emit manifests for active (or given) runtime."""
    trail.ensure_layout(root)
    ensure_profiles(root)
    rt = runtime or active_runtime(root)
    profiles = profiles if profiles is not None else active_profiles(root)

    plugins = list_plugins(root, artifact_id)
    # allocate keys: default http/db/aux PLUS one per plugin name
    keys: list[str] = list(DEFAULT_KEYS)
    for p in plugins:
        if p["name"] not in keys:
            keys.append(p["name"])
    alloc = allocate_ports(root, artifact_id, keys=keys)

    art = artifact_dir(root, artifact_id)
    art.mkdir(parents=True, exist_ok=True)
    emitted: dict[str, str] = {}

    if rt == "compose":
        text = emit_compose(root, artifact_id, alloc, profiles=profiles)
        out = art / "compose.yml"
        out.write_text(text, encoding="utf-8")
        # also stash under runtime/compose for the emitter tree
        rt_out = (
            root
            / ".emperor"
            / "sandbox"
            / "runtime"
            / "compose"
            / f"{_safe_name(artifact_id)}.yml"
        )
        rt_out.write_text(text, encoding="utf-8")
        emitted["compose"] = str(out)
    elif rt == "podman":
        compose_txt, play_txt = emit_podman(
            root, artifact_id, alloc, profiles=profiles
        )
        c_out = art / "podman-compose.yml"
        p_out = art / "podman-play.yaml"
        c_out.write_text(compose_txt, encoding="utf-8")
        p_out.write_text(play_txt, encoding="utf-8")
        # mirror into runtime/podman
        rt_dir = root / ".emperor" / "sandbox" / "runtime" / "podman"
        (rt_dir / f"{_safe_name(artifact_id)}-compose.yml").write_text(
            compose_txt, encoding="utf-8"
        )
        (rt_dir / f"{_safe_name(artifact_id)}-play.yaml").write_text(
            play_txt, encoding="utf-8"
        )
        emitted["podman-compose"] = str(c_out)
        emitted["podman-play"] = str(p_out)
    elif rt == "k8s":
        text = emit_k8s(root, artifact_id, alloc, profiles=profiles)
        out = art / "k8s-manifests.yaml"
        out.write_text(text, encoding="utf-8")
        rt_out = (
            root
            / ".emperor"
            / "sandbox"
            / "runtime"
            / "k8s"
            / f"{_safe_name(artifact_id)}.yaml"
        )
        rt_out.write_text(text, encoding="utf-8")
        emitted["k8s"] = str(out)
    else:
        raise ValueError(f"unknown runtime {rt}")

    state = {
        "artifact": artifact_id,
        "runtime": rt,
        "status": "planned",
        "ports": alloc,
        "profiles": profiles,
        "plugins": [p["name"] for p in plugins],
        "emitted": emitted,
        "stub_up": False,
    }
    write_state(root, artifact_id, state)
    return state


def _which(cmd: str) -> str | None:
    return shutil.which(cmd)


def _run(cmd: list[str], *, cwd: Path | None = None) -> tuple[int, str]:
    try:
        r = subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return 127, f"{cmd[0]} not found"
    out = ((r.stdout or "") + (r.stderr or "")).strip()
    return r.returncode, out


def up(root: Path, artifact_id: str = "default") -> dict[str, Any]:
    """Bring stack up for active runtime. Honest skip if binary missing."""
    art = artifact_dir(root, artifact_id)
    st_path = state_path(root, artifact_id)
    if not st_path.is_file():
        plan(root, artifact_id)
    state = json.loads(st_path.read_text(encoding="utf-8"))
    rt = state.get("runtime") or active_runtime(root)

    invoked = False
    note = ""
    rc = 0
    out = ""

    if rt == "compose":
        compose = art / "compose.yml"
        if not compose.is_file():
            plan(root, artifact_id, runtime="compose")
        bin_dc = _which("docker")
        if bin_dc:
            rc, out = _run(
                [bin_dc, "compose", "-f", str(art / "compose.yml"), "up", "-d"],
                cwd=art,
            )
            invoked = True
            note = "docker compose up"
        else:
            note = "docker not on PATH — plan artifacts written; up skipped (honest)"
            rc = 0
    elif rt == "podman":
        play = art / "podman-play.yaml"
        pcompose = art / "podman-compose.yml"
        if not play.is_file() and not pcompose.is_file():
            plan(root, artifact_id, runtime="podman")
            play = art / "podman-play.yaml"
            pcompose = art / "podman-compose.yml"
        if _which("podman"):
            if play.is_file():
                rc, out = _run(["podman", "play", "kube", str(play)], cwd=art)
                note = "podman play kube"
            elif _which("podman-compose") and pcompose.is_file():
                rc, out = _run(
                    ["podman-compose", "-f", str(pcompose), "up", "-d"], cwd=art
                )
                note = "podman-compose up"
            else:
                note = "podman present but no play/compose file"
                rc = 1
            invoked = True
        elif _which("podman-compose") and pcompose.is_file():
            rc, out = _run(
                ["podman-compose", "-f", str(pcompose), "up", "-d"], cwd=art
            )
            invoked = True
            note = "podman-compose up"
        else:
            note = "podman/podman-compose not on PATH — plan written; up skipped"
            rc = 0
    elif rt == "k8s":
        mani = art / "k8s-manifests.yaml"
        if not mani.is_file():
            plan(root, artifact_id, runtime="k8s")
            mani = art / "k8s-manifests.yaml"
        if _which("kubectl"):
            rc, out = _run(["kubectl", "apply", "-f", str(mani)], cwd=art)
            invoked = True
            note = "kubectl apply"
        else:
            note = "kubectl not on PATH — plan written; up skipped (honest)"
            rc = 0
    else:
        note = f"unknown runtime {rt}"
        rc = 1

    state["status"] = "up" if (invoked and rc == 0) else ("planned" if rc == 0 else "up-failed")
    state["up"] = {
        "invoked": invoked,
        "note": note,
        "rc": rc,
        "out_tail": (out or "")[-500:],
    }
    write_state(root, artifact_id, state)
    state["_note"] = note
    state["_rc"] = rc
    return state


def down(root: Path, artifact_id: str = "default") -> dict[str, Any]:
    """Tear stack down for active runtime. Honest skip if binary missing."""
    art = artifact_dir(root, artifact_id)
    st_path = state_path(root, artifact_id)
    rt = active_runtime(root)
    if st_path.is_file():
        state = json.loads(st_path.read_text(encoding="utf-8"))
        rt = state.get("runtime") or rt
    else:
        state = {"artifact": artifact_id, "runtime": rt}

    invoked = False
    note = ""
    rc = 0
    out = ""

    if rt == "compose":
        compose = art / "compose.yml"
        if _which("docker") and compose.is_file():
            rc, out = _run(
                ["docker", "compose", "-f", str(compose), "down"], cwd=art
            )
            invoked = True
            note = "docker compose down"
        else:
            note = "docker/compose absent or no compose.yml — down skipped"
            rc = 0
    elif rt == "podman":
        play = art / "podman-play.yaml"
        pcompose = art / "podman-compose.yml"
        if _which("podman") and play.is_file():
            rc, out = _run(["podman", "kube", "down", str(play)], cwd=art)
            if rc != 0:
                # older podman: play kube --down
                rc2, out2 = _run(
                    ["podman", "play", "kube", "--down", str(play)], cwd=art
                )
                rc, out = rc2, out2
            invoked = True
            note = "podman kube down"
        elif _which("podman-compose") and pcompose.is_file():
            rc, out = _run(
                ["podman-compose", "-f", str(pcompose), "down"], cwd=art
            )
            invoked = True
            note = "podman-compose down"
        else:
            note = "podman absent or no play/compose — down skipped"
            rc = 0
    elif rt == "k8s":
        mani = art / "k8s-manifests.yaml"
        if _which("kubectl") and mani.is_file():
            rc, out = _run(
                ["kubectl", "delete", "-f", str(mani), "--ignore-not-found"],
                cwd=art,
            )
            invoked = True
            note = "kubectl delete"
        else:
            note = "kubectl absent or no manifests — down skipped"
            rc = 0
    else:
        note = f"unknown runtime {rt}"
        rc = 1

    state["status"] = "down"
    state["down"] = {
        "invoked": invoked,
        "note": note,
        "rc": rc,
        "out_tail": (out or "")[-500:],
    }
    write_state(root, artifact_id, state)
    state["_note"] = note
    state["_rc"] = rc
    return state


def ports_report(root: Path) -> dict[str, Any]:
    trail.ensure_layout(root)
    return load_ports(root)


# ---------------------------------------------------------------------------
# CLI (also imported by super_context)
# ---------------------------------------------------------------------------


def _resolve_root(args: Any) -> Path:
    """Honor explicit --root; otherwise detect from cwd."""
    explicit = getattr(args, "root", "") or ""
    if explicit:
        return Path(explicit).resolve()
    cur = Path.cwd().resolve()
    for p in [cur, *cur.parents]:
        if (p / ".git").exists() or (p / "SKILL.md").exists():
            return p
    return cur


def cmd_sandbox_cli(args: Any) -> int:
    root = _resolve_root(args)
    action = args.sandbox_action
    artifact_id = getattr(args, "artifact", None) or "default"

    if action == "ports":
        data = ports_report(root)
        print(json.dumps(data, indent=2))
        return 0
    if action == "plan":
        state = plan(root, artifact_id)
        print(
            f"SANDBOX plan artifact={artifact_id} runtime={state['runtime']}"
        )
        for k, v in (state.get("emitted") or {}).items():
            print(f"EMIT {k}={v}")
        print(f"PORTS {json.dumps(state['ports'])}")
        print(f"PROFILES {','.join(state.get('profiles') or [])}")
        return 0
    if action == "up":
        state = up(root, artifact_id)
        print(
            f"SANDBOX up artifact={artifact_id} runtime={state.get('runtime')} "
            f"status={state.get('status')}"
        )
        print(f"NOTE: {state.get('_note', '')}")
        return int(state.get("_rc") or 0)
    if action == "down":
        state = down(root, artifact_id)
        print(
            f"SANDBOX down artifact={artifact_id} runtime={state.get('runtime')} "
            f"status={state.get('status')}"
        )
        print(f"NOTE: {state.get('_note', '')}")
        return int(state.get("_rc") or 0)
    print(f"SANDBOX FAIL: unknown action {action}", file=sys.stderr)
    return 1


def cmd_runtime_cli(args: Any) -> int:
    root = _resolve_root(args)
    action = args.runtime_action
    paths = trail.ensure_layout(root)
    if action == "use":
        choice = (getattr(args, "backend", None) or "").strip()
        if choice not in RUNTIMES:
            print("RUNTIME FAIL: use compose|podman|k8s", file=sys.stderr)
            return 1
        set_runtime(root, choice)
        print(f"RUNTIME use backend={choice}")
        print(f"EMITTER dir={paths['runtime'] / choice}")
        # persist note that switch survives
        print(f"RUNTIME persisted active={paths['runtime'] / 'active'}")
        return 0
    if action == "status":
        cur = active_runtime(root)
        print(f"RUNTIME status backend={cur}")
        for name in RUNTIMES:
            mark = "*" if name == cur else " "
            print(f"  [{mark}] {name} -> {paths['runtime'] / name}")
        return 0
    print(f"RUNTIME FAIL: unknown action {action}", file=sys.stderr)
    return 1


__all__ = [
    "allocate_ports",
    "release_ports",
    "plan",
    "up",
    "down",
    "ports_report",
    "emit_compose",
    "emit_podman",
    "emit_k8s",
    "active_runtime",
    "set_runtime",
    "ensure_profiles",
    "load_profile",
    "active_profiles",
    "list_plugins",
    "cmd_sandbox_cli",
    "cmd_runtime_cli",
]
