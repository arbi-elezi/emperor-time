# Adapter — OpenCode (rich playbook)

OpenCode (Anomaly / `opencode-ai` CLI; formerly SST) is a **first-class OSS
harness** for Emperor Time: multi-provider (OpenRouter mid/flash, local
OpenAI-compat, free OpenCode catalog models). This playbook is the depth target
for Small C — not Claude SessionStart parity theater. Claude remains a supported
native path; ORI/OpenCode is the visible stranger mid-model route (not a
Claude-first reposition).

**Claim bar:** docs + recipe here are **rich**. Equal-UX-proven only when a
dated field receipt shows the **OpenCode binary** path green on a foreign ask.
AGENTS.md+scripts fallback alone is **not** equal-UX-proven.

**Deferred (not this adapter):** Cursor very-rich, Grok, Colibrì
*ownership* (inference-host integrate pack lives in `adapters/colibri/`; this
adapter does not own Colibrì), Android C++, multi-16B graph runtimes. Colibrì
remains an optional **OpenAI-compat inference** backend you can point OpenCode
at; do not own the runtime here.

---

## 0. Prereqs

```bash
# OpenCode CLI (verify at install time)
npm install -g opencode-ai          # bin: opencode (often lands in ~/.local/bin)
# or: curl -fsSL https://opencode.ai/install | bash
export PATH="$HOME/.local/bin:$PATH"   # PATH footgun: fresh shells without this → "No such file"
# or invoke absolute: ~/.local/bin/opencode  (Linux ELF may be named opencode.exe)
opencode --version                  # observed example: 1.18.x
opencode --help
```

Local toy / OpenAI-compat (optional for QA smoke):

```bash
# Ollama example (toy models: llama3.2:3b / qwen2.5:3b / heavy-quant)
ollama serve                        # default http://127.0.0.1:11434
ollama pull llama3.2:3b
```

Iron gates never soften for weak models. Judgment stays **off** for toy smoke
(see `config.snippet.yaml`).

---

## 1. Install Emperor Time into OpenCode

### 1a. Skills directory

```bash
# from emperor-time tip
./scripts/install.sh opencode user
# → ~/.opencode/skills/emperor-time/
# Windows: .\scripts\install.ps1 -Harness opencode -Scope user
```

OpenCode skill format may differ (Handlebars / native skill files). At dowse
time verify with `opencode --help` and docs; if plain `SKILL.md` folders are
ignored, Chain-Jail-adapt: flatten master `SKILL.md` into the expected shape
(frontmatter kept). Do not invent a second doctrine tree.

Invoke (verify flag spelling each release):

```bash
opencode run --skill emperor-time "<task>"
# or project-dir form:
opencode run --dir /path/to/repo "<task>"
```

### 1b. AGENTS.md (canonical standing orders)

OpenCode treats `AGENTS.md` as canonical project instructions. Drop the
repo-root `AGENTS.md` from Emperor Time tip into the **target** project (or
append the short pointer below). Pair with a `scripts/` symlink or absolute
path to tip scripts so `boot` / `activate` / `done` resolve.

Minimal pointer (if you already installed the skill folder):

```markdown
## Emperor Time discipline

This repo runs under Emperor Time. Before creative work: silent boot, then
MUST-route (`scripts/emperor activate` / `route`), then ask→spec + harness-plan
at tiny by default. Iron gates never soft. Ledgers → `.emperor/`.
If the skill folder is missing, apply `adapters/generic/EMPEROR_TIME.core.md`.
```

---

## 2. Session path (boot → activate/route → done)

OpenCode has **no** Claude `SessionStart` hook. Agent (or human) must run:

```bash
# cwd = foreign or target project
bash scripts/boot.sh                 # or: python3 $ET/scripts/lib/boot.py --root .
# read:
#   .emperor/host.env
#   .emperor/survey.md
#   .emperor/eval.log   # only when this tree *is* Emperor Time

python3 scripts/lib/activate.py --cwd . -u "<ask>"
# open ACTIVATION next=  (MUST-route before clarifying / exploring / coding)

python3 scripts/lib/route.py "<ask>"   # exit 1 → fall back to SKILL tables

# tiny default — emit ask→spec (chains harness-plan):
python3 scripts/lib/ask_spec.py --emit --effort-class tiny \
  --write .emperor/tasks/<id>/ask-spec.md "<ask>"

# …do the smallest change…

python3 scripts/lib/done.py .emperor/tasks/<id>
# exit 0 = green; else FAIL + ledger (honest)
```

Do not ask the client their OS/shell/language — read `host.env` / `survey.md`.
Foreign/lost tree: `scripts/emperor identify <path>`.

Config bridge: copy `adapters/opencode/config.snippet.yaml` → project
`.emperor/config.yaml` (or merge knobs). Prefer `python3 scripts/lib/config.py`
for config-only smoke so boot does not stall.

---


## MUST-route (before creative work)

Silent boot is not enough. Before clarifying questions, exploring, or writing
code, open one governing file from the `SKILL.md` tables, or run
`scripts/emperor route "<utterance>"` / `scripts/emperor activate` (or
`emperor activate "<utterance>"`) and open `ACTIVATION next=`. Same bite as
Claude SessionStart MUST-route; Emperor Time stays the orchestrator (no foreign
master router).

## 3. Providers — OpenRouter mid/flash + local OpenAI-compat

### OpenRouter mid/flash (pattern)

```bash
# Credentials via OpenCode providers (do not paste secrets into ledgers)
opencode providers          # aliases: auth
# Set OPENROUTER_API_KEY in the host env / OpenCode auth store — never commit it.

opencode run -m openrouter/<mid-or-flash-slug> --dir . "<ask>"
```

Pick **one** mid and **one** flash slug at dowse time (no provider catalog
sprawl). ET structure (gates, ask→spec, done) is the usefulness thesis when
tokens are cheap — not token-shave theater.

### Local OpenAI-compat (Ollama / Colibrì-as-inference)

```bash
# Ollama OpenAI-compatible endpoint (typical):
#   http://127.0.0.1:11434/v1
# Point OpenCode / provider config at that base URL with a toy model id
# (llama3.2:3b | qwen2.5:3b | heavy-quant). Verify with `opencode models`.

opencode run -m ollama/llama3.2:3b --dir . "<tiny ask>"
```

**Colibrì:** not an owned harness here. Integrate-if-you-want pack:
`adapters/colibri/` (JustVugg/colibri as OpenAI-compat inference host). If
present on the host, point OpenCode at `http://127.0.0.1:8000/v1` (or your
bind), document base URL + model id in NOTES, and keep ET loaded on the
OpenCode side. Do not ship Colibrì runtime inside ET.

### Preferred free OpenRouter (P0 lab)

```bash
# OPENROUTER_API_KEY must be set in the environment (never commit/print).
# Under non-TTY (agent/CI pipe), wrap with script/pty — see Failure modes.
opencode run -m openrouter/stealth/space-bunny-alpha --dir . "<tiny ask>"
# timeout 20 script -q -c 'opencode run -m openrouter/stealth/space-bunny-alpha --dir . "<tiny ask>"' /dev/null
```

Local fallback when OpenRouter/OpenCode fails: llama.cpp CPU +
Qwen2.5-Coder 1.5B Q4_K_M (colibri-toy probe path). Do not block on Ollama.

### Free OpenCode catalog models

`opencode models` may list `opencode/*-free` entries. Useful for connectivity
smoke; **do not** sell a free-catalog PASS as Astra-bridge / mid-16B proof.

---

## 4. Failure modes (triage)

| Symptom | Likely class | Action |
|---|---|---|
| No `.emperor/host.env` / activate never run | **ET-bug** / operator skip | Run boot + activate; do not blame the model |
| `done` FAIL on probe the model never touched | **ET-bug** (probe/path) | Fix DONE.md / cwd / scripts wiring |
| Iron gate refuses forge/secrets without consent | **PASS** (iron working) | Expected — do not soften |
| Model ignores MUST-route / skips ask→spec | **model-FAIL** | Record FAIL; keep iron; try clearer AGENTS.md |
| OpenCode binary missing | **blocked** | AGENTS.md+scripts fallback only; no equal-UX claim |
| `timeout: … No such file` / `opencode` not found | **PATH footgun** | Add `~/.local/bin` to PATH or use absolute `~/.local/bin/opencode` — not the hang |
| Hang after log `message=init`; timeout → EXIT **124**; empty stdout | **harness hang (non-TTY)** | OpenCode 1.18.x `run` stalls under pipe/non-TTY. Wrap with `script -q -c 'opencode run …'` or python `pty`; keep `timeout` ≤30s while probing |
| `--format json` / `--interactive` still 124 under pipe | **same hang class** | Those flags do **not** unblock; needs a real TTY |
| Toy model missing (no Ollama / no weights) | **blocked** (model portion) | Ship docs + smoke recipe; receipt discloses |

Triage labels for receipts: **ET-bug** | **model-FAIL** | **PASS** | **blocked** (binary/PATH/hang).

### Non-TTY hang workaround (binary lane)

Agent/CI shells often pipe stdout → OpenCode `run` hangs after `init` (EXIT 124). Prefer:

```bash
# always bound probes
timeout 20 script -q -c 'opencode run -m openrouter/stealth/space-bunny-alpha --dir . "<ask>"' /dev/null
# or: python3 -c 'import pty,sys; sys.exit(pty.spawn(["opencode","run",...]))'
```

Portability: GNU/util-linux `script -q -c 'cmd' file` vs BSD/Darwin `script -q file cmd` (no `-c`; command after the typescript path). Prefer a real TTY/PTY — the `python3` `pty.spawn` one-liner is the portable recipe.

Structure path (AGENTS.md + `boot`/`activate`/`done`) and direct OpenRouter HTTPS remain valid when the binary lane is pipe-blocked. Direct HTTPS is a **compat/fallback probe**, not **ORI live PASS** (TTY-as-gate — see below). **Equal-UX-proven** still requires a dated **binary** green receipt **and** PO accept of claim language — do not auto-claim from docs or AGENTS-only PASS.

---

## 5. OpenCode as enlisted worker (Steal Chain)

```bash
opencode run "<scoped worker prompt>"
opencode serve
opencode run --attach http://localhost:4096 "<prompt>"
```

Prepend the Vow card from `adapters/generic/EMPEROR_TIME.core.md` when the
worker host lacks the skill install. Consent before enlist.

---

## 6. QA entrypoint

Repeatable toy smoke without frontier models: **`QA-SMOKE.md`** (this directory).

---

## Why OpenCode in the roster

It fronts many providers, including local/OpenRouter mid-flash — the practical
path for buyers who are not on Claude Code. Rich docs here; proof via receipts.
