# lost-fs fixture

Synthetic lost Forth tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, and `evals/fixtures/lost-ada/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.FS` | DOS-era 8.3 caps filename; prints `EMPEROR-TIME-FORTH-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Forth runs)

**Named era+dialect from evidence alone:**

- Extension `.FS` / `.fs` / `.fth` / `.4th` + 8.3 uppercase name → Forth
  source culture (ANS Forth / Forth-2012 family *or* pForth / Gforth consuming
  the same `."` / `CR` surface).
- Source uses only `."` (dot-quote) and `CR` — ANS Core-compatible enough that
  pForth, Gforth, and other ANS-like Forths accepting string print would both
  accept this subset.
- No CREATE/DOES>, no vocabularies, no block files — deliberately
  dialect-honest (string-print probe, not a Forth-2012 claim).

Until `pforth` / `gforth` / another Forth runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running include or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-fs
# or: bash scripts/identify.sh evals/fixtures/lost-fs
```
