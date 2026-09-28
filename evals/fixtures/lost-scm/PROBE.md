# Boot probe — lost-scm / HELLO.SCM

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~05:46 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **CHICKEN** 5.3.0-2 (`chicken-bin` Debian package) |
| Binary | `/usr/bin/csi` (interpreter); `/usr/bin/chicken` (compiler) |
| Reported | `Version 5.3.0 (rev e31bbee5)` / `linux-unix-gnu-x86-64` |
| Install | `apt-get install chicken-bin` (Debian trixie) |

Probe used interpreter script / batch file execution
(`csi -s HELLO.SCM`)
on a minimal `display` / `newline` source. Identify fossils
use `*.scm` only. Prefer `csi` / `chicken` / `chicken-scheme` / `.scm`; bare English
`scheme` is **refused** as a dedicated route tag (common-English collision —
"color scheme", "scheme of things"). Do not claim a full Racket / Guile /
Chez / MIT Scheme / R7RS recovery from a Chicken display probe.

## Commands (VERIFIED)

```text
$ dpkg -l chicken-bin | awk '/^ii/ {print $2, $3}'
chicken-bin 5.3.0-2

$ csi -s evals/fixtures/lost-scm/HELLO.SCM
EMPEROR-TIME-SCM-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Scheme fossil named `HELLO.SCM` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-scm` prints `1 *.scm` |
| Runs under CHICKEN 5.3.0 `csi -s` script invocation | VERIFIED | `csi -s HELLO.SCM` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-SCM-PROBE-OK` |
| Dialect is a specific Racket / Guile / Chez / R7RS claim | CONJECTURE | No other Scheme jury beyond `display` / `newline` |
| Would run under period Scheme48 / MIT Scheme ROM | UNVERIFIABLE here | No period Scheme ROM run in this session |
| Full R5RS / R7RS / egg / module suite | UNVERIFIABLE here | display + newline probe only |

## Not done (honest gaps)

- No Jail-hunt of the full R5RS / R7RS / CHICKEN User's Manual beyond
  interpreter script options (deferred; pin is **csi -s / -script PATHNAME** — see
  `references/archaeology-scheme-manual.md`).
- No bare English `scheme` route tag (common-English collision).
- No `*.ss` fossil this leaf (`.scm` only; Chez/Racket `.ss` deferred).
