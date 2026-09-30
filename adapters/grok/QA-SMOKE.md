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
3. **OpenRouter / ORI live route (supported when native `grok` is BLOCKED;
   still not Grok Build):** **ORI live PASS = TTY-as-gate**. Prefer a real TTY
   (`script` / PTY) — bare pipes can hang (see OpenCode Bet D). Example:
   `script -q -c 'opencode run -m openrouter/x-ai/grok-4.3 --dir . "<ask>"' /dev/null`
   *(Darwin/BSD: no `script -c` — use `script -q file cmd` or `python3` `pty.spawn`.)*
   Direct OpenAI-compat HTTPS is compat/fallback only — not ORI live PASS.
   Host label mandatory: **Grok model via OpenCode/ORI**. Auth =
   `OPENROUTER_API_KEY` only (never print/commit). Historical playbook slug
   `x-ai/grok-code-fast-1` is **deprecated** on OpenRouter (404; recommends
   Grok 4.3) — record the **live** `x-ai/*` slug you actually invoke. Do not
   sell ORI live as Grok Build equal-UX or as Astra-bridge.

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
8. **Receipt:** CONTEXT / BEFORE / AFTER / NOTES / claim (+ MATRIX/raw as
   needed) under `/workspace/field-receipts/receipts/<date>/bet-f-ori-grok/`
   (or a dated ORI short-name — **not** a native Grok Build claim folder)
   with triage label and the mandatory OpenCode/ORI host label.

## Pass / fail

| Result | Meaning |
|---|---|
| done exit 0 + honest probes | **PASS** (structure exercised) — not equal-UX |
| done FAIL, probes/config wrong | **ET-bug** |
| done FAIL / nonsense after a correct ET path on a live model | **model-FAIL** |
| no `grok` binary, or no auth / no `XAI_API_KEY` | **blocked** (binary lane; docs + structure may still ship) |
| OpenRouter `x-ai/*` via OpenCode TTY green (ORI) | **ORI live PASS** — supported when native binary BLOCKED; host = OpenCode/ORI; **not** Grok Build equal-UX |
| Locked historical `x-ai/grok-code-fast-1` 404/deprecated | model-route inventory — record successor slug; do not invent equal-UX |
| OpenRouter 401 / timeout on live `x-ai/*` via OpenCode | **blocked** / model-FAIL (route) — not Grok Build evidence |

Do **not** sell a toy or API PASS as Astra-bridge or mid-16B proof.
Do **not** claim equal-UX from structure PASS or from ORI live PASS. Native
Grok Build equal-UX waits on a green `grok` binary foreign receipt **and**
explicit PO claim ACCEPT. ORI live PASS is allowed and distinct.
