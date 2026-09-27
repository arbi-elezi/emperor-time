# Defense-in-depth — multi-layer validation HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/defense-in-depth.md
- source-hash: sha256:1e175fb86fc357e58c6aebf5441e481e1b7868b4380c0456b63a17eefbd18ba7
- heading: Validate at every layer / The Four Layers
- license: MIT
- access-date: 2026-09-27
- issue-context: after root-cause source fix, agents still ship a single guard at one site; Chain Jail extract-aspect names Validate-at-every-layer / Four-layers only (not whole systematic-debugging, not find-polluter.sh, not condition-based-waiting, not pressure tests).

**Contract:** when a bug was caused by invalid data, after fixing at the source, add validation at **every layer** data passes through so the bug becomes structurally impossible. Emperor Time stays the orchestrator via Holy Chain / emperor-heal; do **not** announce or load whole `systematic-debugging`.

Mechanical card: `scripts/emperor defense` (Python: `scripts/lib/defense.py`).
Companion reference: `references/defense-in-depth.md`.
Source-fix companion: `skills/emperor-heal/root-cause-tracing.md` + `emperor trace`.
Phase order companion: `skills/emperor-heal/debug-four-phases.md` + `emperor heal`.

## HARD-GATE — No single-layer validation

```
NO SINGLE LAYER VALIDATION
```

One check at one site? **Not enough.** Map checkpoints; add entry / business / environment / debug layers. Defense-in-depth is additive after the source fix — never a substitute for tracing.

## The four layers

1. **Entry Point Validation** — reject obviously invalid input at the API / CLI boundary.
2. **Business Logic Validation** — ensure data makes sense for this operation.
3. **Environment Guards** — refuse dangerous ops in test / CI / wrong-cwd contexts.
4. **Debug Instrumentation** — capture stack/context at the dangerous op for forensics.

Applying the pattern: trace data flow → map all checkpoints → add validation at each layer → try to bypass layer 1 and verify layer 2+ catches it.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "Entry validation already rejects empty paths" | Other paths / mocks / refactoring bypass it. Add deeper layers. |
| "One guard is faster" | Single-layer fixes feel done; multi-layer makes the bug impossible. |
| "Layers replace tracing to the source" | Forbidden. Trace + fix at source first (`emperor trace`), then layer. |
| "Load systematic-debugging" | Forbidden — leaf only; ET + Holy Chain orchestrate. |

## ET mapping

| Need | Where |
|---|---|
| Multi-layer validation HARD-GATE | emperor-heal + `emperor defense` |
| Backward-trace / source fix | emperor-heal + `emperor trace` |
| Phase order (1→4) | emperor-heal + `emperor heal` |
