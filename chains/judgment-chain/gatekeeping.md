# Gatekeeping — opening gates on evidence

**Contract:** for the gate in question, walk its checklist below; every item
is answered by pointing at evidence (a ledger section, a quoted output, a
file). Output: one gate line in the ledger — `G<n> OPENED <date>` with the
pointers, or `G<n> BLOCKED: <missing>`.

A gate check takes minutes. If it's taking longer, the phase isn't done —
that's the gate working, not the gate failing.

## G0 — Dowse (task defined)

- [ ] The task is stated in one sentence a stranger could act on.
- [ ] Origin recorded: assigned (client's words **quoted**, not paraphrased —
      paraphrase is where scope drift is born) or dowsed (evidence cited).
- [ ] If dowsed: the client picked it, or standing auto-pick authority is on
      record in the ledger.
- [ ] Ledger file exists at `.emperor/tasks/<task-id>/ledger.md`.

## G1 — Require (done is defined)

- [ ] Every acceptance criterion is **checkable**: a probe could pass/fail it.
      Test each by asking "what command or observation settles this?" — no
      answer, no criterion.
- [ ] Out-of-scope list exists and names the nearest tempting expansions.
- [ ] Every known unknown is either resolved or sits in the Claim Ledger as a
      labeled assumption.
- [ ] Nothing in the criteria contradicts the client's quoted words (re-read
      them now — G0's quote exists precisely for this check).

## G2 — Design (how, and how we'll know)

- [ ] Approach written; **one rejected alternative** named with the reason
      (its absence means alternatives were never weighed).
- [ ] Impact map: files/systems touched; rollback story if state is involved.
- [ ] **Test plan maps every G1 criterion to a probe.** Walk the criteria list
      one by one — an unmapped criterion sends the phase back to G1.
- [ ] Missing capabilities identified → Chain Jail engaged or consciously
      deferred (recorded).
- [ ] Planned dispatches (if any) listed with their consent status.

## G3 — Build (change complete per design)

- [ ] The change exists and builds/lints cleanly (output tail quoted).
- [ ] Diff walked against the design: divergences either absent, or recorded
      and the design delta re-judged.
- [ ] Tripwires observed: flags/APIs/paths used in the change were verified,
      and the ledger's tripwire line says which.
- [ ] Mid-build discoveries went to the dowsing pool — the diff contains no
      unrequested riders (walk the diff specifically for this).
- [ ] Enlisted-agent contributions passed quarantine before merging.

## G4 — Verify (the Trial)

This gate is a sequence, not a checklist — run the aspects in order:

1. Test plan executed, outputs quoted (`claim-audit.md` checks coverage).
2. Claim Ledger swept to terminal states → `claim-audit.md`.
3. Self-critique completed → `self-critique.md`.
4. Hetero-critique run or unavailability recorded → `hetero-critique.md`.
5. Ruling issued → `verdicts-and-breaches.md`.

G4 opens only on PASS or PASS-WITH-CONDITIONS.

## G5 — Deliver (task closes)

- [ ] Shipped the way this project ships (house rules followed; commits only
      if the client's workflow says so).
- [ ] Commit messages carry no agent attribution trailers (`Co-Authored-By`,
      `Generated-with`, …) — the history is the client's; provenance belongs
      in the ledger. (Exception only if the client asked for the trailer.)
- [ ] The report leads with the outcome and uses calibrated language mapped
      from claim statuses (the table in `references/scientific-method.md`).
- [ ] Conditions from the verdict appear in the report — not just the ledger.
- [ ] Provenance included if agents were enlisted.
- [ ] Lifespan Ledger closed; empty "bought" cells got register lines.
- [ ] Breach Register state (even "empty") reflected honestly in the ledger.

## Right-sizing at the gate

A trivial task may satisfy an entire gate in one ledger sentence — the checks
above still each get a yes, they just point at less. The gate never shrinks to
zero items; the *evidence* shrinks to one line. (Worked example: the fast-path
in `references/micro-waterfall.md`.)
