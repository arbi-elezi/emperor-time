# Boot probe — lost-jpg / HELLO.jpg

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~21:50 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **python3-pil** 11.1.0-5+deb13u4 (Debian trixie) |
| Module | `PIL` / Pillow 11.1.0 (`from PIL import Image`) |
| Reported | Pillow 11.1.0 |
| Install | already on box this leaf — **zero new Apt Worthy Spend**; Debian `python3-pil` already present (same package as PNG leaf); still prefer over deferred TeXlive / C++ / graphviz multi-dep apt; ImageMagick `convert`/`identify`/`magick` REJECTED as leaf owner vs already-on-box Pillow (and `identify` collides with ET identify survey); ffmpeg REJECTED as leaf owner this turn (WAV audio peer, prior leaf) |

Probe used Pillow `Image.open` + JPEG COM marker (`im.info["comment"]`) on a minimal
RGB JPEG. Identify fossils use `*.jpg` / `*.jpeg`. Prefer `jpeg` / `jpg` / `.jpg` / `.jpeg`.
Bare `jpeg` / `jpg` are **allowed** as route tags (format / short name).
Bare `.jpg` / `.jpeg` are **allowed** with extension-boundary matching (do not invent
`.jpgfoo` / `.jpegfoo` prefix hits). Bare `imagemagick` / `magick` / `convert` / `identify` / `ffmpeg` refused this leaf (wrong owner / ET identify collision / audio peer).
JPEG raster leaf after WAV; treats JPEG as peer image fossil not house twin language.
Do **not** claim a full ImageMagick / libjpeg-tools / ffmpeg suite recovery from a
Pillow `Image.open` + COM probe alone — this leaf pins Pillow JPEG open + COM read
with the probe token in the comment marker. Do **not** claim ImageMagick / ffmpeg as the verified
toolchain this leaf (rejected as owner; Pillow already on box).
Distinct from PNG (`*.png` / Pillow tEXt), WAV (`*.wav` / ffmpeg), PDF (`*.pdf` / pdftotext),
PostScript (`*.ps` / ghostscript), and PPTX (`*.pptx` / zipfile).
Do **not** steal plain `*.png` or `*.wav` or `*.pdf` or `*.ps` or `*.pptx` ownership — those remain prior leaves.
Defer TeX/LaTeX / C++ / openjdk-as-owner / graphviz / CLIPS / embeddings this turn.

## Commands (VERIFIED)

```text
$ python3 -c "import PIL; print(PIL.__version__)"
11.1.0

$ dpkg-query -W -f='${Version}' python3-pil
11.1.0-5+deb13u4

$ python3 - <<'EOF'
from PIL import Image
im = Image.open("HELLO.jpg")
print(im.format, im.size, im.mode)
c = im.info.get("comment")
print(c.decode() if isinstance(c, (bytes, bytearray)) else c)
EOF
JPEG (64, 32) RGB
EMPEROR-TIME-JPEG-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Pillow 11.1.0 `Image.open` + JPEG COM `comment=EMPEROR-TIME-JPEG-PROBE-OK` on this HELLO (RGB 64×32) | VERIFIED |
| Full ImageMagick / libjpeg-tools / ffmpeg / Cairo / Skia suite are this dialect | CONJECTURE |
| Full Debian imagemagick/ffmpeg suite recovery from this probe alone | UNVERIFIABLE |
