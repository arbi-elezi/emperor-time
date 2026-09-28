# Jail pin — Python zipfile.ZipFile.namelist/read for HELLO.apk (APK format)

Contemporaneous manual pin for the lost-apk archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how APKs
work" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-apk/HELLO.apk` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `zipfile`
under Linux x86_64
(`python3` + `ZipFile.namelist`/`read` on HELLO.apk → member
`PROBE.txt` yields `EMPEROR-TIME-APK-PROBE-OK`). Filename culture
(Android SDK / aapt / apktool / adb / Dalvik / ART / OOXML)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.apk`.
Bare `apk` / `pyapk` / `android-package` are **allowed** as route tags (format / family / format-name).
Bare `.apk` is **allowed** as a route tag with
extension-boundary matching. Prefer `apk` /
`pyapk` / `android-package` / `.apk`.
Bare `android` / `adb` / `aapt` / `apktool` are **refused** this leaf (Android-SDK discourse / apt surface).
Do **not** steal plain `*.zip` or `*.whl` or `*.jar` or `*.war` ownership from the zip / wheel / jar / war leaves;
a `.apk` is a distinct zip-based container fossil (Android package + AndroidManifest.xml layout).
Toolchain is CPython stdlib `zipfile` already on box (**zero new apt**).
Debian `unzip` / `zip` / `android-sdk*` / `aapt*` apt were considered and **REJECTED**
as the verified leaf owner vs stdlib (same as lost-zip / lost-whl / lost-jar / lost-war). This note supplies
the Jail pin so excavate can name the **verified** stdlib `zipfile`
namelist/read shape on an APK without inventing a full
Android SDK / aapt / apktool / adb / Dalvik / ART suite claim for a
single-member probe. Distinct from the zip archaeology leaf (`*.zip` /
zipfile), wheel (`*.whl` / zipfile), JAR (`*.jar` / zipfile), WAR (`*.war` / zipfile), compressed-TAR (`*.tar.gz` / tarfile), plain tar (`*.tar` /
tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json),
and CSV (`*.csv` / csv).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `zipfile`: Work with ZIP archives* + *Android Developers — Application fundamentals / APK* |
| **Heading** | **`ZipFile.namelist` / `ZipFile.read` on `.apk`** — List APK archive members by name; return the bytes of a named member (APK is ZIP-format with `.apk` extension + AndroidManifest.xml + optional META-INF/ + classes.dex) |
| **Dialect pinned** | **CPython stdlib `zipfile.ZipFile.namelist`/`read`** on a `.apk` with member `PROBE.txt` → print token — **not** full Android SDK / aapt / apktool / adb / Dalvik / ART suite claim |
| **URL** | https://docs.python.org/3/library/zipfile.html (Python docs — `zipfile`); https://developer.android.com/guide/components/fundamentals (Android Developers — Application fundamentals); CPython 3.13.5 on box |
| **Anchors** | `.apk` archive path; `ZipFile(path)`; `namelist()`; `read(name)`; APK = ZIP-format + `.apk` (+ AndroidManifest.xml + META-INF + classes.dex) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `zipfile.ZipFile.namelist` / `read` + Android Application fundamentals)

> ZipFile.namelist() — Return a list of archive members by name.
>
> ZipFile.read(name, pwd=None) — Return the bytes of the file name in the archive. name is the name of the file in the archive, or a ZipInfo object.
>
> Android apps can be written using Kotlin, Java, and C++ languages. The Android SDK tools compile your code along with any data and resource files into an APK, an Android package. An APK file contains all of the contents of an Android app and is the file that Android-powered devices use to install the app.

(Source: Python 3 Library Reference, section
**zipfile — Work with ZIP archives — ZipFile objects**,
https://docs.python.org/3/library/zipfile.html
accessed 2026-09-28 Europe/Tirane;
Android Developers — Application fundamentals,
https://developer.android.com/guide/components/fundamentals
accessed 2026-09-28 Europe/Tirane.
Module intro: "The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file."
APK intro: "The Android SDK tools compile your code along with any data and resource files into an APK, an Android package. An APK file contains all of the contents of an Android app and is the file that Android-powered devices use to install the app."
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`ZipFile('HELLO.apk').read('PROBE.txt').decode().strip()`
so stdlib zipfile loads the named `.apk` and prints the member token.
Format: PKZIP / Info-ZIP compatible deflated APK archive with META-INF/MANIFEST.MF + AndroidManifest.xml.)

### Why this heading (HELLO.apk / excavate)

A minimal HELLO surface looks like a one-package deflated APK with
`PROBE.txt` holding a probe token plus `META-INF/MANIFEST.MF` and `AndroidManifest.xml`. That is exactly the pinned form:
**stdlib `ZipFile.namelist`/`read` on `.apk`**, observe member bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated APK ZIP with PROBE.txt + META-INF + AndroidManifest.xml).
- CONJECTURE: any claim that Android SDK / aapt / apktool / adb / Dalvik / ART / full signing / OOXML are this dialect.
- UNVERIFIABLE: Debian unzip / zip / android-sdk / aapt / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, android-sdk/aapt as leaf owner (apt size); graphviz this turn (multi-dep); Debian `unzip` / `zip` apt (unnecessary vs stdlib); bare `unzip` / `zip` / `android-sdk` / `aapt` apt as verified toolchain; `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` fossils this leaf (defer); stealing plain `*.zip` or `*.whl` or `*.jar` or `*.war` ownership from the zip / wheel / jar / war leaves.
