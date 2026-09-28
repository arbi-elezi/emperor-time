# Jail pin — GNU sed sed -f script-file invocation (HELLO.SED)

Contemporaneous manual pin for the lost-sed archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how sed
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-sed/HELLO.SED` with
runnable dialect **VERIFIED** as GNU sed 4.9
under Linux x86_64
(`printf 'probe-input\n' | sed -f HELLO.SED` →
`EMPEROR-TIME-SED-PROBE-OK`). Filename culture
(`.SED` / 8.3 caps → sed *naming*) remains **CONJECTURE** only.
Identify fossils use `*.sed` only. Bare `sed` is allowed as a
route tag (POSIX / tool binary name — not an English collision like
`scheme` / `basic`, and not a two-letter collision like refused bare
`gs`). This note supplies the Jail pin so excavate
can name the **verified** sed `-f` / `--file` script-file shape
without inventing a full POSIX sed / BSD sed / BusyBox sed claim for
an `s///` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *sed, a stream editor* — Running sed / Command-Line Options |
| **Heading** | **Command-Line Options** — `-f script-file` / `--file=script-file` |
| **Dialect pinned** | **sed via GNU sed** with `s///` substitute surface — **not** full POSIX sed / BSD sed / BusyBox sed claim |
| **URL** | https://www.gnu.org/software/sed/manual/html_node/Command_002dLine-Options.html (Command-Line Options — `-f` / `--file`); package `sed` 4.9-2+deb13u1 on Debian trixie; Invoking sed TOC confirmed at https://www.gnu.org/software/sed/manual/html_node/Invoking-sed.html |
| **Anchors** | `-f script-file` / `--file=script-file` — add the contents of script-file to the commands to be executed |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from GNU sed 4.9 `--help` / Command-Line Options anchors)

> `-f script-file, --file=script-file`
>                  add the contents of script-file to the commands to be executed

(Source: installed `sed --help` on GNU sed 4.9, matching the Command-Line
Options anchors documented at
https://www.gnu.org/software/sed/manual/html_node/Command_002dLine-Options.html ,
accessed 2026-09-28 Europe/Tirane. Invoking sed chapter TOC lists
Command-Line Options under Running sed. Probe uses
`sed -f HELLO.SED` so the editor loads the named script file and applies
it to the input stream non-interactively.
`s/.*/…/` replaces the pattern space and prints the probe string.
Bare `sed HELLO.SED` without `-f` is not the verified form.)

### Why this heading (HELLO.SED / excavate)

A minimal HELLO surface looks like:

```sed
# EMPEROR-TIME SED PROBE
s/.*/EMPEROR-TIME-SED-PROBE-OK/
```

in a `.SED` / `.sed` file. That is exactly the pinned form:
**`sed -f`** loads and runs the named script file against stdin / file
args, observe substitute at run time. Pinning Command-Line Options / `-f` /
`--file` lets excavate treat `sed` / `gsed` / `.sed` + `s///` as
**era evidence** (GNU sed / sed script
file) without rewriting the fixture into a shell one-liner,
a Python port, or an awk script.

**Dialect precision:** this pin authorizes GNU sed reading of
the `s///` / `-f` script-file shape only. It does
**not** claim the lost tree is POSIX sed, BSD sed, or BusyBox sed
on this host. Those are other manuals /
toolchains. HELLO's "gsed-ish / substitute subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — GNU sed
accepting the `s///` shape and printing the probe string is the
VERIFIED claim for this leaf.
