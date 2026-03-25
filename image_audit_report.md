# UNDRGRND Movement Website Image Audit Report

**Date:** March 25, 2026  
**Author:** Manus AI  
**Scope:** Full repository scan of all active HTML pages (`*.html`)  

## Executive Summary

A comprehensive scan of the UNDRGRND Movement website was conducted to audit all image references across the site. The audit checked `<img>` tags, `<source>` tags (for responsive `srcset` images), and CSS background images to ensure the referenced files exist and render correctly.

The audit revealed that the vast majority of images are displaying correctly across the site. However, **7 active program pages** are currently experiencing broken hero images due to missing files. These missing files are a direct result of the recent page renaming task (adding the `-foundations` suffix), where the HTML references were updated but the corresponding image files were not duplicated or renamed to match.

| Metric | Count |
|--------|-------|
| Total Pages Scanned | 38 |
| Total Image References | 180 |
| Images Displaying Correctly | 159 |
| Missing Image Files | 21 (across 7 pages) |

## Detailed Findings

### 1. Core Pages (Working Correctly)

All core landing pages and structural images are loading perfectly. Visual browser checks confirmed that hero images, instructor portraits, and program cards are rendering as expected.

*   **Homepage (`index.html`)**: All 5 images load correctly, including the main hero image and logos.
*   **Adults Landing (`adults.html`)**: All 6 images load correctly, including the adult hero image.
*   **Kids Landing (`kids.html`)**: All 6 images load correctly, including the kids hero image.
*   **About Page (`about.html`)**: All 3 images load correctly, including the instructor portrait (Olga).
*   **Global Elements**: The header logo (`logo-header.webp`) and footer logo (`logo-full.webp`) load correctly across all pages.

### 2. Program Pages (Working Correctly)

The following program pages have all their images intact and displaying correctly:

*   `programs/aerial-silks-foundations.html`
*   `programs/afro-groove-foundations.html`
*   `programs/booty-burn-foundations.html`
*   `programs/kids-aerial-silks.html`
*   `programs/kids-aerial-yoga.html`
*   `programs/kids-creative-dance.html`
*   `programs/kids-dance-moves.html`
*   `programs/kids-modern-contemporary.html`
*   `programs/kids-pole-foundations.html`
*   `programs/kids-yoga.html`
*   `programs/pole-fitness-foundations.html`
*   `programs/pole-flow-foundations.html`
*   `programs/pole-strength-movement.html`

### 3. Program Pages with Broken Images (Action Required)

The audit identified 7 active program pages where the hero images are broken. In all cases, the HTML is looking for an image file with the `-foundations` suffix, but the actual image file in the `images/hero/` directory still uses the old naming convention.

Each page is missing 3 image references (desktop webp, mobile webp, and fallback).

| Page | Missing Image Reference | Existing Source Image |
|------|-------------------------|-----------------------|
| `aerial-yoga-foundations.html` | `aerial-yoga-foundations.webp` | `aerial-yoga.webp` |
| `choreography-fusion-foundations.html` | `choreography-fusion-foundations.webp` | `choreography-fusion.webp` |
| `flow-yoga-foundations.html` | `flow-yoga-foundations.webp` | `modern-yoga.webp` |
| `fusion-yoga-foundations.html` | `fusion-yoga-foundations.webp` | `yoga-fusion.webp` |
| `movement-flow-foundations.html` | `movement-flow-foundations.webp` | `movement-dance.webp` |
| `recovery-movement-flow-foundations.html` | `recovery-movement-flow-foundations.webp` | `recovery-movement.webp` |
| `traditional-yoga-foundations.html` | `traditional-yoga-foundations.webp` | `traditional-yoga.webp` |

*Note: The same applies to the `-mobile.webp` variants for each of the above.*

## Recommendations

To fix the broken images on the 7 affected pages, the existing image files need to be copied or renamed to match the new `-foundations` naming convention expected by the HTML. 

For example, running the following commands in the terminal will resolve the issue:

```bash
cd images/hero/
cp aerial-yoga.webp aerial-yoga-foundations.webp
cp aerial-yoga-mobile.webp aerial-yoga-foundations-mobile.webp
# ... repeat for the other 6 programs
```

Once these files are duplicated or renamed, all 180 image references across the entire website will display correctly.
