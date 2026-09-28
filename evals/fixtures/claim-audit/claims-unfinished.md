# Claim Ledger — unfinished-reject

Statuses: CONJECTURE → HYPOTHESIS → TESTED → **VERIFIED** | **REFUTED** | **UNVERIFIABLE**

| # | Claim | Status | Prediction (written first) | Experiment / Sources | Evidence (quoted) | Date |
|---|---|---|---|---|---|---|
| 1 | retry bug is in fetchWithRetry | HYPOTHESIS | mock 503 loops forever | vitest retry.probe | — | 2026-09-28 |
| 2 | suite is green | TESTED | pytest exits 0 | `pytest -q` | partial | 2026-09-28 |

CLAIM AUDIT: 2 rows — 0 VERIFIED / 0 REFUTED / 0 CONJECTURE-labeled / 0 UNVERIFIABLE-labeled; spot-checks: none (rows unfinished)

Notes:
- HYPOTHESIS/TESTED left open — claim_audit.py must FAIL.
