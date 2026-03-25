#!/usr/bin/env python3
"""
Audit all buttons and CTAs across the UNDRGRND Movement website.
Extracts <a> tags with button-like classes or text, and <button> elements.
"""

import os
import re
from collections import defaultdict

ROOT = '/home/ubuntu/undrgrnd'

# Classes that indicate a button/CTA
BUTTON_CLASSES = [
    'cta-button', 'cta-btn', 'btn', 'button',
    'cta-primary', 'cta-secondary', 'cta-link',
    'btn-primary', 'btn-secondary', 'btn-learn', 'btn-book',
    'hero-cta', 'nav-cta', 'footer-cta',
    'book-btn', 'booking-btn',
    'primary-btn', 'secondary-btn',
    'waitlist-btn', 'join-waitlist',
]

# Text patterns that indicate a CTA link
CTA_TEXT_PATTERNS = [
    r'book\s*(now|this|your|a\s*class)?',
    r'enrol\s*(now)?',
    r'register',
    r'sign\s*up',
    r'get\s*started',
    r'reserve',
    r'join\s*(waitlist|now|us)?',
    r'view\s*timetable',
    r'check\s*schedule',
    r'learn\s*more',
    r'find\s*out\s*more',
    r'contact\s*us',
    r'call\s*us',
    r'email\s*us',
    r'start\s*(your|my)?',
    r'try\s*(it|now|a\s*class)?',
    r'explore',
    r'see\s*(all|more|classes)',
    r'coming\s*soon',
    r'waitlist',
]

CTA_TEXT_RE = re.compile('|'.join(CTA_TEXT_PATTERNS), re.IGNORECASE)

def get_html_files():
    """Get all HTML files, excluding old legacy pages."""
    files = []
    # Core pages
    for f in ['index.html', 'adults.html', 'kids.html', 'timetable.html',
              'about.html', 'contact.html', '404.html',
              'privacy-policy.html', 'terms-of-service.html']:
        path = os.path.join(ROOT, f)
        if os.path.exists(path):
            files.append((f, path))

    # Component files
    for f in os.listdir(os.path.join(ROOT, 'components')):
        if f.endswith('.html'):
            files.append((f'components/{f}', os.path.join(ROOT, 'components', f)))

    # Program pages (active ones only - skip old legacy pages)
    legacy = {
        'movement-dance.html', 'recovery-movement.html', 'yoga-fusion.html',
        'modern-yoga.html', 'traditional-yoga.html', 'aerial-yoga.html',
        'choreography-fusion.html', 'pole-flow.html', 'aerial-silks.html',
    }
    prog_dir = os.path.join(ROOT, 'programs')
    for f in sorted(os.listdir(prog_dir)):
        if f.endswith('.html') and f not in legacy:
            files.append((f'programs/{f}', os.path.join(prog_dir, f)))

    return files

def extract_buttons(filepath):
    """Extract all button-like elements from an HTML file."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()

    buttons = []

    # Pattern 1: <a> tags with button classes
    a_tag_re = re.compile(
        r'<a\s+([^>]*?)>(.*?)</a>',
        re.IGNORECASE | re.DOTALL
    )

    for match in a_tag_re.finditer(content):
        attrs = match.group(1)
        inner = match.group(2)
        # Clean inner text
        text = re.sub(r'<[^>]+>', '', inner).strip()
        text = re.sub(r'\s+', ' ', text).strip()

        # Get href
        href_match = re.search(r'href=["\']([^"\']*)["\']', attrs)
        href = href_match.group(1) if href_match else '#'

        # Get class
        class_match = re.search(r'class=["\']([^"\']*)["\']', attrs)
        classes = class_match.group(1) if class_match else ''

        # Determine if this is a button
        is_button = False
        reason = ''

        # Check if any button class is present
        for bc in BUTTON_CLASSES:
            if bc in classes:
                is_button = True
                reason = f'class:{bc}'
                break

        # Check if text matches CTA patterns
        if not is_button and text and CTA_TEXT_RE.search(text):
            is_button = True
            reason = f'text:{text[:30]}'

        if is_button and text and href:
            buttons.append({
                'text': text[:60],
                'href': href,
                'classes': classes[:80],
                'reason': reason,
            })

    # Pattern 2: <button> elements
    button_re = re.compile(r'<button\s+([^>]*?)>(.*?)</button>', re.IGNORECASE | re.DOTALL)
    for match in button_re.finditer(content):
        attrs = match.group(1)
        inner = match.group(2)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        text = re.sub(r'\s+', ' ', text).strip()
        # Get onclick or data-href
        onclick_match = re.search(r'onclick=["\']([^"\']*)["\']', attrs)
        href = onclick_match.group(1) if onclick_match else '(no href - JS button)'
        if text:
            buttons.append({
                'text': text[:60],
                'href': href,
                'classes': '',
                'reason': 'button element',
            })

    # Deduplicate within this file
    seen = set()
    unique = []
    for b in buttons:
        key = (b['text'].lower(), b['href'])
        if key not in seen:
            seen.add(key)
            unique.append(b)

    return unique

def categorise_href(href):
    """Categorise a URL into a human-readable destination type."""
    if not href or href == '#':
        return 'Anchor / No destination'
    if href.startswith('mailto:'):
        return 'Email'
    if href.startswith('tel:'):
        return 'Phone call'
    if 'classmanager.com/classes' in href:
        return 'Class Manager — Browse & Book'
    if 'classmanager.com/portal' in href and 'register' in href:
        return 'Class Manager — New Student Register'
    if 'classmanager.com/portal' in href and 'login' in href:
        return 'Class Manager — Student Login'
    if 'classmanager.com' in href:
        return 'Class Manager (other)'
    if href.startswith('/') or href.startswith('./') or not href.startswith('http'):
        return 'Internal page'
    if href.startswith('http'):
        return 'External URL'
    return 'Other'

def main():
    files = get_html_files()
    report = []

    # Group: core pages, components, programs
    groups = {
        'Core Pages': [],
        'Components': [],
        'Program Pages': [],
    }

    for filename, filepath in files:
        buttons = extract_buttons(filepath)
        if not buttons:
            continue

        if filename.startswith('components/'):
            group = 'Components'
        elif filename.startswith('programs/'):
            group = 'Program Pages'
        else:
            group = 'Core Pages'

        groups[group].append((filename, buttons))

    # Build report
    lines = []
    lines.append('# UNDRGRND Movement — Button & CTA Audit Report')
    lines.append('')
    lines.append('Generated from all active HTML files in the repository.')
    lines.append('')

    # Summary table first
    lines.append('## Summary: Destination Types')
    lines.append('')
    dest_counts = defaultdict(int)
    all_buttons = []
    for group_name, group_files in groups.items():
        for filename, buttons in group_files:
            for b in buttons:
                dest = categorise_href(b['href'])
                dest_counts[dest] += 1
                all_buttons.append((filename, b['text'], b['href'], dest))

    lines.append('| Destination Type | Count |')
    lines.append('|---|---|')
    for dest, count in sorted(dest_counts.items(), key=lambda x: -x[1]):
        lines.append(f'| {dest} | {count} |')
    lines.append('')

    # Detail by group
    for group_name in ['Core Pages', 'Components', 'Program Pages']:
        group_files = groups[group_name]
        if not group_files:
            continue

        lines.append(f'---')
        lines.append('')
        lines.append(f'## {group_name}')
        lines.append('')

        for filename, buttons in sorted(group_files):
            lines.append(f'### `{filename}`')
            lines.append('')
            lines.append('| Button Text | Destination | Type |')
            lines.append('|---|---|---|')
            for b in buttons:
                dest = categorise_href(b['href'])
                href_display = b['href']
                if len(href_display) > 70:
                    href_display = href_display[:67] + '...'
                lines.append(f'| {b["text"]} | `{href_display}` | {dest} |')
            lines.append('')

    return '\n'.join(lines)

if __name__ == '__main__':
    report = main()
    output_path = '/home/ubuntu/undrgrnd/button_audit_report.md'
    with open(output_path, 'w') as f:
        f.write(report)
    print(f'Report written to {output_path}')
    # Also print line count
    print(f'Report lines: {len(report.splitlines())}')
