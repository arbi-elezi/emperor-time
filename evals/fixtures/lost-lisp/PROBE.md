# Boot probe — lost-lisp / HELLO.LISP

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~00:33 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `clisp` **1:2.49.20241228.gitc3ec11b-2** (Debian trixie) |
| Binary | `/usr/bin/clisp` |
| Reported | `GNU CLISP 2.49.95+ (2024-11-03) (built on sbuild [127.0.1.1])` |
| Install | `sudo apt-get update && sudo apt-get install -y clisp` → exit **0** |

SBCL / CCL / ECL were **not** installed on this box for the probe. Probe used
GNU CLISP 2.49.95+ on Linux because that is what can actually load+run on this
host. Uppercase `HELLO.LISP` is accepted as a source filename; that is
documented CLISP scripting culture, not a probe failure.

## Commands (VERIFIED)

Working directory for load/run: `/tmp/lisp-probe` (copy of `HELLO.LISP`;
no fasl / binary committed).

```text
$ clisp --version
GNU CLISP 2.49.95+ (2024-11-03) (built on sbuild [127.0.1.1])
…

$ clisp -q -norc HELLO.LISP
EMPEROR-TIME-LISP-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Lisp fossil named `HELLO.LISP` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-lisp` prints `1 *.lisp` |
| Runs under GNU CLISP 2.49.95+ (batch lisp-file) | VERIFIED | `clisp -q -norc HELLO.LISP` exit 0 |
| Prints known string | VERIFIED | stdout is `EMPEROR-TIME-LISP-PROBE-OK` |
| Dialect is ANSI Common Lisp specifically | CONJECTURE | No ANSI CL jury PDF; `FORMAT` / `T` / `~%` subset only |
| Would run under period Maclisp / Interlisp on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of a purchased ANSI CL Hyperspec clause book (deferred; pin is
  CLISP invokation Non-Interactive Batch Mode — see
  `references/archaeology-lisp-manual.md`).
- No SBCL / CCL / ECL compile.
- No CLOS / package / ASDF claim.
