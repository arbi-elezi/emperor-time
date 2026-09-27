# Find polluter — find which test creates unwanted state HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/find-polluter.sh
- source-hash: sha256:dd7b8f13c4cc2a24b33ff87b18da9248f3e1c80a085c3316224f69ff0fa5c43c
- heading: Find which test creates unwanted files/state / do not guess the polluter
- license: MIT
- access-date: 2026-09-27
- issue-context: after condition-based-waiting, shared-state / leftover files still invite guessing which test polluted; Chain Jail extract-aspect names find-polluter only (not whole systematic-debugging, not pressure/academic packs). Sibling leaves: four-phases, root-cause-tracing, defense-in-depth, condition-based-waiting.

**Contract:** when leftover files or shared state break later tests, **find which test creates the pollution** by running candidates one-by-one (or bisecting). Do not guess. Stop at the first creator; fix cleanup there. Emperor Time stays the orchestrator via Holy Chain / emperor-heal; do **not** announce or load whole `systematic-debugging`.

Mechanical card: `scripts/emperor polluter` (Python: `scripts/lib/polluter.py`).
Companion reference: `references/find-polluter.md`.
Phase order companion: `skills/emperor-heal/debug-four-phases.md` + `emperor heal` (Phase 1–2 shared-state).
Source-fix companion: `skills/emperor-heal/root-cause-tracing.md` + `emperor trace`.
Timing companion: `skills/emperor-heal/condition-based-waiting.md` + `emperor wait` (different leaf).

## HARD-GATE — No guess the polluter

```
NO GUESS THE POLLUTER
```

"Probably the setup file"? **Not enough.** Name the marker; list candidates; run one-by-one until FOUND POLLUTER; investigate that test only.

## Bisect steps

1. **Name the pollution marker** — path / file / dir that should not exist after a clean run.
2. **List candidate tests** — enumerate test files matching the suite pattern (sorted).
3. **Run one test at a time** — before each run confirm marker absent; run only that test.
4. **Stop at first creator** — first test that creates the marker is the polluter.
5. **Investigate that test only** — fix cleanup / isolation there (not elsewhere).

Rules: marker must be absent before a candidate; runner-agnostic (pytest / npm test / go test / …); stop at first FOUND POLLUTER; fix teardown at the polluter, do not paper over with later deletes.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "It is probably the setup hook" | Guessing. Run candidates until FOUND POLLUTER. |
| "Delete the leftover in afterAll instead" | Papers over the polluter. Fix cleanup where it is created. |
| "Re-run the whole suite until green" | Order luck is not a root cause. Identify the creator. |
| "Load systematic-debugging" | Forbidden — leaf only; ET + Holy Chain orchestrate. |

## ET mapping

| Need | Where |
|---|---|
| Find-polluter HARD-GATE | emperor-heal + `emperor polluter` |
| Phase order (1→4) / shared-state | emperor-heal + `emperor heal` |
| Backward-trace / source fix | emperor-heal + `emperor trace` |
| Flaky / timing waits | emperor-heal + `emperor wait` |
