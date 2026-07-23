<img src="assets/shovel.png" width="330" alt="pixel art: a shovel planted in a dirt mound speckled with red and orange flecks">

*Dowse. Dig. Verify. Pay in tokens.*

```text
▐██▌          ▐██▌   █████ █   █ ████  █████ ████   ███  ████
 ██            ██    █     ██ ██ █   █ █     █   █ █   █ █   █
  ██          ██     ████  █ █ █ ████  ████  ████  █   █ ████
   ██        ██      █     █   █ █     █     █ █   █   █ █ █
    ██      ██       █████ █   █ █     █████ █  █   ███  █  █
     ██    ██
      ██  ██         █████ █████ █   █ █████
       ████            █     █   ██ ██ █
        ██             █     █   █ █ █ ████
       ████            █     █   █   █ █
    ████  ████         █     █   █   █ █████
   ████    ████
   ███      ███
   ██        ██
```

<img src="assets/scarlet-eyes.png" width="660" alt="pixel art: close-up of scarlet eyes under blond bangs, ringed pink irises with star glints">

*The eyes have turned scarlet. Emperor Time is active — every token is paid for.*

# Emperor Time

**A unified coding-harness skill that ironically maximizes token usage — and
non-ironically maximizes delivered, verified value.**

Named for Kurapika's Specialist ability in *Hunter × Hunter*: when his eyes turn
scarlet, he gains 100% proficiency in every Nen category, paying one hour of
lifespan per second of use. This skill does the same to a coding agent: every
SDLC discipline at full rigor, paid for in tokens. The contract that makes the
irony safe: **every token spent must convert into verified value** — rigor,
evidence, critique — never repetition or filler.

It is written in the open **Agent Skills** format (`SKILL.md`), so it runs
natively in **Claude Code** and **Kimi CLI** (which share skill directories),
and deploys to Codex CLI, Copilot CLI, opencode, Ollama, and any open-weight
model via the adapters.

## The lore → mechanics map

| Hunter × Hunter | Emperor Time (this repo) |
|---|---|
| **Emperor Time** — all Nen types at 100%, costs lifespan | All SDLC phases at full rigor per task, costs tokens; spend must buy verified value |
| **Holy Chain** (thumb) — heals wounds | Recovery: regressions, red builds, corrupted state, derailed process |
| **Steal Chain** (index) — takes another's ability | Hetero-agent orchestration: enlist Claude Code / Kimi / Codex / Copilot / opencode / Ollama as workers and critics |
| **Chain Jail** (middle) — binds the target, forces Zetsu | Skill capture: find the closest skill on the net, adapt it to this harness, or author one — then bind (test) it before use |
| **Dowsing Chain** (ring) — finds things, detects lies | Intuition: discover your own tasks from repo evidence; scan the machine for counterpart agents; flag contradictions |
| **Judgment Chain** (pinky) — a rule staked into the heart | Process gates: scientific-method fact-checking, mandatory critique; vow breaches are recorded and remediated, never hidden |
| **Restriction & Pledge** — stricter vow, stronger power | The Six Vows: evidence, phases, ledger, critique, consent, worthy spend |

## Quickstart

### Claude Code (native) — also covers Kimi CLI

```powershell
# user-level (all projects) — Kimi CLI reads this same directory
.\scripts\install.ps1 -Harness claude-code -Scope user

# or project-level: installs into <project>\.claude\skills\emperor-time\
.\scripts\install.ps1 -Harness claude-code -Scope project -Project C:\path\to\repo
```

Then just say "emperor time" (or describe a task that needs full rigor) in
Claude Code, or run `/skill:emperor-time` in Kimi CLI.

### macOS / Linux

```bash
chmod +x scripts/*.sh                     # once, after clone (or prefix with `bash`)
./scripts/install.sh claude-code user     # same coverage: Claude Code + Kimi CLI
./scripts/dowse.sh                        # scan the machine for enlistable agents
```

Shell layer — a single `emperor` command with completion:

```bash
# zsh (~/.zshrc) — or symlink scripts/ into ${ZSH_CUSTOM}/plugins/emperor-time for oh-my-zsh:
source /path/to/emperor-time/scripts/emperor-time.plugin.zsh
# bash (~/.bashrc):
source /path/to/emperor-time/scripts/emperor-time.bash

emperor dowse                 # machine scan
emperor install kimi user     # deploy
emperor core | pbcopy         # distilled prompt → clipboard (xclip/wl-copy on Linux)
```

The `.ps1` scripts also run under pwsh on macOS/Linux if you prefer PowerShell.

### Vendor-neutral (any Agent-Skills harness)

```powershell
.\scripts\install.ps1 -Harness generic-agents    # → ~/.config/agents/skills/emperor-time/
```

### opencode / Ollama / plain open-weight models

See `adapters/opencode/`, `adapters/ollama/`, and `adapters/generic/` —
the last contains `adapters/generic/EMPEROR_TIME.core.md`, the whole doctrine
distilled into a single system prompt for models that can't load a skill tree.

### Scan your machine for enlistable agents

```powershell
.\scripts\dowse.ps1            # detection only — read-only, touches no credentials
```

## How a task flows

```
  intake ──► DOWSE ──G0──► REQUIRE ──G1──► DESIGN ──G2──► BUILD ──G3──► VERIFY ──G4──► DELIVER ──G5──► rest
             find/scope     acceptance     approach +      smallest      trials +       ledger +
             the task       criteria       test plan       change        claims +       faithful
                                                                        critique       report
```

One task = one micro-waterfall = one ledger in `.emperor/tasks/<id>/`. Gates are
never skipped, only right-sized: a trivial task's phases may each be one
sentence. Iteration happens across tasks, not by skipping within one.

## Repo map

```
SKILL.md                          The master skill: vows, loop, and the Invocation
                                  Ritual (md-selection — load one file at a time)
chains/                           Five chains — each a router SKILL.md + one MD per aspect
  dowsing-chain/                  task-dowsing · system-dowsing · lie-detection
  chain-jail/                     absence-check · hunt · adaptation · authoring · trial-and-register
  judgment-chain/                 gatekeeping · claim-audit · self-critique · hetero-critique · verdicts-and-breaches
  steal-chain/                    consent-protocol · sign-in-handoff · dispatch · quarantine · routing
  holy-chain/                     triage · reproduce-and-bisect · heal-and-verify · process-healing
references/
  micro-waterfall.md              Full phase/gate spec + right-sizing rules
  scientific-method.md            Claim lifecycle, tripwires, evidence rules
  agent-registry.md               Detect / sign-in / invoke matrix per agent CLI
  portability.md                  Deploying to other harnesses & open-weight models
templates/
  task-ledger.md                  Per-task record (phases, lifespan, breaches)
  claim-ledger.md                 Claims → experiments → evidence
  critique.md                     Prosecutor checklist + verdict
adapters/
  claude-code/  kimi-cli/  opencode/  ollama/  generic/
scripts/
  dowse.ps1  dowse.sh             Read-only machine scan for agent CLIs
  install.ps1  install.sh         Deploy the skill into a harness
  emperor-time.plugin.zsh         zsh layer: `emperor` command (oh-my-zsh compatible)
  emperor-time.bash               bash layer: same command for ~/.bashrc
```

## Design notes

- **Why waterfall, per task?** A strict sequence with gates is exactly what
  keeps an LLM from writing code before understanding requirements, or claiming
  success before verifying. Sized to a single task, it *is* iteration — agile at
  the macro scale, waterfall at the micro scale.
- **Why so strict?** Nen logic: power comes from Restriction and Pledge. Each
  vow exists to close a known LLM failure mode — hallucinated flags, phantom
  success reports, silent scope drift, repeated failing commands.
- **Selection over bulk-loading:** the tree is deliberately wide so each load
  is narrow. Chain routers map a situation to exactly one aspect MD; the
  master SKILL.md's Invocation Ritual forbids preloading. Nothing is "all
  bashed in the prompt at once" — context is aura, and leaked context is
  leaked lifespan.
- **Privacy stance:** the orchestrator never signs in to anything. Detected
  agents needing auth are handed back to the human, who logs in from their own
  terminal; the orchestrator re-checks with harmless status commands only.
- **One install, two harnesses (verified 2026-07-22):** Kimi CLI's documented
  skill search paths include `~/.claude/skills/` and project `.claude/skills/`,
  so the Claude Code install location serves both natively.
- **Untrusted by default:** anything an enlisted agent returns is CONJECTURE
  until the orchestrator verifies it. Hallucination containment applies across
  agents, not just within one.
- **Platforms:** Windows (PowerShell 5.1+), macOS and Linux (POSIX-lean bash
  scripts, compatible with macOS's stock bash 3.2; zsh plugin for the macOS
  default shell). `.gitattributes` pins shell scripts to LF so a Windows-side
  clone can't break Unix shebangs. pwsh runs the `.ps1` variants anywhere.

## License

Pick one before publishing (MIT recommended for a skill meant to be captured,
adapted, and re-bound by others — that is, after all, what Chain Jail does).
