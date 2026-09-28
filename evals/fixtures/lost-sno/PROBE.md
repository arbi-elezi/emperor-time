# Boot probe — lost-sno / HELLO.SNO

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~03:13 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | CSNOBOL4B (**snobol4**) from https://ftp.regressive.org/snobol/snobol4-2.3.4.tar.gz |
| Binary | `/tmp/toolchain-probe/snobol4-2.3.4/snobol4` (local `./configure && make`) |
| Reported | `CSNOBOL4B version 2.3.4 (April 24, 2026)` |
| Install | `curl -fsSL -o snobol4-2.3.4.tar.gz https://ftp.regressive.org/snobol/snobol4-2.3.4.tar.gz && tar xzf snobol4-2.3.4.tar.gz && cd snobol4-2.3.4 && ./configure --add-opt=-O0 && make` then `export PATH="$PWD:$PATH"` |

Probe used `snobol4 -b` on a Macro SNOBOL4 source that assigns to the
default `OUTPUT` variable (unit 6 / standard output) then `END`.
Identify fossils use `*.sno` only. Prefer `snobol4` / `snobol` /
`csnobol4` / `.sno`; bare English token `output` alone is **refused** as
a route tag (`OUTPUT` keyword / English collision class). Do not commit
generated listing files from the probe.

## Commands (VERIFIED)

Working directory for run: fixture dir (or any dir with the source).

```text
$ snobol4 -v
CSNOBOL4B version 2.3.4 (April 24, 2026)

$ snobol4 -b HELLO.SNO
EMPEROR-TIME-SNO-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is SNOBOL fossil named `HELLO.SNO` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-sno` prints `1 *.sno` |
| Runs under CSNOBOL4B 2.3.4 (`snobol4 -b`) | VERIFIED | `snobol4 -b HELLO.SNO` exit 0 |
| Prints known string | VERIFIED | stdout is `EMPEROR-TIME-SNO-PROBE-OK` |
| Dialect is a specific Griswold book printing / SPITBOL / SITBOL full claim | CONJECTURE | No SPITBOL/SITBOL jury beyond default OUTPUT; Macro SNOBOL4 OUTPUT subset only |
| Would run under period Bell Labs Macro SNOBOL4 on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of full Griswold *The SNOBOL4 Programming Language* /
  string-pattern chapter (deferred; pin is CSNOBOL4 snobol4cmd SYNOPSIS —
  see `references/archaeology-snobol-manual.md`).
- No SPITBOL / SITBOL / Catspaw SNOBOL4+ claim beyond CSNOBOL4 Macro
  OUTPUT.
- No bare `output` route tag (OUTPUT keyword English collision).
