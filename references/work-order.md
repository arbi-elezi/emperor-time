# Work Order law (G2 handoff)

Load this file when DESIGN opens and the task is not a one-line typo.

## Why this exists

The Task Ledger is an **audit log**. It cannot be the worker interface.
A worker (you in an hour, a Steal Chain agent, a later session) has zero
context and questionable taste. The work order is the closed unit they
execute.

## Law

1. Non-trivial tasks **must** write `.emperor/tasks/<id>/work-order.md`
   from `templates/work-order.md` before BUILD.
2. Every task step names real paths, real commands, and the **expected
   fail/pass string**. "Add tests" is not a step.
3. Write the failing probe *in the work order* before the implementation
   sketch.
4. Interface contracts between Task N and Task N+1 are written in the
   Contract section. No TBD.
5. Planned dispatches attach to a work-order task, not to a vibe.
6. Right-size by shrinking text, not by deleting sections.


## Plan header (Superpowers leaf)

Non-trivial work orders **must** include the Plan Document Header fields
adapted from obra/superpowers `skills/writing-plans` (MIT), heading
"Plan Document Header" only — not the whole skill:

- `**Goal:**` / `**Architecture:**` / `**Tech Stack:**` / `**Spec:**`
- `## Global Constraints`
- `## Review Focus` (five uncovered failure modes, or `none (checked)`)

`scripts/lib/work_order.py` enforces this at G2. Empty Review Focus without
an explicit `none (checked)` fails the gate.

## Gate hook

`scripts/gate.sh g2` (Python `scripts/lib/gate.py`) fails if:

- the work order is missing on size=standard|heavy
- any task step lacks an `Expected:` line
- acceptance criteria is empty
- plan header fields missing / Review Focus empty without `none (checked)` (`scripts/lib/work_order.py`)

## Relation to chains

- Dowsing Chain fills Origin + Client quote.
- Steal Chain workers get this file + named paths only.
- Judgment Chain examiners get this file's criteria + the review pack,
  not the author's diary.
