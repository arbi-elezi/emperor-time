# Boot probe — lost-bas / HELLO.BAS

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~05:31 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Bywater BASIC** 2.20pl2-14 (`bwbasic` Debian package) |
| Binary | `/usr/bin/bwbasic` |
| Reported | `Bywater BASIC Interpreter/Shell, version 2.20 patch level 2` |
| Install | `apt-get install bwbasic` (Debian trixie) |

Probe used command-line file execution
(`bwbasic HELLO.BAS`)
on a minimal `PRINT` / `SYSTEM` source. Identify fossils
use `*.bas` only. Prefer `bwbasic` / `bywater` / `.bas`; bare English
`basic` is **refused** as a dedicated route tag (common-English collision).
Bare `print` is **refused** as a route tag (shared keyword across many
dialects). Do not claim a full Microsoft GW-BASIC / QuickBASIC / Visual
Basic / BBC BASIC / FreeBASIC recovery from a Bywater print probe.

## Commands (VERIFIED)

```text
$ dpkg -l bwbasic | awk '/^ii/ {print $2, $3}'
bwbasic 2.20pl2-14

$ bwbasic evals/fixtures/lost-bas/HELLO.BAS
Bywater BASIC Interpreter/Shell, version 2.20 patch level 2
Copyright (c) 1993, Ted A. Campbell
Copyright (c) 1995-1997, Jon B. Volkoff

EMPEROR-TIME-BAS-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is BASIC fossil named `HELLO.BAS` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-bas` prints `1 *.bas` |
| Runs under Bywater BASIC 2.20pl2 file invocation | VERIFIED | `bwbasic HELLO.BAS` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-BAS-PROBE-OK` |
| Dialect is a specific Microsoft / ANSI Full BASIC / BBC claim | CONJECTURE | No GW-BASIC / QB / VB / BBC / FreeBASIC jury beyond `PRINT` / `SYSTEM` |
| Would run under period Microsoft BASICA / GW-BASIC ROM | UNVERIFIABLE here | No period DOS / BASICA run in this session |
| Full ANSI Full BASIC / graphics / structured-BASIC suite | UNVERIFIABLE here | print + SYSTEM probe only |

## Not done (honest gaps)

- No Jail-hunt of the full ANSI Minimal BASIC / Full BASIC standards
  (deferred; pin is **bwbasic command-line file execution** — see
  `references/archaeology-basic-manual.md`).
- No bare English `basic` route tag (common-English collision).
- No bare `print` route tag (cross-dialect keyword).
