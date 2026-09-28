# Work Order — plans-header-no-tasks

- **Task:** demo missing Task N structure
- **Client quote:** "add task structure gate"
- **Origin:** assigned
- **Size:** standard

## Plan header (agentic handoff)

**Goal:** Prove Task-N validator rejects header-only work orders.

**Architecture:** Static markdown fixture for scripts/lib/work_order.py --check-tasks.

**Tech Stack:** Python 3, bash eval harness

**Spec:** evals/fixtures/plans-header/work-order-no-tasks.md

## Global Constraints

- none (checked)

## Review Focus

- missing Task N → validator must FAIL before BUILD

## Acceptance criteria (checkable)

1. work_order.py --check-tasks exits 1 on this file

## Out of scope

- version bump

## Approach

Demo only — header filled, Tasks section empty of Task N headings.

**Rejected alternative:** treat Expected: anywhere as enough

## Tasks (bite-sized, executable)

(no Task N headings — intentional soft gap fixture)
