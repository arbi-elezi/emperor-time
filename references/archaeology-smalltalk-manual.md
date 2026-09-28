# Jail pin — GNU Smalltalk gst file invocation (HELLO.ST)

Contemporaneous manual pin for the lost-Smalltalk archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Smalltalk
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-st/HELLO.ST` with
runnable dialect **VERIFIED** as GNU Smalltalk version 3.2.5
under Linux x86_64
(`./gst -q HELLO.ST` → `EMPEROR-TIME-ST-PROBE-OK`). Filename culture
(`.ST` / 8.3 caps → Smalltalk *naming*) remains **CONJECTURE** only.
Identify fossils use `*.st` only (not `*.cs` — C# collision). Bare `.st`
is refused as a route tag (short-extension collision with `.stack` /
`.string` / …). This note supplies the Jail pin so excavate can name the
**verified** gst file-invocation shape without inventing a full period
Smalltalk-80 / Pharo / Squeak Morphic claim for a print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GNU Smalltalk User's Guide* — Invocation / Command line arguments |
| **Heading** | **Command line arguments** — `gst [ flags … ] [ file … ]`; files are read and executed in order |
| **Dialect pinned** | **Smalltalk via GNU Smalltalk gst** with `Transcript show:` / `cr` print surface — **not** full Pharo / Squeak / Morphic / Blue Book image claim |
| **URL** | https://www.gnu.org/software/smalltalk/manual/html_node/Invocation.html (Invocation); distribution https://ftp.gnu.org/gnu/smalltalk/smalltalk-3.2.5.tar.gz ; local source pin `doc/gst.texi` `@node Invocation` in the 3.2.5 tarball |
| **Anchors** | Invocation — `gst [ flags … ] [ file … ]`; "If you specify one or more files, they will be read and executed in order" |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from GNU Smalltalk User's Guide — Invocation / Command line arguments)

> The GNU Smalltalk virtual machine may be invoked via the following command:
>
> `gst [ flags … ] [ file … ]`
>
> If you specify one or more files, they will be read and executed
> in order, and Smalltalk will exit when end of file is reached.

(Source: `doc/gst.texi` `@node Invocation` in smalltalk-3.2.5; same
text as the published Invocation HTML node. Probe uses `./gst -q HELLO.ST`
from the build tree so the libtool wrapper finds `libgst` + local
`gst.im` / `kernel/`. `Transcript show: …; cr.` prints the probe string.)

### Why this heading (HELLO.ST / excavate)

A minimal HELLO surface looks like:

```smalltalk
Transcript show: 'EMPEROR-TIME-ST-PROBE-OK'; cr.
```

in a `.ST` / `.st` file. That is exactly the pinned form:
**`gst`** reads the named source file and executes it, observe
`Transcript show:` at run time. Pinning Invocation / file arguments lets
excavate treat `gst` / `smalltalk` / `gnu-smalltalk` + `Transcript show:` /
`cr` as **era evidence** (GNU Smalltalk / source file) without rewriting the
fixture into a Pharo zeroconf image, Squeak changesets, or a Python port.

**Dialect precision:** this pin authorizes GNU Smalltalk gst reading of the
`Transcript show:` / `cr` / file-invocation shape only. It does **not**
claim the lost tree is period Smalltalk-80 on Xerox media, a specific
Pharo/Squeak release, or a working Morphic GUI session on this host. Those
are other manuals / toolchains. HELLO's "GNU-Smalltalk-ish / Transcript
subset" label remains **CONJECTURE** until a dialect-specific vendor run is
evidence — gst accepting the `Transcript show:` shape and printing the
probe string is the VERIFIED claim for this leaf.
