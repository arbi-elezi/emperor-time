# This upgrade — work-order Task-N structure HARD-GATE (v0.4.121)

- **Task:** Ship mechanical Task-N structure gate on work orders (Files / Expected FAIL+PASS / Commit / no Contract TBD) with `--reject-*` exit codes, thin twins, emperor peer, eval fixtures. Not another checklist.md. Feeds SDD lifecycle (v0.4.120).
- **Client quote:** VERTICAL DEPTH audit — not enough depth; rule enforcing is just md-files with no hard checkers. Want mechanical HARD checkers (exit codes). Prefer Judgment claim-audit OR work-order Task-N (if both thin, ship Task-N first).
- **Consent:** Soft-ET continuous improvement standing consent; Worthy Spend for Task-N mechanical gate.
- **Queue id:** work-order-task-n / v0.4.121
- **Tip at spend:** v0.4.121 (branch `et-manager/work-order-task-n`)

## Acceptance

1. SKILL.md version ≥ 0.4.121; plugin/marketplace lockstep.
2. `emperor work-order --reject-tbd` and `--reject-no-tasks` always exit ≠0 with REJECT lines.
3. `--check-tasks` rejects no-tasks + thin-task fixtures; accepts complete fixture.
4. G2 / `work_order.py <path>` validates header **and** Task-N for non-trivial orders.
5. Thin twins + emperor peers; eval + bakeoff honesty lockstep.
6. Not archaeology; not claim-audit this turn (backlog #1 next).

## Non-goals

- Judgment claim-audit mechanical (next soft-gate priority)
- Archaeology language/format pins
- Embeddings or emperor.py mega-dispatcher
- Vendoring whole Superpowers writing-plans

## Rejected alternatives

Rejected alternative: ship claim-audit mechanical first (both thin; user said Task-N first — feeds SDD).
Rejected alternative: another checklist.md without --reject-* exit codes (user feedback: doctrine-only is the bug).
Rejected alternative: only "any Expected:" line at G2 (already present; still allows skeleton Task headings).
Rejected alternative: archaeology leaf this turn (standing vertical-depth priority).

## Ledger

work_order.py validate_tasks + --reject-tbd / --reject-no-tasks / --check-tasks + WORK-ORDER-TASKS card + thin twins work-order.sh/.ps1 + emperor work-order peers + references/work-order.md Task-N section + eval fixtures plans-header no-tasks/thin-task + bakeoff/honesty lockstep on `et-manager/work-order-task-n`. See git log. Prior leaves retained: dowse.py (v0.4.26), install.py (v0.4.31), boot.py (v0.4.32), worktree.py (v0.4.33), excavate (v0.4.34), session_discovery.py (v0.4.36), diagnose.py (v0.4.37), lost-ada (v0.4.38), root_cause.py (v0.4.39), defense.py (v0.4.40), condition_wait.py (v0.4.41), polluter.py (v0.4.42), pressure.py (v0.4.43), good_tests.py (v0.4.44), skill_test.py (v0.4.45), persuasion.py (v0.4.46), sdo.py (v0.4.47), lost-fs (v0.4.48), lost-lisp (v0.4.49), lost-prolog (v0.4.50), lost-tcl (v0.4.51), lost-erl (v0.4.52), lost-rex (v0.4.53), lost-mod (v0.4.54), lost-a68 (v0.4.55), lost-a60 (v0.4.56), lost-alw (v0.4.57), lost-icn (v0.4.58), lost-obn (v0.4.59), lost-sno (v0.4.60), lost-cim (v0.4.61), lost-apl (v0.4.62), lost-bcpl (v0.4.63), lost-pli (v0.4.64), lost-st (v0.4.65), lost-ps (v0.4.66), lost-bas (v0.4.67), lost-scm (v0.4.68), lost-awk (v0.4.69), lost-sed (v0.4.70), lost-m4 (v0.4.71), lost-ed (v0.4.72), lost-make (v0.4.73), lost-dc (v0.4.74), lost-lex (v0.4.75), lost-yacc (v0.4.76), lost-roff (v0.4.77), lost-pl (v0.4.78), lost-bc (v0.4.79), lost-expect (v0.4.80), lost-lua (v0.4.81), lost-ruby (v0.4.82), lost-go (v0.4.83), lost-rust (v0.4.84), lost-c (v0.4.85), lost-js (v0.4.86), lost-py (v0.4.87), lost-ts (v0.4.88), lost-sh (v0.4.89), lost-php (v0.4.90), lost-sql (v0.4.91), lost-jq (v0.4.92), lost-xsl (v0.4.93), lost-xml (v0.4.94), lost-yaml (v0.4.95), lost-toml (v0.4.96), lost-html (v0.4.97), lost-csv (v0.4.98), lost-json (v0.4.99), lost-ini (v0.4.100), lost-plist (v0.4.101), lost-eml (v0.4.102), lost-zip (v0.4.103), lost-tar (v0.4.104), lost-gz (v0.4.105), lost-targz (v0.4.106), lost-whl (v0.4.107), lost-jar (v0.4.108), lost-war (v0.4.109), lost-apk (v0.4.110), lost-docx (v0.4.111), lost-xlsx (v0.4.112), lost-tsv (v0.4.113), lost-jsonl (v0.4.114), lost-pptx (v0.4.115), lost-pdf (v0.4.116), lost-png (v0.4.117), lost-wav (v0.4.118), lost-jpg (v0.4.119), sdd_workspace.py / task_brief.py / task_start.py / task_done.py / sdd_review_pack.py (v0.4.120).

## Tests

| Check | Status | Evidence |
|-------|--------|----------|
| --reject-tbd / --reject-no-tasks exit ≠0 | TESTED | eval work-order Task-N section |
| --check-tasks rejects no-tasks fixture | TESTED | evals/fixtures/plans-header/work-order-no-tasks.md |
| thin Task skeleton rejected | TESTED | work-order-thin-task.md |
| complete Task-N accepted | TESTED | work-order-complete.md |
| card + thin twin | TESTED | work-order.sh → WORK-ORDER-TASKS checklist=yes |
| Live defect-rate vs Superpowers | UNVERIFIABLE | no three-vendor third-repo bake-off run |
