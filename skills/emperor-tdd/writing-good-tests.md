# Writing good tests — Name the Break / Exercise the Real Thing HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/test-driven-development/writing-good-tests.md
- source-hash: sha256:51471c853306ff92ca8bb41dcaea05f31c0e46b03651f8f3c99754b7172f4ae1
- heading: Name the Break / Exercise the Real Thing / Gate Function / Mutation Check
- license: MIT
- access-date: 2026-09-27
- issue-context: after RGR iron-law, agents still ship mirror assertions, change detectors, and mock-existence checks; Chain Jail extract-aspect names writing-good-tests companion only (not whole test-driven-development). Sibling leaf: red-green-refactor.

**Contract:** before writing or changing a test, **name the production break** it catches and **exercise the real thing**. Hand-derive expectations. Run the mutation check before finish. Emperor Time stays the orchestrator via emperor-tdd; do **not** announce or load whole `test-driven-development`.

Mechanical card: `scripts/emperor good-tests` (Python: `scripts/lib/good_tests.py`).
Companion reference: `references/writing-good-tests.md`.
RGR companion: `skills/emperor-tdd/red-green-refactor.md` + `emperor tdd`.

## HARD-GATE — Every test names the break

```
EVERY TEST NAMES THE BREAK
```

"Assert the mock / mirror the builder / lock a constant"? **Not enough.** Name a bug-shaped production change. Exercise the real component.

## Principles (adapted)

1. **Name the Break** — every test names the production change that would make it fail (a bug, not a redesign decision).
2. **Exercise the Real Thing** — mock earns no assertions; assert real behavior; unmock or delete mock-existence checks.
3. **Hand-derived expectations** — literals / hand-checked fixtures; never reuse code-under-test helpers for want.
4. **Mutation check** — before finish, at least one test fails for each realistic production mutation.

## Gate Function (before body)

```
BEFORE writing the test body:
  Name the production change that would make this test fail.

  Cannot name one            → redesign around an observable behavior
  "The source text changed"  → run the artifact and assert its effects
  Only intentional decisions → change detector; test the behavior
                               that depends on the decision

  Confirm the expected value is derived without the code under test.
```

## Mechanical flags

```
scripts/emperor good-tests --reject-mirror
scripts/emperor good-tests --reject-change-detector
scripts/emperor good-tests --check-named-break "Name the break: wrong branch. Exercise the real component. Hand-derived literal. Mutation check."
```

`--reject-mirror` / `--reject-change-detector` always exit non-zero.
`--check-named-break` needs name-the-break plus real-thing / hand-derived / mutation / gate-before signals.
