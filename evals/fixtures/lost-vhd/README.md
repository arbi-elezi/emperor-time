# lost-vhd fixture

Synthetic lost VHDL tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, and `evals/fixtures/lost-f90/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.VHD` | DOS-era 8.3 caps filename; `report` prints `EMPEROR-TIME-VHD-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a simulator runs)

**Named era+dialect from evidence alone:**

- Extension `.VHD` / `.vhd` + 8.3 uppercase name → VHDL source culture
  (IEEE Std 1076 family *or* GHDL consuming the same entity/architecture surface).
- Source uses only `entity` / `architecture` / `process` / `report` / `wait` —
  VHDL-93-compatible enough that GHDL, ModelSim/Questa, and Vivado sim would
  both accept this subset.
- No `library IEEE`, no `std_logic`, no synthesis attributes — deliberately
  dialect-honest (simulation `report` probe, not an FPGA bitstream claim).

Until `ghdl` / ModelSim / Vivado (or an emulator) runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running simulation or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-vhd
# or: bash scripts/identify.sh evals/fixtures/lost-vhd
```
