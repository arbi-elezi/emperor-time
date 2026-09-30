# Adapter — Cursor (rich playbook)

Cursor (IDE rules + optional `cursor-agent` CLI) is a **documented host** for
Emperor Time. This playbook mirrors OpenCode-class depth with **Cursor-native**
wiring — not Claude SessionStart parity theater, and not a copy of OpenCode
CLI flags sold as Cursor commands.

**Claim bar:** docs + recipe here are **rich** (structure lane). Equal-UX is
**HOLD**: structure PASS (boot→activate→done on a foreign tiny ask) is **not**
equal-UX-proven. Equal-UX-proven only when PO accepts claim language after a
dated receipt shows the **Cursor binary / IDE** path green on a foreign ask
with auth honest. AGENTS.md+scripts fallback alone is **not** equal-UX-proven.

**Deferred (not this adapter):** Grok ownership, Colibrì *ownership*
(inference-host integrate pack lives in `adapters/colibri/`; this adapter does
not own Colibrì), Android C++, multi-16B graph runtimes. **ORI live**
(OpenRouter via OpenCode or direct OpenAI-compat) is the **supported live
model route** when `cursor-agent` is Not logged in / binary BLOCKED. Host
labeled; not Cursor equal-UX.

---

## 0. Prereqs

Two surfaces — do not conflate them:

| Surface | What it is | ET load path |
|---|---|---|
| **Cursor IDE** | Editor + project rules / skills | Point rules at tip `AGENTS.md` + `SKILL.md`; optional `.cursor/rules` |
| **`cursor-agent` CLI** | Headless agent binary (often `~/.local/bin/cursor-agent` → `agent`) | Same ET scripts; auth must be honest before binary-lane claims |

```bash
# PATH footgun: fresh shells without ~/.local/bin → "command not found"
export PATH="$HOME/.local/bin:$PATH"
command -v cursor-agent || command -v agent
cursor-agent --version    # or: agent --version
cursor-agent status       # expect "Logged in" or "Not logged in"
```

**Auth honesty (iron):** if `cursor-agent status` prints **`Not logged in`**,
label the binary lane **BLOCKED**. Do **not** chase login, paste API keys into
ledgers, invent auth bypass, or set `CURSOR_API_KEY` into committed files.
Structure path (AGENTS.md + tip scripts) still runs without Cursor auth.

Local toy / OpenAI-compat (optional for QA smoke when Cursor hosts a model
route): Ollama / OpenAI-compat endpoint — iron gates never soften; judgment
**off** for toy smoke (see `config.snippet.yaml`).

---

## 1. Install Emperor Time into Cursor

There is **no** `./scripts/install.sh cursor` harness today
(`install.py` harnesses: claude-code | kimi | codex | opencode | generic-agents).
Use **honest paste / pointer** — do not invent a Cursor marketplace install
or claim install.sh covers Cursor.

### 1a. Project rules → AGENTS.md + SKILL.md

In the **target** project (foreign or ET tip):

1. Copy tip `AGENTS.md` into the project root (or append the short pointer below).
2. Ensure Cursor project rules / User Rules / `.cursor/rules` **point at** or
   include the standing orders from tip `AGENTS.md` and load doctrine from tip
   `SKILL.md` (one file at a time — no second doctrine tree).
3. Symlink or absolute-path tip `scripts/` so `boot` / `activate` / `done` resolve.

Minimal pointer (if rules already reference the skill folder elsewhere):

```markdown
## Emperor Time discipline

This repo runs under Emperor Time. Before creative work: silent boot, then
MUST-route (`scripts/emperor activate` / `route`), then ask→spec + harness-plan
at tiny by default. Iron gates never soft. Ledgers → `.emperor/`.
If the skill folder is missing, apply `adapters/generic/EMPEROR_TIME.core.md`.
```

### 1b. `.cursor/rules` guidance

- Prefer a short rule that **defers** to repo-root `AGENTS.md` / tip `SKILL.md`
  rather than pasting the whole doctrine into `.cursor/rules`.
- Keep secrets out of rules files. Never commit `OPENROUTER_API_KEY`,
  `CURSOR_API_KEY`, or auth cookies.
- Project skills (Cursor project skill dirs), if used: mirror the same
  MUST-route + tiny-default bite; Chain-Jail-adapt format only — do not fork
  doctrine.

### 1c. `cursor-agent` CLI (optional binary lane)

```bash
export PATH="$HOME/.local/bin:$PATH"
cursor-agent status
# Not logged in → binary lane BLOCKED (structure path still valid)
# Logged in → may run print/non-interactive probes per Cursor docs; keep timeout
```

Do not treat CLI absence or auth BLOCKED as an ET-bug.

---

## 2. Session path (boot → activate/route → ask-spec → done)

Cursor has **no** Claude `SessionStart` hook. Agent (or human) must run:

```bash
# cwd = foreign or target project; ET = tip checkout
bash scripts/boot.sh                 # or: scripts/emperor boot
# zsh:  zsh scripts/emperor.zsh boot   (same silent-boot contract)
# Windows: pwsh -NoProfile -File scripts/boot.ps1
#          (or: pwsh -NoProfile -File scripts/emperor.ps1 boot)
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
Resume from STATE.md / `scripts/emperor queue next`. Do not tell the client
to run `identify` or `eval` — those are internals.

On Windows, `scripts/emperor.ps1 <tool>` silent-boots when `.emperor/host.env`
is missing — same contract as `scripts/emperor` (bash) and `scripts/emperor.zsh`.

Config bridge: copy `adapters/cursor/config.snippet.yaml` → project
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

## 3. Providers — ORI live when Cursor binary BLOCKED + local OpenAI-compat

### ORI live (supported when `cursor-agent` BLOCKED)

When `cursor-agent status` is **Not logged in** / binary lane **BLOCKED**, do
**not** chase Cursor login. The supported **live model route** is **ORI** —
OpenRouter via a labeled host:

1. **Preferred:** OpenCode TTY — `opencode run -m openrouter/<slug> --dir <foreign>`
   (use `script`/`pty` + timeout; Bet D: pipes can hang). Prefer free lab slug
   `stealth/space-bunny-alpha` unless PO names another.
2. **Fallback:** direct OpenRouter OpenAI-compat HTTPS chat completion with the
   same `OPENROUTER_API_KEY` if OpenCode flakes.

**Host must be labeled honestly** (OpenCode or HTTPS). This is **not** Cursor
equal-UX. Equal-UX still requires Cursor binary/IDE green + PO accept.

```bash
# Set OPENROUTER_API_KEY in the host environment only.
# Never commit, print, or paste the key into receipts or rules files.
export PATH="$HOME/.local/bin:$PATH"
cursor-agent status   # Not logged in → binary BLOCKED; use ORI below
# Preferred ORI host (OpenCode), PTY-safe:
# timeout 60 script -q -c 'opencode run -m openrouter/stealth/space-bunny-alpha --dir <foreign> "<tiny ask>"' /tmp/ori.log
```

When Cursor IDE / `cursor-agent` **is** Logged in, mid/flash may also route
through Cursor's model picker / provider settings — still never paste keys into
`.emperor/` or git. ET structure (gates, ask→spec, done) remains the usefulness
thesis when tokens are cheap — not token-shave theater.

### Local OpenAI-compat (Ollama / Colibrì-as-inference)

```bash
# Typical Ollama OpenAI-compatible endpoint:
#   http://127.0.0.1:11434/v1
# Point Cursor / local provider config at that base URL with a toy model id
# (llama3.2:3b | qwen2.5:3b | heavy-quant). Verify in Cursor model settings.
```

**Colibrì:** not an owned harness here. Integrate-if-you-want pack:
`adapters/colibri/` (JustVugg/colibri as OpenAI-compat inference host). If
present on the host, point Cursor's local provider at
`http://127.0.0.1:8000/v1` (or your bind), document base URL + model id in
NOTES, and keep ET loaded on the Cursor side. Do not ship Colibrì runtime
inside ET.

### Preferred free OpenRouter (P0 lab)

`OPENROUTER_API_KEY` in env for **ORI** (OpenCode or OpenAI-compat) — never
commit/print. Prefer slug `stealth/space-bunny-alpha` for free lab smokes.
Local fallback when OpenRouter fails: llama.cpp CPU + Qwen2.5-Coder 1.5B Q4_K_M
(colibri-toy probe path). Do not block on Ollama. Score ORI PASS separately from
equal-UX HOLD.

---

## 4. Failure modes (triage)

| Symptom | Likely class | Action |
|---|---|---|
| No `.emperor/host.env` / activate never run | **ET-bug** / operator skip | Run boot + activate; do not blame the model |
| `done` FAIL on probe the model never touched | **ET-bug** (probe/path) | Fix DONE.md / cwd / scripts wiring |
| Iron gate refuses forge/secrets without consent | **PASS** (iron working) | Expected — do not soften |
| Model ignores MUST-route / skips ask→spec | **model-FAIL** | Record FAIL; keep iron; clarify AGENTS.md / rules |
| `cursor-agent status` → **Not logged in** | **BLOCKED** (binary) | Structure path OK; run **ORI live** smoke (OpenCode or OpenAI-compat); host labeled; do **not** chase login; equal-UX stays HOLD |
| `cursor-agent` / `agent` missing | **PATH / blocked** | Add `~/.local/bin` or absolute path; no equal-UX claim |
| Rules / AGENTS.md not loaded in IDE | **operator** | Fix `.cursor/rules` pointer; re-open project |
| Boot skipped; creative work first | **operator / model-FAIL** | Enforce MUST-route; receipt as FAIL if claimed PASS |
| Bakeoff / high-stakes pause requested | **Pause** | Stop; do not soft-iron or auto-claim |
| Structure green but IDE/binary unproven | **equal-UX HOLD** | PO-gated; structure PASS ≠ equal-UX |
| Toy model missing (no Ollama / no weights) | **blocked** (model portion) | Ship docs + smoke recipe; receipt discloses |

Triage labels for receipts: **ET-bug** | **model-FAIL** | **PASS** | **BLOCKED** (auth/binary/PATH) | **HOLD** (equal-UX).

Structure path (AGENTS.md + `boot`/`activate`/`done`) remains valid when the
binary lane is auth-BLOCKED. **ORI live PASS** is claimable after a dated
receipt with a labeled host (OpenCode / OpenAI-compat) — still **not** Cursor
equal-UX. **Equal-UX-proven** still requires a dated **binary/IDE** green
receipt **and** PO accept of claim language — do not auto-claim from docs,
AGENTS-only PASS, or ORI alone.

---

## 5. Cursor as enlisted worker (Steal Chain)

When Cursor/`cursor-agent` runs a scoped worker prompt, prepend the Vow card
from `adapters/generic/EMPEROR_TIME.core.md` if the worker host lacks standing
orders. Consent before enlist. Auth BLOCKED workers do not get secret paste.

---

## 6. QA entrypoint

Repeatable toy smoke without frontier models: **`QA-SMOKE.md`** (this directory).

---

## Why Cursor in the roster

Buyers already live in Cursor. Rich docs + structure recipe here; proof via
receipts. Equal-UX stays HOLD until PO says otherwise.
