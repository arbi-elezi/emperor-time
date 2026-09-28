# Boot probe — lost-st / HELLO.ST

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~05:02 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **GNU Smalltalk** 3.2.5 from https://ftp.gnu.org/gnu/smalltalk/smalltalk-3.2.5.tar.gz |
| Binary | `/tmp/toolchain-probe/smalltalk/smalltalk-3.2.5/gst` (libtool wrapper; build tree) |
| Reported | `GNU Smalltalk version 3.2.5` |
| Install | extract tarball → `./configure --prefix=… --disable-gtk --without-tcl --without-tk --without-x` → `make` (optional packages may fail modern gcc iconv; core `gst` + `gst.im` suffice) |

Probe used non-interactive file run
(`./gst -q HELLO.ST` from the build tree, or
`gst --kernel-directory=…/kernel -I …/gst.im -q HELLO.ST`)
on a `Transcript show: …; cr.` print source. Identify fossils
use `*.st` only. Prefer `gst` / `smalltalk` / `gnu-smalltalk`; bare `.st`
is **refused** as a route tag (short-extension collision with `.stack` /
`.string` / …). Bare English tokens (`transcript` / `show` / `cr`) alone are
**refused** as route tags (keyword collision class). Do not commit the
optional `iconv` package object debris from a full `make`.

## Commands (VERIFIED)

Working directory: the GNU Smalltalk 3.2.5 build tree (so the libtool
`gst` wrapper finds `.libs/gst` + `libgst.so.7` and the local `gst.im` /
`kernel/`).

```text
$ /tmp/toolchain-probe/smalltalk/smalltalk-3.2.5/gst --version
GNU Smalltalk version 3.2.5
Copyright 2009 Free Software Foundation, Inc.
Written by Steve Byrne (sbb@gnu.org) and Paolo Bonzini (bonzini@gnu.org)

$ cd /tmp/toolchain-probe/smalltalk/smalltalk-3.2.5
$ ./gst -q /workspace/emperor-time/evals/fixtures/lost-st/HELLO.ST
EMPEROR-TIME-ST-PROBE-OK
# exit 0

# Equivalent when cwd is not the build tree:
$ gst --kernel-directory=/tmp/toolchain-probe/smalltalk/smalltalk-3.2.5/kernel \
    -I /tmp/toolchain-probe/smalltalk/smalltalk-3.2.5/gst.im \
    -q evals/fixtures/lost-st/HELLO.ST
EMPEROR-TIME-ST-PROBE-OK
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Smalltalk fossil named `HELLO.ST` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-st` prints `1 *.st` |
| Runs under GNU Smalltalk 3.2.5 file invocation | VERIFIED | `./gst -q HELLO.ST` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-ST-PROBE-OK` |
| Dialect is a specific Pharo / Squeak / Morphic full claim | CONJECTURE | No image / Morphic jury beyond `Transcript show:` print |
| Would run under period Smalltalk-80 on original media | UNVERIFIABLE here | No period Xerox / vendor image run in this session |
| Full `make install` of all optional packages (iconv) | UNVERIFIABLE here | modern gcc rejects packages/iconv `iconv()` signature; core VM verified |

## Not done (honest gaps)

- No Jail-hunt of the full GNU Smalltalk / Smalltalk-80 Blue Book
  (deferred; pin is **gst file invocation** — see
  `references/archaeology-smalltalk-manual.md`).
- No bare `.st` route tag (short-extension collision).
- No bare English keyword route tags (`transcript` / `show` / `cr`).
