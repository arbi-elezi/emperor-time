# Boot probe — lost-sed / HELLO.SED

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~06:10 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **sed** 4.9-2+deb13u1 (`sed` Debian package) |
| Binary | `/usr/bin/sed` (GNU sed) |
| Reported | `sed (GNU sed) 4.9` |
| Install | `apt-get install sed` (Debian trixie; usually preinstalled) |

Probe used script-file invocation
(`sed -f HELLO.SED` with stdin line)
on a minimal `s///` substitute script. Identify fossils
use `*.sed` only. Prefer `sed` / `gsed` / `.sed`. Bare `sed` is
**allowed** as a route tag because it is the POSIX / tool binary name
(unlike English `scheme` / `basic` collisions, and unlike refused bare
`gs` two-letter process-status collision). Do not claim a full POSIX
sed / BSD sed / BusyBox sed recovery from a GNU sed `s///` probe alone —
this leaf pins GNU sed.

## Commands (VERIFIED)

```text
$ dpkg -l sed | awk '/^ii/ {print $2, $3}'
sed 4.9-2+deb13u1

$ sed --version | head -1
sed (GNU sed) 4.9

$ printf 'probe-input\n' | sed -f evals/fixtures/lost-sed/HELLO.SED
EMPEROR-TIME-SED-PROBE-OK
# exit 0
```

Note: bare `sed HELLO.SED` (no `-f`) treats the path as the script text
(or fails oddly). Documented VERIFIED form is **`sed -f`** with an input
stream (stdin or file args after the script-file).

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is sed fossil named `HELLO.SED` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-sed` prints `1 *.sed` |
| Runs under GNU sed 4.9 `-f` script-file invocation | VERIFIED | `sed -f HELLO.SED` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-SED-PROBE-OK` |
| Dialect is a specific POSIX / BSD / BusyBox claim | CONJECTURE | No other sed jury beyond `s///` under GNU sed |
| Would run under period AT&T / 7th Edition sed ROM | UNVERIFIABLE here | No period sed ROM run in this session |
| Full GNU sed extensions / in-place / extended-regex suite | UNVERIFIABLE here | single substitute probe only |

## Not done (honest gaps)

- No Jail-hunt of the full GNU sed manual beyond
  Command-Line Options `-f` / `--file` (deferred; pin is **sed -f
  script-file** — see `references/archaeology-sed-manual.md`).
- Bare `sed` is allowed (tool binary name); no English-collision refuse.
- No `*.gsed` fossil this leaf (`.sed` only).
