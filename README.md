# UNDRGRND Movement — Website

Static marketing site for **UNDRGRND Movement**, a Gold Coast movement studio (dance, pole, yoga, aerial — adults & kids) serving Surfers Paradise & surrounding areas. It operates as a service-area business — class times and locations are flexible and confirmed when the customer gets in touch.

- **Live:** https://www.undrgrnd.com.au
- **Repo:** https://github.com/BcomServicesLimited/undrgrnd
- **Hosting:** Cloudflare Pages — **auto-deploys on every push to `main`**. No build step; the repo root is served as-is.

## Contact / NAP (canonical)
- **Service area:** Surfers Paradise & surrounding areas · Gold Coast QLD (no fixed venue — locations are flexible, confirmed on contact)
- **Phone:** 0721 402 690  ·  **Email:** undrgrndgc@gmail.com

## Stack
Hand-written HTML5 + one stylesheet (`css/global.css`) + vanilla JS. No framework, no bundler.

## Structure
```
/                         Home, adults, kids, enrol, about, contact, learn, legal, 404
/programs/*.html          18 individual program pages
/learn/*.html             8 SEO/blog articles
/css/global.css           Shared design tokens + utilities
/js/booking-controller.js Term-aware Stripe booking links (see below)
/js/schema-generator.js   Runtime JSON-LD schema injection
/site-config.json         Business data, navigation, programs (consumed at runtime)
/images/                  hero/, learn/, programs/, instructor/, logo/
/_redirects               301s for old/retired URLs
/sitemap.xml /robots.txt /llms.txt
```

## Booking & pricing
`js/booking-controller.js` is the single source of truth for booking links. Pricing is **$35/class**, paid upfront for the classes remaining in the current QLD school term. It holds the term date ranges and 10 pre-made Stripe links (1–10 weeks, $35–$350) and rewrites every `.dance-booking-button` at runtime. It also exposes `window.UNDRGRND_Booking` so `enrol.html` can build its term buttons from the same data.

## Currently bookable (active)
Only the live classes sell via Stripe Buy Now; everything else shows **Join Waitlist**. The Enrol page shows no class times/dates — customers contact UNDRGRND to arrange a time.

- Movement Flow, Booty Burn Dance, Aerial Silks, Stretch & Mobility, Fusion Yoga, Pole Fitness (adults)
- Urban Mix / Kids Dance Moves, Kids Creative Dance (kids)

Program status (`active` vs `coming_soon`) lives in `site-config.json`; the adults/kids landing pages build their cards from it.

## Editing
- **Business data, contact, hours, programs:** `site-config.json`.
- **Booking prices/terms/Stripe links:** `js/booking-controller.js` (creating a new Stripe link is required for any new price point).
- **Nav/footer:** currently inlined per page (kept in sync via the per-page populate JS). Consolidating these into a shared include is a known follow-up.

## Deploy
`git add … && git commit && git push` to `main` → Cloudflare Pages deploys automatically.

© 2026 UNDRGRND Movement. All rights reserved.
