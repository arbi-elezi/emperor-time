# Receipt + PR-body tip hygiene

Standing checklist for SWEs. After every rebase or tip move, refresh
**receipt SHAs** and the **PR-body base/head tip** in the same amend
**before** pinging PO or QA. Stops receipt lag (obsolete SHAs left in
CONTEXT / BEFORE / AFTER / DOGFOOD / MATRIX / SUMMARY / claim) and stale
PR-base prose after rebase onto a newer main.

## Before PO/QA ping

1. Record the new **head tip SHA** and **base tip SHA** (origin/main after
   rebase).
2. Refresh every receipt pack cite in CONTEXT, BEFORE, AFTER, DOGFOOD,
   MATRIX, SUMMARY, and claim. Grep for obsolete short SHAs and replace
   them.
3. Update the PR body: base tip, head tip, and any "rebased onto" note
   (`gh pr edit` or the web UI).
4. Land receipt + PR-body refreshes in the **same amend** / force-with-lease
   push as the rebase. Do not ping on a stale receipt pack plus stale PR
   prose.
5. Soft minors already ACCEPTed may stay waived. Still fix local receipts
   when cheap.

## Why tip-local

`/workspace/field-receipts/` sits outside the tip tree. Strangers cloning
emperor-time never see it. This page lives under `references/` next to
kill-hold and graph-midflash so the checklist travels with the tip.

## Pointers

- QA smoke receipt step: `adapters/opencode/QA-SMOKE.md` (receipt bullet).
- Scope refuse process (not this page): `references/kill-hold.md`.
