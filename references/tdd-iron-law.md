# TDD iron law — full form

See `skills/emperor-tdd/SKILL.md` and the HARD-GATE leaf
`skills/emperor-tdd/red-green-refactor.md`. Load the skill (or run
`scripts/emperor tdd`) at build time — not this pointer alone.
This page exists so `eval.sh` and the master skill can name the law without
loading the phase skill twice.

Law: no production code without a failing probe first.
Prediction in the ledger before the command.
Delete implementation written before the fail was observed.
Mechanical card: `scripts/lib/tdd.py` via `scripts/emperor tdd`.

Test quality companion: `skills/emperor-tdd/writing-good-tests.md` + `scripts/emperor good-tests` (Name the Break / Exercise the Real Thing).
