# Boot probe — lost-sh / HELLO.sh

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~11:01 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **bash** 5.2.37-2+b10 (Debian trixie) |
| Binary | `/usr/bin/bash` (same inode as `/bin/bash`) |
| Reported | `GNU bash, version 5.2.37(1)-release (x86_64-pc-linux-gnu)` |
| Install | Already on box (no apt this leaf) |

Probe used `bash HELLO.sh` on a minimal `echo` program.
Identify fossils use `*.sh` only (no `*.bash` this leaf). Prefer `bash` /
`bash5` / `bash5.2` / `gnu-bash` / `.sh`.
Bare `bash` is **allowed** as a route tag (tool binary name; word-boundary).
Bare `sh` is **refused** (POSIX / dash ambiguity; verified toolchain is bash).
Bare `.sh` is **allowed** with extension-boundary matching (does not
prefix-hit `.sha` / `.shar` / `.shtml`). Classic shell-script leaf after
TypeScript; treats Bash as peer fossil not house twin language. Do **not**
claim a full POSIX sh / dash / zsh / ksh recovery from an `echo` probe alone —
this leaf pins `bash` file-argument script run.

## Commands (VERIFIED)

```text
$ which bash
/usr/bin/bash

$ bash --version | head -1
GNU bash, version 5.2.37(1)-release (x86_64-pc-linux-gnu)

$ bash HELLO.sh
EMPEROR-TIME-BASH-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `bash` 5.2.37 on `HELLO.sh` → probe string | VERIFIED |
| Filename culture (`.bash` / `.bashrc` / login shells) maps to this dialect | CONJECTURE (probe uses plain `.sh` + `bash` file arg) |
| Full POSIX sh / dash / zsh / ksh recovery | UNVERIFIABLE from echo probe alone |
| bare `sh` as verified bash toolchain | REJECTED (POSIX/dash ambiguity; not used this leaf) |
