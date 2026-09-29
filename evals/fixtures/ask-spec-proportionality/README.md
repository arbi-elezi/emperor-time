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
| `task-no-class/` | bump stamps tiny — critique/finish/grill not unbounded |
| `task-no-class-over/` | FAIL — cycle ledger without class still hits tiny cap |

Honesty: idle Steal/Jail/Holy vacuous PASS is separate; these fixtures cover task-path thrash only.
v0.4.145: missing effort_class on critique/finish/grill / cycle ledger defaults to tiny hard caps (`MISSING_CLASS_DEFAULTS_TINY` / `bump_and_check`).
