# lost-roff fixture

Synthetic lost roff / nroff / groff tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-sed/`, `evals/fixtures/lost-m4/`,
`evals/fixtures/lost-ed/`, `evals/fixtures/lost-make/`,
`evals/fixtures/lost-dc/`, `evals/fixtures/lost-lex/`,
and `evals/fixtures/lost-yacc/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.ROFF` | DOS-era 8.3 caps filename; groff `-Tascii` prints `EMPEROR-TIME-ROFF-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a roff system runs)

**Named era+dialect from evidence alone:**

- Extension `.ROFF` / `.roff` + 8.3 uppercase name → roff document culture
  (GNU troff / POSIX nroff / classical troff consumers of the same
  request/escape surface).
- Source uses only a trivial no-fill text block — dialect-honest (formatter
  invoke probe, not a full ms/me/mm/man macro package claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.roff`.

Until `groff` / `nroff` / another roff formatter runs against this
file, the dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Markdown or Python. Understanding is a running
roff formatter. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-roff
# or: bash scripts/identify.sh evals/fixtures/lost-roff
```
