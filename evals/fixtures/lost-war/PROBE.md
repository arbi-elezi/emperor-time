# Boot probe — lost-war / HELLO.war

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~17:41 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `zipfile` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `zipfile.ZipFile.namelist` / `read` |
| Reported | `Python 3.13.5` / stdlib `zipfile` (`python3 --version`; `python3 -c 'import zipfile; print(zipfile.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `unzip` / `zip` / `openjdk` / `tomcat` apt REJECTED vs zero-apt stdlib; still prefer over deferred TeXlive / C++ / graphviz multi-dep apt |

Probe used `python3` + stdlib `zipfile.ZipFile` on a minimal
`.war` (ZIP-based Java Web Application archive) and printed the contents of member `PROBE.txt`.
Identify fossils use `*.war` (WAR peer leaf after JAR). Prefer `war` / `pywar` / `web-archive` / `.war`.
Bare `war` / `pywar` / `web-archive` are **allowed** as route tags (format / family / format-name).
Bare `.war` is **allowed** with extension-boundary matching (do not invent
`.warfoo` prefix hits). Bare `java` / `openjdk` / `javac` / `tomcat` / `servlet` refused this leaf (JDK / servlet-container discourse / apt surface).
Zip-based WAR leaf after JAR; treats WAR as peer archive fossil not house twin language.
Do **not** claim a full JVM / openjdk / javac / jar-tool / servlet-container / Tomcat suite recovery from a CPython
stdlib `ZipFile.namelist`/`read` probe alone — this leaf pins stdlib
`zipfile` namelist+read on a `.war` with the probe token printed. Do **not** claim Debian
`unzip` / `zip` / `openjdk-*` / `tomcat*` as the verified toolchain this leaf (apt REJECTED).
Distinct from zip (`*.zip` / zipfile), wheel (`*.whl` / zipfile), JAR (`*.jar` / zipfile), compressed-TAR (`*.tar.gz` / tarfile),
plain tar (`*.tar` / tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json), and CSV (`*.csv` / csv).
Do **not** steal plain `*.zip` or `*.whl` or `*.jar` ownership — those remain the zip / wheel / jar leaves.
Defer `*.apk` / `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import zipfile; print(zipfile.__file__)'
/usr/lib/python3.13/zipfile/__init__.py

$ python3 -c "from zipfile import ZipFile; z=ZipFile('HELLO.war'); print(z.read('PROBE.txt').decode().strip())"
EMPEROR-TIME-WAR-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated WAR ZIP with PROBE.txt + META-INF/MANIFEST.MF + WEB-INF/web.xml) | VERIFIED |
| Full JVM / openjdk / javac / jar-tool / Tomcat / servlet-container / EAR/APK suite are this dialect | CONJECTURE |
| Full Debian unzip/zip/openjdk/tomcat suite recovery from this probe alone | UNVERIFIABLE |
