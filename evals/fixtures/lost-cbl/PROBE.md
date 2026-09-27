# Boot probe — lost-cbl / HELLO.CBL

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-27 ~17:37 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `gnucobol` meta → `gnucobol3` **3.2-3** + `libcob4t64` **3.2-3** (Debian trixie) |
| Binary | `/usr/bin/cobc` |
| Reported | `cobc --version` → `cobc (GnuCOBOL) 3.2.0` |
| Install | `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y gnucobol` → exit **0** |

IBM Enterprise COBOL / Micro Focus / AcuCOBOL / DOS COBOL were **not** present. Probe used GnuCOBOL 3.2 on Linux because that is what can actually compile+link+run on this box.

## Commands (VERIFIED)

Working directory for compile/run: `/tmp/cbl-probe` (copy of `HELLO.CBL`; binary not committed).

```text
$ cobc --version
cobc (GnuCOBOL) 3.2.0
…

$ cobc -x -o HELLO HELLO.CBL
# exit 0 (may warn about libxml version mismatch — non-fatal)

$ ./HELLO
EMPEROR-TIME-CBL-PROBE-OK
# exit 0

$ file HELLO
HELLO: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, …
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is COBOL fossil named `HELLO.CBL` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-cbl` prints `1 *.cbl` |
| Compiles under GnuCOBOL 3.2.0 fixed format | VERIFIED | `cobc -x -o HELLO HELLO.CBL` exit 0 |
| Prints known string | VERIFIED | stdout exactly `EMPEROR-TIME-CBL-PROBE-OK` |
| Dialect is IBM Enterprise / Micro Focus / ANS74 specifically | CONJECTURE | No IBM/MF compiler; no obsolete AUTHOR paragraphs exercised; ANSI-85-ish subset only |
| Would run under DOS / mainframe COBOL on original media | UNVERIFIABLE here | No mainframe / DOS COBOL run in this session |

## Not done (honest gaps)

- No Jail-hunt of a contemporaneous IBM VS COBOL II manual heading (deferred; pin is GnuCOBOL Programmer’s Guide §4 — see `references/archaeology-cobol-manual.md`).
- No Micro Focus / IBM Enterprise compile.
- No free-format (`-free`) rewrite of the same probe.
- No port to Python (forbidden by doctrine).
