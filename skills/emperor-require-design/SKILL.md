---
name: emperor-require-design
description: >-
  Emperor Time — REQUIRE + DESIGN. Write acceptance criteria and a fat work
  order a zero-context worker can execute. Use when planning, writing a spec,
  designing an approach, or before any implementation. Pairs with G1/G2.
license: MIT
metadata:
  version: 0.3.0
  chain: judgment-chain
---

# Emperor Require-Design (G1/G2 wrapper)

1. Confirm G0/G1 exist. If not, load `skills/emperor-scope/SKILL.md` first.
2. Read `references/work-order.md` then copy `templates/work-order.md` to
   `.emperor/tasks/<id>/work-order.md`.
3. Every non-trivial task step must include: real paths, exact commands,
   `Expected: FAIL` then `Expected: PASS` strings. No TBD.
4. Rejected alternative is mandatory (one line).
5. Run `scripts/gate.sh g2 <task-dir>` and quote the tail before BUILD.
6. Judgment on the design (does the work order match G1?) uses
   `chains/judgment-chain/SKILL.md` → `gatekeeping.md` only.
