---
name: emperor-dispatch
description: >-
  Emperor Time — DISPATCH / Steal Chain. Consent-first enlistment of local
  CLIs (Claude Code, Kimi, Codex, Copilot, opencode, Ollama). Use when the user
  asks to use another agent, parallelize, or review via a different model.
license: MIT
metadata:
  version: 0.3.0
  chain: steal-chain
---

# Emperor Dispatch (Steal Chain wrapper)

1. Read `chains/steal-chain/SKILL.md` → one aspect
   (`consent-protocol.md` first unless consent is already on the ledger).
2. Dowse the machine (`scripts/dowse.sh` / `dowse.ps1`) if the roster is stale.
3. Client consents per agent per task (or a standing policy they stated).
4. Workers receive the **work order + named files**, never the author's diary.
5. Capture to `.emperor/runs/<task>/<agent>/` (`prompt.md`, `out.txt`, `meta.md`).
6. Output is CONJECTURE until Judgment + `scripts/gate.sh g4`.
7. Sign-in is the client's terminal. You never run interactive logins.
