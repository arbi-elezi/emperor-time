# Task Ledger — jail-incomplete-pin

## G0
- Origin: eval fixture
- Task: prove URL+hash without peers fails
- pin-and-consent incomplete

## G1 Acceptance criteria
1. pin_consent.py fails incomplete pin

## Out of scope
- none

## G2
Size: trivial

## G3
Build: fixtures

## G4
- Verdict: expect FAIL

## Pin theater
source-url: https://example.com/skills/demo-skill/SKILL.md
source-hash: sha256:abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789

JAIL-CONSENT: client said "yes, bind demo-skill" naming this captured skill.
