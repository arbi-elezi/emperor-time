# Boot probe — lost-ada / HELLO.ADB

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-27 ~21:45 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `gnat-13` **13.3.0-16** → `gnat-13-x86-64-linux-gnu` **13.3.0-16** + `libgnat-13` (Debian trixie) |
| Binary | `/usr/bin/gnatmake` → `x86_64-linux-gnu-gnatmake-13` |
| Reported | `gnatmake --version` → `GNATMAKE 13.3.0` |
| Install | `sudo apt-get update && sudo apt-get install -y gnat-13` → exit **0** |

GNAT Studio / ObjectAda / Janus/Ada / Alire were **not** present. Probe used
GNATMAKE 13.3.0 on Linux because that is what can actually compile+bind+link
on this box. Uppercase `HELLO.ADB` yields executable `HELLO` (and a filename
vs unit-name warning); that is documented GNAT naming culture, not a probe
failure.

## Commands (VERIFIED)

Working directory for compile/run: `/tmp/ada-probe` (copy of `HELLO.ADB`;
`.o` / `.ali` / binary not committed).

```text
$ gnatmake --version
GNATMAKE 13.3.0
…

$ gnatmake HELLO.ADB
x86_64-linux-gnu-gcc-13 -c -x ada HELLO.ADB
HELLO.ADB:5:11: warning: file name does not match unit name, should be "hello.adb" [enabled by default]
x86_64-linux-gnu-gnatbind-13 -x HELLO.ali
x86_64-linux-gnu-gnatlink-13 HELLO.ali
# exit 0

$ ./HELLO
EMPEROR-TIME-ADA-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Ada fossil named `HELLO.ADB` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-ada` prints `1 *.adb` |
| Compiles under GNATMAKE 13.3.0 | VERIFIED | `gnatmake HELLO.ADB` exit 0 |
| Runs and prints known string | VERIFIED | `./HELLO` stdout is `EMPEROR-TIME-ADA-PROBE-OK` |
| Dialect is Ada 95 / 2005 / 2012 specifically | CONJECTURE | No ISO 8652 jury PDF; procedure/`Ada.Text_IO` subset only |
| Would run under period vendor Ada on original media | UNVERIFIABLE here | No ObjectAda / Janus / period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of a purchased ISO/IEC 8652 clause (deferred; pin is GNAT
  User's Guide Building with gnatmake — see
  `references/archaeology-ada-manual.md`).
- No ObjectAda / Janus/Ada / Alire compile.
- No package spec (`.ads`) / tasking / generics claim.
- No port to Python (forbidden by doctrine).
