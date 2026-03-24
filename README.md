# UNDRGRND Movement Website

Official website for UNDRGRND Movement — Gold Coast's premier movement studio offering dance, pole fitness, yoga, and aerial classes.

## Live Site
- **Domain:** https://www.undrgrnd.com.au
- **Repository:** https://github.com/BcomServicesLimited/BcomITSolutionsPROJECT

## Location
- **Studio:** Inside Flips Academy, 163 Ferry Rd, Southport QLD 4215
- **Phone:** 0721 402 690
- **Email:** undrgrndgc@gmail.com
- **Booking:** https://undrgrnd-movement.classmanager.com/register

## 🏗️ Built With
- HTML5 (semantic markup)
- CSS3 (custom styles, no frameworks)
- Vanilla JavaScript
- Class Manager booking integration

## 📁 File Structure

```
/
├── index.html                          # Homepage
├── adults.html                         # Adults landing page
├── kids.html                           # Kids landing page
├── timetable.html                      # Booking calendar
├── about.html                          # About page
├── contact.html                        # Contact page
├── privacy-policy.html                 # Privacy policy
├── terms-of-service.html               # Terms of service
├── 404.html                            # Error page
├── sitemap.xml                         # SEO sitemap
├── robots.txt                          # Crawl rules
├── site-config.json                    # Single source of truth for all data
│
├── programs/                                       # Individual program pages
│   │
│   ├── ADULTS — DANCE
│   ├── afro-groove-foundations.html                # Afro Groove - Foundations (ACTIVE)
│   ├── booty-burn-foundations.html                 # Booty Burn - Foundations (ACTIVE, NEW 2026)
│   ├── movement-flow-foundations.html              # Movement Flow - Foundations (ACTIVE)
│   ├── recovery-movement-flow-foundations.html     # Recovery Movement Flow - Foundations (COMING SOON)
│   │
│   ├── ADULTS — POLE
│   ├── pole-fitness-foundations.html               # Pole Fitness - Foundations (COMING SOON)
│   ├── pole-flow-foundations.html                  # Pole Flow - Foundations (COMING SOON)
│   ├── pole-strength-movement.html                 # Pole Strength & Movement - Foundations (ACTIVE)
│   │
│   ├── ADULTS — YOGA
│   ├── fusion-yoga-foundations.html                # Fusion Yoga - Foundations (ACTIVE)
│   ├── traditional-yoga-foundations.html           # Traditional Yoga - Foundations (ACTIVE)
│   ├── flow-yoga-foundations.html                  # Flow Yoga - Foundations (ACTIVE)
│   ├── aerial-yoga-foundations.html                # Aerial Yoga - Foundations (ACTIVE)
│   │
│   ├── ADULTS — AERIAL
│   ├── aerial-silks-foundations.html               # Aerial Silks - Foundations (ACTIVE)
│   │
│   ├── ADULTS — CHOREOGRAPHY
│   ├── choreography-fusion-foundations.html        # Choreography Fusion - Foundations (ACTIVE)
│   │
│   ├── KIDS — DANCE
│   ├── kids-dance-moves.html                       # Dance Moves (Urban Mix) - Foundations (ACTIVE)
│   ├── kids-modern-contemporary.html               # Modern Contemporary (Rhythm & Motion) - Foundations (ACTIVE)
│   ├── kids-creative-dance.html                    # Creative Dance - Foundations (ACTIVE)
│   │
│   ├── KIDS — YOGA
│   ├── kids-yoga.html                              # Kids Yoga - Foundations (ACTIVE)
│   ├── kids-aerial-yoga.html                       # Kids Aerial Yoga - Foundations (COMING SOON)
│   │
│   ├── KIDS — POLE
│   ├── kids-pole-foundations.html                  # Pole Fitness Kids - Foundations (COMING SOON)
│   │
│   └── KIDS — AERIAL
│       └── kids-aerial-silks.html                  # Kids Aerial Silks - Foundations (COMING SOON)
│
├── css/
│   └── global.css                      # Main stylesheet (design tokens from site-config.json)
│
├── js/
│   └── schema-generator.js             # JSON-LD schema markup generator
│
├── components/
│   ├── nav-component.html              # Navigation (reusable)
│   └── footer-component.html          # Footer (reusable)
│
└── images/
    ├── hero/                                       # Hero images (desktop + mobile WebP)
    └── undgrnd-logo.png                            # UNDRGRND Movement logo
```

## 🚀 Deployment

### Before Launch Checklist
- [ ] Update `site-config.json` with actual business details (phone, social media URLs)
- [ ] Configure Class Manager booking URLs in `site-config.json → booking`
- [ ] Add Google Analytics GA4 tracking code to `site-config.json → analytics.ga4_id`
- [ ] Add Facebook Pixel ID to `site-config.json → analytics.facebook_pixel_id`
- [ ] Add Google Tag Manager ID to `site-config.json → analytics.gtm_id`
- [ ] Set up SSL certificate (HTTPS)
- [ ] Test all contact forms
- [ ] Verify all internal links work
- [ ] Check mobile responsiveness on real devices
- [ ] Run accessibility audit (WCAG 2.1 AA)
- [ ] Submit sitemap to Google Search Console
- [ ] Set up and verify Google My Business listing
- [ ] Replace all image placeholders with real photography
- [ ] Test booking integration (Class Manager iframe)

### Deploy to GitHub
```bash
git init
git add .
git commit -m "Initial website deployment"
git remote add origin https://github.com/BcomServicesLimited/undrgrnd.git
git push -u origin main
```

### Deploy to Hosting

**Option 1: Netlify (Recommended)**
1. Connect GitHub repo at https://app.netlify.com
2. Set publish directory to `/` (root)
3. Auto-deploys on every push to `main`
4. HTTPS automatically configured
5. Add custom domain `undrgrnd.com.au` in site settings

**Option 2: Traditional Hosting**
1. Upload all files via FTP to public root (e.g. `public_html/`)
2. Configure domain DNS — point A record to hosting IP
3. Install SSL certificate (Let's Encrypt or provider certificate)
4. Test live site across devices and browsers

## ⚙️ Configuration

All website data is stored in `site-config.json` — the **single source of truth**. Never hardcode business details, colours, program information, or pricing directly into HTML files. All pages fetch and render data from this file at runtime.

Key sections in `site-config.json`:

| Section | Contents |
|---|---|
| `project` | Name, tagline, domain, repository |
| `business` | Legal name, address, contact details, hours |
| `design` | Colours, fonts, spacing, effects |
| `navigation` | Menu items, CTA button |
| `programs.adults` | All 13 adult programs (dance, pole, yoga, aerial, choreography) |
| `programs.adults.intensity_groups` | Intensity group definitions (balanced, moderate, active) |
| `programs.kids` | All 7 kids programs |
| `programs.kids.age_bands` | Age band definitions (4–7, 8–12, 13–16) |
| `booking` | Class Manager integration URLs |
| `legal` | Disclaimers, waiver, privacy summary, COVID policy |
| `instructor` | Instructor bio, qualifications, philosophy |
| `analytics` | GA4, Facebook Pixel, GTM IDs |

## 📊 SEO
- Local SEO optimised for Gold Coast and Southport
- JSON-LD schema markup on all pages (LocalBusiness, DanceSchool, YogaStudio, Service, FAQPage, BreadcrumbList)
- XML sitemap with 27 URLs at `/sitemap.xml`
- `robots.txt` allows all crawlers
- NAP (Name, Address, Phone) consistency across all pages
- Mobile-first responsive design
- Semantic HTML5 with ARIA attributes

## Contact
- **Email:** undrgrndgc@gmail.com
- **Phone:** 0721 402 690
- **Studio:** Inside Flips Academy, 163 Ferry Rd, Southport QLD 4215

## 📄 License
© 2026 UNDRGRND Movement. All rights reserved.
