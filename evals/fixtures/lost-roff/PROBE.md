# Boot probe — lost-roff / HELLO.ROFF

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~07:57 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **groff** 1.23.0-9 (Debian package; meta pulls **groff-base** 1.23.0-9) |
| Binary | `/usr/bin/groff` (GNU groff); `/usr/bin/nroff` (GNU nroff wrapper) |
| Reported | `GNU groff version 1.23.0` |
| Install | `apt-get install groff` (Debian trixie) |

Probe used groff ASCII device output
(`groff -Tascii HELLO.ROFF`)
on a minimal roff input with a no-fill text line printing the probe string.
Identify fossils use `*.roff`. Prefer `roff` / `nroff` /
`groff` / `gnu-groff` / `.roff`. Bare `roff`, `nroff`, and `groff` are
**allowed** as route tags because they are tool binary names (unlike
English `scheme` / `basic` collisions, and unlike refused bare `make`
factory collision). Do not claim a full AT&T troff / Heirloom Doctools /
ms/me/mm/man macro suite recovery from a GNU groff `-Tascii` print probe
alone — this leaf pins GNU groff (roff-compatible formatter).

## Commands (VERIFIED)

```text
$ dpkg -l groff groff-base | awk '/^ii/ {print $2, $3}'
groff 1.23.0-9
groff-base 1.23.0-9

$ groff -v 2>&1 | head -1
GNU groff version 1.23.0

$ which groff nroff
/usr/bin/groff
/usr/bin/nroff

$ cd evals/fixtures/lost-roff
$ groff -Tascii HELLO.ROFF | sed '/^$/d'
EMPEROR-TIME-ROFF-PROBE-OK
# exit 0

$ nroff HELLO.ROFF | sed '/^$/d'
EMPEROR‐TIME‐ROFF‐PROBE‐OK
# exit 0 (nroff may emit Unicode hyphens; ASCII probe string verified via groff -Tascii)
```

Note: groff(1) SYNOPSIS is `groff [OPTION]... [file ...]`. With a file
argument groff reads roff input and formats it for the selected output
device (`-T output-device`). Documented VERIFIED form is
**`groff -Tascii HELLO.ROFF`**. Blank page padding is normal for roff
terminal devices; `sed '/^$/d'` is only for human-readable capture (same
pattern as Debian groff(1) Examples). The fixture uses `.nf` / `.fi`
around a single probe line so the leaf pins formatter invocation, not a
macro-package jury.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is roff fossil named `HELLO.ROFF` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-roff` prints `1 *.roff` |
| Formats under GNU groff 1.23.0 file input | VERIFIED | `groff -Tascii HELLO.ROFF` exit 0 |
| Prints known ASCII string | VERIFIED | stdout contains `EMPEROR-TIME-ROFF-PROBE-OK` |
| Dialect is a specific AT&T troff / Heirloom / ms claim | CONJECTURE | No other roff jury beyond GNU groff `-Tascii` of this input |
| Would run under period AT&T nroff on original media | UNVERIFIABLE here | No period AT&T nroff ROM run in this session |
| Full ms/me/mm/man / eqn/tbl/pic suite | UNVERIFIABLE here | single `-Tascii` print probe only |

## Not done (honest gaps)

- No Jail-hunt of the full groff Texinfo manual beyond
  SYNOPSIS file operands + Options `-T` / output-device (deferred; pin is
  **groff -Tascii FILE** — see `references/archaeology-roff-manual.md`).
- Bare `roff` / `nroff` / `groff` allowed (tool binary names).
- No `*.ms` / `*.me` / `*.mm` / `*.man` / section-number (`*.1`…) fossil
  this leaf (`.roff` only; avoid short/numeric collisions and macro-package
  overclaim).
