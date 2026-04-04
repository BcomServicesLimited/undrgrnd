"""
Fix all remaining age references on kids.html and kids program pages.
All kids classes are now for ages 6–8 only.
"""
import os, re, glob

# ─── kids.html specific fixes ────────────────────────────────────────────────

kids = open('kids.html', encoding='utf-8').read()

# 1. Schema JSON-LD: "from age 4" and "age 16"
kids = kids.replace(
    '"text": "We offer programs for children from age 4. Our Creative Dance class is designed specifically',
    '"text": "We offer programs for children aged 6 to 8. Our Creative Dance class is designed specifically'
)
kids = re.sub(r'from age 4\.', 'for children aged 6 to 8.', kids)
kids = re.sub(r'age 4 to 16', 'age 6 to 8', kids)
kids = re.sub(r'ages? 4 to 16', 'ages 6 to 8', kids)
kids = re.sub(r'aged 4 to 16', 'aged 6 to 8', kids)

# 2. "Programs for ages 4–16" subtitle
kids = kids.replace('Programs for ages 4–16', 'Programs for ages 6–8')

# 3. Age band cards — collapse to single 6–8 band
old_age_bands_grid = '''    <div class="age-bands-grid">
      <div class="age-band-card">
        <div class="age-band-label ages-4-7">Ages 4–7</div>
        <h3>Little Movers</h3>
        <p>Play-based movement for young children. Focus on imagination, rhythm, and body awareness in a joyful, pressure-free environment at our Southport studio.</p>
        <ul>
          <li>Creative Dance - Foundations</li>
        </ul>
      </div>
      <div class="age-band-card">
        <div class="age-band-label ages-8-12">Ages 8–12</div>
        <h3>Junior Explorers</h3>
        <p>Structured movement classes that build real skills. Dance, yoga, aerial, and pole fitness for primary school-aged children on the Gold Coast.</p>
        <ul>
          <li>Dance Moves (Urban Mix) - Foundations</li>
          <li>Modern Contemporary (Rhythm &amp; Motion) - Foundations</li>
          <li>Kids Yoga - Foundations</li>
          <li>Kids Aerial Yoga - Foundations (Coming Soon)</li>
          <li>Kids Aerial Silks - Foundations (Coming Soon)</li>
          <li>Pole Fitness Kids - Foundations (Coming Soon)</li>
        </ul>
      </div>
      <div class="age-band-card">
        <div class="age-band-label ages-13-16">Ages 13–16</div>
        <h3>Teen Movers</h3>
        <p>More advanced movement for teenagers. Build strength, confidence, and coordination through dance, aerial, and fitness-focused classes in Southport.</p>
        <ul>
          <li>Dance Moves (Urban Mix) - Foundations</li>
          <li>Modern Contemporary (Rhythm &amp; Motion) - Foundations</li>
          <li>Kids Yoga - Foundations</li>
          <li>Kids Aerial Yoga - Foundations (Coming Soon)</li>
          <li>Kids Aerial Silks - Foundations (Coming Soon)</li>
          <li>Pole Fitness Kids - Foundations (Coming Soon)</li>
        </ul>
      </div>
    </div>'''

new_age_bands_grid = '''    <div class="age-bands-grid">
      <div class="age-band-card">
        <div class="age-band-label ages-6-8">Ages 6–8</div>
        <h3>Young Movers</h3>
        <p>Structured, age-appropriate movement classes for children aged 6 to 8. Dance, yoga, aerial, and pole fitness in a safe, fun, and supportive environment at our Southport studio.</p>
        <ul>
          <li>Creative Dance - Foundations</li>
          <li>Dance Moves (Urban Mix) - Foundations</li>
          <li>Modern Contemporary (Rhythm &amp; Motion) - Foundations</li>
          <li>Kids Yoga - Foundations</li>
          <li>Kids Aerial Yoga - Foundations (Coming Soon)</li>
          <li>Kids Aerial Silks - Foundations (Coming Soon)</li>
          <li>Pole Fitness Kids - Foundations (Coming Soon)</li>
        </ul>
      </div>
    </div>'''

kids = kids.replace(old_age_bands_grid, new_age_bands_grid)

# 4. Age group tabs — remove 4-7, 8-12, 13-16 buttons, keep All Ages
old_tabs = '''      <button class="tab-btn active" data-age="all"   role="tab" aria-selected="true"  type="button">All Ages</button>
      <button class="tab-btn"        data-age="4-7"   role="tab" aria-selected="false" type="button">Ages 4–7</button>
      <button class="tab-btn"        data-age="8-12"  role="tab" aria-selected="false" type="button">Ages 8–12</button>
      <button class="tab-btn"        data-age="13-16" role="tab" aria-selected="false" type="button">Ages 13–16</button>'''
new_tabs = '''      <button class="tab-btn active" data-age="all"   role="tab" aria-selected="true"  type="button">All Ages (6–8)</button>'''
kids = kids.replace(old_tabs, new_tabs)

# 5. SEO section headings and content — replace age-group subsections
kids = kids.replace(
    '<h3>Ages 4–7: Little Movers</h3>',
    '<h3>Ages 6–8: Young Movers</h3>'
)
kids = kids.replace(
    '''    <p>
      Our youngest students begin with <strong>Creative Dance - Foundations</strong>, a play-based introduction to movement for children aged 4 to 7. Classes encourage imagination, rhythm, and physical expression through games, stories, and guided exploration. Children build coordination and body awareness in a joyful, pressure-free environment at our Southport studio. This class is the ideal first movement experience for Gold Coast children starting their journey.
    </p>
    <h3>Ages 8–12: Junior Explorers</h3>
    <p>
      Primary school-aged children on the Gold Coast have the widest range of class options at UNDRGRND Movement. <strong>Dance Moves (Urban Mix) - Foundations</strong> introduces hip hop and urban dance styles in a fun, structured format, building rhythm, coordination, and performance confidence through age-appropriate choreography. <strong>Modern Contemporary (Rhythm &amp; Motion) - Foundations</strong> takes a more expressive approach, developing movement quality, musicality, and artistic awareness.
    </p>
    <p>
      <strong>Kids Yoga - Foundations</strong> is available for children aged 6 to 8 and uses age-appropriate poses, breathing exercises, and mindfulness activities to support physical and mental wellbeing. For children who want to take their practice further, <strong>Kids Aerial Yoga - Foundations</strong> (coming soon to our Southport studio) uses suspended silk hammocks to create a unique, playful yoga experience that builds strength, flexibility, and spatial awareness. <strong>Kids Aerial Silks - Foundations</strong> (coming soon) and <strong>Pole Fitness Kids - Foundations</strong> (coming soon) round out our aerial and strength offerings for this age group.
    </p>
    <h3>Ages 13–16: Teen Movers</h3>
    <p>
      Teenagers on the Gold Coast can access the full range of kids' programs at UNDRGRND Movement. The same dance, yoga, aerial, and pole fitness classes available to 8–12 year olds are also open to teenagers, with instructors adapting the level of challenge and complexity to suit older students. Our Southport studio provides a non-competitive, encouraging environment where teenagers can explore movement at their own pace and build genuine physical confidence.
    </p>''',
    '''    <p>
      All UNDRGRND Movement kids' programs are designed for children aged 6 to 8 years. <strong>Creative Dance - Foundations</strong> introduces movement through play, imagination, and rhythm — the perfect first movement experience for Gold Coast children. <strong>Dance Moves (Urban Mix) - Foundations</strong> brings hip hop and urban dance styles to life in a fun, structured format, building coordination and performance confidence through age-appropriate choreography. <strong>Modern Contemporary (Rhythm &amp; Motion) - Foundations</strong> takes a more expressive approach, developing movement quality, musicality, and artistic awareness.
    </p>
    <p>
      <strong>Kids Yoga - Foundations</strong> uses age-appropriate poses, breathing exercises, and mindfulness activities to support physical and mental wellbeing. For children who want to take their practice further, <strong>Kids Aerial Yoga - Foundations</strong> (coming soon to our Southport studio) uses suspended silk hammocks to create a unique, playful yoga experience that builds strength, flexibility, and spatial awareness. <strong>Kids Aerial Silks - Foundations</strong> (coming soon) and <strong>Pole Fitness Kids - Foundations</strong> (coming soon) round out our aerial and strength offerings for this age group.
    </p>'''
)

# 6. SEO paragraph "from age 4" / "age 4 to 16"
kids = re.sub(
    r'We offer programs for children from age 4\. Our Creative Dance class is designed specifically for children aged 4 to 7[^.]*\.',
    'We offer programs for children aged 6 to 8. Our Creative Dance class is designed specifically for this age group.',
    kids
)
kids = re.sub(r'aged 4 to 7', 'aged 6 to 8', kids)
kids = re.sub(r'ages 4 to 16', 'ages 6 to 8', kids)
kids = re.sub(r'age 4 to 16', 'age 6 to 8', kids)
kids = re.sub(r'ages? 4–16', 'ages 6–8', kids)
kids = re.sub(r'8–12 year olds', '6–8 year olds', kids)

open('kids.html', 'w', encoding='utf-8').write(kids)
print("Fixed: kids.html")

# ─── kids-modern-contemporary.html: "children aged 10" ──────────────────────
f = 'programs/kids-modern-contemporary.html'
content = open(f, encoding='utf-8').read()
# Fix "children aged 6 to 8. The more nuanced... children aged 10"
content = re.sub(r'children aged 10\b', 'children aged 6 to 8', content)
open(f, 'w', encoding='utf-8').write(content)
print(f"Fixed: {f}")

# ─── about.html: "ages 4 to 16" ─────────────────────────────────────────────
f = 'about.html'
content = open(f, encoding='utf-8').read()
content = re.sub(r'Kids programs span ages 4 to 16', 'Kids programs are for children aged 6 to 8', content)
content = re.sub(r'ages 4 to 16', 'ages 6 to 8', content)
open(f, 'w', encoding='utf-8').write(content)
print(f"Fixed: {f}")

print("\nAll done.")
