# Absence Check — confirm it is truly missing

**Contract:** prove local absence before hunting. Output: a short checked-list
in the ledger ("looked in X, Y, Z; found nothing / found near-miss N") — it is
the license for every later Chain Jail step.

## Step 1 — Name the capability precisely

One sentence, verb-first: "convert OpenAPI specs to typed clients",
"review SQL migrations for lock hazards". Too broad ("do databases") can never
be checked for absence; narrow until a skill either does it or doesn't. Write
the sentence in the ledger — it is also the future skill's description seed.

## Step 2 — Sweep local skill locations

Check what exists on this machine and project (list what you actually
checked — paths differ per harness; skip-and-declare the ones that don't
apply):

```
Project (from repo root):
  .claude/skills/   .agents/skills/   .kimi/skills/   .codex/skills/
  .emperor/captured-skills/
User:
  ~/.claude/skills/          ~/.config/agents/skills/   ~/.agents/skills/
  ~/.kimi/skills/            ~/.codex/skills/           ~/.opencode/skills/
```

Concrete sweep (POSIX / adapt for PowerShell):

```bash
for d in .claude/skills .agents/skills ~/.claude/skills ~/.config/agents/skills \
         ~/.agents/skills ~/.kimi/skills ~/.codex/skills ~/.opencode/skills; do
  [ -d "$d" ] && grep -il -r --include=SKILL.md "<capability keywords>" "$d"
done
```

Then read the `description:` frontmatter of every hit — descriptions are the
routing surface, so absence is judged against descriptions first, bodies
second.

## Step 3 — Sweep harness built-ins

The harness itself may already expose the capability: its skill listing, its
built-in tools, its slash commands. Check the listing the harness shows you;
don't assume from memory which builtins exist (tripwire).

## Step 4 — Judge near-misses honestly

| Finding | Ruling |
|---|---|
| Exact match | Use it. Chain disengages. |
| Does 80%+, gap is additive | **Extend it** (a small edit to an existing skill outranks a capture — record the extension as the task's change) |
| Same domain, different job | Not a match — but note it in the hunt brief; its structure may inform adaptation |
| Matches but broken/stale | Fixing it IS the capture — enter `adaptation.md` with the local skill as the candidate |

The temptation to call a near-miss "not quite right" and hunt for something
shinier is NIH wearing a scarlet cloak. The Limitation exists for exactly this
judgment: extend beats capture beats author.

## Step 5 — Record and proceed

Ledger entry (three lines suffice):

```
ABSENCE CHECK: "<capability sentence>"
Checked: <dirs + harness listing>  |  Hits: <none | near-miss list with rulings>
Verdict: MISSING → hunt.md  |  EXTEND <path>  |  EXISTS <path> (chain disengages)
```
