# Boot probe — lost-png / HELLO.png

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~21:05 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **python3-pil** 11.1.0-5+deb13u4 (Debian trixie) |
| Module | `PIL` / Pillow 11.1.0 (`from PIL import Image, PngImagePlugin`) |
| Reported | Pillow 11.1.0 |
| Install | already on box this leaf — **zero new Apt Worthy Spend**; Debian `python3-pil` already present; still prefer over deferred TeXlive / C++ / graphviz multi-dep apt; ImageMagick `convert`/`identify`/`magick` REJECTED as leaf owner vs already-on-box Pillow (and `identify` collides with ET identify survey); ffmpeg REJECTED as leaf owner this turn (media container peer, separate pin) |

Probe used Pillow `Image.open` + PNG `tEXt` chunk key `EmperorProbe` on a minimal
RGB PNG. Identify fossils use `*.png`. Prefer `png` / `pillow` / `pil` / `.png`.
Bare `png` / `pillow` / `pil` are **allowed** as route tags (format / tool / family).
Bare `.png` is **allowed** with extension-boundary matching (do not invent
`.pngfoo` prefix hits). Bare `imagemagick` / `magick` / `convert` / `identify` / `ffmpeg` refused this leaf (wrong owner / ET identify collision / media peer).
PNG raster leaf after PDF; treats PNG as peer image fossil not house twin language.
Do **not** claim a full ImageMagick / libpng / libpng-tools / ffmpeg suite recovery from a
Pillow `Image.open` + `tEXt` probe alone — this leaf pins Pillow PNG open + `tEXt` read
with the probe token in metadata. Do **not** claim ImageMagick / ffmpeg as the verified
toolchain this leaf (rejected as owner; Pillow already on box).
Distinct from PDF (`*.pdf` / pdftotext), PostScript (`*.ps` / ghostscript), PPTX (`*.pptx` / zipfile),
and HTML (`*.html` / tidy).
Do **not** steal plain `*.pdf` or `*.ps` or `*.pptx` ownership — those remain prior leaves.
Defer TeX/LaTeX / C++ / openjdk-as-owner / graphviz / CLIPS / embeddings / ffmpeg this turn.

## Commands (VERIFIED)

```text
$ python3 -c "import PIL; print(PIL.__version__)"
11.1.0

$ dpkg-query -W -f='${Version}' python3-pil
11.1.0-5+deb13u4

$ python3 - <<'EOF'
from PIL import Image
im = Image.open("HELLO.png")
print(im.format, im.size, im.mode)
print(im.text.get("EmperorProbe"))
EOF
PNG (64, 32) RGB
EMPEROR-TIME-PNG-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Pillow 11.1.0 `Image.open` + PNG `tEXt` `EmperorProbe` on this HELLO (RGB 64×32) | VERIFIED |
| Full ImageMagick / libpng-tools / ffmpeg / Cairo / Skia suite are this dialect | CONJECTURE |
| Full Debian imagemagick/ffmpeg suite recovery from this probe alone | UNVERIFIABLE |
