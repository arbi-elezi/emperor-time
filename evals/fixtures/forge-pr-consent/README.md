# forge-pr-consent fixtures

Prove forge PR-consent HARD-GATE (`forge.py --reject-no-pr-consent` /
`--check-pr-consent`). Steal enlistment (`consent.py --reject-no-consent`)
is a different gate.

| Fixture | Expect |
|---|---|
| `forge-ok.md` | PASS — forge signal + PR consent quote |
| `forge-no-consent.md` | FAIL — forge/PR claimed, missing consent |
| `forge-vacuous.md` | PASS vacuous — no forge/PR signal |
| `task-ok/` | PASS — ledger forge + consent / env |
| `task-no-consent/` | FAIL — opening a PR, no consent |
| `task-vacuous/` | PASS vacuous — merge-locally only |
