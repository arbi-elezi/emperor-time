# Jail pin — bash(1) ARGUMENTS (`bash` … file) for HELLO.sh

Contemporaneous manual pin for the lost-sh archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Bash
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-sh/HELLO.sh` with
runnable dialect **VERIFIED** as GNU Bash 5.2.37
under Linux x86_64
(`bash HELLO.sh` →
`EMPEROR-TIME-BASH-PROBE-OK`). Filename culture
(`.bash` / `.bashrc` / login shells) remains
**CONJECTURE** only for shell-startup / naming labels. Identify fossils use `*.sh` only
(no `*.bash` this leaf).
Bare `bash` is **allowed** as a route tag (tool binary name;
word-boundary). Bare `sh` is **refused** (POSIX / dash ambiguity;
verified toolchain is bash). Bare `.sh` is **allowed** as a route tag with
extension-boundary matching (does not prefix-hit peer forms
`.sha` / `.shar` / `.shtml`). Prefer `bash` /
`bash5` / `bash5.2` / `gnu-bash` / `.sh`.
Toolchain is Debian package `bash` 5.2.37-2+b10 providing
`/usr/bin/bash`. This note supplies
the Jail pin so excavate can name the **verified** Bash
file-argument script run shape without inventing a full POSIX sh /
dash / zsh / ksh suite claim for an
`echo` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *bash(1)* — ARGUMENTS / script-file invocation |
| **Heading** | **ARGUMENTS** — first remaining argument treated as a shell script file (`bash file`) |
| **Dialect pinned** | **Bash via GNU bash 5.2.37** with `echo` source → script-file run — **not** full POSIX sh / dash / zsh / ksh suite claim |
| **URL** | https://www.man7.org/linux/man-pages/man1/bash.1.html#ARGUMENTS (bash(1) — ARGUMENTS); Debian package `bash` 5.2.37-2+b10; installed `bash --version` |
| **Anchors** | `.sh` / script file path as first non-option argument; non-interactive script-file evaluation; `$0` set to the file name |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from bash(1) — ARGUMENTS)

> If arguments remain after option processing, and neither the `-c`
> nor the `-s` option has been supplied, the first argument is treated
> as the name of a file containing shell commands (a *shell script*).
> When bash is invoked in this fashion, `$0` is set to the name of the
> file, and the positional parameters are set to the remaining
> arguments. Bash reads and executes commands from this file, then
> exits.

(Source: bash(1), section
**ARGUMENTS**,
https://www.man7.org/linux/man-pages/man1/bash.1.html#ARGUMENTS
accessed 2026-09-28 Europe/Tirane.
Installed `bash --version` reports GNU bash 5.2.37 and matches the
script-file argument surface. Probe uses
`bash HELLO.sh` so bash
loads and runs the named script non-interactively and prints the probe
string. Language: Bash — see also the GNU Bash Reference Manual.)

### Why this heading (HELLO.sh / excavate)

A minimal HELLO surface looks like:

```bash
#!/usr/bin/env bash
echo "EMPEROR-TIME-BASH-PROBE-OK"
```

in a `.sh` file. That is exactly the pinned form:
**`bash FILE.sh`**, observe string print at run time.
Pinning bash(1) ARGUMENTS lets excavate treat
`bash` / `bash5` / `bash5.2` / `gnu-bash` / `.sh` + `echo`
as **era evidence** (Bash / script-file run) without rewriting the
fixture into a dash one-liner, a Python port, or an interactive REPL.
Identify surveys `*.sh` fossils on disk. `.sh` extension (boundary-safe
vs `.sha` / `.shar` / `.shtml`) and `bash` /
`bash5` / `bash5.2` tags cover excavate intent. bare `sh` is not the verified
toolchain.
