# lost-tcl fixture

Synthetic lost Tcl tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`, and
`evals/fixtures/lost-prolog/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.TCL` | DOS-era 8.3 caps filename; prints `EMPEROR-TIME-TCL-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Tcl runs)

**Named era+dialect from evidence alone:**

- Extension `.TCL` / `.tcl` / `.tk` + 8.3 uppercase name → Tcl / Tk script
  culture (Tcl 8.x family *or* any `tclsh` / `wish` consuming the same
  `puts` surface).
- Source uses only `puts` with a double-quoted string — dialect-honest
  (string-print probe, not a Tk GUI or package require claim).
- No `package require`, no Tk widgets, no Expect — deliberately minimal.

Until `tclsh` / another Tcl runs against this file, the dialect label stays
**CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `tclsh` or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-tcl
# or: bash scripts/identify.sh evals/fixtures/lost-tcl
```
