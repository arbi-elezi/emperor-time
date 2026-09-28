# Jail pin — GNU bc DESCRIPTION file arguments + PSEUDO STATEMENTS `quit` + STATEMENTS `print` (HELLO.BC)

Contemporaneous manual pin for the lost-bc archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how bc
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-bc/HELLO.BC` with
runnable dialect **VERIFIED** as GNU bc 1.07.1
under Linux x86_64
(`bc HELLO.BC` / `bc -q HELLO.BC` →
`EMPEROR-TIME-BC-PROBE-OK`). Filename culture
(`.BC` / 8.3 caps → bc script *naming*) remains **CONJECTURE** only.
Identify fossils use `*.bc` only. Bare `bc` is allowed as a
route tag (tool binary name — word-boundary match does not false-hit
`bcpl`). Bare `.bc` is **refused** as a route tag (substring collision
with BCPL `.bcpl`). Companion to the dc leaf
(`references/archaeology-dc-manual.md`); both come from the GNU bc/dc
package family. This note supplies the Jail pin so excavate
can name the **verified** bc file-evaluation shape
without inventing a full POSIX bc / BSD bc / mathlib
suite claim for a `print`/`quit` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *bc(1)* — DESCRIPTION file arguments / STATEMENTS `print` / PSEUDO STATEMENTS `quit` |
| **Heading** | **DESCRIPTION** — files listed on the command line; **STATEMENTS** `print list`; **PSEUDO STATEMENTS** `quit` |
| **Dialect pinned** | **bc via GNU bc** with `print`/`quit` surface — **not** full POSIX bc / BSD bc / mathlib suite claim |
| **URL** | https://manpages.debian.org/trixie/bc/bc.1.en.html (bc(1)); package `bc` 1.07.1-4 on Debian trixie; GNU bc upstream https://www.gnu.org/software/bc/ ; installed `bc --version` |
| **Anchors** | command-line files processed before stdin; `print` extension for string output; `quit` terminates without waiting for stdin |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Debian trixie bc(1) DESCRIPTION / STATEMENTS / PSEUDO STATEMENTS)

> **SYNTAX**
> `bc [ -hlwsqv ] [long-options] [ file ... ]`

> **DESCRIPTION**
> bc starts by processing code from all the files listed on the command
> line in the order listed. After all files have been processed, bc
> reads from the standard input. All code is executed as it is read.
> (If a file contains a command to halt the processor, bc will never
> read from the standard input.)

> **STATEMENTS** — `print list`
> The print statement (an extension) provides another method of output.
> The "list" is a list of strings and expressions separated by commas.
> … No terminating newline is printed. … Strings in the print statement
> … may contain special characters. … "n" (newline) …

> **PSEUDO STATEMENTS** — `quit`
> When the quit statement is read, the bc processor is terminated,
> regardless of where the quit statement is found.

(Source: Debian manpages for package `bc` 1.07.1-4 on trixie,
https://manpages.debian.org/trixie/bc/bc.1.en.html sections
**SYNTAX**, **DESCRIPTION**, **STATEMENTS**, and **PSEUDO STATEMENTS**,
accessed 2026-09-28 Europe/Tirane.
Installed `bc --version` on GNU bc 1.07.1 matches the file-argument
surface. Probe uses `bc HELLO.BC` / `bc -q HELLO.BC` so the calculator
reads commands from the named script and exits via `quit`.
Unlike GNU dc, this GNU bc has **no** `-f` / `--file` option.)

### Why this heading (HELLO.BC / excavate)

A minimal HELLO surface looks like:

```bc
print "EMPEROR-TIME-BC-PROBE-OK\n"
quit
```

in a `.BC` / `.bc` file. That is exactly the pinned form:
**`bc FILE`** (optionally **`bc -q FILE`**) reads calculator commands
from the named script, observe string print at run time, halt via
`quit` so stdin is never entered. Pinning DESCRIPTION file arguments +
STATEMENTS `print` + PSEUDO STATEMENTS `quit` lets excavate treat
`bc` / `gnu-bc` + `print`/`quit` as **era evidence** (GNU bc /
bc script file) without rewriting the fixture into a shell one-liner,
a Python port, or an interactive stdin session. Bare `.bc` stays off
the route table so BCPL `.bcpl` utterances do not false-route here;
identify still surveys `*.bc` fossils on disk. Word-boundary matching
on bare `bc` already covers `hello.bc` utterances without the
extension tag.

**Dialect precision:** this pin authorizes GNU bc reading of
the `print`/`quit` / file-evaluation shape only. It does
**not** claim the lost tree is POSIX bc (`-s`) or BSD bc on this host.
Those are other manuals / toolchains. HELLO's "gnu-bc-ish / print
subset" label remains **CONJECTURE** until a dialect-specific vendor
run is evidence — GNU bc accepting the `print`/`quit` shape and
printing the probe string is the VERIFIED claim for this leaf.
