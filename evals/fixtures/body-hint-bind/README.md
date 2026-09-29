# body-hint-bind fixtures

Prove ask→spec full-file body hint-corpus HARD-GATE
(`ask_spec.py --reject-over-body-class` / `--check-body-hints`).

SCOPE_HINT_BIND binds Ask(quoted)∪goal∪done-when∪out-of-scope. Body-hint
bind closes the remaining bypass: park tiny-hint language ("fix typo" /
"one-line") in ## Notes / ## Context / stray bullets while
Ask/goal/done-when/out-of-scope stay clean so FORCE_TABLE[large] /
EFFORT_CAPS[large] unlock while SCOPE_HINT_BIND stays green. Harness
owns force — agent does not inflate class by editing freeform sections.

Length-only infer stays advisory. Only strong `_TINY_HINTS` bind.
`_LARGE_HINTS` lift the ceiling. Tighter-than-hint class remains OK.
Rejected: binding noisy `_SMALL_HINTS` (HARD-GATE/fixture/patch).
Ledger-wide park closed by `TASK_HINT_BIND` (v0.4.161).

| Fixture | Expect |
|---|---|
| `task-notes-park/` | FAIL — Notes tiny hints, Ask/goal/done-when/oos clean, effort_class:large |
| `task-clean/` | PASS — tiny-hint corpus + effort_class:tiny |
| `task-tighter/` | PASS — no tiny hints; medium class unbound |
| `task-vacuous/` | `--check-body-hints` SKIP vacuous (no ask→spec) |

Honesty: `--check-scope-hints` may PASS on notes-park (Ask/goal/done-when/oos
clean) while `--check-body-hints` FAILS — distinct from SCOPE_HINT_BIND.
Iron: `BODY_HINT_BIND` (alongside `SCOPE_HINT_BIND` / `SPEC_HINT_BIND` / `ASK_HINT_BIND`).
G4 wires `_run_body_hints` after `_run_scope_hints`. v0.4.160.
