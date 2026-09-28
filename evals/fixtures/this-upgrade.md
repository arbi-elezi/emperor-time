# This upgrade — queue multi-WIP HARD-GATE (v0.4.129)

- **Task:** Ship mechanical queue multi-WIP gate (refuse >1 in-progress / active `[~]` on the ledger) with `--reject-multi-wip` / `--check-wip` exit codes, thin twins, emperor peers, eval fixtures. Deepen queue beyond `next` WIP refuse theater. Next VERTICAL DEPTH hard checker after diagnose report-skeleton (v0.4.128).
- **Client quote:** Queue maturity: queue.py WIP=1 on next but agents who skip the script have no always-fail --reject-multi-wip. Add --reject-multi-wip / --check-wip that FAIL when ledger shows >1 in-progress / active WIP.
- **Consent:** Soft-ET continuous improvement standing consent; Worthy Spend for queue multi-WIP mechanical gate.
- **Queue id:** queue-reject-multi-wip / v0.4.129
- **Tip at spend:** v0.4.128 (branch `et-manager/queue-reject-multi-wip`)

## Acceptance

1. SKILL.md version ≥ 0.4.129; plugin/marketplace lockstep.
2. `emperor queue --reject-multi-wip` always exit ≠0 with REJECT MULTI WIP line.
3. `--check-wip` rejects queue-multi-two / queue-multi-three / missing file; accepts queue-ok-one / queue-ok-zero / queue-ok-placeholder.
4. Thin twins + emperor queue peers; emperor-queue skill + mechanical-gates + software-factory + eval + bakeoff honesty lockstep.
5. Not archaeology; not embeddings; prefer extending scripts/lib/queue.py.

## Non-goals

- Archaeology language/format pins
- Embeddings or emperor.py mega-dispatcher
- Changing `queue next` promote semantics (still WIP-refuses while one active exists; still exit 0 with active message)
- Auto-demoting / auto-closing excess `[~]` lines (check fails; agent must finish or `queue done`)

## Rejected alternatives

Rejected alternative: another emperor-queue SKILL paragraph without --reject-multi-wip / --check-wip exit codes (user tip: agents who skip the script have no always-fail).
Rejected alternative: archaeology leaf this turn (standing vertical-depth priority is queue multi-WIP).
Rejected alternative: new standalone checker script (user tip: prefer extending scripts/lib/queue.py).

## Ledger

queue.py --reject-multi-wip / --check-wip / REJECT MULTI WIP iron + thin twins queue.sh/.ps1 + emperor queue peers + emperor-queue SKILL HARD-GATE + eval fixtures queue-reject-multi-wip/ + bakeoff/honesty lockstep on `et-manager/queue-reject-multi-wip`. See git log. Prior leaves retained: dowse.py (v0.4.26), install.py (v0.4.31), boot.py (v0.4.32), worktree.py (v0.4.33), excavate (v0.4.34), session_discovery.py (v0.4.36), diagnose.py (v0.4.37), lost-ada (v0.4.38), root_cause.py (v0.4.39), defense.py (v0.4.40), condition_wait.py (v0.4.41), polluter.py (v0.4.42), pressure.py (v0.4.43), good_tests.py (v0.4.44), skill_test.py (v0.4.45), persuasion.py (v0.4.46), sdo.py (v0.4.47), lost-fs (v0.4.48), lost-lisp (v0.4.49), lost-prolog (v0.4.50), lost-tcl (v0.4.51), lost-erl (v0.4.52), lost-rex (v0.4.53), lost-mod (v0.4.54), lost-a68 (v0.4.55), lost-a60 (v0.4.56), lost-alw (v0.4.57), lost-icn (v0.4.58), lost-obn (v0.4.59), lost-sno (v0.4.60), lost-cim (v0.4.61), lost-apl (v0.4.62), lost-bcpl (v0.4.63), lost-pli (v0.4.64), lost-st (v0.4.65), lost-ps (v0.4.66), lost-bas (v0.4.67), lost-scm (v0.4.68), lost-awk (v0.4.69), lost-sed (v0.4.70), lost-m4 (v0.4.71), lost-ed (v0.4.72), lost-make (v0.4.73), lost-dc (v0.4.74), lost-lex (v0.4.75), lost-yacc (v0.4.76), lost-roff (v0.4.77), lost-pl (v0.4.78), lost-bc (v0.4.79), lost-expect (v0.4.80), lost-lua (v0.4.81), lost-ruby (v0.4.82), lost-go (v0.4.83), lost-rust (v0.4.84), lost-c (v0.4.85), lost-js (v0.4.86), lost-py (v0.4.87), lost-ts (v0.4.88), lost-sh (v0.4.89), lost-php (v0.4.90), lost-sql (v0.4.91), lost-jq (v0.4.92), lost-xsl (v0.4.93), lost-xml (v0.4.94), lost-yaml (v0.4.95), lost-toml (v0.4.96), lost-html (v0.4.97), lost-csv (v0.4.98), lost-json (v0.4.99), lost-ini (v0.4.100), lost-plist (v0.4.101), lost-eml (v0.4.102), lost-zip (v0.4.103), lost-tar (v0.4.104), lost-gz (v0.4.105), lost-targz (v0.4.106), lost-whl (v0.4.107), lost-jar (v0.4.108), lost-war (v0.4.109), lost-apk (v0.4.110), lost-docx (v0.4.111), lost-xlsx (v0.4.112), lost-tsv (v0.4.113), lost-jsonl (v0.4.114), lost-pptx (v0.4.115), lost-pdf (v0.4.116), lost-png (v0.4.117), lost-wav (v0.4.118), lost-jpg (v0.4.119), sdd_workspace.py / task_brief.py / task_start.py / task_done.py / sdd_review_pack.py (v0.4.120), work_order.py validate_tasks / reject-no-tasks / Task-N (v0.4.121), claim_audit.py (v0.4.122), quarantine.py (v0.4.123), critique.py --reject-incomplete-critique / eight-count / Checked (v0.4.124), verdict.py --reject-hidden-breach / --check-verdict / Breach Register (v0.4.125), finish.py --reject-red-suite / --require-green / --check-suite (v0.4.126), grill.py --reject-no-path / --reject-stage-skip / --reject-impl-before-approval / --check-path / PATH_AND_STAGE_BEFORE_IMPL (v0.4.127), diagnose.py --reject-no-report / --check-report / CITE_OR_FAIL_REPORT / diagnose-report-skeleton (v0.4.128).

## Tests

| Check | Status | Evidence |
|-------|--------|----------|
| --reject-multi-wip exit ≠0 | TESTED | eval queue-reject-multi-wip HARD-GATE section |
| --check-wip rejects multi-two / multi-three | TESTED | evals/fixtures/queue-reject-multi-wip/queue-multi-*.md |
| --check-wip rejects missing file | TESTED | non-existent path in eval |
| --check-wip accepts ok-one / ok-zero / placeholder | TESTED | queue-ok-*.md |
| thin twin forwards flags | TESTED | queue.sh --check-wip |
| Live defect-rate vs Superpowers | UNVERIFIABLE | no three-vendor third-repo bake-off run |
