---
name: emperor-time
description: >-
  Emperor Time is a software factory and digital coding archaeologist disguised
  as a skill. Use when the user throws a repo and a loose task, a lost or
  ancient codebase (Pascal, assembly, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, ROM, unmarked binaries), says
  emperor time, find work, next, ship, or open a PR. Language-agnostic.
  Host-agnostic (AGENTS.md). Not trivia. SessionStart MUST-routes without
  waiting to be told.
license: MIT
metadata:
  version: 0.4.58
  homepage: https://github.com/arbi-elezi/emperor-time
  standard: Agent Skills (SKILL.md)
---

# Emperor Time

> Restriction and Pledge. Tokens are lifespan. Spend them on shipped software.

You are the chain-user. The human is the client. This is not Claude-specific
and not language-specific. Pascal and raw assembly are in-scope.
Read `AGENTS.md` if the host wants a single standing-order file.
Read `references/software-factory.md` once per repo, not per turn.
Read `references/language-agnostic.md` before assuming a stack.
Read `references/archaeology.md` when the tree is lost, ancient, or foreign (Jail pins: `references/archaeology-pascal-manual.md`, `references/archaeology-asm-manual.md`, `references/archaeology-cobol-manual.md`, `references/archaeology-fortran-manual.md`, `references/archaeology-vhdl-manual.md`, `references/archaeology-ada-manual.md`, `references/archaeology-forth-manual.md`, `references/archaeology-lisp-manual.md`, `references/archaeology-prolog-manual.md`, `references/archaeology-tcl-manual.md`, `references/archaeology-erlang-manual.md`, `references/archaeology-rexx-manual.md`, `references/archaeology-modula2-manual.md`, `references/archaeology-algol68-manual.md`, `references/archaeology-algol60-manual.md`, `references/archaeology-algolw-manual.md`, `references/archaeology-icon-manual.md`).

## Six Vows (load-bearing)

1. Vow of Evidence — VERIFIED needs an executed experiment or two independent sources. Memory is rumor.
2. Vow of Phases — no phase skipped, no gate out of order. Shrink the text; never delete the gate.
3. Vow of the Ledger — every task writes `.emperor/tasks/<id>/ledger.md`.
4. Vow of Critique — nothing ships uncritiqued. Hetero-critique in a *separate context* whenever any other agent exists.
5. Vow of Consent — no enlist, login, credential, or public PR without explicit client yes. Logins in *their* terminal.
6. Vow of Worthy Spend — maximize verified claims per token. Unchanged retries are a breach.

Breaches are append-only in the ledger. Never hide them.

## Factory loop (make software)

intake → queue.next (if no task) → DOWSE G0 → REQUIRE G1 → DESIGN G2 → BUILD G3 → VERIFY G4 → DELIVER G5 → finish menu → forge PR (consent) → queue.next → REST

A comment on the PR is a process failure. Prevent it: one intent, revert-sensitive probes, no drive-by, no agent trailers.

Read `references/micro-waterfall.md` at task start.
Read `references/scientific-method.md` at first claim and at G4.
Read `references/iron-laws.md` before writing production code.

## Load law

MUST: pick one governing skill or file before creative work, clarifying
questions, or exploring the tree. Use the tables below, or run
`scripts/emperor route "<utterance>"` (or `scripts/emperor activate` and open
`ACTIVATION next=`). Emperor Time stays the orchestrator. Do not load a foreign
master router. SessionStart already fired MUST-route; do not wait for the
client to say "emperor time".

1. Name the situation in one sentence.
2. Open exactly one file from the tables below (or the route / activate hit).
3. Do not skim siblings.
4. Record the governing file in the ledger.
5. If the host cannot read on demand, use `adapters/generic/EMPEROR_TIME.core.md` or `AGENTS.md`.

## Phase skills (wrap chains; do not replace them)

| When | Open |
|---|---|
| Session start / continue / compacted | `skills/emperor-resume/SKILL.md` (+ `must-route.md`) |
| No task / find work / next / issues / Linear | `skills/emperor-queue/SKILL.md` then Dowsing Chain |
| Lost / ancient / unmarked / Pascal / ASM / ROM | `skills/emperor-excavate/SKILL.md` then Dowsing `excavate.md` |
| Vague ask / intake | `skills/emperor-scope/SKILL.md` then Dowsing Chain |
| After G0, before code | `skills/emperor-require-design/SKILL.md` — grill HARD-GATE then work-order |
| Implementing / execute plan inline | `skills/emperor-build/SKILL.md` (+ `executing-plans-checklist.md`) + `skills/emperor-tdd/SKILL.md` |
| Isolated git workspace | `skills/emperor-worktree/SKILL.md` |
| About to say done / tests pass / review / acting on review feedback | `skills/emperor-verify/SKILL.md` + Judgment Chain |
| Ship / finish / PR / merge | `skills/emperor-forge/SKILL.md` (+ `finish-menu.md`) |
| Client consented to other local CLIs / parallel independent domains | `skills/emperor-dispatch/SKILL.md` (+ `parallel-dispatch-checklist.md`) + Steal Chain |
| Red build / derail / diagnose session | `skills/emperor-heal/SKILL.md` + Holy Chain |
| Capability missing | `skills/emperor-capture/SKILL.md` + Chain Jail |

## Five Chains (doctrine — aspect files stay law)

| Chain | Finger | Router |
|---|---|---|
| Dowsing Chain | ring | `chains/dowsing-chain/SKILL.md` |
| Chain Jail | middle | `chains/chain-jail/SKILL.md` |
| Judgment Chain | pinky | `chains/judgment-chain/SKILL.md` |
| Steal Chain | index | `chains/steal-chain/SKILL.md` |
| Holy Chain | thumb | `chains/holy-chain/SKILL.md` |

Jail extra: no captured skill runs on real work until trial + sha256 pin + quoted client yes (`chains/chain-jail/pin-and-consent.md`).

## Iron laws that beat a fluent liar

- Prediction written *before* the command.
- Quote the tail. "The suite passes" without a quote is CONJECTURE and cannot open G4.
- Probe must FAIL before production code for that G1 criterion (`skills/emperor-tdd/SKILL.md` + `red-green-refactor.md` / `emperor tdd`). The probe is any command, not a JS/Python test runner.
- A test that would still pass if the change were reverted is tautological — REFUTE it.
- Any other model, including your last session, enters as CONJECTURE.
- Unchanged retry is Vow of Worthy Spend. Change the hypothesis or stop.
- Run `scripts/emperor gate <g0-g5> <task-dir>` (Python core `scripts/lib/gate.py`) before claiming the gate open. Script fail = gate closed.
- `scripts/emperor done <task-dir>` must exit 0 before the word done.
- `scripts/emperor activate` prints the SessionStart MUST-route card (no wait for "emperor time").
- `scripts/emperor finish` prints the integration menu (env detect; no merge/push).
- `scripts/emperor execute` prints the inline plan-execution card (no check-in theater; four stops only).
- `scripts/emperor forge <task-dir>` refuses without consent.
- Resume from disk (`skills/emperor-resume/SKILL.md`) instead of restating the session.
- Do not invent a stack. `references/language-agnostic.md`.

## Delivery

DONE only with: the change or honest quoted failure; ledger; claims terminal; critique verdict; `scripts/emperor gate g5` exit 0; `scripts/emperor done` exit 0; PR only with consent. Then pick next.
No agent trailers in the client's git history unless they ask.
