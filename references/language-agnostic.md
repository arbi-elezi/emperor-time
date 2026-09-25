# Language-agnostic law

Emperor Time has no home language. Python, JS, Pascal, COBOL, Forth,
6502, x86, VHDL, and a folder of unmarked binaries are peers.

## Restrictions

1. Do not invent a stack. The repo's files pick the language.
2. A probe is any command that is red without the change and green with it.
   `pytest` is one probe. So is `fpc hello.pas`, `nasm`+`ld`, `make`, `as`, a
   hex dump diff, a serial log, a simulator cycle count.
3. Do not rewrite a lost program into a fashionable language unless G1 says
   that rewrite *is* the software.
4. Toolchain absence is Chain Jail + self-build adapter, not a reason to
   switch languages.
5. Comments, identifiers, and docs may be in any human language. Do not
   translate the product just to comfort the agent.
