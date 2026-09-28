# Jail pin — GNU Make make(1) DESCRIPTION / OPTIONS `-f` (Makefile)

Contemporaneous manual pin for the lost-make archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how make
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-make/Makefile` with
runnable dialect **VERIFIED** as GNU Make 4.4.1
under Linux x86_64
(`make -C evals/fixtures/lost-make` / `make -f HELLO.MK` →
`EMPEROR-TIME-MAKE-PROBE-OK`). Filename culture
(`Makefile` / `HELLO.MK` → make *naming*) remains **CONJECTURE** only.
Identify fossils use `Makefile` / `makefile` / `*.mak` / `*.mk`.
Bare English `make` is **refused** as a route tag (factory speech
collision with "make software" / common English — unlike bare `ed` /
`m4` / `sed` / `awk` tool-binary tags). Prefer `gmake` / `gnu-make` /
`.mk` / `.mak` / `makefile`. This note supplies the Jail pin so excavate
can name the **verified** default-name / `-f` makefile shape
without inventing a full POSIX make / BSD make / Automake
suite claim for a `.PHONY`/`echo` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GNU Make* — make(1) DESCRIPTION (default makefile names) + OPTIONS `-f` / `--file` / `--makefile` |
| **Heading** | **DESCRIPTION / OPTIONS** — look for `GNUmakefile`, `makefile`, `Makefile`; `-f file` use file as a makefile |
| **Dialect pinned** | **make via GNU Make** with `.PHONY`/`echo` surface — **not** full POSIX make / BSD make / Automake suite claim |
| **URL** | https://manpages.debian.org/trixie/make/make.1.en.html (make(1) DESCRIPTION + OPTIONS `-f`); package `make` 4.4.1-2 on Debian trixie; project https://www.gnu.org/software/make/ ; installed `make --help` `-f FILE, --file=FILE, --makefile=FILE` |
| **Anchors** | default search `GNUmakefile`, `makefile`, `Makefile`; `-f file` / `--file` / `--makefile` use file as a makefile |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Debian make(1) DESCRIPTION / OPTIONS + installed `make --help`)

> If no `-f` option is present, make will look for the makefiles
> `GNUmakefile`, `makefile`, and `Makefile`, in that order.
> Normally you should call your makefile either `makefile` or
> `Makefile`.

> `-f file`, `--file=file`, `--makefile=FILE`
> Use file as a makefile.

(Source: Debian trixie `make` 4.4.1-2 man page make(1) at
https://manpages.debian.org/trixie/make/make.1.en.html ,
accessed 2026-09-28 Europe/Tirane. Installed `make --help` on GNU Make
4.4.1 matches: `-f FILE, --file=FILE, --makefile=FILE` /
`Read FILE as a makefile`. Probe uses `make -C lost-make` so the
utility loads the default-name `Makefile`, and `make -f HELLO.MK` for
the explicit file form.
`.PHONY: all` / `@echo …` prints the probe string.)

### Why this heading (Makefile / excavate)

A minimal HELLO surface looks like:

```make
.PHONY: all
all:
	@echo EMPEROR-TIME-MAKE-PROBE-OK
```

in a `Makefile` / `HELLO.MK` file. That is exactly the pinned form:
**default-name `Makefile`** or **`make -f FILE`** reads and runs the
named makefile recipe, observe echo at run time. Pinning make(1)
DESCRIPTION / OPTIONS `-f` lets excavate treat `gmake` / `gnu-make` /
`.mk` / `.mak` / `makefile` + recipe tabs as
**era evidence** (GNU Make / makefile
file) without rewriting the fixture into a shell one-liner,
a Python port, or a CMakeLists.txt.

**Dialect precision:** this pin authorizes GNU Make reading of
the `.PHONY`/`echo` / default-name / `-f` shape only. It does
**not** claim the lost tree is POSIX make, BSD make, or Automake
on this host. Those are other manuals /
toolchains. HELLO's "gmake-ish / recipe subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — GNU Make
accepting the `.PHONY`/`echo` shape and printing the probe string is the
VERIFIED claim for this leaf.

**Route honesty:** bare English `make` is refused so factory utterances
like "make software" do not MUST-route to excavate. Use `gmake` /
`gnu-make` / `.mk` / `.mak` / `makefile` (filename token).
