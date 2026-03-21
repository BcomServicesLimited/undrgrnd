# UNDGRND Movement — Website

Official website for **UNDGRND Movement**, a Gold Coast dance and movement studio.

---

## Project Structure

```
undrgrnd/
├── assets/
│   ├── images/          # Logo, program images, instructor photos
│   └── fonts/           # Custom font files (if self-hosted)
├── src/                 # Source code (components, pages, styles)
├── site-config.json     # ⭐ SINGLE SOURCE OF TRUTH — all site data lives here
└── README.md
```

---

## ⭐ site-config.json — Single Source of Truth

**All website data is defined in `site-config.json`.** This includes:

| Section | Contents |
|---|---|
| `site` | Site name, tagline, URL, logo path |
| `brand` | Colours, fonts, logo description |
| `business` | Contact details, address, hours, social links |
| `navigation` | Nav items and CTA button |
| `hero` | Headline, body copy, CTAs |
| `about` | About section copy and values |
| `programs` | All class/program definitions |
| `schedule` | Weekly class timetable |
| `instructors` | Instructor profiles |
| `pricing` | Pricing plans and trial offer |
| `testimonials` | Student reviews |
| `faq` | Frequently asked questions |
| `contact` | Contact form fields |
| `seo` | Page titles, descriptions, keywords |

> **Rule:** Never hardcode any business details, program information, colours, or content in components or pages. Always read from `site-config.json`.

---

## Brand Colours

| Name | Hex |
|---|---|
| Primary Purple | `#7B2FFF` |
| Accent Pink | `#FF2FBF` |
| Neon Cyan | `#00FFFF` |
| Neon Yellow | `#FFE600` |
| Background | `#000000` |
| Surface | `#1A1A1A` |
| Text | `#FFFFFF` |

---

## Development

> Build instructions will be added as the project progresses.

---

## Repository

[https://github.com/BcomServicesLimited/undrgrnd](https://github.com/BcomServicesLimited/undrgrnd)

---

*Built by [Bcom IT Solutions](https://bcomservices.com.au) for UNDGRND Movement.*
