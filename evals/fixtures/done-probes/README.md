Fixtures for agent-defined DONE probes (Python core `scripts/lib/done.py`).

- `ok/` — probe/expect that must PASS → exit 0 + DONE OK
- `fail/` — probe/expect that must FAIL → exit non-zero
- `no-probes/` — DONE.md without probe: lines → exit non-zero
