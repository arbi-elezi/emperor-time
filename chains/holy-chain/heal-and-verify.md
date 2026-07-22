# Heal and Verify — the minimal cure, proven

**Contract:** cause in, verified heal out. The change is the smallest that
addresses the root cause; the proof covers cure, no-new-wounds, and
mechanism; the postmortem line closes it. Output: the heal + its evidence
block + the postmortem line.

## Step 1 — Choose the heal honestly

Two legitimate shapes — the crime is mislabeling one as the other:

- **Root-cause heal**: removes the mechanism identified by bisection. The
  default; what "fixed" means without qualifiers.
- **Labeled symptom-patch**: suppresses the failure without removing the
  mechanism (timeout widened, retry added, feature flagged off). Legitimate
  as an *emergency call* — when shipped-severity demands relief before the
  root heal is safe to make. Requirements: the label ("mitigation, root
  cause still live"), the root cause filed as a task candidate with the
  combat ledger as evidence, and the client told which one they got. An
  unlabeled symptom-patch is a delayed lie: it converts today's visible
  failure into next month's mystery.

## Step 2 — Keep it minimal

The heal touches what the mechanism requires — nothing else:

- **No riders.** The refactor you noticed mid-bisection, the rename that
  would make this "cleaner", the adjacent bug you spotted: dowsing pool, own
  task, own waterfall. A heal-plus-improvements diff makes the verification
  claim ("this fixed it") unfalsifiable — which change did what?
- Smallest ≠ hackiest: minimal means minimal *scope*, not minimal thought.
  If the root-cause heal is properly a 40-line change, 40 lines it is; what
  it may not be is 40 lines plus 200 of opportunity.

## Step 3 — The verification triad

All three, quoted into the ledger; the heal is unverified until each holds:

1. **Cure**: the triage-captured reproduction now passes — same invocation,
   same environment, output quoted. (The *original* repro, not a friendlier
   variant written today. Fingerprint match matters: the failure you fixed
   must be the failure you had.)
2. **No new wounds**: the surrounding suite/build passes at the pre-breakage
   scope — the G2 test plan subset for the touched area at minimum, the full
   suite when blast radius earned it at triage. A heal that trades one red
   for a different red is a relocation, not a restoration.
3. **Mechanism**: the root-cause claim reaches VERIFIED in the Claim Ledger —
   you can state *why* it broke and why this change removes that why, with
   the bisection evidence behind it. For symptom-patches, this row instead
   reads honestly: `mechanism suppressed, not removed — see candidate <id>`.

Then unwind triage's scaffolding deliberately: drop the stash / merge the
rescue branch / delete the `.holy-` copy — *after* the triad, never before
(the snapshot is the undo for a failed heal attempt; discarding it early
re-gambles).

## Step 4 — The postmortem line

One structured line, appended to the task ledger:

```
BROKE: <what> | CAUSE: <verified mechanism> | HEAL: <change, root|mitigation>
| CAUGHT-BY: <signal that surfaced it> | WOULD-HAVE-CAUGHT-SOONER: <cheapest check>
```

The last field is the only forward-looking one and the whole point:

- Names something cheap (a test, a lint rule, a gate item, a probe timeout) →
  creating it becomes a dowsing-pool candidate *now*, evidence attached.
- Names a process rule → candidate amendment to the relevant chain aspect,
  proposed to the client (the system evolves through exactly this path).
- Honestly nothing? Rare. Write `nothing cheap — <one-line why>` rather than
  inventing a plausible-sounding guard that wouldn't actually have fired
  (postmortem theater fails the same honesty bar as everything else).

Recurring `CAUGHT-BY: client` or `CAUGHT-BY: luck` across ledgers is itself
a finding about the verification culture — surface it.
