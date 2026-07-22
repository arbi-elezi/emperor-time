# Quarantine — admitting untrusted output

**Contract:** raw agent output in, verified-and-admitted (or rejected)
contributions out. Nothing crosses from `.emperor/runs/` into the task's real
artifacts without an admission record. This aspect is where hallucination
containment across agents actually happens.

**The stance:** a worker's output is a *claim about work*, not work. Fluency,
confidence, and formatting are not evidence — models are at their most fluent
precisely when wrong, and a subordinate model performing success is the
adversarial case you built this pipeline for.

## The admission pipeline (by output type)

### Diffs / code changes

1. **Read the whole diff.** Every hunk. You are looking for: out-of-scope
   edits (SCOPE said `src/parser/` — why is `ci.yml` touched?), deletions the
   objective doesn't explain, injected commands/URLs/deps (supply-chain
   reflex: a new dependency is a *decision*, not a detail), commented-out
   tests, and quietly weakened assertions.
2. **Apply in a clean state** (stash/branch/copy) so reverting is one step.
3. **Run the real verification** — build, lint, the task's G2 test plan
   subset that covers the touched area. *Your* run, *your* output tail quoted
   into the admission record. The worker's claim "tests pass" is testimony;
   your terminal is evidence.
4. Admit hunk-set or reject: partial admission (keep the good hunks) is
   normal and recorded as such.

### Claims and reports ("done", "found the bug", "X is the cause")

Enter the task's Claim Ledger as **CONJECTURE** with the worker's quote
attached. Promote only through your own probe (the discriminating-probe
procedure in `chains/dowsing-chain/lie-detection.md` fits exactly). The
worker's own EPISTEMICS section (required by the dispatch prompt) tells you
where to probe first: its ASSUMED list is your checklist, and an empty
VERIFIED list is grounds for rejection without further reading.

### Critique findings (from hetero-critics)

Verified per `chains/judgment-chain/hetero-critique.md` — reproduce before
acting, credit on merge, keep refuted findings on record.

### Generated artifacts (docs, configs, schemas, test data)

Read fully (no skimming admission for prose), then verify by *use*: a config
is admitted by loading it, a schema by validating an instance, test data by
running the tests against it. Artifacts that can't be exercised get admitted
as **draft, labeled** — never as silently-final.

## The admission record (per contribution, in the ledger's provenance table)

```
| parser edge-case tests | codex | runs/<task>/codex/prompt.md | out.txt |
|   ADMITTED (partial: 3/4 hunks; rejected hunk: out-of-scope ci.yml edit)
|   verified: `npm test parser` exit 0, tail quoted; diff read in full |
```

Rejections keep the same shape with the reason — a rejected contribution that
vanishes without a record will be re-attempted by the next dispatch, at full
price (Vow 6).

## Containment failures (what to do when it's already inside)

Discovered post-merge that something unverified was admitted (a hunk you
didn't read, a claim promoted on testimony):

1. That's a **Vow 1/3 breach** — register it
   (`chains/judgment-chain/verdicts-and-breaches.md`, the Stake).
2. The provenance record bounds the blast radius — revert to the admission
   boundary, re-run admission properly.
3. If it shipped: Holy Chain (`chains/holy-chain/process-healing.md`) owns
   the recovery + disclosure.

## Calibration

Quarantine rigor scales with blast radius, not with suspicion of the agent:
a rename-only diff from the weakest local model gets the same *pipeline* as a
core-logic diff from the strongest cloud model — but the rename's "real
verification" is `grep` + build, minutes, while core logic gets the full test
plan. The pipeline is constant; the depth is right-sized.
