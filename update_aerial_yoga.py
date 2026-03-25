#!/usr/bin/env python3
"""
Update aerial-yoga-foundations.html:
1. Add "Coming Soon" badge next to existing badge
2. Change all "Book Now" / "Book This Class" / "Book Drop-In" / "Get Class Pack" / "Go Unlimited" buttons to "Join Waitlist"
3. Change all booking URLs to mailto:undrgrndgc@gmail.com?subject=Waitlist: Aerial Yoga
4. Update sticky book now button
5. Update program-cta section
"""

FILEPATH = '/home/ubuntu/undrgrnd/programs/aerial-yoga-foundations.html'
WAITLIST_URL = 'mailto:undrgrndgc@gmail.com?subject=Waitlist: Aerial Yoga'

with open(FILEPATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the hero badge to include "Coming Soon"
content = content.replace(
    '<div class="program-hero__badge">Balanced &nbsp;·&nbsp; Beginner Friendly</div>',
    '<div class="program-hero__badge">Balanced &nbsp;·&nbsp; Beginner Friendly</div>\n      <div class="program-hero__badge" style="background:rgba(236,72,153,.15);border-color:rgba(236,72,153,.4);color:#EC4899;">Coming Soon</div>'
)

# 2. Change hero CTA "Book This Class" button to "Join Waitlist"
content = content.replace(
    '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="cta-button">Book This Class</a>',
    '<a href="' + WAITLIST_URL + '" class="cta-button">Join Waitlist</a>'
)

# 3. Change quick-info "Book Now" button to "Join Waitlist"
content = content.replace(
    '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="cta-button" style="width:100%;text-align:center;display:block;">Book Now</a>',
    '<a href="' + WAITLIST_URL + '" class="cta-button" style="width:100%;text-align:center;display:block;">Join Waitlist</a>'
)

# 4. Change pricing card buttons to "Join Waitlist"
content = content.replace(
    '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="cta-secondary" style="display:block;text-align:center;">Book Drop-In</a>',
    '<a href="' + WAITLIST_URL + '" class="cta-secondary" style="display:block;text-align:center;">Join Waitlist</a>'
)
content = content.replace(
    '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="cta-button" style="display:block;text-align:center;">Get Class Pack</a>',
    '<a href="' + WAITLIST_URL + '" class="cta-button" style="display:block;text-align:center;">Join Waitlist</a>'
)
content = content.replace(
    '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="cta-secondary" style="display:block;text-align:center;">Go Unlimited</a>',
    '<a href="' + WAITLIST_URL + '" class="cta-secondary" style="display:block;text-align:center;">Join Waitlist</a>'
)

# 5. Update the program-cta section
content = content.replace(
    '<section class="program-cta" aria-label="Book Aerial Yoga - Foundations">',
    '<section class="program-cta" aria-label="Aerial Yoga - Foundations Coming Soon">'
)
content = content.replace(
    '<a href="https://app.classmanager.com/classes/undrgrnd-movement" class="cta-button">Book Your First Class</a>',
    '<a href="' + WAITLIST_URL + '" class="cta-button">Join the Waitlist</a>'
)

# 6. Update sticky book now button
content = content.replace(
    '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="cta-button">Book Aerial Yoga - Foundations</a>',
    '<a href="' + WAITLIST_URL + '" class="cta-button">Join Aerial Yoga Waitlist</a>'
)

# 7. Catch any remaining register URLs in this file
content = content.replace(
    'https://app.classmanager.com/portal/undrgrnd-movement/register',
    WAITLIST_URL
)

with open(FILEPATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("aerial-yoga-foundations.html updated successfully")

# Verify
import subprocess
result = subprocess.run(['grep', '-c', 'Join Waitlist', FILEPATH], capture_output=True, text=True)
print(f"'Join Waitlist' occurrences: {result.stdout.strip()}")
result2 = subprocess.run(['grep', '-c', 'Coming Soon', FILEPATH], capture_output=True, text=True)
print(f"'Coming Soon' occurrences: {result2.stdout.strip()}")
result3 = subprocess.run(['grep', '-c', 'register', FILEPATH], capture_output=True, text=True)
print(f"Remaining 'register' URLs: {result3.stdout.strip()}")
