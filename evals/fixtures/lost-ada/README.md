# lost-ada fixture

Synthetic lost Ada tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`, and
`evals/fixtures/lost-vhd/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.ADB` | DOS-era 8.3 caps filename; prints `EMPEROR-TIME-ADA-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a compiler runs)

**Named era+dialect from evidence alone:**

- Extension `.ADB` / `.adb` + 8.3 uppercase name → Ada body culture
  (ISO/IEC 8652 family *or* GNAT consuming the same procedure body surface).
- Source uses only `with Ada.Text_IO` / `procedure` / `Put_Line` —
  Ada 95-compatible enough that GNAT, and other Ada compilers accepting
  Text_IO Hello World, would both accept this subset.
- No package spec (`.ads`), no generics, no tasking — deliberately
  dialect-honest (library-level procedure body probe, not an Ada 2012 claim).

Until `gnatmake` / another Ada compiler runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running compile or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-ada
# or: bash scripts/identify.sh evals/fixtures/lost-ada
```
