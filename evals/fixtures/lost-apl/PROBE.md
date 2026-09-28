# Boot probe — lost-apl / HELLO.APL

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~03:56 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **GNU APL 2.0** from https://mirrors.kernel.org/gnu/apl/apl-2.0.tar.gz |
| Binary | `/tmp/toolchain-probe/apl/install/bin/apl` (prefix install after local build) |
| Reported | `Project: GNU APL` / `Version / SVN: 2.0` via `--version` |
| Install | `./configure --prefix=… --with-optional_libs=no --without-postgresql && make && make install` |

Probe used GNU APL script mode (`-s --OFF -f`) on a `⎕←'…'` print
source. Identify fossils use `*.apl` only. Prefer `apl` / `gnu-apl` /
`.apl`; bare English tokens alone are **refused** as route tags
(keyword / English collision class). Do not commit generated workspaces
or `CONTINUE` / `SETUP` artifacts from the probe.

**Binary .deb note:** `apl_2.0-1_amd64.deb` from the same GNU mirror
extracts an `apl` binary that needs `libgsl.so.27` + `libpq.so.5`. This
trixie host has `libgsl28` (not `.27`), so the prebuilt deb link is
**UNVERIFIABLE** here without matching libs. The VERIFIED run is the
source build above.

## Commands (VERIFIED)

Working directory: any dir with the source (fixture dir used).

```text
$ /tmp/toolchain-probe/apl/install/bin/apl --version
BUILDTAG:
---------
    Project:        GNU APL
    Version / SVN:  2.0 / SVN: no-svnversion
    Build Date:     2026-09-28 03:54:51 CEST
    Build OS:       Linux 6.12.94+ x86_64

$ /tmp/toolchain-probe/apl/install/bin/apl -s --OFF -f evals/fixtures/lost-apl/HELLO.APL
EMPEROR-TIME-APL-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is APL fossil named `HELLO.APL` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-apl` prints `1 *.apl` |
| Runs under GNU APL 2.0 (source build, optional libs off) | VERIFIED | `apl -s --OFF -f HELLO.APL` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-APL-PROBE-OK` |
| Dialect is a specific ISO 13751 Extended / nested-array full claim | CONJECTURE | No ⎕ML / nested-array jury beyond `⎕←` print |
| Would run under period IBM APL\360 / APL2 vendor on original media | UNVERIFIABLE here | No period vendor run in this session |
| Prebuilt `apl_2.0-1_amd64.deb` on this host | UNVERIFIABLE here | Needs `libgsl.so.27`; trixie has `libgsl28` |

## Not done (honest gaps)

- No Jail-hunt of the full ISO 13751 Extended APL chapter
  (deferred; pin is GNU APL **SYNOPSIS** / `-f file` — see
  `references/archaeology-apl-manual.md`).
- No prebuilt Debian binary VERIFIED claim on this host (GSL SONAME).
- No bare English keyword route tags (extension / `apl` / `gnu-apl` only).
