# Jail pin — Assembler section heading (FOO.ASM)

Contemporaneous manual pin for the lost-asm archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how assembly
works” stays **CONJECTURE** until an assemble/link/run is ledgered.

**Related work:** merged PR [#10](https://github.com/arbi-elezi/emperor-time/pull/10)
(`et-manager/archaeology-asm-probe`) adds `evals/fixtures/lost-asm/FOO.ASM`
with runnable dialect **VERIFIED** as NASM Intel-syntax Linux x86-64 ELF
(syscalls; `nasm -f elf64` + GNU `ld`). Filename culture (`.ASM` / 8.3 caps
→ late-DOS / MASM-adjacent *naming*) remains **CONJECTURE** only. This note
does **not** depend on rewriting that fixture; it only supplies the Jail pin
so excavate can name the **verified** dialect without inventing a MASM/DOS
manual for a NASM probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *NASM — The Netwide Assembler*, version **2.16.03** (matches probe toolchain) |
| **Heading** | **7.3 `SECTION` or `SEGMENT`: Changing and Defining Sections** |
| **Dialect pinned** | **NASM** Intel syntax, Unix/`elf64` section names — **not** MASM, **not** TASM, **not** DOS `.COM` / 16-bit `INT 21h`, **not** AT&T `gas` |
| **URL** | https://www.nasm.us/xdoc/2.16.03/html/nasmdoc7.html |
| **Access date** | 2026-09-27 |

### Quote (from §7.3)

> **7.3 `SECTION` or `SEGMENT`: Changing and Defining Sections**
>
> The `SECTION` directive (`SEGMENT` is an exactly equivalent synonym)
> changes which section of the output file the code you write will be
> assembled into. In some object file formats, the number and names of
> sections are fixed; in others, the user may make up as many as they wish.
>
> The Unix object formats, and the `bin` object format (but see section
> 8.1.3), all support the standardized section names `.text`, `.data` and
> `.bss` for the code, data and uninitialized-data sections.

### Why this heading (FOO.ASM / excavate)

A minimal FOO surface looks like:

```asm
        global  _start

        section .data
msg:    db      "EMPEROR-TIME-ASM-PROBE-OK", 10
len:    equ     $ - msg

        section .text
_start:
        ; sys_write / sys_exit via syscall
```

That is exactly the NASM Unix section form: `section .data` / `section .text`
as named in §7.3, plus a `GLOBAL` entry symbol for the linker. Pinning §7.3
lets excavate treat `section` / `.text` / `.data` as **era evidence** (NASM
Unix ELF layout) without rewriting the fixture into MASM `SEGMENT` /
`MODEL`, a DOS `.COM` `ORG 100h` program, or a Python port.

**Dialect precision:** this pin authorizes NASM reading of the section names
and switch form only. It does **not** claim the lost tree is Microsoft MASM,
Borland TASM, 16-bit DOS, or GNU `as` AT&T syntax. Those are other manuals.
FOO’s “DOS-era 8.3 filename culture” label in PR #10 remains **CONJECTURE**;
the binary that prints is NASM+ld ELF64 — **VERIFIED** in
`evals/fixtures/lost-asm/PROBE.md` (nasm 2.16.03, `nasm -f elf64`).

### How it informs excavate without modernizing

1. Match the artifact’s section switches to the pinned names (`.text` /
   `.data` / `.bss`) under a NASM Unix/`elf*` output format.
2. Prefer the same surface toolchain already ledgered (`nasm -f elf64` +
   `ld`) — do not invent `SEGMENT _TEXT`, `MODEL SMALL`, `INT 21h`, or AT&T
   `%`-registers absent from the source.
3. Record any dialect leap (e.g. rewriting for MASM/DOSBox, or `gas` AT&T)
   as **CONJECTURE** or **VERIFIED** with a quoted run, separate from this
   pin.

---

## Corroboration (not the pin)

Same manual, adjacent headings — useful for `_start` export and the
`db`/`equ $-label` length idiom FOO uses, but **§7.3 remains the Jail pin**
(one heading).

| Field | Value |
|-------|--------|
| **Manual** | *NASM — The Netwide Assembler* 2.16.03 |
| **Heading** | **7.7 `GLOBAL`: Exporting Symbols to Other Modules** |
| **URL** | https://www.nasm.us/xdoc/2.16.03/html/nasmdoc7.html |
| **Access date** | 2026-09-27 |

> `GLOBAL` is the other end of `EXTERN`: if one module declares a symbol as
> `EXTERN` and refers to it, then in order to prevent linker errors, some
> other module must actually define the symbol and declare it as `GLOBAL`.
>
> ```
> global _main
> _main:
>         ; some code
> ```

| Field | Value |
|-------|--------|
| **Manual** | *NASM — The Netwide Assembler* 2.16.03 |
| **Heading** | **3.2.4 `EQU`: Defining Constants** |
| **URL** | https://www.nasm.us/xdoc/2.16.03/html/nasmdoc3.html |
| **Access date** | 2026-09-27 |

> ```
> message         db      'hello, world'
> msglen          equ     $-message
> ```
>
> defines `msglen` to be the constant 12.

| Field | Value |
|-------|--------|
| **Manual** | *NASM — The Netwide Assembler* 2.16.03 |
| **Heading** | **8.9 `elf32`, `elf64`, `elfx32`: Executable and Linkable Format Object Files** |
| **URL** | https://www.nasm.us/xdoc/2.16.03/html/nasmdoc8.html |
| **Access date** | 2026-09-27 |

> The `elf32`, `elf64` and `elfx32` output formats generate `ELF32 and
> ELF64` (Executable and Linkable Format) object files, as used by Linux as
> well as Unix System V…

A blog post about “hello world in assembly” or an Intel SDM opcode page is
**secondary** and must not replace the NASM §7.3 URL above. A MASM/DOS
manual would pin a **different** dialect than the verified probe — do not
substitute it for this Jail pin.
