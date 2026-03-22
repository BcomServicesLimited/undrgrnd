# UNDRGRND Movement Website - Quality Control & Validation Guide

## Data Validation Rules

### For site-config.json

All data must pass these validation rules before deployment:

#### Business Information
- ✓ `business.address.street`: Must match Google My Business exactly
- ✓ `business.address.suburb`: "Southport" (capital S)
- ✓ `business.address.state`: "QLD" (uppercase)
- ✓ `business.address.postcode`: "4215" (4 digits)
- ✓ `business.contact.email`: Valid email format (contains @)
- ✓ `business.contact.phone`: Australian phone format
- ✓ Geo coordinates: Within Gold Coast area (-27.9 to -28.2 lat, 153.3 to 153.6 long)

#### Program Data
Each program object must have:
- ✓ `id`: Unique identifier (lowercase, hyphens)
- ✓ `name`: Display name
- ✓ `slug`: URL-friendly (matches id)
- ✓ `category`: One of [Dance, Pole Fitness, Yoga, Aerial, Choreography]
- ✓ `level`: Specified
- ✓ `short_description`: 100-200 characters
- ✓ `estimated_pricing`: At least one price option

Optional but recommended:
- `full_description`: 300-500 words
- `core_focus`: Array of 3-6 items
- `who_its_for`: Array of 4-6 items
- `what_to_expect`: Array of 5-7 items

#### Color Values
All colors must be valid hex codes:
- ✓ Format: `#RRGGBB`
- ✓ Six characters after #
- ✓ Valid hex characters (0-9, A-F)

#### URLs
All URLs must be:
- ✓ Absolute (start with http:// or https://)
- ✓ No trailing slashes (except root domain)
- ✓ URL-encoded special characters
- ✓ Working (return 200 status code)

---

## Content Quality Standards

### Text Content

**Headings (H1-H6):**
- H1: One per page, contains primary keyword + location
- H2: 3-6 per page, descriptive and keyword-rich
- H3: Used for subsections within H2 content
- Never skip heading levels (H1 → H3)

**Body Text:**
- Paragraphs: 2-4 sentences each
- Sentences: 15-25 words average
- Grade level: 8-10 (accessible to broad audience)
- Active voice preferred
- No jargon without explanation
- Inclusive language (avoid gendered terms unless specific)

**Local SEO Requirements:**
- "Gold Coast" appears 10-15 times per page
- "Southport" appears 5-10 times per page
- Suburb names appear naturally 2-3 times
- Location in first paragraph
- Location in at least one H2
- Location in meta description

**Keyword Density:**
- Primary keyword: 0.5-2.5% of content
- Secondary keywords: 0.3-1% each
- LSI keywords: Natural distribution
- No keyword stuffing
- Synonyms used for variety

### Image Standards

**File Specifications:**
- Format: WebP with JPG fallback
- Max size: 200KB per image
- Max dimensions: 2000px width
- Min dimensions: 800px width
- Aspect ratio: Consistent within sections
- Compression: 75-85% quality

**Alt Text Requirements:**
- Every image must have alt attribute
- 50-125 characters recommended
- Describe image content specifically
- Include keywords naturally if relevant
- Don't start with "Image of" or "Picture of"
- Be descriptive for screen readers

**File Naming:**
- Lowercase only
- Hyphens for spaces
- Descriptive (not IMG_1234.jpg)
- Include keyword if relevant
- Format: `category-description-location.webp`
- Example: `aerial-silks-southport-studio.webp`

---

## Code Quality Standards

### HTML

**Required Elements:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title | UNDRGRND Movement</title>
    <meta name="description" content="...">
    <link rel="canonical" href="https://www.undrgrnd.com.au/page">
    <!-- Schema markup -->
    <!-- Favicon links -->
</head>
```

**Semantic Structure:**
- Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`
- Proper nesting (no `<div>` soup)
- Logical heading hierarchy
- Descriptive class names (BEM methodology)
- ARIA labels where needed

**Validation:**
- No errors in W3C HTML Validator
- No broken links
- All forms have labels
- All inputs have associated labels
- Button text is descriptive

### CSS

**Organization:**
```css
/* 1. Reset/normalize */
/* 2. CSS variables */
/* 3. Base elements (html, body, a, etc.) */
/* 4. Layout (.container, .grid, etc.) */
/* 5. Components (.card, .button, etc.) */
/* 6. Page-specific styles */
/* 7. Utilities (.text-center, .mt-4, etc.) */
/* 8. Media queries */
```

**Best Practices:**
- Mobile-first media queries
- CSS variables for all design tokens
- No inline styles (except critical CSS)
- Logical property grouping
- Comments for complex sections
- Consistent naming (kebab-case)
- Avoid !important unless necessary

**Performance:**
- Minimize specificity
- Avoid expensive selectors
- Use shorthand properties
- Remove unused CSS
- Minify for production

### JavaScript

**Code Structure:**
```javascript
// 1. Constants and configuration
// 2. Utility functions
// 3. Component initialization
// 4. Event listeners
// 5. Main execution
```

**Best Practices:**
- Use strict mode (`'use strict';`)
- Descriptive variable names
- Const by default, let if needed, avoid var
- Arrow functions for callbacks
- Comments for complex logic
- Error handling (try/catch)
- No console.log in production

**Performance:**
- Minimize DOM manipulation
- Event delegation for dynamic content
- Debounce/throttle scroll/resize events
- Lazy load non-critical scripts
- Async/defer attributes
- Minify for production

---

## Accessibility Checklist

### WCAG 2.1 Level AA Compliance

**Perceivable:**
- [ ] All images have alt text
- [ ] Color contrast ratios ≥4.5:1 (text)
- [ ] Color contrast ratios ≥3:1 (UI components)
- [ ] Text can be resized to 200%
- [ ] No information conveyed by color alone

**Operable:**
- [ ] All functionality available via keyboard
- [ ] No keyboard traps
- [ ] Skip navigation link present
- [ ] Focus indicators visible
- [ ] Touch targets ≥44x44px

**Understandable:**
- [ ] Language specified (lang="en")
- [ ] Consistent navigation
- [ ] Predictable interaction patterns
- [ ] Error messages are clear
- [ ] Labels and instructions for forms

**Robust:**
- [ ] Valid HTML
- [ ] ARIA used correctly
- [ ] Name, role, value for UI components
- [ ] Status messages use role="status"

### Testing Tools:
- **WAVE**: https://wave.webaim.org/
- **axe DevTools**: Browser extension
- **Lighthouse**: Chrome DevTools
- **Screen reader**: NVDA (Windows) or VoiceOver (Mac)

---

## SEO Quality Checklist

### On-Page SEO

**Meta Tags:**
- [ ] Unique title per page (50-60 characters)
- [ ] Unique description per page (150-160 characters)
- [ ] Primary keyword in title
- [ ] Location in title
- [ ] Primary keyword in description
- [ ] Location in description

**Content Structure:**
- [ ] H1 contains primary keyword + location
- [ ] 800-1200 words minimum (content pages)
- [ ] Keywords in first paragraph
- [ ] Keywords in at least one H2
- [ ] Internal links to relevant pages (3-5 per page)
- [ ] External links to authoritative sources (if applicable)

**Schema Markup:**
- [ ] LocalBusiness schema on every page
- [ ] Breadcrumb schema on internal pages
- [ ] Service schema on program pages
- [ ] FAQ schema where applicable
- [ ] Validates at schema.org validator

**Images:**
- [ ] Alt text contains keywords (naturally)
- [ ] File names are descriptive
- [ ] Proper image size/compression
- [ ] Lazy loading implemented

**Technical SEO:**
- [ ] HTTPS enabled
- [ ] Mobile-friendly (Google test)
- [ ] Page speed <3 seconds
- [ ] No broken links (404s)
- [ ] XML sitemap present
- [ ] Robots.txt allows crawling
- [ ] Canonical tags set
- [ ] Structured URLs (no ?id=123)

### Local SEO Specific

**NAP Consistency:**
- [ ] Name identical everywhere
- [ ] Address identical everywhere (abbreviations match)
- [ ] Phone number format consistent
- [ ] Appears in footer of every page
- [ ] Matches Google My Business exactly

**Local Keywords:**
- [ ] City name in title
- [ ] City name in H1
- [ ] City name in meta description
- [ ] Suburb name in content
- [ ] Service area mentioned
- [ ] Local landmarks referenced

**Schema Specific:**
- [ ] Geo coordinates accurate
- [ ] Service area defined
- [ ] Opening hours specified
- [ ] Price range indicated
- [ ] Multiple business types listed

---

## Performance Benchmarks

### Target Metrics

**Google PageSpeed Insights:**
- Performance: ≥90
- Accessibility: ≥95
- Best Practices: ≥90
- SEO: 100

**Core Web Vitals:**
- Largest Contentful Paint (LCP): <2.5s
- First Input Delay (FID): <100ms
- Cumulative Layout Shift (CLS): <0.1

**Page Size Targets:**
- HTML: <50KB
- CSS: <100KB
- JavaScript: <200KB
- Images (total): <1MB
- Total page weight: <2MB

**Loading Performance:**
- First Contentful Paint: <1.8s
- Time to Interactive: <3.5s
- Speed Index: <3.0s
- Total Blocking Time: <200ms

### Optimization Techniques

**Images:**
- WebP format with fallbacks
- Responsive srcset
- Lazy loading (loading="lazy")
- Proper sizing (no scaling in browser)
- Compression (75-85% quality)
- CDN delivery (if using)

**CSS:**
- Critical CSS inline
- Non-critical CSS async
- Remove unused styles
- Minify production files
- Combine files where possible

**JavaScript:**
- Defer non-critical scripts
- Async where appropriate
- Minify production files
- Remove console.logs
- Code splitting for large apps
- Tree shaking unused code

**Fonts:**
- Preload critical fonts
- Font-display: swap
- Subset fonts (only needed characters)
- WOFF2 format
- Limit font weights/styles

**Caching:**
- Browser caching headers
- Service worker (if PWA)
- CDN caching
- Cache busting for updates

---

## Security Checklist

### Before Launch

**HTTPS:**
- [ ] SSL certificate installed
- [ ] All resources loaded via HTTPS
- [ ] HTTP redirects to HTTPS
- [ ] HSTS header set

**Forms:**
- [ ] CSRF protection
- [ ] Spam protection (honeypot or reCAPTCHA)
- [ ] Input validation
- [ ] Email validation
- [ ] Sanitize user input

**External Resources:**
- [ ] Trusted CDNs only
- [ ] Subresource integrity (SRI) for CDN scripts
- [ ] rel="noopener" on external links
- [ ] rel="noreferrer" where privacy matters

**Code:**
- [ ] No sensitive data in client-side code
- [ ] No API keys in JavaScript
- [ ] No database credentials exposed
- [ ] No debug/console output in production
- [ ] Error messages don't reveal system info

**Headers:**
- [ ] X-Content-Type-Options: nosniff
- [ ] X-Frame-Options: SAMEORIGIN
- [ ] Referrer-Policy: strict-origin-when-cross-origin
- [ ] Content-Security-Policy defined

---

## Testing Procedures

### Manual Testing

**Functionality Test:**
1. Click every link → verify destination
2. Submit every form → verify receipt
3. Test all buttons → verify action
4. Test navigation → all pages accessible
5. Test filters → results update correctly
6. Test modals → open/close properly
7. Test mobile menu → toggles correctly

**Content Review:**
1. Read all text → no typos/errors
2. Check all images → display correctly
3. Verify contact info → all correct
4. Verify pricing → all accurate
5. Verify disclaimers → legally compliant
6. Check dates → all current
7. Verify program details → match offerings

**Responsive Testing:**
1. Mobile (375px) → all readable/functional
2. Mobile landscape (667px) → layout correct
3. Tablet (768px) → layout correct
4. Desktop (1440px) → layout correct
5. Large desktop (1920px) → not too stretched

**Browser Testing:**
1. Chrome latest → works perfectly
2. Safari latest → works perfectly
3. Firefox latest → works perfectly
4. Edge latest → works perfectly
5. Mobile Safari iOS → works perfectly
6. Mobile Chrome Android → works perfectly

### Automated Testing

**Lighthouse (Chrome DevTools):**
```bash
# Run Lighthouse audit
1. Open DevTools (F12)
2. Go to Lighthouse tab
3. Select all categories
4. Generate report
5. Fix issues with score <90
```

**W3C Validators:**
```
HTML: https://validator.w3.org/
CSS: https://jigsaw.w3.org/css-validator/
```

**Schema Validator:**
```
https://validator.schema.org/
https://search.google.com/test/rich-results
```

**Broken Link Checker:**
```
https://www.deadlinkchecker.com/
```

**PageSpeed Insights:**
```
https://pagespeed.web.dev/
```

---

## Pre-Deployment Checklist

### Critical Items

- [ ] All [PLACEHOLDER] text replaced in site-config.json
- [ ] Class Manager URLs configured and tested
- [ ] Google Analytics tracking code added
- [ ] Business hours finalized
- [ ] Contact information verified
- [ ] Social media links added
- [ ] All images optimized and uploaded
- [ ] Favicon files generated and linked
- [ ] Privacy policy reviewed by legal
- [ ] Terms of service reviewed by legal
- [ ] All program pricing verified
- [ ] Medical disclaimers legally compliant
- [ ] HTTPS certificate installed
- [ ] Domain DNS configured
- [ ] Email forwarding set up
- [ ] Backup/restore plan in place

### Final Quality Checks

- [ ] No console errors in browser
- [ ] No broken images
- [ ] No broken links (internal or external)
- [ ] All forms submit successfully
- [ ] Mobile responsive on all devices
- [ ] Cross-browser tested
- [ ] Load time <3 seconds all pages
- [ ] SEO score 100 (Lighthouse)
- [ ] Accessibility score ≥95 (Lighthouse)
- [ ] Schema markup validates
- [ ] Sitemap submitted to Google
- [ ] Google My Business verified
- [ ] Google Search Console set up
- [ ] Client approval received

---

## Post-Launch Monitoring

### Week 1 After Launch

**Daily:**
- [ ] Check Google Analytics (traffic)
- [ ] Monitor Google Search Console (errors)
- [ ] Test booking system (one test booking)
- [ ] Review contact form submissions
- [ ] Check website uptime

**Weekly:**
- [ ] Review performance metrics
- [ ] Check search rankings (branded terms)
- [ ] Review any 404 errors
- [ ] Backup website files
- [ ] Check SSL certificate status

### Monthly Maintenance

- [ ] Review analytics trends
- [ ] Update program information if needed
- [ ] Add new testimonials
- [ ] Update blog/news (if applicable)
- [ ] Check all external links still work
- [ ] Review and respond to reviews
- [ ] Update seasonal content
- [ ] Run full SEO audit
- [ ] Check mobile usability
- [ ] Review conversion rates

### Quarterly Reviews

- [ ] Comprehensive SEO audit
- [ ] Competitor analysis
- [ ] Content refresh (update dates, stats)
- [ ] Image optimization review
- [ ] Performance optimization
- [ ] Security review
- [ ] Backup testing (restore test)
- [ ] Review Google My Business insights
- [ ] Strategy session with client

---

## Emergency Procedures

### Website Down

1. Check hosting provider status
2. Verify domain DNS settings
3. Check SSL certificate
4. Review recent changes (Git history)
5. Restore from backup if needed
6. Contact hosting support
7. Post status update on social media

### Booking System Not Working

1. Test Class Manager URL directly
2. Check iframe integration
3. Verify booking URLs in site-config.json
4. Show fallback contact information
5. Email client with alternative booking method
6. Contact Class Manager support
7. Fix and test before removing fallback

### Security Breach

1. Take site offline immediately
2. Change all passwords
3. Review server logs
4. Identify vulnerability
5. Patch security hole
6. Scan for malware
7. Restore from clean backup
8. Notify hosting provider
9. File incident report
10. Monitor closely

### Data Loss

1. Don't panic
2. Check Git repository (latest commit)
3. Check hosting provider backups
4. Check local backups
5. Restore from most recent backup
6. Verify data integrity
7. Test all functionality
8. Document what was lost
9. Improve backup procedures

---

## Version Control Best Practices

### Commit Messages

**Format:**
```
[Type] Brief description (50 chars max)

Optional detailed explanation of what changed and why.
Reference issue numbers if applicable.
```

**Types:**
- `[FEAT]` New feature
- `[FIX]` Bug fix
- `[CONTENT]` Content update
- `[STYLE]` CSS/design changes
- `[REFACTOR]` Code restructure (no functionality change)
- `[DOCS]` Documentation update
- `[CONFIG]` Configuration changes

**Examples:**
```
[FEAT] Add medical clearance modal for recovery classes
[FIX] Correct contact email in footer
[CONTENT] Update Afro Groove pricing and description
[STYLE] Adjust mobile menu spacing
[CONFIG] Update Class Manager booking URLs
```

### Branching Strategy

**Main branches:**
- `main` → Production-ready code
- `develop` → Development/staging
- `feature/[name]` → New features
- `hotfix/[issue]` → Emergency fixes

**Workflow:**
1. Create feature branch from develop
2. Make changes and commit
3. Test thoroughly
4. Merge to develop
5. Test on staging
6. Merge to main
7. Deploy to production

---

## Documentation Maintenance

Keep these files up to date:

- `BUILD-INSTRUCTIONS.md` → When build process changes
- `QUICK-REFERENCE.md` → When adding common tasks
- `TESTING-CHECKLIST.md` → When adding test requirements
- `site-config.json` → When data structure changes
- `README.md` → Overview and setup instructions
- This file → When adding quality standards

**Review quarterly** to ensure accuracy.

---

This quality control guide ensures the UNDRGRND Movement website maintains professional standards for code, content, performance, accessibility, and SEO.
