# Boot probe — lost-fs / HELLO.FS

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~00:09 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `pforth` **1:2.0.1-1** (Debian trixie) |
| Binary | `/usr/bin/pforth` |
| Reported | `PForth V2.0.0, LE/64, built Jan  9 2023 23:55:24 (static)` |
| Install | `sudo apt-get update && sudo apt-get install -y pforth` → exit **0** |

Gforth / SwiftForth / VFX were **not** in apt on this box (`gforth` package
missing). Probe used pForth 2.0.0 on Linux because that is what can actually
INCLUDE+run on this host. Uppercase `HELLO.FS` is accepted as a source
filename; that is documented pForth include culture, not a probe failure.

## Commands (VERIFIED)

Working directory for include/run: `/tmp/forth-probe` (copy of `HELLO.FS`;
no dictionary / binary committed).

```text
$ pforth  # banner
PForth V2.0.0, LE/64, built Jan  9 2023 23:55:24 (static)
…

$ pforth -q HELLO.FS
EMPEROR-TIME-FORTH-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Forth fossil named `HELLO.FS` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-fs` prints `1 *.fs` |
| Runs under pForth 2.0.0 (`-q` include) | VERIFIED | `pforth -q HELLO.FS` exit 0 |
| Prints known string | VERIFIED | stdout is `EMPEROR-TIME-FORTH-PROBE-OK` |
| Dialect is ANS Forth / Forth-2012 specifically | CONJECTURE | No Forth-2012 jury PDF; `."` / `CR` subset only |
| Would run under period FIG / vendor Forth on original media | UNVERIFIABLE here | No FIG / SwiftForth / period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of a purchased Forth-2012 clause book (deferred; pin is
  pForth README How to Run — see `references/archaeology-forth-manual.md`).
- No Gforth / SwiftForth / VFX compile.
- No CREATE/DOES> / vocabulary / block-file claim.
