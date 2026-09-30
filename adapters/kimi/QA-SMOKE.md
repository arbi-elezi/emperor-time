# QA smoke — Kimi + ORI via OpenCode (≤1 page)

**Goal:** exercise ET boot→activate→done on a **foreign** tiny ask, then prove
**ORI live** with one locked OpenRouter Kimi slug under a real TTY. Judgment
off. Iron hard. Triage **ET-bug | model-FAIL | PASS | blocked**.

## Preferred paths (label the host honestly)

1. **Structure (always):** tip `AGENTS.md` + `scripts/` + `config.snippet.yaml`.
   No OpenCode binary and no API key required. A green `done` here is
   **structure PASS**, not equal-UX and not ORI live.
2. **ORI live (required for this bet's live gate):** OpenCode with a real TTY
   (`script` / PTY), timeout ≤30s, locked slug
   `openrouter/moonshotai/kimi-k3`. Host label mandatory:
   **Kimi model via OpenCode/ORI**. Auth = `OPENROUTER_API_KEY` only (never
   print/commit). Do **not** sell free-catalog toys (`space-bunny`,
   `opencode/*-free`) as Kimi proof. If K3 is unavailable → **blocked** + PO
   ping; one Kimi-family successor OK only with an honest inventory note.
3. **Native Kimi CLI:** out of scope for equal-UX (standing policy). Pointers
   live in `adapters/kimi-cli/`. Absence of `kimi` does **not** block this pack.

## Prereqs checklist

- [ ] Emperor-Time tip checked out (record SHA / 0.4.174+)
- [ ] `opencode --version` works with `PATH` including `~/.local/bin` (or absolute
      path) **or** mark OpenCode binary **blocked**
- [ ] `OPENROUTER_API_KEY` present in env / OpenCode auth store **or** mark ORI
      **blocked** (do not print the key)
- [ ] Foreign repo cloned (not bakeoff T1–T4, not is-buffer/isarray/is-obj redo,
      not emperor-time itself)

## Steps

1. **Wire:** copy tip `AGENTS.md` + symlink `scripts` → tip `scripts`; copy
   `adapters/kimi/config.snippet.yaml` → foreign `.emperor/config.yaml`.
2. **Boot:** `python3 $ET/scripts/lib/boot.py --root . --skip-eval` (foreign).
   Read `.emperor/host.env` + `survey.md`.
3. **MUST-route:** `activate.py --cwd . -u "<tiny ask>"`; open `ACTIVATION next=`.
4. **ask→spec:** `--emit --effort-class tiny` (judgment stays off).
5. **Change:** one wording/one-liner class edit only. No upstream PR without consent.
6. **done:** write `DONE.md` probes that match the edit; `done.py` — record exit code.
7. **ORI live:** ensure `PATH` includes `~/.local/bin`. Prefer:
   `timeout 30 script -q -c 'opencode run -m openrouter/moonshotai/kimi-k3 --dir . "<same ask>"' /dev/null`
   Bare pipe may hang after `init` → EXIT **124** — that is non-TTY, not a
   model-FAIL. Missing binary / missing key / slug 404 → ORI lane **blocked**.
8. **Receipt:** CONTEXT / BEFORE / AFTER / NOTES / claim under
   `/workspace/field-receipts/receipts/<date>/bet-g-kimi-ori/` with **separate**
   structure vs ORI triage labels and the mandatory host label. No secrets.

## Pass / fail

| Result | Meaning |
|---|---|
| done exit 0 + honest probes | **PASS** (structure exercised) — not equal-UX |
| done FAIL, probes/config wrong | **ET-bug** |
| done FAIL / nonsense after a correct ET path on a live model | **model-FAIL** |
| OpenCode TTY + locked `moonshotai/kimi-k3` green (ORI) | **ORI live PASS** — host = **Kimi model via OpenCode/ORI**; **not** native Kimi equal-UX |
| Locked K3 unavailable / 404 | **blocked** (slug inventory) — ping PO; do not swap to non-Kimi free catalog |
| hang after `init` → EXIT 124 (pipe/non-TTY) | **blocked** binary lane — use `script`/`pty`; do not claim ORI live from bare pipe |
| no OpenCode / no `OPENROUTER_API_KEY` | **blocked** (ORI lane; structure may still PASS) |

Do **not** sell a toy or free-catalog PASS as Kimi proof, Astra-bridge, or
mid-16B proof. Do **not** claim native Kimi CLI equal-UX from structure PASS
or from ORI live PASS.
