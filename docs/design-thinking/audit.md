# Preliminary audit: hypedup.uk (live GoDaddy site)

_Date: 2026-11-08 · Pages checked: homepage (mobile), Vehicle Security (desktop), plus the
7 Nov site-wide review in `memory/current-site.md` · Labels: **observed** (seen on the page),
**data** (measured or from analytics), **recommendation**._

**How this was done.** UX heuristic review by Claude from screenshots and page structure. The
accessibility and SEO checks ran on the live pages with a custom script in the installed browser.
The `accessibility-scan` skill (AccessLint) couldn't run: this session's safety check blocked
downloading its tool. So contrast, names, labels, headings, target size and alt text are covered,
but this **isn't a full WCAG 2.2 conformance scan**. Re-run `accessibility-scan` on Dani's computer
or allow it here. Raw results: `audit/results.json`. Screenshots: `audit/`.

## Top issues, ranked by impact

### 1. The phone homepage is very heavy and slow
- **Data:** the homepage on mobile loaded **~12.9 MB** in **59 requests**, and took **~13.8 s** to the load event (cloud test, one run; indicative, not a lab score). The Security page was ~1.4 MB.
- **Observed:** large background video/images in the hero; sections are rendered several times in the HTML (builder duplication).
- **Recommendation:** image and video budget per page, modern formats, lazy-load below the fold, no duplicated markup. *Serves: more enquiries (mobile users bounce), ranking (Core Web Vitals).*

### 2. Above the fold says "security specialists" and little else
- **Observed:** on a phone, the first screen is the headline, a generic subtitle and two red pill buttons. The cookie banner covers the bottom third until dismissed. No price, no proof (reviews, real work), no clue to the creative/styling side.
- **Recommendation:** first screen = who + what (electronics and styling) + proof (a real build or rating) + one primary action (WhatsApp quote). Smaller, lighter consent notice. *Serves: trust, enquiries, positioning.*

### 3. Claims that can't be backed up, and conflicting prices
- **Observed:** "Thatcham Approved", "Insurance-approved", "Reduce premiums up to 30%", "20+ Years Expertise" (in the H1 area and meta description); unsourced stats on Security ("26,117 cars stolen in 2022", "95% returned… 86% within 24 hours").
- **Data:** homepage prices clash with the price list (CarPlay £195 vs £600; remap £435 vs £250–400; plates £35 vs £30).
- **Recommendation:** one confirmed price list; sourced stats only; claims Hypa signs off. *Serves: trust, legal safety.*

### 4. Broken page structure (headings) hurts screen readers and SEO
- **Data:** the trust bar "✓ Thatcham Approved ✓ 20+ Years…" is an **H3 repeated 6 times**; "Why choose" has **6 empty H4s**; service titles are H4s with no H2/H3 above them; Security has 6 empty H4s.
- **Recommendation:** one H1, then H2 per section, H3 per item; no headings used for decoration. *Serves: accessibility (WCAG 1.3.1), ranking, AI understanding.*

### 5. Controls without names, small tap targets, low-contrast contact text
- **Data:** 9 buttons/links with **no accessible name** on each page checked (likely icon-only and carousel controls); 6–7 targets **under 24×24 px** (WCAG 2.5.8); contact details in the footer at **3.9:1 contrast** (needs 4.5:1).
- **Observed:** body text in letter-spaced light type on photos; legibility depends on the image behind it.
- **Recommendation:** label every icon button; 44 px tap targets on mobile; contrast tokens checked in the design system. *Serves: accessibility baseline (WCAG 2.2 AA).*

### 6. Electronics, the priority, has no pages of its own
- **Observed:** Ghost, trackers, dash cams, CarPlay, audio are paragraphs inside two broad pages ("Vehicle security", "Multimedia upgrade"). Wraps, PPF and tint share one page; plates and detailing have none.
- **Data:** searches are specific: car tracker 14,800/mo, Ghost immobiliser 14,800/mo, front and rear dash cam 4,800/mo, car wrap cost 4,700/mo. Search Console: almost all clicks are brand searches ("hyped up limited" 10, "hyped up" 4); non-brand ~1 click each.
- **Recommendation:** a page per high-demand service, each with price, FAQ, real work and schema. *Serves: ranking, AI citations, electronics growth.*

### 7. The brand doesn't feel like the workshop
- **Observed:** standard GoDaddy layout: centred stacks, pill buttons, slab-serif headings, generic icons (shield, map pin). None of the graffiti, colour, craft or car/bike culture visible in the workshop photos and Instagram.
- **Recommendation:** visual direction built from the workshop itself (see `visual-direction.md`). *Serves: brand, enthusiast audience.*

### 8. Technical SEO gaps
- **Observed / data (from 7 Nov review):** blog posts not in the sitemap; the homepage exists at two URLs (`/` and `/hyped-up`); weak titles on the audio and wrapping pages; meta descriptions repeat the unsupported claims; schema is injected through Google Tag Manager instead of the page.
- **Observed (positive):** `lang="en-GB"`, viewport set, canonical tags present, AutomotiveBusiness schema present, all visible images have alt attributes, WhatsApp links pre-fill a message.
- **Recommendation:** native schema per page (LocalBusiness, Service, FAQ, Article), every page in the sitemap, one URL per page, 301 plan (already listed in `memory/current-site.md`). *Serves: ranking, AI citations.*

### 9. Quote journey works, but it's generic
- **Data:** WhatsApp links pre-fill "I'm interested in a quote for" with no service or car; the phone link is `tel:020 3340 0632` (works, but international format is safer).
- **Recommendation:** pre-fill service + page + car, track every click as an enquiry event. *Serves: enquiries, data.*

## What to keep
- WhatsApp as the main channel, with pre-filled messages
- Real workshop photos (Porsche, Mini, Abarth…) and the workshop mural
- The blog voice: honest, local, practical
- Service naming customers recognise (CarPlay, Ghost, dash cam, wraps)

## Next steps (ranked)
1. Confirm the price list and claims with Hypa (blocks content)
2. Page-per-service information architecture, electronics first
3. Performance and accessibility budgets in the design system
4. Native schema + sitemap + redirects in the build
5. Full `accessibility-scan` / `seo-audit` once tools can run (Dani's computer)
