# Adaptation — conforming a captured skill

**Contract:** transform the captured artifact into a skill that (a) runs on
the target harness and (b) operates inside Emperor Time's workflow. Every
material change is listed in the provenance header. Output: the adapted skill
folder, ready for trial (never for direct use).

## Step 1 — Frontmatter conversion

Portable core: `name` + `description`. Everything else is dialect.

| From \ To | Claude Code / Kimi (Agent Skills) | opencode | Codex | Plain prompt |
|---|---|---|---|---|
| Agent Skills SKILL.md | keep as-is | flatten to its skill-file shape; convert params to Handlebars only if parameterized | keep folder; verify activation at dowse | strip frontmatter → title + body |
| opencode skill | lift prompt into SKILL.md body; params become "inputs" section in prose | keep | as Agent Skills | strip |
| Copilot/other agent files | extract instructions → SKILL.md body; drop platform blocks | flatten | as Agent Skills | strip |
| Plain prompt/gist | wrap: write `name` + trigger-bearing `description`, body = prompt | wrap per its shape | wrap | keep |

Rules:
- `name` = folder name, kebab-case, collision-checked against the absence
  sweep's dir listing.
- `description` rewritten to **router grammar**: what it does + when to
  trigger, with the trigger phrases the client would actually say. The
  description is the routing surface — a captured skill with a vague
  description will never fire.
- Harness-specific fields (`allowed-tools`, flow definitions, Handlebars
  params) that the target can't read: translate if meaningful, else delete —
  never leave fields the target will misparse. Kimi flow skills (`/flow:`)
  moving to a non-Kimi harness: linearize the flow into numbered steps in the
  body.

## Step 2 — Tool-verb translation

The captured body says "use tool X" — the target harness may not have X.

| Abstract action | Claude Code | Kimi | Generic instruction fallback |
|---|---|---|---|
| read file | Read | its file-read tool | "open and read <path>" |
| edit/write | Edit / Write | its editor tools | "modify <path> so that…" |
| run command | Bash / PowerShell | its shell tool | "run: `<cmd>` and capture output" |
| search code | Grep / Glob | its search | "search the tree for <pattern>" |
| fetch web | WebFetch / WebSearch | its web tool (if any) | "fetch <url>" or degrade per no-web rule |

When the target's tool names are unknown, translate to the generic fallback —
plain imperatives survive every harness. Never leave a foreign tool name in an
instruction; the target model will either error or hallucinate a tool.

## Step 3 — Path and workflow conformance

- Repoint hardcoded paths to the target's conventions; artifacts the skill
  produces land in `.emperor/` (harness-neutral) unless the skill's own
  ecosystem dictates otherwise.
- Wire into the micro-waterfall: the skill acts **inside a phase**; strip any
  instruction that would bypass gates ("just commit when done" → "hand back
  for G4/G5"). A captured skill never gets more authority than the chain-user
  running it.
- Its factual assertions inherit claim discipline: commands it teaches are
  tripwires to verify at trial, not truths to trust because they're written
  down.

## Step 4 — The provenance header (mandatory, first thing in the body)

```markdown
> **Captured by Chain Jail** on 2026-07-22
> Source: <URL> (license: MIT) — retrieved <date>
> Adapted for: <harness> — changes:
>   - frontmatter: description rewritten for routing; allowed-tools dropped
>   - tools: `apply_patch` → Edit
>   - paths: output moved to .emperor/captured-skills/…
>   - removed: telemetry curl call (unreviewable endpoint)
```

Every *material* change gets a line. "Removed" lines matter most — they are
the audit trail proving the suspicious parts were seen and handled.

## Step 5 — Hand to trial

Adaptation never ends in use. It ends in `trial-and-register.md`, with the
adapted folder staged in `.emperor/captured-skills/<name>/`.
