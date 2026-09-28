# lost-a60 fixture

Synthetic lost ALGOL 60 tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, and `evals/fixtures/lost-a68/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.A60` | DOS-era 8.3 caps filename; `outstring` prints `EMPEROR-TIME-A60-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an ALGOL 60 translator runs)

**Named era+dialect from evidence alone:**

- Extension `.A60` / `.a60` + 8.3 uppercase name → ALGOL 60 culture
  (GNU MARST / Algol-to-C family *or* any IFIP ALGOL 60 subset consuming
  the same `outstring` surface).
- Source uses only `begin` / `outstring` / `end` — dialect-honest
  (string-print probe, not a full block / own / switch claim).
- No `own`, no `switch`, no call-by-name gymnastics — deliberately minimal.
- Fossils deliberately use `*.a60` (not `*.alg`) so identify does not
  collide with the Algol 68 leaf's `*.alg` fossil.

Until `marst` / another ALGOL 60 implementation runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `marst` + `gcc`
`-lalgol` binary chain or emulator trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-a60
# or: bash scripts/identify.sh evals/fixtures/lost-a60
```
