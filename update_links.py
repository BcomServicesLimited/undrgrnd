#!/usr/bin/env python3
"""Update all internal links from old program slugs to new ones"""
import os
import re

BASE = '/home/ubuntu/undrgrnd'

# Mapping: old slug → new slug
RENAMES = {
    'movement-dance': 'movement-flow-foundations',
    'recovery-movement': 'recovery-movement-flow-foundations',
    'pole-flow': 'pole-flow-foundations',
    'yoga-fusion': 'fusion-yoga-foundations',
    'traditional-yoga': 'traditional-yoga-foundations',
    'modern-yoga': 'flow-yoga-foundations',
    'aerial-yoga': 'aerial-yoga-foundations',
    'aerial-silks': 'aerial-silks-foundations',
    'choreography-fusion': 'choreography-fusion-foundations',
}

# Files to update (excluding the new files themselves)
FILES_TO_UPDATE = [
    'index.html',
    'programs/aerial-silks.html',
    'programs/aerial-yoga.html',
    'programs/afro-groove-foundations.html',
    'programs/booty-burn-foundations.html',
    'programs/choreography-fusion.html',
    'programs/kids-aerial-silks.html',
    'programs/kids-aerial-yoga.html',
    'programs/kids-modern-contemporary.html',
    'programs/kids-pole-foundations.html',
    'programs/kids-yoga.html',
    'programs/modern-yoga.html',
    'programs/movement-dance.html',
    'programs/pole-fitness-foundations.html',
    'programs/pole-flow.html',
    'programs/pole-strength-movement.html',
    'programs/recovery-movement.html',
    'programs/traditional-yoga.html',
    'programs/yoga-fusion.html',
]

def update_file(filepath):
    full_path = os.path.join(BASE, filepath)
    if not os.path.exists(full_path):
        print(f'  SKIP (not found): {filepath}')
        return 0
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = 0
    
    for old_slug, new_slug in RENAMES.items():
        # Replace in href="/programs/old-slug.html"
        pattern = f'/programs/{old_slug}.html'
        replacement = f'/programs/{new_slug}.html'
        if pattern in content:
            count = content.count(pattern)
            content = content.replace(pattern, replacement)
            changes += count
            print(f'    {old_slug} → {new_slug}: {count} replacement(s)')
    
    if changes > 0:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Updated: {filepath} ({changes} total changes)')
    else:
        print(f'  No changes: {filepath}')
    
    return changes

print('=== Updating internal links ===\n')
total = 0
for f in FILES_TO_UPDATE:
    total += update_file(f)

print(f'\n=== Done. Total replacements: {total} ===')
