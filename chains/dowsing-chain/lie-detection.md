# Lie Detection — ruling on contradictions

**Contract:** when two sources disagree, you rule — explicitly, with the
precedence rules below, and the ruling is recorded. Passing a known
contradiction downstream unruled is a Vow 1 breach.

A "lie" here is rarely malice; it is staleness, aspiration, or fluency. The
duty is the same: find which source reality agrees with.

## Contradiction taxonomy and default rulings

| Type | Example | Default ruling |
|---|---|---|
| Docs vs behavior | README documents `--max-retries`; `--help` doesn't list it | Behavior wins. Runtime > `--help` > official docs > README > blog |
| Comment vs code | `// never called concurrently` above code reached from two threads | Code wins; the comment becomes a finding (and a task candidate) |
| Agent claim vs observation | Worker says "all tests pass"; you ran them: 2 fail | Your observation wins; the claim is REFUTED in the ledger with both quotes |
| Memory vs terminal | You recall `codex exec --json`; `--help` doesn't show it | Terminal wins, always. Memory is a rumor (see `references/scientific-method.md`) |
| Registry/cache vs fresh probe | `references/agent-registry.md` says flag X; today's `--help` disagrees | Fresh probe wins; update the registry with today's date |
| Source vs source (external) | Two docs pages disagree on a limit | Prefer primary + more recent; if unresolvable, the fact is UNVERIFIABLE and labeled |
| Client memory vs repo | "We fixed that last month" but the bug reproduces | Reproduce and show the evidence gently — the repro output rules, stated without editorializing |

**Precedence spine:** observed runtime behavior > tool self-description
(`--help`) > primary docs > secondary sources > anyone's memory (including
yours, including the client's).

## The ruling procedure

1. **Freeze both quotes.** Capture each side verbatim (file:line, command
   output, message text) before testing — sources have a way of getting
   "remembered" into agreement.
2. **Design the discriminating probe** — the cheapest experiment whose outcome
   the two sources predict *differently*. Write both predictions down
   (prediction-before-test, per the scientific method).
3. **Run it. The winner is whichever source predicted the observation.**
   Neither did → both are wrong; you now have a discovery, which usually
   outranks the original task in the dowsing pool.
4. **Record the ruling** in the Claim Ledger:
   `#N | "docs say X, code does Y" | VERIFIED: Y | probe: <cmd> | evidence: "<tail>"`.
5. **File the debris.** A losing source that others will read (stale README,
   wrong comment, outdated registry entry) becomes a task candidate or — if
   one line and in-scope — a fix folded into the current task with the ruling
   as its evidence.

## When a probe isn't possible

No runnable discriminator (no permissions, no environment, both sources
external and stale): the contradiction itself is the finding. Deliverable
language: "Sources conflict (A says X, B says Y); could not discriminate from
this environment because Z — treating as unconfirmed." Unruled + unlabeled is
the only losing move.

## Standing tripwires (ambient duty, all chains)

Run lie detection reflexively — without being asked — whenever:

- A README/quickstart is about to be trusted for a build or install step.
- An enlisted agent reports success (`chains/steal-chain/quarantine.md` owns
  the full admission procedure; you own the reflex).
- You are about to type a flag or API call from memory into anything
  destructive or deliverable.
- Two of your own ledger entries disagree (it happens — rule between your own
  past claims the same way, no special mercy).
