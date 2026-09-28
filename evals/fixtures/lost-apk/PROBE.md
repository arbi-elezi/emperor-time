# Boot probe — lost-apk / HELLO.apk

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~18:12 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `zipfile` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `zipfile.ZipFile.namelist` / `read` |
| Reported | `Python 3.13.5` / stdlib `zipfile` (`python3 --version`; `python3 -c 'import zipfile; print(zipfile.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `unzip` / `zip` / `android-sdk` / `aapt` apt REJECTED vs zero-apt stdlib; still prefer over deferred TeXlive / C++ / graphviz multi-dep apt |

Probe used `python3` + stdlib `zipfile.ZipFile` on a minimal
`.apk` (ZIP-based Android package) and printed the contents of member `PROBE.txt`.
Identify fossils use `*.apk` (APK peer leaf after WAR). Prefer `apk` / `pyapk` / `android-package` / `.apk`.
Bare `apk` / `pyapk` / `android-package` are **allowed** as route tags (format / family / format-name).
Bare `.apk` is **allowed** with extension-boundary matching (do not invent
`.apkfoo` prefix hits). Bare `android` / `adb` / `aapt` / `apktool` refused this leaf (Android-SDK discourse / apt surface).
Zip-based APK leaf after WAR; treats APK as peer archive fossil not house twin language.
Do **not** claim a full Android SDK / aapt / apktool / adb / Dalvik / ART / signing suite recovery from a CPython
stdlib `ZipFile.namelist`/`read` probe alone — this leaf pins stdlib
`zipfile` namelist+read on a `.apk` with the probe token printed. Do **not** claim Debian
`unzip` / `zip` / `android-sdk*` / `aapt*` as the verified toolchain this leaf (apt REJECTED).
Distinct from zip (`*.zip` / zipfile), wheel (`*.whl` / zipfile), JAR (`*.jar` / zipfile), WAR (`*.war` / zipfile), compressed-TAR (`*.tar.gz` / tarfile),
plain tar (`*.tar` / tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json), and CSV (`*.csv` / csv).
Do **not** steal plain `*.zip` or `*.whl` or `*.jar` or `*.war` ownership — those remain the zip / wheel / jar / war leaves.
Defer `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import zipfile; print(zipfile.__file__)'
/usr/lib/python3.13/zipfile/__init__.py

$ python3 -c "from zipfile import ZipFile; z=ZipFile('HELLO.apk'); print(z.read('PROBE.txt').decode().strip())"
EMPEROR-TIME-APK-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated APK ZIP with PROBE.txt + META-INF/MANIFEST.MF + AndroidManifest.xml) | VERIFIED |
| Full Android SDK / aapt / apktool / adb / Dalvik / ART / signing suite are this dialect | CONJECTURE |
| Full Debian unzip/zip/android-sdk/aapt suite recovery from this probe alone | UNVERIFIABLE |
