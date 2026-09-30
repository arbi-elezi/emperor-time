# Adapter — Ollama (local open-weight models)

Ollama here is a **local worker persona bake**: paste distilled doctrine into a
Modelfile `SYSTEM` prompt so a named local model always carries the vows.
Ollama is **not** an Emperor Time harness and does **not** own orchestration,
SessionStart, or iron gates. The client-side harness (OpenCode / Cursor /
Claude / …) + tip scripts stay the orchestrator.
Native Ollama equal-UX is **HOLD** — a green `ollama run` toy is not
equal-UX-proven.

## Build the persona model

```powershell
# 1. pick a base model you've pulled (client consents to pulls — disk state):
ollama pull qwen3            # or any capable coder model you prefer

# 2. edit Modelfile.example: set FROM, and paste the contents of
#    ..\generic\EMPEROR_TIME.core.md into the SYSTEM block
#    (small models <14B: paste only the Vow card — the top section)

# 3. create:
ollama create emperor -f .\Modelfile.example

# 4. trial before real use (Chain Jail rule — toy task, prediction first):
ollama run emperor "Reply with exactly: ok"
```

## Role in the hetero-agent roster

An Ollama model is a **worker or critic, never the orchestrator**:

- Bulk mechanical edits, boilerplate, first-draft tests — free and private.
- Hetero-critique — a genuinely different model family means uncorrelated
  failure modes (Steal Chain's diversity principle).
- Privacy-sensitive content that must not leave the machine.

Small models follow the Vow card imperfectly; that's expected. The
orchestrator's quarantine-and-judge step (everything returned = CONJECTURE) is
what makes an imperfect worker safe to use.

**Worker / critic only — never orchestrator.** Quarantine returns as
CONJECTURE. Do not promote Ollama to master router, silent boot owner, or
merge authority.

## Local inference vs this bake

- **Equal-UX HOLD.** Structure / Modelfile bake ≠ vendor equal-UX. Do not claim
  native Ollama equal-UX without an explicit PO-accepted receipt language
  (none today).
- **Local inference host:** prefer Colibrì as the integrate-if-you-want model
  server — see `adapters/colibri/STRANGER.md`. Point the *client* harness at
  Colibrì; load ET on the client. Colibrì is inference, not a harness; Ollama
  is not either.
- **Live mid-model path** for field proof stays OpenCode/ORI (TTY-as-gate) per
  root README + `adapters/opencode/ORI-REGRESSION.md` — not an Ollama-as-harness
  lane.

## Dispatch forms

```powershell
ollama list                                  # liveness + roster of pulled models
ollama run emperor "<scoped worker prompt>"  # one-shot, stdout
# structured/scripted: POST http://localhost:11434/api/generate
```

Context windows are the constraint: keep worker prompts scoped (one file, one
function, one question) and let the orchestrator hold the big picture. See the
distillation ladder in `references/portability.md`.

## Session boot (host-agnostic)

Ollama has no Claude `SessionStart` hook. Do not ask the client their OS,
shell, or language. Before dispatching a worker (or when `.emperor/` is
missing), the orchestrator runs silent boot once, then reads what it wrote:

```bash
bash scripts/boot.sh   # or: scripts/emperor boot
# Windows: pwsh -NoProfile -File scripts/boot.ps1
```

Then open:

- `.emperor/host.env` — os, shell, wsl, encoding
- `.emperor/survey.md` — artifact classes (do not ask the client their stack)
- `.emperor/eval.log` — when this tree *is* Emperor Time

Resume from STATE.md / `scripts/emperor queue next`. Do not tell the client
to run `identify` or `eval`. Those are internals.
Foreign/lost tree: `scripts/emperor identify <path>`.

## MUST-route (before creative work)

Silent boot is not enough. Before clarifying questions, exploring, or writing
code, open one governing file from the `SKILL.md` tables, or run
`scripts/emperor route "<utterance>"` / `scripts/emperor activate` and open
`ACTIVATION next=`. Same bite as Claude SessionStart MUST-route; Emperor Time
stays the orchestrator (no foreign master router).

