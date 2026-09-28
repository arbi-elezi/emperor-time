# Jail pin — Python tarfile.open/getmembers/extractfile for HELLO.tar

Contemporaneous manual pin for the lost-tar archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how tar
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-tar/HELLO.tar` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `tarfile`
under Linux x86_64
(`python3` + `tarfile.open`/`getmembers`/`extractfile` on HELLO.tar → member
`PROBE.txt` yields `EMPEROR-TIME-TAR-PROBE-OK`). Filename culture
(`.tar.gz` / `.tgz` / `.tar.bz2` / `.tar.xz` / pax / sparse)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.tar`.
Bare `tar` / `pytar` / `tarfile` are **allowed** as route tags (format / family / module).
Bare `.tar` is **allowed** as a route tag with
extension-boundary matching. Prefer `tar` /
`pytar` / `tarfile` / `.tar`.
Toolchain is CPython stdlib `tarfile` already on box (**zero new apt**).
Debian `tar` 1.35+dfsg-3.1 (Installed-Size ~3085 kB; already on box) was considered and **REJECTED**
as the verified leaf owner vs stdlib. This note supplies
the Jail pin so excavate can name the **verified** stdlib `tarfile`
list/read shape without inventing a full
GNU tar / pax / sparse / multi-volume suite claim for a
single-member probe. Distinct from the zip archaeology leaf (`*.zip` /
zipfile), eml (`*.eml` / email.parser), plist (`*.plist` / plistlib), JSON (`*.json` / json),
and CSV (`*.csv` / csv).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `tarfile`: Read and write tar archive files* |
| **Heading** | **`tarfile.open` / `TarFile.getmembers` / `TarFile.extractfile`** — Open a TAR archive; list members; return a file-like object for a member |
| **Dialect pinned** | **CPython stdlib `tarfile.open`/`getmembers`/`extractfile`** with member `PROBE.txt` → print token — **not** full GNU tar / pax / sparse / multi-volume / compressed suite claim |
| **URL** | https://docs.python.org/3/library/tarfile.html (Python docs — `tarfile`); CPython 3.13.5 on box |
| **Anchors** | `.tar` archive path; `tarfile.open(path)`; `getmembers()`; `extractfile(member)` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `tarfile.open` / `TarFile.getmembers` / `extractfile`)

> tarfile.open(name=None, mode='r', …) — Return a TarFile object for the pathname name.
>
> TarFile.getmembers() — Return the members of the archive as a list of TarInfo objects. The list has the same order as the members in the archive.
>
> TarFile.extractfile(member) — Extract a member from the archive as a file object. member may be a filename or a TarInfo object. If member is a regular file or a link, an io.BufferedReader object is returned. Otherwise, None is returned.

(Source: Python 3 Library Reference, section
**tarfile — Read and write tar archive files — TarFile Objects**,
https://docs.python.org/3/library/tarfile.html
accessed 2026-09-28 Europe/Tirane.
Module intro: "The tarfile module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression."
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`tarfile.open('HELLO.tar').extractfile(getmembers()[0]).read().decode().strip()`
so stdlib tarfile loads the named `.tar` and prints the member token.
Format: ustar / POSIX TAR compatible uncompressed archive.)

### Why this heading (HELLO.tar / excavate)

A minimal HELLO surface looks like a one-member ustar TAR with
`PROBE.txt` holding a probe token. That is exactly the pinned form:
**stdlib `tarfile.open`/`getmembers`/`extractfile`**, observe member bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `tarfile.open`/`getmembers`/`extractfile` on this HELLO (ustar TAR with PROBE.txt).
- CONJECTURE: any claim that GNU tar / pax / sparse / multi-volume / compressed `.tar.gz` are this dialect.
- UNVERIFIABLE: Debian tar / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `tar` as verified leaf owner (stdlib owns); bare `tar` apt/system as verified toolchain; `*.tar.gz` / `*.tgz` / `*.tar.bz2` / `*.tar.xz` / `*.jar` / `*.war` / `*.apk` / `*.whl` / `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` fossils this leaf (defer).
