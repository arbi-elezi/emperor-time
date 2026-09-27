# Boot probe — lost-tcl / HELLO.TCL

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~00:56 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `tcl` **8.6.16** (Debian trixie default) |
| Binary | `/usr/bin/tclsh` → `tclsh8.6` |
| Reported | `info patchlevel` → **8.6.16** |
| Install | Already present on box (`/usr/bin/tclsh`) |

Tk windowing shell (`wish`) was **not** required for this string-print
probe. Probe used `tclsh` 8.6.16 on Linux because that is what can actually
source+run on this host. Uppercase `HELLO.TCL` is accepted as a source
filename; that is normal Tcl scripting culture, not a probe failure.
Identify fossils use `*.tcl` / `*.tk` (no known collision with other
house fossils).

## Commands (VERIFIED)

Working directory for load/run: fixture dir (and earlier `/tmp` copy).

```text
$ echo 'puts [info patchlevel]' | tclsh
8.6.16

$ tclsh HELLO.TCL
EMPEROR-TIME-TCL-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Tcl fossil named `HELLO.TCL` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-tcl` prints `1 *.tcl` |
| Runs under Tcl 8.6.16 (`tclsh` file arg) | VERIFIED | `tclsh HELLO.TCL` exit 0 |
| Prints known string | VERIFIED | stdout is `EMPEROR-TIME-TCL-PROBE-OK` |
| Dialect is a specific Tcl 8.6 year/patch claim beyond puts | CONJECTURE | No TIP jury; `puts` subset only |
| Would run under period Tcl 7.x / Wish on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of a purchased Ousterhout book clause (deferred; pin is
  tclsh SCRIPT FILES — see `references/archaeology-tcl-manual.md`).
- No `wish` / Tk widget compile.
- No Expect / TclOO / coroutine claim.
