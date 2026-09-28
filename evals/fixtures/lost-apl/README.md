# lost-apl fixture

Synthetic lost APL tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, `evals/fixtures/lost-a68/`,
`evals/fixtures/lost-a60/`, `evals/fixtures/lost-alw/`,
`evals/fixtures/lost-icn/`, `evals/fixtures/lost-obn/`,
`evals/fixtures/lost-sno/`, and `evals/fixtures/lost-cim/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.APL` | DOS-era 8.3 caps filename; `⎕←` prints `EMPEROR-TIME-APL-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an APL interpreter runs)

**Named era+dialect from evidence alone:**

- Extension `.APL` / `.apl` + 8.3 uppercase name → APL culture
  (GNU APL / ISO 13751 Extended family consuming the same `⎕←` print
  surface).
- Source uses only `⎕←'…'` — dialect-honest (print probe, not a full
  nested-array / ⎕SQL / ⎕FFT claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.apl` only (not bare English keywords).

Until `apl` / another APL implementation runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running APL
interpreter or emulator trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-apl
# or: bash scripts/identify.sh evals/fixtures/lost-apl
```
