# ask-spec-harness-plan-emit fixtures

Prove `ask_spec.py --emit --write` chains idempotent `harness-plan.md` (+ json)
emit from stamped `effort_class` — one mechanical path (no second
`harness-plan --emit` CLI recall before G0 `--require-plan`).

| Fixture | Expect |
|---|---|
| `ask-tiny.txt` | `--write` → ask-spec.md + harness-plan.md/json; effort_class=tiny; FORCE_TABLE Caps/Forbidden present; `--require-plan` PASS |
| `ask-small.txt` | `--write` → small class plan with work-order/tdd tools |
| re-write same path | idempotent overwrite; still PASS `--require-plan` |
| `--emit` without `--write` | stdout only — no harness-plan.md on disk |

Iron: standing `*-hint-bind` leaf chain is ENOUGH (no new HINT_BIND / CAPS_BIND /
peer-echo binders). Soft→hard via this HARD-GATE. v0.4.172.
