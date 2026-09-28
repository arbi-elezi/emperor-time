# Jail pin — GCC Overall Options (`file.c` / `-o file`) for HELLO.c

Contemporaneous manual pin for the lost-c archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how C
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-c/HELLO.c` with
runnable dialect **VERIFIED** as GCC 14.2.0
under Linux x86_64
(`gcc HELLO.c -o HELLO` → `./HELLO` →
`EMPEROR-TIME-C-PROBE-OK`). Filename culture
(`.C` uppercase → C++ per GCC; 8.3 caps → C source *naming*) remains
**CONJECTURE** only for era labels. Identify fossils use `*.c` only.
Bare `c` is **refused** as a route tag (single-letter / common-English
collision). Bare `.c` is **allowed** as a route tag with
extension-boundary matching (does not prefix-hit peer excavate fossils
`.cbl` / `.cl`). Prefer `gcc` / `gcc14` / `c11` / `.c`.
Debian packages `gcc` (4:14.2.0-1) / `gcc-14` (14.2.0-19) provide
`/usr/bin/gcc`. This note supplies the Jail pin so excavate
can name the **verified** C compile-and-run shape
without inventing a full ISO C / multi-TU / linker-script
suite claim for a `puts` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Using the GNU Compiler Collection (GCC)* — 3.2 Options Controlling the Kind of Output (Overall Options) |
| **Heading** | **Options Controlling the Kind of Output** — `file.c` is C source that must be preprocessed; `-o file` places the primary output |
| **Dialect pinned** | **C via GCC 14.2** with `main` + `puts` compile-then-run surface — **not** full ISO C / multi-TU / freestanding suite claim |
| **URL** | https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gcc/Overall-Options.html (GCC 14.2.0 — Overall Options / Options Controlling the Kind of Output); packages `gcc` 4:14.2.0-1 / `gcc-14` 14.2.0-19 on Debian trixie; installed `gcc --version` |
| **Anchors** | `file.c` → C source that must be preprocessed; `-o file` names executable; default `a.out` when `-o` omitted; `puts` / stdio for string output; binary run after compile |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Using the GNU Compiler Collection (GCC) — Overall Options)

> For any given input file, the file name suffix determines what kind of
> compilation is done:
>
> **file.c**
> C source code that must be preprocessed.
>
> …
>
> **-o file**
> Place the primary output in file *file*. This applies to whatever
> sort of output is being produced, whether it be an executable file, an
> object file, an assembler file or preprocessed C code.
>
> If `-o` is not specified, the default is to put an executable
> file in `a.out`…

(Source: Using the GNU Compiler Collection (GCC) 14.2.0, section
**3.2 Options Controlling the Kind of Output**,
https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gcc/Overall-Options.html
accessed 2026-09-28 Europe/Tirane.
Installed `gcc --version` reports 14.2.0 and matches the
compile-then-run surface. Probe uses `gcc HELLO.c -o HELLO` then
`./HELLO` so gcc compiles the C translation unit and the binary prints
the probe string. Language: C — see also ISO/IEC 9899.)

### Why this heading (HELLO.c / excavate)

A minimal HELLO surface looks like:

```c
#include <stdio.h>

int main(void) {
    puts("EMPEROR-TIME-C-PROBE-OK");
    return 0;
}
```

in a `.c` file (lowercase). That is exactly the pinned form:
**`gcc FILE.c -o OUT`** then run the produced binary, observe string print at run time.
Pinning GCC Overall Options lets excavate treat `gcc` /
`gcc14` / `c11` / `.c` + `puts` as **era evidence** (C / C source
file) without rewriting the fixture into a shell one-liner, a Python
port, or an interactive REPL. Identify surveys `*.c` fossils on
disk. `.c` extension (boundary-safe) and `gcc` / `gcc14` / `c11` tags cover excavate intent.
