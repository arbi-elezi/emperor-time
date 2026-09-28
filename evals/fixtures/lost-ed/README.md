# lost-ed fixture

Synthetic lost ed tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-scm/`, `evals/fixtures/lost-awk/`,
`evals/fixtures/lost-sed/`, and `evals/fixtures/lost-m4/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.ED` | DOS-era 8.3 caps filename; `a`/`,p`/`Q` prints `EMPEROR-TIME-ED-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an ed system runs)

**Named era+dialect from evidence alone:**

- Extension `.ED` / `.ed` + 8.3 uppercase name → ed script file culture
  (GNU ed / other ed consumers of the same `a`/`,p`/`Q`
  surface).
- Source uses only append + print + quit — dialect-honest (print probe,
  not a full POSIX ed / BSD ed / Plan 9 ed
  claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.ed` only.

Until `ed` / another line editor runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running ed
system. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-ed
# or: bash scripts/identify.sh evals/fixtures/lost-ed
```
