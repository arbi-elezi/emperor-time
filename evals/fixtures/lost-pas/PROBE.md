# Boot probe — lost-pas / HELLO.PAS

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-27 ~12:03 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `fpc` / `fpc-3.2.2` **3.2.2+dfsg-46** (Debian trixie) |
| Binary | `/usr/bin/fpc` |
| Reported | `fpc -iV` → `3.2.2` ; `fpc -iW` → `3.2.2+dfsg-46` |
| Install | `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y fpc` → exit **0** |

Classic Turbo Pascal `tpc` was **not** present on this box. Probe used Free Pascal as the contemporaneous-enough ISO-compatible compiler for this subset (see README dialect CONJECTURE).

## Commands (VERIFIED)

Working directory for compile/run: `/tmp/pas-probe` (copy of `HELLO.PAS`; binary not committed).

```text
$ fpc -Miso HELLO.PAS
Free Pascal Compiler version 3.2.2+dfsg-46 [2025/02/08] for x86_64
Copyright (c) 1993-2021 by Florian Klaempfl and others
Target OS: Linux for x86-64
Compiling HELLO.PAS
Linking HELLO
7 lines compiled, 0.0 sec
# exit 0

$ ./HELLO
EMPEROR-TIME-PAS-PROBE-OK
# exit 0

$ fpc -oHELLO_default HELLO.PAS
# … same success; exit 0

$ ./HELLO_default
EMPEROR-TIME-PAS-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Pascal fossil named `HELLO.PAS` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-pas` prints `1 *.pas` |
| Compiles under Free Pascal 3.2.2 ISO mode | VERIFIED | `fpc -Miso HELLO.PAS` exit 0 |
| Prints known string | VERIFIED | stdout exactly `EMPEROR-TIME-PAS-PROBE-OK` |
| Dialect is Turbo Pascal 5.5 / 7.0 specifically | CONJECTURE | No `tpc`; no TP-only units exercised; ISO-ish subset only |
| Would run under DOS Turbo on original media | UNVERIFIABLE here | No DOS emulator / TPC run in this session |

## Not done (honest gaps)

- No Jail-hunt of a contemporaneous Turbo manual heading (deferred).
- No DOSBox / TPC boot.
- No port to Python (forbidden by doctrine).
