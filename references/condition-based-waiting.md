# Condition-based waiting (HARD-GATE)

Emperor Time owned guidance for flaky / timing waits.
Adapted from
[obra/superpowers](https://github.com/obra/superpowers)
`skills/systematic-debugging/condition-based-waiting.md` (MIT), accessed 2026-09-27
— Wait for the actual condition / not a guess about timing only.
Source URL:
https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/condition-based-waiting.md
sha256:e89fec8400d6cd50f43407cec9fab50976ba4d55d0ec2eb51c0bd68036b54c26
ET + Holy Chain remain the orchestrator; do not load whole
systematic-debugging.

Mechanical card: `scripts/emperor wait`
(`scripts/lib/condition_wait.py`). Skill leaf:
`skills/emperor-heal/condition-based-waiting.md`.
Phase companion: `scripts/emperor heal` (Phase 4).
Source-fix companion: `scripts/emperor trace`.
Layers companion: `scripts/emperor defense`.

## Iron law

1. **No arbitrary sleep** (`setTimeout` / `sleep` / `time.sleep`) as the wait.
2. Wait for event / state / count / file. Poll ~10ms. Always timeout.
3. Fresh getter inside the loop. Document WHY only when timed behavior is real.

## HARD-GATE helpers

```bash
scripts/emperor wait --reject-sleep          # always exit 1
scripts/emperor wait --reject-unguessed      # always exit 1
scripts/emperor wait --check-condition "waitFor ready state"
```

`--check-condition` needs at least one strong token (`waitfor`, `until`,
`condition`, `poll`, `exists`, `ready`, `event`) or a waitFor-style pattern.

## Out of scope

- Whole `systematic-debugging` skill folder
- Pressure / academic packs (find-polluter is a separate leaf: `emperor polluter`)
- Replacing root-cause tracing or defense-in-depth with blind sleeps
