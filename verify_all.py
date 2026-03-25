#!/usr/bin/env python3
"""
Final verification script for UNDRGRND Movement website
Checks: booking URLs, timetable links, related program links, broken internal links
"""
import os
import re
from pathlib import Path

BASE = Path('/home/ubuntu/undrgrnd')

# Expected booking URLs per program
EXPECTED_BOOKING_URLS = {
    'booty-burn-foundations': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/booty-burn-foundations',
    'movement-flow-foundations': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/movement-flow-foundations',
    'fusion-yoga-foundations': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/fusion-yoga-foundations',
    'aerial-silks-foundations': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/aerial-silks-foundations',
    'choreography-fusion-foundations': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/choreography-fusion-foundations',
    'stretch-mobility-foundations': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/stretch-mobility-foundations',
}

# Programs that should be COMING SOON (waitlist/mailto)
COMING_SOON_PROGRAMS = [
    'aerial-yoga-foundations',
    'recovery-movement-flow-foundations',
    'pole-foundations',
    'pole-flow-foundations',
]

# Programs that should NOT exist
DELETED_PROGRAMS = [
    'afro-groove-foundations.html',
    'traditional-yoga-foundations.html',
    'flow-yoga-foundations.html',
]

print("=" * 70)
print("UNDRGRND MOVEMENT — FINAL VERIFICATION REPORT")
print("=" * 70)

issues = []
passes = []

# 1. Check deleted pages don't exist
print("\n[1] CHECKING DELETED PAGES DON'T EXIST")
for fname in DELETED_PROGRAMS:
    fpath = BASE / 'programs' / fname
    if fpath.exists():
        issues.append(f"  FAIL: {fname} still exists (should be deleted)")
    else:
        passes.append(f"  PASS: {fname} correctly deleted")
        print(f"  PASS: {fname} correctly deleted")

# 2. Check new stretch-mobility page exists
print("\n[2] CHECKING NEW STRETCH & MOBILITY PAGE EXISTS")
sm_path = BASE / 'programs' / 'stretch-mobility-foundations.html'
if sm_path.exists():
    passes.append("  PASS: stretch-mobility-foundations.html exists")
    print("  PASS: stretch-mobility-foundations.html exists")
else:
    issues.append("  FAIL: stretch-mobility-foundations.html MISSING")
    print("  FAIL: stretch-mobility-foundations.html MISSING")

# 3. Check booking URLs in active program pages
print("\n[3] CHECKING BOOKING URLS IN PROGRAM PAGES")
for slug, expected_url in EXPECTED_BOOKING_URLS.items():
    fpath = BASE / 'programs' / f'{slug}.html'
    if not fpath.exists():
        issues.append(f"  FAIL: {slug}.html not found")
        continue
    content = fpath.read_text()
    if expected_url in content:
        passes.append(f"  PASS: {slug} has correct booking URL")
        print(f"  PASS: {slug} has correct booking URL")
    else:
        # Check what URL is actually there
        urls = re.findall(r'href="(https://app\.classmanager\.com[^"]*)"', content)
        booking_urls = [u for u in urls if 'enrolment' in u or 'register' in u or 'book' in u.lower()]
        issues.append(f"  FAIL: {slug} missing correct booking URL. Found: {booking_urls[:2]}")
        print(f"  FAIL: {slug} missing correct booking URL")
        if booking_urls:
            print(f"        Found instead: {booking_urls[:2]}")

# 4. Check aerial-yoga is Coming Soon
print("\n[4] CHECKING AERIAL YOGA IS COMING SOON")
aerial_path = BASE / 'programs' / 'aerial-yoga-foundations.html'
if aerial_path.exists():
    content = aerial_path.read_text()
    if 'Coming Soon' in content or 'COMING SOON' in content or 'coming-soon' in content:
        passes.append("  PASS: aerial-yoga-foundations.html has Coming Soon badge")
        print("  PASS: aerial-yoga-foundations.html has Coming Soon badge")
    else:
        issues.append("  FAIL: aerial-yoga-foundations.html missing Coming Soon badge")
        print("  FAIL: aerial-yoga-foundations.html missing Coming Soon badge")
    if 'waitlist' in content.lower() or 'JOIN WAITLIST' in content:
        passes.append("  PASS: aerial-yoga-foundations.html has waitlist button")
        print("  PASS: aerial-yoga-foundations.html has waitlist button")
    else:
        issues.append("  FAIL: aerial-yoga-foundations.html missing waitlist button")
        print("  FAIL: aerial-yoga-foundations.html missing waitlist button")

# 5. Check all internal links to deleted pages across all active -foundations pages
print("\n[5] CHECKING FOR BROKEN LINKS TO DELETED PROGRAMS")
deleted_slugs = ['afro-groove-foundations', 'traditional-yoga-foundations', 'flow-yoga-foundations']
all_html = list(BASE.glob('*.html')) + list((BASE / 'programs').glob('*-foundations.html'))
broken_found = False
for fpath in all_html:
    content = fpath.read_text()
    for slug in deleted_slugs:
        if f'/{slug}.html' in content or f'programs/{slug}.html' in content:
            issues.append(f"  FAIL: {fpath.name} links to deleted {slug}.html")
            print(f"  FAIL: {fpath.name} links to deleted {slug}.html")
            broken_found = True
if not broken_found:
    passes.append("  PASS: No broken links to deleted programs found")
    print("  PASS: No broken links to deleted programs found")

# 6. Check timetable links point to /timetable.html in program pages
print("\n[6] CHECKING TIMETABLE LINKS IN PROGRAM PAGES")
timetable_issues = []
for fpath in (BASE / 'programs').glob('*-foundations.html'):
    content = fpath.read_text()
    # Check for View Timetable buttons
    if 'timetable' in content.lower():
        bad_timetable = re.findall(r'href="([^"]*timetable[^"]*)"', content)
        for url in bad_timetable:
            if url not in ['/timetable.html', '../timetable.html', 'https://app.classmanager.com/classes/undrgrnd-movement']:
                timetable_issues.append(f"  WARN: {fpath.name} has unusual timetable link: {url}")
if timetable_issues:
    for issue in timetable_issues:
        print(issue)
else:
    passes.append("  PASS: All timetable links look correct")
    print("  PASS: All timetable links look correct")

# 7. Check site-config.json is valid and has correct programs
print("\n[7] CHECKING SITE-CONFIG.JSON")
import json
config_path = BASE / 'site-config.json'
try:
    with open(config_path) as f:
        config = json.load(f)
    passes.append("  PASS: site-config.json is valid JSON")
    print("  PASS: site-config.json is valid JSON")
    
    # Count adult programs
    adult_programs = []
    for category, programs in config.get('programs', {}).get('adults', {}).items():
        if isinstance(programs, list):
            adult_programs.extend(programs)
    
    # Check deleted programs are gone
    deleted_ids = ['afro-groove', 'traditional-yoga', 'flow-yoga']
    for prog in adult_programs:
        if prog.get('id') in deleted_ids:
            issues.append(f"  FAIL: {prog['id']} still in site-config.json")
    
    # Check stretch-mobility exists
    sm_exists = any(p.get('id') == 'stretch-mobility' for p in adult_programs)
    if sm_exists:
        passes.append("  PASS: stretch-mobility in site-config.json")
        print("  PASS: stretch-mobility in site-config.json")
    else:
        issues.append("  FAIL: stretch-mobility missing from site-config.json")
        print("  FAIL: stretch-mobility missing from site-config.json")
    
    # Check aerial-yoga is coming_soon
    aerial = next((p for p in adult_programs if p.get('id') == 'aerial-yoga'), None)
    if aerial:
        if aerial.get('status') == 'coming_soon':
            passes.append("  PASS: aerial-yoga status is coming_soon")
            print("  PASS: aerial-yoga status is coming_soon")
        else:
            issues.append(f"  FAIL: aerial-yoga status is '{aerial.get('status')}' not coming_soon")
    
    print(f"\n  INFO: Total adult programs in config: {len(adult_programs)}")
    for p in adult_programs:
        status = p.get('status', 'active')
        print(f"    - {p.get('id')} [{status}]")

except json.JSONDecodeError as e:
    issues.append(f"  FAIL: site-config.json is invalid JSON: {e}")
    print(f"  FAIL: site-config.json is invalid JSON: {e}")

# 8. Check index.html has no Afro Groove in featured programs
print("\n[8] CHECKING INDEX.HTML FEATURED PROGRAMS")
index_content = (BASE / 'index.html').read_text()
if 'afro-groove' not in index_content and 'Afro Groove' not in index_content:
    passes.append("  PASS: index.html has no Afro Groove reference")
    print("  PASS: index.html has no Afro Groove reference")
else:
    issues.append("  FAIL: index.html still references Afro Groove")
    print("  FAIL: index.html still references Afro Groove")

if 'movement-flow-foundations.html' in index_content:
    passes.append("  PASS: index.html features Movement Flow - Foundations")
    print("  PASS: index.html features Movement Flow - Foundations")
else:
    issues.append("  FAIL: index.html missing Movement Flow - Foundations card")

# SUMMARY
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"  PASSED: {len(passes)}")
print(f"  ISSUES: {len(issues)}")
if issues:
    print("\nISSUES TO FIX:")
    for issue in issues:
        print(issue)
else:
    print("\nALL CHECKS PASSED — Site is ready to deploy!")
