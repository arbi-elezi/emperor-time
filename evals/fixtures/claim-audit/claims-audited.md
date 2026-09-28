# Claim Ledger — audited-accept

Statuses: CONJECTURE → HYPOTHESIS → TESTED → **VERIFIED** | **REFUTED** | **UNVERIFIABLE**

| # | Claim | Status | Prediction (written first) | Experiment / Sources | Evidence (quoted) | Date |
|---|---|---|---|---|---|---|
| 1 | claim_audit rejects missing audit | VERIFIED | `--check-audit` exits 1 | `python3 scripts/lib/claim_audit.py --check-audit evals/fixtures/claim-audit/claims-no-audit.md` | `"claim_audit FAIL: missing CLAIM AUDIT line"` | 2026-09-28 |
| 2 | --max-retries flag exists | REFUTED | `--help` lists it | `tool --help` | `"Options: --retries <n>"` | 2026-09-28 |
| 3 | upstream fixed in v9 | UNVERIFIABLE | — | changelog unreachable | — labeled in delivery | 2026-09-28 |
| 4 | worker log is testimony | CONJECTURE (carried) | — | enlisted agent quote | labeled assumption | 2026-09-28 |

CLAIM AUDIT: 4 rows — 1 VERIFIED / 1 REFUTED / 1 CONJECTURE-labeled / 1 UNVERIFIABLE-labeled; spot-checks: row 1 prediction-before-run + quoted evidence ok

Notes:
- All rows terminal or explicitly carried — claim_audit.py must PASS.
