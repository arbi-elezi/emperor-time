# QA smoke — OpenCode + toy local (≤1 page)

**Goal:** exercise ET boot→activate→done on a foreign tiny ask without frontier
models. Triage **ET-bug | model-FAIL | PASS**. Judgment off. Iron hard.

## Preferred model path (P0)

1. **OpenRouter free:** `openrouter/stealth/space-bunny-alpha` via OpenCode
   (`OPENROUTER_API_KEY` in env — never commit/print the key).
2. **Local fallback:** llama.cpp CPU + Qwen2.5-Coder 1.5B Q4_K_M (see
   `/workspace/emperor-time-colibri-local-probe.md`) if OpenRouter/OpenCode fails.
3. Ollama toys (`llama3.2:3b` / `qwen2.5:3b`) optional — do not block on Ollama.

## Prereqs checklist

- [ ] Emperor-Time tip checked out (record SHA / 0.4.174+)
- [ ] `opencode --version` works **or** mark OpenCode binary **blocked**
- [ ] Toy model available (`ollama list` shows llama3.2:3b / qwen2.5:3b / heavy-quant)
      **or** mark model portion **blocked** (still run AGENTS.md path)
- [ ] Foreign repo cloned (not bakeoff T1–T4 / not is-buffer redo)

## Steps

1. **Wire:** copy tip `AGENTS.md` + symlink `scripts` → tip `scripts`; copy
   `adapters/opencode/config.snippet.yaml` → foreign `.emperor/config.yaml`.
2. **Boot:** `python3 $ET/scripts/lib/boot.py --root . --skip-eval` (foreign).
   Read `.emperor/host.env` + `survey.md`.
3. **MUST-route:** `activate.py --cwd . -u "<tiny ask>"`; open `ACTIVATION next=`.
4. **ask→spec:** `--emit --effort-class tiny` (judgment stays off).
5. **Change:** one wording/one-liner class edit only.
6. **done:** `done.py` on the task dir — record exit code.
7. **Optional OpenCode binary:**  
   `opencode run -m openrouter/stealth/space-bunny-alpha --dir . "<same ask>"`
   (fallback: `ollama/<toy>` or llama.cpp 1.5B path — see Preferred model path)  
   If binary or model missing → stop that lane; do not claim equal-UX-proven.
8. **Receipt:** CONTEXT/BEFORE/AFTER/NOTES/claim under
   `/workspace/field-receipts/receipts/<date>/opencode-toy-lab/` with triage label.

## Pass / fail

| Result | Meaning |
|---|---|
| done exit 0 + honest probes | **PASS** (structure exercised) |
| done FAIL, probes/config wrong | **ET-bug** |
| done FAIL / nonsense after correct ET path | **model-FAIL** |
| no OpenCode / no toy weights | **blocked** (disclose; docs still ship) |

Do **not** sell toy PASS as Astra-bridge or mid-16B proof.
