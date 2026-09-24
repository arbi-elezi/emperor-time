# Swarm emulate — fan-out when the host has no swarm button

Native swarm (Kimi `AgentSwarm` / `/swarm`, UltraCode swarm, similar) is preferred
when present and consented. This aspect is the rite when that button is missing.

## Detect

- Kimi: `/swarm` or AgentSwarm tool exists → use it, then quarantine each item.
- Else: emulate.

## Emulation (Steal + worktrees)

1. Split G2 work-order into N **disjoint** SCOPE lists (no shared writable file).
2. One worker prompt per item (`dispatch.md` anatomy). Same scaffold for all.
3. Launch in parallel:
   - separate git worktrees (`scripts/worktree.sh <id>-<n>`), or
   - separate processes (`claude -p`, `codex exec`, `kimi -p`) with timeouts.
4. Bound N. Default cap 4 unless CI env sets `EMPEROR_SWARM_N`.
5. Collect `.emperor/runs/<task>/swarm-<n>/`. Each out.txt is CONJECTURE.
6. Synthesize yourself. A worker does not merge siblings.
7. One retry per item with a changed prompt. Second fail → you do that item.

Lack of vendor swarm is not an excuse to serialize disjoint work, and not an
excuse to yolo 30 agents into one dirty tree.
