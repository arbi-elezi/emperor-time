# Jail pin — Pillow Image.open + JPEG COM for HELLO.jpg (JPEG / JFIF)

Contemporaneous manual pin for the lost-jpg archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how JPEG
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-jpg/HELLO.jpg` with
runnable dialect **VERIFIED** as Pillow 11.1.0
under Linux x86_64
(`Image.open("HELLO.jpg").info["comment"]` →
`EMPEROR-TIME-JPEG-PROBE-OK`). Filename culture
(ImageMagick / libjpeg-tools / ffmpeg / Cairo / Skia / png / wav)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.jpg` / `*.jpeg`.
Bare `jpeg` / `jpg` are **allowed** as route tags (format / short name).
Bare `.jpg` / `.jpeg` are **allowed** as route tags with
extension-boundary matching. Prefer `jpeg` /
`jpg` / `.jpg` / `.jpeg`.
Bare `imagemagick` / `magick` / `convert` / `identify` / `ffmpeg` are **refused** this leaf (wrong owner / ET identify collision / audio peer).
Do **not** steal plain `*.png` or `*.wav` or `*.pdf` or `*.ps` or `*.pptx` ownership from prior leaves;
a `.jpg` / `.jpeg` is a distinct image fossil (JPEG / JFIF via Pillow).
Toolchain is Debian `python3-pil` already on box (**zero new apt**).
ImageMagick / ffmpeg apt were considered and **REJECTED**
as the verified leaf owner vs already-on-box Pillow (same honesty as lost-png already-on-box Pillow; standing prefer-Python rule). This note supplies
the Jail pin so excavate can name the **verified** Pillow
`Image.open` + JPEG COM shape on a JPEG without inventing a full
ImageMagick / libjpeg-tools / ffmpeg suite claim for a
minimal probe. Distinct from the PNG archaeology leaf (`*.png` /
Pillow tEXt), WAV (`*.wav` / ffmpeg), PDF (`*.pdf` / pdftotext),
PostScript (`*.ps` / ghostscript), and PPTX (`*.pptx` / zipfile).
Chain Jail leaf only — excavate fossil pin, not a vendored foreign image skill.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Pillow (PIL Fork) Image module — JPEG reader* + *ITU-T T.81 / JFIF* |
| **Heading** | **`Image.open` + JPEG COM on `.jpg`** — Open a JPEG; read the COM marker via `Image.info["comment"]` |
| **Dialect pinned** | **Pillow 11.1.0 `Image.open` + JPEG COM** on a `.jpg` with `comment=EMPEROR-TIME-JPEG-PROBE-OK` — **not** full ImageMagick / libjpeg-tools / ffmpeg suite claim |
| **URL** | https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg (Pillow JPEG); https://www.w3.org/Graphics/JPEG/ (W3C JPEG overview); python3-pil 11.1.0-5+deb13u4 on box |
| **Anchors** | `.jpg` / `.jpeg` path; `Image.open(path)`; `im.info["comment"]`; Pillow version |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Pillow JPEG docs)

> Pillow reads JPEG, JFIF, and Adobe JPEG files containing L, RGB, or CMYK data. […] comment — A comment about the image, from the COM marker. This is separate from the UserComment tag that may be stored in the EXIF data.

(Source: Pillow handbook Image file formats — JPEG
https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg
accessed 2026-09-28 Europe/Tirane;
W3C Graphics JPEG overview https://www.w3.org/Graphics/JPEG/ accessed 2026-09-28 Europe/Tirane.
Installed `python3 -c "import PIL; print(PIL.__version__)"` reports 11.1.0.
Probe uses
`Image.open("HELLO.jpg").info.get("comment")`
so Pillow opens the JPEG and returns the probe token from the COM marker.
Format: RGB 64×32 JPEG with COM `EMPEROR-TIME-JPEG-PROBE-OK`.)

### Why this heading (HELLO.jpg / excavate)

A minimal HELLO surface looks like a small RGB JPEG with a COM
marker carrying the probe token. That is exactly the pinned form:
**Pillow `Image.open` + JPEG COM on `.jpg`**, observe comment bytes at run time.

### Honesty

- VERIFIED: Pillow 11.1.0 `Image.open` + JPEG COM `comment=EMPEROR-TIME-JPEG-PROBE-OK` on this HELLO (RGB 64×32).
- CONJECTURE: any claim that ImageMagick / libjpeg-tools / ffmpeg / Cairo / Skia are this dialect.
- UNVERIFIABLE: Debian imagemagick / ffmpeg / full multi-dialect image recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, ImageMagick/ffmpeg as leaf owner (wrong owner / ET identify collision); graphviz this turn (multi-dep); bare `imagemagick` / `magick` / `convert` / `identify` as verified JPEG toolchain; stealing plain `*.png` or `*.wav` or `*.pdf` or `*.ps` or `*.pptx` ownership from prior leaves; vendoring foreign image skills as this Jail pin.
