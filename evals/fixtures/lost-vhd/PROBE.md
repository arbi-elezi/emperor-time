# Boot probe — lost-vhd / HELLO.VHD

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-27 ~21:02 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `ghdl` **5.0.1+dfsg-1+b1** → `ghdl-common` **5.0.1+dfsg-1+b1** + `ghdl-mcode` **5.0.1+dfsg-1+b1** (Debian trixie) |
| Binary | `/usr/bin/ghdl` |
| Reported | `ghdl --version` → `GHDL 5.0.1 (Debian 5.0.1+dfsg-1+b1) [Dunoon edition]` / mcode JIT |
| Install | `sudo apt-get update && sudo apt-get install -y ghdl` → exit **0** |

ModelSim / Questa / Vivado / NVC were **not** present. Probe used GHDL 5.0.1
mcode on Linux because that is what can actually analyze+elaborate+run on this
box. mcode elaborates in memory (no separate ELF); that is documented GHDL
behavior, not a probe failure.

## Commands (VERIFIED)

Working directory for analyze/run: `/tmp/vhd-probe` (copy of `HELLO.VHD`;
work library not committed).

```text
$ ghdl --version
GHDL 5.0.1 (Debian 5.0.1+dfsg-1+b1) [Dunoon edition]
…

$ ghdl -a HELLO.VHD
# exit 0

$ ghdl -e hello
# exit 0 (mcode: elaborates; no ELF artifact)

$ ghdl -r hello
HELLO.VHD:11:5:@0ms:(report note): EMPEROR-TIME-VHD-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is VHDL fossil named `HELLO.VHD` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-vhd` prints `1 *.vhd` |
| Analyzes under GHDL 5.0.1 | VERIFIED | `ghdl -a HELLO.VHD` exit 0 |
| Runs and prints known string | VERIFIED | `ghdl -r hello` stdout contains `EMPEROR-TIME-VHD-PROBE-OK` |
| Dialect is IEEE 1076-1993 / 2008 / Vivado specifically | CONJECTURE | No IEEE jury PDF; no ModelSim/Vivado; entity/architecture/`report` subset only |
| Would run under period vendor sim on original media | UNVERIFIABLE here | No ModelSim / Vivado / period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of a purchased IEEE Std 1076 clause (deferred; pin is GHDL
  Invoking GHDL Analysis/Elaboration/Run — see
  `references/archaeology-vhdl-manual.md`).
- No ModelSim / Questa / Vivado / NVC compile.
- No `std_logic` / synthesis / waveform GHW claim.
- No port to Python (forbidden by doctrine).
