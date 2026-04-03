"""
Update all program pages to new flat $35/class term-commitment pricing model.
- Replace all info-box pricing blocks with new single $35 per class row
- Remove 10-class pack and unlimited monthly rows
- Remove "Prices are estimates" note
- Update body text mentions of old pricing
- Update index.html program card prices
"""
import re, os

BASE = '/home/ubuntu/undrgrnd'

# ─────────────────────────────────────────────────────────────────────────────
# NEW PRICING BLOCK — replaces whatever is between the divider and the CTA
# ─────────────────────────────────────────────────────────────────────────────
NEW_PRICING_BLOCK = '''      <p class="info-box__pricing-title">Pricing</p>
      <div id="infoBoxPricing">
        <div class="info-box__price-row">
          <span class="info-box__price-label">Per Class</span>
          <span class="info-box__price-amount">$35</span>
        </div>
      </div>
      <p class="info-box__note">Term commitment required. Payment of $35 is automatically deducted the day before each class. Join any time — pay weekly for the remainder of the term. No refunds for missed classes.</p>'''

# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM PAGES — list of (file, old_pricing_block, has_estimate_note)
# We'll use a regex approach to replace the pricing div block generically
# ─────────────────────────────────────────────────────────────────────────────

def update_program_page(filepath):
    content = open(filepath).read()
    original = content

    # 1. Replace the entire pricing div block (from pricing-title to end of div + optional note)
    #    Pattern: <p class="info-box__pricing-title">Pricing</p>\n      <div...>...</div>\n      <p class="info-box__note">...</p>
    #    OR without the note
    pattern = (
        r'<p class="info-box__pricing-title">Pricing</p>\s*'
        r'<div[^>]*>.*?</div>\s*'
        r'(?:<p class="info-box__note">.*?</p>\s*)?'
    )
    new_content = re.sub(pattern, NEW_PRICING_BLOCK + '\n', content, flags=re.DOTALL)

    if new_content == content:
        print(f"  WARNING: pricing block not found in {filepath}")
    else:
        content = new_content

    # 2. Fix body text price mentions
    # Old per-session prices
    content = re.sub(r'\$29 per (class|session)', '$35 per class', content)
    content = re.sub(r'\$32 per (class|session)', '$35 per class', content)
    content = re.sub(r'\$28 per (class|session)', '$35 per class', content)
    content = re.sub(r'\$30 per (class|session)', '$35 per class', content)

    # Remove 10-class pack / unlimited monthly body text sentences
    content = re.sub(
        r',?\s*(?:with\s+)?(?:a\s+)?10[- ]class packs?\s+(?:available\s+)?(?:for\s+)?\$\d+[^.]*\.?',
        '', content, flags=re.IGNORECASE
    )
    content = re.sub(
        r',?\s*(?:and\s+)?unlimited monthly memberships?\s+\(\$\d+[^)]*\)[^.]*\.?',
        '', content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'We offer flexible booking options including drop-in classes \(\$\d+ per session\)[^<]*\.',
        'Classes are $35 per session. Term commitment is required — students commit to the full Queensland school term, with $35 automatically deducted the day before each class.',
        content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'Drop-in classes are \$\d+[^<]*\.',
        'Classes are $35 per session, with term commitment required.',
        content, flags=re.IGNORECASE
    )
    # Generic "are $XX per session" fixes
    content = re.sub(r'are \$(?:29|32|28|30) per session', 'are $35 per session', content)
    content = re.sub(r'are \$(?:29|32|28|30) per class', 'are $35 per class', content)

    if content != original:
        open(filepath, 'w').write(content)
        print(f"  UPDATED: {filepath}")
    else:
        print(f"  NO CHANGE: {filepath}")

# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM PAGES TO UPDATE
# ─────────────────────────────────────────────────────────────────────────────
program_pages = [
    'programs/booty-burn-foundations.html',
    'programs/movement-flow-foundations.html',
    'programs/fusion-yoga-foundations.html',
    'programs/choreography-fusion-foundations.html',
    'programs/aerial-silks-foundations.html',
    'programs/stretch-mobility-foundations.html',
    'programs/pole-fitness-foundations.html',
    'programs/pole-flow-foundations.html',
    'programs/pole-strength-movement.html',
    'programs/aerial-yoga-foundations.html',
    'programs/recovery-movement-flow-foundations.html',
    'programs/kids-creative-dance.html',
    'programs/kids-dance-moves.html',
    'programs/kids-modern-contemporary.html',
    'programs/kids-yoga.html',
    'programs/kids-aerial-silks.html',
    'programs/kids-aerial-yoga.html',
    'programs/kids-pole-foundations.html',
]

print("=== Updating program pages ===")
for page in program_pages:
    update_program_page(os.path.join(BASE, page))

# ─────────────────────────────────────────────────────────────────────────────
# INDEX.HTML — update program card prices
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Updating index.html ===")
idx_path = os.path.join(BASE, 'index.html')
content = open(idx_path).read()
original = content

# Replace all program-card__price values
content = re.sub(
    r'(<p class="program-card__price"><strong>)\$(?:29|32|35|28|30)(</strong> per class</p>)',
    r'\g<1>$35\g<2>',
    content
)

if content != original:
    open(idx_path, 'w').write(content)
    print("  UPDATED: index.html")
else:
    print("  NO CHANGE: index.html")

# ─────────────────────────────────────────────────────────────────────────────
# TIMETABLE.HTML — update any per-class pricing mentions
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Updating timetable.html ===")
tt_path = os.path.join(BASE, 'timetable.html')
content = open(tt_path).read()
original = content
content = re.sub(r'\$(?:29|32|28|30) per (class|session)', '$35 per class', content)
if content != original:
    open(tt_path, 'w').write(content)
    print("  UPDATED: timetable.html")
else:
    print("  NO CHANGE: timetable.html")

print("\nDone.")
