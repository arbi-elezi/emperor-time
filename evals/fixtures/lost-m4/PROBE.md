# Boot probe — lost-m4 / HELLO.M4

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~06:26 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **m4** 1.4.19-8 (`m4` Debian package) |
| Binary | `/usr/bin/m4` (GNU M4) |
| Reported | `m4 (GNU M4) 1.4.19` |
| Install | `apt-get install m4` (Debian trixie; usually preinstalled) |

Probe used FILE-argument invocation
(`m4 HELLO.M4`)
on a minimal `define` / `dnl` macro script. Identify fossils
use `*.m4` only. Prefer `m4` / `gm4` / `.m4`. Bare `m4` is
**allowed** as a route tag because it is the tool binary name
(unlike English `scheme` / `basic` collisions, and unlike refused bare
`gs` two-letter process-status collision). Do not claim a full POSIX
m4 / traditional AT&T m4 / Autoconf suite recovery from a GNU m4
`define`/`dnl` probe alone — this leaf pins GNU m4.

## Commands (VERIFIED)

```text
$ dpkg -l m4 | awk '/^ii/ {print $2, $3}'
m4 1.4.19-8

$ m4 --version | head -1
m4 (GNU M4) 1.4.19

$ m4 evals/fixtures/lost-m4/HELLO.M4
EMPEROR-TIME-M4-PROBE-OK
# exit 0
```

Note: GNU m4 reads remaining command-line arguments as input file
names (Invoking m4 / Command line files). Documented VERIFIED form is
**`m4 HELLO.M4`** with classic backtick/apostrophe quoting in the
`define` surface.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is m4 fossil named `HELLO.M4` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-m4` prints `1 *.m4` |
| Runs under GNU M4 1.4.19 FILE-argument invocation | VERIFIED | `m4 HELLO.M4` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-M4-PROBE-OK` |
| Dialect is a specific POSIX / AT&T / Autoconf claim | CONJECTURE | No other m4 jury beyond `define`/`dnl` under GNU m4 |
| Would run under period AT&T / SysV m4 ROM | UNVERIFIABLE here | No period m4 ROM run in this session |
| Full GNU m4 extensions / freeze / Autoconf suite | UNVERIFIABLE here | single define/dnl probe only |

## Not done (honest gaps)

- No Jail-hunt of the full GNU M4 manual beyond
  Invoking m4 / Command line files (deferred; pin is **m4 FILE**
  — see `references/archaeology-m4-manual.md`).
- Bare `m4` is allowed (tool binary name); no English-collision refuse.
- No `*.gm4` fossil this leaf (`.m4` only).
