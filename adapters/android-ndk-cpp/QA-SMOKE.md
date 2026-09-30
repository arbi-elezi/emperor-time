# QA smoke — Android NDK/C++ domain pack (≤1 page)

**Goal:** exercise ET boot→activate→ask→spec→done on a **foreign** tiny
**C++/JNI-shaped** ask; confirm toolchain honesty; prove **ORI live** with
OpenCode TTY + `stealth/space-bunny-alpha` (multi-probe when cheap). Judgment
off. Iron hard. Triage **ET-bug | model-FAIL | PASS | BLOCKED | HOLD**.

**Toolchain:** this pack is built with **ET+ORI** (OpenCode +
`stealth/space-bunny-alpha`) as the coding toolchain, so each ET pack is the
recursive build of the next one with the tool itself. Receipts must show
**real harness utilization** with the host labeled **OpenCode/ORI**.
MATRIX/SUMMARY must cite the **final ship tip SHA** (no stale tip labels).

## Preferred paths (label the host honestly)

1. **Structure (always):** tip `AGENTS.md` + `scripts/` + `config.snippet.yaml`
   on a CMake/JNI-shaped foreign leaf. No NDK and no API key required. Green
   `done` = **structure PASS**, not equal-UX and not ORI live.
2. **Toolchain:** if `ANDROID_NDK_HOME` unset and `ndk-build` absent → label
   **BLOCKED**. Do **not** install NDK/SDK/emulator. Structure + ORI still valid.
3. **ORI live:** OpenCode real TTY (`script` / PTY), slug
   `openrouter/stealth/space-bunny-alpha`. Host label: **OpenCode/ORI**. Prefer
   a small MATRIX (≥2–3 cheap probes: token, surface triage, iron refuse) —
   not one token toy only. Auth = `OPENROUTER_API_KEY` only (never print/commit).
   Canonical stranger ORI contract: `adapters/opencode/ORI-REGRESSION.md` (do not fork checklists).
4. **Equal-UX / native Android CLI:** out of scope (standing policy).

## Prereqs checklist

- [ ] Emperor-Time tip checked out (record SHA / 0.4.174+)
- [ ] NDK probe recorded (expect BLOCKED on boxes without NDK)
- [ ] `opencode --version` with `PATH` incl. `~/.local/bin` **or** mark ORI binary **BLOCKED**
- [ ] `OPENROUTER_API_KEY` present **or** mark ORI **BLOCKED** (do not print)
- [ ] Foreign C++/JNI-shaped tree (not bakeoff T1–T4, not emperor-time itself)

## Steps

1. **Wire:** copy tip `AGENTS.md` + symlink `scripts` → tip `scripts`; copy
   `adapters/android-ndk-cpp/config.snippet.yaml` → foreign `.emperor/config.yaml`.
2. **Boot:** `python3 $ET/scripts/lib/boot.py --root . --skip-eval` (foreign).
3. **MUST-route:** `activate.py --cwd . -u "<tiny C++/JNI ask>"`; open `ACTIVATION next=`.
4. **ask→spec:** `--emit --effort-class tiny` (judgment off). Name the surface.
5. **Change:** one wording / one export / one comment class edit only.
6. **done:** `DONE.md` with `probe:`/`expect:` matching the edit; record exit.
7. **Toolchain:** record `ANDROID_NDK_HOME` + `ndk-build` raw → BLOCKED if absent.
8. **ORI live (multi-probe):** `timeout 30 script -q -c 'opencode run -m openrouter/stealth/space-bunny-alpha --dir . "<probe>"' /dev/null` for each MATRIX row. *(Darwin/BSD: no `script -c` — use `script -q file cmd` or `python3` `pty.spawn`.)* Bare pipe → EXIT 124 is non-TTY, not model-FAIL. **ORI live PASS = TTY-as-gate.**
9. **Receipt:** CONTEXT / MATRIX / NOTES / claim + raw/ under
   `/workspace/field-receipts/receipts/<date>/bet-h-android-cpp/`. No secrets.

## Pass / fail

| Result | Meaning |
|---|---|
| done exit 0 + honest probes on C++/JNI ask | **PASS** (structure) — not equal-UX |
| done FAIL, probes/config wrong | **ET-bug** |
| NDK/`ndk-build` absent | **BLOCKED** (toolchain) — expected on many boxes |
| OpenCode TTY + slug green on MATRIX probes | **ORI live PASS** — host = **OpenCode/ORI** |
| hang after `init` → EXIT 124 (pipe) | **BLOCKED** binary lane — use `script`/`pty` |
| no OpenCode / no key | **BLOCKED** (ORI; structure may still PASS) |
| equal-UX / game / emulator claim | **refused** — out of scope |

Do **not** install NDK to flip toolchain. Do **not** claim native Android CLI
equal-UX from structure or ORI PASS.
