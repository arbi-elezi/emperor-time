# Adapter — Kimi CLI (native, shared install)

Kimi CLI supports the open Agent Skills format and — verified against its docs
2026-07-22 — searches these skill directories:

- user, brand group: `~/.kimi/skills/`, **`~/.claude/skills/`**, `~/.codex/skills/`
- user, generic group: `~/.config/agents/skills/` (Kimi's recommended neutral path), `~/.agents/skills/`
- project (relative to nearest `.git`): `.kimi/skills/`, **`.claude/skills/`**, `.codex/skills/`, `.agents/skills/`

**Consequence: the Claude Code install already covers Kimi CLI.** One folder,
two harnesses, zero conversion. If you want Kimi-first or vendor-neutral
placement instead:

```powershell
.\scripts\install.ps1 -Harness kimi            # → ~/.kimi/skills/emperor-time/
.\scripts\install.ps1 -Harness generic-agents  # → ~/.config/agents/skills/emperor-time/
```

(`merge_all_available_skills` defaults to true, so multiple locations merge —
avoid installing to several at once or you'll shadow yourself on upgrades.)

## Setup (client's terminal — Vow of Consent)

```powershell
# Windows
Invoke-RestMethod https://code.kimi.com/install.ps1 | Invoke-Expression
# Linux/macOS
curl -LsSf https://code.kimi.com/install.sh | bash
# or: uv tool install --python 3.13 kimi-cli   (Python 3.12–3.14)
```

Then run `kimi` in the project and `/login` (browser OAuth or API key). The
orchestrator never performs this step.

zsh users: Moonshot also ships an oh-my-zsh plugin —
`git clone https://github.com/MoonshotAI/zsh-kimi-cli.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/kimi-cli`
[verified 2026-07-22] — which pairs well with this repo's
`scripts/emperor-time.plugin.zsh`.

## Activate

In a Kimi session: `/skill:emperor-time` — loads the master SKILL.md as the
working prompt. Chains: Kimi loads the referenced `chains/*.md` files on
demand like any skill support file; or install with chain-skills exposed and
call `/skill:chain-jail` etc. directly.

## Kimi as an *enlisted worker*

As of 2026-07-22 the getting-started docs document no headless print flag.
Options, in order:

1. `kimi --help` at dowse time — check whether a non-interactive mode landed.
2. **kimi-agent-sdk** (MoonshotAI's programmatic interface to the CLI) for
   scripted dispatch.
3. `kimi acp` — Agent Client Protocol server mode, if your orchestrator speaks ACP.
4. Fall back to using Kimi interactively for its tasks while other agents run
   headless (note it in the dispatch plan).

## Flow skills (optional, Kimi extension)

Kimi adds `/flow:<name>` — multi-step workflows embedded in SKILL.md. The
micro-waterfall is a natural candidate for a flow-skill port (each phase a
step, gates as checks). Chain Jail rules apply if you build it: trial on a toy
task before real use; it's a Kimi-only artifact, keep it in `~/.kimi/skills/`.
