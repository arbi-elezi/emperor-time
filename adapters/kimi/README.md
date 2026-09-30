# Adapter — Kimi (rich playbook; ORI live path)

Moonshot **Kimi** models are a first-class **live model route** for Emperor
Time when the host is OpenCode (or any OpenAI-compat client) pointed at
OpenRouter. This pack deepens Kimi around that supported path — **not** a
chase for native Kimi CLI equal-UX.

**Claim bar:** docs + recipe here are **rich**. Live proof is **ORI live
PASS** when a dated field receipt shows OpenCode (TTY preferred) green on a
foreign ask with a locked OpenRouter Kimi/Moonshot slug. Host label mandatory:
**Kimi model via OpenCode/ORI**. That is **not** native Kimi CLI equal-UX.
AGENTS.md + scripts alone is **structure proven**, not equal-UX.

**Surfaces (do not conflate):**

| Surface | Role in this pack |
|---|---|
| **OpenCode + OpenRouter `moonshotai/kimi-*` (ORI)** | **Primary live path.** Locked slug: `moonshotai/kimi-k3` → OpenCode `openrouter/moonshotai/kimi-k3`. Real TTY (`script` / PTY). |
| **AGENTS.md + `scripts/`** | Canonical structure fallback. Always ship. Runnable with no OpenCode binary and no API key. |
| **Native Kimi CLI (`kimi`)** | Pointer only — see `adapters/kimi-cli/`. Skill dirs shared with Claude Code. Equal-UX chase is **out of scope** (standing policy). |
| **Moonshot API / SDK** | Mention only. Inference loop ≠ harness. |

**Deferred (not this adapter):** Cursor / Grok ownership, Colibrì ownership,
Android C++, multi-16B graph runtimes. Do not edit `adapters/kimi-cli/` from
this lane.

---

## 0. Prereqs

```bash
# OpenCode CLI (verify at install time) — the ORI host
npm install -g opencode-ai          # bin: opencode (often ~/.local/bin)
# or: curl -fsSL https://opencode.ai/install | bash
export PATH="$HOME/.local/bin:$PATH"
opencode --version                  # observed example: 1.18.x
opencode --help
```

Auth for ORI: `OPENROUTER_API_KEY` in the host env / OpenCode auth store.
**Never** commit or print the key (Vow of Consent / secrets-no-leak).

Native `kimi` binary is **optional and not required** for this pack's live
claim. If you want native install pointers only, see `adapters/kimi-cli/`.

Iron gates never soften for mid/flash models. Judgment stays **off** for toy
smoke (see `config.snippet.yaml`).

---

## 1. Install / paste path

### 1a. OpenCode skill install (when OpenCode is the host)

```bash
# from emperor-time tip
./scripts/install.sh opencode user
# → ~/.opencode/skills/emperor-time/
# Windows: .\scripts\install.ps1 -Harness opencode -Scope user
```

OpenCode skill format may differ by release — verify with `opencode --help`.
Do not invent a second doctrine tree. Shared OpenCode depth lives in
`adapters/opencode/`; this pack is the **Kimi/ORI labeling + slug** layer on
top of that host.

### 1b. Native Kimi CLI (pointer only — equal-UX out of scope)

Claude Code install already covers Kimi CLI skill dirs (verified path overlap).
For Kimi-first placement: `./scripts/install.sh kimi user` →
`~/.kimi/skills/emperor-time/`. Detail: `adapters/kimi-cli/README.md`.
Do **not** claim native equal-UX from this pack.

### 1c. AGENTS.md (canonical standing orders — always)

Drop the tip `AGENTS.md` into the **target** project (or append the short
pointer below). Symlink or copy `scripts/` so `boot` / `activate` / `done`
resolve.

Minimal pointer:

```markdown
## Emperor Time discipline

This repo runs under Emperor Time. Before creative work: silent boot, then
MUST-route (`scripts/emperor activate` / `route`), then ask→spec + harness-plan
at tiny by default. Iron gates never soft. Ledgers → `.emperor/`.
If the skill folder is missing, apply `adapters/generic/EMPEROR_TIME.core.md`.
```

---

## 2. Session path (boot → activate/route → done)

Neither OpenCode nor Kimi CLI provides a Claude `SessionStart` hook. Agent
(or human) must run:

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

Config bridge: copy `adapters/kimi/config.snippet.yaml` → project
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

## 3. Providers / models — ORI live (primary)

### Locked OpenRouter Kimi slug

```bash
# OPENROUTER_API_KEY in the host env / OpenCode auth store — never commit it.
# Prefer a real TTY (`script` / PTY); bare pipes can hang (OpenCode Bet D).
# timeout ≤30s while probing.
export PATH="$HOME/.local/bin:$PATH"
timeout 30 script -q -c \
  'opencode run -m openrouter/moonshotai/kimi-k3 --dir . "<ask>"' \
  /dev/null
# portable: python3 -c 'import pty,sys; sys.exit(pty.spawn(["opencode","run",...]))'
```

*(Darwin/BSD: `script` has no `-c` — use `script -q file cmd` or prefer `python3 -c 'import pty,sys; sys.exit(pty.spawn([...]))'`.)* **ORI live PASS requires a real TTY/PTY**; bare OpenAI-compat HTTPS is compat/fallback only — not ORI live PASS.

- **Locked OpenRouter model ID:** `moonshotai/kimi-k3`
- **OpenCode invocation:** `openrouter/moonshotai/kimi-k3`
- **Host label:** **Kimi model via OpenCode/ORI**
- Do **not** use the moving `kimi-latest` alias, and do **not** substitute
  free-catalog toys (`space-bunny`, `opencode/*-free`) as Kimi proof.
- If K3 is unavailable at dowse, record **blocked** and request a PO decision
  before swapping. One Moonshot/Kimi-family successor may be accepted with an
  honest inventory note (same pattern as `grok-code-fast-1` → `grok-4.3`).

### Direct OpenAI-compat fallback (optional twin — **not** ORI live PASS)

Same key, same slug, no OpenCode binary. Use for route/inventory smoke only.
**Null / short content** from this twin does **not** satisfy **ORI live PASS** —
standing gate is **TTY-as-gate** (OpenCode under `script` / PTY). Fullshape + TTY
carry the token.

```bash
# never print the key; record HTTP status + a short token only
# Do NOT score this as ORI live PASS even when HTTP 200.
curl -sS https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"moonshotai/kimi-k3","messages":[{"role":"user","content":"<tiny ask>"}]}'
```

Structure path (AGENTS.md + `boot`/`activate`/`done`) remains valid when the
binary lane is pipe-blocked. **ORI live PASS** needs a dated **TTY/PTY** green
receipt with the host label above — compat twin alone is insufficient.

### Dowse / install pointers

```bash
./scripts/dowse.sh                 # detection only — no credentials
./scripts/install.sh opencode user # OpenCode skill dir
./scripts/install.sh kimi user     # native Kimi skill dir (pointer; not equal-UX)
```

---

## 4. Failure modes (triage)

| Symptom | Likely class | Action |
|---|---|---|
| No `.emperor/host.env` / activate never run | **ET-bug** / operator skip | Run boot + activate; do not blame the model |
| `done` FAIL on a probe the change never touched | **ET-bug** (probe/path) | Fix DONE.md / cwd / scripts wiring |
| Iron gate refuses forge/secrets without consent | **PASS** (iron working) | Expected — do not soften |
| Model ignores MUST-route / skips ask→spec | **model-FAIL** | Record FAIL; keep iron; tighten AGENTS.md |
| OpenCode binary missing / PATH miss | **blocked** (binary) | AGENTS.md+scripts only; no ORI-binary claim |
| Hang after log `message=init`; timeout → EXIT **124**; empty stdout | **harness hang (non-TTY)** | OpenCode `run` stalls under pipe. Wrap with `script`/`pty`; keep `timeout` ≤30s |
| `--format json` / `--interactive` still 124 under pipe | **same hang class** | Those flags do **not** unblock; needs a real TTY |
| OpenRouter 401 / 429 / timeout on `moonshotai/kimi-*` | **blocked** (ORI route) | Key/quota/model; does not indict AGENTS.md structure |
| Locked `moonshotai/kimi-k3` 404 / unavailable | **blocked** (slug inventory) | Record; ping PO — do not silently swap to non-Kimi free catalog |
| Native `kimi` missing / unauthed | **N/A for this pack's live claim** | ORI is the live path; native equal-UX out of scope |

Triage labels for receipts: **ET-bug** | **model-FAIL** | **PASS** | **blocked**
(binary / PATH / hang / slug).

---

## 5. Kimi as enlisted worker (Steal Chain)

Via OpenCode/ORI (preferred for headless):

```bash
script -q -c 'opencode run -m openrouter/moonshotai/kimi-k3 --dir . "<scoped worker prompt>"' /dev/null
```

Native `kimi`: check `kimi --help` at dowse for a headless flag; else
`kimi-agent-sdk` / `kimi acp` (see `adapters/kimi-cli/`). Consent before enlist.
No auth bypass.

Prepend the Vow card from `adapters/generic/EMPEROR_TIME.core.md` when the
worker host lacks the skill install.

---

## 6. QA entrypoint

Repeatable structure + ORI live smoke: **`QA-SMOKE.md`** (this directory).

---

## Why Kimi in the roster

OpenRouter carries current Moonshot `moonshotai/kimi-*` coding models; OpenCode
is the practical ORI host for buyers who are not on Claude Code or native Kimi
CLI. Rich docs here; structure and ORI live can be proven without chasing native
CLI equal-UX. Native Kimi CLI remains documented under `adapters/kimi-cli/` for
install/skill discovery only.
