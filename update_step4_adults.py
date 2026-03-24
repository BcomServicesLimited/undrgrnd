#!/usr/bin/env python3
"""Step 4A: Update adults.html with intensity section, coming-soon states, and SEO updates."""

with open('adults.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. Add CSS for intensity section and coming-soon badge
# ============================================================
intensity_css = """
    /* -----------------------------------------------------------------------
       INTENSITY GROUPS SECTION
    ----------------------------------------------------------------------- */
    .intensity-groups {
      padding: 4rem 1.5rem;
      background: rgba(139, 92, 246, 0.03);
      border-bottom: 1px solid rgba(139, 92, 246, 0.1);
    }
    .intensity-groups .container {
      max-width: 1200px;
      margin: 0 auto;
    }
    .intensity-groups h2 {
      font-family: 'Outfit', sans-serif;
      font-size: clamp(1.6rem, 3vw, 2.2rem);
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 0.75rem;
    }
    .intensity-groups .section-intro {
      color: #A1A1A1;
      font-size: 1rem;
      max-width: 640px;
      margin-bottom: 2.5rem;
      line-height: 1.7;
    }
    .intensity-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      margin: 2rem 0;
    }
    .intensity-card {
      background: #1A1A1A;
      border-radius: 20px;
      padding: 2rem;
      border: 1px solid rgba(139, 92, 246, 0.2);
    }
    .intensity-badge {
      display: inline-block;
      padding: 0.5rem 1rem;
      border-radius: 20px;
      font-weight: 600;
      font-size: 0.9rem;
      margin-bottom: 1rem;
    }
    .intensity-badge.dynamic {
      background: rgba(236, 72, 153, 0.2);
      color: #EC4899;
    }
    .intensity-badge.balanced {
      background: rgba(139, 92, 246, 0.2);
      color: #8B5CF6;
    }
    .intensity-badge.gentle {
      background: rgba(167, 139, 250, 0.2);
      color: #A78BFA;
    }
    .intensity-card h3 {
      color: #FFFFFF;
      font-family: 'Outfit', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
      margin: 1rem 0 0.5rem;
    }
    .intensity-card p {
      color: #A1A1A1;
      font-size: 0.9rem;
      line-height: 1.6;
      margin-bottom: 1rem;
    }
    .intensity-card ul {
      list-style: none;
      padding: 0;
      margin: 1rem 0;
    }
    .intensity-card ul li {
      padding: 0.5rem 0;
      color: #A1A1A1;
      font-size: 0.9rem;
      border-bottom: 1px solid rgba(139, 92, 246, 0.1);
    }
    .intensity-card ul li:last-child {
      border-bottom: none;
    }
    .intensity-groups .note {
      color: #A1A1A1;
      font-size: 0.85rem;
      font-style: italic;
      margin-top: 1.5rem;
      padding: 1rem 1.25rem;
      background: rgba(139, 92, 246, 0.05);
      border-left: 3px solid rgba(139, 92, 246, 0.3);
      border-radius: 0 8px 8px 0;
    }
    /* Coming Soon badge */
    .badge--coming-soon {
      background: rgba(245, 158, 11, 0.15);
      color: #FBBF24;
      border-color: rgba(245, 158, 11, 0.25);
    }
    .btn-learn.disabled {
      opacity: 0.5;
      cursor: not-allowed;
      pointer-events: none;
    }
    /* Intensity badge on program cards */
    .intensity-badge-card {
      display: inline-block;
      font-family: 'Outfit', sans-serif;
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 0.22rem 0.7rem;
      border-radius: 50px;
      border: 1px solid;
      width: fit-content;
      margin-top: 0.3rem;
    }
    .intensity-badge-card.dynamic {
      background: rgba(236, 72, 153, 0.12);
      color: #EC4899;
      border-color: rgba(236, 72, 153, 0.25);
    }
    .intensity-badge-card.balanced {
      background: rgba(139, 92, 246, 0.12);
      color: #A78BFA;
      border-color: rgba(139, 92, 246, 0.25);
    }
    .intensity-badge-card.gentle {
      background: rgba(167, 139, 250, 0.12);
      color: #A78BFA;
      border-color: rgba(167, 139, 250, 0.25);
    }
"""

# Insert intensity CSS before the closing </style> of the page-specific styles block
# Find the first </style> tag after the page-specific styles comment
style_insert_marker = "    /* -----------------------------------------------------------------------\n       BEGINNER-FRIENDLY SECTION"
html = html.replace(style_insert_marker, intensity_css + "\n    /* -----------------------------------------------------------------------\n       BEGINNER-FRIENDLY SECTION", 1)

# ============================================================
# 2. Add intensity groups section HTML after hero, before filter section
# ============================================================
intensity_section_html = """<!-- =========================================================================
     1B. INTENSITY GROUPS SECTION
     ========================================================================= -->
<section class="intensity-groups" aria-labelledby="intensityHeading">
  <div class="container">
    <h2 id="intensityHeading">Find Your Perfect Intensity</h2>
    <p class="section-intro">
      We group our adult programs by intensity and target age to help you find classes that match your energy and goals on the Gold Coast.
    </p>

    <div class="intensity-grid">

      <div class="intensity-card">
        <div class="intensity-badge dynamic">Dynamic / High Energy</div>
        <h3>16-25 (Young Adults)</h3>
        <p>Fast-paced, energetic classes for younger adults seeking dynamic movement and high-intensity workouts at UNDRGRND Movement Southport.</p>
        <ul>
          <li>Afro Groove - Foundations</li>
          <li>Booty Burn - Foundations</li>
        </ul>
      </div>

      <div class="intensity-card">
        <div class="intensity-badge balanced">Balanced / Flow</div>
        <h3>26-45 (General Adults)</h3>
        <p>Moderate intensity with emphasis on flow, technique, and sustainable movement practice on the Gold Coast.</p>
        <ul>
          <li>Movement Flow - Foundations</li>
          <li>Pole Fitness - Foundations (Coming Soon)</li>
          <li>Pole Flow - Foundations (Coming Soon)</li>
          <li>Fusion Yoga - Foundations</li>
          <li>Traditional Yoga - Foundations</li>
          <li>Flow Yoga - Foundations</li>
          <li>Aerial Yoga - Foundations</li>
          <li>Aerial Silks - Foundations</li>
          <li>Choreography Fusion - Foundations</li>
        </ul>
      </div>

      <div class="intensity-card">
        <div class="intensity-badge gentle">Gentle / Slow</div>
        <h3>45+ (Gentle / Recovery)</h3>
        <p>Low-impact, supportive classes for gentle movement and safe return to training at UNDRGRND Movement Southport.</p>
        <ul>
          <li>Recovery Movement Flow - Foundations (Coming Soon)</li>
        </ul>
      </div>

    </div>

    <p class="note">
      These are recommendations based on typical energy levels. All adults are welcome in any class that appeals to them — choose based on what feels right for your body and goals.
    </p>
  </div>
</section>
"""

# Insert after the hero section closing comment, before the filter section comment
filter_comment = "<!-- =========================================================================\n     2. PROGRAM FILTER"
html = html.replace(filter_comment, intensity_section_html + filter_comment, 1)

# ============================================================
# 3. Update buildProgramCard JS to add intensity badges and coming-soon states
# ============================================================
old_medical_badge_block = """    /* Medical badge */
    var medicalBadge = isMedical
      ? '<span class="medical-badge"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>Medical Clearance Required</span>'
      : '';
    /* Book Now button — triggers modal for recovery classes */
    var bookBtn = isMedical
      ? '<button class="btn-book" data-medical="true" type="button">Book Now</button>'
      : '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="btn-book">Book Now</a>';
    return '<article class="program-card program-card--' + meta.cls + ' reveal" data-category="' + catKey + '">'
      + '<div class="program-card__img">'
      +   '<img src="/images/hero/' + escHtml(slug) + '.webp" alt="' + escHtml(program.name) + ' class at UNDRGRND Movement Gold Coast" loading="lazy" width="600" height="338">'
      + '</div>'
      + '<div class="program-card__body">'
      +   '<span class="program-badge badge--' + meta.cls + '">' + escHtml(meta.label) + '</span>'
      +   (medicalBadge ? medicalBadge : '')
      +   '<h3 class="program-card__name">' + escHtml(program.name) + '</h3>'
      +   (program.level ? '<p class="program-card__level">' + escHtml(program.level) + '</p>' : '')
      +   '<p class="program-card__desc">' + escHtml(program.short_description || '') + '</p>'
      +   (focusItems ? '<ul class="program-card__focus">' + focusItems + '</ul>' : '')
      +   priceHtml
      + '</div>'
      + '<div class="program-card__actions">'
      +   '<a href="/programs/' + escHtml(slug) + '.html" class="btn-learn">Learn More</a>'
      +   bookBtn
      + '</div>'
      + '</article>';"""

new_medical_badge_block = """    /* Medical badge */
    var medicalBadge = isMedical
      ? '<span class="medical-badge"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>Medical Clearance Required</span>'
      : '';
    /* Coming Soon badge */
    var isComingSoon = program.status === 'coming_soon';
    var comingSoonBadge = isComingSoon
      ? '<span class="program-badge badge--coming-soon">Coming Soon</span>'
      : '';
    /* Intensity badge */
    var intensityMap = {
      'Active':   { cls: 'dynamic',  label: 'Dynamic / High Energy' },
      'Balanced': { cls: 'balanced', label: 'Balanced / Flow' },
      'Moderate': { cls: 'balanced', label: 'Balanced / Flow' },
      'Gentle':   { cls: 'gentle',   label: 'Gentle / Slow' }
    };
    var intensityInfo = intensityMap[program.intensity] || null;
    var intensityBadgeHtml = intensityInfo
      ? '<span class="intensity-badge-card ' + intensityInfo.cls + '">' + intensityInfo.label + '</span>'
      : '';
    /* Book Now button — triggers modal for recovery classes; disabled for coming soon */
    var bookBtn = isComingSoon
      ? '<a href="mailto:undrgrndgc@gmail.com?subject=Waitlist for ' + escHtml(program.name) + '" class="btn-learn">Join Waitlist</a>'
      : (isMedical
          ? '<button class="btn-book" data-medical="true" type="button">Book Now</button>'
          : '<a href="https://app.classmanager.com/portal/undrgrnd-movement/register" class="btn-book">Book Now</a>');
    var learnBtn = isComingSoon
      ? '<a href="#" class="btn-learn disabled" aria-disabled="true">Coming Soon</a>'
      : '<a href="/programs/' + escHtml(slug) + '.html" class="btn-learn">Learn More</a>';
    return '<article class="program-card program-card--' + meta.cls + ' reveal" data-category="' + catKey + '">'
      + '<div class="program-card__img">'
      +   '<img src="/images/hero/' + escHtml(slug) + '.webp" alt="' + escHtml(program.name) + ' class at UNDRGRND Movement Gold Coast" loading="lazy" width="600" height="338">'
      + '</div>'
      + '<div class="program-card__body">'
      +   '<span class="program-badge badge--' + meta.cls + '">' + escHtml(meta.label) + '</span>'
      +   (comingSoonBadge ? comingSoonBadge : '')
      +   (medicalBadge ? medicalBadge : '')
      +   intensityBadgeHtml
      +   '<h3 class="program-card__name">' + escHtml(program.name) + '</h3>'
      +   (program.level ? '<p class="program-card__level">' + escHtml(program.level) + '</p>' : '')
      +   '<p class="program-card__desc">' + escHtml(program.short_description || '') + '</p>'
      +   (focusItems ? '<ul class="program-card__focus">' + focusItems + '</ul>' : '')
      +   priceHtml
      + '</div>'
      + '<div class="program-card__actions">'
      +   learnBtn
      +   bookBtn
      + '</div>'
      + '</article>';"""

if old_medical_badge_block in html:
    html = html.replace(old_medical_badge_block, new_medical_badge_block, 1)
    print("JS buildProgramCard updated")
else:
    print("WARNING: Could not find old_medical_badge_block in adults.html")

# ============================================================
# 4. Update SEO section
# ============================================================
old_seo = """<section class="seo-section reveal" aria-labelledby="seoHeading">
  <div class="seo-section__inner">
    <h2 id="seoHeading">Transform Your Body and Mind with Adult Movement Classes on the Gold Coast</h2>
    <p>
      Finding the right movement practice as an adult on the Gold Coast can feel overwhelming. Gyms, fitness studios, and dance schools all promise results — but very few offer the kind of personalised, beginner-friendly environment that actually supports long-term change. <strong>UNDRGRND Movement</strong> in Southport is different. Our adult movement classes are built around one principle: personal transformation over performance. Whether you are stepping into a studio for the first time or returning to movement after years away, our Gold Coast classes meet you exactly where you are.
    </p>
    <h3>Why Adults Choose UNDRGRND Movement in Southport</h3>
    <p>
      Adults across the Gold Coast choose UNDRGRND Movement because our approach is genuinely inclusive. We do not run competitive classes. We do not push students beyond their limits. Instead, our qualified instructors build structured, progressive programs that develop real movement skills at a pace that works for each individual. Our Southport studio is conveniently located for residents of Surfers Paradise, Broadbeach, Bundall, Main Beach, and the broader Gold Coast region.
    </p>
    <p>
      Every adult program at UNDRGRND Movement begins with foundations. Before you learn to flow, spin, or fly, you learn to move safely and with confidence. This approach dramatically reduces injury risk and builds the kind of body awareness that carries over into everyday life. It is not just about fitness — it is about learning to inhabit your body with more ease, strength, and joy.
    </p>
    <h3>Adult Dance Classes on the Gold Coast</h3>
    <p>
      Our adult dance programs are among the most popular offerings at our Southport studio. <strong>Afro Groove Foundations</strong> is a beginner-friendly dance fitness class inspired by Afrobeat and groove-based movement styles. It builds rhythm, coordination, lower body strength, and core stability through simple, repeatable patterns. No prior dance experience is required. <strong>Movement Dance</strong> takes a more expressive approach, helping students build body flow and confidence through creative movement exploration. Both classes are open to adults of all fitness levels across the Gold Coast.
    </p>
    <p>
      For adults interested in choreography, our <strong>Choreography Fusion</strong> class blends movement and confidence-building through structured dance sequences. This class is particularly popular among women on the Gold Coast who want to explore movement as a form of self-expression in a supportive, non-competitive environment.
    </p>
    <h3>Pole Fitness Classes for Adults in Southport</h3>
    <p>
      Pole fitness is one of the most effective full-body workouts available to adults on the Gold Coast. Our <strong>Pole Fitness Foundations</strong> class is designed for complete beginners and teaches grip techniques, basic spins, body positioning, and safety protocols in a structured, supportive environment. As students progress, they can move into <strong>Pole Flow</strong> — developing smooth transitions and flowing movement — and <strong>Pole Strength and Movement</strong>, which focuses on conditioning, holds, and controlled technique.
    </p>
    <p>
      All pole fitness classes at our Southport studio are taught by qualified instructors with a strong emphasis on safety and individual progression. Adults from across the Gold Coast, including Surfers Paradise and Broadbeach, regularly attend our pole fitness classes. No prior experience is needed to begin, and our instructors ensure every student feels comfortable and supported from their very first class.
    </p>
    <h3>Yoga Classes for Adults on the Gold Coast</h3>
    <p>
      UNDRGRND Movement offers a comprehensive range of adult yoga classes in Southport. Our yoga timetable includes <strong>Traditional Yoga</strong> for those seeking classical techniques, <strong>Modern Yoga</strong> for a contemporary approach, <strong>Yoga Fusion</strong> which blends traditional and contemporary movement, and <strong>Aerial Yoga</strong> — a unique practice performed in suspended silk hammocks that provides deep decompression and a completely different relationship with gravity.
    </p>
    <p>
      All yoga classes at our Gold Coast studio are suitable for all levels. Whether you are a complete beginner or an experienced practitioner, our Southport yoga classes provide a calm, welcoming environment focused on body-mind connection rather than performance or competition.
    </p>
    <h3>Aerial Arts for Adults — Silks and Aerial Yoga on the Gold Coast</h3>
    <p>
      <strong>Aerial Silks</strong> is one of the most visually stunning and physically rewarding movement practices available to adults on the Gold Coast. Students learn to climb, wrap, and create shapes using suspended fabric, building upper body strength, core stability, and spatial awareness. Our beginner-friendly Aerial Silks class in Southport provides step-by-step instruction with individual spotting and attention. No prior experience is required — just a willingness to challenge yourself and trust the process.
    </p>
    <h3>Recovery Movement — Specialised Adult Classes in Southport</h3>
    <p>
      UNDRGRND Movement is one of the only Gold Coast studios to offer a dedicated <strong>Recovery Movement Dance</strong> program for adults. This specialised class supports individuals returning to movement after injury, surgery, or extended periods of physical or emotional stress. Using slow, mindful movement with controlled range of motion, the program provides a safe, supported pathway back to physical activity. Medical clearance from a healthcare provider is required before participating.
    </p>
    <p>
      Our recovery movement approach is trauma-informed and developed in collaboration with registered counsellors. This makes UNDRGRND Movement a genuinely unique offering on the Gold Coast — a studio that treats movement as both a physical and emotional practice, with the professional support structures to match.
    </p>
    <h3>Serving Adults Across the Gold Coast</h3>
    <p>
      UNDRGRND Movement's Southport studio is accessible to adults from across the Gold Coast, including Surfers Paradise, Broadbeach, Bundall, Main Beach, and surrounding suburbs. Our multi-environment approach means that some classes also take place in local parks and on the beaches of the Gold Coast, offering a movement experience that goes beyond the traditional studio setting.
    </p>
    <div class="seo-section__cta-text">
      Ready to start your movement journey? <a href="/timetable.html">View our adult class timetable</a> or <a href="/contact.html">contact our Southport studio today</a>.
    </div>
  </div>
</section>"""

new_seo = """<section class="seo-section reveal" aria-labelledby="seoHeading">
  <div class="seo-section__inner">
    <h2 id="seoHeading">Adult Movement Classes on the Gold Coast — Dance, Pole, Yoga &amp; Aerial at UNDRGRND Movement Southport</h2>
    <p>
      <strong>UNDRGRND Movement</strong> in Southport offers beginner-friendly adult classes across dance, pole fitness, yoga, and aerial disciplines on the Gold Coast. Our foundation programs are designed for complete beginners, with intensity levels to match your energy and goals. Whether you are 16 or 65, returning after years away or stepping into a studio for the first time, our Gold Coast classes meet you exactly where you are.
    </p>
    <h3>Dynamic / High Energy Classes (16-25 Young Adults)</h3>
    <p>
      For younger adults seeking fast-paced, energetic movement on the Gold Coast, our Dynamic classes deliver. <strong>Afro Groove - Foundations</strong> combines Afrobeat rhythms with full-body dance fitness, building rhythm, coordination, lower body strength, and core stability through simple, repeatable patterns. No prior dance experience is required. Our new <strong>Booty Burn - Foundations</strong> targets lower body strength through groove-based movement — a fun, music-driven class that works glutes, hips, and core while developing coordination and body confidence. Both classes at our Southport studio are open to adults of all fitness levels across the Gold Coast.
    </p>
    <h3>Balanced / Flow Classes (26-45 General Adults)</h3>
    <p>
      Our Balanced intensity classes suit adults seeking moderate-paced movement with emphasis on technique and flow. <strong>Movement Flow - Foundations</strong> teaches natural movement principles for body confidence and expressive movement. <strong>Pole Fitness - Foundations</strong> and <strong>Pole Flow - Foundations</strong> (both coming soon to our Southport studio) introduce pole movement safely, building grip technique, body positioning, and flowing transitions. Adults from across the Gold Coast, including Surfers Paradise, Broadbeach, and Bundall, regularly attend our pole fitness classes.
    </p>
    <p>
      Our yoga offerings each bring different approaches to building strength and flexibility on the Gold Coast. <strong>Fusion Yoga - Foundations</strong> blends traditional yoga with contemporary movement for a dynamic practice. <strong>Traditional Yoga - Foundations</strong> follows classical sequences for those seeking a grounded, classical approach. <strong>Flow Yoga - Foundations</strong> takes a contemporary approach with fluid, connected sequences. <strong>Aerial Yoga - Foundations</strong> uses suspended silk hammocks for a unique, decompressive practice. <strong>Aerial Silks - Foundations</strong> builds upper body strength, core stability, and spatial awareness through suspended fabric work. <strong>Choreography Fusion - Foundations</strong> builds coordination and confidence through accessible, structured dance sequences at UNDRGRND Movement Southport.
    </p>
    <h3>Gentle / Slow Classes (45+ Recovery)</h3>
    <p>
      <strong>Recovery Movement Flow - Foundations</strong> (coming soon) supports safe return to movement after injury or extended breaks. This gentle class in Southport requires medical clearance and focuses on slow, controlled sequences that rebuild trust in your body. Perfect for adults on the Gold Coast recovering from injury, managing physical limitations, or simply seeking a more supportive and mindful approach to movement. UNDRGRND Movement is one of the only Gold Coast studios to offer a dedicated recovery movement program — a genuinely unique offering that treats movement as both a physical and emotional practice.
    </p>
    <h3>Why Choose UNDRGRND Movement on the Gold Coast</h3>
    <p>
      Every adult program at our Southport studio starts with foundations — no experience required. We keep classes small (maximum 15 students) to ensure every adult on the Gold Coast receives individual attention and instruction. Our qualified instructors build structured, progressive programs that develop real movement skills at a pace that works for each person. We do not run competitive classes. We do not push students beyond their limits. Instead, we create a welcoming, non-judgmental environment where adults of all ages and abilities can discover what their bodies are capable of.
    </p>
    <p>
      Book your first class at UNDRGRND Movement Southport and discover movement that feels good. From dance to pole to yoga to aerial, we will help you build strength, confidence, and a sustainable practice on the Gold Coast.
    </p>
    <h3>Serving Adults Across the Gold Coast</h3>
    <p>
      UNDRGRND Movement's Southport studio is accessible to adults from across the Gold Coast, including Surfers Paradise, Broadbeach, Bundall, Main Beach, Nerang, Robina, and surrounding suburbs. Our timetable is designed to suit working adults, with morning, afternoon, and evening sessions available throughout the week.
    </p>
    <div class="seo-section__cta-text">
      Ready to start your movement journey? <a href="/timetable.html">View our adult class timetable</a> or <a href="/contact.html">contact our Southport studio today</a>.
    </div>
  </div>
</section>"""

if old_seo in html:
    html = html.replace(old_seo, new_seo, 1)
    print("SEO section updated")
else:
    print("WARNING: Could not find old SEO section in adults.html")
    # Try a partial match
    old_seo_h2 = '<h2 id="seoHeading">Transform Your Body and Mind with Adult Movement Classes on the Gold Coast</h2>'
    if old_seo_h2 in html:
        print("Found SEO H2 - will need manual fix")
    else:
        print("SEO H2 also not found")

# ============================================================
# 5. Write output
# ============================================================
with open('adults.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("adults.html updated successfully")
print(f"New line count: {html.count(chr(10))}")
