# Find polluter (HARD-GATE)

Emperor Time owned guidance for shared-state / leftover-file pollution.
Adapted from
[obra/superpowers](https://github.com/obra/superpowers)
`skills/systematic-debugging/find-polluter.sh` (MIT), accessed 2026-09-27
— Find which test creates unwanted files/state / do not guess the polluter only.
Source URL:
https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/find-polluter.sh
sha256:dd7b8f13c4cc2a24b33ff87b18da9248f3e1c80a085c3316224f69ff0fa5c43c
ET + Holy Chain remain the orchestrator; do not load whole
systematic-debugging.

Mechanical card: `scripts/emperor polluter`
(`scripts/lib/polluter.py`). Skill leaf:
`skills/emperor-heal/find-polluter.md`.
Phase companion: `scripts/emperor heal` (Phase 1–2).
Source-fix companion: `scripts/emperor trace`.
Timing companion: `scripts/emperor wait` (different leaf).

## Iron law

1. **No guess the polluter** — run candidates one-by-one (or bisect).
2. Name the marker. Marker must be absent before each candidate run.
3. Stop at first creator. Fix cleanup at the polluter test.

## HARD-GATE helpers

```bash
scripts/emperor polluter --reject-guess          # always exit 1
scripts/emperor polluter --reject-unbisected     # always exit 1
scripts/emperor polluter --check-found "FOUND POLLUTER Test: src/foo.test.ts Created: .git"
```

`--check-found` needs polluter identity (`FOUND POLLUTER` + test path, or
`polluter` / `created:` / path signals).

## Out of scope

- Whole `systematic-debugging` skill folder
- Pressure / academic packs (`test-pressure-*.md`, `test-academic.md`)
- Replacing root-cause tracing with a guessed cleanup elsewhere
- Hardcoding one test runner (npm-only); ET card is runner-agnostic
