# Jail pin — ffmpeg/ffprobe format tags for HELLO.wav (Waveform Audio File Format)

Contemporaneous manual pin for the lost-wav archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how WAV
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-wav/HELLO.wav` with
runnable dialect **VERIFIED** as ffmpeg/ffprobe 7.1.5
under Linux x86_64
(`ffprobe -show_entries format_tags=comment` →
`EMPEROR-TIME-WAV-PROBE-OK`). Filename culture
(GStreamer / sox / audacity / libavfilter / mp4 / png)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.wav`.
Bare `wav` / `ffmpeg` / `ffprobe` are **allowed** as route tags (format / tool / family).
Bare `.wav` is **allowed** as a route tag with
extension-boundary matching. Prefer `wav` /
`ffmpeg` / `ffprobe` / `.wav`.
Bare `sox` / `audacity` / `imagemagick` / `magick` / `convert` / `identify` are **refused** this leaf (wrong owner / ET identify collision).
Do **not** steal plain `*.png` or `*.pdf` or `*.ps` or `*.pptx` ownership from prior leaves;
a `.wav` is a distinct audio fossil (RIFF/WAVE via ffmpeg).
Toolchain is Debian `ffmpeg` already on box (**zero new apt**).
sox / ImageMagick apt were considered and **REJECTED**
as the verified leaf owner vs already-on-box ffmpeg (same honesty as lost-png already-on-box Pillow; standing prefer-Python rule wraps ffprobe). This note supplies
the Jail pin so excavate can name the **verified** ffmpeg
`ffprobe` format-tag shape on a WAV without inventing a full
GStreamer / sox / audacity suite claim for a
minimal probe. Distinct from the PNG archaeology leaf (`*.png` /
Pillow), PDF (`*.pdf` / pdftotext), PostScript (`*.ps` / ghostscript),
and PPTX (`*.pptx` / zipfile).
Chain Jail leaf only — excavate fossil pin, not a vendored foreign media skill.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *FFmpeg Documentation — ffprobe* + *Microsoft / IBM RIFF WAVE* |
| **Heading** | **`ffprobe` format tags on `.wav`** — Open a WAV; read textual format metadata via `-show_entries format_tags` |
| **Dialect pinned** | **ffmpeg/ffprobe 7.1.5 format tag `comment`** on a `.wav` with `EMPEROR-TIME-WAV-PROBE-OK` — **not** full GStreamer / sox / audacity suite claim |
| **URL** | https://ffmpeg.org/ffprobe.html (ffprobe); https://ffmpeg.org/ffmpeg.html (ffmpeg); ffmpeg 7:7.1.5-0+deb13u1 on box |
| **Anchors** | `.wav` path; `ffprobe -show_entries format_tags=comment`; Python subprocess wrapper; ffmpeg version |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from FFmpeg ffprobe docs)

> ffprobe gathers information from multimedia streams and prints it in human- and machine-readable fashion. […] `-show_entries` sets the entries which need to be shown. […] Format metadata (title, artist, comment, …) is exposed under `format_tags`.

(Source: FFmpeg ffprobe documentation
https://ffmpeg.org/ffprobe.html
accessed 2026-09-28 Europe/Tirane;
FFmpeg general https://ffmpeg.org/ffmpeg.html accessed 2026-09-28 Europe/Tirane.
Installed `ffmpeg -version` reports 7.1.5-0+deb13u1.
Probe uses
`ffprobe -v error -show_entries format_tags=comment -of default=noprint_wrappers=1:nokey=1 HELLO.wav`
so ffprobe opens the WAV and returns the probe token from the format `comment` tag.
Format: PCM s16le mono ~50 ms WAV with RIFF INFO/comment metadata.)

### Why this heading (HELLO.wav / excavate)

A minimal HELLO surface looks like a short PCM WAV with a format
metadata `comment` carrying the probe token. That is exactly the pinned form:
**ffmpeg `ffprobe` format tags on `.wav`**, observe metadata text at run time
(via a Python subprocess wrapper — standing prefer-Python rule).

### Honesty

- VERIFIED: ffmpeg/ffprobe 7.1.5 format tag `comment=EMPEROR-TIME-WAV-PROBE-OK` on this HELLO (PCM s16le mono ~50 ms).
- CONJECTURE: any claim that GStreamer / sox / audacity / libavfilter / mp4 are this dialect.
- UNVERIFIABLE: Debian multimedia full multi-dialect recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, sox/ImageMagick as leaf owner (wrong owner / ET identify collision); graphviz this turn (multi-dep); bare `sox` / `audacity` / `imagemagick` / `magick` / `convert` / `identify` as verified WAV toolchain; stealing plain `*.png` or `*.pdf` or `*.ps` or `*.pptx` ownership from prior leaves; vendoring foreign media skills as this Jail pin.
