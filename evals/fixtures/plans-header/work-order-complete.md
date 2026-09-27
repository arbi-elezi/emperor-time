# Work Order — plans-header-ok

- **Task:** demo complete plan header
- **Client quote:** "add plans header"
- **Origin:** assigned
- **Size:** standard

## Plan header (agentic handoff)

**Goal:** Prove plan-header validator accepts a filled header.

**Architecture:** Static markdown fixture exercised by scripts/lib/work_order.py in eval.sh.

**Tech Stack:** Python 3, bash eval harness

**Spec:** evals/fixtures/plans-header/work-order-complete.md

## Global Constraints

- none (checked)

## Review Focus

- empty Goal line → validator must FAIL before BUILD

## Contract (interfaces between tasks)

- **Inputs on disk:** fixtures only
- **Outputs on disk:** none
- **Forbidden:** credentials

## Acceptance criteria (checkable)

1. work_order.py exits 0 on this file

## Out of scope

- version bump

## Approach

Demo only.

**Rejected alternative:** skip header

## Tasks (bite-sized, executable)

### Task 1 — demo

**Files:**
- Modify: `templates/work-order.md`

**Step 1 — write the probe that must fail**

```bash
true
```

Expected: FAIL
Quoted signal: `missing`

**Step 2 — smallest change that makes the probe pass**

```bash
true
```

Expected: PASS
Quoted signal: `ok`

**Commit:** `test: demo`
