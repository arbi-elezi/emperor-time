# Boot probe — lost-jq / HELLO.jq

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~11:44 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **jq** 1.7.1-6+deb13u4 (Debian trixie) |
| Binary | `/usr/bin/jq` |
| Reported | `jq-1.7` (`jq --version`) |
| Install | already on box this leaf (apt Worthy Spend 0 B after SQL; Installed-Size 125 kB; still prefer over TeXlive / C++ / openjdk apt) |

Probe used `jq -nr -f HELLO.jq` on a minimal
string-literal filter (`-n` null-input, `-r` raw-output, `-f` from-file).
Identify fossils use `*.jq` only. Prefer `jq` /
`jq1.7` / `jqlang` / `.jq`.
Bare `jq` is **allowed** as a route tag (tool binary name; word-boundary).
Bare `.jq` is **allowed** with extension-boundary matching (does not
prefix-hit `.jquery`). JSON filter leaf after SQL;
treats jq as peer fossil not house twin language. Do **not**
claim a full gojq / jaq / JSONPath suite recovery from a Debian `jq`
CLI probe alone — this leaf pins `jq` `-f` file filter evaluation
with null-input and raw-output.

## Commands (VERIFIED)

```text
$ which jq
/usr/bin/jq

$ jq --version
jq-1.7

$ jq -nr -f HELLO.jq
EMPEROR-TIME-JQ-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `jq` 1.7 CLI `-nr -f` on `HELLO.jq` → probe string | VERIFIED |
| Filename culture (`.jquery` / browser jQuery) maps to this dialect | CONJECTURE (probe uses plain `.jq` filter file) |
| Full gojq / jaq / JSONPath / jq 1.8+ feature recovery | UNVERIFIABLE from Debian jq 1.7 CLI probe alone |
| bare `gojq` / `jaq` as verified jq toolchain | REJECTED (not used this leaf) |
