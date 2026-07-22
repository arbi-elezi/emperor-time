# Verdicts and Breaches — rulings, re-entry, the Stake

**Contract:** convert an audited, critiqued body of work into exactly one
ruling; run FAIL re-entries correctly; process vow breaches through the Stake
of Retribution. Output: the verdict line in the ledger (and register entries
where earned).

## The ruling

Issued only after: claim audit done, self-critique done, hetero-critique done
or its absence recorded. Three verdicts exist; pick the worst one the evidence
supports (optimistic rounding at the verdict is how everything upstream gets
retroactively wasted):

### PASS
No blockers, no unresolved should-fixes. The gate opens; G5 may proceed.

### PASS-WITH-CONDITIONS
No blockers; should-fixes remain that are (a) contained and (b) not worth
blocking delivery for. Each condition is **named in the delivery report
itself** — a condition the client never sees is a silent defect with
paperwork. Conditions become dowsing-pool candidates with the critique as
their evidence. Conditions are not a dumping ground: a "condition" that would
mislead the client if unfixed is a blocker being euphemized.

### FAIL → phase N
A blocker exists. Determine N — **the earliest phase whose output the blocker
invalidates**:

| Blocker reveals… | Re-enter at |
|---|---|
| The requirement itself was wrong/missing | G1 — Require |
| Approach/test plan can't satisfy a criterion | G2 — Design |
| Implementation diverges from sound design | G3 — Build |
| Evidence gaps only (work may be fine, proof isn't) | G4 — re-verify properly |

Re-entry mechanics: phases from N forward **re-run and re-gate**; later-phase
artifacts survive only if re-judged against the new upstream output ("the
design changed but the diff happens to still fit" is a claim — test it, don't
assume it). No patching forward past a failed gate: fixing the symptom at G4
when the wound is at G2 leaves the design lying about the code. The ledger
records the re-entry: `VERDICT: FAIL → G2 (<blocker>) | re-entered <date>`.

## The Stake of Retribution — processing a vow breach

A breach is a violation of the Six Vows (master SKILL.md): unverified claim
shipped as fact, skipped/out-of-order gate, unconsented enlistment or
credential touch, missing ledger/critique, waste (unchanged retry, padding).

The procedure — four lines, then move:

1. **Record** in the Breach Register (append-only; never edited down):
   `| Vow | what happened | discovered | remediation | lesson |`.
2. **Remediate**: re-enter at the earliest gate the breach invalidated (table
   above applies — a breach is a blocker whose author was the process).
3. **Disclose if delivered**: the client hears it from you, immediately, in
   plain terms: *"I reported X as verified; it was not. Actual state: <what is
   known, with evidence>. Re-verifying now."* A silent post-hoc fix of a
   delivered falsehood is a second breach, graver than the first — it
   converts an error into a cover-up.
4. **Learn**: the lesson line names the cheapest check that would have caught
   it earlier. Recurring lessons (2+ appearances across ledgers) become
   candidate amendments to the relevant chain aspect — the system's own
   evolution path; propose the amendment to the client as a task candidate.

Calibration: the Stake is aimed at the work, not at theater. No
self-flagellation essays, no confidence-performance in either direction. One
register line, one remediation, one disclosure if owed, one lesson. Then move.

## Verdict hygiene

- One ruling per trial; "PASS, mostly" is not a verdict.
- The verdict cites its inputs: `(claim audit: <line>; critique: <file>;
  hetero: <file|absent>)` — a verdict that can't cite its trial record is
  itself unverified.
- Verdicts are claims: a later-discovered wrong PASS is processed as a breach
  (Vow 1 — the evidence didn't support the ruling), not as bad luck.
