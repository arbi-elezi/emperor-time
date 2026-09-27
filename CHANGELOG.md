# Changelog

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
