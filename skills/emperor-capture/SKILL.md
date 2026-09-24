---
name: emperor-capture
description: >-
  Emperor Time — CAPTURE / Chain Jail. Hunt, adapt, or author a missing skill,
  then pin, get consent, trial, register. Use when a needed capability is
  absent from this harness. Never bind an unpinned web skill.
license: MIT
metadata:
  version: 0.3.0
  chain: chain-jail
---

# Emperor Capture (Chain Jail wrapper)

1. Read `chains/chain-jail/SKILL.md` → `absence-check.md` first.
2. Hunt / adapt / author per router.
3. **Pin + consent + trial are mandatory** before the captured skill may fire:
   read `chains/chain-jail/pin-and-consent.md` then `trial-and-register.md`.
4. Captured skills live in `.emperor/captured-skills/` with provenance headers.
5. A captured skill that fails trial stays quarantined. Using it is a Vow of
   Evidence + Vow of Consent breach.
