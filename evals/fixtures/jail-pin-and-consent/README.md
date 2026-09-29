# jail-pin-and-consent fixtures

Prove Jail pin-and-consent HARD-GATE (`pin_consent.py --reject-unpinned` /
`--reject-no-skill-consent` / `--check-pin-consent`).

| Fixture | Expect |
|---|---|
| `pin-ok.md` | PASS — full pin + JAIL-CONSENT |
| `pin-unpinned.md` | FAIL — jail signal, missing source-url/hash |
| `pin-no-consent.md` | FAIL — pin present, missing named-skill consent |
| `pin-incomplete.md` | FAIL — URL+hash only, no captured-at/license/adapter |
| `pin-vacuous.md` | PASS vacuous — no Jail pin signal |
| `task-ok/` | PASS — captured-skill + ledger pin + consent |
| `task-unpinned/` | FAIL — adaptation claimed, no pin |
| `task-no-consent/` | FAIL — pin ok, no JAIL-CONSENT |
| `task-incomplete-pin/` | FAIL — URL+hash theater, no peers |
| `task-vacuous/` | PASS vacuous — ordinary ledger |
