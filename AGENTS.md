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

## Consent

No other CLI, no login, no public PR without explicit client yes.
