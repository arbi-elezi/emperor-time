# Root-cause tracing (backward chain HARD-GATE)

Emperor Time owned guidance for Phase-1 backward tracing.
Adapted from
[obra/superpowers](https://github.com/obra/superpowers)
`skills/systematic-debugging/root-cause-tracing.md` (MIT), accessed 2026-09-27
— Trace backward / Fix at source / Never fix just the symptom only.
ET + Holy Chain remain the orchestrator; do not load whole
systematic-debugging.

Mechanical card: `scripts/emperor trace`
(`scripts/lib/root_cause.py`). Skill leaf:
`skills/emperor-heal/root-cause-tracing.md`.
Phase companion: `references/` via heal four-phases
(`scripts/emperor heal`).

## Iron law

1. **No symptom fix without a source trace.**
2. Trace: symptom → immediate cause → caller → … → original trigger.
3. Fix at the source. Defense-in-depth layers are optional and additive.

## HARD-GATE helpers

```bash
scripts/emperor trace --reject-symptom-fix   # always exit 1
scripts/emperor trace --reject-untraced        # always exit 1
scripts/emperor trace --check-chain "A → called by B → called by C"
```

`--check-chain` needs at least two backward links (`called by`, `→`, `←`,
`->`, or `<-`).

## Out of scope

- Whole `systematic-debugging` skill folder
- `find-polluter.sh`, defense-in-depth essay, condition-based-waiting
- Pressure / academic test packs from that skill
