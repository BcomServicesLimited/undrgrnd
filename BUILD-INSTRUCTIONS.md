# UNDRGRND Movement Website - Build Instructions for Manus

## Project Overview
Build a multi-page HTML website for UNDRGRND Movement, a Gold Coast movement studio offering dance, pole fitness, yoga, and aerial classes. The site must be heavily optimized for local SEO, LLM-friendly, and integrate with Class Manager booking system.

## Single Source of Truth
**ALL site configuration is in `site-config.json`**
- Business details, contact info, hours
- Design tokens (colors, fonts, spacing)
- Program catalog with full descriptions
- SEO keywords and local areas
- Legal disclaimers and policies
- Navigation structure

**Never hardcode these values - always reference site-config.json**

---

## Build Order & Prompts

### STEP 1: Setup & Shared Components

#### Prompt 1.1: Create Global CSS Stylesheet
```
Using the design tokens from site-config.json, create a global stylesheet (global.css) that defines:

1. CSS Variables for all colors, fonts, spacing from site-config.json
2. Reset/normalize styles
3. Base typography styles (h1-h6, p, a, etc.)
4. Reusable utility classes:
   - .container (max-width: 1400px, centered)
   - .section-padding (from site-config)
   - .gradient-text (purple gradient)
   - .card (background, border, radius from config)
   - .cta-button (primary and secondary variants)
5. Responsive breakpoints:
   - Mobile: 320px - 767px
   - Tablet: 768px - 1023px
   - Desktop: 1024px+
6. Animation keyframes for:
   - Fade in on scroll
   - Pulse effect
   - Slide up
   - Hover lift

Reference the exact color codes, fonts, and spacing from site-config.json.
Make this stylesheet comprehensive so all pages can import it.
```

#### Prompt 1.2: Create Navigation Component
```
Create a reusable navigation HTML snippet (nav-component.html) that can be included on all pages.

Requirements:
1. Fixed position header with backdrop blur
2. Logo using "UNDRGRND movement" text with gradient from site-config.json colors
3. Navigation links from site-config.json navigation.main_menu array
4. CTA button from site-config.json navigation.cta_button
5. Mobile hamburger menu (JavaScript toggle)
6. Active state for current page
7. Smooth scroll behavior for anchor links

Design:
- Use fonts and colors from site-config.json
- Sticky on scroll with slight transparency
- Border bottom using primary purple with opacity
- Logo should link to homepage (/)

JavaScript:
- Toggle mobile menu on hamburger click
- Close menu when link is clicked
- Add 'scrolled' class to nav when page scrolls >50px
- Highlight active page link based on current URL
```

#### Prompt 1.3: Create Footer Component
```
Create a reusable footer HTML snippet (footer-component.html).

Content structure:
1. Three columns:
   - Column 1: Logo, tagline from site-config.json, social links
   - Column 2: Quick links (Adults, Kids, Timetable, About, Contact)
   - Column 3: Contact info from site-config.json
     * Address (full formatted)
     * Email (mailto link)
     * Phone (tel link)
     * Hours summary

2. Bottom bar:
   - Copyright © 2026 UNDRGRND Movement
   - Privacy Policy | Terms of Service
   - "Proudly serving Gold Coast and Southport communities"

Design:
- Dark background with purple accent borders
- Use site-config.json for all colors and fonts
- Social icons (Instagram, Facebook) as outline icons
- Responsive: stack columns on mobile

NAP Consistency:
- Ensure Name, Address, Phone match site-config.json exactly
- This is critical for local SEO
```

#### Prompt 1.4: Create Schema Markup Generator Script
```
Create a JavaScript file (schema-generator.js) that generates JSON-LD structured data.

Functions needed:
1. generateLocalBusinessSchema()
   - Uses data from site-config.json
   - Outputs DanceSchool + YogaStudio + HealthAndBeautyBusiness types
   - Includes address, geo, contact, hours, area served
   
2. generateProgramSchema(programData)
   - Takes program object from site-config.json
   - Creates Service schema with offer pricing
   
3. generateBreadcrumbSchema(breadcrumbArray)
   - Takes array of {name, url} objects
   - Creates BreadcrumbList schema
   
4. generateFAQSchema(faqArray)
   - Takes array of {question, answer} objects
   - Creates FAQPage schema

Each function should return a JSON-LD script tag ready to insert in <head>.
Include comprehensive comments explaining each schema type.
```

---

### STEP 2: Homepage

#### Prompt 2.1: Build Homepage HTML Structure
```
Create index.html for the homepage.

Page structure:
1. <head>
   - Title and meta description from site-config.json SEO
   - Import global.css
   - Import Google Fonts: Bebas Neue and Outfit (weights 300,400,600,700,800)
   - Insert LocalBusinessSchema from schema-generator.js
   - Canonical URL: https://www.undrgrnd.com.au/
   - OG meta tags for social sharing

2. <body>
   - Include nav-component.html
   
   - Hero Section:
     * Full viewport height
     * Grid layout: content left, image right
     * H1: "Gold Coast's Underground Movement Revolution"
     * Subheadline: "Foundational movement for body and mind | Southport Studio"
     * Location: "163 Ferry Rd, Southport QLD 4215"
     * Two CTAs: "Book Your First Class" + "View Timetable"
     * Right side: Placeholder for AI-generated hero image
     * Background: Gradient with animated radial circles in purple
   
   - Class Finder Widget (floats over hero):
     * Card with dark background, purple border
     * "I'm looking for classes for:" [Adults] [Kids] buttons
     * "I'm interested in:" [Dance] [Pole] [Yoga] [Aerial] [Recovery] buttons
     * "Show Me Classes" CTA
     * JavaScript: filters selection, links to appropriate page with hash
   
   - Why UNDRGRND Section:
     * H2: "Why UNDRGRND Movement?"
     * Three pillar cards (Foundation, Recovery, Expression)
     * Each pillar: icon, title, description
     * Pull descriptions from site-config.json philosophy
   
   - Featured Programs Section:
     * H2: "Start Your Movement Journey"
     * Grid of program cards (Afro Groove, Aerial Silks as hero programs)
     * Each card: image placeholder, category tag, title, short description, "Learn More" link
     * Pull from site-config.json programs where hero_program: true
   
   - Location Section:
     * H2: "Movement Beyond Four Walls"
     * Text about studio, beach, park sessions
     * Google Maps embed of 163 Ferry Rd, Southport
   
   - SEO Content Section (below fold):
     * H2: "Gold Coast's Premier Dance School and Yoga Studio in Southport"
     * 800-1200 words of SEO-optimized content mentioning:
       - Gold Coast, Southport 15+ times
       - All program types with local keywords
       - Beginner-friendly emphasis
       - Service area (Surfers Paradise, Broadbeach, etc.)
       - Benefits of movement for body and mind
     * Natural, helpful tone - not keyword stuffing
   
   - Include footer-component.html

3. Page-specific CSS (in <style> tag):
   - Hero background animations
   - Class finder floating card positioning
   - Program card hover effects
   - Responsive adjustments

4. Page-specific JavaScript:
   - Class finder filter functionality
   - Smooth scroll to sections
   - Intersection Observer for fade-in animations
```

#### Prompt 2.2: Add Homepage SEO Content
```
Write the SEO content section for the homepage (800-1200 words).

Requirements:
- Mention "Gold Coast" and "Southport" naturally 15+ times
- Cover all program types: dance, pole fitness, yoga, aerial
- Target keywords from site-config.json naturally
- Address these topics:
  * What makes UNDRGRND Movement unique
  * Who the classes are for (beginners welcome)
  * Benefits of each program type
  * The studio's philosophy and approach
  * Service area and location benefits
  * Medical clearance for recovery classes
  * Multi-environment approach (studio, beach, park)

Tone:
- Welcoming, inclusive, empowering
- Professional but approachable
- Emphasize "personal transformation, not competition"
- Beginner-friendly language

Format:
- Use H3 subheadings to break up sections
- Short paragraphs (3-4 sentences max)
- Include local landmarks/areas naturally
- End with strong CTA to book a class

Output as HTML ready to insert in homepage.
```

---

### STEP 3: Adults Landing Page

#### Prompt 3.1: Build Adults Page HTML
```
Create adults.html landing page.

Page structure:
1. <head>
   - Title: "Adult Movement Classes Gold Coast | Dance, Pole, Yoga & Aerial | Southport"
   - Meta description: "Beginner-friendly movement classes for adults at UNDRGRND Movement, Southport. Dance fitness, pole, yoga, and aerial programs. No experience needed. Book your Gold Coast class today."
   - Import global.css
   - Breadcrumb schema: Home > Adults
   - Service schema for adult programs

2. <body>
   - Include nav-component.html
   
   - Hero Section:
     * H1: "Adult Movement Classes | Gold Coast Dance & Fitness Studio"
     * Subheadline: "Beginner-friendly programs for every body and every goal"
     * Location mention: "Located in Southport, serving the Gold Coast"
     * CTA: "View Timetable"
     * Background: AI-generated image of flexible woman in middle split
   
   - Program Categories:
     * Filter buttons: [All] [Dance] [Pole] [Yoga] [Aerial] [Choreography]
     * Grid of ALL adult program cards from site-config.json programs.adults
     * Each card:
       - Category badge (color-coded)
       - Program name
       - Level indicator
       - Short description
       - Core focus points (first 3)
       - Estimated pricing (drop-in rate)
       - "Learn More" button → individual program page
       - "Book Now" button → timetable with filter
     * JavaScript filtering by category
   
   - "New to Movement?" Section:
     * H2: "Perfect for Beginners"
     * Reassurance content about beginner-friendly approach
     * No experience necessary messaging
     * List of what to expect in first class
   
   - Medical Clearance Notice:
     * Call-out box for Recovery Movement
     * Clear explanation from site-config.json legal.medical_disclaimer
     * Link to contact form for questions
   
   - SEO Content:
     * 800-1000 words about adult movement classes in Gold Coast
     * Benefits of each program type
     * Who each program is suited for
     * Location and accessibility
     * Beginner support and progression
   
   - Include footer-component.html

3. JavaScript:
   - Category filter functionality
   - Smooth animations when filtering
   - Modal for medical clearance info (if recovery class clicked)
```

#### Prompt 3.2: Add Adults Page SEO Content
```
Write SEO content for adults.html (800-1000 words).

Cover:
- Benefits of adult movement classes for fitness and wellbeing
- Why Gold Coast adults choose UNDRGRND Movement
- Overview of each program type (dance, pole, yoga, aerial)
- Beginner-friendly approach and progression
- Recovery and rehabilitation options
- Flexible scheduling and class formats
- Community and supportive environment
- Location convenience for Gold Coast residents

Target these keywords naturally:
- adult dance classes gold coast
- pole fitness for beginners southport
- yoga classes gold coast adults
- aerial silks gold coast
- beginner fitness classes southport

Mention Southport, Gold Coast, and surrounding suburbs 10+ times naturally.
Use H3 subheadings. Keep paragraphs short. End with CTA.
Output as HTML.
```

---

### STEP 4: Kids Landing Page

#### Prompt 4.1: Build Kids Page HTML
```
Create kids.html landing page.

Page structure:
1. <head>
   - Title: "Kids Dance & Movement Classes Gold Coast | Yoga, Pole & Aerial | Southport"
   - Meta description: "Fun, age-appropriate movement classes for children at UNDRGRND Movement, Southport. Kids dance, yoga, pole fitness, and aerial programs. Gold Coast's trusted kids movement studio."
   - Import global.css
   - Breadcrumb schema: Home > Kids
   - Service schema for kids programs

2. <body>
   - Include nav-component.html
   
   - Hero Section:
     * H1: "Kids Movement Classes | Gold Coast Dance & Activity Studio"
     * Subheadline: "Building confidence, strength, and joy through movement"
     * Age range: "Programs for ages 4-16"
     * Location: "Southport studio serving Gold Coast families"
     * CTA: "View Kids Timetable"
     * Background: AI-generated image of children in movement poses
   
   - Age-Based Program Display:
     * Tabs or sections by age group:
       - Ages 4-7 (Creative Dance, Kids Yoga)
       - Ages 8-12 (All programs available)
       - Ages 13-16 (All programs available)
     * Each program card shows:
       - Program name
       - Recommended age range from site-config.json
       - Short description
       - Benefits for children
       - Estimated term pricing
       - "Learn More" button
   
   - Benefits for Children Section:
     * H2: "Why Movement Matters for Kids"
     * Grid of benefit cards:
       - Physical development
       - Confidence building
       - Creative expression
       - Social skills
       - Body awareness
       - Fun and enjoyment
   
   - Safety & Qualifications:
     * H2: "Safe, Qualified Instruction"
     * Instructor qualifications
     * Safety protocols
     * Parent observation policy
     * What to bring to class
   
   - Term Structure:
     * Explanation of 8-week terms
     * Trial class option
     * Drop-in vs. term enrollment
   
   - Parent FAQs:
     * What should my child wear?
     * Can I watch the class?
     * What age should my child start?
     * Is prior experience needed?
     * What if my child is shy/nervous?
   
   - SEO Content:
     * 800-1000 words about kids movement classes in Gold Coast
     * Benefits of each program for child development
     * Age-appropriate activities
     * Qualified instruction
     * Location and convenience for Gold Coast families
   
   - Include footer-component.html

3. JavaScript:
   - Age group filtering/tabs
   - FAQ accordion
   - Smooth scroll and animations
```

---

### STEP 5: Individual Program Pages (Priority 3)

#### Prompt 5.1: Create Program Page Template
```
Create a reusable template for individual program pages (program-template.html).

This template will be used for:
- Afro Groove Foundations
- Aerial Silks  
- Pole Fitness Foundations
- (and all other programs)

Page structure:
1. <head> (populated dynamically based on program):
   - Title: "[Program Name] | UNDRGRND Movement Gold Coast | [Category] Classes Southport"
   - Meta description: Pull from program short_description + location
   - Import global.css
   - Breadcrumb schema: Home > [Adults/Kids] > [Program Name]
   - Service Offer schema for this specific program

2. <body>
   - Include nav-component.html
   
   - Hero Section:
     * Full-width background image (AI-generated based on program type)
     * H1: "[Program Name] | [Category] Classes Gold Coast"
     * Level indicator: "Beginner / Foundation" etc.
     * Location: "Southport Studio"
     * Two CTAs: "Book This Class" + "View Full Timetable"
   
   - Program Overview Section:
     * Program full_description from site-config.json
     * Two-column layout:
       - Left: Description text
       - Right: Quick info box
         * Level
         * Category
         * Duration (typical)
         * Class size
         * What to bring
         * Pricing options
   
   - Core Focus Section:
     * H2: "What You'll Learn"
     * Grid/list of core_focus items from site-config.json
     * Each with icon and description
   
   - Who It's For Section:
     * H2: "Is This Class Right For You?"
     * List of who_its_for from site-config.json
     * Encouragement for beginners
   
   - What to Expect Section:
     * H2: "Your First Class"
     * Timeline/steps of typical class
     * what_to_expect items from site-config.json
     * Reassurance about beginner-friendliness
   
   - Pricing Section:
     * H2: "Flexible Pricing Options"
     * Three pricing tiers from estimated_pricing in site-config.json:
       - Drop-in: $XX per class
       - Class Pack: $XX for 10 classes
       - Unlimited: $XX per month
     * Note: "Prices are estimates. See full pricing in booking system."
   
   - Medical Clearance Section (conditional):
     * Only show if program.medical_clearance_required === true
     * Warning box with legal.medical_disclaimer from site-config.json
     * Clear instructions on what documentation needed
   
   - FAQ Section:
     * Program-specific FAQs with FAQ schema
     * "Do I need experience?"
     * "What should I wear?"
     * "How long are classes?"
     * "Can I try a class first?"
   
   - Related Programs:
     * H2: "You Might Also Like"
     * Cards for 3 related programs (same category or level)
   
   - CTA Section:
     * Bold call-to-action
     * "Ready to Start Your [Program Name] Journey?"
     * "Book Your First Class" button → timetable filtered
   
   - SEO Content:
     * 800-1200 words about this specific program
     * Benefits and outcomes
     * Technique and skills taught
     * Instructor approach
     * Gold Coast/Southport location mentions
     * Who it's perfect for
     * Progression path
   
   - Include footer-component.html

3. CSS:
   - Sticky "Book Now" button on scroll
   - Program-specific color accents based on category
   - Responsive image gallery if multiple images
   - Pricing card hover effects

4. JavaScript:
   - Populate all content from site-config.json based on program slug
   - Intersection Observer for scroll animations
   - FAQ accordion functionality
   - Filter "Book Now" link with program category
```

#### Prompt 5.2: Build Afro Groove Foundations Page
```
Using program-template.html, create afro-groove-foundations.html.

Pull ALL content from site-config.json programs.adults.dance[0] (id: "afro-groove").

Specific requirements:
1. Hero image prompt for AI generation:
   "Athletic flexible African woman in dynamic Afro dance pose, hip movement emphasis, energetic expression, purple and pink gradient lighting, dark background, professional fitness photography"

2. SEO content focus:
   - Afrobeat dance benefits
   - Hip mobility and coordination
   - Beginner-friendly Afro dance in Gold Coast
   - No experience necessary messaging
   - Cultural appreciation and respectful approach
   - Fitness benefits: cardio, strength, coordination
   - Southport studio location and accessibility

3. FAQs specific to Afro Groove:
   - "Do I need to know Afrobeat music?"
   - "Is this class culturally authentic?"
   - "What if I have no rhythm?"
   - "Will I be able to keep up as a beginner?"
   - "What should I wear to Afro Groove?"

4. Related programs to suggest:
   - Movement Dance
   - Choreography Fusion
   - Pole Flow (for similar flow emphasis)

Ensure all data comes from site-config.json. No hardcoded program details.
```

#### Prompt 5.3: Build Aerial Silks Page
```
Using program-template.html, create aerial-silks.html.

Pull ALL content from site-config.json programs.adults.aerial[0] (id: "aerial-silks").

Specific requirements:
1. Hero image prompt for AI generation:
   "Graceful flexible woman suspended on aerial silks, beautiful wrap position, strength and elegance, purple dramatic lighting, dark background, professional aerial arts photography"

2. SEO content focus:
   - Aerial silks for beginners Gold Coast
   - Building upper body strength through aerial arts
   - Safety in aerial training
   - Overcoming fear of heights
   - Artistic expression through aerial dance
   - Southport aerial studio facilities
   - Benefits: strength, flexibility, confidence, creativity

3. Safety callout box:
   - All equipment professionally rigged
   - Crash mats provided
   - Instructors are experienced aerialists
   - Progressive skill-building approach
   - No dropping or falling - you control your descent

4. FAQs specific to Aerial Silks:
   - "Do I need to be strong to start?"
   - "I'm afraid of heights - can I still try?"
   - "Will I get bruises?"
   - "What if I can't climb?"
   - "Do I need to be flexible?"

5. Related programs:
   - Aerial Yoga (easier introduction)
   - Pole Strength & Movement (similar strength focus)

Ensure all data comes from site-config.json.
```

#### Prompt 5.4: Build Pole Fitness Foundations Page
```
Using program-template.html, create pole-fitness-foundations.html.

Pull ALL content from site-config.json programs.adults.pole[0] (id: "pole-foundations").

Specific requirements:
1. Hero image prompt for AI generation:
   "Strong flexible woman demonstrating beginner pole grip, focused expression, controlled positioning, purple accent lighting, professional pole fitness studio photography"

2. SEO content focus:
   - Pole fitness for beginners Gold Coast
   - Safe introduction to pole dancing as fitness
   - Strength and confidence building
   - Non-sexualized, athletic approach
   - Southport pole studio with quality equipment
   - Benefits: full-body strength, coordination, empowerment
   - Beginner-friendly progression

3. Important clarifications:
   - This is pole FITNESS, not pole dancing/exotic dance
   - Athletic, strength-based approach
   - All genders welcome (though primarily women attend)
   - Start from absolute basics - everyone begins here
   - No climbing in foundations - that comes later

4. FAQs specific to Pole Fitness:
   - "Do I need to be strong to start?"
   - "Is pole fitness the same as pole dancing?"
   - "Will I learn tricks in the first class?"
   - "What should I wear?" (shorts and tank top for grip)
   - "I have no upper body strength - can I do this?"

5. Progression path:
   - Pole Foundations (you are here)
   - → Pole Flow (next step)
   - → Pole Strength & Movement (advanced)

6. Related programs:
   - Pole Flow
   - Pole Strength & Movement
   - Aerial Silks (similar strength focus)

Ensure all data comes from site-config.json.
```

---

### STEP 6: Timetable Page

#### Prompt 6.1: Build Timetable Page with Booking Integration
```
Create timetable.html with Class Manager integration.

Page structure:
1. <head>
   - Title: "Class Timetable | Book Dance, Pole, Yoga & Aerial Classes | UNDRGRND Movement Gold Coast"
   - Meta description: "View and book movement classes at UNDRGRND Movement, Southport. Live timetable with availability for dance, pole fitness, yoga, and aerial classes on the Gold Coast."
   - Import global.css

2. <body>
   - Include nav-component.html
   
   - Hero Section:
     * H1: "Class Timetable | Book Your Session"
     * Subheadline: "View live availability and book directly"
     * Location: "163 Ferry Rd, Southport QLD 4215"
   
   - Filter Bar:
     * Sticky filter bar below header
     * Buttons: [All Classes] [Adults] [Kids]
     * Category filters: [Dance] [Pole] [Yoga] [Aerial] [Recovery]
     * Week navigation: [← Previous Week] [This Week] [Next Week →]
     * These filters should update the iframe src with query parameters (when Class Manager supports it)
   
   - Class Manager Integration:
     * Large iframe container (min-height: 900px)
     * Placeholder message: "Loading class schedule..."
     * iframe src from site-config.json booking.timetable_url
     * Full-width, responsive
     * Border styling to match site design
   
   - Troubleshooting Section (below calendar):
     * H3: "Having trouble booking?"
     * Common issues and solutions:
       - Clear browser cache
       - Ensure JavaScript enabled
       - Contact us if issues persist
     * Contact info:
       - Email: olga.coaching1@gmail.com
       - Phone: [from site-config.json]
   
   - Booking Policies:
     * H3: "Booking Policies"
     * Cancellation policy (24 hours notice)
     * Late arrival policy
     * First-time visitor information
     * What to bring to class
   
   - Include footer-component.html

3. CSS:
   - iframe should be fully responsive
   - Remove default iframe borders
   - Loading spinner while iframe loads
   - Sticky filter bar on scroll

4. JavaScript:
   - Filter functionality (updates iframe URL if supported)
   - Loading state management
   - Detect if iframe fails to load
   - Show fallback contact info if booking system down
   - Store last selected filters in localStorage
```

#### Prompt 6.2: Create Booking Fallback Page
```
Create book-now.html as a fallback if Class Manager is unavailable.

Page content:
1. Header: "Book Your Class"
2. Message: "Our online booking system is temporarily unavailable."
3. Alternative booking methods:
   - Email form to request booking
   - Phone number to call
   - Expected response time: "within 24 hours"
4. Apology and reassurance
5. Link back to timetable to try again

Form fields:
- Name
- Email
- Phone
- Preferred program (dropdown from site-config.json)
- Preferred date/time
- Message (optional)
- Submit button

Form should validate and could email to olga.coaching1@gmail.com
(or store submissions in a JSON file for manual processing).
```

---

### STEP 7: Contact Page

#### Prompt 7.1: Build Contact Page
```
Create contact.html.

Page structure:
1. <head>
   - Title: "Contact Us | UNDRGRND Movement Gold Coast | Southport Dance & Yoga Studio"
   - Meta description: "Get in touch with UNDRGRND Movement in Southport, Gold Coast. Visit us at 163 Ferry Rd or email olga.coaching1@gmail.com. Book your first class today."
   - Import global.css
   - LocalBusiness schema with contact info

2. <body>
   - Include nav-component.html
   
   - Hero:
     * H1: "Get In Touch"
     * Subheadline: "We'd love to hear from you"
   
   - Two-column layout:
     
     LEFT COLUMN - Contact Information:
     * Studio Location
       - Full address from site-config.json
       - Google Maps embed (interactive map)
       - Directions link
     
     * Contact Details
       - Email (clickable mailto:)
       - Phone (clickable tel:)
       - Hours of operation
     
     * Social Media
       - Instagram link with icon
       - Facebook link with icon
     
     * Parking & Access Information
       - Street parking availability
       - Accessibility notes
       - Public transport options
     
     RIGHT COLUMN - Contact Form:
     * Form fields:
       - Name (required)
       - Email (required, validated)
       - Phone (optional)
       - Subject dropdown:
         * General Inquiry
         * Class Information
         * Booking Question
         * Medical Clearance Question
         * Instructor/Partnership Inquiry
       - Program Interest (dropdown from site-config.json programs)
       - Message (textarea, required)
       - Submit button: "Send Message"
     
     * Form validation with JavaScript
     * Success message after submission
     * Could use Formspree, Netlify Forms, or similar service
   
   - FAQ Section:
     * H2: "Frequently Asked Questions"
     * Common pre-contact questions:
       - "Do I need to book in advance?"
       - "What should I wear to class?"
       - "Do you offer trial classes?"
       - "Is parking available?"
       - "Are classes suitable for complete beginners?"
       - "Do you offer private sessions?"
     * Each with concise answer
     * FAQ schema markup
   
   - "Proudly Serving" Section:
     * H3: "Proudly Serving Gold Coast Communities"
     * List of suburbs:
       - Southport
       - Surfers Paradise
       - Broadbeach
       - Bundall
       - Main Beach
       - Labrador
       - Arundel
       - And surrounding Gold Coast areas
   
   - Include footer-component.html

3. JavaScript:
   - Form validation
   - Google Maps initialization
   - FAQ accordion
   - Form submission handling
```

---

### STEP 8: About Page

#### Prompt 8.1: Build About Page
```
Create about.html.

Page structure:
1. <head>
   - Title: "About UNDRGRND Movement | Gold Coast Movement Studio | Our Story & Philosophy"
   - Meta description: "Learn about UNDRGRND Movement's unique approach to dance, pole, yoga, and aerial classes in Southport, Gold Coast. Founded on the principle of personal transformation, not competition."
   - Import global.css

2. <body>
   - Include nav-component.html
   
   - Hero:
     * H1: "About UNDRGRND Movement"
     * Mission statement from site-config.json philosophy.mission
     * Background image: studio space or abstract movement imagery
   
   - Our Philosophy Section:
     * H2: "Movement for Body and Mind"
     * Pull from site-config.json philosophy.mission and values
     * Three columns covering:
       - "Not Competition" - personal journey focus
       - "Personal Transformation" - individual growth
       - "Every Body Welcome" - inclusive approach
     * Use icon + text format
   
   - Meet Ollie Section:
     * H2: "Meet Your Instructor"
     * Two-column layout:
       - Left: Photo placeholder (professional headshot)
       - Right: Bio from site-config.json instructor
     * Name and title
     * Bio (site-config.json instructor.bio_short)
     * Qualifications list
     * Personal philosophy quote
   
   - Our Unique Approach:
     * H2: "Movement Beyond Four Walls"
     * Explanation of multi-environment approach
     * Three location types:
       - Studio: "Our Southport home base at 163 Ferry Rd"
       - Beach: "Ocean-side sessions at Gold Coast beaches"
       - Park: "Outdoor movement in natural settings"
     * Each with description and benefits
     * Reference WHO and IADMS recommendations from site-config.json
   
   - What Makes Us Different:
     * H2: "Why Choose UNDRGRND Movement?"
     * Grid of differentiators:
       - Beginner-friendly focus
       - Medical clearance support
       - Trauma-informed practices
       - Small class sizes
       - Qualified instructors
       - Inclusive, judgment-free environment
       - Flexible class formats
       - Multiple training environments
   
   - Credentials & Affiliations:
     * Qualifications held
     * Industry associations
     * Insurance and safety compliance
     * Reference to WHO, IADMS, somatic movement education
   
   - Community Section:
     * H2: "Join Our Community"
     * Testimonials (when available - leave placeholder)
     * Community values
     * Social media feed embed
   
   - Call to Action:
     * "Ready to Start Your Movement Journey?"
     * CTA buttons to Timetable and Contact
   
   - Include footer-component.html

3. SEO Content:
   - 800-1000 words total across sections
   - Mention Gold Coast, Southport throughout
   - Emphasize beginner-friendly, inclusive approach
   - Highlight unique multi-environment model
   - Personal transformation focus
```

---

### STEP 9: Legal & Policy Pages

#### Prompt 9.1: Create Privacy Policy Page
```
Create privacy-policy.html.

Content:
1. Standard Australian privacy policy compliant with Privacy Act 1988
2. Sections:
   - Information we collect (name, email, phone, health info for medical clearance)
   - How we use information (bookings, communications, safety)
   - How we store information (secure systems)
   - Third parties (Class Manager, email provider)
   - Your rights (access, correction, deletion)
   - Contact for privacy concerns
3. Use site-config.json legal.privacy_policy_summary as base
4. Professional legal tone
5. Last updated date: [Current date]

Simple page layout:
- Header with title
- Table of contents with anchor links
- Clearly formatted sections with H2/H3 headings
- Footer with contact email for privacy questions
```

#### Prompt 9.2: Create Terms of Service Page
```
Create terms-of-service.html.

Content based on site-config.json legal section:
1. Acceptance of terms
2. Participation waiver (from legal.liability_waiver)
3. Medical clearance requirements (from legal.medical_disclaimer)
4. General disclaimer (from legal.general_disclaimer)
5. Booking and cancellation policies
6. Code of conduct
7. Intellectual property
8. Limitation of liability
9. Governing law (Queensland, Australia)
10. Changes to terms

Compliance with:
- Australian Consumer Law
- Queensland health and safety regulations
- Insurance requirements for fitness instruction

Simple page layout with clear sections and anchor links.
```

---

### STEP 10: Additional Pages & Features

#### Prompt 10.1: Create 404 Error Page
```
Create 404.html.

Design:
- Friendly, on-brand 404 message
- "Oops! This page doesn't exist"
- Helpful links:
  * Home
  * View Classes
  * Timetable
  * Contact Us
- Search functionality (optional)
- Purple gradient background
- Maintain nav and footer for consistency

Keep it light and helpful, not frustrated or technical.
```

#### Prompt 10.2: Create Medical Clearance Modal Component
```
Create medical-clearance-modal.html (reusable component).

Triggered when:
- User clicks "Book Now" on Recovery Movement classes
- User selects Recovery Movement in class finder

Modal content:
1. Warning icon
2. H2: "Medical Clearance Required"
3. Full disclaimer from site-config.json legal.medical_disclaimer
4. Requirements:
   - Written clearance from GP or specialist
   - Bring documentation to first class
   - Must be dated within last 3 months
5. Two buttons:
   - "I Have Clearance - Continue to Booking"
   - "I Need More Information - Contact Us"

Styling:
- Dark overlay backdrop
- Centered modal card
- Purple accent borders
- Clear, serious tone
- Close button (X) in corner

JavaScript:
- Show/hide functionality
- Prevent booking without acknowledgment
- Remember acknowledgment in session storage
```

#### Prompt 10.3: Create Robots.txt and Sitemap.xml
```
Create robots.txt:
- Allow all search engines
- Sitemap location: https://www.undrgrnd.com.au/sitemap.xml
- Disallow: none (everything is public)

Create sitemap.xml:
- Include all pages with priority and changefreq:
  * Homepage (priority 1.0, weekly)
  * Adults (0.9, weekly)
  * Kids (0.9, weekly)
  * Timetable (0.8, daily)
  * Contact (0.7, monthly)
  * About (0.7, monthly)
  * All individual program pages (0.8, monthly)
  * Legal pages (0.3, yearly)
- Use current date for lastmod
- Include proper XML namespace declarations
```

---

### STEP 11: Performance & SEO Optimization

#### Prompt 11.1: Create Favicon Set
```
Using the UNDRGRND logo image at /mnt/user-data/uploads/UNDRGRND_Logo__1_.png:

1. Extract or create a square version focusing on the "U" or the word "UNDRGRND"
2. Generate multiple sizes:
   - favicon.ico (16x16, 32x32)
   - favicon-16x16.png
   - favicon-32x32.png
   - apple-touch-icon.png (180x180)
   - android-chrome-192x192.png
   - android-chrome-512x512.png
3. Create site.webmanifest with app info
4. Add favicon link tags to HTML template

Ensure favicons use the purple gradient from brand colors.
```

#### Prompt 11.2: Optimize Images and Performance
```
Performance optimization checklist:

1. Image Optimization:
   - All AI-generated images should be:
     * WebP format with fallback
     * Lazy loading (loading="lazy")
     * Proper alt text for accessibility and SEO
     * Responsive srcset for different screen sizes
     * Max dimensions: 2000px wide
     * Compressed to <200KB per image

2. CSS Optimization:
   - Critical CSS inline in <head>
   - Non-critical CSS loaded asynchronously
   - Minify all CSS files
   - Use CSS variables for consistency
   - Purge unused CSS

3. JavaScript Optimization:
   - Defer non-critical JS
   - Minimize DOM manipulation
   - Use event delegation
   - Minify all JS files
   - Bundle common scripts

4. Loading Performance:
   - Preload critical fonts
   - Preconnect to external domains
   - Add rel="preload" for hero images
   - Minimize render-blocking resources
   - Target <2 second load time

5. Accessibility:
   - All images have descriptive alt text
   - Proper heading hierarchy (H1 → H2 → H3)
   - ARIA labels where needed
   - Keyboard navigation support
   - Color contrast ratios meet WCAG AA
   - Focus indicators visible
```

#### Prompt 11.3: Local SEO Checklist
```
Ensure every page has:

1. Schema Markup:
   - LocalBusiness schema on every page
   - Breadcrumb schema on all internal pages
   - Service/Offer schema on program pages
   - FAQ schema where FAQs exist
   - Review schema when testimonials added

2. NAP Consistency:
   - Name: UNDRGRND Movement (exactly as in site-config.json)
   - Address: 163 Ferry Rd, Southport QLD 4215
   - Phone: [from site-config.json]
   - Must be IDENTICAL on every page, footer, and in schema

3. Local Keywords:
   - "Gold Coast" mentioned 10-15 times per page
   - "Southport" mentioned 5-10 times per page
   - Service area suburbs mentioned naturally
   - Target keywords in:
     * H1 (once)
     * H2s (2-3 times)
     * First paragraph
     * Alt text
     * Meta description

4. Google My Business Optimization:
   - Ensure NAP matches GMB exactly
   - Category: Dance School (primary), Yoga Studio (secondary)
   - Service area: Gold Coast suburbs
   - Website link: https://www.undrgrnd.com.au

5. Link Building:
   - Internal linking between related pages
   - Program pages link to timetable
   - All pages link to contact
   - Breadcrumb navigation
```

---

### STEP 12: Testing & Launch Checklist

#### Prompt 12.1: Create Pre-Launch Testing Checklist
```
Create TESTING-CHECKLIST.md file:

Functionality Testing:
□ All navigation links work
□ CTA buttons link to correct pages
□ Contact form submits successfully
□ Class Manager iframe loads
□ Mobile hamburger menu toggles
□ Filter buttons function correctly
□ FAQ accordions expand/collapse
□ Medical clearance modal triggers
□ External links open in new tabs
□ Email and phone links work (mailto/tel)

Responsive Design Testing:
□ Mobile (375px, 414px)
□ Tablet (768px, 1024px)
□ Desktop (1440px, 1920px)
□ All images scale properly
□ Text remains readable at all sizes
□ No horizontal scrolling
□ Touch targets are 44px minimum
□ Hamburger menu works on mobile

Browser Testing:
□ Chrome (latest)
□ Safari (latest)
□ Firefox (latest)
□ Edge (latest)
□ Mobile Safari (iOS)
□ Mobile Chrome (Android)

SEO Testing:
□ All pages have unique titles
□ All pages have meta descriptions
□ All images have alt text
□ Schema markup validates (Google Rich Results Test)
□ Sitemap.xml accessible
□ Robots.txt allows crawling
□ Canonical URLs set
□ Open Graph tags for social sharing

Performance Testing:
□ Page load <3 seconds (Google PageSpeed)
□ First Contentful Paint <1.8s
□ Largest Contentful Paint <2.5s
□ Cumulative Layout Shift <0.1
□ All images optimized and lazy loaded
□ CSS and JS minified

Accessibility Testing:
□ Keyboard navigation works
□ Screen reader friendly (test with NVDA/JAWS)
□ Color contrast ratios pass WCAG AA
□ Focus indicators visible
□ ARIA labels present where needed
□ Semantic HTML structure

Content Review:
□ No placeholder text remains
□ Contact details updated
□ Social media links updated
□ Class Manager URLs configured
□ All pricing displays correctly
□ Legal disclaimers present
□ Spelling and grammar checked
□ Brand voice consistent

Security:
□ HTTPS enabled (SSL certificate)
□ Contact form has spam protection
□ No sensitive data in client-side code
□ External links use rel="noopener"

Analytics:
□ Google Analytics tracking code added
□ GA4 property set up
□ Goal conversion tracking configured
□ Form submissions tracked
□ Button clicks tracked
```

---

## File Structure

Your project should have this structure:

```
/undrgrnd-website/
├── index.html                          # Homepage
├── adults.html                         # Adults landing page
├── kids.html                           # Kids landing page
├── timetable.html                      # Timetable with booking
├── contact.html                        # Contact page
├── about.html                          # About page
├── book-now.html                       # Booking fallback
├── privacy-policy.html                 # Privacy policy
├── terms-of-service.html               # Terms of service
├── 404.html                            # 404 error page
│
├── programs/                           # Individual program pages
│   ├── afro-groove-foundations.html
│   ├── aerial-silks.html
│   ├── pole-fitness-foundations.html
│   ├── movement-dance.html
│   ├── recovery-movement.html
│   ├── pole-flow.html
│   ├── pole-strength-movement.html
│   ├── yoga-fusion.html
│   ├── traditional-yoga.html
│   ├── modern-yoga.html
│   ├── aerial-yoga.html
│   ├── choreography-fusion.html
│   ├── kids-yoga.html
│   ├── kids-aerial-yoga.html
│   ├── kids-pole-foundations.html
│   ├── kids-aerial-silks.html
│   ├── kids-dance-moves.html
│   ├── kids-modern-contemporary.html
│   └── kids-creative-dance.html
│
├── css/
│   ├── global.css                      # Global styles
│   └── components.css                  # Component-specific styles
│
├── js/
│   ├── schema-generator.js             # Schema markup generator
│   ├── navigation.js                   # Nav functionality
│   ├── class-finder.js                 # Homepage class finder
│   ├── filters.js                      # Filter functionality
│   ├── medical-modal.js                # Medical clearance modal
│   └── analytics.js                    # Analytics tracking
│
├── components/
│   ├── nav-component.html              # Navigation component
│   ├── footer-component.html           # Footer component
│   └── medical-clearance-modal.html    # Medical modal
│
├── images/
│   ├── hero/                           # Hero images (AI-generated)
│   ├── programs/                       # Program-specific images
│   ├── logo/                           # Logo files
│   └── favicons/                       # Favicon set
│
├── site-config.json                    # SINGLE SOURCE OF TRUTH
├── sitemap.xml                         # SEO sitemap
├── robots.txt                          # Robots file
├── site.webmanifest                    # PWA manifest
└── TESTING-CHECKLIST.md                # Pre-launch checklist
```

---

## Working with Site Config

**CRITICAL: Always reference site-config.json**

When building any page:
1. Import or read site-config.json
2. Use data from config, never hardcode
3. If data is missing, add it to config first
4. Keep config as single source of truth

Example JavaScript to load config:
```javascript
// Load site config
fetch('/site-config.json')
  .then(response => response.json())
  .then(config => {
    // Use config data
    document.getElementById('phone').href = `tel:${config.business.contact.phone}`;
    document.getElementById('email').href = `mailto:${config.business.contact.email}`;
    // etc.
  });
```

---

## Deployment Instructions

### Before Launch:
1. Update all [PLACEHOLDER] values in site-config.json
2. Configure Class Manager integration URLs
3. Set up Google Analytics
4. Add actual business hours
5. Add phone number
6. Add social media links
7. Run through TESTING-CHECKLIST.md
8. Get client approval on all content

### Git Deployment:
```bash
# Initialize repository
git init
git remote add origin https://github.com/BcomServicesLimited/undrgrnd.git

# Add all files
git add .
git commit -m "Initial UNDRGRND Movement website build"

# Push to main branch
git push -u origin main
```

### Hosting Options:
- **Netlify**: Drag & drop deployment, auto HTTPS
- **Vercel**: Git integration, auto deploy
- **GitHub Pages**: Free hosting from repo
- **Traditional hosting**: Upload via FTP to web host

---

## Troubleshooting Guide

### Common Issues:

**Issue: Class Manager iframe not loading**
- Check booking.timetable_url in site-config.json
- Ensure Class Manager allows iframe embedding
- Check browser console for CORS errors
- Test direct URL in new tab
- Show fallback contact info if iframe fails

**Issue: Images not displaying**
- Verify image paths are correct
- Check file extensions (.jpg vs .png)
- Ensure images are in /images/ directory
- Check for case sensitivity in filenames

**Issue: Navigation not highlighting active page**
- Verify JavaScript is loading
- Check that URL matching logic is correct
- Ensure nav links have correct href attributes

**Issue: Forms not submitting**
- Check form action URL
- Verify email service (Formspree, etc.) is configured
- Check browser console for JavaScript errors
- Test with different browsers

**Issue: Schema markup errors**
- Validate at schema.org validator
- Check that all required properties are present
- Ensure date formats are correct
- Verify URLs are absolute (not relative)

**Issue: Poor mobile performance**
- Compress images further
- Minimize CSS and JavaScript
- Remove unused code
- Enable caching headers
- Use WebP format for images

---

## Maintenance & Updates

### To Add a New Program:
1. Add program data to site-config.json in appropriate section
2. Create new program page using program-template.html
3. Update adults.html or kids.html to include new program card
4. Add to sitemap.xml
5. Update timetable filters if new category
6. Generate AI hero image for program
7. Test all links and functionality

### To Update Contact Information:
1. Update site-config.json business.contact section
2. All pages will automatically reflect changes (if using JavaScript to populate)
3. Update Google My Business listing to match
4. Update schema markup (should auto-update from config)

### To Change Pricing:
1. Update estimated_pricing in site-config.json for affected programs
2. All program pages will reflect new pricing
3. Add note about when pricing was last updated

### To Add Testimonials:
1. Create testimonials section in site-config.json
2. Add testimonial component to homepage
3. Add to about.html
4. Add review schema markup
5. Display on relevant program pages

---

## Final Notes for Manus

- Every prompt is designed to be self-contained and executable
- Always start by reading site-config.json
- Never hardcode data that should come from config
- Follow the file structure exactly
- Test each component as you build it
- Use semantic HTML5 elements
- Maintain accessibility standards (WCAG AA)
- Optimize for mobile-first
- Keep code clean and well-commented
- Commit regularly to Git with descriptive messages

**The entire website is data-driven from site-config.json. This makes it easy to:**
- Update content without touching code
- Add new programs quickly
- Maintain consistency across pages
- Diagnose issues by checking one source
- Scale the site as the business grows

Good luck building! The structure is designed to be maintainable, scalable, and SEO-optimized for local search in Gold Coast and Southport.
