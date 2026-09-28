# This upgrade — SDD task lifecycle vertical depth (v0.4.120)

- **Task:** Ship plan-scoped SDD task lifecycle (brief / BASE / task-done) under `.emperor/sdd/<plan-slug>/`, deepening execute/subagent from print-cards into mutating mechanics. Python cores + thin .sh/.ps1 twins + emperor peers. Eval-locked. Not archaeology. Never vendor whole Superpowers prompts/templates.
- **Client quote:** Soft-ET consented continuous soft self-host improvements. Largest Superpowers *script* gap remaining after executing-plans / subagent-driven cards: plan-scoped workspace + task-brief + BASE record + task-done progress with probe/range guards. ET layout `.emperor/sdd/` (NOT `.superpowers/`). Skip archaeology. Skip embeddings/emperor.py mega-dispatcher.
- **Consent:** Soft-ET continuous improvement standing consent; Worthy Spend for vertical depth SDD lifecycle.
- **Queue id:** sdd-task-lifecycle / v0.4.120
- **Tip at spend:** v0.4.120 (branch `et-manager/sdd-task-lifecycle`)

## Acceptance

1. SKILL.md version ≥ 0.4.120; plugin/marketplace lockstep.
2. `emperor task-brief <work-order> N` writes non-empty brief or exits ≠0.
3. `emperor task-start` prints `brief:` + `base:`; `task-done` refuses failing probe / empty BASE..HEAD.
4. Workspace plan-scoped (two plans → two dirs; collision marker works); `.emperor/sdd/` self-ignore.
5. Checklists point at scripts; eval fixtures `sdd-lifecycle`; bakeoff + honesty inventory rows.
6. No archaeology fixtures; no whole-SP prompt templates.

## Non-goals

- Archaeology language/format pins
- Embeddings or emperor.py mega-dispatcher
- Vendoring whole Superpowers (prompts/templates/implementer-prompt)
- `.superpowers/sdd/` layout

## Rejected alternatives

Rejected alternative: archaeology leaf this turn (standing vertical-depth priority; SP script gap larger).
Rejected alternative: keep execute/subagent as print-cards only (lifecycle stays unread/unmutated).
Rejected alternative: vendor whole Superpowers SDD skill + prompt templates (Chain Jail aspect only; ET owns layout).
Rejected alternative: embeddings/emperor.py mega-dispatcher (deferred).
Rejected alternative: `.superpowers/sdd/` path (ET is `.emperor/sdd/`).

## Ledger

sdd_workspace.py + task_brief.py + task_start.py + task_done.py + sdd_review_pack.py + thin twins + emperor peers + checklist/SKILL pointers + eval/bakeoff/honesty lockstep on `et-manager/sdd-task-lifecycle`. See git log. Prior leaves retained: dowse.py (v0.4.26), install.py (v0.4.31), boot.py (v0.4.32), worktree.py (v0.4.33), excavate (v0.4.34), session_discovery.py (v0.4.36), diagnose.py (v0.4.37), lost-ada (v0.4.38), root_cause.py (v0.4.39), defense.py (v0.4.40), condition_wait.py (v0.4.41), polluter.py (v0.4.42), pressure.py (v0.4.43), good_tests.py (v0.4.44), skill_test.py (v0.4.45), persuasion.py (v0.4.46), sdo.py (v0.4.47), lost-fs (v0.4.48), lost-lisp (v0.4.49), lost-prolog (v0.4.50), lost-tcl (v0.4.51), lost-erl (v0.4.52), lost-rex (v0.4.53), lost-mod (v0.4.54), lost-a68 (v0.4.55), lost-a60 (v0.4.56), lost-alw (v0.4.57), lost-icn (v0.4.58), lost-obn (v0.4.59), lost-sno (v0.4.60), lost-cim (v0.4.61), lost-apl (v0.4.62), lost-bcpl (v0.4.63), lost-pli (v0.4.64), lost-st (v0.4.65), lost-ps (v0.4.66), lost-bas (v0.4.67), lost-scm (v0.4.68), lost-awk (v0.4.69), lost-sed (v0.4.70), lost-m4 (v0.4.71), lost-ed (v0.4.72), lost-make (v0.4.73), lost-dc (v0.4.74), lost-lex (v0.4.75), lost-yacc (v0.4.76), lost-roff (v0.4.77), lost-pl (v0.4.78), lost-bc (v0.4.79), lost-expect (v0.4.80), lost-lua (v0.4.81), lost-ruby (v0.4.82), lost-go (v0.4.83), lost-rust (v0.4.84), lost-c (v0.4.85), lost-js (v0.4.86), lost-py (v0.4.87), lost-ts (v0.4.88), lost-sh (v0.4.89), lost-php (v0.4.90), lost-sql (v0.4.91), lost-jq (v0.4.92), lost-xsl (v0.4.93), lost-xml (v0.4.94), lost-yaml (v0.4.95), lost-toml (v0.4.96), lost-html (v0.4.97), lost-csv (v0.4.98), lost-json (v0.4.99), lost-ini (v0.4.100), lost-plist (v0.4.101), lost-eml (v0.4.102), lost-zip (v0.4.103), lost-tar (v0.4.104), lost-gz (v0.4.105), lost-targz (v0.4.106), lost-whl (v0.4.107), lost-jar (v0.4.108), lost-war (v0.4.109), lost-apk (v0.4.110), lost-docx (v0.4.111), lost-xlsx (v0.4.112), lost-tsv (v0.4.113), lost-jsonl (v0.4.114), lost-pptx (v0.4.115), lost-pdf (v0.4.116), lost-png (v0.4.117), lost-wav (v0.4.118), lost-jpg (v0.4.119).

## Tests

| Check | Status | Evidence |
|-------|--------|----------|
| task-brief writes non-empty / exits ≠0 if missing | TESTED | eval SDD section + fixtures/sdd-lifecycle |
| task-start prints brief: + base: | TESTED | eval lock |
| task-done refuses empty range / failing probe | TESTED | eval tmp-repo probe |
| plan-scoped workspace + collision marker | TESTED | alpha vs beta work-order.md |
| sdd_review_pack ancestor + non-empty guards | TESTED | eval lock |
| Live defect-rate vs Superpowers | UNVERIFIABLE | no three-vendor third-repo bake-off run |
