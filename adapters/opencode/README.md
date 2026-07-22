# Adapter — opencode

opencode (SST's open-source harness) takes Emperor Time two ways; use both.

## 1. Skills directory

Copy this repo's contents to `~/.opencode/skills/emperor-time/`
(`.\scripts\install.ps1 -Harness opencode`). opencode's skill format has its
own conventions (it documents Handlebars-templated skill files and
`opencode run --skill <name>`); its tolerance for plain SKILL.md folders vs.
its native format **must be verified at dowse time** — run
`opencode --help` and its docs, and if needed, Chain-Jail-adapt: flatten the
master SKILL.md into opencode's expected skill file shape (frontmatter kept,
Handlebars params only if you parameterize).

Invoke: `opencode run --skill emperor-time "<task>"` (verify flag spelling).

## 2. AGENTS.md pointer (always-on, canonical for opencode)

opencode treats `AGENTS.md` as canonical instructions (CLAUDE.md is fallback
only). Add to the target repo's `AGENTS.md`:

```markdown
## Emperor Time discipline

This repo runs under the Emperor Time protocol. Before any task, read
~/.opencode/skills/emperor-time/SKILL.md and follow it: six vows,
micro-waterfall G0–G5, claim ledger with prediction-before-test, mandatory
critique, consent-based agent enlistment. Ledgers go to .emperor/.
If the skill folder is missing, apply the embedded core rules from
~/.opencode/skills/emperor-time/adapters/generic/EMPEROR_TIME.core.md.
```

## opencode as an *enlisted worker*

```bash
opencode run "<scoped worker prompt>"
# long sessions / repeated dispatch:
opencode serve            # client starts it (occupies a terminal)
opencode run --attach http://localhost:4096 "<prompt>"
```

Prepend the Vow card (top of `adapters/generic/EMPEROR_TIME.core.md`) to
worker prompts — opencode workers won't have the skill loaded unless the
target machine installed it.

## Why opencode matters in the roster

It fronts many providers, including local models — which makes it the easiest
**different-vendor hetero-critic** to stand up when your orchestrator is
Claude or Kimi (uncorrelated errors; see Steal Chain routing hints).
