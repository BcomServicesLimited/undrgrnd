# UNDGRND Movement Website - Quick Reference Guide

## For Non-Technical Updates

### How to Update Contact Information
1. Open `site-config.json`
2. Find the `business.contact` section
3. Update email, phone, social media links
4. Save the file
5. The website will automatically use new information

### How to Change Business Hours
1. Open `site-config.json`
2. Find `business.hours` section
3. Update days and times
4. Save the file

### How to Add a New Program
1. Open `site-config.json`
2. Find either `programs.adults` or `programs.kids`
3. Find the correct category (dance, pole, yoga, aerial)
4. Copy an existing program object
5. Update all the fields with new program details
6. Create a new HTML page in `/programs/` folder using the template
7. Add the program to the adults.html or kids.html listing

### How to Update Pricing
1. Open `site-config.json`
2. Find the program you want to update
3. Update the `estimated_pricing` section
4. Save the file
5. The program page will show new pricing

---

## For Manus: Common Commands

### Building Individual Pages

**Homepage:**
```
Follow BUILD-INSTRUCTIONS.md Step 2 (Prompts 2.1 and 2.2)
```

**Adults Page:**
```
Follow BUILD-INSTRUCTIONS.md Step 3 (Prompts 3.1 and 3.2)
```

**Individual Program Page:**
```
Follow BUILD-INSTRUCTIONS.md Step 5
Use program-template.html as base
Pull data from site-config.json for specific program
```

### Testing Checklist
```
Follow TESTING-CHECKLIST.md in Step 12.1
Run through all items before considering page complete
```

---

## File Locations Quick Reference

| What | Where |
|------|-------|
| Configuration | `/site-config.json` |
| Homepage | `/index.html` |
| CSS Styles | `/css/global.css` |
| Navigation | `/components/nav-component.html` |
| Footer | `/components/footer-component.html` |
| Program Pages | `/programs/[program-slug].html` |
| Images | `/images/` subdirectories |
| JavaScript | `/js/` |

---

## Color Reference (from brand)

```css
--primary-purple: #8B5CF6
--accent-purple: #A78BFA
--pink-accent: #EC4899
--dark-bg: #0A0A0A
--card-bg: #1A1A1A
--text-white: #FFFFFF
--text-gray: #A1A1A1
```

---

## SEO Checklist for Every Page

- [ ] Unique `<title>` tag with "Gold Coast" and location
- [ ] Meta description <160 characters
- [ ] H1 tag with primary keyword
- [ ] Schema markup in `<head>`
- [ ] All images have alt text
- [ ] Internal links to other pages
- [ ] NAP (Name, Address, Phone) in footer
- [ ] Mention "Gold Coast" or "Southport" 10+ times
- [ ] Mobile responsive
- [ ] Load time <3 seconds

---

## Git Commands

### First Time Setup
```bash
cd /path/to/website
git init
git remote add origin https://github.com/BcomServicesLimited/undrgrnd.git
git add .
git commit -m "Initial website build"
git push -u origin main
```

### Regular Updates
```bash
# After making changes
git add .
git commit -m "Description of what you changed"
git push
```

### Creating a Backup Branch
```bash
git checkout -b backup-before-changes
git push origin backup-before-changes
git checkout main
```

---

## Emergency Contacts

**Client Email:** olga.coaching1@gmail.com
**Repository:** https://github.com/BcomServicesLimited/undrgrnd.git
**Domain:** https://www.undrgrnd.com.au

---

## Before Launch Checklist

Critical items to update in `site-config.json`:

```json
{
  "business": {
    "contact": {
      "phone": "[UPDATE THIS]",
      "instagram": "[UPDATE THIS]",
      "facebook": "[UPDATE THIS]"
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

After updating config:
1. Test all pages locally
2. Run through TESTING-CHECKLIST.md
3. Get client approval
4. Deploy to production
5. Submit sitemap to Google Search Console
6. Set up Google My Business
7. Configure Class Manager integration

---

## Common AI Image Prompts

Use these for generating images with DALL-E or similar:

**Homepage Hero:**
```
Diverse group of people in dynamic movement poses, dance and aerial movements, 
purple and pink gradient dramatic lighting, dark background, professional 
fitness photography, energetic and empowering atmosphere
```

**Afro Groove:**
```
Athletic flexible African woman in dynamic Afro dance pose, hip movement 
emphasis, energetic expression, purple and pink gradient lighting, dark 
background, professional fitness photography
```

**Aerial Silks:**
```
Graceful flexible woman suspended on aerial silks in beautiful wrap position, 
strength and elegance, purple dramatic lighting, dark background, professional 
aerial arts photography
```

**Pole Fitness:**
```
Strong flexible woman demonstrating pole fitness grip, focused expression, 
controlled positioning, athletic wear, purple accent lighting, professional 
pole fitness studio photography
```

**Yoga:**
```
Flexible woman in advanced yoga pose (specify pose), serene focused expression, 
purple ambient lighting, minimal background, professional yoga photography
```

**Kids Classes:**
```
Diverse group of children ages 8-12 in playful movement poses, joyful 
expressions, colorful athletic wear, bright energetic lighting, safe studio 
environment, professional photography
```

---

## Support Resources

- **HTML Reference:** https://developer.mozilla.org/en-US/docs/Web/HTML
- **CSS Reference:** https://developer.mozilla.org/en-US/docs/Web/CSS
- **Schema Markup:** https://schema.org
- **Google SEO:** https://developers.google.com/search/docs
- **Accessibility:** https://www.w3.org/WAI/WCAG21/quickref/
- **Netlify Docs:** https://docs.netlify.com
- **Git Tutorial:** https://git-scm.com/docs

---

## Performance Targets

Aim for these Google PageSpeed scores:

- **Performance:** >90
- **Accessibility:** >95
- **Best Practices:** >90
- **SEO:** 100

Key metrics:
- First Contentful Paint: <1.8s
- Largest Contentful Paint: <2.5s
- Time to Interactive: <3.5s
- Total page size: <2MB
- Image file sizes: <200KB each

---

## Updating This Guide

When you make significant changes or additions:

1. Document the change in this file
2. Update BUILD-INSTRUCTIONS.md if process changes
3. Update site-config.json if new data fields added
4. Commit with clear message: `git commit -m "Updated docs: [what changed]"`
