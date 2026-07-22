# Process Healing — when the loop itself is the wound

**Contract:** repair breakage in the *discipline*: skipped gates, bad
admissions, delivered falsehoods, derailed waterfalls. Output: the breach
processed (register + remediation + disclosure where owed) and the loop
re-entered at the earliest sound gate. Code damage left behind routes back
into the code-healing sequence.

Process wounds outrank code wounds: a broken test fails loudly; a broken
process fails silently and *compounds* — every step taken past a skipped gate
is built on an unopened gate's missing evidence.

## Wound catalog and procedures

### A gate was skipped (discovered mid-task)

1. Declare it — register entry via the Stake
   (`chains/judgment-chain/verdicts-and-breaches.md`), no narrative padding.
2. Find the earliest gate whose exit criteria are **not actually satisfied**
   (walk `chains/judgment-chain/gatekeeping.md` backward from where you are;
   check criteria against evidence, not against memory of having done them).
3. Re-enter there. Work above the unopened gate is **re-judged, not
   grandfathered**: it may all survive — but it survives by passing the gate
   now, not by already existing.

### The waterfall derailed (phases interleaved, scope slid, ledger went stale)

Symptoms: building during design, requirements "remembered" differently than
G0's quote, ledger last touched two phases ago. Procedure: freeze (no new
work), reconstruct the ledger from artifacts that exist (diffs, outputs,
messages — evidence, not recollection), then the skipped-gate procedure from
whatever the reconstruction shows as the earliest unsound gate. The
reconstruction gap itself is the register entry (Vow 3).

### A bad admission (enlisted-agent work merged unverified)

1. Register entry (the quarantine that was rushed or skipped).
2. Bound the damage by provenance: `.emperor/runs/<task>/<agent>/` +
   admission records mark the boundary; revert to it.
3. Re-run admission properly (`chains/steal-chain/quarantine.md`) on the
   reverted contribution — it may be fine; *unverified* was the wound, not
   necessarily *wrong*.
4. Code damage discovered while reverting → triage sequence, but the
   bisection is pre-scoped: bisect over admission boundaries first.
5. Roster note on the agent only if the *content* was bad; the process note
   ("rushed admission under time pressure") is about you, and goes in the
   postmortem's would-have-caught-sooner field.

### A delivered falsehood (breach discovered after G5)

The gravest, and the one with a non-negotiable clock:

1. **Disclose first, fix second.** The client hears it from you before you
   start repairing — plain terms, no cushioning: *"I reported X as verified.
   It was not. What is actually known: <evidence>. What I'm doing: <plan>."*
   Fixing quietly first and disclosing a pre-solved problem is the cover-up
   shape (register-worthy on its own) even when the fix is perfect.
2. Register entry with the delivery's claim quoted next to reality.
3. Re-enter at the gate that should have stopped it (usually G4; sometimes
   G1 if the falsehood was a requirement misread).
4. Re-deliver with the corrected report — calibrated language, the breach
   visible in the ledger the client can read.

### Systemic drift (the same breach keeps recurring)

Three appearances of the same lesson line across ledgers = the rule is losing
to some pressure. Diagnose the pressure (time? phrasing? a gate item that's
easy to "yes" without evidence?), then propose the structural fix as a task
candidate: amend the aspect file, add the gate item, automate the check. The
skill amending itself through evidence is the intended endgame — Chain Jail
binding a lesson captured from your own history.

## Re-entry mechanics (shared by all wounds)

- Re-entry is forward-moving: gates from the re-entry point re-run in order;
  no gate re-opens "just to check" gates that were sound.
- The ledger shows the seam: `RE-ENTERED G2 <date> (breach #3)` — a reader
  must be able to see where the first pass ended and the healed pass began.
- Lifespan honesty: the re-run's cost lands in the Lifespan Ledger like any
  other spend; process wounds are expensive, and hiding their cost would
  falsify the one record that motivates preventing them.

## What process healing is not

- Not punishment theater — the register line is one line; the work is the
  apology.
- Not an amnesty mechanism — "declare it and keep the output anyway,
  unjudged" is the skipped gate wearing a confession as a costume.
- Not rare, ideally — a register with occasional small entries and fast
  remediations is the healthy signature; an always-empty register on complex
  work is more likely unexamined than immaculate.
