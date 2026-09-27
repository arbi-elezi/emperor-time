# Boot probe — lost-a68 / HELLO.A68

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~01:54 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `algol68g` **3.1.2-1+b1** (Debian trixie) |
| Binary | `/usr/bin/a68g` |
| Reported | Algol 68 Genie **3.1.2** |
| Install | `sudo apt-get install -y algol68g` on this box |

Probe used `a68g` (Algol 68 Genie 3.1.2) on a particular-program with
standard-prelude `print` + `new line`. Identify fossils use `*.a68` /
`*.alg`. Bare English token `print` alone is **refused** as a route tag;
prefer `a68g` / `algol68g` / `algol68` / `.a68` / `.alg` / space-intent
`algol`. Note: `a68g` may write a local `.Random.seed` beside the source;
do not commit that artifact.

## Commands (VERIFIED)

Working directory for run: fixture dir.

```text
$ a68g --version | head -1
Algol 68 Genie 3.1.2

$ a68g HELLO.A68
EMPEROR-TIME-A68-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Algol 68 fossil named `HELLO.A68` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-a68` prints `1 *.a68` |
| Runs under a68g 3.1.2 | VERIFIED | `a68g HELLO.A68` exit 0 |
| Prints known string | VERIFIED | stdout is `EMPEROR-TIME-A68-PROBE-OK` |
| Dialect is a specific Revised Report year / full RR claim beyond print | CONJECTURE | No RR jury; Genie subset `print` particular-program only |
| Would run under period Algol 68 (ALGOL 68R / ALGOL 68C / FLACC) on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of the full Revised Report transput clause set
  (deferred; pin is Algol 68 Genie Synopsis invoke + Transput `print` —
  see `references/archaeology-algol68-manual.md`).
- No ALGOL 60 / Algol W claim (different language family).
- No FORMAT / format-texts claim (Genie documents FORMAT as unimplemented).
