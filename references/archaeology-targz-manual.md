# Jail pin — Python tarfile compressed modes for HELLO.tar.gz / .tgz / .tar.bz2 / .tar.xz

Contemporaneous manual pin for the lost-targz archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how compressed tar
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-targz/HELLO.tar.gz` (plus
`.tgz` / `.tar.bz2` / `.tar.xz` siblings) with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `tarfile`
compressed modes under Linux x86_64
(`python3` + `tarfile.open`/`getmembers`/`extractfile` with `r:gz` / `r:bz2` / `r:xz`
→ member `PROBE.txt` yields `EMPEROR-TIME-TARGZ-PROBE-OK`). Filename culture
(pax / sparse / multi-volume / exotic compressors)
remains **CONJECTURE** only for naming collisions. Identify fossils use
`*.tar.gz` / `*.tgz` / `*.tar.bz2` / `*.tar.xz`.
Bare `targz` / `tarball` / `pytargz` are **allowed** as route tags (format / family / module-family).
Bare `.tar.gz` / `.tgz` / `.tar.bz2` / `.tar.xz` are **allowed** as route tags with
extension-boundary matching. Prefer `targz` /
`tarball` / `pytargz` / `.tar.gz` / `.tgz` / `.tar.bz2` / `.tar.xz`.
Do **not** steal plain `*.tar` or plain `*.gz` ownership from prior leaves;
a `.gz` suffix match may still fire excavate on `file.tar.gz` via the gzip leaf
without owning compressed-TAR — this leaf adds the compound fossils.
Toolchain is CPython stdlib `tarfile` already on box (**zero new apt**).
Debian `tar` / `gzip` / `bzip2` / `xz-utils` (already on box) were considered and **REJECTED**
as the verified leaf owner vs stdlib. This note supplies
the Jail pin so excavate can name the **verified** stdlib `tarfile`
compressed-mode list/read shape without inventing a full
GNU tar / pax / sparse / multi-volume suite claim for a
single-member probe. Distinct from the plain tar archaeology leaf (`*.tar` /
tarfile), plain gzip (`*.gz` / gzip), zip (`*.zip` /
zipfile), eml (`*.eml` / email.parser), plist (`*.plist` / plistlib), JSON (`*.json` / json),
and CSV (`*.csv` / csv).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `tarfile`: Read and write tar archive files* |
| **Heading** | **`tarfile.open` with compression modes `r:gz` / `r:bz2` / `r:xz`** — Open a compressed TAR archive; list members; return a file-like object for a member |
| **Dialect pinned** | **CPython stdlib `tarfile.open`/`getmembers`/`extractfile`** under compressed modes with member `PROBE.txt` → print token — **not** full GNU tar / pax / sparse / multi-volume suite claim |
| **URL** | https://docs.python.org/3/library/tarfile.html (Python docs — `tarfile`); CPython 3.13.5 on box |
| **Anchors** | `.tar.gz` / `.tgz` / `.tar.bz2` / `.tar.xz` archive paths; `tarfile.open(path, 'r:gz'|'r:bz2'|'r:xz')`; `getmembers()`; `extractfile(member)` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `tarfile.open` compression modes)

> tarfile.open(name=None, mode='r', …) — Return a TarFile object for the pathname name.
>
> mode must be a string of the form 'filemode[:compression]'
>
> 'r:gz' Open for reading with gzip compression.
> 'r:bz2' Open for reading with bzip2 compression.
> 'r:xz' Open for reading with lzma compression.

(Source: Python 3 Library Reference, section
**tarfile — Read and write tar archive files — TarFile Objects**,
https://docs.python.org/3/library/tarfile.html
accessed 2026-09-28 Europe/Tirane.
Module intro: "The tarfile module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression."
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`tarfile.open('HELLO.tar.gz', 'r:gz').extractfile(getmembers()[0]).read().decode().strip()`
(and sibling `r:bz2` / `r:xz` / `.tgz`)
so stdlib tarfile loads the named compressed TAR and prints the member token.
Format: ustar / POSIX TAR compatible archive under gzip / bzip2 / xz compression.)

### Why this heading (HELLO.tar.gz / excavate)

A minimal HELLO surface looks like a one-member compressed TAR with
`PROBE.txt` holding a probe token. That is exactly the pinned form:
**stdlib `tarfile` compressed-mode open/list/read**, observe member bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `tarfile.open`/`getmembers`/`extractfile` on this HELLO family (`r:gz` / `r:bz2` / `r:xz` compressed TAR with PROBE.txt).
- CONJECTURE: any claim that GNU tar / pax / sparse / multi-volume / exotic compressors are this dialect.
- UNVERIFIABLE: Debian tar/gzip/bzip2/xz / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `tar`/`gzip`/`bzip2`/`xz-utils` as verified leaf owner (stdlib owns); bare apt/system as verified toolchain; `*.jar` / `*.war` / `*.apk` / `*.whl` / `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` fossils this leaf (defer); stealing plain `*.tar` or plain `*.gz` ownership from prior leaves.
