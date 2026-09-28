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

## Sandbox / sim engine (stubs in v1)

Powers: sandboxing, mocking, simulating, isolating, parallel testing.

- Ports allocated per artifact (`.emperor/sandbox/ports.json`).
- Stacks raised per artifact; simulator emits docker-compose (or equivalent)
  that wires plugin repos so they fire together
  (`emperor sandbox plan` merges `sot/plugins/*/compose.fragment.yml`).

CLI stubs:

```
emperor sot status|sync|add-plugin <name> [url]
emperor sandbox plan|up|down|ports [--artifact ID]
emperor context artifacts list|stub-create
```

`up`/`down`/`sync` are honest stubs in v1 (print NOTE; do not shell out to
docker/git fetch unless a later vertical deepens them).

## Pluggable runtimes

Sandbox simulator backends: **docker compose AND k8s AND podman**.
Compose is not the only emitter. Select with:

```
emperor runtime use compose|podman|k8s
emperor runtime status
```

## Blind credentials

Unified secret obtain/inject into workspace/stacks **without the LLM
seeing values** (vault / 1Password / env-file broker). Agent sees
names + status only — never plaintext on stdout.

```
emperor secrets list
emperor secrets declare --name DB_PASSWORD
emperor secrets inject --artifact <id>   # receipt only; no values printed
```

## Unified workspace env

Env management is for the *workspace* (multi-repo artifact), not
per-repo classical dotenv alone — **repo≠workspace**. ET owns merge/
override across plugins.

```
emperor env show    # redacted
emperor env sync    # merge stub; no secrets from example
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
