# Work Order — plans-header-thin-task

- **Task:** demo thin Task N skeleton
- **Client quote:** "add task structure gate"
- **Origin:** assigned
- **Size:** standard

## Plan header (agentic handoff)

**Goal:** Prove Task-N validator rejects skeleton Task headings.

**Architecture:** Static markdown fixture for scripts/lib/work_order.py Task-N lock.

**Tech Stack:** Python 3, bash eval harness

**Spec:** evals/fixtures/plans-header/work-order-thin-task.md

## Global Constraints

- none (checked)

## Review Focus

- Task heading without Files/Expected/Commit → FAIL

## Contract (interfaces between tasks)

- **Inputs on disk:** TBD
- **Outputs on disk:** TBD
- **Forbidden:** none

## Acceptance criteria (checkable)

1. work_order.py exits 1 on this file

## Out of scope

- version bump

## Approach

Demo only.

**Rejected alternative:** accept vibe Task headings

## Tasks (bite-sized, executable)

### Task 1 — <name>

Implement the feature.
