# ask-spec-proportionality fixtures

Prove ask→spec + proportionality HARD-GATEs (`ask_spec.py --reject-no-spec` /
`--check-ask-spec`; `proportionality.py --reject-over-verify` /
`--check-proportionality`).

| Fixture | Expect |
|---|---|
| `spec-ok-tiny.md` | PASS — full ask→spec, effort_class=tiny |
| `spec-missing.md` | FAIL — ask-spec signal, missing fields |
| `ask-tiny.txt` | emit → effort_class=tiny |
| `task-ok/` | PASS — ask-spec + under-cap cycles |
| `task-no-spec/` | FAIL — ask-spec claimed, fields missing |
| `task-over-verify/` | FAIL — tiny class, cycles over cap |
| `task-under-cap/` | PASS — tiny class, cycles under cap |
| `task-vacuous/` | PASS vacuous — ordinary ledger, no ask-spec activity |

Honesty: idle Steal/Jail/Holy vacuous PASS is separate; these fixtures cover task-path thrash only.
