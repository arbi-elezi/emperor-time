# Jail pin — GNU Awk gawk -f file invocation (HELLO.AWK)

Contemporaneous manual pin for the lost-AWK archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how AWK
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-awk/HELLO.AWK` with
runnable dialect **VERIFIED** as GNU Awk 5.2.1
under Linux x86_64
(`gawk -f HELLO.AWK` →
`EMPEROR-TIME-AWK-PROBE-OK`). Filename culture
(`.AWK` / 8.3 caps → AWK *naming*) remains **CONJECTURE** only.
Identify fossils use `*.awk` only. Bare `awk` is allowed as a
route tag (POSIX / tool binary name — not an English collision like
`scheme` / `basic`, and not a two-letter collision like refused bare
`gs`). This note supplies the Jail pin so excavate
can name the **verified** gawk `-f` / `--file` program-file shape
without inventing a full POSIX awk / nawk / mawk / BusyBox / One True
Awk claim for a BEGIN/print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GAWK: Effective AWK Programming* — Running awk and gawk / Command-Line Options |
| **Heading** | **Command-Line Options** — `-f source-file` / `--file source-file` |
| **Dialect pinned** | **AWK via GNU Awk gawk** with `BEGIN` / `print` surface — **not** full POSIX awk / nawk / mawk / BusyBox / One True Awk claim |
| **URL** | https://www.gnu.org/software/gawk/manual/html_node/Options.html (Command-Line Options — `-f` / `--file`); package `gawk` 1:5.2.1-2+b1 on Debian trixie |
| **Anchors** | `-f source-file` / `--file source-file` — read awk program source from source-file instead of the first nonoption argument |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from GAWK: Effective AWK Programming — Command-Line Options)

> `-f source-file`
> `--file source-file`
>
> Read the awk program source from source-file
> instead of in the first nonoption argument.
> This option may be given multiple times; the awk
> program consists of the concatenation of the contents of
> each specified source-file.

(Source: GAWK: Effective AWK Programming — Command-Line Options,
https://www.gnu.org/software/gawk/manual/html_node/Options.html , accessed
2026-09-28 Europe/Tirane. Probe uses
`gawk -f HELLO.AWK` so the interpreter
loads and runs the named program file non-interactively.
`BEGIN` + `print` prints the probe string and exits. Bare
`gawk HELLO.AWK` without `-f` is not the verified form.)

### Why this heading (HELLO.AWK / excavate)

A minimal HELLO surface looks like:

```awk
BEGIN { print "EMPEROR-TIME-AWK-PROBE-OK" }
```

in a `.AWK` / `.awk` file. That is exactly the pinned form:
**`gawk -f`** loads and runs the named program file, observe
`print` at run time. Pinning Command-Line Options / `-f` /
`--file` lets excavate treat `gawk` / `awk` / `nawk` / `.awk` + `BEGIN` /
`print` as **era evidence** (GNU Awk / AWK source
file) without rewriting the fixture into a shell one-liner,
a Python port, or a sed script.

**Dialect precision:** this pin authorizes GNU Awk gawk reading of
the `BEGIN` / `print` / `-f` program-file shape only. It does
**not** claim the lost tree is POSIX awk, nawk, mawk, BusyBox awk,
or One True Awk on this host. Those are other manuals /
toolchains. HELLO's "gawk-ish / BEGIN print subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — gawk
accepting the `BEGIN`/`print` shape and printing the probe string is the
VERIFIED claim for this leaf.
