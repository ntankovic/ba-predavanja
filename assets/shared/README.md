# Shared course assets

## FIPU logo

- Original: `fipu-dark.pdf`, supplied by the lecturer on 2026-09-14.
- Derived vector PDF: `fipu-logo.pdf`, for LaTeX/PDF publishing.
- Derived SVG: `fipu-logo.svg`, for HTML slides; lettering is converted to paths to avoid font dependencies.
- Derived transparent PNG: `fipu-logo.png`, 1128 × 1126 pixels, for software requiring raster images.

The visible artwork is a light-blue circle with white FIPU lettering. Derivatives isolate that artwork from the original A4 page using the source-page rectangle `(16, 139, 580, 702)` in PDF points, preserving its proportions and colours. The original is unchanged. The PDF and a raster preview were visually checked.

The logo is integrated into the book title page, all slide decks through `publishing/slides/revealjs.yml`. Use the SVG for browser output and the vector PDF for printed output. Keep source provenance when sharing assets; no general redistribution license was supplied.

