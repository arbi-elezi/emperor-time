# Jail pin — Expect SYNOPSIS cmdfile + USAGE script-file evaluation (HELLO.EXP)

Contemporaneous manual pin for the lost-expect archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Expect
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-expect/HELLO.EXP` with
runnable dialect **VERIFIED** as Expect 5.45.4
under Linux x86_64
(`expect HELLO.EXP` →
`EMPEROR-TIME-EXPECT-PROBE-OK`). Filename culture
(`.EXP` / 8.3 caps → Expect script *naming*) remains **CONJECTURE** only.
Identify fossils use `*.exp` only. Bare `expect` is allowed as a
route tag (tool binary name — word-boundary match). Bare `.exp` is
**allowed** as a route tag (no known peer excavate substring collision).
Companion to the Tcl leaf
(`references/archaeology-tcl-manual.md`); Expect is Don Libes'
Tcl-based programmed-dialogue tool (Debian packages `expect` /
`tcl-expect`). This note supplies the Jail pin so excavate
can name the **verified** Expect cmdfile-evaluation shape
without inventing a full spawn/expect/send dialogue
suite claim for a `puts`/`exit` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *expect(1)* — SYNOPSIS cmdfile / USAGE script-file evaluation |
| **Heading** | **SYNOPSIS** — `expect … [ [ - [f| b] ] cmdfile ]`; **USAGE** — Expect reads cmdfile for a list of commands to execute |
| **Dialect pinned** | **Expect via Don Libes Expect 5** with `puts`/`exit` cmdfile surface — **not** full spawn/expect/send / Expectk / libexpect suite claim |
| **URL** | https://manpages.debian.org/trixie/expect/expect.1.en.html (expect(1)); package `expect` 5.45.4-4 on Debian trixie; installed `expect -v` |
| **Anchors** | cmdfile on the command line; `-f` optional (#! notation); Tcl `puts` for string output; `exit` status terminates |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Debian trixie expect(1) SYNOPSIS / USAGE)

> **SYNOPSIS**
> `expect [ -dDinN ] [ -c cmds ] [ [ - [f| b] ] cmdfile ] [ args ]`

> **USAGE**
> Expect reads cmdfile for a list of commands to execute. Expect may also
> be invoked implicitly on systems which support the #! notation by
> marking the script executable, and making the first line in your script:
>
> `#!/usr/bin/expect -f`
>
> …
>
> The -f flag prefaces a file from which to read commands from. The flag
> itself is optional as it is only useful when using the #! notation …

> **COMMANDS** — `exit` / Tcl `puts`
> Expect uses Tcl (Tool Command Language). … `exit [-opts] [status]`
> causes Expect to exit … status (or 0 if not specified) is returned as
> the exit status of Expect. exit is implicitly executed if the end of
> the script is reached.

(Source: Debian manpages for package `expect` 5.45.4-4 on trixie,
https://manpages.debian.org/trixie/expect/expect.1.en.html sections
**SYNOPSIS**, **USAGE**, and **COMMANDS**,
accessed 2026-09-28 Europe/Tirane.
Installed `expect -v` reports Expect version 5.45.4 and matches the
cmdfile surface. Probe uses `expect HELLO.EXP` so Expect reads commands
from the named script and exits via `exit 0`. Author credit: Don Libes,
NIST — see AUTHOR / SEE ALSO "Exploring Expect".)

### Why this heading (HELLO.EXP / excavate)

A minimal HELLO surface looks like:

```tcl
puts "EMPEROR-TIME-EXPECT-PROBE-OK"
exit 0
```

in a `.EXP` / `.exp` file. That is exactly the pinned form:
**`expect FILE`** (optionally **`expect -f FILE`**) reads Expect/Tcl
commands from the named script, observe string print at run time, halt via
`exit`. Pinning SYNOPSIS cmdfile + USAGE script-file evaluation lets
excavate treat `expect` / `tcl-expect` / `.exp` + `puts`/`exit` as
**era evidence** (Don Libes Expect / Expect script file) without rewriting
the fixture into a shell one-liner, a Python port, or an interactive
spawn/expect/send session. Identify surveys `*.exp` fossils on disk.
Word-boundary matching on bare `expect` covers `hello.exp` utterances
alongside the `.exp` extension tag.

**Dialect precision:** this pin authorizes Expect reading of
the `puts`/`exit` / cmdfile-evaluation shape only. It does
**not** claim the lost tree is Expectk, libexpect(3), or a full
spawn/expect/send dialogue recovery on this host.
Those are other manuals / toolchains. HELLO's "expect-ish / puts
subset" label remains **CONJECTURE** until a dialect-specific vendor
run is evidence — Expect accepting the `puts`/`exit` shape and
printing the probe string is the VERIFIED claim for this leaf.
