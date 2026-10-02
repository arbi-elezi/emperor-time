# ET vs other SDLC models

Load when a client asks how Emperor Time relates to Waterfall, Agile, Kanban,
Spiral, DevOps, or trunk-based development. This is a map, not a sales pitch.
The vows still govern.

## One-line thesis

ET is a **per-task micro-waterfall** with **mechanical gates**, **evidence
vows**, and **archaeology / heal / capture / steal** overlays. Iteration is
between tasks (queue → next), not by skipping a gate inside one.

## Model map

| Model | What it optimizes | How ET relates |
|---|---|---|
| Classical Waterfall | Big-bang phases across a whole product | Same *shape* (require → design → build → verify → deliver), but scoped to **one task**. No multi-month "design freeze." |
| Micro-waterfall (ET) | Honest gates per unit of work | Canonical. G0–G5 + ledger. Right-size text; never delete a gate (`references/micro-waterfall.md`). |
| Agile / Scrum | Timeboxed iteration, ceremony, team sync | Macro loop is agile (ship → next). **No** sprint planning, standups, story points, or retrospectives as rites. Client consent replaces ceremony. |
| Kanban | Flow, WIP limits, visible board | Intent is WIP=1 (one active task). Local queue is markdown via `scripts/lib/queue.py` (statuses + WIP refuse on `main`). |
| Spiral | Risk-driven cycles, prototypes | Dowsing + Chain Jail play the risk/prototype role: hunt evidence, trial a captured skill, then bind. Not a formal risk matrix. |
| DevOps / CI/CD | Continuous integration + delivery | Factory ends at forge/PR with consent. Local structural eval (`scripts/lib/eval.py` via thin `eval.sh`/`eval.ps1`) and remote `.github/workflows/eval.yml` are on `main`. |
| Trunk-based | Short-lived branches, frequent integrate | Compatible: small diffs, revert-sensitive probes, no drive-by. ET does not mandate trunk vs short PR branches — house git rules win. |

## ET factory (G0–G5) in SDLC words

```
intake / queue.next
  → G0 DOWSE     (scope / discovery)
  → G1 REQUIRE   (acceptance + out-of-scope)
  → G2 DESIGN    (approach + test plan on disk)
  → G3 BUILD     (smallest change; TDD probes)
  → G4 VERIFY    (quoted evidence + critique)
  → G5 DELIVER   (ship / report; forge PR if consented)
  → queue.next → REST
```

Gates are **exit codes** (`scripts/emperor gate …`), not markdown wishes
(`references/mechanical-gates.md`).

## Overlays other SDLCs rarely name

| Overlay | Role | Nearest classical cousin |
|---|---|---|
| Archaeology / excavate | Recover behavior from lost or ancient trees before modernizing | Reverse engineering / brownfield discovery — language-agnostic |
| Heal (Holy Chain) | Red build / derail → reproduce, bisect, minimal heal, process postmortem | Incident response + root-cause, not "retry the same prompt" |
| Capture (Chain Jail) | Missing capability → hunt/adapt/author, pin, consent, trial | Tooling acquisition with quarantine — not unchecked plugin install |
| Steal (Steal Chain) | Consent-based multi-agent / multi-shell twins for parallel work | Pairing / swarm under quarantine; outputs stay CONJECTURE until Judgment |

## Strengths (load-bearing, not slogans)

- **Mechanical gates** — Vow of Phases enforced by scripts; fluent "done" without `gate`/`done` exit 0 is heresy.
- **Language-agnostic archaeology** — Pascal, ASM, COBOL, ROM are in-scope; probes are any command, not a favorite test runner.
- **Multi-shell twins** — `.sh` / `.ps1` (and cmd/zsh entrypoints) so the rite
  has a **structure path** on Windows and Unix. Preferred stranger path is
  PowerShell Core / `pwsh`. Native Windows PowerShell 5.1 equal-smooth is
  **HOLD** until a dated receipt; thin `.ps1` still hardcode `python3` (S12).
  See README Platforms + `references/portability.md`.
- **Evidence vows** — VERIFIED needs a quoted experiment or two independent sources; memory is rumor.
- **Consent boundary** — no enlist, login, or public PR without explicit client yes.

## Gaps (honest)

| Gap | Today on `main` | Closing without depending on unmerged PRs |
|---|---|---|
| No sprint ceremony | By design (no backlog grooming rite) | Stay ceremony-free; queue + ledger replace standups |
| WIP metrics thin | WIP=1 is **intent** in doctrine/queue skill; no cycle-time dashboard | Optional `started`/`finished` fields and status marks remain optional polish |
| Board / route UX | Skill tables + Dowsing + trigger→skill Router MVP (`scripts/emperor route`, Python `scripts/lib/route.py`) on `main` | Keep loading exactly one governing file; route refines when utterance is ambiguous |
| Remote CI | Local `scripts/lib/eval.py` (thin `eval.sh`/`eval.ps1`) **and** `.github/workflows/eval.yml` on `main` | Do not invent green checks; quote the workflow run you actually saw |
| Adapter boot / MUST-route | Silent boot + host-agnostic MUST-route notes on cursor/codex/kimi-cli/ollama/opencode/generic adapters | Claude SessionStart still runs boot + activate; other hosts follow adapter README |
| Excavate ergonomics | Identify/survey path **and** first-class `excavate` alias on `main` | Prefer `scripts/emperor excavate` / archaeology skill for lost trees |

Phrase carefully in client reports: quote the eval path you ran (local script and/or Actions run). Never claim "CI is green on main" without a check run you can point at.

## What not to say

- Do not claim ET *is* Scrum with different labels.
- Do not claim Kanban metrics exist beyond what the checked-out queue scripts print.
- Do not claim trunk-based or CI/CD policy for the *client's* product repo — only for how ET itself ships when that repo's rules say so.
- Do not load this file every turn. Once per "how does this compare?" conversation is enough.
