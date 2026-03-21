# UNDGRND Movement Website - Complete Build System

## 🎯 Project Overview

This is a comprehensive, production-ready website build system for **UNDGRND Movement**, a Gold Coast movement studio offering dance, pole fitness, yoga, and aerial classes for adults and children.

**Repository:** https://github.com/BcomServicesLimited/undrgrnd.git  
**Domain:** https://www.undrgrnd.com.au  
**Location:** 163 Ferry Rd, Southport QLD 4215

---

## 📁 What You've Received

This package contains everything Manus needs to build a professional, SEO-optimized, LLM-friendly website:

### 1. **site-config.json** (22KB)
The **single source of truth** for the entire website. Contains:
- Business details (address, contact, hours)
- All program descriptions and pricing
- Design tokens (colors, fonts, spacing)
- SEO keywords and local areas
- Legal disclaimers
- Navigation structure
- Analytics configuration

**⚠️ CRITICAL:** Never hardcode data. Always reference this file.

### 2. **BUILD-INSTRUCTIONS.md** (46KB)
Step-by-step prompts for Manus to build the entire website. Includes:
- **12 detailed build steps** with specific prompts
- Shared components (navigation, footer, schema)
- All page templates with exact requirements
- Integration instructions for Class Manager
- Testing procedures
- Deployment guidelines

**How to use:** Follow the prompts in order, step by step.

### 3. **QUICK-REFERENCE.md** (6.3KB)
Fast lookup guide for:
- Common update tasks (changing contact info, pricing, etc.)
- File locations
- Color codes
- Git commands
- SEO checklists
- AI image prompts
- Emergency contacts

**How to use:** Quick answers without reading full instructions.

### 4. **QUALITY-CONTROL.md** (17KB)
Comprehensive quality standards covering:
- Data validation rules
- Content quality standards (text, images)
- Code quality standards (HTML, CSS, JS)
- Accessibility checklist (WCAG 2.1 AA)
- SEO quality checklist
- Performance benchmarks
- Security checklist
- Testing procedures
- Pre-deployment checklist
- Post-launch monitoring
- Emergency procedures

**How to use:** Reference before deployment and during maintenance.

---

## 🚀 Quick Start for Manus

### Step 1: Read the Configuration
```bash
# Open and review the single source of truth
cat site-config.json
```

Understand:
- Business details
- Program structure
- Design tokens
- What needs updating before launch

### Step 2: Start Building
```bash
# Open the build instructions
cat BUILD-INSTRUCTIONS.md
```

Follow the prompts in order:
1. **Step 1:** Global CSS + Shared Components
2. **Step 2:** Homepage
3. **Step 3:** Adults Landing Page
4. **Step 4:** Kids Landing Page
5. **Step 5:** Individual Program Pages (3 priority)
6. **Step 6:** Timetable Page
7. **Step 7:** Contact Page
8. **Step 8:** About Page
9. **Step 9:** Legal Pages
10. **Step 10:** Additional Features
11. **Step 11:** Optimization
12. **Step 12:** Testing & Launch

### Step 3: Quality Check
```bash
# Before deploying, run through quality control
cat QUALITY-CONTROL.md
```

Verify:
- All data validated
- Content meets standards
- Code is clean
- Accessibility compliant
- SEO optimized
- Performance targets met

### Step 4: Deploy
```bash
# Initialize Git repository
git init
git remote add origin https://github.com/BcomServicesLimited/undrgrnd.git
git add .
git commit -m "Initial UNDGRND Movement website build"
git push -u origin main
```

---

## 🎨 Design System

### Colors (from brand logo)
```css
--primary-purple: #8B5CF6
--accent-purple: #A78BFA
--pink-accent: #EC4899
--dark-bg: #0A0A0A
--card-bg: #1A1A1A
--text-white: #FFFFFF
--text-gray: #A1A1A1
```

### Typography
- **Display Font:** Bebas Neue (headings, hero text)
- **Body Font:** Outfit (weights: 300, 400, 600, 700, 800)

### Design Philosophy
- **Aesthetic:** Bold, underground/edgy sophistication
- **Contrast:** High contrast purple neon on deep blacks
- **Style:** Geometric minimalism meets organic movement
- **Vibe:** Professional yet accessible, empowering yet welcoming

---

## 📊 SEO Strategy

### Local SEO Focus
**Primary Location:** Southport, Gold Coast, QLD  
**Service Area:** Gold Coast and surrounding suburbs

**Target Keywords:**
- dance school gold coast
- yoga studio southport
- pole fitness gold coast
- aerial classes southport
- kids dance classes gold coast
- beginner dance fitness gold coast

**Content Requirements:**
- "Gold Coast" mentioned 10-15 times per page
- "Southport" mentioned 5-10 times per page
- 800-1200 words per content page
- Schema markup on every page
- NAP consistency (Name, Address, Phone)

### LLM-First Design
Structured for AI assistants to easily parse and recommend:
- Comprehensive JSON-LD schema on every page
- Semantic HTML5 structure
- Clear heading hierarchy
- FAQ schema where applicable
- Breadcrumb navigation
- Descriptive alt text

---

## 🔧 Technical Specifications

### Platform
- **Type:** Multi-page HTML website
- **Why:** Better SEO, easier to crawl, simpler Class Manager integration
- **Tech Stack:**
  - HTML5 (semantic markup)
  - CSS3 (custom, no heavy frameworks)
  - Vanilla JavaScript (minimal, performant)
  - Class Manager integration (iframe embed)

### Performance Targets
- **Load Time:** <3 seconds
- **PageSpeed Score:** >90 (all metrics)
- **Page Weight:** <2MB total
- **Image Size:** <200KB each

### Browser Support
- Chrome (latest)
- Safari (latest)
- Firefox (latest)
- Edge (latest)
- Mobile Safari iOS
- Mobile Chrome Android

---

## 📱 Key Features

### Class Manager Integration
- **System:** Class Manager booking platform
- **Integration:** iframe embed (placeholder provided)
- **Location:** Timetable page (main), CTAs throughout site
- **Fallback:** Contact form if booking system unavailable

### Medical Clearance System
- **Trigger:** Recovery Movement classes require medical clearance
- **Implementation:** Modal disclaimer before booking
- **Content:** From site-config.json legal section
- **Compliance:** Australian/Queensland legislation

### Multi-Environment Approach
Classes held in:
- Studio (163 Ferry Rd, Southport)
- Beach (Gold Coast beaches)
- Park (outdoor natural settings)

Referenced in WHO and IADMS recommendations.

---

## 📋 Before Launch Checklist

**Critical Updates in site-config.json:**

```json
{
  "business": {
    "contact": {
      "phone": "[UPDATE]",
      "instagram": "[UPDATE]", 
      "facebook": "[UPDATE]"
    },
    "hours": {
      "note": "[UPDATE WITH ACTUAL HOURS]"
    }
  },
  "booking": {
    "timetable_url": "[INSERT CLASS MANAGER URL]",
    "booking_widget_url": "[INSERT CLASS MANAGER URL]"
  },
  "analytics": {
    "google_analytics_id": "[ADD GA4 ID]"
  }
}
```

**Additional Pre-Launch Tasks:**
- [ ] Generate favicon set from logo
- [ ] Create AI-generated hero images
- [ ] Set up Google Analytics
- [ ] Configure Class Manager integration
- [ ] Test all forms
- [ ] Run full quality control checklist
- [ ] Get client approval
- [ ] Set up Google My Business
- [ ] Submit sitemap to Google Search Console

---

## 🗂️ Expected File Structure

After build completion:

```
/undrgrnd-website/
├── index.html                    # Homepage
├── adults.html                   # Adults landing
├── kids.html                     # Kids landing
├── timetable.html                # Booking integration
├── contact.html                  # Contact page
├── about.html                    # About page
├── privacy-policy.html           # Legal
├── terms-of-service.html         # Legal
├── 404.html                      # Error page
│
├── programs/                     # Individual programs
│   ├── afro-groove-foundations.html
│   ├── aerial-silks.html
│   ├── pole-fitness-foundations.html
│   └── [17 other program pages]
│
├── css/
│   ├── global.css               # Main stylesheet
│   └── components.css           # Component styles
│
├── js/
│   ├── schema-generator.js      # Schema markup
│   ├── navigation.js            # Nav functionality
│   ├── class-finder.js          # Homepage finder
│   └── [other scripts]
│
├── components/
│   ├── nav-component.html       # Reusable nav
│   ├── footer-component.html    # Reusable footer
│   └── medical-clearance-modal.html
│
├── images/
│   ├── hero/                    # Hero images
│   ├── programs/                # Program images
│   └── favicons/                # Favicon set
│
├── site-config.json             # SINGLE SOURCE OF TRUTH
├── sitemap.xml                  # SEO sitemap
├── robots.txt                   # Crawl instructions
└── README.md                    # This file
```

---

## 👥 Roles & Responsibilities

### Manus (AI Build Agent)
- Follow BUILD-INSTRUCTIONS.md step by step
- Pull all data from site-config.json
- Generate HTML, CSS, JavaScript files
- Create AI images using provided prompts
- Validate code and content quality
- Run pre-deployment tests

### Developer/Maintainer
- Update site-config.json placeholders
- Configure Class Manager integration
- Set up hosting and domain
- Install SSL certificate
- Configure Google Analytics
- Monitor post-launch performance

### Client (UNDGRND Movement)
- Provide final business details
- Approve all content
- Configure Class Manager account
- Provide actual class schedule
- Manage bookings and inquiries

---

## 🔍 How This System Works

### Single Source of Truth
All data lives in **site-config.json**. Benefits:
- ✅ Update once, change everywhere
- ✅ Easy to maintain
- ✅ Prevents inconsistencies
- ✅ Simple to audit
- ✅ Version controlled

### Data-Driven Pages
Every page is built using prompts that reference site-config.json:
- Pull business details
- Insert program descriptions
- Use design tokens
- Apply legal disclaimers
- Configure navigation

### Prompt-Based Build
BUILD-INSTRUCTIONS.md contains **exact prompts** to give Manus:
- Clear, specific requirements
- No ambiguity
- Repeatable process
- Quality guaranteed
- Easy to modify

---

## 🆘 Support & Resources

### Documentation Files
1. **BUILD-INSTRUCTIONS.md** → How to build everything
2. **QUICK-REFERENCE.md** → Fast answers
3. **QUALITY-CONTROL.md** → Standards and checklists
4. **site-config.json** → All website data
5. **README.md** → This overview

### External Resources
- HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
- CSS: https://developer.mozilla.org/en-US/docs/Web/CSS
- Schema: https://schema.org
- SEO: https://developers.google.com/search
- Accessibility: https://www.w3.org/WAI/WCAG21/quickref/

### Contact
- **Client Email:** olga.coaching1@gmail.com
- **Repository:** https://github.com/BcomServicesLimited/undrgrnd.git

---

## 🎯 Success Criteria

The website is ready to launch when:

**Technical:**
- ✅ All pages load in <3 seconds
- ✅ Mobile responsive on all devices
- ✅ No broken links or images
- ✅ Class Manager integration works
- ✅ Forms submit successfully
- ✅ HTTPS enabled

**SEO:**
- ✅ PageSpeed score >90
- ✅ Schema markup validates
- ✅ All pages indexed by Google
- ✅ Local keywords ranking
- ✅ Google My Business verified

**Content:**
- ✅ All placeholders replaced
- ✅ Legal disclaimers approved
- ✅ Program details accurate
- ✅ Contact information correct
- ✅ Images professional quality

**User Experience:**
- ✅ Easy navigation
- ✅ Clear call-to-actions
- ✅ Booking flow intuitive
- ✅ Accessibility compliant
- ✅ Fast loading

---

## 📈 Post-Launch

### Week 1
- Monitor Google Analytics daily
- Check booking system functionality
- Review contact form submissions
- Fix any immediate issues
- Respond to client feedback

### Month 1
- Track search rankings
- Analyze user behavior
- Optimize conversion paths
- Add testimonials
- Refine content based on data

### Quarter 1
- Comprehensive SEO audit
- Performance optimization
- Content expansion
- Competitor analysis
- Strategy refinement

---

## 💡 Key Principles

1. **Data-Driven:** Everything comes from site-config.json
2. **Mobile-First:** Designed for mobile, enhanced for desktop
3. **SEO-Optimized:** Local search dominance
4. **LLM-Friendly:** Structured for AI recommendations
5. **Accessible:** WCAG 2.1 AA compliant
6. **Fast:** Performance-optimized
7. **Maintainable:** Clean, documented code
8. **Scalable:** Easy to add programs/pages

---

## 🙏 Final Notes

This build system is designed to make Manus's job **as easy as possible** while delivering a **professional, high-quality website**.

**Follow the instructions step by step.**  
**Reference site-config.json for all data.**  
**Use QUALITY-CONTROL.md before deployment.**

The result will be a website that:
- Ranks well in local search
- Converts visitors to bookings
- Represents the UNDGRND Movement brand
- Scales with business growth
- Is easy to maintain

**Good luck with the build! 🚀**

---

*Last Updated: March 21, 2026*  
*Version: 1.0*  
*Build System Created by: Claude (Anthropic)*
