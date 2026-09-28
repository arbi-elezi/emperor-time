# lost-bas fixture

Synthetic lost BASIC tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, `evals/fixtures/lost-a68/`,
`evals/fixtures/lost-a60/`, `evals/fixtures/lost-alw/`,
`evals/fixtures/lost-icn/`, `evals/fixtures/lost-obn/`,
`evals/fixtures/lost-sno/`, `evals/fixtures/lost-cim/`,
`evals/fixtures/lost-apl/`, `evals/fixtures/lost-bcpl/`,
`evals/fixtures/lost-pli/`, `evals/fixtures/lost-st/`,
and `evals/fixtures/lost-ps/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.BAS` | DOS-era 8.3 caps filename; `PRINT` / `SYSTEM` prints `EMPEROR-TIME-BAS-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a BASIC system runs)

**Named era+dialect from evidence alone:**

- Extension `.BAS` / `.bas` + 8.3 uppercase name → BASIC file culture
  (Bywater / Microsoft-family consumers of the same `PRINT` /
  `SYSTEM` surface).
- Source uses only `PRINT` + `SYSTEM` — dialect-honest (print probe,
  not a full GW-BASIC / QuickBASIC / Visual Basic / BBC / FreeBASIC
  claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.bas` only.

Until `bwbasic` / another BASIC interpreter runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running BASIC
interpreter. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-bas
# or: bash scripts/identify.sh evals/fixtures/lost-bas
```
