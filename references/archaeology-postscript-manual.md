# Jail pin — GPL Ghostscript gs file invocation (HELLO.PS)

Contemporaneous manual pin for the lost-PostScript archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how PostScript
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-ps/HELLO.PS` with
runnable dialect **VERIFIED** as GPL Ghostscript 10.05.1
under Linux x86_64
(`gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage HELLO.PS` →
`EMPEROR-TIME-PS-PROBE-OK`). Filename culture
(`.PS` / 8.3 caps → PostScript *naming*) remains **CONJECTURE** only.
Identify fossils use `*.ps` + `*.eps` (not `*.ps1` — PowerShell collision).
Bare `.ps` is refused as a route tag (short-extension collision with
`.ps1`). Bare `gs` is refused as a route tag (two-letter collision with
Unix process-status / other short tokens). This note supplies the Jail pin
so excavate can name the **verified** gs file-invocation shape without
inventing a full period Adobe printer ROM / Distiller / Display PostScript
claim for a print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Using Ghostscript* — Invoking Ghostscript |
| **Heading** | **Invoking Ghostscript** — `gs [options] {filename 1} ... [options] {filename N} ...` |
| **Dialect pinned** | **PostScript via GPL Ghostscript gs** with `print` / `flush` / `quit` surface — **not** full Adobe Distiller / Level-3 RIP / printer-firmware / Display PostScript claim |
| **URL** | https://ghostscript.readthedocs.io/en/latest/Use.html (Using / Invoking Ghostscript); package `ghostscript` 10.05.1 on Debian trixie |
| **Anchors** | Invoking Ghostscript — `gs [options] {filename 1} ...`; interpreter reads and executes the files in sequence |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Using Ghostscript — Invoking Ghostscript)

> The command line to invoke Ghostscript is essentially the same on all
> systems, although the name of the executable program itself may differ
> among systems. For instance, to invoke Ghostscript on unix-like systems
> type:
>
> `gs [options] {filename 1} ... [options] {filename N} ...`
>
> Ghostscript is capable of interpreting PostScript, encapsulated
> PostScript (EPS), DOS EPS (EPSF), and Adobe Portable Document Format
> (PDF). The interpreter reads and executes the files in sequence…

(Source: Ghostscript User Guide — Using / Invoking Ghostscript,
https://ghostscript.readthedocs.io/en/latest/Use.html , accessed
2026-09-28 Europe/Tirane. Probe uses
`gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage HELLO.PS` so the interpreter
runs the named source non-interactively on the nullpage device.
`(string) print` + `flush` + `quit` prints the probe string.)

### Why this heading (HELLO.PS / excavate)

A minimal HELLO surface looks like:

```postscript
%!PS
(EMPEROR-TIME-PS-PROBE-OK) print
(\n) print
flush
quit
```

in a `.PS` / `.ps` file. That is exactly the pinned form:
**`gs`** reads the named source file and executes it, observe
`print` / `flush` at run time. Pinning Invoking Ghostscript / file
arguments lets excavate treat `ghostscript` / `postscript` + `print` /
`flush` / `quit` as **era evidence** (Ghostscript / PostScript source
file) without rewriting the fixture into a Distiller job, a full EPS
BoundingBox figure, or a Python port.

**Dialect precision:** this pin authorizes GPL Ghostscript gs reading of
the `print` / `flush` / `quit` / file-invocation shape only. It does
**not** claim the lost tree is period Adobe LaserWriter ROM, a specific
PostScript Language Level, Display PostScript, or a working CUPS filter
pipeline on this host. Those are other manuals / toolchains. HELLO's
"Ghostscript-ish / print subset" label remains **CONJECTURE** until a
dialect-specific vendor run is evidence — gs accepting the `print` shape
and printing the probe string is the VERIFIED claim for this leaf.
