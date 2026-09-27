# Boot probe — lost-f90 / HELLO.F90

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-27 ~17:51 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `gfortran` meta **4:14.2.0-1** → `gfortran-14` **14.2.0-19** + `libgfortran-14-dev` **14.2.0-19** (Debian trixie) |
| Binary | `/usr/bin/gfortran` |
| Reported | `gfortran --version` → `GNU Fortran (Debian 14.2.0-19) 14.2.0` |
| Install | `sudo apt-get update && sudo apt-get install -y gfortran` → exit **0** |

Intel ifort / ifx / NAG / classic f90 / Lahey were **not** present. Probe used
GNU Fortran 14.2 on Linux because that is what can actually compile+link+run on
this box.

## Commands (VERIFIED)

Working directory for compile/run: `/tmp/f90-probe` (copy of `HELLO.F90`; binary not committed).

```text
$ gfortran --version
GNU Fortran (Debian 14.2.0-19) 14.2.0
…

$ gfortran -o HELLO HELLO.F90
# exit 0

$ ./HELLO
EMPEROR-TIME-F90-PROBE-OK
# exit 0

$ file HELLO
HELLO: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, …
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Fortran fossil named `HELLO.F90` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-f90` prints `1 *.f90` |
| Compiles under GNU Fortran 14.2 free form | VERIFIED | `gfortran -o HELLO HELLO.F90` exit 0 |
| Prints known string | VERIFIED | stdout exactly `EMPEROR-TIME-F90-PROBE-OK` |
| Dialect is ISO 1539:1991 F90 / F95 / ifort specifically | CONJECTURE | No ISO jury; no ifort/nagfor; free-form F90-ish subset only |
| Would run under period DOS / vendor f90 on original media | UNVERIFIABLE here | No DOS / vendor f90 run in this session |

## Not done (honest gaps)

- No Jail-hunt of a contemporaneous ISO 1539:1991 purchased PDF clause (deferred; pin is GNU Fortran §2.2 free-form dialect — see `references/archaeology-fortran-manual.md`).
- No ifort / NAG / classic f90 compile.
- No fixed-form `.f` / `.for` rewrite of the same probe.
- No port to Python (forbidden by doctrine).
