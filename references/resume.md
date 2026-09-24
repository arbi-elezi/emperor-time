# Resume / anti-rot

GSD wins long projects by putting state on disk and giving each phase a fresh
window. Emperor Time does the same with three files:

1. `.emperor/STATE.md` — from `templates/STATE.md`
2. `.emperor/tasks/<id>/ledger.md`
3. `.emperor/tasks/<id>/work-order.md`

On SessionStart or after compaction: read STATE.md first. Do not reload every
chain. Continue at the next unopened gate.
