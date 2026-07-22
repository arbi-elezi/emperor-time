# Claim Ledger — <task-id>

Statuses: CONJECTURE → HYPOTHESIS → TESTED → **VERIFIED** | **REFUTED** | **UNVERIFIABLE**
(rules in `references/scientific-method.md` — prediction written before test; quote, don't paraphrase)

| # | Claim | Status | Prediction (written first) | Experiment / Sources | Evidence (quoted) | Date |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

## Worked example

| # | Claim | Status | Prediction (written first) | Experiment / Sources | Evidence (quoted) | Date |
|---|---|---|---|---|---|---|
| 1 | Retry bug is in `fetchWithRetry`, not callers | VERIFIED | Unit-probing it with a mock 503 will reproduce the infinite loop | `npx vitest run retry.probe.test.ts` | `"…retries: 8192, elapsed 30s (test timeout)"` | 2026-07-22 |
| 2 | `--max-retries` flag exists on the CLI | REFUTED | `--help` will list it | `tool --help` | `"Options: --retries <n> …"` (no `--max-retries`) | 2026-07-22 |
| 3 | Upstream fixed this in v3.2 | UNVERIFIABLE | — | changelog URL unreachable from this env | — labeled in delivery | 2026-07-22 |

Notes:
- Rows never get deleted — REFUTED rows prevent re-testing dead ends.
- A row an enlisted agent contributed starts at CONJECTURE no matter what it claimed.
- Every row must be terminal (VERIFIED/REFUTED/UNVERIFIABLE or explicitly-carried CONJECTURE) before G4 opens.
