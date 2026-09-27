# Defense-in-depth (multi-layer validation HARD-GATE)

Emperor Time owned guidance for post-source-fix layered validation.
Adapted from
[obra/superpowers](https://github.com/obra/superpowers)
`skills/systematic-debugging/defense-in-depth.md` (MIT), accessed 2026-09-27
— Validate at every layer / The Four Layers only.
ET + Holy Chain remain the orchestrator; do not load whole
systematic-debugging.

Mechanical card: `scripts/emperor defense`
(`scripts/lib/defense.py`). Skill leaf:
`skills/emperor-heal/defense-in-depth.md`.
Source-fix companion: `scripts/emperor trace`.
Phase companion: `scripts/emperor heal`.

## Iron law

1. **No single-layer validation** as the whole fix for invalid-data bugs.
2. Layers: entry → business → environment → debug.
3. Source fix first (`emperor trace`). Layers are additive, not a substitute.

## HARD-GATE helpers

```bash
scripts/emperor defense --reject-single-layer   # always exit 1
scripts/emperor defense --reject-unlayered      # always exit 1
scripts/emperor defense --check-layers "entry + business + environment"
```

`--check-layers` needs at least two distinct layer ids (`entry`, `business`,
`environment`, `debug`).

## Out of scope

- Whole `systematic-debugging` skill folder
- `find-polluter.sh`, condition-based-waiting, pressure / academic packs
- Replacing root-cause tracing with layered guards
