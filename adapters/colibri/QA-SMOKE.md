# QA smoke: Colibrì integrate-if-you-want (≤1 page)

**Goal:** exercise ET boot, activate, ask then spec, tiny change, `done` on a
**foreign** tiny ask. Judgment off. Iron hard. Triage **ET-bug | model-FAIL |
PASS | blocked**. Label structure vs Colibrì-live vs optional compat-shape
separately.

## Preferred paths (label honestly)

1. **Structure (always required):** tip `AGENTS.md` + `scripts/` +
   `adapters/colibri/config.snippet.yaml`. No `coli` binary required. Green
   `done` here is **structure PASS**, not Colibrì engine PASS and not equal-UX.
2. **Colibrì engine live (preferred when available):** real `coli serve` on
   localhost with a converted model. Hit `/v1/models` or a short
   `/v1/chat/completions`. If `coli` or a usable model is missing, record
   **Colibrì engine live = BLOCKED** with reason (disk, RAM, binary, build).
   Do not silent-skip.
3. **Optional OpenAI-compat shape:** local stand-in (example colibri-toy /
   llama.cpp HTTP) that exercises the same base-URL wiring. Label
   **compat-shape** only. **Never** sell as Colibrì engine PASS.
4. **Recursive build / coding toolchain:** OpenCode + ORI (example
   space-bunny-alpha) while shipping docs is toolchain only, not Colibrì proof.

## Prereqs checklist

- [ ] Emperor-Time tip checked out (record SHA / 0.4.174; bakeoff PIN 0.4.171)
- [ ] `coli doctor` / `coli plan` work **or** mark Colibrì engine **BLOCKED**
- [ ] Foreign disposable repo cloned (not bakeoff T1–T4, not prior bet foreign
      ids, not emperor-time itself)
- [ ] No secrets printed or committed

## Steps

1. **Wire:** copy tip `AGENTS.md` + symlink `scripts` to tip `scripts`; copy
   `adapters/colibri/config.snippet.yaml` to foreign `.emperor/config.yaml`.
2. **Boot:** `python3 $ET/scripts/lib/boot.py --root . --skip-eval` (foreign).
   Read `.emperor/host.env` + `survey.md`.
3. **MUST-route:** `activate.py --cwd . -u "<tiny ask>"`; open `ACTIVATION next=`.
4. **ask then spec:** `--emit --effort-class tiny` (judgment stays off).
5. **Change:** one wording / one-liner class edit only. No upstream PR without
   consent.
6. **done:** write `DONE.md` with `probe:` / `expect:` lines that match the
   edit; `done.py` (record exit code).
7. **Colibrì live:** if `coli` is present and a model is usable, start
   `coli serve`, smoke `/v1`, record PASS. Else **BLOCKED** + reason.
8. **Optional shape:** if a stand-in HTTP server is already available, one short
   chat completion; label shape only.
9. **Receipt:** CONTEXT / BEFORE / AFTER / NOTES / SUMMARY (or claim) under
   `/workspace/field-receipts/receipts/<date>/bet-i-colibri-integrate/` with
   separate triage labels. Redact secrets.

## Pass / fail

| Result | Meaning |
|---|---|
| done exit 0 + honest probes | **structure PASS** (not Colibrì engine, not equal-UX) |
| done FAIL, probes/config wrong | **ET-bug** |
| done FAIL / nonsense after a correct ET path on a live model | **model-FAIL** |
| no `coli` binary, or no usable model / disk / RAM | **Colibrì engine live = BLOCKED** |
| `coli serve` + short `/v1` green | **Colibrì engine live PASS** |
| llama.cpp / toy HTTP green | **compat-shape** only (not Colibrì engine) |
| OpenCode + ORI while shipping | coding toolchain only (not Colibrì proof) |

Do **not** sell structure PASS, toy shape, or ORI toolchain as Colibrì engine
PASS. Do **not** claim harness ownership or native equal-UX from this pack.
