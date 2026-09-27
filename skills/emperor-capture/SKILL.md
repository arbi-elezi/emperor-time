---
name: emperor-capture
description: >-
  Emperor Time — CAPTURE / Chain Jail. Hunt, adapt, or author a missing skill,
  then pin, get consent, trial, register. Use when a needed capability is
  absent from this harness. Never bind an unpinned web skill.
license: MIT
metadata:
  version: 0.4.13
  chain: chain-jail
---

# Emperor Capture (Chain Jail wrapper)

1. Read `chains/chain-jail/SKILL.md` → `absence-check.md` first.
2. Hunt / adapt / author per router.
3. **Authoring iron law:** before writing or substantively editing a skill,
   open `chains/chain-jail/authoring-checklist.md` and/or run
   `scripts/emperor author` (HARD-GATE: no skill body without a failing
   baseline). Jumping to prose → `scripts/emperor author --reject-untested`.
4. **Testing-skills companion:** before trial/register of a discipline skill,
   open `chains/chain-jail/testing-skills.md` and/or run
   `scripts/emperor skill-test` (HARD-GATE: combined pressure + watch baseline
   FAIL). Academic-only → `scripts/emperor skill-test --reject-academic-only`.
5. **Pin + consent + trial are mandatory** before the captured skill may fire:
   read `chains/chain-jail/pin-and-consent.md` then `trial-and-register.md`.
6. Captured skills live in `.emperor/captured-skills/` with provenance headers.
7. A captured skill that fails trial stays quarantined. Using it is a Vow of
   Evidence + Vow of Consent breach.
