# Jail pin — GNU dc DESCRIPTION / OPTIONS `-f` / `--file` (HELLO.DC)

Contemporaneous manual pin for the lost-dc archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how dc
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-dc/HELLO.DC` with
runnable dialect **VERIFIED** as GNU dc 1.4.1 (GNU bc 1.07.1)
under Linux x86_64
(`dc -f HELLO.DC` / `dc HELLO.DC` →
`EMPEROR-TIME-DC-PROBE-OK`). Filename culture
(`.DC` / 8.3 caps → dc script *naming*) remains **CONJECTURE** only.
Identify fossils use `*.dc` only. Bare `dc` is allowed as a
route tag (tool binary name — not an English collision like
`scheme` / `basic`, and not a factory collision like refused bare
`make`). This note supplies the Jail pin so excavate
can name the **verified** dc file-evaluation shape
without inventing a full POSIX dc / BSD dc / AT&T Seventh Edition dc
suite claim for a `[string]P` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *dc(1)* — DESCRIPTION file arguments / OPTIONS `-f` / `--file` |
| **Heading** | **DESCRIPTION** — filenames on the command line; **OPTIONS** `-f` / `--file=script-file` |
| **Dialect pinned** | **dc via GNU dc** with `[string]P` surface — **not** full POSIX dc / BSD dc / AT&T Seventh Edition dc suite claim |
| **URL** | https://manpages.debian.org/trixie/dc/dc.1.en.html (dc(1)); package `dc` 1.07.1-4 on Debian trixie; GNU bc/dc upstream https://www.gnu.org/software/bc/ ; installed `dc --help` |
| **Anchors** | command-line filenames executed before stdin; `-f` / `--file` add file commands to the run set |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Debian trixie dc(1) DESCRIPTION / OPTIONS)

> Normally dc reads from the standard input; if any command arguments
> are given to it, they are filenames, and dc reads and executes the
> contents of the files before reading from standard input.

> `-f script-file` / `--file=script-file`
> Add the commands contained in the file script-file to the set of
> commands to be run while processing the input.

(Source: Debian manpages for package `dc` 1.07.1-4 on trixie,
https://manpages.debian.org/trixie/dc/dc.1.en.html sections
**DESCRIPTION** and **OPTIONS**, accessed 2026-09-28 Europe/Tirane.
Installed `dc --help` on GNU dc 1.4.1 matches:
`-f, --file=FILE  evaluate contents of file`.
Probe uses `dc -f HELLO.DC` / `dc HELLO.DC` so the calculator reads
commands from the named script non-interactively.
`[EMPEROR-TIME-DC-PROBE-OK]P` pushes a string and prints it without a
trailing newline — see Printing Commands `P` and Strings
`[characters]` on the same man page.)

### Why this heading (HELLO.DC / excavate)

A minimal HELLO surface looks like:

```dc
[EMPEROR-TIME-DC-PROBE-OK]P
```

in a `.DC` / `.dc` file. That is exactly the pinned form:
**`dc -f FILE`** (or positional `dc FILE`) reads calculator commands
from the named script, observe string print at run time. Pinning
DESCRIPTION / OPTIONS `-f` / `--file` lets excavate treat
`dc` / `gnu-dc` / `.dc` + `[string]P` as **era evidence** (GNU dc /
dc script file) without rewriting the fixture into a shell one-liner,
a Python port, or an interactive stdin session.

**Dialect precision:** this pin authorizes GNU dc reading of
the `[string]P` / file-evaluation shape only. It does
**not** claim the lost tree is POSIX dc, BSD dc, or AT&T Seventh
Edition dc on this host. Those are other manuals /
toolchains. HELLO's "gnu-dc-ish / string-print subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — GNU dc
accepting the `[string]P` shape and printing the probe string is the
VERIFIED claim for this leaf.
