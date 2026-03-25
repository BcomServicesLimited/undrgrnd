#!/usr/bin/env python3
"""
Complete button/CTA audit for UNDRGRND Movement website.
Maps every button against the new URL rules and flags what needs to change.

URL Rules:
  VIEW_TIMETABLE   -> https://www.undrgrnd.com.au/timetable
  BOOK_GENERAL     -> https://app.classmanager.com/classes/undrgrnd-movement
  BOOK_SPECIFIC    -> https://app.classmanager.com/portal/undrgrnd-movement/register
  BOOK_FIRST       -> https://app.classmanager.com/classes/undrgrnd-movement
  LOGIN            -> https://app.classmanager.com/portal/undrgrnd-movement/login
"""

import os
import re
from collections import defaultdict

ROOT = '/home/ubuntu/undrgrnd'

# ── URL rules ──────────────────────────────────────────────────────────────────
RULES = {
    'VIEW_TIMETABLE':  'https://www.undrgrnd.com.au/timetable',
    'BOOK_GENERAL':    'https://app.classmanager.com/classes/undrgrnd-movement',
    'BOOK_SPECIFIC':   'https://app.classmanager.com/portal/undrgrnd-movement/register',
    'BOOK_FIRST':      'https://app.classmanager.com/classes/undrgrnd-movement',
    'LOGIN':           'https://app.classmanager.com/portal/undrgrnd-movement/login',
}

# ── Classify a button by its text into a rule category ────────────────────────
def classify_button(text, is_program_page):
    t = text.lower().strip()

    # View Timetable
    if re.search(r'view\s+timetable|check\s+(the\s+)?schedule|see\s+timetable', t):
        return 'VIEW_TIMETABLE'

    # Login
    if re.search(r'\blogin\b|\blog\s+in\b|\bmy\s+account\b|\bstudent\s+portal\b', t):
        return 'LOGIN'

    # Book Your First Class (specific text)
    if re.search(r'book\s+your\s+first', t):
        return 'BOOK_FIRST'

    # Specific booking on a class page
    if is_program_page:
        if re.search(
            r'^book\s+(this\s+class|drop.?in|a\s+class|now|aerial|pole|yoga|dance|flow|'
            r'recovery|movement|fusion|contemporary|silks|groove|burn|kids|creative|'
            r'choreography|traditional|strength|afro)',
            t
        ):
            return 'BOOK_SPECIFIC'
        if re.search(r'^(book|enrol|register|get\s+(pack|class\s+pack)|go\s+unlimited)', t):
            return 'BOOK_SPECIFIC'
        if re.search(r'i\s+have\s+clearance', t):
            return 'BOOK_SPECIFIC'

    # General Book Now (header, footer, general pages)
    if re.search(r'\bbook\s*(now|online)?\b|\benrol\b|\bregister\b|\bget\s+started\b|\bjoin\s+(now|us)\b', t):
        return 'BOOK_GENERAL'

    return None  # Not a booking/timetable button

# ── Get all active HTML files ──────────────────────────────────────────────────
def get_html_files():
    files = []
    core = ['index.html', 'adults.html', 'kids.html', 'timetable.html',
            'about.html', 'contact.html', '404.html',
            'privacy-policy.html', 'terms-of-service.html']
    for f in core:
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            files.append((f, p, False))

    comp_dir = os.path.join(ROOT, 'components')
    if os.path.isdir(comp_dir):
        for f in sorted(os.listdir(comp_dir)):
            if f.endswith('.html'):
                files.append((f'components/{f}', os.path.join(comp_dir, f), False))

    legacy = {
        'movement-dance.html', 'recovery-movement.html', 'yoga-fusion.html',
        'modern-yoga.html', 'traditional-yoga.html', 'aerial-yoga.html',
        'choreography-fusion.html', 'pole-flow.html', 'aerial-silks.html',
    }
    prog_dir = os.path.join(ROOT, 'programs')
    for f in sorted(os.listdir(prog_dir)):
        if f.endswith('.html') and f not in legacy:
            files.append((f'programs/{f}', os.path.join(prog_dir, f), True))

    return files

# ── Extract <a> buttons from a file ───────────────────────────────────────────
def extract_links(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()

    results = []
    a_re = re.compile(r'<a\s+([^>]*?)>(.*?)</a>', re.IGNORECASE | re.DOTALL)

    BUTTON_CLASSES = [
        'cta-button', 'cta-btn', 'btn', 'button',
        'cta-primary', 'cta-secondary', 'cta-link',
        'btn-primary', 'btn-secondary', 'btn-learn', 'btn-book',
        'hero-cta', 'nav-cta', 'footer-cta',
        'book-btn', 'booking-btn', 'primary-btn', 'secondary-btn',
        'waitlist-btn', 'join-waitlist',
    ]
    CTA_TEXT_RE = re.compile(
        r'book|enrol|register|sign\s*up|get\s*started|join|view\s*timetable|'
        r'check\s*schedule|learn\s*more|contact\s*us|call\s*us|email\s*us|'
        r'start\s*your|try\s*(it|now|a\s*class)?|explore|see\s*(all|more|classes)|'
        r'coming\s*soon|waitlist|login|log\s*in|my\s*account',
        re.IGNORECASE
    )

    seen = set()
    for match in a_re.finditer(content):
        attrs = match.group(1)
        inner = match.group(2)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        text = re.sub(r'\s+', ' ', text).strip()
        if not text or len(text) > 120:
            continue

        href_m = re.search(r'href=["\']([^"\']*)["\']', attrs)
        href = href_m.group(1) if href_m else ''
        if not href:
            continue

        class_m = re.search(r'class=["\']([^"\']*)["\']', attrs)
        classes = class_m.group(1) if class_m else ''

        is_button = any(bc in classes for bc in BUTTON_CLASSES) or bool(CTA_TEXT_RE.search(text))
        if not is_button:
            continue

        key = (text.lower(), href)
        if key in seen:
            continue
        seen.add(key)

        results.append({'text': text, 'href': href, 'classes': classes})

    return results

# ── Main audit ─────────────────────────────────────────────────────────────────
def main():
    files = get_html_files()

    # Collect all findings
    findings = []  # (filename, is_program, text, current_href, rule, correct_href, status)

    for filename, filepath, is_program in files:
        links = extract_links(filepath)
        for link in links:
            text = link['text']
            href = link['href']

            rule = classify_button(text, is_program)
            if rule is None:
                continue

            correct = RULES[rule]
            if href == correct:
                status = 'OK'
            else:
                status = 'CHANGE'

            findings.append({
                'file': filename,
                'is_program': is_program,
                'text': text,
                'current': href,
                'rule': rule,
                'correct': correct,
                'status': status,
            })

    # ── Build report ──────────────────────────────────────────────────────────
    lines = []
    lines.append('# UNDRGRND Movement — Button Audit & Recommended Changes')
    lines.append('')
    lines.append('**URL Rules Applied:**')
    lines.append('')
    lines.append('| Rule | Correct URL |')
    lines.append('|---|---|')
    for rule, url in RULES.items():
        lines.append(f'| {rule} | `{url}` |')
    lines.append('')

    # Summary counts
    total = len(findings)
    needs_change = [f for f in findings if f['status'] == 'CHANGE']
    already_ok = [f for f in findings if f['status'] == 'OK']

    lines.append('## Summary')
    lines.append('')
    lines.append(f'- **Total buttons audited:** {total}')
    lines.append(f'- **Already correct:** {len(already_ok)}')
    lines.append(f'- **Needs updating:** {len(needs_change)}')
    lines.append('')

    # Breakdown by rule
    lines.append('### Changes needed by rule type')
    lines.append('')
    lines.append('| Rule | Needs Change | Already OK |')
    lines.append('|---|---|---|')
    for rule in RULES:
        rule_findings = [f for f in findings if f['rule'] == rule]
        change = sum(1 for f in rule_findings if f['status'] == 'CHANGE')
        ok = sum(1 for f in rule_findings if f['status'] == 'OK')
        lines.append(f'| {rule} | {change} | {ok} |')
    lines.append('')

    # ── Recommended changes section ───────────────────────────────────────────
    lines.append('---')
    lines.append('')
    lines.append('## Recommended Changes')
    lines.append('')
    lines.append('The following buttons need their `href` updated. Grouped by file.')
    lines.append('')

    # Group changes by file
    changes_by_file = defaultdict(list)
    for f in needs_change:
        changes_by_file[f['file']].append(f)

    # Sort: core pages first, then components, then programs
    def sort_key(fname):
        if fname.startswith('components/'):
            return (1, fname)
        elif fname.startswith('programs/'):
            return (2, fname)
        else:
            return (0, fname)

    for filename in sorted(changes_by_file.keys(), key=sort_key):
        file_changes = changes_by_file[filename]
        lines.append(f'### `{filename}`')
        lines.append('')
        lines.append('| Button Text | Current URL | Rule | Correct URL |')
        lines.append('|---|---|---|---|')
        for fc in file_changes:
            cur = fc['current']
            if len(cur) > 60:
                cur = cur[:57] + '...'
            cor = fc['correct']
            lines.append(f'| {fc["text"][:55]} | `{cur}` | {fc["rule"]} | `{cor}` |')
        lines.append('')

    # ── Already correct section ────────────────────────────────────────────────
    lines.append('---')
    lines.append('')
    lines.append('## Already Correct (No Changes Needed)')
    lines.append('')
    lines.append('| File | Button Text | URL | Rule |')
    lines.append('|---|---|---|---|')
    for f in already_ok:
        lines.append(f'| `{f["file"]}` | {f["text"][:45]} | `{f["correct"]}` | {f["rule"]} |')
    lines.append('')

    return '\n'.join(lines)

if __name__ == '__main__':
    report = main()
    out = '/home/ubuntu/undrgrnd/button_audit_v2_report.md'
    with open(out, 'w') as fh:
        fh.write(report)
    print(f'Written: {out}')
    print(f'Lines: {len(report.splitlines())}')
