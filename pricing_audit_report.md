# UNDRGRND Movement Pricing Audit Report

This report details all locations across the website where pricing needs to be updated to reflect the new single-price-per-class model. All mentions of "Drop-In", "Class Packs", and "Unlimited Memberships" need to be removed and replaced with the correct single class price.

## 1. Required Pricing Updates

Based on the provided screenshots, the correct single class prices are:

| Program | Correct Price |
|---|---|
| Movement Flow - Foundations | **$35.00** |
| Choreography Fusion - Foundations | **$32.00** |
| Fusion Yoga - Foundations | **$32.00** |
| Stretch & Mobility - Foundations | **$35.00** |
| Booty Burn - Foundations | **$29.00** |
| Aerial Silks - Foundations | **$35.00** |

---

## 2. Global Configuration Changes

### `site-config.json`
The central configuration file currently uses a 3-tier pricing structure for almost every adult program. This needs to be flattened.

**Current Structure (Example):**
```json
"estimated_pricing": {
  "drop_in": 25,
  "class_pack_10": 200,
  "unlimited_monthly": 180
}
```

**Required Change:**
- Remove `class_pack_10`, `class_pack_8`, and `unlimited_monthly` from all programs.
- Rename `drop_in` to `price` (or keep as `drop_in` but update the value to the correct single price).
- Update the amounts to match the table above.

---

## 3. Core Page Changes

### `index.html` (Homepage)
- **Featured Program Cards:** The 4 featured cards currently say "From **$25** drop-in". 
  - *Action:* Update to "Price: **$XX** per class" using the correct amounts.

### `adults.html`
- **Program Cards:** The dynamic card generation script currently outputs "From **$XX** per class".
  - *Action:* Update the script to remove "From" and just show the exact price.

### `about.html`
- **Text Mentions:** 
  - Line 1631: *"Drop-in, class packs, unlimited — choose what works for you."*
  - Line 1775: *"All programs are available on a drop-in basis, as class packs, or as unlimited monthly memberships..."*
  - *Action:* Rewrite these paragraphs to focus on the simple, single-price per class model with no lock-in contracts.

### `contact.html`
- **FAQ Section:**
  - Line 1555 & 1689: *"Drop-in rates are available for all programs — no commitment required. It's the best way to find the right class for you before committing to a pack or membership."*
  - *Action:* Rewrite to remove mentions of packs and memberships.

---

## 4. Program Page Changes

Every active adult program page (`programs/*.html`) has three areas that need updating:

### A. Quick Info Bar (Hero Section)
- Currently says: **$25** / **per drop-in class**
- *Action:* Update to the correct price and change label to **per class**.

### B. Pricing Section (The 3-Tier Cards)
- Currently displays a 3-column grid: Drop-In, 10-Class Pack, Unlimited Monthly.
- *Action:* Completely remove the 3-column grid. Replace it with a single, simple pricing block or card that states the exact price per class.

### C. SEO / Footer Text
- Currently says: *"We offer flexible booking options including drop-in classes ($25 per session), 10-class packs ($200), and unlimited monthly memberships ($180 per month)."*
- *Action:* Rewrite to state the single class price and remove pack/membership mentions.

**Affected Pages:**
- `booty-burn-foundations.html`
- `movement-flow-foundations.html`
- `fusion-yoga-foundations.html`
- `aerial-silks-foundations.html`
- `choreography-fusion-foundations.html`
- `stretch-mobility-foundations.html`

*(Note: Coming Soon pages like Pole Fitness and Recovery Movement Flow also have these pricing sections which should be updated or hidden until they launch).*

---

## 5. Kids Program Pages

While the request focused on adult classes, it's worth noting that the 7 kids program pages also mention "drop-in classes" and "8-week term available for $150". 

*Action Required:* Please confirm if Kids pricing is also changing to a single price per class, or if they are keeping the term packages.

---

## Next Steps

If you approve this report, I can write a script to automatically apply all these changes across the entire site — flattening the config, updating the HTML templates, and rewriting the text mentions.
