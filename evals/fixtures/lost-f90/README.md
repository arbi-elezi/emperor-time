# lost-f90 fixture

Synthetic lost Fortran 90 tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`, and
`evals/fixtures/lost-cbl/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.F90` | DOS-era 8.3 caps filename; prints `EMPEROR-TIME-F90-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a compiler runs)

**Named era+dialect from evidence alone:**

- Extension `.F90` + 8.3 uppercase name → Fortran 90 free-form source culture
  (ISO/IEC 1539 family *or* GNU Fortran consuming the same free-form surface).
- Source uses only `PROGRAM` / `WRITE(*,'(A)')` / `END PROGRAM` — F90-compatible
  enough that `gfortran`, classic f90, and period free-form compilers would both
  accept this subset.
- Free form (not fixed-form columns 1–72). No `IMPLICIT NONE` required for this
  tiny probe, no modules, no coarrays, no OpenMP — deliberately dialect-honest.

Until `gfortran` / ifort / nagfor (or an emulator) runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running binary or emulator trace.
See `references/archaeology.md` and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-f90
# or: bash scripts/identify.sh evals/fixtures/lost-f90
```
