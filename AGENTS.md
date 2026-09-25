# Emperor Time — standing orders for any coding agent

You are making **software**, not writing code. A loose task plus this repo is
enough. Do not ask for a framework tour.

## Loop

intake → queue.next (if no task) → G0/G1 → design-on-disk → TDD build →
verify + `scripts/emperor done` → forge PR (consent) → queue.next → rest

Read `SKILL.md` only as the router. Then open **one** file.

## Disk is memory

- `.emperor/state.md` — resume here
- `.emperor/tasks/<id>/PLAN.md` `FINDINGS.md` `PROGRESS.md` `DONE.md` `ledger.md`
- `.emperor/queue.md` — local backlog if no GitHub/Linear

Do not restate a session that these files already hold.

## Mechanical locks

```
scripts/emperor done <task-dir>     # must exit 0 before "done"
scripts/emperor gate g4 <task-dir>  # unquoted VERIFIED cannot pass
scripts/emperor queue next          # pick work
scripts/emperor forge <task-dir>    # PR; refuses without consent
```

Windows: `pwsh -File scripts/emperor.ps1 <tool> ...`
cmd: `scripts\emperor.cmd <tool> ...`
zsh: `scripts/emperor.zsh <tool> ...`

## Consent

No other CLI, no login, no public PR, no Linear/GitHub write without an
explicit client yes recorded in the ledger. Tokens never land in git.

## PR quality (minimize review comments)

- One intent per PR.
- Tests that fail if the change is reverted.
- No comments that narrate what the code already says.
- No drive-by refactors, no formatting-only noise, no AI trailer.
- PR body = G1 + quoted probe tails + out-of-scope.

## Chains

Capability missing → Chain Jail (steal one heading, pin+trial).
Other agents → Steal Chain (quarantine).
Red build → Holy Chain.
Find work → Dowsing + `queue next`.
