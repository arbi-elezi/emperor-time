---
name: chain-jail
description: >-
  Emperor Time's middle-finger chain — skill capture and binding. Router for
  five aspects: absence check (is it truly missing?), hunt (find the closest
  skill on the net), adaptation (conform a captured skill to this harness and
  workflow), authoring (write one from scratch), and trial-and-register (test
  in quarantine, then install with provenance). Use when a task needs a
  capability the harness lacks, or the user asks to find/adapt/make a skill.
  Load one aspect file at a time per the Invocation Ritual.
metadata:
  version: 0.2.0
  part-of: emperor-time
  kind: router
---

# Chain Jail — router

> *The chain that binds. Its Limitation is what makes it unbreakable: only
> legitimate targets — and the captured stay in Zetsu until judged.*

Chain Jail acquires abilities the harness lacks. Its power comes from its
restriction.

## The Limitation (chain-wide law)

1. **Only the genuinely missing.** Capturing what already exists locally
   (duplicating, re-downloading, NIH-rewriting) is misuse of the chain and a
   vow breach — which is why every capture starts at the absence check.
2. **Zetsu until judged.** Nothing captured or authored acts on real work
   before passing its trial.
3. **Provenance always.** Every bound skill carries where it came from, its
   license, and what was changed.

## Selection table — read exactly one

Aspects run in order for a full capture; enter mid-sequence when the earlier
steps are already satisfied (and say so in the ledger).

| Your situation | Aspect file |
|---|---|
| A capability seems missing — confirm before anything else | `absence-check.md` |
| Confirmed missing — search the net for the closest existing skill | `hunt.md` |
| A candidate is captured — conform it to this harness and workflow | `adaptation.md` |
| Nothing suitable exists — write the skill from scratch | `authoring.md` |
| Adapted/authored skill ready — trial it, then install with provenance | `trial-and-register.md` |

Special case — the missing skill is needed by an **enlisted agent**, not you:
same sequence, but adapt to *that* harness's format (`adaptation.md` has the
per-harness matrix), install into its directory, have that agent run the
trial, and judge its output yourself.

## Exit conditions

- Absence check finds a local skill → use/extend it; chain disengages.
- Hunt finds nothing worth adapting → skip to `authoring.md`.
- Trial fails twice after re-adaptation → release the capture (rejection is
  recorded with reasons; the need returns to the task as an open constraint).
