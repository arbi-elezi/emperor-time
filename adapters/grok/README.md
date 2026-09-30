# Adapter — Grok Build (rich playbook)

Grok Build (`grok`, xAI terminal coding agent) is a **first-class harness**
for Emperor Time: native **AGENTS.md**, skills under `~/.grok/skills/` and
`./.grok/skills/`, plus the generic `~/.agents/skills/` discovery path. This
playbook is the depth target for Bet E2 — not Claude SessionStart parity
theater, and not a claim that every Grok-branded surface is the same product.

**Claim bar:** docs + recipe here are **rich**. Equal-UX-proven **only** when
a dated field receipt shows the **`grok` binary** path green on a foreign ask
**and** the PO accepts that claim language. AGENTS.md + scripts alone is
**structure proven, not equal-UX**. An OpenRouter `x-ai/*` call through
another host (OpenCode, curl) is a **model** note, not Grok Build proof.

**Surfaces (do not conflate):**

| Surface | Role in this pack |
|---|---|
| **Grok Build CLI (`grok`)** | Primary harness. TUI, headless `-p`, ACP. |
| **AGENTS.md + `scripts/`** | Canonical fallback. Always ship. Runnable with no `grok` binary. |
| **OpenRouter `x-ai/grok-code-fast-1`** | One named coding mid/flash **model** example when the host is OpenCode or another OpenAI-compat client. Not a substitute for Grok Build. |
| **xAI API / `xai-sdk`** | Mention only. Inference loop ≠ harness. |
| **Grok.com chat** | Mention only. Paste Core / Vow. No boot/done theater. |
| **Grok Bot (cloud teammate)** | Pointer only. If it is sitting in a project tree, follow AGENTS.md and this session path. Cursor-host depth stays in `adapters/cursor/` — do not deepen it here. |

**Deferred (not this adapter):** Cursor very-rich (sibling lane), Colibrì
ownership, Android C++, multi-16B graph runtimes.

---

## 0. Prereqs

```bash
# Grok Build CLI (client runs; orchestrator never logs in)
curl -fsSL https://x.ai/cli/install.sh | bash
# docs: https://docs.x.ai/build
export PATH="$HOME/.local/bin:$PATH"   # install location varies — check `command -v grok`
grok version    # or: grok --version — verify the flag this release
grok --help
```

Auth is the client's: browser OAuth (`grok login`, verify the subcommand at
dowse) **or** `XAI_API_KEY` in the environment. Emperor Time does not perform
login and does not read or print keys (Vow of Consent).

Optional, **model-via-other-host only** (not required for the AGENTS.md path):
`OPENROUTER_API_KEY` when the host is OpenCode. Never commit the key.

If `grok` is absent or unauthenticated, stop the binary lane and continue with
§1b. That is a valid **structure** run. It is not equal-UX.

Iron gates never soften for mid/flash models. Judgment stays **off** for toy
smoke (see `config.snippet.yaml`).

---

## 1. Install / paste path

### 1a. Skills directory (preferred when `grok` is present)

```bash
# from emperor-time tip
./scripts/install.sh grok user
# → ~/.grok/skills/emperor-time/
./scripts/install.sh grok project /path/to/target
# → <target>/.grok/skills/emperor-time/
# Windows: .\scripts\install.ps1 -Harness grok -Scope user
#          .\scripts\install.ps1 -Harness grok -Scope project -Project C:\repos\app
```

Grok also discovers `~/.agents/skills/`. `./scripts/install.sh generic-agents user`
remains valid and is not a second doctrine tree.

**Manual copy (fallback)** if you do not run `install.py`: copy the same set
`scripts/lib/install.py` ships (`SKILL.md`, `README.md`, `chains`,
`references`, `templates`, `adapters`, `scripts`) into
`~/.grok/skills/emperor-time/` or `<target>/.grok/skills/emperor-time/`.
Do not invent a vendor-specific vow file.

Invoke (verify flag spelling each release — `grok --help`):

```bash
grok inspect          # lists rules / skills the CLI actually found
grok                  # TUI in the target project
grok -p "<task>"      # headless; confirm -p still means print/headless
```

### 1b. AGENTS.md (canonical standing orders — always)

Grok Build treats `AGENTS.md` as project instructions (same family as Codex).
Drop the repo-root `AGENTS.md` from the Emperor Time tip into the **target**
project (or append the short pointer below). Symlink or copy `scripts/` so
`boot` / `activate` / `done` resolve. `grok inspect` should list that
`AGENTS.md`; if it does not, the binary did not see the file (PATH, cwd, or
install), which is **blocked** / operator — not a model fail.

Minimal pointer (if the skill folder is already installed):

```markdown
## Emperor Time discipline

This repo runs under Emperor Time. Before creative work: silent boot, then
MUST-route (`scripts/emperor activate` / `route`), then ask→spec + harness-plan
at tiny by default. Iron gates never soft. Ledgers → `.emperor/`.
If the skill folder is missing, apply `adapters/generic/EMPEROR_TIME.core.md`.
```

---

## 2. Session path (boot → activate/route → done)

Grok Build has **no** Claude `SessionStart` hook. Agent (or human) must run:

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

Config bridge: copy `adapters/grok/config.snippet.yaml` → project
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

## 3. Providers / models

### Native Grok Build (verify at dowse — no catalog)

```bash
grok models           # whatever this install lists; do not freeze a slug here
grok -m <id>          # only if --help still documents -m
grok --effort <lvl>   # only if --help still documents --effort
```

Model ids move. Record the id you actually invoked in the receipt. Do not
paste a second native catalog into this file.

### OpenRouter mid/flash (one example, other host)

When the host is OpenCode or any OpenAI-compat client — **not** Grok Build:

```bash
# OPENROUTER_API_KEY in the host env / OpenCode auth store — never commit it.
opencode run -m openrouter/x-ai/grok-code-fast-1 --dir . "<ask>"
```

Locked example: **`x-ai/grok-code-fast-1`** only. No second slug in this
playbook. Label the receipt "Grok **model** via OpenCode" (or via curl). Do
not sell that connectivity as Grok Build equal-UX.

### xAI API / `xai-sdk` (mention only)

`xai-sdk` (PyPI) and `https://api.x.ai/v1` (OpenAI-compat) are inference.
They are not a coding harness: no `grok inspect`, no skill dir, no session
boot. Paste `adapters/generic/EMPEROR_TIME.core.md` or the Vow card and drive
your own loop if you must. Not equal-UX.

### Grok.com chat (mention only)

Web chat has no project tools and no gates. Paste
`adapters/generic/EMPEROR_TIME.core.md` (or the Vow card) as instructions.
Do not perform boot/done theater and call it a harness run.

---

## 4. Failure modes (triage)

| Symptom | Likely class | Action |
|---|---|---|
| No `.emperor/host.env` / activate never run | **ET-bug** / operator skip | Run boot + activate; do not blame the model |
| `done` FAIL on a probe the change never touched | **ET-bug** (probe/path) | Fix DONE.md / cwd / scripts wiring |
| Iron gate refuses forge/secrets without consent | **PASS** (iron working) | Expected — do not soften |
| Model ignores MUST-route / skips ask→spec | **model-FAIL** | Record FAIL; keep iron; tighten the AGENTS.md pointer |
| `grok` missing on PATH | **blocked** (binary) | AGENTS.md+scripts only; no equal-UX claim |
| No `XAI_API_KEY` and `grok login` not done | **blocked** (auth) | Client auths; orchestrator does not log in or read keys |
| `grok inspect` shows no AGENTS.md | **blocked** / operator | Wrong cwd, file not at project root, or CLI did not load rules |
| OpenRouter 401 / 429 on `x-ai/grok-code-fast-1` via another host | **blocked** (model-via-other-host) | Key/quota; does not indict the AGENTS.md structure path |

Triage labels for receipts: **ET-bug** | **model-FAIL** | **PASS** | **blocked**
(binary / auth / PATH).

Do not import another harness's hang rows here. If a future `grok -p` probe
stalls under a pipe, document **that** probe — do not copy lore from OpenCode.

---

## 5. Grok as enlisted worker (Steal Chain)

```bash
# verify flags at dowse (`grok --help`); do not enlist without consent
grok -p "<scoped worker prompt>"
grok agent stdio          # ACP, if this release still exposes it
```

Prepend the Vow card from `adapters/generic/EMPEROR_TIME.core.md` when the
worker host lacks the skill install. Consent before enlist. No auth bypass.

---

## 6. QA entrypoint

Repeatable toy smoke without a frontier Grok session: **`QA-SMOKE.md`**
(this directory).

---

## Why Grok in the roster

xAI ships a terminal coding agent with AGENTS.md and skill dirs, and
OpenRouter carries `x-ai/grok-code-fast-1` for mid/flash buyers who are not
on Claude Code. Rich docs here; structure can be proven without the binary.
Equal-UX stays withheld until `grok` itself is green on a foreign ask and
the PO accepts the claim.
