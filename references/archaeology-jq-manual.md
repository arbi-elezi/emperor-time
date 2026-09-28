# Jail pin — jq Invoking jq (`-f` / `--from-file` …) for HELLO.jq

Contemporaneous manual pin for the lost-jq archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how jq
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-jq/HELLO.jq` with
runnable dialect **VERIFIED** as jq 1.7 CLI
under Linux x86_64
(`jq -nr -f HELLO.jq` →
`EMPEROR-TIME-JQ-PROBE-OK`). Filename culture
(`.jquery` / browser jQuery) remains
**CONJECTURE** only for naming collisions. Identify fossils use `*.jq` only.
Bare `jq` is **allowed** as a route tag (tool binary name;
word-boundary). Bare `.jq` is **allowed** as a route tag with
extension-boundary matching (does not prefix-hit peer forms
`.jquery`). Prefer `jq` /
`jq1.7` / `jqlang` / `.jq`.
Toolchain is Debian package `jq` 1.7.1-6+deb13u4 providing
`/usr/bin/jq`. This note supplies
the Jail pin so excavate can name the **verified** jq
CLI `-f` from-file filter-evaluation shape without inventing a full gojq /
jaq / JSONPath suite claim for a
string-literal probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *jq 1.7 Manual — Invoking jq* |
| **Heading** | **Invoking jq** — `-f filename` / `--from-file filename` reads the filter from a file; `-n` / `--null-input` runs once on `null`; `-r` / `--raw-output` writes strings without JSON quotes |
| **Dialect pinned** | **jq 1.7 CLI** with string-literal filter source → `-nr -f` file evaluation — **not** full gojq / jaq / JSONPath suite claim |
| **URL** | https://jqlang.github.io/jq/manual/v1.7/ (jq 1.7 Manual — Invoking jq); Debian package `jq` 1.7.1-6+deb13u4; installed `jq --version` |
| **Anchors** | `.jq` / filter file path as `-f` argument; `-n` null-input; `-r` raw-output; filter is a program (not JSON data alone) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from jq 1.7 Manual — Invoking jq)

> You can affect how jq reads and writes its input and output using some
> command-line options:
>
> - `--null-input` / `-n`:
>
> Don't read any input at all. Instead, the filter is run once using
> `null` as the input. This is useful when using jq as a simple
> calculator or to construct JSON data from scratch.
>
> - `--raw-output` / `-r`:
>
> With this option, if the filter's result is a string then it will be
> written directly to standard output rather than being formatted as a
> JSON string with quotes. This can be useful for making jq filters talk
> to non-JSON-based systems.
>
> - `-f filename` / `--from-file filename`:
>
> Read filter from the file rather than from a command line, like awk's
> -f option. You can also use '#' to make comments.

(Source: jq 1.7 Manual, section
**Invoking jq**,
https://jqlang.github.io/jq/manual/v1.7/
accessed 2026-09-28 Europe/Tirane.
Installed `jq --version` reports jq-1.7 and matches the
CLI `-f` / `-n` / `-r` surface. Probe uses
`jq -nr -f HELLO.jq` so jq
loads and runs the named filter non-interactively with null input and
raw string output and prints the probe
string. Language: jq — see also the jq Manual.)

### Why this heading (HELLO.jq / excavate)

A minimal HELLO surface looks like:

```jq
"EMPEROR-TIME-JQ-PROBE-OK"
```

in a `.jq` file. That is exactly the pinned form:
**`jq -nr -f FILE.jq`**, observe string print at run time.

### Honesty

- VERIFIED: Debian `jq` 1.7.1 `-nr -f` on this HELLO.
- CONJECTURE: any claim that `.jquery` browser assets are this dialect.
- UNVERIFIABLE: gojq / jaq / jq 1.8+ / JSONPath recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size).
