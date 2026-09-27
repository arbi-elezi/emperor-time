# Emperor Time — standing orders for any coding agent

You are making **software**, not writing code. A loose task plus this repo is
enough. Do not ask the client their OS, shell, or language.

## Defaults (already ran)

Session start runs `scripts/boot.sh` (or `boot.ps1`) with no user output.
Read the files it left:

- `.emperor/host.env` — os, shell, wsl, encoding
- `.emperor/survey.md` — artifact classes (Pascal, asm, …)
- `.emperor/eval.log` — structural eval when this tree *is* Emperor Time

Do not tell the client to run `identify` or `eval`. Those are internals.
For a foreign/lost tree the agent may run `scripts/emperor identify <path>`.

## MUST-route (standing order)

Before creative work, clarifying questions, or exploring the tree, open one
governing file from the `SKILL.md` tables, or run
`scripts/emperor route "<utterance>"` / `scripts/emperor activate` and open
`ACTIVATION next=`. Silent boot alone is not enough. Emperor Time stays the
orchestrator (leaf aspects only; no foreign master router).

## Loop

intake → queue.next (if no task) → G0/G1 → design-on-disk → TDD build →
verify + `scripts/emperor done` → forge PR (consent) → queue.next → rest

Read `SKILL.md` only as the router. Then open **one** file.

## Mechanical locks

```
scripts/emperor done <task-dir>
scripts/emperor gate g4 <task-dir>
scripts/emperor queue next
scripts/emperor forge <task-dir>
```

## Route (trigger to skill)

When the utterance is ambiguous (or at session start), run
`scripts/emperor route "<utterance>"` (Python core: `scripts/lib/route.py`).
It prints one skill/chain path and a short reason from `evals/triggers.json`
(no embeddings). Example: `scripts/emperor route "lost pascal tree"` prints
`skills/emperor-excavate/SKILL.md`. Exit 1 means no match; fall back to the
phase table in `SKILL.md`. Language-agnostic: pas/asm/cobol/rom/lost/vintage
map to excavate.

## Consent

No other CLI, no login, no public PR without explicit client yes.
