# lost-awk fixture

Synthetic lost AWK tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-ps/`, `evals/fixtures/lost-bas/`,
and `evals/fixtures/lost-scm/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.AWK` | DOS-era 8.3 caps filename; `BEGIN` / `print` prints `EMPEROR-TIME-AWK-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an AWK system runs)

**Named era+dialect from evidence alone:**

- Extension `.AWK` / `.awk` + 8.3 uppercase name → AWK file culture
  (gawk / other AWK consumers of the same `BEGIN` /
  `print` surface).
- Source uses only `BEGIN` + `print` — dialect-honest (print probe,
  not a full POSIX awk / nawk / mawk / BusyBox / One True Awk
  claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.awk` only.

Until `gawk` / another AWK interpreter runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running AWK
system. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-awk
# or: bash scripts/identify.sh evals/fixtures/lost-awk
```
