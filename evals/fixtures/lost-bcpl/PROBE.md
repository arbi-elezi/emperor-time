# Boot probe — lost-bcpl / HELLO.B

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~04:23 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Martin Richards BCPL Cintcode** from https://www.cl.cam.ac.uk/~mr10/BCPL/bcpl.tgz |
| Binary | `/tmp/toolchain-probe/bcpl/extract/BCPL/cintcode/bin/cintsys` (prefix after local `make`) |
| Reported | `BCPL 32-bit Cintcode System (16 May 2026)` / compiler `32 bit BCPL (18 Apr 2026)` |
| Install | extract `bcpl.tgz` → `cd BCPL/cintcode` → `export BCPLROOT=$(pwd)` → `export PATH=$BCPLROOT/bin:$PATH` → `make` |

Probe used non-interactive CLI (`cintsys -q -c 'bcpl hello.b to hello; hello'`)
on a `GET "libhdr"` / `writef` print source. Identify fossils use `*.b` and
`*.bcpl`. Prefer `bcpl` / `cintsys` / `cintcode` / `.bcpl`; bare English
tokens (`get` / `writef` / `libhdr`) and bare `.b` alone are **refused** as
route tags (keyword / short-extension collision class — `.b` matches
`.bin` / `.bak` / `.backup` substrings). Do not commit compiled Cintcode
outputs (`hello` without extension) or `DUMP.mem` from the probe.

**Case note:** Martin Richards `bcpl` expects a lowercase `hello.b` path.
Fixture keeps `HELLO.B` 8.3 caps for sister-fixture culture; probe uses
`ln -sf HELLO.B hello.b` (or a lowercase copy) before compile.

## Commands (VERIFIED)

Working directory: any dir with the source (fixture dir used) and
`BCPLROOT` / `PATH` pointing at the built cintcode tree.

```text
$ export BCPLROOT=/tmp/toolchain-probe/bcpl/extract/BCPL/cintcode
$ export PATH=$BCPLROOT/bin:$PATH
$ /tmp/toolchain-probe/bcpl/extract/BCPL/cintcode/bin/cintsys -h | head -5
Valid arguments:

-h            Output this help information
-m n          Set Cintcode memory size to n words
-t n          Set Tally vector size to n words

$ ln -sf HELLO.B hello.b
$ cintsys -q -c 'bcpl hello.b to hello; hello'
EMPEROR-TIME-BCPL-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is BCPL fossil named `HELLO.B` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-bcpl` prints `1 *.b` |
| Compiles+runs under Martin Richards Cintcode (16 May 2026) | VERIFIED | `cintsys -q -c 'bcpl hello.b to hello; hello'` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-BCPL-PROBE-OK` |
| Dialect is a specific period Cambridge BCPL / Tripos full claim | CONJECTURE | No Tripos / native-code jury beyond `writef` print |
| Would run under period CTSS / Multics / other vendor BCPL on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of the full Martin Richards BCPL language reference
  (deferred; pin is Cintcode **cintsys `-c` / `bcpl … to …`** compile-run —
  see `references/archaeology-bcpl-manual.md`).
- No bare `.b` route tag (short-extension collision class).
- No bare English keyword route tags (`get` / `writef` / `libhdr`).
