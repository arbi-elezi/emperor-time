# Adapter — Claude Code (native)

Emperor Time's canonical format *is* Claude Code's skill format. No conversion.

## Install

```powershell
# from the repo root — user scope (all projects):
.\scripts\install.ps1 -Harness claude-code -Scope user
# → %USERPROFILE%\.claude\skills\emperor-time\

# project scope:
.\scripts\install.ps1 -Harness claude-code -Scope project -Project C:\path\to\repo
# → <repo>\.claude\skills\emperor-time\
```

POSIX: `./scripts/install.sh claude-code user` / `./scripts/install.sh claude-code project /path/to/repo`

Installing to the user path also enables Kimi CLI (it reads `~/.claude/skills/`
— see `adapters/kimi-cli/`).

## Activate

- Say "emperor time", or describe work matching the skill description
  (full rigor, multi-agent orchestration, "find your own tasks", zero-hallucination
  delivery) — Claude Code routes on the frontmatter description.
- The master SKILL.md loads lean; chains and references load only when engaged
  (progressive disclosure keeps the resting cost low — lifespan drains when
  chains activate, which is the intended joke).

## Claude Code as an *enlisted worker* (when another harness orchestrates)

```bash
claude -p "<scoped worker prompt>" --output-format json
```

Useful with: `--append-system-prompt` (inject the Vow card from
`adapters/generic/EMPEROR_TIME.core.md`), `--allowedTools` (scope the blast
radius), `--permission-mode` (e.g. plan for read-only analysis), `--model`.
Confirm current flags with `claude --help` at dowse time.

## Notes

- Ledgers land in the target project's `.emperor/` (gitignore it) — not in the
  skill folder.
- Sub-chains ride inside the skill as `chains/*/SKILL.md`; Claude loads them as
  reference files. To also expose a chain as its own top-level skill (e.g.
  direct `/chain-jail`), install with `-WithChainSkills` — each chain becomes a
  separate skill folder.
