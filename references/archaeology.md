# Digital coding archaeology

Load when the client hands a lost, ancient, incomplete, or hostile codebase:
no README, dead compiler, Pascal from a floppy image, raw assembly, a ROM,
a forum post that is the only spec.

The factory still applies. The unit of software is **recovered behavior**.

## Loop

```
survey artifacts
  → name the era and toolchain from evidence (CONJECTURE until a compiler/sim runs)
  → hunt manuals/specs on the public net (two sources or a quoted run)
  → recreate ONE runnable probe (assemble, compile, emulate, hex-check)
  → characterize before changing
  → G1 = the lost unit does a user-visible thing again
  → ship that, then next
```

## Survey (Dowsing — read-only)

- Extensions, magic bytes, encodings, Makefiles, `.dpr` `.pas` `.asm` `.s`
  `.inc` `.cbl` `.for` `.f90` `.vhd` `.adb` `.ads` `.fs` `.fth` `.4th` `.lisp` `.lsp` `.cl` `.pro` `.prolog` `.tcl` `.tk` `.erl` `.hrl` `.rex` `.rexx` `.mod` `.def` `.a68` `.alg` `.a60` `.alw` `.icn` `.obn` `.sno` `.sim` `.apl` `.b` `.bcpl` `.pli` `.pl1` `.st` `.ps` `.eps` `.bas` `.scm` `.awk` `.rel` object files, disk images.
- For *this* repo, read `.emperor/survey.md` (silent boot already wrote it).
  For a *foreign* tree: `scripts/emperor identify <path>` or `scripts/emperor excavate <path>` (alias; Python core `scripts/lib/identify.py`; thin identify + excavate twins call the core directly).
  Quote the tail. Do not guess "this is probably Node" because you like Node.
- Utterance router: `scripts/emperor route "hello.f90"` / `"gfortran …"` / `"hello.vhd"` / `"ghdl …"` / `"hello.adb"` / `"gnatmake …"` / `"hello.fs"` / `"pforth …"` / `"hello.lisp"` / `"clisp …"` / `"hello.pro"` / `"swipl …"` / `"hello.tcl"` / `"tclsh …"` / `"hello.erl"` / `"escript …"` / `"hello.rex"` / `"regina …"` / `"hello.mod"` / `"gm2 …"` / `"hello.a68"` / `"a68g …"` / `"hello.a60"` / `"marst …"` / `"hello.alw"` / `"awe …"` / `"hello.icn"` / `"icont …"` / `"hello.obn"` / `"voc …"` / `"hello.sno"` / `"snobol4 …"` / `"hello.sim"` / `"cim …"` / `"hello.apl"` / `"apl …"` / `"bcpl …"` / `"cintsys …"` / `"hello.pli"` / `"plic …"` / `"gst …"` / `"smalltalk …"` / `"ghostscript …"` / `"postscript …"` / `"bwbasic …"` / `"bywater …"` / `"hello.bas"` / `"csi …"` / `"chicken …"` / `"hello.scm"` / `"gawk …"` / `"awk …"` / `"hello.awk"` (Python `scripts/lib/route.py`, triggers excavate patterns) maps Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, and AWK fossils to excavate — same as `.pas` / `.asm` / `.cbl`.
- Skipped probes are listed. Absence of a modern test runner is not a defect.

## Hunt (Jail, aimed at manuals not skills)

Public SKILL.md files rarely know Turbo Pascal 5.5 or a particular assembler
dialect. Hunt:

- vendor PDFs, scanned manuals, instruction set PDFs, old man pages
- archive.org, bitsavers, compiler release notes, extant forum threads

Extract **one heading** that unblocks *this* probe. Pin the URL + date +
quoted paragraph in the ledger. Memory of "how Pascal works" is CONJECTURE.
Worked examples (Jail pins): [archaeology-pascal-manual.md](archaeology-pascal-manual.md) — ISO 7185 §6.10 program heading for HELLO.PAS; [archaeology-asm-manual.md](archaeology-asm-manual.md) — NASM 2.16.03 §7.3 SECTION pin for FOO.ASM; [archaeology-cobol-manual.md](archaeology-cobol-manual.md) — GnuCOBOL Programmer’s Guide §4 IDENTIFICATION DIVISION / PROGRAM-ID for HELLO.CBL; [archaeology-fortran-manual.md](archaeology-fortran-manual.md) — GNU Fortran Compiler §2.2 free-form dialect / `.f90` for HELLO.F90. [archaeology-vhdl-manual.md](archaeology-vhdl-manual.md) — GHDL Invoking GHDL Analysis/Elaboration/Run for HELLO.VHD; [archaeology-ada-manual.md](archaeology-ada-manual.md) — GNAT User's Guide Building with gnatmake for HELLO.ADB. [archaeology-forth-manual.md](archaeology-forth-manual.md) — pForth README How to Run INCLUDE / `pforth myprogram.fth` for HELLO.FS. [archaeology-lisp-manual.md](archaeology-lisp-manual.md) — CLISP Non-Interactive (Batch) Mode lisp-file run for HELLO.LISP. [archaeology-prolog-manual.md](archaeology-prolog-manual.md) — SWI-Prolog initialization/2 main role for HELLO.PRO. [archaeology-tcl-manual.md](archaeology-tcl-manual.md) — tclsh SCRIPT FILES for HELLO.TCL. [archaeology-erlang-manual.md](archaeology-erlang-manual.md) — escript main/1 for HELLO.ERL. [archaeology-rexx-manual.md](archaeology-rexx-manual.md) — Classic Rexx SAY for HELLO.REX. [archaeology-modula2-manual.md](archaeology-modula2-manual.md) — GNU Modula-2 Example compile and link for HELLO.MOD. [archaeology-algol68-manual.md](archaeology-algol68-manual.md) — Algol 68 Genie Synopsis / Transput print for HELLO.A68. [archaeology-algol60-manual.md](archaeology-algol60-manual.md) — GNU MARST Usage Example / outstring for HELLO.A60. [archaeology-algolw-manual.md](archaeology-algolw-manual.md) — Awe SYNOPSIS / EXAMPLES WRITE for HELLO.ALW. [archaeology-icon-manual.md](archaeology-icon-manual.md) — Icon 9 UNIX Manual Page SYNOPSIS / File Names for HELLO.ICN. [archaeology-oberon-manual.md](archaeology-oberon-manual.md) — Vishap Compiling Main module for HELLO.OBN. [archaeology-snobol-manual.md](archaeology-snobol-manual.md) — CSNOBOL4 snobol4cmd(1) SYNOPSIS for HELLO.SNO. [archaeology-simula-manual.md](archaeology-simula-manual.md) — Portable Simula Usage synopsis for HELLO.SIM. [archaeology-apl-manual.md](archaeology-apl-manual.md) — GNU APL SYNOPSIS / `-f file` for HELLO.APL. [archaeology-bcpl-manual.md](archaeology-bcpl-manual.md) — Martin Richards cintsys `-c` / `bcpl … to …` for HELLO.B. [archaeology-pli-manual.md](archaeology-pli-manual.md) — Iron Spring plic `-C` / ld `-lprf` for HELLO.PLI. [archaeology-smalltalk-manual.md](archaeology-smalltalk-manual.md) — GNU Smalltalk Invocation / `gst` file run for HELLO.ST. [archaeology-postscript-manual.md](archaeology-postscript-manual.md) — Ghostscript Invoking Ghostscript / `gs` file run for HELLO.PS. [archaeology-basic-manual.md](archaeology-basic-manual.md) — bwbasic(1) §4.d Command-Line Execution / `bwbasic prog.bas` for HELLO.BAS. [archaeology-scheme-manual.md](archaeology-scheme-manual.md) — CHICKEN Using the interpreter / `csi -s` / `-script PATHNAME` for HELLO.SCM. [archaeology-awk-manual.md](archaeology-awk-manual.md) — GAWK Command-Line Options / `gawk -f` / `--file source-file` for HELLO.AWK.

## Recover

1. Smallest command that proves the artifact is what you think it is.
2. Smallest command that produces an output the original author would
   recognize.
3. Only then change source.

A clean-room rewrite in another language is a new product. It needs its own
G1 and explicit client yes.

## Internet traversal

Search is allowed. Credentials are not. If a manual is paywalled, record the
gap and work from what is public. Do not pirate.
