# QA smoke — Cursor + structure path (≤1 page)

**Goal:** exercise ET boot→activate→done on a foreign tiny ask without frontier
models and without Cursor auth chase. Triage **ET-bug | model-FAIL | PASS |
BLOCKED**. Judgment off. Iron hard. Equal-UX HOLD (structure PASS ≠ equal-UX).

## Preferred model path (P0)

1. **Structure lane (required):** tip scripts + `AGENTS.md` paste — no Cursor
   login required.
2. **Binary lane:** `cursor-agent status` — if **Not logged in**, label
   **BLOCKED**; do **not** chase login.
3. **ORI live (supported when binary BLOCKED):** OpenRouter via **OpenCode TTY/PTY**
   (`opencode run -m openrouter/stealth/space-bunny-alpha --dir <foreign>` under
   `script`/`pty` + timeout). **TTY-as-gate** — direct OpenAI-compat HTTPS is
   fallback/inventory only and is **not** ORI live PASS. `OPENROUTER_API_KEY` in
   env — never commit/print. Host labeled **OpenCode/ORI**. Score **ORI live PASS**
   separately from **equal-UX HOLD**. Prefer slug `stealth/space-bunny-alpha`.
4. **Local fallback:** llama.cpp CPU + Qwen2.5-Coder 1.5B Q4_K_M if OpenRouter
   fails. Ollama toys optional — do not block on Ollama.
5. **When Cursor is Logged in (optional):** mid/flash via Cursor provider
   settings — still never paste keys into git; equal-UX still PO-gated.

## Prereqs checklist

- [ ] Emperor-Time tip checked out (record SHA / 0.4.174+)
- [ ] `PATH` includes `~/.local/bin` **or** absolute `~/.local/bin/cursor-agent`
- [ ] `cursor-agent status` observed (Logged in **or** Not logged in → BLOCKED)
- [ ] Foreign repo cloned (not bakeoff T1–T4; prefer fresh tiny OSS ask)
- [ ] No Cursor auth bypass / no keys in git

## Steps

1. **Wire:** copy tip `AGENTS.md` + symlink `scripts` → tip `scripts`; copy
   `adapters/cursor/config.snippet.yaml` → foreign `.emperor/config.yaml`.
   Point Cursor `.cursor/rules` (if present) at AGENTS.md — honest paste only
   (`install.sh` has no `cursor` harness).
2. **Boot:** `python3 $ET/scripts/lib/boot.py --root . --skip-eval` (foreign).
   Read `.emperor/host.env` + `survey.md`.
3. **MUST-route:** `activate.py --cwd . -u "<tiny ask>"`; open `ACTIVATION next=`.
4. **ask→spec:** `--emit --effort-class tiny` (judgment stays off).
5. **Change:** one wording/one-liner class edit only.
6. **done:** `done.py` on the task dir — record exit code.
7. **Binary lane:** `cursor-agent status` → if **Not logged in**, mark **BLOCKED**;
   do not run login flows or paste `CURSOR_API_KEY`. Optional print probe only
   when Logged in and PO asked.
8. **ORI live (when binary BLOCKED):** run OpenCode **TTY/PTY** smoke with
   `openrouter/stealth/space-bunny-alpha` (or PO-named slug) on the foreign dir.
   Optional OpenAI-compat HTTPS if OpenCode flakes is **compat/fallback only** —
   not ORI live PASS (**TTY-as-gate**). Label host **OpenCode/ORI**. Score
   **ORI live PASS/FAIL** separately from equal-UX **HOLD**. Do not chase login.
9. **Receipt:** MATRIX/NOTES + raw/ under
   `/workspace/field-receipts/receipts/<date>/bet-f-ori-cursor/` (or dated
   Cursor receipt dir) with triage labels (structure PASS vs binary BLOCKED vs
   ORI live PASS/FAIL vs equal-UX HOLD). MATRIX/SUMMARY must cite the **final
   ship tip SHA** (ban stale tip labels).

## Pass / fail

| Result | Meaning |
|---|---|
| done exit 0 + honest probes | **PASS** (structure exercised) |
| done FAIL, probes/config wrong | **ET-bug** |
| done FAIL / nonsense after correct ET path | **model-FAIL** |
| `Not logged in` / no cursor-agent | **BLOCKED** (binary; disclose) — run ORI live next |
| ORI live green (OpenCode **TTY/PTY**, host labeled) | **PASS** (ORI live) — still not equal-UX; HTTPS compat alone ≠ ORI live PASS |
| ORI live red (auth/quota/hang) | **FAIL** / **BLOCKED** (model-route; honest) |
| structure green, no IDE/binary green + PO | **HOLD** equal-UX — do not auto-claim |

Do **not** sell structure PASS or ORI live PASS as equal-UX-proven.
Do **not** chase Cursor login to unblock a smoke.
