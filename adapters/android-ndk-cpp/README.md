# Adapter — Native Android C++ / NDK (domain/stack pack)

This is a **domain/stack** pack for Emperor Time when the work target is
**native Android C++ / NDK** (CMake leaf, JNI `.so`, or the Gradle/JNI boundary).
It is **not** a vendor CLI host chase and **not** a claim that Android Studio /
`ndk-build` is an ET harness peer.

**Claim bar:** docs + recipe here are **rich**. Live coding model path is
**ORI live** via OpenCode + a locked OpenRouter mid/flash slug (lab default:
`stealth/space-bunny-alpha`) — host label mandatory: **OpenCode/ORI**. That is
**not** a native Android CLI equal-UX claim (standing policy: no equal-UX chase).
AGENTS.md + scripts alone is **structure proven**. Missing NDK/SDK is
**toolchain BLOCKED** — honest; structure + ORI remain valid without installing
a farm.

**Surfaces (do not conflate):**

| Surface | What it is | ET load path |
|---|---|---|
| **Pure CMake C++ leaf** | Host- or cross-buildable C++ without full APK | AGENTS.md + `scripts/` + this pack; tiny ask→spec |
| **JNI `.so`** | Native lib loaded by Java/Kotlin (`JNI_OnLoad`, `JNIEnv`) | Same ET path; keep JNI boundary notes in ask→spec |
| **Full APK / Gradle app** | Android application packaging | Out of default smoke; escalate only when the ask earns it |
| **Emulator / device farm** | Runtime verification on Android | **Out of scope** for this pack's proof bar |
| **OpenCode + OpenRouter (ORI)** | **Primary live model path** when coding | TTY preferred (`script` / PTY); host = **OpenCode/ORI** |
| **AGENTS.md + `scripts/`** | Canonical structure fallback | Always ship; no NDK and no API key required |

**Deferred (not this pack):** shipping a game, emulator farm, Colibrì ownership,
OpenAPPA babysitter, bakeoff Run, Cursor/Grok/Kimi ownership. Do not deepen
those adapters from this lane.

---

## 0. Prereqs

```bash
# Structure path — always
# Tip AGENTS.md + scripts/ + this pack's config.snippet.yaml

# Toolchain (optional for structure; required only for native binary claims)
echo "ANDROID_NDK_HOME=${ANDROID_NDK_HOME:-}"
command -v ndk-build || true
# If both absent → label toolchain **BLOCKED**. Do NOT install NDK/SDK/emulator
# farm from this pack's smoke recipe.

# ORI live host (OpenCode)
export PATH="$HOME/.local/bin:$PATH"
opencode --version                  # observed example: 1.18.x
# Auth: OPENROUTER_API_KEY in host env / OpenCode auth store
# Never commit or print the key (Vow of Consent / secrets-no-leak).
```

Iron gates never soften for mid/flash models or for "docs-only Android pack"
asks. Judgment stays **off** for toy smoke (see `config.snippet.yaml`).

---

## 1. Install / paste path

There is **no** `./scripts/install.sh android-ndk-cpp` harness — this is a
domain pack, not a vendor CLI. Use honest paste / pointer.

### 1a. AGENTS.md (canonical standing orders — always)

Drop the tip `AGENTS.md` into the **target** C++/JNI project (or append the
short pointer below). Symlink or copy `scripts/` so `boot` / `activate` /
`done` resolve.

Minimal pointer:

```markdown
## Emperor Time discipline

This repo runs under Emperor Time. Before creative work: silent boot, then
MUST-route (`scripts/emperor activate` / `route`), then ask→spec + harness-plan
at tiny by default. Iron gates never soft. Ledgers → `.emperor/`.
If the skill folder is missing, apply `adapters/generic/EMPEROR_TIME.core.md`.
Domain notes: `adapters/android-ndk-cpp/` (CMake leaf ≠ JNI `.so` ≠ APK ≠ emulator).
```

### 1b. Config bridge

Copy `adapters/android-ndk-cpp/config.snippet.yaml` → project
`.emperor/config.yaml` (or merge knobs). Prefer `python3 scripts/lib/config.py`
for config-only smoke so boot does not stall.

### 1c. OpenCode skill (when OpenCode is the ORI host)

```bash
./scripts/install.sh opencode user
# → ~/.opencode/skills/emperor-time/
```

Shared OpenCode depth lives in `adapters/opencode/`; this pack is the
**Android NDK/C++ domain + ORI labeling** layer.

---

## 2. Session path (boot → activate/route → ask-spec → done)

No Claude `SessionStart` on a raw CMake/JNI tree. Agent (or human) must run:

```bash
# cwd = foreign or target C++/JNI project
bash scripts/boot.sh                 # or: python3 $ET/scripts/lib/boot.py --root .
# foreign: prefer --skip-eval
# read:
#   .emperor/host.env
#   .emperor/survey.md

python3 scripts/lib/activate.py --cwd . -u "<ask>"
# open ACTIVATION next=  (MUST-route before clarifying / exploring / coding)

python3 scripts/lib/route.py "<ask>"   # exit 1 → fall back to SKILL tables

# tiny default — emit ask→spec (chains harness-plan):
python3 scripts/lib/ask_spec.py --emit --effort-class tiny \
  --write .emperor/tasks/<id>/ask-spec.md "<ask>"

# …do the smallest change (one export / one comment / one CMake knob)…

python3 scripts/lib/done.py .emperor/tasks/<id>
# exit 0 = green; else FAIL + ledger (honest)
```

Do not ask the client their OS/shell/language — read `host.env` / `survey.md`.
Foreign/lost tree: `scripts/emperor identify <path>`.

Name the **surface** in the ask→spec (pure CMake leaf vs JNI `.so` vs APK).
Do not silently escalate a leaf edit into an emulator farm.

---

## MUST-route (before creative work)

Silent boot is not enough. Before clarifying questions, exploring, or writing
code, open one governing file from the `SKILL.md` tables, or run
`scripts/emperor route "<utterance>"` / `scripts/emperor activate` and open
`ACTIVATION next=`. Same bite as Claude SessionStart MUST-route; Emperor Time
stays the orchestrator.

---

## 3. Providers / models — ORI live (primary)

### Locked OpenRouter mid/flash slug (lab default)

```bash
# OPENROUTER_API_KEY in the host env / OpenCode auth store — never commit it.
# Prefer a real TTY (`script` / PTY); bare pipes can hang (OpenCode Bet D).
# timeout ≤30–90s while probing.
export PATH="$HOME/.local/bin:$PATH"
timeout 30 script -q -c \
  'opencode run -m openrouter/stealth/space-bunny-alpha --dir . "<ask>"' \
  /dev/null
# portable: python3 -c 'import pty,sys; sys.exit(pty.spawn(["opencode","run",...]))'
```

*(Darwin/BSD: `script` has no `-c` — use `script -q file cmd` or prefer `pty.spawn`.)*
**ORI live PASS = TTY-as-gate.**

- **Lab / standing slug:** `stealth/space-bunny-alpha`
- **OpenCode invocation:** `openrouter/stealth/space-bunny-alpha`
- **Host label:** **OpenCode/ORI**
- Multi-probe MATRIX preferred when cheap (token ping + domain surface triage
  + iron refuse) — one token toy alone is a weak live claim.
- Do **not** claim native Android Studio / `ndk-build` equal-UX from ORI live.
- If the slug is unavailable at dowse, record **blocked** and request a PO
  decision before swapping.

### Direct OpenAI-compat fallback (optional twin — **not** ORI live PASS)

Same key, same slug, no OpenCode binary. Route/inventory only. **Null / short
content** from this twin does **not** satisfy **ORI live PASS** — fullshape +
TTY carry the token (TTY-as-gate).

```bash
# never print the key; record HTTP status + a short token only
# Do NOT score this as ORI live PASS even when HTTP 200.
curl -sS https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"stealth/space-bunny-alpha","messages":[{"role":"user","content":"<tiny ask>"}]}'
```

Structure path remains valid when ORI is blocked. Toolchain BLOCKED (no NDK)
does **not** indict structure or ORI.

### Dowse / install pointers

```bash
./scripts/dowse.sh                 # detection only — no credentials
./scripts/install.sh opencode user # OpenCode skill dir (ORI host)
```

`dowse` scans vendor agent CLIs — it will **not** list `android-ndk-cpp`
(domain pack, not a CLI host). Discover via `adapters/android-ndk-cpp/` + root README.

---

## 4. Failure modes (triage)

| Symptom | Likely class | Action |
|---|---|---|
| No `.emperor/host.env` / activate never run | **ET-bug** / operator skip | Run boot + activate; do not blame the model |
| `done` FAIL on a probe the change never touched | **ET-bug** (probe/path) | Fix DONE.md / cwd / scripts wiring |
| Iron gate refuses forge/secrets without consent | **PASS** (iron working) | Expected — do not soften |
| Model ignores MUST-route / skips ask→spec | **model-FAIL** | Record FAIL; keep iron; tighten AGENTS.md |
| `ANDROID_NDK_HOME` unset / `ndk-build` missing | **BLOCKED** (toolchain/SDK) | Honest label; do **not** install farm; structure + ORI still valid |
| OpenCode binary missing / PATH miss | **BLOCKED** (binary) | AGENTS.md+scripts only; no ORI-binary claim |
| Hang after log `message=init`; timeout → EXIT **124**; empty stdout | **harness hang (non-TTY)** | Wrap with `script`/`pty`; keep timeout |
| OpenRouter 401 / 429 / timeout on slug | **BLOCKED** (ORI route) | Key/quota/model; does not indict AGENTS.md structure |
| Ask conflates CMake leaf with full APK/emulator | **HOLD** / scope | Narrow ask→spec to named surface; emulator out of scope |

Triage labels for receipts: **ET-bug** | **model-FAIL** | **PASS** |
**BLOCKED** (toolchain/SDK / binary / ORI) | **HOLD**.

---

## 5. Enlisted worker (Steal Chain) via ORI

```bash
script -q -c \
  'opencode run -m openrouter/stealth/space-bunny-alpha --dir . "<scoped worker prompt>"' \
  /dev/null
```

Consent before enlist. No auth bypass. Prepend the Vow card from
`adapters/generic/EMPEROR_TIME.core.md` when the worker host lacks the skill
install. Keep the scoped prompt on the named surface (leaf vs JNI vs APK).

---

## 6. QA entrypoint

Repeatable structure + toolchain honesty + ORI live smoke: **`QA-SMOKE.md`**
(this directory).

---

## Why this pack exists

Pitch-domain work is often **native Android game / pure C++/NDK**. Emperor Time
needed a first-class guidelines pack for that stack: surface honesty, session
path, iron, ORI mid/flash notes, and failure triage — without shipping a game
or chasing emulator farms. Structure and ORI can be proven when NDK is absent;
toolchain BLOCKED is an honest label, not a soft fail of the pack.
