# Claim Audit — the G4 scientific-method sweep

**Contract:** walk the task's Claim Ledger row by row; every row terminates,
every VERIFIED survives a spot-check, cross-agent claims get no courtesy.
Output: the audit line in the ledger (`CLAIM AUDIT: n rows — v VERIFIED /
r REFUTED / c CONJECTURE-labeled / u UNVERIFIABLE-labeled; spot-checks: …`).

## Step 1 — Completeness: are all the claims even IN the ledger?

The ledger is audited against the *work*, not just against itself. Scan the
deliverable-to-be (diff, report draft, design notes) for assertions that never
became rows:

- Words that smuggle claims: "obviously", "always", "never", "should work",
  "the standard way", "as documented".
- Every external fact in the report draft (version numbers, API behavior,
  tool capabilities) — row or label, no third option.
- Every enlisted-agent statement that influenced a decision.

Found unrowed claims → add them as CONJECTURE now, then continue the audit.

## Step 2 — Termination: no unfinished states

| Row status | Ruling |
|---|---|
| VERIFIED / REFUTED | terminal ✓ |
| UNVERIFIABLE | terminal ✓ *if* the delivery draft carries its label |
| CONJECTURE | allowed to survive only as an explicitly labeled assumption that the deliverable repeats |
| HYPOTHESIS / TESTED | **unfinished** — the experiment exists but wasn't run, or ran without sufficient evidence. Finish it or demote honestly to UNVERIFIABLE with the reason |

## Step 3 — Spot-check VERIFIED rows (the audit's teeth)

For each VERIFIED row — all of them on normal tasks, a sample on huge ones
(sampling declared in the audit line):

1. **Prediction check** — was the prediction written before the run? A row
   whose prediction column was back-filled to match the observation is TESTED
   at best; re-mark it (and register the Vow 1 near-miss if it was about to
   ship as VERIFIED).
2. **Evidence-actually-supports check** — re-read the quoted evidence cold and
   ask: does this output prove *this claim*, or does it merely sit near it?
   The classic failure: suite output proves "tests pass", the row claims "the
   new path works" — but no test exercises the new path. Near-evidence
   demotes the row.
3. **Freshness check** — was the evidence produced *after* the last change to
   what it verifies? Evidence from before the final edit verifies the
   penultimate version. Stale → re-run the probe.
4. **Two-source check** (external facts) — two *independent* sources, not one
   page and its quotation. Same-origin pairs collapse to one source; the row
   demotes unless an experiment covered it.

## Step 4 — Cross-agent claims

Any row sourced from another model (worker, critic, prior session) with
status above CONJECTURE must cite **your** verification, not theirs.
"kimi-worker reported X and its log says so" is CONJECTURE with a quote, not
TESTED — logs presented by the claimant are testimony, not evidence. Promote
only through your own re-run/probe.

## Step 5 — REFUTED rows are checked too (cheaply)

- Still present? (Deleting refuted rows re-opens dead ends — restore any that
  vanished; that deletion is itself register-worthy.)
- Did anything downstream keep relying on the refuted belief? Search the
  design/diff for its fingerprints — a refuted assumption with living
  descendants is an unfixed bug wearing a "handled" tag.

## Step 6 — Write the audit line and hand off

Sequence position: the audit runs **before** self-critique (the prosecutor
argues from an audited ledger — count 8, "honesty of the report", depends on
these statuses being real). Hand to `self-critique.md`.
