# Condition-based waiting — wait for the actual condition HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/condition-based-waiting.md
- source-hash: sha256:e89fec8400d6cd50f43407cec9fab50976ba4d55d0ec2eb51c0bd68036b54c26
- heading: Wait for the actual condition / not a guess about timing
- license: MIT
- access-date: 2026-09-27
- issue-context: after defense-in-depth, flaky tests still guess at timing with arbitrary sleep/setTimeout; Chain Jail extract-aspect names Wait-for-the-actual-condition only (not whole systematic-debugging, not find-polluter.sh; pressure/academic is sibling leaf `emperor pressure`). Sibling leaves: four-phases, root-cause-tracing, defense-in-depth.

**Contract:** when a test or async path waits, wait for the **actual condition** (event / state / count / file), not a guess about how long it takes. Always timeout; poll ~10ms; fresh getter inside the loop. Emperor Time stays the orchestrator via Holy Chain / emperor-heal; do **not** announce or load whole `systematic-debugging`.

Mechanical card: `scripts/emperor wait` (Python: `scripts/lib/condition_wait.py`).
Companion reference: `references/condition-based-waiting.md`.
Phase order companion: `skills/emperor-heal/debug-four-phases.md` + `emperor heal` (Phase 4 flaky/timing cure).
Source-fix companion: `skills/emperor-heal/root-cause-tracing.md` + `emperor trace`.
Layers companion: `skills/emperor-heal/defense-in-depth.md` + `emperor defense`.

## HARD-GATE — No arbitrary sleep

```
NO ARBITRARY SLEEP
```

`setTimeout` / `sleep` / `time.sleep` as the wait? **Not enough.** Name the condition; poll until it is true; always timeout. Document WHY only when testing real timed behavior after the trigger condition.

## Condition patterns

1. **Wait for event** — poll until the named event appears.
2. **Wait for state** — poll until machine/object reaches ready / target state.
3. **Wait for count** — poll until length / count meets the threshold.
4. **Wait for file** — poll until path exists / is readable.

Rules: poll ~10ms; always include a timeout with a clear error; call the getter inside the loop (no stale cache); if an arbitrary timeout is truly needed, document WHY after waiting for the trigger.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "50ms is usually enough on my machine" | CI / load / parallel runs race. Wait for the condition. |
| "sleep is simpler than waitFor" | Simple flakes. Condition waits pass under load. |
| "No timeout keeps it flexible" | Forever loops hide deadlocks. Always timeout. |
| "Load systematic-debugging" | Forbidden — leaf only; ET + Holy Chain orchestrate. |

## ET mapping

| Need | Where |
|---|---|
| Condition-based waiting HARD-GATE | emperor-heal + `emperor wait` |
| Phase order (1→4) / flaky cure | emperor-heal + `emperor heal` |
| Backward-trace / source fix | emperor-heal + `emperor trace` |
| Multi-layer validation after source fix | emperor-heal + `emperor defense` |
