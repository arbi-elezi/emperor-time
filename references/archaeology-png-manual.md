# Jail pin — Pillow Image.open + PNG tEXt for HELLO.png (Portable Network Graphics)

Contemporaneous manual pin for the lost-png archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how PNG
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-png/HELLO.png` with
runnable dialect **VERIFIED** as Pillow 11.1.0
under Linux x86_64
(`Image.open("HELLO.png").text["EmperorProbe"]` →
`EMPEROR-TIME-PNG-PROBE-OK`). Filename culture
(ImageMagick / libpng-tools / ffmpeg / Cairo / Skia / pdf / ps)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.png`.
Bare `png` / `pillow` / `pil` are **allowed** as route tags (format / tool / family).
Bare `.png` is **allowed** as a route tag with
extension-boundary matching. Prefer `png` /
`pillow` / `pil` / `.png`.
Bare `imagemagick` / `magick` / `convert` / `identify` / `ffmpeg` are **refused** this leaf (wrong owner / ET identify collision / media peer).
Do **not** steal plain `*.pdf` or `*.ps` or `*.pptx` ownership from prior leaves;
a `.png` is a distinct image fossil (ISO/IEC 15948 / PNG via Pillow).
Toolchain is Debian `python3-pil` already on box (**zero new apt**).
ImageMagick / ffmpeg apt were considered and **REJECTED**
as the verified leaf owner vs already-on-box Pillow (same honesty as lost-json already-on-box CPython; standing prefer-Python rule). This note supplies
the Jail pin so excavate can name the **verified** Pillow
`Image.open` + PNG `tEXt` shape on a PNG without inventing a full
ImageMagick / libpng-tools / ffmpeg suite claim for a
minimal probe. Distinct from the PDF archaeology leaf (`*.pdf` /
pdftotext), PostScript (`*.ps` / ghostscript), PPTX (`*.pptx` / zipfile),
and HTML (`*.html` / tidy).
Chain Jail leaf only — excavate fossil pin, not a vendored foreign image skill.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Pillow (PIL Fork) Image module — Portable Network Graphics reader* + *ISO/IEC 15948 / PNG* |
| **Heading** | **`Image.open` + PNG `tEXt` on `.png`** — Open a PNG; read textual metadata chunks via `Image.text` |
| **Dialect pinned** | **Pillow 11.1.0 `Image.open` + `tEXt`** on a `.png` with `EmperorProbe` text chunk — **not** full ImageMagick / libpng-tools / ffmpeg suite claim |
| **URL** | https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png (Pillow PNG); https://www.w3.org/TR/PNG/ (W3C PNG); python3-pil 11.1.0-5+deb13u4 on box |
| **Anchors** | `.png` path; `Image.open(path)`; `im.text["EmperorProbe"]`; Pillow version |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Pillow PNG docs + PNG spec)

> Pillow reads and writes PNG files using the libpng library. PNG files can store textual information using tEXt, zTXt, and iTXt chunks. Pillow exposes these via the `Image.text` dictionary after open.
>
> Portable Network Graphics (PNG) is an extensible file format for the lossless, portable, well-compressed storage of raster images.

(Source: Pillow handbook Image file formats — PNG
https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png
accessed 2026-09-28 Europe/Tirane;
W3C PNG https://www.w3.org/TR/PNG/ accessed 2026-09-28 Europe/Tirane.
Installed `python3 -c "import PIL; print(PIL.__version__)"` reports 11.1.0.
Probe uses
`Image.open("HELLO.png").text.get("EmperorProbe")`
so Pillow opens the PNG and returns the probe token from the `tEXt` chunk.
Format: RGB 64×32 PNG with `tEXt` key `EmperorProbe`.)

### Why this heading (HELLO.png / excavate)

A minimal HELLO surface looks like a small RGB PNG with a `tEXt`
metadata chunk carrying the probe token. That is exactly the pinned form:
**Pillow `Image.open` + PNG `tEXt` on `.png`**, observe metadata text at run time.

### Honesty

- VERIFIED: Pillow 11.1.0 `Image.open` + PNG `tEXt` `EmperorProbe` on this HELLO (RGB 64×32).
- CONJECTURE: any claim that ImageMagick / libpng-tools / ffmpeg / Cairo / Skia are this dialect.
- UNVERIFIABLE: Debian imagemagick / ffmpeg / full multi-dialect image recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, ImageMagick/ffmpeg as leaf owner (wrong owner / ET identify collision); graphviz this turn (multi-dep); bare `imagemagick` / `magick` / `convert` / `identify` as verified PNG toolchain; stealing plain `*.pdf` or `*.ps` or `*.pptx` ownership from prior leaves; vendoring foreign image skills as this Jail pin.
