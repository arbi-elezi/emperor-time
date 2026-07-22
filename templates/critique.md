# Critique — <task-id>

- **Role:** self-prosecution | hetero-critique by <agent>
- **Subject:** <diff/artifact under trial>
- **Date:** <date>

## The eight counts

For each: what was actually checked (commands run, paths read), findings, severity.
"No findings" without naming what was checked is not a pass — it's an unexamined count.

| # | Count | Checked (evidence of examination) | Findings | Severity |
|---|---|---|---|---|
| 1 | Requirements coverage (all of G1, nothing beyond scope) | | | |
| 2 | Correctness at the edges (empty/huge/unicode/concurrent/error paths) | | | |
| 3 | Hidden assumptions (environment preconditions — checked or ledgered?) | | | |
| 4 | Evidence quality (do tests exercise the change, or run near it?) | | | |
| 5 | Regression surface (what else touches this path; re-verified?) | | | |
| 6 | Security & safety (injection, secrets, unguarded destructive ops) | | | |
| 7 | Simpler alternative (could half the diff do the job?) | | | |
| 8 | Honesty of the report (does the summary claim more than the ledger proves?) | | | |

Severity: **blocker** (FAIL the gate) · **should-fix** (conditions on PASS) · **note** (dowsing pool)

## Findings disposition

| Finding | Severity | Disposition (fixed / condition / pooled / refuted-with-evidence) |
|---|---|---|

## Verdict

**PASS** | **PASS-WITH-CONDITIONS:** <list> | **FAIL → phase <N>:** <why>

*Hetero-critique reminder: a critic's findings arrive as CONJECTURE — verify
before acting, refute with evidence where wrong, and record the critic's
identity in the provenance table.*
