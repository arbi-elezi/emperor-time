# Work Order — sdd-lifecycle-alpha

- **Task:** SDD lifecycle fixture plan A
- **Client quote:** "ship plan-scoped briefs"
- **Origin:** assigned
- **Size:** standard

## Plan header (agentic handoff)

**Goal:** Fixture plan for emperor SDD task-brief / task-start / task-done evals.

**Architecture:** Static markdown with two bite-sized tasks under Tasks section.

**Tech Stack:** Python 3, bash eval harness

**Spec:** evals/fixtures/sdd-lifecycle/alpha/work-order.md

## Global Constraints

- none (checked)

## Review Focus

- missing Task N → task-brief must exit ≠0

## Acceptance criteria (checkable)

1. task-brief extracts Task 1 non-empty
2. task-start prints brief: and base:
3. task-done refuses empty BASE..HEAD

## Out of scope

- archaeology

## Approach

Eval fixture only.

**Rejected alternative:** vendor whole Superpowers prompts

## Tasks (bite-sized, executable)

### Task 1 — write greeting probe

**Files:**
- Create: `hello.txt`

**Step 1 — write the probe that must fail**

```bash
test -f hello.txt
```

Expected: FAIL
Quoted signal: `missing`

**Step 2 — smallest change that makes the probe pass**

```bash
echo ok > hello.txt
```

Expected: PASS
Quoted signal: `ok`

**Commit:** `test: sdd task 1`

### Task 2 — append second line

**Files:**
- Modify: `hello.txt`

**Step 1 — failing probe**

```bash
grep -qx second hello.txt
```

Expected: FAIL

**Step 2 — pass**

```bash
echo second >> hello.txt
```

Expected: PASS

**Commit:** `test: sdd task 2`
