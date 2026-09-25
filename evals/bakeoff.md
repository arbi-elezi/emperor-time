# Bake-off — 2026-09-25

Three closed tasks on this repo. One agent. Not three isolated vendor sessions
(that would be a different experiment). Lenses: Emperor Time (executed),
Superpowers process-from-public-names (not executed as a plugin),
naked (what we would have shipped without a rite).

## Tasks (G1)

1. Steal router selection table names `ci-mode.md` and `swarm-emulate.md`.
2. SessionStart hook treats `emperor.cmd` as a peer, not “No cmd.exe shim”.
3. `scripts/eval.sh` fails if (1) or (2) regress.

Out of scope: spawning Claude with the Superpowers plugin; Windows live pwsh.

## ET path (executed)

probe: grep -q ci-mode.md chains/steal-chain/SKILL.md && grep -q swarm-emulate.md chains/steal-chain/SKILL.md && echo STEAL_ROWS_OK
expect: STEAL_ROWS_OK

probe: grep -q emperor.cmd hooks/hooks.json && echo HOOK_PEER_OK
expect: HOOK_PEER_OK

probe: bash scripts/eval.sh
expect: EVALS PASSED

Babysitting: one standing order (“do it”). No mid-flight questions.

## Superpowers lens (not executed — CONJECTURE)

Would announce using-superpowers → writing-plans → TDD on eval.sh first.
Would likely fix the same holes. Would not add claim-ledger states.
Would ask design questions before the three-line patch (Socratic cost).
Activation advantage: marketplace hook would have fired without this chat.

## Naked lens (not executed — CONJECTURE)

Would patch the router and stop. Would not grow eval.sh. Hook wording would
stay stale. Regression next week.

## Verdict

ET wins this slice on *mechanical lock-in* (eval now owns the rows).
Superpowers still wins *activation* (we had to be told “do it”).
Naked loses on (3).
This is not a substitute for three isolated vendor sessions on a third repo.
