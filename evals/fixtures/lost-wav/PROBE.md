# Boot probe — lost-wav / HELLO.wav

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~21:18 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **ffmpeg** 7:7.1.5-0+deb13u1 (Debian trixie) |
| Tools | `ffmpeg` / `ffprobe` 7.1.5 (`ffprobe -show_entries format_tags=comment`) |
| Reported | ffmpeg version 7.1.5-0+deb13u1 Copyright (c) 2000-2026 the FFmpeg developers |
| Install | already on box this leaf — **zero new Apt Worthy Spend**; Debian `ffmpeg` already present; still prefer over deferred TeXlive / C++ / graphviz multi-dep apt; ImageMagick `convert`/`identify`/`magick` REJECTED as leaf owner for audio (and `identify` collides with ET identify survey); sox / audacity REJECTED as leaf owner vs already-on-box ffmpeg; Pillow REJECTED as leaf owner this turn (PNG raster peer, prior leaf) |

Probe used `ffprobe` format tag `comment` on a minimal
PCM WAV (via Python subprocess wrapper — standing prefer-Python rule). Identify fossils use `*.wav`. Prefer `wav` / `ffmpeg` / `ffprobe` / `.wav`.
Bare `wav` / `ffmpeg` / `ffprobe` are **allowed** as route tags (format / tool / family).
Bare `.wav` is **allowed** with extension-boundary matching (do not invent
`.wavfoo` prefix hits). Bare `sox` / `audacity` / `imagemagick` / `magick` / `convert` / `identify` refused this leaf (wrong owner / ET identify collision).
WAV media leaf after PNG; treats WAV as peer audio fossil not house twin language.
Do **not** claim a full GStreamer / sox / audacity / libavfilter suite recovery from an
`ffprobe` format-tag probe alone — this leaf pins ffmpeg/ffprobe WAV open + `comment` tag read
with the probe token in metadata. Do **not** claim ImageMagick / sox as the verified
toolchain this leaf (rejected as owner; ffmpeg already on box).
Distinct from PNG (`*.png` / Pillow), PDF (`*.pdf` / pdftotext), PostScript (`*.ps` / ghostscript), and PPTX (`*.pptx` / zipfile).
Do **not** steal plain `*.png` or `*.pdf` or `*.ps` or `*.pptx` ownership — those remain prior leaves.
Defer TeX/LaTeX / C++ / openjdk-as-owner / graphviz / CLIPS / embeddings this turn.

## Commands (VERIFIED)

```text
$ ffmpeg -version | head -1
ffmpeg version 7.1.5-0+deb13u1 Copyright (c) 2000-2026 the FFmpeg developers

$ dpkg-query -W -f='${Version}' ffmpeg
7:7.1.5-0+deb13u1

$ python3 - <<'EOF'
import subprocess
from pathlib import Path
wav = Path("HELLO.wav")
out = subprocess.check_output([
    "ffprobe", "-v", "error",
    "-show_entries", "format_tags=comment,title",
    "-of", "default=noprint_wrappers=1",
    str(wav),
], text=True)
print(out.strip())
EOF
TAG:comment=EMPEROR-TIME-WAV-PROBE-OK
TAG:title=EmperorProbe
```

## Dialect labels

| Claim | Status |
|-------|--------|
| ffmpeg/ffprobe 7.1.5 format tag `comment=EMPEROR-TIME-WAV-PROBE-OK` on this HELLO (PCM s16le mono ~50 ms) | VERIFIED |
| Full GStreamer / sox / audacity / libavfilter suite are this dialect | CONJECTURE |
| Full Debian multimedia suite recovery from this probe alone | UNVERIFIABLE |
