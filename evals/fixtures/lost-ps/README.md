# lost-ps fixture

Synthetic lost PostScript tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-pli/`, and `evals/fixtures/lost-st/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.PS` | DOS-era 8.3 caps filename; `%!PS` + `print` / `flush` / `quit` prints `EMPEROR-TIME-PS-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a PostScript system runs)

**Named era+dialect from evidence alone:**

- Extension `.PS` / `.ps` + 8.3 uppercase name → PostScript file culture
  (Adobe / Ghostscript family consuming the same `print` / `flush` /
  `quit` surface).
- Source uses only `%!PS` header + `print` / `flush` / `quit` —
  dialect-honest (print probe, not a full Distiller / Level-3 RIP /
  printer-firmware claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.ps` + `*.eps` (EPS sister; not `*.ps1` —
  PowerShell collision).

Until `gs` / another PostScript interpreter runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running PostScript
interpreter or printer job trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-ps
# or: bash scripts/identify.sh evals/fixtures/lost-ps
```
