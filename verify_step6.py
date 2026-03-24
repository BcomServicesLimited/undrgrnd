#!/usr/bin/env python3
"""
Step 6: Comprehensive verification of UNDRGRND Movement website.
Checks file structure, content, links, site-config.json, SEO, NAP, and brand consistency.
"""
import os
import re
import json

BASE = '/home/ubuntu/undrgrnd'
ISSUES = []
WARNINGS = []
PASSES = []

def fail(msg):
    ISSUES.append(f'  FAIL: {msg}')

def warn(msg):
    WARNINGS.append(f'  WARN: {msg}')

def ok(msg):
    PASSES.append(f'  PASS: {msg}')

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

# ============================================================
# 6A: FILE STRUCTURE
# ============================================================
print('\n=== 6A: FILE STRUCTURE ===')

REQUIRED_PROGRAM_FILES = [
    # Adults Dance
    'programs/afro-groove-foundations.html',
    'programs/booty-burn-foundations.html',
    'programs/movement-flow-foundations.html',
    'programs/recovery-movement-flow-foundations.html',
    # Adults Pole
    'programs/pole-fitness-foundations.html',
    'programs/pole-flow-foundations.html',
    'programs/pole-strength-movement.html',
    # Adults Yoga
    'programs/fusion-yoga-foundations.html',
    'programs/traditional-yoga-foundations.html',
    'programs/flow-yoga-foundations.html',
    'programs/aerial-yoga-foundations.html',
    # Adults Aerial
    'programs/aerial-silks-foundations.html',
    # Adults Choreography
    'programs/choreography-fusion-foundations.html',
    # Kids (actual filenames match site-config.json slugs)
    'programs/kids-yoga.html',
    'programs/kids-aerial-yoga.html',
    'programs/kids-pole-foundations.html',
    'programs/kids-aerial-silks.html',
    'programs/kids-dance-moves.html',
    'programs/kids-modern-contemporary.html',
    'programs/kids-creative-dance.html',
]

REQUIRED_CORE_FILES = [
    'index.html', 'adults.html', 'kids.html', 'timetable.html',
    'about.html', 'contact.html', 'privacy-policy.html',
    'terms-of-service.html', '404.html',
    'components/nav-component.html', 'components/footer-component.html',
    'site-config.json', 'css/global.css',
]

for f in REQUIRED_PROGRAM_FILES + REQUIRED_CORE_FILES:
    path = os.path.join(BASE, f)
    if os.path.exists(path):
        ok(f'{f} exists')
    else:
        fail(f'{f} MISSING')

# ============================================================
# 6B: CONTENT VERIFICATION (key pages)
# ============================================================
print('\n=== 6B: CONTENT VERIFICATION ===')

# Check all new/renamed program pages
PROGRAM_PAGES = [
    ('programs/booty-burn-foundations.html', 'Booty Burn - Foundations', False),
    ('programs/movement-flow-foundations.html', 'Movement Flow - Foundations', False),
    ('programs/recovery-movement-flow-foundations.html', 'Recovery Movement Flow - Foundations', True),
    ('programs/pole-flow-foundations.html', 'Pole Flow - Foundations', True),
    ('programs/fusion-yoga-foundations.html', 'Fusion Yoga - Foundations', False),
    ('programs/traditional-yoga-foundations.html', 'Traditional Yoga - Foundations', False),
    ('programs/flow-yoga-foundations.html', 'Flow Yoga - Foundations', False),
    ('programs/aerial-yoga-foundations.html', 'Aerial Yoga - Foundations', False),
    ('programs/aerial-silks-foundations.html', 'Aerial Silks - Foundations', False),
    ('programs/choreography-fusion-foundations.html', 'Choreography Fusion - Foundations', False),
    ('programs/pole-fitness-foundations.html', 'Pole Fitness - Foundations', True),
    ('programs/afro-groove-foundations.html', 'Afro Groove - Foundations', False),
    ('programs/kids-yoga.html', 'Kids Yoga', False),
    ('programs/kids-aerial-yoga.html', 'Kids Aerial Yoga', True),
    ('programs/kids-pole-foundations.html', 'Pole Fitness Kids', True),
    ('programs/kids-aerial-silks.html', 'Kids Aerial Silks', True),
    ('programs/kids-dance-moves.html', 'Dance Moves', False),
    ('programs/kids-modern-contemporary.html', 'Contemporary', False),
    ('programs/kids-creative-dance.html', 'Creative Dance', False),
]

for filepath, expected_name, is_coming_soon in PROGRAM_PAGES:
    content = read_file(os.path.join(BASE, filepath))
    if not content:
        fail(f'{filepath}: cannot read file')
        continue
    
    # Check H1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if h1_match:
        h1_text = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        if expected_name.lower() in h1_text.lower():
            ok(f'{filepath}: H1 contains "{expected_name}"')
        else:
            fail(f'{filepath}: H1 is "{h1_text}", expected to contain "{expected_name}"')
    else:
        fail(f'{filepath}: No H1 found')
    
    # Check title tag
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        title = title_match.group(1)
        if 'Foundations' in title or 'foundations' in title.lower():
            ok(f'{filepath}: title contains Foundations')
        else:
            warn(f'{filepath}: title may not have Foundations: "{title[:60]}"')
    else:
        fail(f'{filepath}: No title tag')
    
    # Check canonical
    if 'rel="canonical"' in content:
        ok(f'{filepath}: canonical present')
    else:
        fail(f'{filepath}: No canonical tag')
    
    # Check booking URL
    booking_url = 'https://undrgrnd-movement.classmanager.com/register'
    if booking_url in content:
        ok(f'{filepath}: correct booking URL present')
    else:
        fail(f'{filepath}: booking URL missing or incorrect')
    
    # Check coming-soon badge
    if is_coming_soon:
        if 'coming-soon' in content.lower() or 'Coming Soon' in content:
            ok(f'{filepath}: Coming Soon badge present')
        else:
            fail(f'{filepath}: Coming Soon badge MISSING (should be coming soon)')
    
    # Check old program names
    old_names = ['Movement Dance', 'Recovery Movement Dance', 'Yoga Fusion', 'Modern Yoga']
    for old in old_names:
        if old in content:
            fail(f'{filepath}: Still contains old name "{old}"')

# ============================================================
# 6C: LINK VERIFICATION
# ============================================================
print('\n=== 6C: LINK VERIFICATION ===')

OLD_URLS = [
    '/programs/movement-dance.html',
    '/programs/recovery-movement.html',
    '/programs/yoga-fusion.html',
    '/programs/modern-yoga.html',
    '/programs/pole-flow.html',
    '/programs/traditional-yoga.html',
    '/programs/aerial-yoga.html',
    '/programs/choreography-fusion.html',
]

# Check all HTML files for old URLs
all_html = []
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules']]
    for f in files:
        if f.endswith('.html'):
            all_html.append(os.path.join(root, f))

old_url_issues = 0
for html_path in sorted(all_html):
    content = read_file(html_path)
    if not content:
        continue
    rel = os.path.relpath(html_path, BASE)
    for old_url in OLD_URLS:
        if old_url in content:
            fail(f'{rel}: Contains old URL "{old_url}"')
            old_url_issues += 1

if old_url_issues == 0:
    ok('No old program URLs found in any HTML file')

# Check new program pages exist for all internal links
new_program_links = set()
for html_path in all_html:
    content = read_file(html_path)
    if not content:
        continue
    links = re.findall(r'href=["\'](/programs/[^"\'#?]+\.html)', content)
    for link in links:
        new_program_links.add(link)

for link in sorted(new_program_links):
    target = os.path.join(BASE, link.lstrip('/'))
    if os.path.exists(target):
        ok(f'Link target exists: {link}')
    else:
        fail(f'BROKEN LINK target: {link}')

# ============================================================
# 6D: SITE-CONFIG.JSON VERIFICATION
# ============================================================
print('\n=== 6D: SITE-CONFIG.JSON VERIFICATION ===')

config_path = os.path.join(BASE, 'site-config.json')
config_content = read_file(config_path)
if config_content:
    try:
        config = json.loads(config_content)
        ok('site-config.json is valid JSON')
        
        # Check old IDs are gone
        config_str = json.dumps(config)
        old_ids = ['movement-dance', 'yoga-fusion', 'modern-yoga']
        for old_id in old_ids:
            # Check if it appears as a slug/id (not in a description)
            if f'"slug": "{old_id}"' in config_str or f'"id": "{old_id}"' in config_str:
                fail(f'site-config.json: old ID "{old_id}" still present')
            else:
                ok(f'site-config.json: old ID "{old_id}" not present as slug/id')
        
        # Check new programs exist
        new_slugs = ['booty-burn', 'movement-flow', 'recovery-flow', 'fusion-yoga', 'flow-yoga']
        for slug in new_slugs:
            if slug in config_str:
                ok(f'site-config.json: "{slug}" found')
            else:
                warn(f'site-config.json: "{slug}" not found')
        
        # Check intensity_groups (stored under programs.adults.intensity_groups)
        if 'intensity_groups' in config_str:
            ok('site-config.json: intensity_groups section exists')
        else:
            fail('site-config.json: intensity_groups section MISSING')
        
        # Check age_bands (stored under programs.kids.age_bands)
        if 'age_bands' in config_str:
            ok('site-config.json: age_bands section exists')
        else:
            fail('site-config.json: age_bands section MISSING')
            
    except json.JSONDecodeError as e:
        fail(f'site-config.json: Invalid JSON - {e}')
else:
    fail('site-config.json: Cannot read file')

# ============================================================
# 6I: SEO & NAP VERIFICATION
# ============================================================
print('\n=== 6I: SEO & NAP VERIFICATION ===')

NAP_EMAIL = 'undrgrndgc@gmail.com'
NAP_PHONE_DISPLAY = '0721 402 690'
NAP_ADDRESS = '163 Ferry Rd'
BRAND_NAME = 'UNDRGRND Movement'
WRONG_BRANDS = ['UNDGRND Movement', 'UNDRGRUND Movement', 'UNDRGRND  Movement']

CORE_PAGES = ['index.html', 'adults.html', 'kids.html', 'timetable.html', 'about.html', 'contact.html']

for page in CORE_PAGES:
    content = read_file(os.path.join(BASE, page))
    if not content:
        fail(f'{page}: Cannot read')
        continue
    
    # Check brand name spelling
    for wrong in WRONG_BRANDS:
        if wrong in content:
            fail(f'{page}: Wrong brand name "{wrong}"')
    
    # Check meta description
    if '<meta name="description"' in content:
        ok(f'{page}: meta description present')
    else:
        fail(f'{page}: meta description MISSING')
    
    # Check Open Graph
    if 'og:title' in content:
        ok(f'{page}: OG tags present')
    else:
        warn(f'{page}: OG tags missing')

# Check NAP in footer component
footer = read_file(os.path.join(BASE, 'components/footer-component.html'))
if footer:
    if NAP_EMAIL in footer:
        ok(f'Footer: email {NAP_EMAIL} present')
    else:
        fail(f'Footer: email {NAP_EMAIL} MISSING')
    
    if NAP_PHONE_DISPLAY in footer:
        ok(f'Footer: phone {NAP_PHONE_DISPLAY} present')
    else:
        fail(f'Footer: phone {NAP_PHONE_DISPLAY} MISSING')
    
    if NAP_ADDRESS in footer:
        ok(f'Footer: address {NAP_ADDRESS} present')
    else:
        fail(f'Footer: address {NAP_ADDRESS} MISSING')

# ============================================================
# 6K: CONTENT CONSISTENCY
# ============================================================
print('\n=== 6K: CONTENT CONSISTENCY ===')

# Check no old program names in active pages (excluding legacy files)
LEGACY_FILES = {
    'programs/movement-dance.html', 'programs/recovery-movement.html',
    'programs/yoga-fusion.html', 'programs/modern-yoga.html',
    'programs/traditional-yoga.html', 'programs/aerial-yoga.html',
    'programs/choreography-fusion.html', 'programs/pole-flow.html',
    'programs/aerial-silks.html',
}
OLD_NAMES_CHECK = ['Movement Dance', 'Recovery Movement Dance', 'Yoga Fusion', 'Modern Yoga']

old_name_issues = 0
for html_path in sorted(all_html):
    rel = os.path.relpath(html_path, BASE)
    if rel in LEGACY_FILES:
        continue
    content = read_file(html_path)
    if not content:
        continue
    for old_name in OLD_NAMES_CHECK:
        if old_name in content:
            fail(f'{rel}: Contains old name "{old_name}"')
            old_name_issues += 1

if old_name_issues == 0:
    ok('No old program names found in any active HTML file')

# ============================================================
# SUMMARY
# ============================================================
print('\n' + '='*60)
print('VERIFICATION SUMMARY')
print('='*60)
print(f'\nPASSED: {len(PASSES)}')
print(f'WARNINGS: {len(WARNINGS)}')
print(f'FAILED: {len(ISSUES)}')

if ISSUES:
    print('\n--- FAILURES ---')
    for i in ISSUES:
        print(i)

if WARNINGS:
    print('\n--- WARNINGS ---')
    for w in WARNINGS:
        print(w)

print('\n--- READY FOR DEPLOYMENT:', 'YES' if len(ISSUES) == 0 else 'NO - FIX ISSUES ABOVE', '---')
