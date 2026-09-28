# Boot probe — lost-awk / HELLO.AWK

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~06:02 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **gawk** 1:5.2.1-2+b1 (`gawk` Debian package) |
| Binary | `/usr/bin/gawk`; `/usr/bin/awk` and `/usr/bin/nawk` → gawk via alternatives |
| Reported | `GNU Awk 5.2.1, API 3.2, PMA Avon 8-g1` |
| Install | `apt-get install gawk` (Debian trixie; usually preinstalled) |

Probe used program-file invocation
(`gawk -f HELLO.AWK`)
on a minimal `BEGIN` / `print` source. Identify fossils
use `*.awk` only. Prefer `gawk` / `awk` / `nawk` / `.awk`. Bare `awk` is
**allowed** as a route tag because it is the POSIX / tool binary name
(unlike English `scheme` / `basic` collisions, and unlike refused bare
`gs` two-letter process-status collision). Do not claim a full POSIX
awk / nawk / mawk / BusyBox / One True Awk recovery from a GNU Awk
`BEGIN`/`print` probe alone — host also has mawk, but this leaf pins gawk.

## Commands (VERIFIED)

```text
$ dpkg -l gawk | awk '/^ii/ {print $2, $3}'
gawk 1:5.2.1-2+b1

$ gawk --version | head -1
GNU Awk 5.2.1, API 3.2, PMA Avon 8-g1, (GNU MPFR 4.2.2, GNU MP 6.3.0)

$ gawk -f evals/fixtures/lost-awk/HELLO.AWK
EMPEROR-TIME-AWK-PROBE-OK
# exit 0
```

Note: bare `gawk HELLO.AWK` (no `-f`) treats the path as program text and
fails. Documented VERIFIED form is **`gawk -f`**.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is AWK fossil named `HELLO.AWK` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-awk` prints `1 *.awk` |
| Runs under GNU Awk 5.2.1 `-f` file invocation | VERIFIED | `gawk -f HELLO.AWK` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-AWK-PROBE-OK` |
| Dialect is a specific POSIX / nawk / mawk / BusyBox claim | CONJECTURE | No other AWK jury beyond `BEGIN` / `print` under gawk |
| Would run under period AT&T / One True Awk ROM | UNVERIFIABLE here | No period AWK ROM run in this session |
| Full POSIX awk / gawk extensions / networking suite | UNVERIFIABLE here | BEGIN + print probe only |

## Not done (honest gaps)

- No Jail-hunt of the full GAWK Effective AWK Programming manual beyond
  Command-Line Options `-f` / `--file` (deferred; pin is **gawk -f
  source-file** — see `references/archaeology-awk-manual.md`).
- Bare `awk` is allowed (tool binary name); no English-collision refuse.
- No `*.gawk` fossil this leaf (`.awk` only).
