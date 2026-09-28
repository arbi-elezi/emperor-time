# Boot probe — lost-alw / HELLO.ALW

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~02:27 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | Awe **2026-05 Version** (built from https://github.com/glynawe/awe) |
| Binary | `/usr/local/bin/awe` |
| Reported | `2026-05 Version` (`/tmp/awe/VERSION` at build) |
| Install | `make build && sudo make install` on this box (needs ocaml-nox, libgc-dev, python3-markdown) |

Probe used `awe` (Awe 2026-05) to compile an Algol W program with
standard `WRITE` to an executable and run it. Identify fossils use
`*.alw` (not `*.a60` / `*.a68` / `*.alg` — those fossils belong to other
Algol-family leaves). Prefer `awe` / `algolw` / `algol-w` / `.alw` /
space-intent `algol w`; bare English token `write` alone is **refused**
as a route tag. Do not commit generated `.c` or linked binaries from the
probe.

## Commands (VERIFIED)

Working directory for run: fixture dir (or any dir with the source).

```text
$ cat /tmp/awe/VERSION
2026-05 Version

$ awe HELLO.ALW -o HELLO
# exit 0

$ ./HELLO
EMPEROR-TIME-ALW-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Algol W fossil named `HELLO.ALW` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-alw` prints `1 *.alw` |
| Compiles under Awe 2026-05 | VERIFIED | `awe HELLO.ALW -o HELLO` exit 0 |
| Runs and prints known string | VERIFIED | stdout is `EMPEROR-TIME-ALW-PROBE-OK` |
| Dialect is a specific June 1972 full Language Description claim beyond WRITE | CONJECTURE | No IFIP/Stanford jury; Awe subset `WRITE` program only |
| Would run under period OS/360 ALGOL W on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of the full June 1972 procedure set
  (deferred; pin is Awe SYNOPSIS / EXAMPLES `WRITE` —
  see `references/archaeology-algolw-manual.md`).
- No ALGOL 60 / Algol 68 claim (different language family leaves at
  `lost-a60` / `lost-a68`).
- No claim on `*.a60` / `*.a68` / `*.alg` fossil naming for this leaf
  (shared Algol-family culture; identify fossil for Algol W here is
  `*.alw` only).
