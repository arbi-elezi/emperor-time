# Changelog

## 0.4.14
- Verification-before-completion / evidence HARD-GATE leaf: Superpowers `verification-before-completion` → **The Iron Law** + **The Gate Function** only, adapted into `skills/emperor-verify/verification-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/evidence.py` prints EVIDENCE/STEP/MUST card, rejects step skips (`--advance`), hard-gates unverified completion claims (`--reject-unverified`); thin `evidence.sh` / `evidence.ps1`; `emperor evidence` on bash/ps1/zsh/cmd peers
- emperor-verify MUST the checklist before any completion / pass / fixed / done claim; catalog + navigation point local-first; eval locks card + skip rejection + reject-unverified
- Plugin, marketplace, and SKILL.md at 0.4.14

## 0.4.13
- Authoring iron-law / skill-RGR leaf: Superpowers `writing-skills` → **The Iron Law (Same as TDD)** + skill RED-GREEN-REFACTOR only, adapted into `chains/chain-jail/authoring-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/author.py` prints AUTHOR/STEP/MUST card, rejects step skips (`--advance`), hard-gates untested skill writes (`--reject-untested`); thin `author.sh` / `author.ps1`; `emperor author` on bash/ps1/zsh/cmd peers
- Chain Jail authoring.md + emperor-capture MUST the checklist before skill body; catalog + navigation point local-first; eval locks card + skip rejection + reject-untested
- Plugin, marketplace, and SKILL.md at 0.4.13

## 0.4.12
- Archaeology COBOL leaf: `evals/fixtures/lost-cbl/HELLO.CBL` + identify smoke; GnuCOBOL 3.2 boot probe VERIFIED (`cobc -x`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due)
- Jail pin `references/archaeology-cobol-manual.md` — GnuCOBOL Programmer’s Guide §4 IDENTIFICATION DIVISION / PROGRAM-ID
- Catalog + SKILL.md + archaeology.md link the third pin alongside Pascal and ASM; eval locks `*.cbl` identify on lost-cbl
- Plugin, marketplace, and SKILL.md at 0.4.12

## 0.4.11
- Request-review HARD-GATE leaf: Superpowers `requesting-code-review` → When / How / Act-on-feedback only, adapted into `skills/emperor-verify/request-review-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/review_req.py` prints REVIEW/STEP/MUST card, rejects step skips (`--advance`), hard-gates author self-review (`--reject-self-review`); thin `review.sh` / `review.ps1`; `emperor review` on bash/ps1/zsh/cmd peers
- emperor-verify MUST the checklist before merge / major feature / subagent task done; reuses `review-pack` at Step 3; eval locks card + skip rejection + reject-self-review

## 0.4.10
- Worktree isolation leaf: Superpowers `using-git-worktrees` → detect / native-or-git / check-ignore / baseline HARD-GATE only, adapted into `skills/emperor-worktree/isolation-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/worktree_iso.py` prints WORKTREE/STEP/MUST card, rejects step skips (`--advance`), hard-gates blind create (`--reject-blind-create`); thin `iso.sh` / `iso.ps1`; `emperor iso` on bash/ps1/zsh/cmd peers
- emperor-worktree + emperor-build MUST the checklist before standard/heavy mutate; `.worktrees/` gitignored; eval locks card + skip rejection + reject-blind-create

## 0.4.9
- TDD iron-law / RGR leaf: Superpowers `test-driven-development` → **The Iron Law** + **Red-Green-Refactor** HARD-GATE only, adapted into `skills/emperor-tdd/red-green-refactor.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/tdd.py` prints TDD/STEP/MUST card, rejects step skips (`--advance`), hard-gates prod-before-fail (`--reject-prod`); thin `tdd.sh` / `tdd.ps1`; `emperor tdd` on bash/ps1/zsh/cmd peers
- emperor-tdd + emperor-build MUST the checklist before production code; eval locks card + skip rejection + reject-prod

## 0.4.8
- Grill/brainstorm leaf: Superpowers `brainstorming` → **HARD-GATE** only, adapted into `skills/emperor-require-design/grill-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/grill.py` prints GRILL/STEP/MUST card, rejects step skips (`--advance`), hard-gates impl jumps (`--reject-impl`); thin `grill.sh` / `grill.ps1`; `emperor grill` on bash/ps1/zsh/cmd peers
- require-design MUST the checklist before BUILD; eval locks card + skip rejection + reject-impl

## 0.4.7
- Heal four-phase leaf: Superpowers `systematic-debugging` → **The Four Phases** only, adapted into `skills/emperor-heal/debug-four-phases.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/debug_phases.py` prints DEBUG/PHASE/MUST card and rejects phase skips (`--advance`); thin `heal.sh` / `heal.ps1`; `emperor heal` on bash/ps1/zsh/cmd peers
- Holy Chain router + emperor-heal skill MUST the checklist before proposing fixes; eval locks card + skip rejection

## 0.4.6
- MUST-route doctrine bite: Load law + AGENTS.md standing order require one governing skill/file (or `emperor route` / `emperor activate`) before creative work, clarifying questions, or exploring
- Python-first router: `scripts/lib/route.py` owns matching; `route.sh` / `route.ps1` are thin twins (same exits 0/1/2)
- Adapter SessionStart notes: cursor/codex/kimi-cli/ollama/opencode/generic document host-agnostic silent boot + MUST-route
- Honest `references/sdlc-comparison.md` refresh: Router MVP, excavate alias, remote CI `eval.yml`, adapter MUST-route notes
- Eval locks `route.py` presence + `finish the branch` → forge; SessionStart MUST-route language retained

## 0.4.5
- Silent activation MUST-route: Superpowers `using-superpowers` 1% leaf adapted into `skills/emperor-resume/must-route.md` — SessionStart fires without waiting for "emperor time"
- Python core `scripts/lib/activate.py` prints ACTIVATION/MUST card from disk state or utterance; thin `activate.sh` / `activate.ps1`; `emperor activate` on bash/ps1/zsh/cmd peers
- SessionStart hook runs activate after boot; eval locks the card + utterance route smoke

## 0.4.4
- Finish menu: Superpowers finish-branch aspect adapted into `skills/emperor-forge/finish-menu.md` (merge locally / PR / keep; typed `discard`; owned-worktree cleanup)
- `scripts/finish.sh` / `finish.ps1` twins detect env and print the menu (no merge/push); `emperor finish` wired on bash/ps1/zsh/cmd peers
- Route triggers: finish the branch / implementation complete / merge locally → forge; eval locks the aspect + script output

## 0.4.3
- Silent-boot PS parity: `boot.ps1` sources `lib/host.ps1` + `Write-EmperorHostReport` (same host.env keys as bash); `emperor.ps1` auto-boots when `.emperor/host.env` missing; Cursor adapter documents `emperor boot` / Windows silent-boot contract
- Archaeology: Jail-pin NASM 2.16.03 §7.3 SECTION for FOO.ASM (`references/archaeology-asm-manual.md`)
- Route trigger harden: blocked/WIP → queue; red build/derail → heal; missing capability/jail → capture; nasm/assembler → excavate
- Catalog links: archaeology Jail pins (pascal + asm) from `archaeology.md`, skill-catalog, and SKILL.md
- Queue empty UX: comment-only empty `.emperor/queue.md`; `queue.sh`/`queue.ps1` skip `(empty…)` / parentheses-only placeholder lines so `queue next` never promotes junk (WIP=1 kept)
- Plugin, marketplace, SKILL.md, excavate + queue skill frontmatter at 0.4.3

## 0.4.2
- Wave merge: CI eval workflow; adapter silent-boot parity; SDLC comparison; Pascal Jail pin (ISO 7185 §6.10)
- Queue Kanban maturity (WIP=1 statuses); trigger→skill `route` MVP (sh/ps1 twins)
- First-class `excavate` alias + usage hygiene across emperor peers
- Archaeology probes: `lost-pas` HELLO.PAS + `lost-asm` FOO.ASM fixtures with dialect-honest identify smokes
- Plugin, marketplace, and SKILL.md at 0.4.2

## 0.4.1
- Silent boot: `scripts/boot.sh` / `boot.ps1` write `.emperor/host.env`, `survey.md`, and optional `eval.log` with no user ritual
- Identify is internal: fossils and `scripts/emperor identify <path>` for foreign trees; agents read survey, do not ask the client to run identify
- Excavate router: lost/ancient/unmarked codebases via `skills/emperor-excavate` and Dowsing excavate
- Plugin, marketplace, and SKILL.md at 0.4.1 (archaeology keywords)
- Audit-fixes merge: `emperor.cmd` hook peer, eval twins for queue/forge/identify/boot, +x on factory scripts

## 0.3.3
- Plugin and marketplace register `emperor-tdd` and `emperor-worktree`
- `references/iron-laws.md` and `templates/state.md` (names SKILL.md already used)
- Self-application fixture: `evals/fixtures/this-upgrade.md`

## 0.3.2
- SKILL.md rewritten as orchestrator (vows + five chains kept)
- TDD iron law skill, worktree skill, SessionStart hook, STATE resume

## 0.3.0
- Work-order, review-pack, gate.sh, eval.sh, phase skills, jail pin-and-consent

## 0.2.0
- Plugin marketplace packaging, privacy policy
