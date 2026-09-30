# QA smoke — Grok Build + AGENTS.md (≤1 page)

**Goal:** exercise ET boot→activate→done on a **foreign** tiny ask. Judgment
off. Iron hard. Triage **ET-bug | model-FAIL | PASS | blocked**.

## Preferred paths (label the host honestly)

1. **Structure (always):** tip `AGENTS.md` + `scripts/` + `config.snippet.yaml`.
   No `grok` binary required. A green `done` here is **structure PASS**, not
   equal-UX.
2. **Grok Build binary (optional):** `grok -p "<same ask>"` only if `grok`
   is on PATH **and** the client is authed (`XAI_API_KEY` or `grok login`).
   If the binary is absent or auth is missing → **blocked**. Do not install
   or log in from the orchestrator.
3. **OpenRouter model note (optional, not Grok Build):**  
   `opencode run -m openrouter/x-ai/grok-code-fast-1 --dir . "<ask>"`  
   Label it "Grok **model** via OpenCode". One slug only:
   `x-ai/grok-code-fast-1`. Never print the key. Do not sell this as Grok
   Build equal-UX or as Astra-bridge.

## Prereqs checklist

- [ ] Emperor-Time tip checked out (record SHA / 0.4.174+)
- [ ] `grok version` / `grok --help` works **or** mark binary **blocked**
- [ ] `XAI_API_KEY` or an existing `grok` login **or** mark auth **blocked**
      (do not create a login; do not read key files)
- [ ] Foreign repo cloned (not bakeoff T1–T4, not is-buffer redo, not
      emperor-time itself)

## Steps

1. **Wire:** copy tip `AGENTS.md` + symlink `scripts` → tip `scripts`; copy
   `adapters/grok/config.snippet.yaml` → foreign `.emperor/config.yaml`.
2. **Boot:** `python3 $ET/scripts/lib/boot.py --root . --skip-eval` (foreign).
   Read `.emperor/host.env` + `survey.md`.
3. **MUST-route:** `activate.py --cwd . -u "<tiny ask>"`; open `ACTIVATION next=`.
4. **ask→spec:** `--emit --effort-class tiny` (judgment stays off).
5. **Change:** one wording/one-liner class edit only. No upstream PR without consent.
6. **done:** write `DONE.md` probes that match the edit; `done.py` — record exit code.
7. **Optional binary:** if `grok` is installed and authed, run the documented
   headless flag from `grok --help` (expected: `grok -p`) with a timeout.
   Missing binary or missing auth → binary lane **blocked**.
8. **Receipt:** CONTEXT / BEFORE / AFTER / NOTES / claim under
   `/workspace/field-receipts/receipts/<date>/grok-rich/` with triage label.

## Pass / fail

| Result | Meaning |
|---|---|
| done exit 0 + honest probes | **PASS** (structure exercised) — not equal-UX |
| done FAIL, probes/config wrong | **ET-bug** |
| done FAIL / nonsense after a correct ET path on a live model | **model-FAIL** |
| no `grok` binary, or no auth / no `XAI_API_KEY` | **blocked** (binary lane; docs + structure may still ship) |
| OpenRouter `x-ai/grok-code-fast-1` via OpenCode green or 401 | model-via-other-host only — not Grok Build |

Do **not** sell a toy or API PASS as Astra-bridge or mid-16B proof.
Do **not** claim equal-UX from structure PASS. That claim waits on a green
`grok` binary foreign receipt **and** explicit PO claim ACCEPT.
