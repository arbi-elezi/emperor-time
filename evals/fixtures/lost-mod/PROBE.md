# Boot probe — lost-mod / HELLO.MOD

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~01:41 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `gm2` **4:14.2.0-1** meta → `gm2-14` **14.2.0-19** (Debian trixie) |
| Binary | `/usr/bin/gm2` |
| Reported | gm2 (Debian 14.2.0-19) **14.2.0** |
| Install | `sudo apt-get install -y gm2` on this box |

Probe used `gm2` (GCC GNU Modula-2 14.2.0) on a PIM `StrIO` source with
`WriteString` / `WriteLn`. Uppercase `HELLO.MOD` needs `-x modula-2` because
the driver keys language off lowercase `.mod`; that is normal gm2 culture,
not a probe failure. Identify fossils use `*.mod` / `*.def` (Fortran
compiler module artifacts can also use `.mod` — survey honesty, not a
refusal). Bare English/token `mod` alone is **refused** as a route tag;
prefer `gm2` / `modula-2` / `modula2` / `.mod` / `.def` / space-intent
`modula`.

## Commands (VERIFIED)

Working directory for compile/run: fixture dir (and earlier `/tmp` copy).

```text
$ gm2 --version | head -1
gm2 (Debian 14.2.0-19) 14.2.0

$ gm2 -g -x modula-2 -o hello HELLO.MOD && ./hello
EMPEROR-TIME-MOD-PROBE-OK
# exit 0
```

(Lowercase `hello.mod` also works as `gm2 -g -o hello hello.mod` without
`-x modula-2`.)

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Modula-2 fossil named `HELLO.MOD` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-mod` prints `1 *.mod` |
| Compiles and runs under gm2 14.2.0 (`gm2 -g -x modula-2`) | VERIFIED | `./hello` exit 0 |
| Prints known string | VERIFIED | stdout is `EMPEROR-TIME-MOD-PROBE-OK` |
| Dialect is a specific ISO 10514-1 year / PIM-2 claim beyond StrIO | CONJECTURE | No ISO jury; PIM StrIO WriteString subset only |
| Would run under period Wirth / Logitech / TopSpeed Modula-2 on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of a purchased Wirth *Programming in Modula-2* clause
  (deferred; pin is GNU Modula-2 Example compile and link — see
  `references/archaeology-modula2-manual.md`).
- No DEFINITION MODULE / `.def` pair claim.
- No SYSTEM / COROUTINES / ISO STextIO-only claim (probe uses PIM StrIO).
