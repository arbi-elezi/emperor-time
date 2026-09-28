# This upgrade — SOT + artifact multi-repo sync (v0.4.134)

- **Task:** Deepen inverted workspace: real fetch-only SOT plugin mirrors (`sot add-plugin` / `sot sync`) and multi-repo artifact materialization (`artifacts sync`) from those mirrors. Next VERTICAL DEPTH after thoughttrail-super-context (v0.4.133).
- **Client quote:** P1 after P0 merge — SOT sync/add-plugin + artifact multi-repo stubs real enough to sync.
- **Consent:** Soft-ET continuous improvement standing consent; Worthy Spend.
- **Queue id:** sot-artifact-sync / v0.4.134
- **Tip at spend:** v0.4.133 @ 8c4781c (branch `et-manager/sot-artifact-sync` from origin/main after #149).

## Why this leaf (not neighbors)

Vertical depth on inverted workspace. Graph+trail already shipped; now SOT/artifact sync teeth.
Rejected alternative: forge residual; archaeology; embeddings; Graphify copy.
Rejected alternative: MD-only HARD-GATE claims without exit codes are not enough.

## Delivery

super_context.py sot add-plugin|sync (git clone --mirror / fetch) + artifacts sync (multi-repo copies under artifacts/<id>/repos/) + fixtures sot-artifact-sync/ + bakeoff/honesty + doctrine lockstep on `et-manager/sot-artifact-sync`. See git log. Prior leaves retained: dowse.py (v0.4.26), install.py (v0.4.31), boot.py (v0.4.32), worktree.py (v0.4.33), excavate (v0.4.34), session_discovery.py (v0.4.36), diagnose.py (v0.4.37), lost-ada (v0.4.38), root_cause.py (v0.4.39), defense.py (v0.4.40), condition_wait.py (v0.4.41), polluter.py (v0.4.42), pressure.py (v0.4.43), good_tests.py (v0.4.44), skill_test.py (v0.4.45), persuasion.py (v0.4.46), sdo.py (v0.4.47), lost-fs (v0.4.48), lost-lisp (v0.4.49), lost-prolog (v0.4.50), lost-tcl (v0.4.51), lost-erl (v0.4.52), lost-rex (v0.4.53), lost-mod (v0.4.54), lost-a68 (v0.4.55), lost-a60 (v0.4.56), lost-alw (v0.4.57), lost-icn (v0.4.58), lost-obn (v0.4.59), lost-sno (v0.4.60), lost-cim (v0.4.61), lost-apl (v0.4.62), lost-bcpl (v0.4.63), lost-pli (v0.4.64), lost-st (v0.4.65), lost-ps (v0.4.66), lost-bas (v0.4.67), lost-scm (v0.4.68), lost-awk (v0.4.69), lost-sed (v0.4.70), lost-m4 (v0.4.71), lost-ed (v0.4.72), lost-make (v0.4.73), lost-dc (v0.4.74), lost-lex (v0.4.75), lost-yacc (v0.4.76), lost-roff (v0.4.77), lost-pl (v0.4.78), lost-bc (v0.4.79), lost-expect (v0.4.80), lost-lua (v0.4.81), lost-ruby (v0.4.82), lost-go (v0.4.83), lost-rust (v0.4.84), lost-c (v0.4.85), lost-js (v0.4.86), lost-py (v0.4.87), lost-ts (v0.4.88), lost-sh (v0.4.89), lost-php (v0.4.90), lost-sql (v0.4.91), lost-jq (v0.4.92), lost-xsl (v0.4.93), lost-xml (v0.4.94), lost-yaml (v0.4.95), lost-toml (v0.4.96), lost-html (v0.4.97), lost-csv (v0.4.98), lost-json (v0.4.99), lost-ini (v0.4.100), lost-plist (v0.4.101), lost-eml (v0.4.102), lost-zip (v0.4.103), lost-tar (v0.4.104), lost-gz (v0.4.105), lost-targz (v0.4.106), lost-whl (v0.4.107), lost-jar (v0.4.108), lost-war (v0.4.109), lost-apk (v0.4.110), lost-docx (v0.4.111), lost-xlsx (v0.4.112), lost-tsv (v0.4.113), lost-jsonl (v0.4.114), lost-pptx (v0.4.115), lost-pdf (v0.4.116), lost-png (v0.4.117), lost-wav (v0.4.118), lost-jpg (v0.4.119), sdd_workspace.py / task_brief.py / task_start.py / task_done.py / sdd_review_pack.py (v0.4.120), work_order.py validate_tasks / reject-no-tasks / Task-N (v0.4.121), claim_audit.py (v0.4.122), quarantine.py (v0.4.123), critique.py --reject-incomplete-critique / eight-count / Checked (v0.4.124), verdict.py --reject-hidden-breach / --check-verdict / Breach Register (v0.4.125), finish.py --reject-red-suite / --require-green / --check-suite (v0.4.126), grill.py --reject-no-path / --reject-stage-skip / --reject-impl-before-approval / --check-path / PATH_AND_STAGE_BEFORE_IMPL (v0.4.127), diagnose.py --reject-no-report / --check-report / CITE_OR_FAIL_REPORT / diagnose-report-skeleton (v0.4.128), queue.py --reject-multi-wip / --check-wip / REJECT MULTI WIP / queue-reject-multi-wip (v0.4.129), consent.py --reject-no-consent / --check-consent / REJECT NO CONSENT / steal-consent (v0.4.130), heal_verify.py --reject-no-triad / --reject-no-postmortem / --check-heal / TRIAD_THEN_POSTMORTEM / heal-and-verify (v0.4.131), review_pack.py --reject-unisolated / --reject-author-diary / --check-isolation / hetero-critique-isolation (v0.4.132)., context.py / md_graph.py / reject-no-graph / thoughttrail-super-context (v0.4.133).

## Claims

| Claim | Status | Evidence |
|---|---|---|
| sot add-plugin clones mirror | TESTED | eval sot-artifact-sync |
| sot sync fetches tip | TESTED | eval sot-artifact-sync |
| artifacts sync materializes repos/ | TESTED | eval sot-artifact-sync |
| --reject-no-graph exit ≠0 | TESTED | eval thoughttrail-super-context HARD-GATE section |
| --reject-no-trail exit ≠0 | TESTED | eval thoughttrail-super-context HARD-GATE section |
| --check-context rejects missing graph/L0 | TESTED | evals/fixtures/thoughttrail-super-context/* |
| version 0.4.134 lockstep | TESTED | plugin / marketplace / SKILL / CHANGELOG |
| version 0.4.133 lockstep | TESTED | retained prior |
| version 0.4.132 lockstep | TESTED | retained prior |

## Honesty

| Claim | Status | Evidence |
|---|---|---|
| Live defect-rate vs Superpowers | UNVERIFIABLE | no three-vendor third-repo bake-off run |
