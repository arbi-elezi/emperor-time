# lost-lisp fixture

Synthetic lost Common Lisp tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`, and
`evals/fixtures/lost-fs/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.LISP` | DOS-era 8.3 caps filename; prints `EMPEROR-TIME-LISP-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Lisp runs)

**Named era+dialect from evidence alone:**

- Extension `.LISP` / `.lisp` / `.lsp` / `.cl` + 8.3 uppercase name → Common
  Lisp / Lisp source culture (ANSI CL family *or* CLISP / SBCL consuming the
  same `FORMAT` surface).
- Source uses only `FORMAT` with `T` and `~%` — ANSI-compatible enough that
  CLISP, SBCL, and other ANSI-ish Common Lisps accepting FORMAT would both
  accept this subset.
- No macros, no packages, no CLOS, no ASDF — deliberately dialect-honest
  (string-print probe, not an ANSI CL year claim).

Until `clisp` / `sbcl` / another Common Lisp runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running load or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-lisp
# or: bash scripts/identify.sh evals/fixtures/lost-lisp
```
