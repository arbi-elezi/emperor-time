# Authoring checklist — skill Iron Law HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md
- source-hash: sha256:bbdfe742f853562e643a3d40d64476359d47881e39cef80a189283fa26d11ab9
- heading: "The Iron Law (Same as TDD)" (+ RED-GREEN-REFACTOR for Skills cycle only)
- license: MIT
- issue-context: authoring.md had doctrine (description-first, body procedure, trial) but no enforceable baseline-before-write script path; Chain Jail extract-aspect names Iron Law / skill RGR only (not whole writing-skills, not SDO essay, not whole writing-skills graphviz companion, not anthropic-best-practices dump; testing-skills-with-subagents is a sibling leaf (`testing-skills.md`); persuasion-principles is a sibling leaf (`persuasion-principles.md`))

**Contract:** before writing or editing a skill under Chain Jail authoring (or capture→author path), complete the skill RGR cycle. No skill body without a failing baseline first. Emperor Time stays the orchestrator via Chain Jail `authoring.md` + emperor-capture; do **not** announce or load whole `writing-skills`.

Mechanical card: `scripts/emperor author` (Python: `scripts/lib/author.py`).
Companion for pressure-testing skills: `chains/chain-jail/testing-skills.md` + `scripts/emperor skill-test`.
Companion for critical-practice wording: `chains/chain-jail/persuasion-principles.md` + `scripts/emperor persuasion`.

## HARD-GATE — The Iron Law

```
NO SKILL WITHOUT A FAILING BASELINE FIRST
```

Write the skill before watching a baseline fail? **Delete it.** Start over.
Edit a skill without a failing baseline for the change? Same violation.

No exceptions:

- Not for "simple additions"
- Not for "just adding a section"
- Not for "documentation updates"
- Don't keep untested drafts as "reference"
- Don't "adapt" while running the baseline
- Delete means delete

ET already owns description-first anatomy in `authoring.md` Steps 1–4 and
trial handoff in Step 5 / `trial-and-register.md`. This leaf only hard-gates
**baseline before write** — the TDD mapping Superpowers applies to skills.

## Authoring RGR steps

Complete each step before the next. Mechanical `--advance` rejects skips.
`--reject-untested` always fails (hard gate when jumping to skill prose).

### Step 1: RED — Design failing baseline

Write one pressure scenario (or structural probe) that must fail if the skill
is absent or the edit is wrong. Name the violation you expect.

ET: ledger a HYPOTHESIS row with the predicted FAIL signal *before* the run.
Subagents are preferred when available; a quoted local fixture / eval case is
enough when the NEED is structural (frontmatter, description trigger, gate).

### Step 2: Verify RED — Watch baseline FAIL

**MANDATORY. Never skip.**

Run the scenario **without** the new/edited skill (or with the old text).
Quote the FAIL / violation verbatim. Capture rationalizations the agent used.

ET: scientific-method claim row; quote the tail. If it unexpectedly passes,
the probe is wrong — fix the probe, not the skill draft.

### Step 3: GREEN — Minimal skill addressing those violations

Write (or edit) the smallest skill text that would make that baseline pass.
Follow `authoring.md` anatomy: description FIRST, procedure body, provenance.

ET: stage under `.emperor/captured-skills/<name>/` still in Zetsu — do not bind.

### Step 4: Verify GREEN — Watch it PASS

**MANDATORY. Never skip.**

Re-run the same scenario with the skill present. Quote compliance. One green
pressure case ≠ ready to register — still hand to `trial-and-register.md`.

### Step 5: REFACTOR — Close loopholes while green

Plug new rationalizations found under pressure. Re-run. No new capabilities
sneaked in. Then hand to trial (`authoring.md` Step 5).

## Quick reference

| Step | Key | Success | ET hook |
|------|-----|---------|---------|
| 1. RED baseline | Pressure scenario / probe | Predicted FAIL ledgered | claim HYPOTHESIS |
| 2. Verify RED | Run without skill; quote | FAIL / violation quoted | Vow of Evidence |
| 3. GREEN skill | Minimal text for those fails | Draft staged (Zetsu) | authoring.md 1–4 |
| 4. Verify GREEN | Re-run with skill | Compliance quoted | pre-trial |
| 5. REFACTOR | Close loopholes; re-run | Still green; no riders | trial-and-register |

## MUST

- Complete Steps 1–2 before any skill body write or substantive edit.
- Delete skill prose written before a quoted baseline FAIL.
- Keep ET + Chain Jail as orchestrator; do not load whole `writing-skills`.
- After Step 5, still run pin + consent + trial before the skill may fire.

## MUST-NOT

- Skip verify-red ("I know it would fail").
- Summarize a whole foreign skill into the description (authoring.md already
  forbids always/never routers; SDO details stay in Superpowers).
- Bind or marketplace-ship before trial-and-register.
- Call this leaf a substitute for `emperor tdd` on product code — different gate.

## Mechanical flags

```
scripts/emperor author                  # print AUTHOR / STEP / MUST card
scripts/emperor author --step N         # focus one step
scripts/emperor author --advance N N+1  # reject skips
scripts/emperor author --reject-untested  # HARD-GATE exit 1
```
