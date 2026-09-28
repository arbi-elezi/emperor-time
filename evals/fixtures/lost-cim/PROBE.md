# Boot probe — lost-cim / HELLO.SIM

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~03:35 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | Portable Simula Revisited **Simula-2.0** (Setup R21, Feb 28 2025) from https://portablesimula.github.io/github.io/setup/SimulaSetup-R21.jar |
| Binary | `java -jar /tmp/toolchain-probe/Simula/Simula-2.0/simula.jar` (Temurin OpenJDK 21.0.12.1) |
| Reported | `Simula-2.0` via `-help`; properties `simula.home=/tmp/toolchain-probe/Simula` |
| Install | Download Temurin JRE/JDK 21; `java -jar SimulaSetup-R21.jar` (or manual extract of `simula.jar` + `rts/` + `~/.simula/simulaProperties.xml`); headless: `-Djava.awt.headless=true` |

Probe used Portable Simula CLI on a Standard `OutText` / `OutImage`
source. Identify fossils use `*.sim` only. Prefer `cim` / `simula` /
`.sim`; bare English tokens `begin` / `outtext` / `outimage` alone are
**refused** as route tags (keyword / English collision class). Do not
commit generated `bin/HELLO.jar` or temp Java from the probe.

**GNU Cim note:** `cim` 3.37 from https://github.com/perbu/cim built on
this host (`./configure --disable-shared` + gnu89 flags) but **segfaults**
before emit (`System error: Segmentation violation`). Cim invoke is
therefore **UNVERIFIABLE** here; the VERIFIED run is Portable Simula.

## Commands (VERIFIED)

Working directory for compile/run: fixture dir (or any dir with the source).

```text
$ java -Djava.awt.headless=true -jar /tmp/toolchain-probe/Simula/Simula-2.0/simula.jar -help
Simula-2.0 See: https://github.com/portablesimula
Usage: java -jar simula.jar  [options]  sourceFile

$ java -Djava.awt.headless=true -jar /tmp/toolchain-probe/Simula/Simula-2.0/simula.jar \
    -noConsole -sourceFileDir /tmp/toolchain-probe/cim-hello HELLO.SIM
… Resulting File: …/bin/HELLO.jar
EMPEROR-TIME-CIM-PROBE-OK
END Execute .jar File. Exit value=0
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Simula fossil named `HELLO.SIM` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-cim` prints `1 *.sim` |
| Compiles and runs under Portable Simula 2.0 (R21) / JDK 21 | VERIFIED | `java -jar simula.jar … HELLO.SIM` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-CIM-PROBE-OK` |
| Dialect is a specific Simula Standard year / Simulation package full claim | CONJECTURE | No Class/Simulation jury beyond OutText/OutImage |
| Would run under period Simula-67 / CDC / DEC vendor on original media | UNVERIFIABLE here | No period vendor run in this session |
| GNU Cim 3.37 `cim HELLO.SIM` on this host | UNVERIFIABLE here | Built binary segfaults before emit |

## Not done (honest gaps)

- No Jail-hunt of the full Simula Standard 1986 / Simulation chapter
  (deferred; pin is Portable Simula **Usage** synopsis — see
  `references/archaeology-simula-manual.md`).
- No GNU Cim VERIFIED claim on this host (segfault).
- No bare `begin` / `outtext` / `outimage` route tags (keyword English
  collision).
