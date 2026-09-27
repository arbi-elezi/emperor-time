# lost-cbl fixture

Synthetic lost COBOL tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/` and `evals/fixtures/lost-asm/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.CBL` | DOS-era 8.3 caps filename; prints `EMPEROR-TIME-CBL-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a compiler runs)

**Named era+dialect from evidence alone:**

- Extension `.CBL` + 8.3 uppercase name → late-DOS / mainframe-adjacent COBOL source culture (ANSI COBOL-85 / IBM-adjacent *or* GnuCOBOL consuming the same fixed-format surface).
- Source uses only `IDENTIFICATION DIVISION` / `PROGRAM-ID` / `PROCEDURE DIVISION` / `DISPLAY` / `STOP RUN` — ANSI-85-compatible enough that GnuCOBOL (`cobc`) and period IBM/Micro Focus compilers would both accept this subset.
- Fixed format (Area A/B columns), not free-format `-free`. No `SCREEN SECTION`, no OO COBOL, no `GOBACK` — deliberately dialect-honest.

Until `cobc` / IBM Enterprise COBOL / Micro Focus (or an emulator) runs against this file, the dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running binary or emulator trace.
See `references/archaeology.md` and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-cbl
# or: bash scripts/identify.sh evals/fixtures/lost-cbl
```
