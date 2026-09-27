# Jail pin — tclsh SCRIPT FILES (HELLO.TCL)

Contemporaneous manual pin for the lost-Tcl archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Tcl
works” stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-tcl/HELLO.TCL` with
runnable dialect **VERIFIED** as Tcl 8.6.16
(`tclsh HELLO.TCL`). Filename culture (`.TCL` / 8.3 caps → Tcl
*naming*) remains **CONJECTURE** only. Identify fossils use `*.tcl` /
`*.tk`. This note supplies the Jail pin so excavate can name the
**verified** non-interactive script-file shape without inventing a Tk /
Expect vendor manual for a `tclsh` Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *tclsh* manual page — Tcl 8.6 Applications (matches probe toolchain family) |
| **Heading** | **SCRIPT FILES** — when `tclsh` is invoked with a fileName, it reads Tcl commands from that file and exits at EOF (no interactive REPL) |
| **Dialect pinned** | **Tcl 8.6** script file with `puts` — **not** Expect, **not** a specific TIP year claim, **not** a Wish/Tk GUI claim |
| **URL** | https://www.tcl-lang.org/man/tcl8.6/UserCmd/tclsh.htm |
| **Anchors** | SCRIPT FILES (batch / application file run) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from SCRIPT FILES)

> If tclsh is invoked with arguments then the first few arguments specify the name of a script file, and, optionally, the encoding of the text data stored in that script file. Any additional arguments are made available to the script as variables (see below). Instead of reading commands from standard input tclsh will read Tcl commands from the named file; tclsh will exit when it reaches the end of the file.

(Tcl 8.6.16 / Debian `tcl` 8.6.16 document the invoke surface used by probe
`tclsh HELLO.TCL`.)

### Why this heading (HELLO.TCL / excavate)

A minimal HELLO surface looks like:

```tcl
puts "EMPEROR-TIME-TCL-PROBE-OK"
```

in a `.TCL` / `.tcl` / `.tk` file. That is exactly the pinned form:
`tclsh` **runs the named script file** non-interactively (no REPL),
observe `puts` output at run time. Pinning SCRIPT FILES lets excavate
treat puts + script-file as **era evidence** (Tcl interpreter / source
file) without rewriting the fixture into Tk widgets, Expect, or a Python
port.

**Dialect precision:** this pin authorizes Tcl reading of the `puts` /
`.tcl` shape only. It does **not** claim the lost tree is a specific TIP,
Expect, or Wish GUI. Those are other manuals. HELLO’s “Tcl 8.x-ish”
label remains **CONJECTURE** until a dialect-specific vendor run is
evidence — `tclsh` accepting the puts shape is the VERIFIED claim for
this leaf.
