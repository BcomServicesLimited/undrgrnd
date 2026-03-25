#!/usr/bin/env python3
"""
Image audit script for UNDRGRND Movement website.
Scans all HTML files for image references (src, srcset, CSS background-image)
and checks whether the referenced files exist on disk.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path("/home/ubuntu/undrgrnd")

# HTML files to scan (exclude old/legacy pages and components)
LEGACY_PAGES = {
    "programs/aerial-silks.html",
    "programs/aerial-yoga.html",
    "programs/choreography-fusion.html",
    "programs/modern-yoga.html",
    "programs/movement-dance.html",
    "programs/pole-flow.html",
    "programs/recovery-movement.html",
    "programs/traditional-yoga.html",
    "programs/yoga-fusion.html",
}

def find_html_files():
    html_files = []
    for p in sorted(REPO_ROOT.rglob("*.html")):
        rel = str(p.relative_to(REPO_ROOT))
        if rel.startswith("components/"):
            continue
        html_files.append(rel)
    return html_files

def extract_images(html_path):
    """Extract all image src/srcset/background-image references from an HTML file."""
    full_path = REPO_ROOT / html_path
    content = full_path.read_text(encoding="utf-8", errors="replace")
    
    images = []
    
    # <img src="...">
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE):
        images.append(("img src", m.group(1), m.start()))
    
    # <img srcset="...">
    for m in re.finditer(r'<img[^>]+srcset=["\']([^"\']+)["\']', content, re.IGNORECASE):
        # srcset can have multiple entries like "url 2x, url2 1x"
        for entry in m.group(1).split(","):
            url = entry.strip().split()[0]
            if url:
                images.append(("img srcset", url, m.start()))
    
    # <source srcset="..."> (picture element)
    for m in re.finditer(r'<source[^>]+srcset=["\']([^"\']+)["\']', content, re.IGNORECASE):
        for entry in m.group(1).split(","):
            url = entry.strip().split()[0]
            if url:
                images.append(("source srcset", url, m.start()))
    
    # CSS background-image: url(...)
    for m in re.finditer(r'background(?:-image)?\s*:\s*url\(["\']?([^"\')\s]+)["\']?\)', content, re.IGNORECASE):
        images.append(("css background", m.group(1), m.start()))
    
    # CSS content: url(...) (rare but possible)
    for m in re.finditer(r'content\s*:\s*url\(["\']?([^"\')\s]+)["\']?\)', content, re.IGNORECASE):
        images.append(("css content", m.group(1), m.start()))
    
    return images

def resolve_path(src, html_path):
    """Resolve an image src to a filesystem path relative to REPO_ROOT."""
    if src.startswith("http://") or src.startswith("https://"):
        return None, "external"
    if src.startswith("data:"):
        return None, "data-uri"
    if src.startswith("/"):
        # Absolute path from repo root
        rel = src.lstrip("/")
        return REPO_ROOT / rel, rel
    else:
        # Relative path from the HTML file's directory
        html_dir = (REPO_ROOT / html_path).parent
        resolved = (html_dir / src).resolve()
        try:
            rel = str(resolved.relative_to(REPO_ROOT))
        except ValueError:
            rel = str(resolved)
        return resolved, rel

def check_file_exists(path):
    if path is None:
        return None
    return path.exists()

def run_audit():
    html_files = find_html_files()
    
    results = []
    
    for html_path in html_files:
        is_legacy = html_path in LEGACY_PAGES
        images = extract_images(html_path)
        
        page_images = []
        for (ref_type, src, pos) in images:
            fs_path, rel = resolve_path(src, html_path)
            if rel == "external":
                status = "external"
                exists = None
            elif rel == "data-uri":
                status = "data-uri"
                exists = None
            else:
                exists = check_file_exists(fs_path)
                status = "OK" if exists else "MISSING"
            
            page_images.append({
                "ref_type": ref_type,
                "src": src,
                "resolved": rel,
                "status": status,
            })
        
        results.append({
            "page": html_path,
            "legacy": is_legacy,
            "image_count": len(page_images),
            "images": page_images,
        })
    
    return results

def summarise(results):
    total_pages = len(results)
    pages_with_images = sum(1 for r in results if r["image_count"] > 0)
    total_refs = sum(r["image_count"] for r in results)
    missing = []
    for r in results:
        for img in r["images"]:
            if img["status"] == "MISSING":
                missing.append((r["page"], img["src"], img["resolved"]))
    
    return {
        "total_pages": total_pages,
        "pages_with_images": pages_with_images,
        "total_image_refs": total_refs,
        "missing_count": len(missing),
        "missing": missing,
    }

if __name__ == "__main__":
    results = run_audit()
    summary = summarise(results)
    
    # Save raw results
    with open(REPO_ROOT / "image_audit_raw.json", "w") as f:
        json.dump({"summary": summary, "pages": results}, f, indent=2)
    
    print(f"Total pages scanned: {summary['total_pages']}")
    print(f"Pages with images: {summary['pages_with_images']}")
    print(f"Total image references: {summary['total_image_refs']}")
    print(f"Missing files: {summary['missing_count']}")
    if summary["missing"]:
        print("\nMISSING FILES:")
        for page, src, resolved in summary["missing"]:
            print(f"  [{page}] src='{src}' → '{resolved}'")
