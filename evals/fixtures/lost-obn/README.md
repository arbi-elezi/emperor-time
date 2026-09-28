# lost-obn fixture

Synthetic lost Oberon tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, `evals/fixtures/lost-a68/`,
`evals/fixtures/lost-a60/`, `evals/fixtures/lost-alw/`, and
`evals/fixtures/lost-icn/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.OBN` | DOS-era 8.3 caps filename; `Out.String` prints `EMPEROR-TIME-OBN-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an Oberon compiler runs)

**Named era+dialect from evidence alone:**

- Extension `.OBN` / `.obn` + 8.3 uppercase name → Oberon culture
  (Vishap / Ofront / Oakwood Oberon-2 family consuming the same `Out`
  / `MODULE` surface). Distinct from Modula-2 `*.mod` (lost-mod).
- Source uses only `MODULE` / `IMPORT Out` / `Out.String` / `Out.Ln` /
  `END` — dialect-honest (string-print probe, not a full Oberon System
  Texts.Writer claim).
- No Oberon.Log, no Texts.Writer, no type extension demo — deliberately
  minimal.
- Fossils deliberately use `*.obn` only so identify does not collide
  with Modula-2 `*.mod` (case-insensitive fossil match).

Until `voc` / another Oberon implementation runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `voc`
executable or emulator trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-obn
# or: bash scripts/identify.sh evals/fixtures/lost-obn
```
