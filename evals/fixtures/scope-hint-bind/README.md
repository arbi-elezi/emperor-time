# scope-hint-bind fixtures

Prove ask→spec out-of-scope hint-corpus HARD-GATE
(`ask_spec.py --reject-over-scope-class` / `--check-scope-hints`).

SPEC_HINT_BIND binds Ask(quoted)∪goal∪done-when. Scope-hint bind closes
the remaining bypass: park tiny-hint language ("fix typo" / "one-line")
in out-of-scope while Ask/goal/done-when stay clean so FORCE_TABLE[large]
/ EFFORT_CAPS[large] unlock while SPEC_HINT_BIND stays green. Harness
owns force — agent does not inflate class by editing out-of-scope.

Length-only infer stays advisory. Only strong `_TINY_HINTS` bind.
`_LARGE_HINTS` lift the ceiling. Tighter-than-hint class remains OK.
Rejected: binding noisy `_SMALL_HINTS` (HARD-GATE/fixture/patch).

| Fixture | Expect |
|---|---|
| `task-scope-park/` | FAIL — out-of-scope tiny hints, Ask/goal/done-when clean, effort_class:large |
| `task-clean/` | PASS — tiny-hint corpus + effort_class:tiny |
| `task-tighter/` | PASS — no tiny hints; medium class unbound |
| `task-vacuous/` | `--check-scope-hints` SKIP vacuous (no ask→spec) |

Honesty: `--check-spec-hints` may PASS on scope-park (Ask/goal/done-when
clean) while `--check-scope-hints` FAILS — distinct from SPEC_HINT_BIND.
Iron: `SCOPE_HINT_BIND` (alongside `SPEC_HINT_BIND` / `ASK_HINT_BIND`).
G4 wires `_run_scope_hints` after `_run_spec_hints`. v0.4.159.
