# Authoring — writing a skill from scratch

**Contract:** when the hunt returns nothing adaptable, write the skill. The
bar is higher than adapting: you are creating the thing future absence-checks
will find, so its routing surface and its honesty determine whether it ever
helps anyone. Output: a skill folder staged for trial.

## The anatomy (what every authored skill contains)

```
<skill-name>/
├── SKILL.md            # frontmatter + lean body (the only mandatory file)
└── references/         # depth, loaded on demand (only if the body would exceed ~150 lines without it)
    └── <topic>.md
```

## Step 1 — Write the description FIRST

The description is the router. Write it before the body, in this grammar:

> *What it does* (verb-first, concrete) + *when to use it* (the situations and
> literal phrases that should trigger it).

Test: read your description as if you were the harness holding 40 skills.
Would it fire on the client's phrasing from the task that spawned this? Would
it *not* fire on neighboring capabilities that other skills own? A
description that fires always or never is the most common authored-skill
defect. (Second most common: describing the implementation instead of the
capability.)

## Step 2 — Write the body as procedure, not essay

- **Contract line first**: inputs → outputs → failure behavior, one line each.
- Numbered steps with concrete commands/forms — the reader executes; prose
  that cannot be executed is decoration (Vow 6 applies to authored skills too).
- State the failure modes: what to do when a step can't run, what degrades to
  what. A skill that only describes the happy path teaches its user to
  improvise exactly where improvisation is most dangerous.
- Tripwire honesty: any flag, API, or path you write from memory gets marked
  `(verify at first use)` unless you verified it *while authoring* — you are
  writing tomorrow's registry; don't seed it with rumors.
- Length: body ≤ ~150 lines. Overflow goes to `references/<topic>.md`, loaded
  from the body by explicit pointer ("for X, read references/topic.md") — the
  same selection ritual this repo uses.

## Step 3 — The self-containment check

Each file must be independently loadable:

- The body must not require reading any reference to execute its main path.
- Each reference must open with enough context to be read alone (one contract
  line — a reference that begins mid-thought forces bulk loading, defeating
  selection).

## Step 4 — Emperor Time conformance

Authored under this system, the skill must:

- Operate inside a phase; never instruct gate-bypassing.
- Produce evidence-shaped output (quoted results, not "done").
- Carry a provenance header even though it's original:

```markdown
> **Authored by Chain Jail** on 2026-07-22
> Reason: hunt returned no adaptable candidate (ledger: <task-id>)
> Informed by: <ideas-only sources, if any — credited even when unlicensed to copy>
```

## Step 5 — Hand to trial

Authored skills take the same trial as captured ones — being homemade earns no
trust (arguably less: nothing has ever executed these words before). Stage in
`.emperor/captured-skills/<name>/` → `trial-and-register.md`.

## Authoring anti-patterns

- **The manifesto** — pages of philosophy, no executable steps. (Flavor is
  allowed exactly one line per section; this repo pushes the limit and knows it.)
- **The mirror** — restating what the harness already does natively, wrapped
  in a new name (absence check exists to prevent this; respect its verdict).
- **The kitchen sink** — one skill, four capabilities. Split; each gets its
  own description, or none will ever route cleanly.
- **The oracle** — instructions that assert world-facts ("API X returns Y")
  instead of teaching the probe that would verify them at use-time.
