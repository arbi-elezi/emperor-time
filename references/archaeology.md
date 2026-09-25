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
  `.inc` `.cbl` `.for` `.vhd` `.rel` object files, disk images.
- Run `scripts/emperor identify` if present. Quote the tail. Do not guess "this
  is probably Node" because you like Node.
- Skipped probes are listed. Absence of a modern test runner is not a defect.

## Hunt (Jail, aimed at manuals not skills)

Public SKILL.md files rarely know Turbo Pascal 5.5 or a particular assembler
dialect. Hunt:

- vendor PDFs, scanned manuals, instruction set PDFs, old man pages
- archive.org, bitsavers, compiler release notes, extant forum threads

Extract **one heading** that unblocks *this* probe. Pin the URL + date +
quoted paragraph in the ledger. Memory of "how Pascal works" is CONJECTURE.

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
