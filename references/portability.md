# Portability

Emperor Time's canonical form is the open **Agent Skills** layout — a folder
with `SKILL.md` (YAML frontmatter: `name`, `description`) plus supporting files
loaded on demand. That format is the lingua franca: Claude Code and Kimi CLI
read it natively (from the *same directories*), Codex reads `~/.codex/skills/`,
opencode has its own skills dir, and everything else can swallow the distilled
prompt form.

## Deployment matrix

| Harness | Where to put it | How it activates |
|---|---|---|
| **Claude Code** | `~/.claude/skills/emperor-time/` (user) or `<repo>/.claude/skills/emperor-time/` (project) | Auto-triggers on the description; or the client mentions "emperor time" |
| **Kimi CLI** | Same directories as Claude Code — reads `~/.claude/skills/` and `.claude/skills/` natively; vendor-neutral: `~/.config/agents/skills/` | `/skill:emperor-time` in-session |
| **Codex CLI** | `~/.codex/skills/emperor-time/` | Per Codex's skill activation (verify at dowse) |
| **Copilot CLI** | Supports skills — location per current docs (verify at dowse) | Per its skill mechanism |
| **opencode** | `~/.opencode/skills/` + an `AGENTS.md` pointer in the repo | `opencode run --skill ...` / AGENTS.md always-on |
| **Ollama / local** | Bake `adapters/generic/EMPEROR_TIME.core.md` into a Modelfile `SYSTEM` | Always-on persona — see `adapters/ollama/` |
| **Any open-weight runner** (llama.cpp, LM Studio, vLLM, …) | Paste `adapters/generic/EMPEROR_TIME.core.md` as the system prompt | Always-on |

`scripts/install.ps1` / `install.sh` automate the top rows.

## The distillation ladder

Context is the scarcest resource on small models. Ship the largest rung the
model can carry *while still leaving room for the actual work*:

1. **Full skill** (~this whole folder, loaded progressively) — frontier
   models in skill-native harnesses. SKILL.md stays lean; chains/references
   load only when engaged.
2. **Core** (`adapters/generic/EMPEROR_TIME.core.md`, ~2.5k tokens) — the six
   vows, the loop with gates, claim states, critique checklist, consent rules,
   delivery contract. For capable open-weight models (≳14B class) as a system
   prompt.
3. **Vow card** (the minimal rung, embedded at the top of Core, ~300 tokens) —
   for small workers that only execute scoped prompts under an external
   orchestrator. They don't run the waterfall; they obey the vows that survive
   miniaturization: *quote evidence, label conjecture, don't retry unchanged,
   report what you verified vs. assumed.*

When distilling further yourself, cut in this order: lore → examples →
templates (orchestrator holds them) → routing tables (orchestrator's job) →
chains other than Judgment. **The last thing standing is always the claim
discipline.** An agent with nothing but "label what you didn't verify" is
still safer than a bare model.

## The compatibility trial

Before running Emperor Time on an unfamiliar harness/model, probe six
capabilities and configure honestly (each probe is an experiment — prediction,
run, observe):

| Probe | If absent → degrade to |
|---|---|
| Read files? | Client pastes content; label all file claims UNVERIFIABLE-here |
| Execute commands? | No experiments possible → static evidence only; most claims cap at TESTED-by-inspection; say so in every delivery |
| Web access? | Chain Jail hunts locally only; external facts rely on client-fetched sources; two-source rule suspended and **replaced by mandatory labeling** |
| Spawn/reach other agents? | Steal Chain dormant; hetero-critique degrades to self-critique (noted in ledger) |
| Ask the user mid-task? | Autonomous mode: defensible defaults + assumption ledger + flagged in delivery |
| Persistent files for ledgers? | Ledger lives in the conversation itself — compressed table forms of the templates |

A harness that fails a probe doesn't disqualify Emperor Time; **pretending the
probe passed does.** The degraded mode goes in the ledger and the delivery
report.

## Conformance checklist (porting to a new format)

Adapting Emperor Time *itself* somewhere new (this is Chain Jail applied
reflexively):

- [ ] `name` + `description` survive in whatever metadata the target supports
      (the description carries the triggers — never drop it).
- [ ] Tool references translated (Read/Write/run/search → target's verbs) or
      abstracted to plain instructions.
- [ ] Paths translated (`~/.claude/...` → target's convention; `.emperor/`
      stays — it's harness-neutral).
- [ ] The Six Vows intact, verbatim or tightened — never loosened.
- [ ] Gates G0–G5 intact (right-size the artifacts, never the gate count).
- [ ] Trial run on a toy task before first real use; result recorded.
- [ ] Provenance header added (adapted-from this repo, date, changes).
