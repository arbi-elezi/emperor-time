# Writing good tests (HARD-GATE)

Chain Jail leaf aspect from obra/superpowers
`skills/test-driven-development/writing-good-tests.md` (MIT),
accessed 2026-09-27 — Name the Break / Exercise the Real Thing /
Gate Function / Mutation Check only.

https://github.com/obra/superpowers/blob/main/skills/test-driven-development/writing-good-tests.md

sha256 (writing-good-tests.md):
`51471c853306ff92ca8bb41dcaea05f31c0e46b03651f8f3c99754b7172f4ae1`

Mechanical card: `scripts/emperor good-tests`
(`scripts/lib/good_tests.py`). Skill leaf:
`skills/emperor-tdd/writing-good-tests.md`.

## Iron

```
EVERY TEST NAMES THE BREAK
```

1. **Name the break** — a bug-shaped production change, not a redesign.
2. **Exercise the real thing** — mock earns no assertions.
3. **Hand-derive want** — no mirror builders from the code under test.
4. **Mutation check** before finish.

## Flags

```
scripts/emperor good-tests --reject-mirror
scripts/emperor good-tests --reject-change-detector
scripts/emperor good-tests --check-named-break "Name the break: wrong branch handler. Exercise the real component. Hand-derived literal want. Mutation check for empty return."
```

`--check-named-break` needs name-the-break plus real-thing / hand-derived /
mutation / gate-before.

## Out of scope (not this leaf)

- Whole `test-driven-development` skill vendoring
- Red-Green-Refactor iron law (sibling leaf `red-green-refactor.md`)
- embeddings / emperor.py dispatcher
