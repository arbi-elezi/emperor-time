# Scope guard — creep and drain

Load when G1 exists and any file is about to change, and again at G4.

## Creep

A hunk that does not map to a G1 line or a DONE probe is creep.
Record `SCOPE-CREEP: <path> <why-tempted> <rejected|widened-with-client>`.
Widening G1 after BUILD started requires a new G1 sentence and a new DONE probe.
Silent widening is heresy.

## Drain

Deleting or softening a G1 line because a probe failed is drain.
Fix the product or quote the honest failure. Do not edit DONE.md to match the
failure unless the client changed the ask (quote them).

## Easy path tells

- skipped the failing file, tested a neighbor
- `# TODO` left on the acceptance path
- captured a whole foreign skill "in case"
- marked done because the diff compiles
