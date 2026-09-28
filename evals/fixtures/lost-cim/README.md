# lost-cim fixture

Synthetic lost Simula tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, `evals/fixtures/lost-a68/`,
`evals/fixtures/lost-a60/`, `evals/fixtures/lost-alw/`,
`evals/fixtures/lost-icn/`, `evals/fixtures/lost-obn/`,
and `evals/fixtures/lost-sno/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.SIM` | DOS-era 8.3 caps filename; `OutText` / `OutImage` prints `EMPEROR-TIME-CIM-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Simula compiler runs)

**Named era+dialect from evidence alone:**

- Extension `.SIM` / `.sim` + 8.3 uppercase name → Simula culture
  (GNU Cim / Portable Simula / Simula Standard family consuming the same
  `OutText` / `OutImage` / `BEGIN`…`END` surface).
- Source uses only `OutText("…")` / `OutImage` — dialect-honest (print
  probe, not a full Class / Simulation / Simset claim).
- No `CLASS`, no `PROCESS`, no `Simset` — deliberately minimal.
- Fossils deliberately use `*.sim` only (not `*.cim` attribute-archive
  culture).

Until `cim` / Portable Simula / another Simula implementation runs against
this file, the dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running Simula
compiler or emulator trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-cim
# or: bash scripts/identify.sh evals/fixtures/lost-cim
```
