# queue-reject-multi-wip fixtures

HARD-GATE: `scripts/lib/queue.py --reject-multi-wip` / `--check-wip`.

- `queue-multi-two.md` / `queue-multi-three.md` → fail (>1 active `[~]`)
- `queue-ok-one.md` / `queue-ok-zero.md` / `queue-ok-placeholder.md` → pass
- Placeholders never count as active WIP
