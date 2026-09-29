# steal-consent fixtures

Prove Steal consent-protocol HARD-GATE (`consent.py --reject-no-consent` /
`--check-consent`).

| Fixture | Expect |
|---|---|
| `consent-ok.md` | PASS — CONSENT + agent → role |
| `consent-header-only.md` | FAIL — header theater |
| `consent-missing.md` | FAIL — steal signal, no CONSENT |
| `consent-solo.md` | PASS vacuous / solo (no steal runs) |
| `task-ok/` | PASS — ledger CONSENT names codex + quarantine-ready |
| `task-no-consent/` | FAIL — runs present, no CONSENT |
| `task-header-only/` | FAIL — CONSENT header without assignment |
| `vacuous.md` / `task-vacuous/` | SKIP vacuous — no steal activity (honest N/A) |
