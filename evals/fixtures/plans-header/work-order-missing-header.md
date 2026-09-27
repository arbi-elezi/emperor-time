# Work Order — plans-header-gap

- **Task:** demo missing plan header
- **Client quote:** "add plans header"
- **Origin:** assigned
- **Size:** standard

## Contract (interfaces between tasks)

- **Inputs on disk:** none
- **Outputs on disk:** none
- **Forbidden:** credentials

## Acceptance criteria (checkable)

1. gate rejects this file

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
