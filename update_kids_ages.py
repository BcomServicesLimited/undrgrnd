"""
Update all kids class age references to 6–8 years old across the entire site.
Replaces all variants of age ranges found in the audit.
"""
import os, re

# All files to update
files_to_update = [
    'kids.html',
    'timetable.html',
    'programs/kids-creative-dance.html',
    'programs/kids-dance-moves.html',
    'programs/kids-modern-contemporary.html',
    'programs/kids-yoga.html',
    'programs/kids-aerial-silks.html',
    'programs/kids-aerial-yoga.html',
    'programs/kids-pole-foundations.html',
]

# Replacement pairs: (old_text, new_text)
# Order matters — more specific first
REPLACEMENTS = [
    # Numeric ranges with various formats
    ('4–10',        '6–8'),
    ('4-10',        '6-8'),
    ('6–16',        '6–8'),
    ('6-16',        '6-8'),
    ('8–16',        '6–8'),
    ('8-16',        '6-8'),
    ('4 to 10',     '6 to 8'),
    ('6 to 16',     '6 to 8'),
    ('8 to 16',     '6 to 8'),
    # HTML entity variants
    ('4&ndash;10',  '6&ndash;8'),
    ('6&ndash;16',  '6&ndash;8'),
    ('8&ndash;16',  '6&ndash;8'),
    # "aged X" patterns
    ('aged 4 to 10',  'aged 6 to 8'),
    ('aged 6 to 16',  'aged 6 to 8'),
    ('aged 8 to 16',  'aged 6 to 8'),
    ('aged 4-10',     'aged 6-8'),
    ('aged 6-16',     'aged 6-8'),
    ('aged 8-16',     'aged 6-8'),
    ('aged 6 and above', 'aged 6 to 8'),
    # Title/meta patterns
    ('Ages 4-10',   'Ages 6-8'),
    ('Ages 6-16',   'Ages 6-8'),
    ('Ages 8-16',   'Ages 6-8'),
    ('Ages 4–10',   'Ages 6–8'),
    ('Ages 6–16',   'Ages 6–8'),
    ('Ages 8–16',   'Ages 6–8'),
    # "minimum age of 8"
    ('minimum age of 8', 'minimum age of 6'),
    # Timetable calendar note (already correct but ensure consistency)
    ('"Ages 6 – 8"', '"Ages 6 – 8"'),  # no-op, already correct
]

total_changes = 0

for filepath in files_to_update:
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filepath}")
        continue

    original = open(filepath, encoding='utf-8').read()
    updated = original

    file_changes = 0
    for old, new in REPLACEMENTS:
        if old == new:
            continue
        count = updated.count(old)
        if count > 0:
            updated = updated.replace(old, new)
            file_changes += count
            print(f"  [{filepath}] '{old}' → '{new}' ({count}x)")

    if file_changes > 0:
        open(filepath, 'w', encoding='utf-8').write(updated)
        print(f"  SAVED {filepath} ({file_changes} changes)")
        total_changes += file_changes
    else:
        print(f"  NO CHANGES: {filepath}")

print(f"\nTotal replacements made: {total_changes}")
