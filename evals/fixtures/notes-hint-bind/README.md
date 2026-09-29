# notes-hint-bind fixtures

Prove ask→spec notes.md hint HARD-GATE
(`ask_spec.py --reject-over-notes-class` / `--check-notes-hints`).

TASK_HINT_BIND binds ask-spec + ledger / work-order / brief / claims.
Notes-hint bind closes the remaining bypass: park tiny-hint language
("fix typo" / "one-line" / wording / trivial / nit / changelog only) in
notes.md while ask-spec+ledger stay clean so FORCE_TABLE[large] /
EFFORT_CAPS[large] unlock while TASK_HINT_BIND stays green. Harness owns
force — agent does not inflate class by editing notes.md.

Length-only infer stays advisory. Only strong `_TINY_HINTS` bind.
`_LARGE_HINTS` lift the ceiling. Tighter-than-hint class remains OK.
Rejected: binding noisy `_SMALL_HINTS` (HARD-GATE/fixture/patch).

| Fixture | Expect |
|---|---|
| `task-notes-park/` | FAIL — notes.md tiny hints, ask-spec+ledger clean, effort_class:large |
| `task-clean/` | PASS — tiny-hint notes corpus + effort_class:tiny |
| `task-tighter/` | PASS — no tiny hints; medium class unbound |
| `task-vacuous/` | `--check-notes-hints` SKIP vacuous (no ask→spec) |

Honesty: `--check-task-hints` may PASS on notes-park (task corpus clean)
while `--check-notes-hints` FAILS — distinct from TASK_HINT_BIND.
Iron: `NOTES_HINT_BIND` (alongside `TASK_HINT_BIND` / `BODY_HINT_BIND` /
`SCOPE_HINT_BIND` / `SPEC_HINT_BIND` / `ASK_HINT_BIND`).
G4 wires `_run_notes_hints` after `_run_task_hints`. v0.4.162.
