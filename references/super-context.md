# Super-context + thoughttrail + inverted workspace

Emperor Time wraps the project *contextually* (virtual context = as large as
the host allows). Meta-explanation + graphing make the repo workable without
mass-grep. **No embeddings. No Graphify code or license-tainted ports.**

## Graph-over-grep (real in v1)

Deterministic Markdown extract → local SQLite graph
(`.emperor/context/graph.sqlite`):

| Confidence | Meaning |
|---|---|
| `EXTRACTED` | Explicit in source (heading, link, fence, ADR/RFC cite) |
| `INFERRED` | Resolved locally (relative link → known file) |

Cores: `scripts/lib/md_graph.py`, `context_store.py`, `thoughttrail.py`,
`super_context.py`. Thin twin: `scripts/context.sh` / `.ps1`.

### Tiers

- **L0** — highest-degree nodes + connected-component communities
  (`.emperor/context/l0.md`). **Load L0 before mass-grep** (resume path).
- **L1** — `find` / `path` / `explain` on edges.
- **L2** — `slice` path:line cites only when asked.

### Thoughttrail

Append-only `.emperor/thoughttrail/trail.jsonl` — reasoning entries with
`node_ids[]` + optional ledger/task paths. CLI: `emperor context trail …`
or `emperor thoughttrail …`.

## Inverted workspace (doctrine + stubs in v1)

Inside ET, repo clones are parallel workable *artifacts* whose job is a fully
SDLC-tested PR. ET owns the workspace model — the live checkout of main is
not the only workspace.

| Path | Role |
|---|---|
| `.emperor/context/` | graph.sqlite + l0.md |
| `.emperor/thoughttrail/` | trail.jsonl |
| `.emperor/sot/` | fetch-only SOT pointer; `plugins/<repo>/` mirrors |
| `.emperor/artifacts/<id>/` | multi-repo worktrees + generated `compose.yml` |
| `.emperor/sandbox/` | ports.json, mock/sim manifests |
| `.emperor/sandbox/runtime/{compose,podman,k8s}/` | pluggable emitters |
| `.emperor/env/` | workspace.env.example + overlays (no secrets in git) |
| `.emperor/secrets/` | name-only manifest; broker inject (blind) |

- **SOT** = copies of bound repos (primary `origin/main` + plugins) kept
  current for context + regression reference. **Never mutate SOT.**
- **Regression** runs from artifact *copies*, not by checking out over SOT.
- **Workspace ≠ one repo** — a task may bind multiple repos; each is a SOT
  *plugin* recognized by the sandbox engine.

## Sandbox / sim engine (real in v0.4.135+)

Powers: sandboxing, mocking, simulating, isolating, parallel testing.
Core: `scripts/lib/sandbox_engine.py` (wired from `super_context.py`).

- **Port allocator** — persist `.emperor/sandbox/ports.json`; no collisions
  across parallel artifacts (scans all allocations before assign).
- **Compose emitter** — `emperor sandbox plan` merges
  `sot/plugins/*/compose.fragment.yml` (+ artifact plugin list) into
  `.emperor/artifacts/<id>/compose.yml`.
- **Podman backend** — emits `podman-compose.yml` (compose-compat) and
  `podman-play.yaml` for `podman play kube`.
- **K8s backend** — emits Namespace + Deployment + Service (+ isolate
  NetworkPolicy) into `k8s-manifests.yaml`.
- **Profiles** (loadable stubs under `.emperor/sandbox/profiles/`):
  `isolate` (internal network), `mock` (placeholder svc), `simulate`.

CLI:

```
emperor sot status|sync|add-plugin <name> [url]
emperor sandbox plan|up|down|ports [--artifact ID]
emperor context artifacts list|stub-create|sync
emperor runtime use compose|podman|k8s
emperor runtime status
```

`sandbox up|down` invoke docker compose / podman (play kube|compose) /
kubectl when on PATH; otherwise honest skip (plan artifacts still written).
**SOT + artifacts sync (v0.4.134):** `sot add-plugin` → `git clone --mirror`;
`sot sync` fetches; `artifacts sync` clones working copies under
`.emperor/artifacts/<id>/repos/<plugin>/` (never mutates SOT).
**HARD-GATE (v0.4.149):** `--reject-mutated-sot` / `--check-sot` refuse SOT READY
when plugins/mirrors missing or mirrors are non-bare (working-tree mutation risk).
`--reject-no-sandbox-plan` / `--check-sandbox` refuse SANDBOX READY without
ports.json + runtime/active + emitted plan. Idle → SKIP (vacuous). G0 wires both.

## Pluggable runtimes

Sandbox simulator backends: **docker compose AND k8s AND podman**.
Compose is not the only emitter. Selection **persists** in
`.emperor/sandbox/runtime/active`:

```
emperor runtime use compose|podman|k8s
emperor runtime status
```

Then `emperor sandbox plan` emits for the active runtime.

## Blind credentials (real in v0.4.136+)

Unified secret obtain/inject into workspace/stacks **without the LLM
seeing values** (vault / 1Password / env-file broker). Agent sees
names + status only — never plaintext on stdout.

Core: `scripts/lib/secrets_broker.py` (wired from `super_context.py`).

- **Manifest** — `.emperor/secrets/manifest.json` (names + status).
- **Bind** — `declare --from-file PATH` copies into gitignored
  `secrets/values/` (or `EMPEROR_SECRET_<NAME>`); value never echoed.
- **Inject** — env-file broker writes artifact `.env.secrets` (outside
  git) + public receipt; vault/1password write hook placeholders.
- **HARD-GATE** — `--reject-secret-leak` (always-fail) /
  `--check-env-redacted PATH` (refuse dumps with unredacted secret values).

```
emperor secrets list
emperor secrets declare --name DB_PASSWORD
emperor secrets declare --name DB_PASSWORD --from-file ./local.secret
emperor secrets inject --artifact <id>   # receipt only; no values printed
emperor secrets --reject-secret-leak
emperor secrets --check-env-redacted PATH
```

## Unified workspace env (real in v0.4.136+)

Env management is for the *workspace* (multi-repo artifact), not
per-repo classical dotenv alone — **repo≠workspace**. ET owns merge/
override across SOT plugins for an artifact.

Core: `scripts/lib/workspace_env.py`.

- **show** — merged view of `workspace.env.example` + `workspace.env` +
  `overlays/*.env` + `sot/plugins/*/env.fragment`; values **redacted**.
- **sync** — writes `.emperor/env/overlays/<artifact>.managed.env`
  without echoing secrets; secret keys kept as `${NAME}` placeholders
  (broker inject owns plaintext).

```
emperor env show [--artifact ID]    # redacted merge
emperor env sync [--artifact ID]    # managed overlay; no secret echo
```

Layout: `.emperor/env/workspace.env.example`, `overlays/`, gitignore
keeps real `workspace.env` out of git.

## Invoke

```
emperor context          # CONTEXT card
emperor context build
emperor context l0
emperor context find "ADR"
emperor context path alpha beta
emperor context explain "Alpha System"
emperor context trail append --text "…" --nodes id1,id2
emperor context slice "alpha"
```

Aliases: `thoughttrail`, `super-context`, `sandbox`, `sot`,
`runtime`, `env`, `secrets`.
