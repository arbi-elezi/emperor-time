# This upgrade — finish suite-green HARD-GATE (v0.4.126)

- **Task:** Ship mechanical finish suite-green gate (refuse menu / done without green suite; integrate done.py probes / eval) with `--reject-red-suite` exit codes, thin twins, emperor peers, eval fixtures. Not menu-only theater. Next VERTICAL DEPTH hard checker after verdict/breach (v0.4.125).
- **Client quote:** Finish suite-green: finish.py is menu-only; Superpowers finishing Step 1 runs full suite before options. Ship next VERTICAL DEPTH hard checker.
- **Consent:** Soft-ET continuous improvement standing consent; Worthy Spend for finish suite-green mechanical gate.
- **Queue id:** finish-suite-green / v0.4.126
- **Tip at spend:** v0.4.126 (branch `et-manager/finish-suite-green`)

## Acceptance

1. SKILL.md version ≥ 0.4.126; plugin/marketplace lockstep.
2. `emperor finish --reject-red-suite` always exits ≠0 with REJECT RED SUITE line.
3. `--require-green` / `--check-suite` reject task-red + task-no-done; accept task-ok and print MENU only when green.
4. Integrates `done.py` probes (and/or eval when present); thin twins + emperor finish peers; eval + bakeoff honesty lockstep.
5. Not archaeology; not embeddings.

## Non-goals

- Archaeology language/format pins
- Embeddings or emperor.py mega-dispatcher
- Vendoring whole Superpowers
- Changing default no-flag ENV/MENU detect (agents must pass `--require-green` before claiming done)

## Rejected alternatives

Rejected alternative: another finish-menu checklist.md without --reject-* exit codes (user tip: finish.py is menu-only today).
Rejected alternative: archaeology leaf this turn (standing vertical-depth priority is finish suite-green).
Rejected alternative: always-run full eval inside default `emperor finish` (re-entry / slow; prefer done.py probes + opt-in `--with-eval`).

## Ledger

finish.py --reject-red-suite / --require-green / --check-suite / FINISH card + thin twins finish.sh/.ps1 + emperor finish peers + finish-menu.md HARD-GATE + eval fixtures finish-suite-green/ + bakeoff/honesty lockstep on `et-manager/finish-suite-green`. See git log. Prior leaves retained: dowse.py (v0.4.26), install.py (v0.4.31), boot.py (v0.4.32), worktree.py (v0.4.33), excavate (v0.4.34), session_discovery.py (v0.4.36), diagnose.py (v0.4.37), lost-ada (v0.4.38), root_cause.py (v0.4.39), defense.py (v0.4.40), condition_wait.py (v0.4.41), polluter.py (v0.4.42), pressure.py (v0.4.43), good_tests.py (v0.4.44), skill_test.py (v0.4.45), persuasion.py (v0.4.46), sdo.py (v0.4.47), lost-fs (v0.4.48), lost-lisp (v0.4.49), lost-prolog (v0.4.50), lost-tcl (v0.4.51), lost-erl (v0.4.52), lost-rex (v0.4.53), lost-mod (v0.4.54), lost-a68 (v0.4.55), lost-a60 (v0.4.56), lost-alw (v0.4.57), lost-icn (v0.4.58), lost-obn (v0.4.59), lost-sno (v0.4.60), lost-cim (v0.4.61), lost-apl (v0.4.62), lost-bcpl (v0.4.63), lost-pli (v0.4.64), lost-st (v0.4.65), lost-ps (v0.4.66), lost-bas (v0.4.67), lost-scm (v0.4.68), lost-awk (v0.4.69), lost-sed (v0.4.70), lost-m4 (v0.4.71), lost-ed (v0.4.72), lost-make (v0.4.73), lost-dc (v0.4.74), lost-lex (v0.4.75), lost-yacc (v0.4.76), lost-roff (v0.4.77), lost-pl (v0.4.78), lost-bc (v0.4.79), lost-expect (v0.4.80), lost-lua (v0.4.81), lost-ruby (v0.4.82), lost-go (v0.4.83), lost-rust (v0.4.84), lost-c (v0.4.85), lost-js (v0.4.86), lost-py (v0.4.87), lost-ts (v0.4.88), lost-sh (v0.4.89), lost-php (v0.4.90), lost-sql (v0.4.91), lost-jq (v0.4.92), lost-xsl (v0.4.93), lost-xml (v0.4.94), lost-yaml (v0.4.95), lost-toml (v0.4.96), lost-html (v0.4.97), lost-csv (v0.4.98), lost-json (v0.4.99), lost-ini (v0.4.100), lost-plist (v0.4.101), lost-eml (v0.4.102), lost-zip (v0.4.103), lost-tar (v0.4.104), lost-gz (v0.4.105), lost-targz (v0.4.106), lost-whl (v0.4.107), lost-jar (v0.4.108), lost-war (v0.4.109), lost-apk (v0.4.110), lost-docx (v0.4.111), lost-xlsx (v0.4.112), lost-tsv (v0.4.113), lost-jsonl (v0.4.114), lost-pptx (v0.4.115), lost-pdf (v0.4.116), lost-png (v0.4.117), lost-wav (v0.4.118), lost-jpg (v0.4.119), sdd_workspace.py / task_brief.py / task_start.py / task_done.py / sdd_review_pack.py (v0.4.120), work_order.py validate_tasks / reject-no-tasks / Task-N (v0.4.121), claim_audit.py (v0.4.122), quarantine.py (v0.4.123), critique.py --reject-incomplete-critique / eight-count / Checked (v0.4.124), verdict.py --reject-hidden-breach / --check-verdict / Breach Register (v0.4.125).

## Tests

| Check | Status | Evidence |
|-------|--------|----------|
| --reject-red-suite exit ≠0 | TESTED | eval finish-suite-green HARD-GATE section |
| --check-suite rejects task-red | TESTED | evals/fixtures/finish-suite-green/task-red |
| --check-suite rejects task-no-done | TESTED | task-no-done |
| --require-green accepts task-ok + MENU | TESTED | task-ok |
| --require-green refuses task-red (no MENU) | TESTED | task-red |
| card + thin twin | TESTED | finish.py --card → FINISH checklist=yes |
| Live defect-rate vs Superpowers | UNVERIFIABLE | no three-vendor third-repo bake-off run |
