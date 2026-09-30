# Adapter: Colibrì (integrate-if-you-want; inference host)

**Claim wording:** Colibrì as inference host, integrate-if-you-want.
Harness ownership and native equal-UX are out of scope.

[JustVugg/colibri](https://github.com/JustVugg/colibri) is a local inference
engine (`coli serve` OpenAI-compatible HTTP API). It does **not** own boot,
activate, MUST-route, AGENTS.md / skill discovery, or iron gates. Emperor Time
stays the orchestrator. The harness (OpenCode, Cursor, or a generic
OpenAI-compat client) loads ET. Colibrì is the model server behind that client.

Do **not** ship Colibrì runtime inside ET. Do **not** claim Colibrì loads
`AGENTS.md`. Target is **JustVugg/colibri** only. A separate search hit for
LastEld/AMS "Colibri System" is a name collision: treat it as out of scope /
stale unless a live URL and commit are supplied.

**Surfaces (do not conflate):**

| Surface | Role in this pack |
|---|---|
| **`coli serve` (JustVugg/colibri)** | Local OpenAI-compat inference host. Default base URL `http://127.0.0.1:8000/v1`. |
| **OpenCode / Cursor / generic client** | Harness that loads ET (`AGENTS.md`, `SKILL.md`, scripts). Points at Colibrì as provider. |
| **AGENTS.md + `scripts/`** | Canonical structure path. Always ship. Runnable with no `coli` binary. |
| **llama.cpp / colibri-toy stand-in** | Optional OpenAI-compat **shape** smoke only. Never Colibrì engine PASS. |

**Out of scope:** Colibrì engine build in-repo, GLM-5.2 download, cluster mode,
AMS Colibri System, native equal-UX chase, claiming Colibrì owns boot/activate.

---

## 0. Stranger recipe (≤1 page)

Install and serve Colibrì, point the harness at the base URL, boot and activate
ET, make a tiny ask, then `done`. Fail closed on triage.

1. **Install Colibrì** (upstream docs): build or install `coli`, convert a model
   directory the engine supports. Run `coli doctor` and `coli plan` first.
2. **Serve (localhost):**

   ```bash
   COLI_MODEL=/path/to/model ./coli serve \
     --host 127.0.0.1 --port 8000 --model-id local-colibri
   ```

   Base URL for clients: `http://127.0.0.1:8000/v1`. Model id: whatever you
   passed to `--model-id` (example: `local-colibri`). If the client insists on
   a key and you have not set `COLI_API_KEY`, use a non-empty dummy (example:
   `local`).
3. **Wire ET on the client** (not inside Colibrì):
   - OpenCode: ET OpenCode adapter + provider at that base URL
     (`adapters/opencode/`, `config.snippet.yaml` here).
   - Cursor: tip `AGENTS.md` / rules + local OpenAI-compat provider
     (`adapters/cursor/`).
   - Generic: inject `adapters/generic/EMPEROR_TIME.core.md` as system prompt
     (`adapters/generic/`).
4. **Boot / activate** in the target project:

   ```bash
   bash scripts/boot.sh
   python3 scripts/lib/activate.py --cwd . -u "<tiny ask>"
   # open ACTIVATION next=
   ```

5. **Tiny ask**, smallest change, then:

   ```bash
   python3 scripts/lib/done.py .emperor/tasks/<id>
   ```

**Fail-closed triage:** if `coli` is missing, mark **Colibrì engine live =
BLOCKED** (not a silent skip). If structure `done` is green without `coli`,
that is **structure PASS** only. Do not sell llama.cpp / toy HTTP as Colibrì
engine PASS. Iron never softens.

Detail below. QA entry: `QA-SMOKE.md`.

---

## 1. Prerequisites

```bash
# Upstream Colibrì (verify install at dowse time)
# docs: https://github.com/JustVugg/colibri
# quickstart: docs/quickstart.md ; API: docs/api.md ; env: docs/ENVIRONMENT.md

coli doctor    # read-only readiness
coli plan      # read-only placement / resource plan
```

Honesty on hardware: Colibrì's advertised frontier containers (example GLM-5.2
int4 ~372 GB) need large disk and comfortable RAM. Small engines on the roster
(example OLMoE-class) may fit a modest host. Record what you actually have
(RAM, free disk, GPU or none). Do not pretend a GLM-class run when the box
cannot host it.

Iron gates never soften for local models. Judgment stays **off** for toy smoke
(see `config.snippet.yaml`).

---

## 2. Serve recipe

```bash
COLI_MODEL=/path/to/model ./coli serve \
  --host 127.0.0.1 --port 8000 --model-id local-colibri
```

| Knob | Typical value |
|---|---|
| Base URL | `http://127.0.0.1:8000/v1` |
| Model id | `local-colibri` (or your `--model-id`) |
| API key | unset by default; dummy non-empty if client insists; set `COLI_API_KEY` before any non-local bind |

Documented surface includes `/v1/models`, `/v1/chat/completions`, and related
endpoints. Tool-calling is **engine-dependent** (check Colibrì's API matrix).
Text-only is the safe smoke assumption. Keep first validation prompts short;
large system prompts plus disk-streaming MoE can look hung on prefill.

**Security:** keep the default localhost bind. Set `COLI_API_KEY` and exact host
allowlists before any non-local exposure. Never commit keys into ET or receipts.

---

## 3. Wire ET on the client side

Layering (client loads ET; Colibrì only serves tokens):

```text
ET SKILL.md / AGENTS.md or generic core
        (loaded by harness / client)
OpenCode, Cursor, generic OpenAI client, etc.
        (sends system + user + tools)
Colibrì localhost API (coli serve)
        (local model)
```

### OpenCode

Install / paste per `adapters/opencode/`. Copy or merge
`adapters/colibri/config.snippet.yaml` into the project's `.emperor/config.yaml`
(judgment off, iron hard). Point an OpenAI-compat provider at
`http://127.0.0.1:8000/v1` with your model id. Verify with `opencode models`
when available.

### Cursor

Keep tip `AGENTS.md` / `SKILL.md` (and optional `.cursor/rules`). Configure
Cursor's local / custom OpenAI-compat provider the same way. Depth stays in
`adapters/cursor/`. Do not claim Cursor equal-UX from this pack.

### Generic OpenAI-compat client

Inject `adapters/generic/EMPEROR_TIME.core.md` (or the Vow card on small
models) as the system prompt. Drive boot / activate / done yourself via
`scripts/`. Same pattern as other local OpenAI-compat workers.

### Session path (always)

```bash
# cwd = foreign or target project
bash scripts/boot.sh
# read .emperor/host.env and .emperor/survey.md

python3 scripts/lib/activate.py --cwd . -u "<ask>"
# open ACTIVATION next=

python3 scripts/lib/route.py "<ask>"

python3 scripts/lib/ask_spec.py --emit --effort-class tiny \
  --write .emperor/tasks/<id>/ask-spec.md "<ask>"

# smallest change only

python3 scripts/lib/done.py .emperor/tasks/<id>
```

---

## 4. Capability / latency triage

| Topic | Expectation |
|---|---|
| Modality | Text completions / chat. No promise of vision or multimodal. |
| Tools | Engine-dependent. Several families reject tools. Keep smoke tool-free. |
| Concurrency | One generation at a time / queued. No continuous-batching promise. |
| Latency | Prefill on disk-streaming MoE can be slow. Short prompts for first smoke. |
| ET ownership | Boot, activate, gates, done stay on ET + harness. Never on `coli`. |

Triage labels for receipts: **PASS** | **ET-bug** | **model-FAIL** | **blocked**
(engine missing / disk / RAM / auth). Separate labels for **structure**,
**Colibrì engine live**, and optional **OpenAI-compat shape** (toy / llama.cpp).

---

## 5. Recursive build note

If you use OpenCode plus an ORI model (example space-bunny-alpha) while shipping
this pack, label that as **coding toolchain only** (ET + ORI recursive build).
It is **not** Colibrì proof.

---

## 6. QA entrypoint

Repeatable structure + honesty rules: **`QA-SMOKE.md`** (this directory).
