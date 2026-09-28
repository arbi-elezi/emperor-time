Fixtures for finish suite-green HARD-GATE (`scripts/lib/finish.py`).

- `task-ok/` — DONE probes PASS → `--require-green` prints MENU
- `task-red/` — DONE probes FAIL → `--require-green` refuses MENU
- `task-no-done/` — no DONE.md → `--require-green` refuses (no suite evidence)
