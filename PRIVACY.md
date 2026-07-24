# Privacy Policy — Emperor Time

**Effective date:** 2026-07-24

**Summary: Emperor Time collects no data. It has no servers, no telemetry, no
analytics, and no accounts. Nothing is transmitted to the author, ever.**

## What this plugin is

Emperor Time is a set of Markdown instruction files (an Agent Skill) plus a few
optional local shell scripts. It contains no MCP servers, no bundled binaries,
and no network clients of its own. It cannot, by itself, open a network
connection or send data anywhere.

## Data the author receives

**None.** There is no backend, no logging endpoint, no crash reporting, no usage
metrics, and no update-check phone-home. The author has no way to observe that
you installed or used this plugin.

## Data processed on your machine

- **Task records ("ledgers").** When a task runs, the skill instructs the agent
  to write working notes — the task, its acceptance criteria, claims and their
  evidence, and a critique record — to an `.emperor/` folder inside your own
  project. These files are created locally by your agent, stay on your disk, and
  are yours to keep or delete. Nothing reads them but you and your agent.
- **Machine scan (optional scripts).** `scripts/dowse.ps1` and `scripts/dowse.sh`
  detect which coding-agent CLIs are installed by checking your `PATH`, running
  `--version`, and — only when you pass `--check-auth` — running harmless status
  commands such as `gh auth status` or `ollama list`. The results are printed to
  your terminal and go nowhere else. These scripts never read credential files,
  token stores, keychains, or environment secrets, never perform logins, and
  never transmit anything.

## Third parties

Emperor Time uses no third-party services on its own. Two things can involve
others, and both require your explicit action:

1. **Other coding agents you choose to enlist.** The skill can orchestrate
   agent CLIs already installed on your machine — for example Claude Code,
   Codex CLI, GitHub Copilot CLI, opencode, Ollama, or Kimi CLI — but only after
   it presents you a list and you approve, per task or by a standing policy you
   grant. When you approve one, the content you approved (such as a diff or a
   file) is sent to that tool, and from there it is governed by **that vendor's**
   privacy policy, not this one. Local tools like Ollama keep the content on your
   machine. The skill is instructed to tell you where data will go as part of
   asking. It never performs sign-ins for you: any login is something you run
   yourself, in your own terminal, and the plugin never handles, stores, reads,
   or displays your credentials.
2. **Web searches you ask for.** If you ask the skill to find and adapt a
   capability it lacks, it searches the web using **your agent's own** web tools,
   subject to your agent's privacy terms. Emperor Time adds no search service of
   its own.

## Children's privacy

The plugin is a developer tool and is not directed at children. It collects no
personal information from anyone, including children.

## Changes to this policy

Any change will be published in this file in the public repository, with the
effective date updated. Because the repository is public, the full history of
this policy is visible in its git log.

## Contact

Questions or concerns: open an issue at
<https://github.com/arbi-elezi/emperor-time/issues>.
