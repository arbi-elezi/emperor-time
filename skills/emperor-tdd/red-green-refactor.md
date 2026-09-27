# Red-Green-Refactor — TDD iron law HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md
- source-hash: sha256:64b03fce4aee5a97a93160cea8111f3ba13a17b7c001db4bd5836d67fd10705d
- heading: "The Iron Law" + "Red-Green-Refactor"
- license: MIT
- issue-context: emperor-tdd had doctrine but no enforceable red→green→refactor script path; Chain Jail extract-aspect names Iron Law / RGR only (not whole TDD skill, not writing-good-tests companion, not rationalization essays)

**Contract:** before any production code for a feature, bugfix, refactor, or behavior change, complete the RGR cycle. No production code without a failing probe first. Emperor Time stays the orchestrator via emperor-tdd + BUILD; do **not** announce or load whole `test-driven-development`.

Mechanical card: `scripts/emperor tdd` (Python: `scripts/lib/tdd.py`).

## HARD-GATE — The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING PROBE FIRST
```

Write production code before the probe failed? **Delete it.** Start over.

No exceptions:

- Don't keep it as "reference"
- Don't "adapt" it while writing probes
- Don't look at it
- Delete means delete

ET is stricter on one point: the prediction is written in the claim ledger
*before* the command runs, and the fail/pass tails are quoted.

Trivial doc/typo tasks: the probe may be `grep` / render, not a unit test.
The law still holds: observe absence, then change, then observe presence.

## Red-Green-Refactor steps

Complete each step before the next. Mechanical `--advance` rejects skips.
`--reject-prod` always fails (hard gate when jumping to production code).

### Step 1: RED — Write failing probe

Write one minimal probe (test or command) that must fail if the change is absent.
One behavior. Clear name. Real code (mocks only if unavoidable).

ET: ledger a HYPOTHESIS row with the predicted FAIL signal *before* the run.
Work-order Tasks already encode Expected: FAIL then Expected: PASS — follow that.

### Step 2: Verify RED — Watch it FAIL

**MANDATORY. Never skip.**

Run the probe. Confirm:

- It fails (not errors from typos / broken harness)
- Failure message matches the prediction
- Fails because the feature is missing

Probe passes? You're testing existing behavior — fix the probe, not the product.
Probe errors? Fix the error, re-run until it fails correctly. Quote the FAIL tail.

### Step 3: GREEN — Minimal production code

Smallest change that makes *that* probe pass. Nothing else.
No features, no sibling refactors, no "while I'm here".

### Step 4: Verify GREEN — Watch it PASS

**MANDATORY.**

Re-run the probe. Confirm PASS. Quote the PASS tail.
Then run the **project** suite (bare `pytest` / `npm test` / `cargo test` /
whatever the repo uses) — a green single probe is not a green suite.
Any failure that run shows goes in the report by name.

### Step 5: REFACTOR — Clean while green

After green only: remove duplication, improve names, extract helpers.
Keep probes green. Do not add behavior. Re-run after each cleanup.

Then: next failing probe for the next G1 criterion.

## Quick reference

| Step | Key | Success | ET hook |
|------|-----|---------|---------|
| 1. RED | One probe; predict FAIL | Probe written; ledger HYPOTHESIS | work-order Expected: FAIL |
| 2. Verify RED | Watch FAIL; quote tail | Fail proves absence | scientific-method claim |
| 3. GREEN | Smallest change only | Probe would pass | BUILD / G3 |
| 4. Verify GREEN | Watch PASS + project suite | Pass quoted; suite named | G3 / G4 evidence |
| 5. REFACTOR | Clean while green | No new behavior | stay on G3 |

## MUST

| Thought | Reality |
|---|---|
| "Too simple to probe" | Simple code breaks. Probe takes seconds. |
| "I'll test after" | After-probes pass immediately — prove nothing. Delete; start RED. |
| "Keep as reference" | You'll adapt it. That's testing after. Delete means delete. |
| "Skip verify-red, I know it fails" | Unwatched fail is CONJECTURE. Quote the tail. |
| "My probe is green; suite can wait" | Project suite is Step 4. Name every red. |
| "Load Superpowers TDD wholesale" | Forbidden — leaf only; ET + emperor-tdd orchestrate. |

## MUST-NOT

- Vendor whole `test-driven-development` (rationalization tables, writing-good-tests companion, debugging-integration essays) into always-on prompt.
- Write production code before Step 2 FAIL was observed and quoted.
- Announce a foreign master router.
- Call Step 4 done from a single-file green without the project suite.

## Related

- `skills/emperor-tdd/SKILL.md` — TDD entry; MUST open this leaf
- `scripts/lib/tdd.py` — mechanical checklist card
- `skills/emperor-build/SKILL.md` — BUILD wraps this cycle per task
- `references/scientific-method.md` — prediction before command
- `chains/chain-jail/extract-aspect.md` — "test-driven-development → Iron Law / RGR"
- `chains/chain-jail/navigation.md` — TDD gap → this leaf
