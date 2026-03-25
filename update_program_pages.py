#!/usr/bin/env python3
"""
Step 4: Update existing program pages with new descriptions and booking URLs.
"""
import re
import os

PROGRAMS_DIR = '/home/ubuntu/undrgrnd/programs'

# New descriptions and booking URLs for each program
UPDATES = {
    'booty-burn-foundations.html': {
        'description': "Feel the beat, step into the movement, and get ready to work. Booty Burn – Foundations is a beginner-friendly class built around rhythm, energy, and a deep, steady burn that builds as you move. This class focuses on the glutes, hips, and core using simple, repeatable patterns that are easy to follow from your first session. You'll work through follow-along drills with a strong focus on pelvic and hip movement, combined with layered leg patterns that keep the lower body constantly engaged. The sequences are simple to learn but designed to be held, repeated, and felt. With a strong focus on pelvic and hip movement, you'll not only feel the burn through the glutes, but also build deeper core strength and support how your body moves day to day. Ideal for those who want to activate, shape, and feel their glutes working.",
        'booking_url': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/booty-burn-foundations',
        'class_name': 'Booty Burn – Foundations',
    },
    'movement-flow-foundations.html': {
        'description': "Move, explore, and reconnect with your body through natural, flowing movement. Movement Flow - Foundations is a beginner-friendly class built around simple sequences that help you move better, feel more confident, and develop your own way of moving. Rather than following a fixed dance style, this class blends different movement approaches into smooth, continuous patterns that feel natural and intuitive. You'll move through guided sequences that improve coordination, mobility, and overall body control without pressure to get everything perfect. With an emphasis on smooth transitions, posture, and ease of movement, you'll build strength, flexibility, and awareness through each curated, smooth, authentic, and holistic movement. Suitable for both men and women, this class offers a structured yet relaxed space to move freely, build confidence, and enjoy the process from the first session.",
        'booking_url': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/movement-flow-foundations',
        'class_name': 'Movement Flow – Foundations',
    },
    'choreography-fusion-foundations.html': {
        'description': "Step in, learn the sequence, and make it your own. Choreography Fusion – Foundations is a beginner-friendly class focused on building confidence through simple, guided choreography that's easy to follow from the first session. 'Fusion' means you're not locked into one style. Each class blends elements from different movement styles — such as groove, flow, and basic contemporary — giving you variety while helping you understand how movement connects across styles. You'll learn short combinations step by step, with clear breakdowns that help you understand timing, transitions, and how sequences are built — not just copy them. The focus is on coordination, timing, and moving through a full sequence with clarity and control, without pressure to perform or get everything perfect. Ideal for adults who want to build confidence, improve coordination, and learn choreography in a structured but flexible way.",
        'booking_url': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/choreography-fusion-foundations',
        'class_name': 'Choreography Fusion – Foundations',
    },
    'fusion-yoga-foundations.html': {
        'description': "A balanced approach to yoga that brings together structure and flow. Fusion Yoga – Foundations is a beginner-friendly class that combines traditional yoga principles with modern, movement-based flow to create a practice that feels both grounded and dynamic. 'Fusion' means you'll experience both sides — the stability of classic postures and the fluidity of continuous movement. Some parts of the class focus on alignment, breath, and controlled holds, while others guide you through smooth transitions that build strength, mobility, and coordination. This combination allows you to develop a deeper understanding of your body while keeping the practice engaging and accessible from the first session. Suitable for beginners with no prior experience, this class offers a structured yet flexible environment to build strength, improve mobility, and move with more awareness and control.",
        'booking_url': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/fusion-yoga-foundations',
        'class_name': 'Fusion Yoga – Foundations',
    },
    'aerial-silks-foundations.html': {
        'description': "Aerial Silks – Foundations introduces you to aerial movement using suspended fabric in a safe and structured environment. This class is built around the fundamentals of aerial acrobatics, where you learn how to climb, wrap, and hold positions on the silks while developing strength, coordination, and body control. Each session guides you through simple, foundational techniques such as basic grips, supported holds, and low-level wraps that form the base of aerial tricks and sequences. With a strong emphasis on technique, posture, and control, you'll build upper body strength, core stability, and confidence while learning how to move safely off the ground. Through each curated, smooth, and authentic movement, you'll begin to understand how aerial skills are constructed, giving you a clear pathway into more advanced tricks and combinations over time. This class is ideal for beginners with no prior experience who want to explore aerial acrobatics in a supportive, structured, and safety-focused environment.",
        'booking_url': 'https://app.classmanager.com/portal/undrgrnd-movement/enrolment/classes/aerial-silks-foundations',
        'class_name': 'Aerial Silks – Foundations',
    },
}

def update_program_description(filepath, new_description, booking_url, class_name):
    """Update the program overview description paragraphs in a program page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Update the program overview description section
    # Find the program-overview__desc div and replace its paragraphs
    # Pattern: find the <div class="program-overview__desc reveal"> section
    desc_pattern = r'(<div class="program-overview__desc reveal">.*?<h2>About [^<]+</h2>)(.*?)(</div>\s*<div class="quick-info reveal">)'
    
    def replace_desc(m):
        # Split description into two paragraphs at a natural break
        desc = new_description
        # Find a good split point (after a sentence that ends a thought)
        sentences = desc.split('. ')
        mid = len(sentences) // 2
        para1 = '. '.join(sentences[:mid]) + '.'
        para2 = '. '.join(sentences[mid:])
        if not para2.endswith('.'):
            para2 += '.'
        return m.group(1) + f'\n      <p>{para1}</p>\n      <p>{para2}</p>\n    ' + m.group(3)
    
    new_content = re.sub(desc_pattern, replace_desc, content, flags=re.DOTALL)
    
    # 2. Update all booking URLs (enrolment-specific ones)
    # Replace old register URL with new enrolment URL
    old_register = 'https://app.classmanager.com/portal/undrgrnd-movement/register'
    new_content = new_content.replace(old_register, booking_url)
    
    # Also replace any existing enrolment URLs for this class that might be wrong
    # (in case the page already has a different enrolment URL)
    enrolment_pattern = r'https://app\.classmanager\.com/portal/undrgrnd-movement/enrolment/classes/[a-z0-9-]+'
    new_content = re.sub(enrolment_pattern, booking_url, new_content)
    
    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Process each program page
results = []
for filename, data in UPDATES.items():
    filepath = os.path.join(PROGRAMS_DIR, filename)
    if os.path.exists(filepath):
        changed = update_program_description(
            filepath,
            data['description'],
            data['booking_url'],
            data['class_name']
        )
        results.append((filename, 'UPDATED' if changed else 'NO CHANGE'))
    else:
        results.append((filename, 'FILE NOT FOUND'))

for filename, status in results:
    print(f"{status}: {filename}")

print("\nDone!")
