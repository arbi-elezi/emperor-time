# Jail pin — Iron Spring PL/I plic `-C` / standalone ld `-lprf` (HELLO.PLI)

Contemporaneous manual pin for the lost-PL/I archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how PL/I
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-pli/HELLO.PLI` with
runnable dialect **VERIFIED** as Iron Spring PL/I compiler 1.4.1
(Linux, 15 Apr 2026) under Linux x86_64
(`plic -C -lixg -ew HELLO.PLI -o hello.o` then
`ld … --oformat=elf32-i386 -melf_i386 -lprf` then `./hello` →
`EMPEROR-TIME-PLI-PROBE-OK`). Filename culture (`.PLI` / 8.3 caps → PL/I
*naming*) remains **CONJECTURE** only. Identify fossils use `*.pli` and
`*.pl1`. This note supplies the Jail pin so excavate can name the
**verified** plic `-C` / ld `-lprf` shape without inventing a full period
IBM MVS/VM / Enterprise claim for a print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Iron Spring PL/I Compiler Programming Guide* Version 1.4.1 — Running the Compiler / plic command syntax |
| **Heading** | **Running the Compiler** — `plic [<options>] <input files> [-o <output file>]`; output option `-C` = generate compiled (object) output |
| **Dialect pinned** | **PL/I via Iron Spring plic** with `PROCEDURE OPTIONS(MAIN)` / `PUT SKIP LIST` print surface — **not** full IBM MVS/VM / Enterprise / STREAM EDIT claim |
| **URL** | http://www.iron-spring.com/prog_guide.html (Running the Compiler); distribution http://www.iron-spring.com/pli-1.4.1.tgz ; Linux link notes http://www.iron-spring.com/readme_linux.html (Using the compiler / SA_make) |
| **Anchors** | Running the Compiler — `-C = generate compiled (object) output`; readme_linux Linking / SA_make `ld … -e main … -lprf` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Iron Spring Programming Guide — Running the Compiler)

> The "plic" command is used to invoke the compiler.
>
> `plic [<options>] <input files> [-o <output file>]`
>
> `<output option> = -S | -C | -L`
> `-C` = generate compiled (object) output.

(Probe uses `plic -C -lixg -ew HELLO.PLI -o hello.o`, then the
readme_linux / SA_make standalone link form
`ld -z muldefs -Bstatic -e main … --oformat=elf32-i386 -melf_i386 -lprf`,
then runs the executable. `PUT SKIP LIST` prints the probe string;
list-directed output may pad a trailing space before the newline.)

### Why this heading (HELLO.PLI / excavate)

A minimal HELLO surface looks like:

```pli
HELLO: procedure options(main);
  put skip list('EMPEROR-TIME-PLI-PROBE-OK');
end HELLO;
```

in a `.PLI` / `.pli` / `.pl1` file. That is exactly the pinned form:
**`plic -C`** compiles the named source to an ELF object, then **`ld … -lprf`**
links the Iron Spring static runtime and the program runs, observe
`PUT SKIP LIST` at run time. Pinning Running the Compiler / `-C` +
standalone `-lprf` lets excavate treat `plic` / `pli` / `pl1` /
`iron-spring` / `.pli` / `.pl1` + `PROCEDURE OPTIONS(MAIN)` / `PUT SKIP LIST`
as **era evidence** (Iron Spring PL/I / source file) without rewriting the
fixture into mainframe JCL, Enterprise STREAM EDIT, or a Python port.

**Dialect precision:** this pin authorizes Iron Spring plic reading of the
`PROCEDURE OPTIONS(MAIN)` / `PUT SKIP LIST` / `plic -C` + `ld -lprf` shape
only. It does **not** claim the lost tree is period IBM PL/I for MVS and VM
on original media, a specific Enterprise release, or a working shared-object
(PIC) build on this host. Those are other manuals / toolchains.
HELLO's "Iron-Spring-ish / PUT LIST subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence —
plic accepting the `PUT SKIP LIST` shape and printing the probe string is
the VERIFIED claim for this leaf.
