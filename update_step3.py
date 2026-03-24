#!/usr/bin/env python3
"""
UNDRGRND Movement — Step 3: Update existing program pages
Processes all 10 program files: renames + updates content
"""
import re
import shutil
import os

BASE = '/home/ubuntu/undrgrnd/programs'
BOOKING_URL = 'https://undrgrnd-movement.classmanager.com/register'
OLD_BOOKING_URL = 'https://app.classmanager.com/portal/undrgrnd-movement/register'

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Written: {os.path.basename(path)}')

def fix_booking_urls(html):
    """Replace all old booking URLs with new one"""
    return html.replace(OLD_BOOKING_URL, BOOKING_URL)

def update_head(html, title, meta_desc, canonical_url, og_title, og_desc, og_url):
    """Update <title>, meta description, canonical, and OG tags"""
    html = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{meta_desc}"', html)
    html = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="{canonical_url}"', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="{og_url}"', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{og_title}"', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{og_desc}"', html)
    return html

def make_coming_soon_badge():
    return '<span class="program-hero__badge program-hero__badge--coming-soon" style="background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.4);color:#F59E0B;">Coming Soon</span>'

def make_waitlist_buttons():
    return f'''<a href="mailto:undrgrndgc@gmail.com?subject=Waitlist%20Request" class="cta-button">Join Waitlist</a>
        <a href="/timetable.html" class="cta-secondary">View Timetable</a>'''

# ─────────────────────────────────────────────────────────────────────────────
# TASK 3A: movement-dance.html → movement-flow-foundations.html
# ─────────────────────────────────────────────────────────────────────────────
def task_3a():
    print('\n[3A] Movement Dance → Movement Flow - Foundations')
    src = f'{BASE}/movement-dance.html'
    dst = f'{BASE}/movement-flow-foundations.html'
    html = read(src)

    # Head
    html = update_head(html,
        title='Movement Flow - Foundations | Movement Classes Gold Coast | UNDRGRND Movement Southport',
        meta_desc='Move better and feel confident with natural movement principles at UNDRGRND Movement Southport. Movement Flow builds coordination and body awareness. Beginner-friendly classes on the Gold Coast.',
        canonical_url='https://www.undrgrnd.com.au/programs/movement-flow-foundations.html',
        og_title='Movement Flow - Foundations | Movement Classes Gold Coast | UNDRGRND Movement',
        og_desc='Move better and feel confident with natural movement principles at UNDRGRND Movement Southport. Beginner-friendly movement classes on the Gold Coast.',
        og_url='https://www.undrgrnd.com.au/programs/movement-flow-foundations.html'
    )

    # Hero section aria-label
    html = html.replace('aria-label="Movement Dance Hero"', 'aria-label="Movement Flow - Foundations Hero"')

    # Badge
    html = html.replace(
        '<div class="program-hero__badge">\n        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>\n        Dance &nbsp;·&nbsp; Beginner / Foundation\n      </div>',
        '<div class="program-hero__badge">\n        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>\n        Balanced / Flow &nbsp;·&nbsp; Beginner Friendly\n      </div>'
    )

    # H1
    html = html.replace(
        '<h1 class="program-hero__h1">Movement Dance<br><span>Dance Classes Gold Coast</span></h1>',
        '<h1 class="program-hero__h1">Movement Flow - Foundations<br><span>Movement Classes Gold Coast</span></h1>'
    )

    # Hero sub
    html = html.replace(
        '<p class="program-hero__sub">Build body flow and confidence through expressive movement. A beginner-friendly dance fitness class at UNDRGRND Movement Southport that welcomes everyone — no experience required.</p>',
        '<p class="program-hero__sub">Reconnect with your body through fluid, natural movement in a calm and supportive environment. A beginner-friendly movement class at UNDRGRND Movement Southport — no experience required.</p>'
    )

    # Hero images
    html = html.replace('../images/hero/movement-dance-mobile.webp', '../images/hero/movement-flow-foundations-mobile.webp')
    html = html.replace('../images/hero/movement-dance.webp', '../images/hero/movement-flow-foundations.webp')
    html = html.replace('alt="Movement Dance class at UNDRGRND Movement, Southport Gold Coast"', 'alt="Movement Flow - Foundations class at UNDRGRND Movement, Southport Gold Coast"')

    # Program overview H2 and description
    html = html.replace('<h2>About Movement Dance</h2>', '<h2>About Movement Flow - Foundations</h2>')
    # Replace overview description paragraphs
    old_overview = '''<p>Build body flow and confidence through expressive, natural movement. A beginner-friendly class at UNDRGRND Movement Southport that welcomes everyone — no experience required.</p>
      <p>At UNDRGRND Movement Southport, our Movement Dance classes blend elements of contemporary dance, somatic movement, and creative expression. Each class is different, ensuring that regular attendees continue to be challenged and inspired while newcomers always feel welcome.</p>'''
    new_overview = '''<p>Movement Flow – Foundations is a beginner-friendly class designed to help you reconnect with your body through fluid, natural movement in a calm and supportive environment. The focus is on developing body awareness, improving mobility, and building confidence through simple, guided movement sequences that feel natural and accessible.</p>
      <p>Each session introduces easy-to-follow patterns that encourage smooth transitions, gentle strength work, and a greater sense of ease in how you move. Through each curated, smooth, and authentic movement, you will develop coordination, flexibility, and a deeper connection to your body. This class is ideal for beginners or anyone returning to movement who wants to build confidence and body awareness in a gentle and structured way.</p>'''
    html = html.replace(old_overview, new_overview)

    # Core focus section subtitle
    html = html.replace(
        '<p>What you will develop in every Movement Dance class at UNDRGRND Movement Southport</p>',
        '<p>What you will develop in every Movement Flow class at UNDRGRND Movement Southport</p>'
    )

    # Core focus cards
    old_core = '''      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 6v6l4 2"/></svg></div>
        <h3>Body Flow &amp; Natural Movement</h3>
        <p>Learn to move with ease and fluidity, connecting breath with movement for a natural, flowing experience.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
        <h3>Confidence Through Expression</h3>
        <p>Build self-confidence by expressing yourself freely through movement in a safe, encouraging environment.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg></div>
        <h3>Creative Movement Exploration</h3>
        <p>Discover your unique movement style through guided creative exploration and improvisation exercises.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
        <h3>Community &amp; Connection</h3>
        <p>Move alongside others in a welcoming Gold Coast community that celebrates every body and every level.</p>
      </div>'''
    new_core = '''      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 6v6l4 2"/></svg></div>
        <h3>Fluid, Natural Movement Patterns</h3>
        <p>Develop ease and fluidity in how you move through guided sequences that feel natural and accessible.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
        <h3>Body Awareness and Mobility</h3>
        <p>Build a deeper connection to your body and improve mobility through mindful, structured movement.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg></div>
        <h3>Smooth Transitions and Coordination</h3>
        <p>Learn to link movements together with control and grace, developing timing and coordination over time.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
        <h3>Confidence Through Gentle Movement</h3>
        <p>Build self-confidence and body awareness in a calm, supportive environment at our Southport studio.</p>
      </div>'''
    html = html.replace(old_core, new_core)

    # Who it's for H2
    html = html.replace('<h2>Who Is Movement Dance For?</h2>', '<h2>Who Is Movement Flow - Foundations For?</h2>')

    # What to expect subtitle
    html = html.replace(
        '<p>A typical Movement Dance session at UNDRGRND Movement Southport</p>',
        '<p>A typical Movement Flow - Foundations session at UNDRGRND Movement Southport</p>'
    )

    # Related programs
    old_related = '''      <a href="/programs/afro-groove-foundations.html" class="related-card reveal">
        <div class="related-card__badge">Dance</div>
        <div class="related-card__name">Afro Groove Foundations</div>
        <div class="related-card__desc">Beginner-friendly dance fitness inspired by Afrobeat and groove-based styles.</div>
      </a>
      <a href="/programs/choreography-fusion.html" class="related-card reveal">
        <div class="related-card__badge">Choreography</div>
        <div class="related-card__name">Choreography Fusion</div>
        <div class="related-card__desc">Women's movement and confidence through choreographed dance sequences.</div>
      </a>
      <a href="/programs/yoga-fusion.html" class="related-card reveal">
        <div class="related-card__badge">Yoga</div>
        <div class="related-card__name">Yoga Fusion</div>
        <div class="related-card__desc">Modern fusion of traditional yoga with contemporary movement on the Gold Coast.</div>
      </a>'''
    new_related = '''      <a href="/programs/afro-groove-foundations.html" class="related-card reveal">
        <div class="related-card__badge">Dance</div>
        <div class="related-card__name">Afro Groove Foundations</div>
        <div class="related-card__desc">Beginner-friendly dance fitness inspired by Afrobeat and groove-based styles.</div>
      </a>
      <a href="/programs/choreography-fusion-foundations.html" class="related-card reveal">
        <div class="related-card__badge">Choreography</div>
        <div class="related-card__name">Choreography Fusion - Foundations</div>
        <div class="related-card__desc">Build confidence through simple, guided choreography sequences in a supportive environment.</div>
      </a>
      <a href="/programs/fusion-yoga-foundations.html" class="related-card reveal">
        <div class="related-card__badge">Yoga</div>
        <div class="related-card__name">Fusion Yoga - Foundations</div>
        <div class="related-card__desc">Blend traditional yoga with modern movement for mobility and strength on the Gold Coast.</div>
      </a>'''
    html = html.replace(old_related, new_related)

    # SEO content section
    old_seo_section = re.search(r'<section class="seo-content".*?</section>', html, re.DOTALL)
    if old_seo_section:
        new_seo = '''<section class="seo-content" aria-label="About Movement Flow on the Gold Coast">
  <div class="seo-content__inner">
    <h2>Movement Flow on the Gold Coast — Build Body Confidence at UNDRGRND Movement Southport</h2>
    <p>UNDRGRND Movement offers Movement Flow – Foundations classes at our Southport studio, located at 163 Ferry Rd in the heart of the Gold Coast. This beginner-friendly class is designed for anyone who wants to reconnect with their body, improve mobility, and build confidence through fluid, natural movement in a calm and supportive environment.</p>
    <h3>What Is Movement Flow - Foundations?</h3>
    <p>Movement Flow – Foundations is a structured beginner class that focuses on natural movement principles rather than performance or technique. Unlike traditional dance classes on the Gold Coast, Movement Flow encourages participants to develop body awareness, smooth transitions, and a greater sense of ease in how they move. Each session at UNDRGRND Movement Southport introduces simple, guided sequences that feel natural and accessible to all participants.</p>
    <p>At our Southport studio, Movement Flow classes blend elements of somatic movement, mobility work, and gentle conditioning. The emphasis is always on how movement feels rather than how it looks, making this class ideal for beginners, those returning to exercise, or anyone on the Gold Coast who wants to move more freely and confidently.</p>
    <h3>Why Movement Flow Is Perfect for Beginners on the Gold Coast</h3>
    <p>One of the most common barriers to starting a movement class on the Gold Coast is the fear of not knowing what to do or feeling out of place. Movement Flow – Foundations at UNDRGRND Movement Southport is specifically designed to remove those barriers. Every session is structured to be welcoming and accessible, with movements introduced gradually and at a pace that suits all fitness levels.</p>
    <p>Our Southport studio provides a calm, non-judgmental environment where Gold Coast participants of all ages and backgrounds feel comfortable exploring movement. Whether you are a complete beginner, someone returning to exercise after a break, or simply looking for a gentler approach to fitness on the Gold Coast, Movement Flow – Foundations is the right starting point.</p>
    <h3>The Benefits of Natural Movement Training</h3>
    <p>Movement Flow – Foundations at UNDRGRND Movement Southport delivers a range of physical and mental benefits through consistent practice. Regular participants on the Gold Coast report improved flexibility, better posture, increased body awareness, and a greater sense of ease in everyday movement. The gentle, low-impact nature of the class makes it suitable for a wide range of fitness levels and ages.</p>
    <p>Because Movement Flow engages the whole body through varied, natural movement patterns, it also develops functional coordination and mobility that translates into everyday life. Gold Coast participants often notice improvements in how they carry themselves, how they move through space, and how connected they feel to their bodies after just a few sessions at our Southport studio.</p>
    <h3>Movement Flow for All Ages and Fitness Levels</h3>
    <p>Movement Flow – Foundations at UNDRGRND Movement is open to all adults on the Gold Coast, regardless of age, fitness level, or prior movement experience. The class is particularly well-suited to those aged 26–45 who are looking for a structured yet gentle approach to building body confidence and coordination. Our Southport instructors adapt each session to the needs of the group, ensuring everyone feels supported and challenged at the right level.</p>
    <p>Whether you are a Gold Coast resident who has never attended a movement class before, or someone who has tried other fitness options and found them too intense or too performance-focused, Movement Flow – Foundations offers a genuinely different experience. The focus is on your personal movement journey, not on keeping up with others or achieving a specific look.</p>
    <h3>Movement Flow at UNDRGRND Movement Southport, Gold Coast</h3>
    <p>UNDRGRND Movement is located at 163 Ferry Rd, Southport QLD 4215, making it easily accessible to Gold Coast residents from Southport, Surfers Paradise, Broadbeach, Robina, and surrounding suburbs. Our Southport studio is purpose-built for movement classes, with a welcoming atmosphere that feels nothing like a traditional gym.</p>
    <p>We offer flexible booking options including drop-in classes ($25 per session), 10-class packs ($200), and unlimited monthly memberships ($180 per month). All options can be booked online through our timetable page, making it easy for Gold Coast residents to fit Movement Flow into their weekly routine.</p>
    <h3>Start Your Movement Journey on the Gold Coast</h3>
    <p>If you have been looking for a movement class on the Gold Coast that welcomes beginners, supports all bodies, and makes movement genuinely enjoyable, Movement Flow – Foundations at UNDRGRND Movement Southport is exactly what you have been searching for. Join our growing community of Gold Coast movers and discover what your body is capable of when given the freedom to explore natural movement.</p>
    <p>Book your first Movement Flow class today at UNDRGRND Movement, 163 Ferry Rd, Southport — Gold Coast's home for accessible, confidence-building movement.</p>
  </div>
</section>'''
        html = html[:old_seo_section.start()] + new_seo + html[old_seo_section.end():]

    # CTA section
    html = html.replace(
        '<section class="program-cta" aria-label="Book Movement Dance">',
        '<section class="program-cta" aria-label="Book Movement Flow - Foundations">'
    )
    html = html.replace(
        '<h2>Ready to Find Your Flow?</h2>\n  <p>Join the Movement Dance community at UNDRGRND Movement Southport. No experience needed — just show up and move.</p>',
        '<h2>Ready to Find Your Flow?</h2>\n  <p>Join Movement Flow – Foundations at UNDRGRND Movement Southport. No experience needed — just show up and move.</p>'
    )
    html = html.replace(
        '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="cta-button">Book Your First Class</a>\n    <a href="/contact.html" class="cta-secondary">Have Questions? Contact Us</a>',
        f'<a href="{BOOKING_URL}" class="cta-button">Book Your First Class</a>\n    <a href="/contact.html" class="cta-secondary">Have Questions? Contact Us</a>'
    )
    html = html.replace(
        '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="cta-button">Book Movement Dance</a>',
        f'<a href="{BOOKING_URL}" class="cta-button">Book Movement Flow</a>'
    )

    # Schema breadcrumb
    html = html.replace(
        "{ name: 'Movement Dance', url: 'https://www.undrgrnd.com.au/programs/movement-dance.html' }",
        "{ name: 'Movement Flow - Foundations', url: 'https://www.undrgrnd.com.au/programs/movement-flow-foundations.html' }"
    )

    # Fix all remaining old booking URLs
    html = fix_booking_urls(html)

    write(dst, html)
    print(f'  [OK] {dst}')


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3B: recovery-movement.html → recovery-movement-flow-foundations.html
# ─────────────────────────────────────────────────────────────────────────────
def task_3b():
    print('\n[3B] Recovery Movement → Recovery Movement Flow - Foundations')
    src = f'{BASE}/recovery-movement.html'
    dst = f'{BASE}/recovery-movement-flow-foundations.html'
    html = read(src)

    # Head
    html = update_head(html,
        title='Recovery Movement Flow - Foundations | Gentle Movement Gold Coast | UNDRGRND Movement Southport',
        meta_desc='Safe return to movement after injury at UNDRGRND Movement Southport. Recovery Movement Flow offers gentle, supportive classes on the Gold Coast. Medical clearance required.',
        canonical_url='https://www.undrgrnd.com.au/programs/recovery-movement-flow-foundations.html',
        og_title='Recovery Movement Flow - Foundations | Gentle Movement Gold Coast | UNDRGRND Movement',
        og_desc='Safe, gentle return to movement after injury or inactivity at UNDRGRND Movement Southport. Medical clearance required. Gold Coast.',
        og_url='https://www.undrgrnd.com.au/programs/recovery-movement-flow-foundations.html'
    )

    # Hero aria-label
    html = re.sub(r'aria-label="Recovery Movement[^"]*Hero"', 'aria-label="Recovery Movement Flow - Foundations Hero"', html)

    # H1
    html = re.sub(r'<h1 class="program-hero__h1">Recovery Movement[^<]*</h1>',
        '<h1 class="program-hero__h1">Recovery Movement Flow - Foundations<br><span>Gentle Movement Classes Gold Coast</span></h1>', html)

    # Hero sub
    old_sub = re.search(r'<p class="program-hero__sub">[^<]*Recovery[^<]*</p>', html)
    if old_sub:
        html = html[:old_sub.start()] + '<p class="program-hero__sub">A safe, gentle return to movement after injury, illness, or extended inactivity. Specialised low-impact classes at UNDRGRND Movement Southport — designed with your recovery in mind. Medical clearance required.</p>' + html[old_sub.end():]

    # Badge — add coming-soon
    html = re.sub(
        r'<div class="program-hero__badge[^"]*">[^<]*(?:Recovery|Gentle)[^<]*</div>',
        '<div class="program-hero__badge">Gentle / Slow &nbsp;·&nbsp; 45+ (Gentle / Recovery)</div>\n      <div class="program-hero__badge" style="background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.4);color:#F59E0B;margin-top:0.5rem;">Medical Clearance Required</div>\n      <div class="program-hero__badge" style="background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.4);color:#F59E0B;margin-top:0.5rem;">Coming Soon</div>',
        html
    )

    # Hero images
    html = html.replace('../images/hero/recovery-movement-mobile.webp', '../images/hero/recovery-movement-flow-foundations-mobile.webp')
    html = html.replace('../images/hero/recovery-movement.webp', '../images/hero/recovery-movement-flow-foundations.webp')
    html = re.sub(r'alt="Recovery Movement[^"]*"', 'alt="Recovery Movement Flow - Foundations class at UNDRGRND Movement, Southport Gold Coast"', html)

    # Book buttons → Join Waitlist / Coming Soon
    html = html.replace(
        f'<a href="{OLD_BOOKING_URL}" class="cta-button">Book This Class</a>',
        '<a href="mailto:undrgrndgc@gmail.com?subject=Recovery%20Movement%20Flow%20Waitlist" class="cta-button">Join Waitlist</a>'
    )
    html = html.replace(
        f'<a href="{OLD_BOOKING_URL}" class="cta-button">Book Now</a>',
        '<a href="mailto:undrgrndgc@gmail.com?subject=Recovery%20Movement%20Flow%20Waitlist" class="cta-button">Join Waitlist</a>'
    )
    html = html.replace(
        f'<a href="{OLD_BOOKING_URL}" class="cta-button">Book Your First Class</a>',
        '<a href="mailto:undrgrndgc@gmail.com?subject=Recovery%20Movement%20Flow%20Waitlist" class="cta-button">Join Waitlist</a>'
    )

    # Add medical clearance notice after hero section
    medical_notice = '''
<!-- Medical Clearance Notice -->
<div style="background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.4);border-radius:12px;padding:1.5rem 2rem;max-width:1400px;margin:2rem auto;font-family:\'Outfit\',sans-serif;">
  <h3 style="color:#F59E0B;font-size:1.1rem;font-weight:700;margin-bottom:0.75rem;">Medical Clearance Required</h3>
  <p style="color:#A1A1A1;line-height:1.7;margin:0;">Recovery Movement Flow requires medical clearance from your healthcare provider. This ensures your safe return to movement after injury, surgery, or extended inactivity. Please contact us at <a href="mailto:undrgrndgc@gmail.com" style="color:#8B5CF6;">undrgrndgc@gmail.com</a> to discuss clearance requirements before booking.</p>
</div>'''
    # Insert after hero section
    html = re.sub(r'(</section>\s*<!-- ═+\s*PROGRAM OVERVIEW)', medical_notice + r'\n\1', html, count=1)

    # Overview H2
    html = re.sub(r'<h2>About Recovery Movement[^<]*</h2>', '<h2>About Recovery Movement Flow - Foundations</h2>', html)

    # Overview description
    old_desc_match = re.search(r'(<div class="program-overview__desc reveal">.*?</div>)', html, re.DOTALL)
    if old_desc_match:
        new_desc = '''<div class="program-overview__desc reveal">
      <h2>About Recovery Movement Flow - Foundations</h2>
      <p>Recovery Movement Flow – Foundations is a gentle, low-impact class designed for individuals who are returning to movement after injury, illness, surgery, or an extended period of inactivity. The class focuses on rebuilding body awareness, improving mobility, and restoring confidence in movement through slow, controlled, and mindful sequences.</p>
      <p>Each session is carefully structured to support safe re-engagement with physical activity, with movements introduced gradually and adapted to individual needs. Through each curated, smooth, and authentic movement, you will rebuild strength, flexibility, and coordination at a pace that feels right for your body. Medical clearance is required before participating in this program.</p>
    </div>'''
        html = html[:old_desc_match.start()] + new_desc + html[old_desc_match.end():]

    # Core focus cards
    old_core_match = re.search(r'<div class="core-focus__grid">.*?</div>\s*</div>\s*</section>', html, re.DOTALL)
    if old_core_match:
        new_core_grid = '''<div class="core-focus__grid">
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 6v6l4 2"/></svg></div>
        <h3>Safe Return to Movement</h3>
        <p>Carefully structured sequences that support a safe, gradual return to physical activity after injury or inactivity.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
        <h3>Low-Impact and Controlled Sequences</h3>
        <p>Gentle, low-impact movements designed to rebuild strength and mobility without placing stress on recovering areas.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg></div>
        <h3>Body Awareness and Mobility Restoration</h3>
        <p>Rebuild your connection to your body and restore range of motion through mindful, guided movement.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
        <h3>Mindful, Gradual Progression</h3>
        <p>Progress at your own pace in a supportive Southport studio environment that prioritises your wellbeing above all else.</p>
      </div>
    </div>
  </div>
</section>'''
        html = html[:old_core_match.start()] + new_core_grid + html[old_core_match.end():]

    # Who it's for H2
    html = re.sub(r'<h2>Who Is Recovery Movement[^<]*</h2>', '<h2>Who Is Recovery Movement Flow - Foundations For?</h2>', html)

    # SEO content
    old_seo_section = re.search(r'<section class="seo-content".*?</section>', html, re.DOTALL)
    if old_seo_section:
        new_seo = '''<section class="seo-content" aria-label="About Recovery Movement Flow on the Gold Coast">
  <div class="seo-content__inner">
    <h2>Recovery Movement Flow on the Gold Coast — Safe, Gentle Classes at UNDRGRND Movement Southport</h2>
    <p>UNDRGRND Movement offers Recovery Movement Flow – Foundations classes at our Southport studio, located at 163 Ferry Rd, Gold Coast. This gentle, low-impact program is designed for Gold Coast adults who are returning to movement after injury, illness, surgery, or an extended period of inactivity. Medical clearance from a healthcare provider is required before participating.</p>
    <h3>What Is Recovery Movement Flow?</h3>
    <p>Recovery Movement Flow – Foundations is a carefully structured program that prioritises safe, gradual re-engagement with physical activity. Unlike general fitness classes on the Gold Coast, this program is specifically designed for individuals whose bodies need a supported, mindful approach to returning to movement. Each session at UNDRGRND Movement Southport is led by a qualified instructor who adapts movements to individual needs and capabilities.</p>
    <p>The class focuses on rebuilding body awareness, restoring mobility, and developing confidence in movement through slow, controlled sequences. At our Southport studio, every session is structured to feel safe and supportive, with movements introduced at a pace that respects each participant's recovery journey.</p>
    <h3>Who Is Recovery Movement Flow For?</h3>
    <p>Recovery Movement Flow – Foundations at UNDRGRND Movement is designed for Gold Coast adults aged 45 and above who are navigating a return to movement after a health event. This includes individuals recovering from surgery, managing a chronic condition, returning to exercise after an extended break, or anyone whose healthcare provider has recommended gentle, supervised movement as part of their recovery plan.</p>
    <p>Medical clearance from your healthcare provider is required before attending this program at our Southport studio. This requirement exists to ensure your safety and to allow our Gold Coast instructors to understand your specific needs and adapt the class accordingly. Please contact us at undrgrndgc@gmail.com to discuss clearance requirements before booking.</p>
    <h3>The Benefits of Gentle Movement for Recovery</h3>
    <p>Gentle, structured movement has been shown to support recovery from a wide range of conditions. At UNDRGRND Movement Southport, Recovery Movement Flow participants on the Gold Coast report improvements in mobility, reduced stiffness, better balance, and increased confidence in their bodies. The low-impact, controlled nature of the class minimises the risk of re-injury while still providing meaningful physical benefit.</p>
    <p>Beyond the physical, the supportive environment at our Southport studio provides significant mental and emotional benefits. Returning to movement after injury or illness can be daunting, and many Gold Coast participants describe the Recovery Movement Flow program as a gentle, encouraging bridge back to an active life. Our instructors understand the unique challenges of recovery and create a space where every participant feels seen, supported, and respected.</p>
    <h3>Recovery Movement Flow at UNDRGRND Movement Southport</h3>
    <p>UNDRGRND Movement is located at 163 Ferry Rd, Southport QLD 4215, making it accessible to Gold Coast residents from Southport, Surfers Paradise, Broadbeach, Robina, and surrounding suburbs. Our Southport studio is purpose-built for movement classes, providing a safe and welcoming environment for all participants.</p>
    <p>Recovery Movement Flow – Foundations is currently accepting waitlist registrations. To join the waitlist or discuss whether this program is right for you, please contact us at undrgrndgc@gmail.com or call 0721 402 690. Our Gold Coast team will be happy to answer any questions and help you take the first step back to movement.</p>
    <h3>Begin Your Recovery Journey on the Gold Coast</h3>
    <p>If you are a Gold Coast resident looking for a safe, gentle, and professionally guided return to movement after injury or inactivity, Recovery Movement Flow – Foundations at UNDRGRND Movement Southport is designed for you. Join our waitlist today and take the first step toward rebuilding your strength, mobility, and confidence in a supportive Southport environment.</p>
  </div>
</section>'''
        html = html[:old_seo_section.start()] + new_seo + html[old_seo_section.end():]

    # CTA section
    html = re.sub(r'<section class="program-cta" aria-label="[^"]*">', '<section class="program-cta" aria-label="Join Recovery Movement Flow Waitlist">', html)
    html = re.sub(r'<h2>Ready[^<]*</h2>', '<h2>Ready to Begin Your Recovery Journey?</h2>', html)
    html = re.sub(r'<p>Join[^<]*Recovery[^<]*</p>', '<p>Recovery Movement Flow – Foundations is coming soon to UNDRGRND Movement Southport. Join the waitlist and be the first to know when classes open.</p>', html)

    # Schema breadcrumb
    html = re.sub(
        r"\{ name: 'Recovery Movement[^']*', url: '[^']*' \}",
        "{ name: 'Recovery Movement Flow - Foundations', url: 'https://www.undrgrnd.com.au/programs/recovery-movement-flow-foundations.html' }",
        html
    )

    # Fix all remaining old booking URLs
    html = fix_booking_urls(html)

    write(dst, html)
    print(f'  [OK] {dst}')


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3C: pole-flow.html → pole-flow-foundations.html
# ─────────────────────────────────────────────────────────────────────────────
def task_3c():
    print('\n[3C] Pole Flow → Pole Flow - Foundations (Coming Soon)')
    src = f'{BASE}/pole-flow.html'
    dst = f'{BASE}/pole-flow-foundations.html'
    html = read(src)

    # Head
    html = update_head(html,
        title='Pole Flow - Foundations | Pole Dance Gold Coast | UNDRGRND Movement Southport',
        meta_desc='Smooth transitions and connected sequences on the pole at UNDRGRND Movement Southport. Pole Flow - Foundations is coming soon to the Gold Coast.',
        canonical_url='https://www.undrgrnd.com.au/programs/pole-flow-foundations.html',
        og_title='Pole Flow - Foundations | Pole Dance Gold Coast | UNDRGRND Movement',
        og_desc='Pole Flow - Foundations — smooth transitions and flow on the pole. Coming soon to UNDRGRND Movement Southport, Gold Coast.',
        og_url='https://www.undrgrnd.com.au/programs/pole-flow-foundations.html'
    )

    # Hero aria-label
    html = html.replace('aria-label="Pole Flow Hero"', 'aria-label="Pole Flow - Foundations Hero"')

    # Badge — add coming soon
    html = html.replace(
        '<div class="program-hero__badge ">Intermediate</div>',
        '<div class="program-hero__badge">Balanced / Flow &nbsp;·&nbsp; Beginner Friendly</div>\n      <div class="program-hero__badge" style="background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.4);color:#F59E0B;margin-top:0.5rem;">Coming Soon</div>'
    )

    # H1
    html = html.replace(
        '<h1 class="program-hero__h1">Pole Flow<br><span>Gold Coast</span></h1>',
        '<h1 class="program-hero__h1">Pole Flow - Foundations<br><span>Pole Dance Gold Coast</span></h1>'
    )

    # Hero sub
    html = html.replace(
        '<p class="program-hero__sub">Create smooth, flowing movement around the pole with seamless transitions and expressive quality. The next step after Pole Fitness Foundations at UNDRGRND Movement Southport, Gold Coast.</p>',
        '<p class="program-hero__sub">Build on the basics of pole movement with smooth transitions, connected sequences, and a greater sense of fluidity and control. Coming soon to UNDRGRND Movement Southport, Gold Coast.</p>'
    )

    # Remove old prerequisite note (emoji)
    html = html.replace(
        '<p style="color:#F59E0B;font-size:.9rem;margin-top:1rem;">⚠ Prerequisite: Pole Fitness Foundations or instructor approval required</p>',
        '<div class="info-box" style="background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.3);border-radius:8px;padding:1rem 1.25rem;margin-top:1rem;"><p style="color:#A1A1A1;font-size:0.9rem;margin:0;"><strong style="color:#FFFFFF;">Recommended:</strong> Pole Fitness Foundations or instructor approval for best progress</p></div>'
    )

    # Book buttons → Join Waitlist
    html = html.replace(
        f'<a href="{OLD_BOOKING_URL}" class="cta-button">Book This Class</a>',
        '<a href="mailto:undrgrndgc@gmail.com?subject=Pole%20Flow%20Foundations%20Waitlist" class="cta-button">Join Waitlist</a>'
    )
    html = html.replace(
        f'<a href="{OLD_BOOKING_URL}" class="cta-button" style="width:100%;text-align:center;display:block;">Book Now</a>',
        '<a href="mailto:undrgrndgc@gmail.com?subject=Pole%20Flow%20Foundations%20Waitlist" class="cta-button" style="width:100%;text-align:center;display:block;">Join Waitlist</a>'
    )
    html = html.replace(
        f'<a href="{OLD_BOOKING_URL}" class="cta-button">Book Your First Class</a>',
        '<a href="mailto:undrgrndgc@gmail.com?subject=Pole%20Flow%20Foundations%20Waitlist" class="cta-button">Join Waitlist</a>'
    )

    # Overview H2 and description
    html = html.replace('<h2>About Pole Flow</h2>', '<h2>About Pole Flow - Foundations</h2>')
    html = html.replace(
        '<p>Create smooth, flowing movement around the pole with seamless transitions and expressive quality. The next step after Pole Fitness Foundations at UNDRGRND Movement Southport, Gold Coast.</p>\n      <p>At UNDRGRND Movement Southport, Pole Flow is taught by our qualified instructor in a small-group, supportive environment. Classes are designed to be accessible and welcoming to all participants, regardless of prior experience.</p>',
        '<p>Pole Flow – Foundations builds on the basics of pole movement by introducing smooth transitions, connected sequences, and a greater sense of fluidity and control on the pole. The class focuses on linking movements together in a way that feels natural and graceful, developing coordination, timing, and body awareness through guided flow-based sequences.</p>\n      <p>Through each curated, smooth, and authentic movement, you will improve your ability to transition between positions with ease and confidence. This class is ideal for those who have completed Pole Fitness – Foundations and are ready to develop their movement quality and flow.</p>'
    )

    # Core focus cards
    old_core_match = re.search(r'<div class="core-focus__grid">.*?</div>\s*</div>\s*</section>', html, re.DOTALL)
    if old_core_match:
        new_core_grid = '''<div class="core-focus__grid">
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div>
        <h3>Smooth Transitions and Connected Sequences</h3>
        <p>Learn to link individual moves into seamless sequences without stopping or breaking the line of movement.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg></div>
        <h3>Flow and Movement Quality</h3>
        <p>Develop the expressive quality of your movement — how you move is as important as what you do on the pole.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
        <h3>Coordination and Timing</h3>
        <p>Build timing and body awareness through structured flow sequences that develop natural rhythm on the pole.</p>
      </div>
      <div class="core-focus__card reveal">
        <div class="core-focus__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
        <h3>Body Awareness and Control</h3>
        <p>Develop spatial awareness and body control through guided flow-based sequences at our Southport studio.</p>
      </div>
    </div>
  </div>
</section>'''
        html = html[:old_core_match.start()] + new_core_grid + html[old_core_match.end():]

    # Related programs — update links
    html = html.replace('href="/programs/aerial-silks.html"', 'href="/programs/aerial-silks-foundations.html"')

    # SEO content
    old_seo_section = re.search(r'<section class="seo-content".*?</section>', html, re.DOTALL)
    if old_seo_section:
        new_seo = '''<section class="seo-content" aria-label="About Pole Flow - Foundations on the Gold Coast">
  <div class="seo-content__inner">
    <h2>Pole Flow - Foundations on the Gold Coast — Coming Soon to UNDRGRND Movement Southport</h2>
    <p>UNDRGRND Movement is bringing Pole Flow – Foundations to our Southport studio at 163 Ferry Rd, Gold Coast. This intermediate pole fitness program is designed for Gold Coast students who have completed Pole Fitness Foundations and are ready to develop smooth, flowing movement on the pole.</p>
    <h3>What Is Pole Flow - Foundations?</h3>
    <p>Pole Flow – Foundations is the natural progression from Pole Fitness Foundations at UNDRGRND Movement. Where Foundations focuses on learning individual techniques safely, Pole Flow – Foundations is about connecting those techniques into seamless sequences — creating movement that flows from one element to the next without stopping or breaking the line of the body.</p>
    <p>At UNDRGRND Movement Southport, Pole Flow – Foundations classes will develop your ability to transition between spins, holds, and floor work with control and grace. The focus is on movement quality — how you move, not just what you do. Students at our Gold Coast studio will develop a personal movement style that is expressive, fluid, and confident.</p>
    <h3>Who Is Pole Flow - Foundations For?</h3>
    <p>Pole Flow – Foundations at UNDRGRND Movement is for students who have a solid foundation in pole technique and are ready to develop their movement quality. Completion of Pole Fitness – Foundations or equivalent experience is recommended. If you are unsure whether you are ready, contact our Southport studio and we will advise you.</p>
    <h3>Join the Waitlist</h3>
    <p>Pole Flow – Foundations is coming soon to UNDRGRND Movement Southport, Gold Coast. Join the waitlist today to be among the first to know when classes open. Email us at undrgrndgc@gmail.com or call 0721 402 690 to register your interest.</p>
  </div>
</section>'''
        html = html[:old_seo_section.start()] + new_seo + html[old_seo_section.end():]

    # CTA
    html = re.sub(r'<section class="program-cta" aria-label="[^"]*">', '<section class="program-cta" aria-label="Join Pole Flow Foundations Waitlist">', html)
    html = re.sub(r'<h2>Ready to Find Your Flow\?</h2>', '<h2>Be First to Know When We Launch</h2>', html)
    html = re.sub(r'<p>Take your pole practice[^<]*</p>', '<p>Pole Flow – Foundations is coming soon to UNDRGRND Movement Southport. Join the waitlist and be the first to book when classes open on the Gold Coast.</p>', html)

    # Sticky book
    html = html.replace(
        f'<a href="{OLD_BOOKING_URL}" class="cta-button">Book Pole Flow</a>',
        '<a href="mailto:undrgrndgc@gmail.com?subject=Pole%20Flow%20Foundations%20Waitlist" class="cta-button">Join Waitlist</a>'
    )

    # Schema breadcrumb
    html = html.replace(
        "{ name: 'Pole Flow', url: 'https://www.undrgrnd.com.au/programs/pole-flow.html' }",
        "{ name: 'Pole Flow - Foundations', url: 'https://www.undrgrnd.com.au/programs/pole-flow-foundations.html' }"
    )

    html = fix_booking_urls(html)
    write(dst, html)
    print(f'  [OK] {dst}')


# ─────────────────────────────────────────────────────────────────────────────
# GENERIC UPDATER for simpler pages (yoga-fusion, traditional-yoga, modern-yoga,
# aerial-yoga, choreography-fusion)
# ─────────────────────────────────────────────────────────────────────────────
def update_simple_page(src_file, dst_file, config):
    """Generic updater for the simpler program pages using program-hero template"""
    print(f'\n[{config["task"]}] {config["old_name"]} → {config["new_name"]}')
    src = f'{BASE}/{src_file}'
    dst = f'{BASE}/{dst_file}'
    html = read(src)

    # Head
    html = update_head(html,
        title=config['title'],
        meta_desc=config['meta_desc'],
        canonical_url=f'https://www.undrgrnd.com.au/programs/{dst_file}',
        og_title=config['og_title'],
        og_desc=config['og_desc'],
        og_url=f'https://www.undrgrnd.com.au/programs/{dst_file}'
    )

    # Hero aria-label
    html = re.sub(r'aria-label="[^"]*Hero"', f'aria-label="{config["new_name"]} Hero"', html, count=1)

    # Badge
    html = re.sub(
        r'<div class="program-hero__badge[^"]*">[^<]*</div>',
        f'<div class="program-hero__badge">{config["badge"]}</div>',
        html, count=1
    )

    # H1
    html = re.sub(
        r'<h1 class="program-hero__h1">[^<]*(?:<br>[^<]*)?</h1>',
        f'<h1 class="program-hero__h1">{config["new_name"]}<br><span>{config["subtitle"]}</span></h1>',
        html, count=1
    )

    # Hero sub
    html = re.sub(
        r'<p class="program-hero__sub">[^<]*</p>',
        f'<p class="program-hero__sub">{config["hero_sub"]}</p>',
        html, count=1
    )

    # Hero images
    slug_old = src_file.replace('.html', '')
    slug_new = dst_file.replace('.html', '')
    html = html.replace(f'../images/hero/{slug_old}-mobile.webp', f'../images/hero/{slug_new}-mobile.webp')
    html = html.replace(f'../images/hero/{slug_old}.webp', f'../images/hero/{slug_new}.webp')
    html = re.sub(r'alt="[^"]*class at UNDRGRND[^"]*"', f'alt="{config["new_name"]} class at UNDRGRND Movement, Southport Gold Coast"', html, count=1)

    # Overview H2
    html = re.sub(r'<h2>About [^<]*</h2>', f'<h2>About {config["new_name"]}</h2>', html, count=1)

    # Overview description — replace the two overview paragraphs
    old_desc_match = re.search(r'(<div class="program-overview__desc reveal">)(.*?)(</div>)', html, re.DOTALL)
    if old_desc_match:
        new_desc = f'{old_desc_match.group(1)}\n      <h2>About {config["new_name"]}</h2>\n      <p>{config["desc_p1"]}</p>\n      <p>{config["desc_p2"]}</p>\n    {old_desc_match.group(3)}'
        html = html[:old_desc_match.start()] + new_desc + html[old_desc_match.end():]

    # Core focus section subtitle
    html = re.sub(
        r'<p>What you will develop in every [^<]* class at UNDRGRND Movement Southport</p>',
        f'<p>What you will develop in every {config["new_name"]} class at UNDRGRND Movement Southport</p>',
        html, count=1
    )

    # Core focus cards
    old_core_match = re.search(r'<div class="core-focus__grid">.*?</div>\s*</div>\s*</section>', html, re.DOTALL)
    if old_core_match:
        cards = config['core_focus']
        icons = [
            '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 6v6l4 2"/></svg>',
            '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
            '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>',
            '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
        ]
        card_html = '\n'.join([
            f'''      <div class="core-focus__card reveal">
        <div class="core-focus__icon">{icons[i]}</div>
        <h3>{c["title"]}</h3>
        <p>{c["desc"]}</p>
      </div>''' for i, c in enumerate(cards[:4])
        ])
        new_core_grid = f'''<div class="core-focus__grid">
{card_html}
    </div>
  </div>
</section>'''
        html = html[:old_core_match.start()] + new_core_grid + html[old_core_match.end():]

    # Who it's for H2
    html = re.sub(r'<h2>Who Is [^<]* For\?</h2>', f'<h2>Who Is {config["new_name"]} For?</h2>', html, count=1)

    # What to expect subtitle
    html = re.sub(
        r'<p>A typical [^<]* session at UNDRGRND Movement Southport</p>',
        f'<p>A typical {config["new_name"]} session at UNDRGRND Movement Southport</p>',
        html, count=1
    )

    # Related programs
    if 'related' in config:
        old_related_match = re.search(r'<div class="related__grid">.*?</div>\s*</div>\s*</section>', html, re.DOTALL)
        if old_related_match:
            rel_html = '\n'.join([
                f'''      <a href="{r['url']}" class="related-card reveal">
        <div class="related-card__badge">{r['badge']}</div>
        <div class="related-card__name">{r['name']}</div>
        <div class="related-card__desc">{r['desc']}</div>
      </a>''' for r in config['related']
            ])
            new_related = f'''<div class="related__grid">
{rel_html}
    </div>
  </div>
</section>'''
            html = html[:old_related_match.start()] + new_related + html[old_related_match.end():]

    # SEO content
    old_seo_section = re.search(r'<section class="seo-content".*?</section>', html, re.DOTALL)
    if old_seo_section:
        html = html[:old_seo_section.start()] + config['seo_section'] + html[old_seo_section.end():]

    # CTA
    html = re.sub(r'<section class="program-cta" aria-label="[^"]*">', f'<section class="program-cta" aria-label="Book {config["new_name"]}">', html, count=1)
    html = re.sub(r'<h2>Ready[^<]*</h2>', f'<h2>{config["cta_heading"]}</h2>', html, count=1)
    html = re.sub(r'<p>Join[^<]*community[^<]*</p>', f'<p>{config["cta_sub"]}</p>', html, count=1)

    # Sticky book
    html = re.sub(
        r'<a href="https://app\.classmanager\.com/portal/undrgrnd-movement/register" class="cta-button">Book [^<]*</a>\s*</div>',
        f'<a href="{BOOKING_URL}" class="cta-button">Book {config["new_name"]}</a>\n</div>',
        html, count=1
    )

    # Schema breadcrumb
    new_name_val = config['new_name']
    breadcrumb_replacement = "{ name: '" + new_name_val + "', url: 'https://www.undrgrnd.com.au/programs/" + dst_file + "' }"
    html = re.sub(
        r"\{ name: '[^']+', url: 'https://www\.undrgrnd\.com\.au/programs/[^']+\.html' \}(?=\s*\])",
        breadcrumb_replacement,
        html
    )

    html = fix_booking_urls(html)
    write(dst, html)
    print(f'  [OK] {dst}')


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3D: yoga-fusion.html → fusion-yoga-foundations.html
# ─────────────────────────────────────────────────────────────────────────────
def task_3d():
    update_simple_page('yoga-fusion.html', 'fusion-yoga-foundations.html', {
        'task': '3D',
        'old_name': 'Yoga Fusion',
        'new_name': 'Fusion Yoga - Foundations',
        'title': 'Fusion Yoga - Foundations | Yoga Classes Gold Coast | UNDRGRND Movement Southport',
        'meta_desc': 'Blend traditional yoga with modern movement at UNDRGRND Movement Southport. Fusion Yoga builds mobility and strength. Beginner-friendly classes on the Gold Coast.',
        'og_title': 'Fusion Yoga - Foundations | Yoga Classes Gold Coast | UNDRGRND Movement',
        'og_desc': 'Blend traditional yoga with modern movement at UNDRGRND Movement Southport. Beginner-friendly yoga classes on the Gold Coast.',
        'badge': 'Balanced &nbsp;·&nbsp; Beginner Friendly',
        'subtitle': 'Yoga Classes Gold Coast',
        'hero_sub': 'Blend traditional yoga with modern movement in a beginner-friendly class at UNDRGRND Movement Southport. Build mobility, strength, and body awareness on the Gold Coast.',
        'desc_p1': 'Fusion Yoga – Foundations is a beginner-friendly class that blends traditional yoga with modern movement to create an accessible and engaging practice. The class focuses on improving mobility, flexibility, and strength while keeping the practice approachable and easy to follow for all levels.',
        'desc_p2': 'Combining traditional yoga elements with modern movement patterns, each session creates an active and engaging experience built around controlled sequences, posture, and body awareness. Through each curated, smooth, and authentic movement, you will develop flexibility, strength, and a deeper understanding of how your body moves.',
        'core_focus': [
            {'title': 'Traditional Yoga and Modern Movement', 'desc': 'Experience the best of both worlds — classical yoga postures combined with contemporary movement patterns.'},
            {'title': 'Mobility and Strength', 'desc': 'Build functional flexibility and strength through a balanced practice that develops both qualities simultaneously.'},
            {'title': 'Controlled Sequences', 'desc': 'Learn to move with intention and control through structured sequences that build body awareness and coordination.'},
            {'title': 'Body Awareness and Posture', 'desc': 'Develop a deeper understanding of your body and improve posture through mindful, guided movement at our Southport studio.'},
        ],
        'related': [
            {'url': '/programs/traditional-yoga-foundations.html', 'badge': 'Yoga', 'name': 'Traditional Yoga - Foundations', 'desc': 'Classic postures, breath control, and mindful movement in a structured beginner-friendly class.'},
            {'url': '/programs/flow-yoga-foundations.html', 'badge': 'Yoga', 'name': 'Flow Yoga - Foundations', 'desc': 'Dynamic yoga with fluid movement, functional strength, and controlled transitions.'},
            {'url': '/programs/movement-flow-foundations.html', 'badge': 'Movement', 'name': 'Movement Flow - Foundations', 'desc': 'Reconnect with your body through fluid, natural movement in a calm and supportive environment.'},
        ],
        'seo_section': '''<section class="seo-content" aria-label="About Fusion Yoga on the Gold Coast">
  <div class="seo-content__inner">
    <h2>Fusion Yoga on the Gold Coast — Beginner-Friendly Classes at UNDRGRND Movement Southport</h2>
    <p>UNDRGRND Movement offers Fusion Yoga – Foundations classes at our Southport studio, located at 163 Ferry Rd, Gold Coast. This beginner-friendly yoga class blends traditional yoga with modern movement to create an accessible, engaging practice that builds mobility, strength, and body awareness for Gold Coast participants of all levels.</p>
    <h3>What Is Fusion Yoga - Foundations?</h3>
    <p>Fusion Yoga – Foundations is a contemporary approach to yoga that combines the time-tested principles of traditional yoga with modern movement patterns. Unlike purely traditional yoga classes on the Gold Coast, Fusion Yoga creates a dynamic practice that feels both grounded and progressive. Each session at UNDRGRND Movement Southport introduces structured sequences that are broken down step by step, making them accessible even for complete beginners.</p>
    <p>The class focuses on improving mobility, flexibility, and functional strength through controlled sequences and body-awareness exercises. At our Southport studio, every session is designed to be welcoming and approachable, with our Gold Coast instructors guiding participants through each movement with clear, supportive instruction.</p>
    <h3>Why Fusion Yoga Is Perfect for Beginners on the Gold Coast</h3>
    <p>Fusion Yoga – Foundations at UNDRGRND Movement Southport is specifically designed for Gold Coast adults who are new to yoga or who have found traditional yoga classes too rigid or inaccessible. By blending classical yoga elements with modern movement, the class creates a practice that feels natural, engaging, and achievable from the very first session.</p>
    <p>Our Southport studio provides a welcoming, non-judgmental environment where Gold Coast participants feel comfortable learning at their own pace. Whether you are a complete beginner, someone returning to yoga after a break, or simply looking for a fresh approach to movement on the Gold Coast, Fusion Yoga – Foundations offers a genuinely accessible starting point.</p>
    <h3>The Benefits of Fusion Yoga Training</h3>
    <p>Regular practice of Fusion Yoga – Foundations at UNDRGRND Movement Southport delivers a wide range of physical benefits. Gold Coast participants report improved flexibility, better posture, increased functional strength, and enhanced body awareness. The combination of traditional yoga and modern movement creates a well-rounded practice that develops multiple physical qualities simultaneously.</p>
    <p>Beyond the physical, Fusion Yoga at our Southport studio provides significant mental benefits. The structured, mindful nature of the practice encourages participants to slow down, focus on their breath, and develop a deeper connection to their bodies. Many Gold Coast participants describe Fusion Yoga as a welcome balance between physical challenge and mental calm.</p>
    <h3>Fusion Yoga at UNDRGRND Movement Southport, Gold Coast</h3>
    <p>UNDRGRND Movement is located at 163 Ferry Rd, Southport QLD 4215, making it easily accessible to Gold Coast residents from Southport, Surfers Paradise, Broadbeach, Robina, and surrounding suburbs. Our Southport studio is purpose-built for movement classes, providing a calm and welcoming environment for yoga practice.</p>
    <p>We offer flexible booking options including drop-in classes ($22 per session), 10-class packs ($180), and unlimited monthly memberships ($160 per month). All options can be booked online through our timetable page, making it easy for Gold Coast residents to fit Fusion Yoga into their weekly routine.</p>
    <h3>Begin Your Fusion Yoga Journey on the Gold Coast</h3>
    <p>If you have been looking for a yoga class on the Gold Coast that is accessible, engaging, and genuinely beginner-friendly, Fusion Yoga – Foundations at UNDRGRND Movement Southport is the right choice. Join our growing community of Gold Coast yoga students and discover the benefits of a practice that blends the best of traditional and modern movement.</p>
    <p>Book your first Fusion Yoga class today at UNDRGRND Movement, 163 Ferry Rd, Southport — Gold Coast's home for accessible, modern yoga.</p>
  </div>
</section>''',
        'cta_heading': 'Ready to Begin Your Fusion Yoga Journey?',
        'cta_sub': 'Join Fusion Yoga – Foundations at UNDRGRND Movement Southport. No experience needed — just bring yourself and an open mind.',
    })


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3E: traditional-yoga.html → traditional-yoga-foundations.html
# ─────────────────────────────────────────────────────────────────────────────
def task_3e():
    update_simple_page('traditional-yoga.html', 'traditional-yoga-foundations.html', {
        'task': '3E',
        'old_name': 'Traditional Yoga',
        'new_name': 'Traditional Yoga - Foundations',
        'title': 'Traditional Yoga - Foundations | Yoga Classes Gold Coast | UNDRGRND Movement Southport',
        'meta_desc': 'Classic yoga postures, breath control, and mindful movement at UNDRGRND Movement Southport. Traditional Yoga - Foundations is beginner-friendly on the Gold Coast.',
        'og_title': 'Traditional Yoga - Foundations | Yoga Classes Gold Coast | UNDRGRND Movement',
        'og_desc': 'Classic yoga postures and breath control at UNDRGRND Movement Southport. Beginner-friendly traditional yoga on the Gold Coast.',
        'badge': 'Balanced &nbsp;·&nbsp; Beginner Friendly',
        'subtitle': 'Yoga Classes Gold Coast',
        'hero_sub': 'Classic postures, breath control, and mindful movement in a structured, beginner-friendly class at UNDRGRND Movement Southport. Traditional yoga on the Gold Coast.',
        'desc_p1': 'Traditional Yoga – Foundations introduces you to the core principles of yoga through classic postures, breath control, and mindful movement. The class is structured to help beginners build a solid foundation in yoga practice, developing alignment, posture, and a sense of ease and control at a comfortable pace.',
        'desc_p2': 'Each session guides you through simple, well-established sequences with a focus on alignment, posture, and controlled breathing. Movements are introduced gradually, allowing you to build confidence and stability without pressure. Through each curated, smooth, and authentic movement, you will develop body awareness, improve mobility, and create a sense of ease and control in your practice.',
        'core_focus': [
            {'title': 'Classic Postures and Breath Control', 'desc': 'Learn foundational yoga postures paired with proper breathing techniques that form the basis of all yoga practice.'},
            {'title': 'Alignment and Posture', 'desc': 'Develop correct alignment and posture through guided instruction that builds a safe and sustainable yoga practice.'},
            {'title': 'Flexibility and Balance', 'desc': 'Improve flexibility and balance through progressive sequences that develop both qualities at a comfortable pace.'},
            {'title': 'Mindful Movement', 'desc': 'Cultivate mindfulness and body awareness through intentional, breath-led movement at our Southport studio.'},
        ],
        'related': [
            {'url': '/programs/fusion-yoga-foundations.html', 'badge': 'Yoga', 'name': 'Fusion Yoga - Foundations', 'desc': 'Blend traditional yoga with modern movement for mobility and strength.'},
            {'url': '/programs/flow-yoga-foundations.html', 'badge': 'Yoga', 'name': 'Flow Yoga - Foundations', 'desc': 'Dynamic yoga with fluid movement, functional strength, and controlled transitions.'},
            {'url': '/programs/movement-flow-foundations.html', 'badge': 'Movement', 'name': 'Movement Flow - Foundations', 'desc': 'Reconnect with your body through fluid, natural movement in a calm and supportive environment.'},
        ],
        'seo_section': '''<section class="seo-content" aria-label="About Traditional Yoga on the Gold Coast">
  <div class="seo-content__inner">
    <h2>Traditional Yoga on the Gold Coast — Beginner-Friendly Classes at UNDRGRND Movement Southport</h2>
    <p>UNDRGRND Movement offers Traditional Yoga – Foundations classes at our Southport studio, located at 163 Ferry Rd, Gold Coast. This beginner-friendly yoga class introduces the core principles of traditional yoga through classic postures, breath control, and mindful movement, providing Gold Coast participants with a solid foundation for their yoga practice.</p>
    <h3>What Is Traditional Yoga - Foundations?</h3>
    <p>Traditional Yoga – Foundations is a structured beginner program that focuses on the foundational elements of yoga practice. Unlike modern yoga hybrids or fitness-focused yoga classes on the Gold Coast, this program stays true to the classical principles of yoga — emphasising alignment, breath control, and mindful movement as the basis for a sustainable, lifelong practice.</p>
    <p>Each session at UNDRGRND Movement Southport introduces well-established yoga postures and sequences in a clear, accessible way. Our Gold Coast instructors guide participants through each movement with detailed alignment cues, ensuring that beginners develop correct technique from the very start. The pace is comfortable and unhurried, allowing participants to build confidence and body awareness gradually.</p>
    <h3>Why Traditional Yoga Is Perfect for Beginners on the Gold Coast</h3>
    <p>Traditional Yoga – Foundations at UNDRGRND Movement Southport is specifically designed for Gold Coast adults who are new to yoga or who want to return to the fundamentals of classical practice. The structured, progressive approach ensures that beginners develop a solid foundation before advancing to more complex postures or sequences.</p>
    <p>Our Southport studio provides a calm, welcoming environment where Gold Coast participants feel comfortable learning at their own pace. Whether you have never attended a yoga class before or are returning to practice after a break, Traditional Yoga – Foundations offers a genuinely accessible and supportive starting point on the Gold Coast.</p>
    <h3>The Benefits of Traditional Yoga Practice</h3>
    <p>Regular practice of Traditional Yoga – Foundations at UNDRGRND Movement Southport delivers a wide range of physical and mental benefits. Gold Coast participants report improved flexibility, better posture, increased body awareness, and a greater sense of calm and mental clarity. The breath-led, mindful nature of traditional yoga creates a practice that benefits both body and mind.</p>
    <p>The emphasis on alignment and correct technique in Traditional Yoga – Foundations also helps Gold Coast participants develop sustainable movement habits that reduce the risk of injury and support long-term physical health. Many students at our Southport studio describe their traditional yoga practice as a cornerstone of their overall wellbeing routine.</p>
    <h3>Traditional Yoga at UNDRGRND Movement Southport, Gold Coast</h3>
    <p>UNDRGRND Movement is located at 163 Ferry Rd, Southport QLD 4215, making it easily accessible to Gold Coast residents from Southport, Surfers Paradise, Broadbeach, Robina, and surrounding suburbs. Our Southport studio is purpose-built for movement classes, providing a calm and welcoming environment for yoga practice.</p>
    <p>We offer flexible booking options including drop-in classes ($22 per session), 10-class packs ($180), and unlimited monthly memberships ($160 per month). All options can be booked online through our timetable page, making it easy for Gold Coast residents to fit Traditional Yoga into their weekly routine.</p>
    <h3>Begin Your Traditional Yoga Journey on the Gold Coast</h3>
    <p>If you have been looking for a traditional yoga class on the Gold Coast that is structured, accessible, and genuinely beginner-friendly, Traditional Yoga – Foundations at UNDRGRND Movement Southport is the right choice. Join our growing community of Gold Coast yoga students and discover the timeless benefits of classical yoga practice.</p>
    <p>Book your first Traditional Yoga class today at UNDRGRND Movement, 163 Ferry Rd, Southport — Gold Coast's home for accessible, classical yoga.</p>
  </div>
</section>''',
        'cta_heading': 'Ready to Begin Your Yoga Journey?',
        'cta_sub': 'Join Traditional Yoga – Foundations at UNDRGRND Movement Southport. No experience needed — just bring yourself and an open mind.',
    })


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3F: modern-yoga.html → flow-yoga-foundations.html
# ─────────────────────────────────────────────────────────────────────────────
def task_3f():
    update_simple_page('modern-yoga.html', 'flow-yoga-foundations.html', {
        'task': '3F',
        'old_name': 'Modern Yoga',
        'new_name': 'Flow Yoga - Foundations',
        'title': 'Flow Yoga - Foundations | Dynamic Yoga Gold Coast | UNDRGRND Movement Southport',
        'meta_desc': 'Dynamic yoga with fluid movement at UNDRGRND Movement Southport. Flow Yoga builds strength and flexibility. Beginner-friendly classes on the Gold Coast.',
        'og_title': 'Flow Yoga - Foundations | Dynamic Yoga Gold Coast | UNDRGRND Movement',
        'og_desc': 'Dynamic yoga with fluid movement and functional strength at UNDRGRND Movement Southport. Beginner-friendly flow yoga on the Gold Coast.',
        'badge': 'Balanced &nbsp;·&nbsp; Dynamic &nbsp;·&nbsp; Beginner Friendly',
        'subtitle': 'Dynamic Yoga Gold Coast',
        'hero_sub': 'Dynamic yoga with fluid movement, functional strength, and simple sequences at UNDRGRND Movement Southport. A beginner-friendly approach to yoga on the Gold Coast.',
        'desc_p1': 'Flow Yoga – Foundations offers a beginner-friendly approach to yoga through fluid movement, functional strength, and simple, dynamic sequences. The class focuses on improving mobility, stability, and overall body control while keeping the practice accessible and easy to follow.',
        'desc_p2': 'Combining traditional yoga elements with modern movement patterns, each session creates an active and engaging experience built around controlled transitions, posture, and strength through movement rather than long static holds. Through each curated, smooth, and authentic movement, you will develop body awareness, improve flexibility, and build strength in a way that feels natural and sustainable.',
        'core_focus': [
            {'title': 'Fluid Movement and Dynamic Sequences', 'desc': 'Experience yoga as a flowing, dynamic practice through sequences that keep the body moving and engaged throughout.'},
            {'title': 'Functional Strength', 'desc': 'Build practical, usable strength through yoga-based movements that develop stability and control in everyday life.'},
            {'title': 'Controlled Transitions', 'desc': 'Learn to move between postures with control and intention, developing coordination and body awareness through practice.'},
            {'title': 'Active and Engaging Practice', 'desc': 'Enjoy a yoga practice that feels energetic and engaging while remaining accessible and beginner-friendly at our Southport studio.'},
        ],
        'related': [
            {'url': '/programs/fusion-yoga-foundations.html', 'badge': 'Yoga', 'name': 'Fusion Yoga - Foundations', 'desc': 'Blend traditional yoga with modern movement for mobility and strength.'},
            {'url': '/programs/traditional-yoga-foundations.html', 'badge': 'Yoga', 'name': 'Traditional Yoga - Foundations', 'desc': 'Classic postures, breath control, and mindful movement in a structured beginner-friendly class.'},
            {'url': '/programs/movement-flow-foundations.html', 'badge': 'Movement', 'name': 'Movement Flow - Foundations', 'desc': 'Reconnect with your body through fluid, natural movement in a calm and supportive environment.'},
        ],
        'seo_section': '''<section class="seo-content" aria-label="About Flow Yoga on the Gold Coast">
  <div class="seo-content__inner">
    <h2>Flow Yoga on the Gold Coast — Dynamic Beginner Classes at UNDRGRND Movement Southport</h2>
    <p>UNDRGRND Movement offers Flow Yoga – Foundations classes at our Southport studio, located at 163 Ferry Rd, Gold Coast. This beginner-friendly yoga class takes a dynamic, fluid approach to yoga practice, building functional strength, flexibility, and body awareness through engaging movement sequences designed for Gold Coast adults of all fitness levels.</p>
    <h3>What Is Flow Yoga - Foundations?</h3>
    <p>Flow Yoga – Foundations is a modern approach to yoga that emphasises fluid movement, controlled transitions, and functional strength over static postures and long holds. Unlike traditional yoga classes on the Gold Coast, Flow Yoga creates a practice that feels active, engaging, and progressive — making it particularly well-suited to Gold Coast adults who want the benefits of yoga but prefer a more dynamic approach.</p>
    <p>Each session at UNDRGRND Movement Southport introduces simple, dynamic sequences that are broken down step by step and accessible to complete beginners. Our Gold Coast instructors guide participants through each movement with clear instruction, ensuring that everyone can follow along and benefit from the practice regardless of prior experience.</p>
    <h3>Why Flow Yoga Is Perfect for Beginners on the Gold Coast</h3>
    <p>Flow Yoga – Foundations at UNDRGRND Movement Southport is specifically designed for Gold Coast adults who are new to yoga or who have found traditional yoga classes too slow or static. The dynamic, movement-based approach creates a practice that feels energetic and engaging while remaining genuinely accessible to beginners.</p>
    <p>Our Southport studio provides a welcoming, supportive environment where Gold Coast participants feel comfortable exploring movement at their own pace. Whether you are a complete beginner or someone who has tried yoga before and found it too passive, Flow Yoga – Foundations offers a fresh and accessible approach to yoga practice on the Gold Coast.</p>
    <h3>The Benefits of Flow Yoga Training</h3>
    <p>Regular practice of Flow Yoga – Foundations at UNDRGRND Movement Southport delivers a wide range of physical benefits. Gold Coast participants report improved flexibility, better functional strength, enhanced coordination, and increased body awareness. The dynamic, movement-based nature of the class creates a well-rounded practice that develops multiple physical qualities simultaneously.</p>
    <p>Beyond the physical, Flow Yoga at our Southport studio provides significant mental benefits. The focused, movement-led nature of the practice encourages participants to stay present and engaged, developing concentration and mental clarity alongside physical fitness. Many Gold Coast participants describe Flow Yoga as a practice that leaves them feeling both energised and centred.</p>
    <h3>Flow Yoga at UNDRGRND Movement Southport, Gold Coast</h3>
    <p>UNDRGRND Movement is located at 163 Ferry Rd, Southport QLD 4215, making it easily accessible to Gold Coast residents from Southport, Surfers Paradise, Broadbeach, Robina, and surrounding suburbs. Our Southport studio is purpose-built for movement classes, providing a welcoming environment for dynamic yoga practice.</p>
    <p>We offer flexible booking options including drop-in classes ($22 per session), 10-class packs ($180), and unlimited monthly memberships ($160 per month). All options can be booked online through our timetable page, making it easy for Gold Coast residents to fit Flow Yoga into their weekly routine.</p>
    <h3>Begin Your Flow Yoga Journey on the Gold Coast</h3>
    <p>If you have been looking for a dynamic, engaging yoga class on the Gold Coast that is accessible and beginner-friendly, Flow Yoga – Foundations at UNDRGRND Movement Southport is the right choice. Join our growing community of Gold Coast yoga students and discover the benefits of a practice that moves, flows, and builds strength in a way that feels natural and sustainable.</p>
    <p>Book your first Flow Yoga class today at UNDRGRND Movement, 163 Ferry Rd, Southport — Gold Coast's home for dynamic, accessible yoga.</p>
  </div>
</section>''',
        'cta_heading': 'Ready to Flow?',
        'cta_sub': 'Join Flow Yoga – Foundations at UNDRGRND Movement Southport. No experience needed — just bring yourself and a willingness to move.',
    })


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3G: aerial-yoga.html → aerial-yoga-foundations.html
# ─────────────────────────────────────────────────────────────────────────────
def task_3g():
    update_simple_page('aerial-yoga.html', 'aerial-yoga-foundations.html', {
        'task': '3G',
        'old_name': 'Aerial Yoga',
        'new_name': 'Aerial Yoga - Foundations',
        'title': 'Aerial Yoga - Foundations | Aerial Fitness Gold Coast | UNDRGRND Movement Southport',
        'meta_desc': 'Supported movement in a hammock at UNDRGRND Movement Southport. Aerial Yoga - Foundations builds flexibility and reduces joint pressure. Beginner-friendly on the Gold Coast.',
        'og_title': 'Aerial Yoga - Foundations | Aerial Fitness Gold Coast | UNDRGRND Movement',
        'og_desc': 'Aerial yoga using a suspended hammock at UNDRGRND Movement Southport. Beginner-friendly aerial fitness on the Gold Coast.',
        'badge': 'Balanced &nbsp;·&nbsp; Beginner Friendly',
        'subtitle': 'Aerial Fitness Gold Coast',
        'hero_sub': 'Explore movement using a suspended hammock in a safe and structured environment. Aerial Yoga – Foundations builds flexibility, mobility, and strength at UNDRGRND Movement Southport.',
        'desc_p1': 'Aerial Yoga – Foundations introduces you to movement using a suspended hammock in a safe and structured environment. The class focuses on improving flexibility, mobility, and strength while reducing pressure on the joints through supported movement.',
        'desc_p2': 'Through simple, guided sequences, the hammock is used to assist stretching, balance, and controlled transitions, allowing you to move with greater ease and confidence. Each session emphasises posture, alignment, and gentle strength work, making movement more accessible while still building control. This class is ideal for beginners with no prior experience who want to explore a supported approach to movement.',
        'core_focus': [
            {'title': 'Supported Movement in Hammock', 'desc': 'Use the hammock to support and enhance your movement, making postures and transitions more accessible and comfortable.'},
            {'title': 'Flexibility and Mobility', 'desc': 'Improve flexibility and range of motion through supported stretching and guided movement sequences in the hammock.'},
            {'title': 'Reduced Joint Pressure', 'desc': 'Experience the benefits of movement with reduced impact on your joints, making this class ideal for all bodies and fitness levels.'},
            {'title': 'Posture and Alignment', 'desc': 'Develop better posture and body alignment through supported movement that encourages correct positioning and control.'},
        ],
        'related': [
            {'url': '/programs/aerial-silks-foundations.html', 'badge': 'Aerial', 'name': 'Aerial Silks - Foundations', 'desc': 'Learn aerial movement using suspended fabric in a safe and structured environment.'},
            {'url': '/programs/fusion-yoga-foundations.html', 'badge': 'Yoga', 'name': 'Fusion Yoga - Foundations', 'desc': 'Blend traditional yoga with modern movement for mobility and strength.'},
            {'url': '/programs/movement-flow-foundations.html', 'badge': 'Movement', 'name': 'Movement Flow - Foundations', 'desc': 'Reconnect with your body through fluid, natural movement in a calm and supportive environment.'},
        ],
        'seo_section': '''<section class="seo-content" aria-label="About Aerial Yoga on the Gold Coast">
  <div class="seo-content__inner">
    <h2>Aerial Yoga on the Gold Coast — Beginner-Friendly Classes at UNDRGRND Movement Southport</h2>
    <p>UNDRGRND Movement offers Aerial Yoga – Foundations classes at our Southport studio, located at 163 Ferry Rd, Gold Coast. This beginner-friendly aerial yoga class introduces movement using a suspended hammock in a safe and structured environment, providing Gold Coast participants with a unique and accessible approach to improving flexibility, mobility, and strength.</p>
    <h3>What Is Aerial Yoga - Foundations?</h3>
    <p>Aerial Yoga – Foundations uses a suspended fabric hammock to support and enhance yoga-based movement. Unlike traditional yoga classes on the Gold Coast, aerial yoga allows participants to explore postures and transitions with the assistance of the hammock, reducing joint pressure and making movement more accessible for a wider range of bodies and fitness levels.</p>
    <p>Each session at UNDRGRND Movement Southport introduces simple, guided sequences that use the hammock to assist stretching, balance, and controlled transitions. Our Gold Coast instructors guide participants through each movement with clear, supportive instruction, ensuring that beginners feel safe and confident from their very first class.</p>
    <h3>Why Aerial Yoga Is Perfect for Beginners on the Gold Coast</h3>
    <p>Aerial Yoga – Foundations at UNDRGRND Movement Southport is specifically designed for Gold Coast adults who are new to aerial movement or who want a gentler, more supported approach to yoga and movement. The hammock provides physical support that makes postures and transitions more accessible, allowing beginners to experience the benefits of aerial movement without the strength or flexibility requirements of more advanced aerial disciplines.</p>
    <p>Our Southport studio provides a safe, welcoming environment where Gold Coast participants feel comfortable exploring aerial movement at their own pace. All equipment is provided, and our instructors ensure that every participant understands how to use the hammock safely before beginning any sequences.</p>
    <h3>The Benefits of Aerial Yoga Training</h3>
    <p>Regular practice of Aerial Yoga – Foundations at UNDRGRND Movement Southport delivers a wide range of physical benefits. Gold Coast participants report improved flexibility, better posture, increased body awareness, and reduced joint discomfort. The supported nature of aerial yoga makes it particularly beneficial for those with joint sensitivity or those who find traditional yoga challenging due to limited flexibility.</p>
    <p>Beyond the physical, Aerial Yoga at our Southport studio provides a unique and enjoyable movement experience that many Gold Coast participants find both calming and invigorating. The sensation of supported movement in the hammock creates a practice that is unlike any other fitness class on the Gold Coast, making it a memorable and rewarding addition to any movement routine.</p>
    <h3>Aerial Yoga at UNDRGRND Movement Southport, Gold Coast</h3>
    <p>UNDRGRND Movement is located at 163 Ferry Rd, Southport QLD 4215, making it easily accessible to Gold Coast residents from Southport, Surfers Paradise, Broadbeach, Robina, and surrounding suburbs. Our Southport studio is equipped with professional aerial rigging and hammocks, providing a safe and purpose-built environment for aerial yoga practice.</p>
    <p>We offer flexible booking options including drop-in classes ($30 per session), 10-class packs ($250), and unlimited monthly memberships ($220 per month). All options can be booked online through our timetable page, making it easy for Gold Coast residents to fit Aerial Yoga into their weekly routine.</p>
    <h3>Begin Your Aerial Yoga Journey on the Gold Coast</h3>
    <p>If you have been curious about aerial yoga on the Gold Coast and are looking for a safe, beginner-friendly introduction, Aerial Yoga – Foundations at UNDRGRND Movement Southport is the right starting point. Join our growing community of Gold Coast aerial students and discover the unique benefits of supported movement in the hammock.</p>
    <p>Book your first Aerial Yoga class today at UNDRGRND Movement, 163 Ferry Rd, Southport — Gold Coast's home for accessible aerial yoga.</p>
  </div>
</section>''',
        'cta_heading': 'Ready to Take Flight?',
        'cta_sub': 'Join Aerial Yoga – Foundations at UNDRGRND Movement Southport. No experience needed — all equipment provided.',
    })


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3I: choreography-fusion.html → choreography-fusion-foundations.html
# ─────────────────────────────────────────────────────────────────────────────
def task_3i():
    update_simple_page('choreography-fusion.html', 'choreography-fusion-foundations.html', {
        'task': '3I',
        'old_name': 'Choreography Fusion',
        'new_name': 'Choreography Fusion - Foundations',
        'title': 'Choreography Fusion - Foundations | Dance Classes Gold Coast | UNDRGRND Movement Southport',
        'meta_desc': 'Build confidence through simple, guided choreography at UNDRGRND Movement Southport. Choreography Fusion - Foundations is beginner-friendly on the Gold Coast.',
        'og_title': 'Choreography Fusion - Foundations | Dance Classes Gold Coast | UNDRGRND Movement',
        'og_desc': 'Build confidence through simple, guided choreography at UNDRGRND Movement Southport. Beginner-friendly dance classes on the Gold Coast.',
        'badge': 'Balanced &nbsp;·&nbsp; Beginner Friendly',
        'subtitle': 'Dance Classes Gold Coast',
        'hero_sub': 'Build confidence through simple, guided movement sequences at UNDRGRND Movement Southport. Choreography Fusion – Foundations is beginner-friendly and welcoming on the Gold Coast.',
        'desc_p1': 'Choreography Fusion – Foundations is a beginner-friendly class designed to help you build confidence through simple, guided movement sequences. The focus is on learning short, easy-to-follow choreography while developing coordination, timing, and body awareness in a supportive environment.',
        'desc_p2': 'Blending elements from different movement styles, each session introduces structured combinations that are broken down step by step, making them accessible even if you have no prior experience. The emphasis is on moving with clarity and confidence, without pressure to perform or get everything perfect. Through each curated, smooth, and authentic movement, you will become more comfortable learning and remembering movement while building confidence in how you move.',
        'core_focus': [
            {'title': 'Short, Easy-to-Follow Choreography', 'desc': 'Learn simple, structured movement sequences that are broken down step by step and accessible to complete beginners.'},
            {'title': 'Coordination and Timing', 'desc': 'Develop coordination and timing through guided choreography that builds your ability to move with clarity and intention.'},
            {'title': 'Body Awareness', 'desc': 'Build a deeper awareness of how your body moves through structured sequences that develop spatial awareness and control.'},
            {'title': 'Confidence Building', 'desc': 'Grow your confidence in movement through a supportive, non-judgmental environment at our Southport studio.'},
        ],
        'related': [
            {'url': '/programs/afro-groove-foundations.html', 'badge': 'Dance', 'name': 'Afro Groove Foundations', 'desc': 'Beginner-friendly dance fitness inspired by Afrobeat and groove-based styles.'},
            {'url': '/programs/booty-burn-foundations.html', 'badge': 'Dance Fitness', 'name': 'Booty Burn - Foundations', 'desc': 'High-energy dance fitness focused on lower body strength and glute activation.'},
            {'url': '/programs/movement-flow-foundations.html', 'badge': 'Movement', 'name': 'Movement Flow - Foundations', 'desc': 'Reconnect with your body through fluid, natural movement in a calm and supportive environment.'},
        ],
        'seo_section': '''<section class="seo-content" aria-label="About Choreography Fusion on the Gold Coast">
  <div class="seo-content__inner">
    <h2>Choreography Fusion on the Gold Coast — Build Confidence Through Movement at UNDRGRND Movement Southport</h2>
    <p>UNDRGRND Movement offers Choreography Fusion – Foundations classes at our Southport studio, located at 163 Ferry Rd, Gold Coast. This beginner-friendly dance class is designed to help Gold Coast adults build confidence through simple, guided movement sequences that blend elements from different dance styles into an accessible and engaging practice.</p>
    <h3>What Is Choreography Fusion - Foundations?</h3>
    <p>Choreography Fusion – Foundations is a structured beginner class that focuses on learning short, easy-to-follow choreography in a supportive and non-judgmental environment. Unlike performance-focused dance classes on the Gold Coast, Choreography Fusion prioritises the learning process over the end result — the goal is to help participants become more comfortable with movement, not to prepare them for a performance.</p>
    <p>Each session at UNDRGRND Movement Southport introduces structured movement combinations that are broken down step by step, making them accessible even for complete beginners. Our Gold Coast instructors guide participants through each sequence with clear, patient instruction, ensuring that everyone can follow along and build confidence at their own pace.</p>
    <h3>Why Choreography Fusion Is Perfect for Beginners on the Gold Coast</h3>
    <p>Choreography Fusion – Foundations at UNDRGRND Movement Southport is specifically designed for Gold Coast adults who have always wanted to learn choreography but have felt intimidated by traditional dance classes. The structured, step-by-step approach removes the pressure of keeping up and creates a learning environment where mistakes are part of the process.</p>
    <p>Our Southport studio provides a welcoming, encouraging environment where Gold Coast participants feel comfortable learning at their own pace. Whether you are a complete beginner, someone who has tried dance before and found it too fast-paced, or simply looking for a fun and engaging way to move on the Gold Coast, Choreography Fusion – Foundations offers a genuinely accessible starting point.</p>
    <h3>The Benefits of Choreography-Based Movement</h3>
    <p>Regular practice of Choreography Fusion – Foundations at UNDRGRND Movement Southport delivers a wide range of physical and mental benefits. Gold Coast participants report improved coordination, better timing, increased body awareness, and a growing sense of confidence in how they move. The structured, sequential nature of choreography learning also develops memory, focus, and cognitive agility.</p>
    <p>Beyond the physical and cognitive, Choreography Fusion at our Southport studio provides significant emotional benefits. Learning to move with confidence and intention is a deeply empowering experience, and many Gold Coast participants describe their Choreography Fusion journey as transformative — not because they became dancers, but because they discovered a new relationship with their bodies and their capacity to learn.</p>
    <h3>Choreography Fusion at UNDRGRND Movement Southport, Gold Coast</h3>
    <p>UNDRGRND Movement is located at 163 Ferry Rd, Southport QLD 4215, making it easily accessible to Gold Coast residents from Southport, Surfers Paradise, Broadbeach, Robina, and surrounding suburbs. Our Southport studio is purpose-built for movement classes, providing a welcoming and supportive environment for choreography learning.</p>
    <p>We offer flexible booking options including drop-in classes ($25 per session), 10-class packs ($200), and unlimited monthly memberships ($180 per month). All options can be booked online through our timetable page, making it easy for Gold Coast residents to fit Choreography Fusion into their weekly routine.</p>
    <h3>Begin Your Choreography Journey on the Gold Coast</h3>
    <p>If you have been looking for a dance class on the Gold Coast that is structured, accessible, and genuinely beginner-friendly, Choreography Fusion – Foundations at UNDRGRND Movement Southport is the right choice. Join our growing community of Gold Coast movers and discover the confidence that comes from learning to move with intention and clarity.</p>
    <p>Book your first Choreography Fusion class today at UNDRGRND Movement, 163 Ferry Rd, Southport — Gold Coast's home for accessible, confidence-building choreography.</p>
  </div>
</section>''',
        'cta_heading': 'Ready to Build Your Confidence?',
        'cta_sub': 'Join Choreography Fusion – Foundations at UNDRGRND Movement Southport. No experience needed — just bring yourself and a willingness to learn.',
    })


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3H: aerial-silks.html — update in place (add Foundations to H1/title)
# ─────────────────────────────────────────────────────────────────────────────
def task_3h():
    print('\n[3H] Aerial Silks — update in place (add Foundations)')
    src = f'{BASE}/aerial-silks.html'
    dst = f'{BASE}/aerial-silks-foundations.html'
    html = read(src)

    # Head
    html = update_head(html,
        title='Aerial Silks - Foundations | Aerial Arts Gold Coast | UNDRGRND Movement Southport',
        meta_desc='Learn aerial silks in a safe, progressive environment at UNDRGRND Movement Southport. Aerial Silks - Foundations for beginners on the Gold Coast.',
        canonical_url='https://www.undrgrnd.com.au/programs/aerial-silks-foundations.html',
        og_title='Aerial Silks - Foundations | Aerial Arts Gold Coast | UNDRGRND Movement',
        og_desc='Beginner aerial silks classes at UNDRGRND Movement Southport. Safe, progressive aerial arts training on the Gold Coast.',
        og_url='https://www.undrgrnd.com.au/programs/aerial-silks-foundations.html'
    )

    # H1
    html = html.replace(
        '<h1 class="prog-hero__h1">Aerial Silks | Aerial Arts Classes Gold Coast</h1>',
        '<h1 class="prog-hero__h1">Aerial Silks - Foundations | Aerial Arts Gold Coast</h1>'
    )

    # Level badge
    html = html.replace(
        '<span class="prog-hero__level" id="heroLevel">All Levels — Beginner Friendly</span>',
        '<span class="prog-hero__level" id="heroLevel">Beginner / Foundation — Balanced</span>'
    )

    # Overview H2
    html = html.replace('<h2 id="overviewHeading">Aerial Silks</h2>', '<h2 id="overviewHeading">Aerial Silks - Foundations</h2>')

    # Overview description
    html = html.replace(
        '<p class="overview-section__desc" id="programDesc">\n        Aerial Silks is a strength and flexibility discipline performed on suspended fabric. Students learn to climb, wrap, and perform controlled movements using two lengths of fabric hung from a rigging point. Classes focus on safe technique, progressive skill-building, and body conditioning. Suitable for beginners with no prior aerial experience — all equipment is provided and classes are structured to build confidence and strength from the ground up.\n      </p>',
        '<p class="overview-section__desc" id="programDesc">\n        Aerial Silks – Foundations introduces you to aerial movement using suspended fabric in a safe and structured environment. The class focuses on building strength, coordination, and body awareness while learning to move with control and confidence off the ground. Through simple, guided techniques such as basic grips, supported holds, and low-level movements, you will develop upper body strength, core stability, and coordination at a comfortable pace.\n      </p>'
    )

    # Schema breadcrumb
    html = html.replace(
        "{ name: 'Aerial Silks', url: 'https://www.undrgrnd.com.au/programs/aerial-silks.html' }",
        "{ name: 'Aerial Silks - Foundations', url: 'https://www.undrgrnd.com.au/programs/aerial-silks-foundations.html' }"
    )

    # Fix booking URLs
    html = fix_booking_urls(html)

    write(dst, html)
    print(f'  [OK] {dst}')


# ─────────────────────────────────────────────────────────────────────────────
# TASK 3J: pole-fitness-foundations.html — add Coming Soon badge, update content
# ─────────────────────────────────────────────────────────────────────────────
def task_3j():
    print('\n[3J] Pole Fitness Foundations — add Coming Soon, update content')
    src = f'{BASE}/pole-fitness-foundations.html'
    dst = src  # update in place
    html = read(src)

    # Add Coming Soon badge to hero level
    html = html.replace(
        '<span class="prog-hero__level" id="heroLevel">Beginner / Foundation</span>',
        '<span class="prog-hero__level" id="heroLevel">Beginner / Foundation</span>\n    <span class="prog-hero__level" style="background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.4);color:#F59E0B;margin-top:0.5rem;display:inline-block;">Coming Soon</span>'
    )

    # Update overview description
    html = html.replace(
        '<p class="overview-section__desc" id="programDesc">\n        Pole Fitness – Foundations is a structured beginner program that introduces students to the fundamentals of pole fitness as a sport. Classes cover grip techniques, basic walks, entry-level spins, and safe body positioning around the pole. All movements are taught with a focus on control, safety, and progressive strength development. No prior experience is required — this program is designed for absolute beginners who want to learn pole fitness from the ground up in a supportive, non-judgmental environment.\n      </p>',
        '<p class="overview-section__desc" id="programDesc">\n        Pole Fitness – Foundations is a beginner-friendly class designed to introduce you to pole movement in a safe, structured environment. The class focuses on developing grip strength, body awareness, and basic technique through low-level spins, walking patterns, and controlled movements around the pole. Through each curated, smooth, and authentic movement, you will build upper body strength, core stability, and coordination at a comfortable pace. No prior experience is required — this program is designed for absolute beginners who want to learn pole fitness from the ground up.\n      </p>'
    )

    # Update CTA buttons to Join Waitlist
    html = html.replace(
        '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="cta-button">Book Your First Pole Fitness Class</a>',
        '<a href="mailto:undrgrndgc@gmail.com?subject=Pole%20Fitness%20Foundations%20Waitlist" class="cta-button">Join Waitlist</a>'
    )

    # Fix booking URLs
    html = fix_booking_urls(html)

    write(dst, html)
    print(f'  [OK] {dst} (updated in place)')


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('=== UNDRGRND Movement — Step 3: Update Program Pages ===\n')
    task_3a()
    task_3b()
    task_3c()
    task_3d()
    task_3e()
    task_3f()
    task_3g()
    task_3h()
    task_3i()
    task_3j()
    print('\n=== All tasks complete ===')
