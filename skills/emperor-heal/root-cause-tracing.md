# Root-cause tracing — backward chain HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/root-cause-tracing.md
- source-hash: sha256:75b933b6a8c40bdb2031b10f21654395b56ec6ab6bc7b018c18d3fe57aeb7fb8
- heading: Trace backward / Fix at source / Never fix just the symptom
- license: MIT
- access-date: 2026-09-27
- issue-context: heal four-phase card names "trace data flow" in Phase 1 but lacked a mechanical backward-chain HARD-GATE; Chain Jail extract-aspect names Trace-backward / Fix-at-source only (not whole systematic-debugging, not find-polluter.sh, not pressure tests). Sibling Chain Jail leaves: defense-in-depth (`emperor defense`), condition-based-waiting (`emperor wait`).

**Contract:** when a bug appears deep in the call stack (wrong cwd, empty path, bad value far from entry), finish a **backward trace to the original trigger** before proposing a fix. Fix at the source, not where the error prints. Emperor Time stays the orchestrator via Holy Chain / emperor-heal; do **not** announce or load whole `systematic-debugging`.

Mechanical card: `scripts/emperor trace` (Python: `scripts/lib/root_cause.py`).
Companion reference: `references/root-cause-tracing.md`.
Phase order companion: `skills/emperor-heal/debug-four-phases.md` + `emperor heal`.

## HARD-GATE — No symptom fix without source trace

```
NO SYMPTOM FIX WITHOUT SOURCE TRACE
```

No backward chain to the original trigger? **Do not patch the symptom site.** Keep tracing up (or instrument and re-run) until the source is named.

## The tracing process

1. **Observe the Symptom** — quote the error / wrong path / bad value.
2. **Find Immediate Cause** — which code directly causes it?
3. **Ask: What Called This?** — one level up, with the value passed.
4. **Keep Tracing Up** — repeat until the bad value originates.
5. **Find Original Trigger** — fix THERE. Optional defense-in-depth layers are additive after the source fix (mechanical card: `scripts/emperor defense` / `skills/emperor-heal/defense-in-depth.md`).

Dead end (cannot trace further): record the dead end, fix at the last reachable layer, and say so honestly. Prefer the source when reachable.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "The stack trace already shows the failing line" | That is the symptom. Trace who called it with the bad value. |
| "Quick guard at the symptom will unblock CI" | Guards without a source fix hide the wound. Trace first. |
| "I cannot see callers, so I will patch locally" | Instrument (stack/log at the failing op), re-run, then read the chain. |
| "Load systematic-debugging" | Forbidden — leaf only; ET + Holy Chain orchestrate. |

## ET mapping

| Need | Where |
|---|---|
| Backward-trace HARD-GATE | emperor-heal + `emperor trace` |
| Phase order (1→4) | emperor-heal + `emperor heal` |
| Session locate / intake | session-discovery / diagnose |
| Multi-layer validation after source fix | emperor-heal + `emperor defense` |
| Condition-based waiting (flaky/timing) | emperor-heal + `emperor wait` |
