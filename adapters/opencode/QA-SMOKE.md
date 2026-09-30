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
- [ ] `opencode --version` works with `PATH` including `~/.local/bin` (or absolute path) **or** mark OpenCode binary **blocked** / PATH footgun
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
   Ensure `PATH` includes `~/.local/bin` (or use absolute `~/.local/bin/opencode`).  
   Under agent/CI **non-TTY**, bare `opencode run` may hang after log `init` → EXIT **124**.  
   Prefer:  
   `timeout 20 script -q -c 'opencode run -m openrouter/stealth/space-bunny-alpha --dir . "<same ask>"' /dev/null`  
   *(Darwin/BSD: no `script -c` — use `script -q file cmd` or prefer `python3` `pty.spawn`.)*  
   (fallback: `ollama/<toy>` or llama.cpp 1.5B — see Preferred model path)  
   If binary missing / PATH miss / pipe hang → mark binary lane **blocked**; keep AGENTS+scripts path; do **not** claim equal-UX-proven without PO.
8. **Receipt:** CONTEXT/BEFORE/AFTER/NOTES/claim under
   `/workspace/field-receipts/receipts/<date>/opencode-hang-equal-ux/` (or toy-lab) with triage label.
   On rebase / tip move, refresh receipt SHAs + PR body base/head tip before
   PO/QA ping (see `references/receipt-pr-tip-hygiene.md`).

## Pass / fail

| Result | Meaning |
|---|---|
| done exit 0 + honest probes | **PASS** (structure exercised) |
| done FAIL, probes/config wrong | **ET-bug** |
| done FAIL / nonsense after correct ET path | **model-FAIL** |
| no OpenCode / no toy weights | **blocked** (disclose; docs still ship) |
| hang after `init` → EXIT 124 (pipe/non-TTY) | **blocked** binary lane — use `script`/`pty` or AGENTS+direct-API; do not claim equal-UX |

Do **not** sell toy PASS as Astra-bridge or mid-16B proof.
Do **not** auto-claim equal-UX from a green TTY receipt until PO accepts claim language.
