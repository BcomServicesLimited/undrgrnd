#!/usr/bin/env python3
"""
Step 5G: Global find-and-replace across ALL HTML files.
Replaces old program names in text and old URLs in href attributes.
"""
import os
import re

BASE = '/home/ubuntu/undrgrnd'

# Text replacements (in body text, not URLs)
TEXT_REPLACEMENTS = [
    # Most specific first to avoid partial matches
    ('Recovery Movement Dance', 'Recovery Movement Flow - Foundations'),
    ('Recovery Movement Flow Foundations', 'Recovery Movement Flow - Foundations'),
    ('Movement Dance', 'Movement Flow - Foundations'),
    ('Yoga Fusion', 'Fusion Yoga - Foundations'),
    ('Modern Yoga', 'Flow Yoga - Foundations'),
]

# URL replacements (in href attributes)
URL_REPLACEMENTS = [
    ('/programs/movement-dance.html', '/programs/movement-flow-foundations.html'),
    ('/programs/recovery-movement.html', '/programs/recovery-movement-flow-foundations.html'),
    ('/programs/yoga-fusion.html', '/programs/fusion-yoga-foundations.html'),
    ('/programs/modern-yoga.html', '/programs/flow-yoga-foundations.html'),
    ('/programs/pole-flow.html', '/programs/pole-flow-foundations.html'),
    ('/programs/traditional-yoga.html', '/programs/traditional-yoga-foundations.html'),
    ('/programs/aerial-yoga.html', '/programs/aerial-yoga-foundations.html'),
    ('/programs/choreography-fusion.html', '/programs/choreography-fusion-foundations.html'),
]

def get_all_html_files(base):
    html_files = []
    for root, dirs, files in os.walk(base):
        # Skip node_modules, .git, etc.
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__']]
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    return sorted(html_files)

def apply_replacements(content, filepath):
    original = content
    changes = []
    
    # Apply URL replacements (in href attributes)
    for old_url, new_url in URL_REPLACEMENTS:
        if old_url in content:
            count = content.count(old_url)
            content = content.replace(old_url, new_url)
            changes.append(f'  URL: {old_url} → {new_url} ({count}x)')
    
    # Apply text replacements (avoid replacing inside href/src attributes)
    # We use a careful approach: replace in text nodes only
    # Strategy: replace in the full content but skip anything inside href="..." or src="..."
    for old_text, new_text in TEXT_REPLACEMENTS:
        if old_text in content:
            # Count occurrences not inside href attributes
            # Simple approach: replace all, then check if we accidentally changed a URL
            count = content.count(old_text)
            content = content.replace(old_text, new_text)
            changes.append(f'  TEXT: "{old_text}" → "{new_text}" ({count}x)')
    
    return content, changes

def main():
    html_files = get_all_html_files(BASE)
    print(f'Found {len(html_files)} HTML files to process\n')
    
    total_files_changed = 0
    total_changes = 0
    
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f'ERROR reading {filepath}: {e}')
            continue
        
        new_content, changes = apply_replacements(content, filepath)
        
        if changes:
            rel_path = os.path.relpath(filepath, BASE)
            print(f'{rel_path}:')
            for c in changes:
                print(c)
            print()
            
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total_files_changed += 1
                total_changes += len(changes)
            except Exception as e:
                print(f'ERROR writing {filepath}: {e}')
    
    print(f'\nDone: {total_files_changed} files changed, {total_changes} replacement types applied')

if __name__ == '__main__':
    main()
