# Website Redesign & Leaving GoDaddy

_Last updated: 7 Nov 2026 · Status: **planning — nothing decided yet**_

## Goal
Redesign hypedup.uk and move it off GoDaddy Website Builder onto a setup Hyped Up controls,
without losing the SEO work already done.

## Why leave GoDaddy (from what we know)
- No native schema support — had to hack it in via GTM
- Limited control over page structure, URLs, speed and per-page SEO
- Simple jobs (fixing icons, adding prices) are awkward in the builder

## Must carry over — migration checklist
- [ ] **Inventory every current URL** (homepage, ~10 pages in sitemap, all 14 blog posts) before anything changes
- [ ] **301 redirects** from every old URL to its new URL (old sitemap: `/sitemap.website.xml`)
- [ ] Export all blog post text + images from GoDaddy (14 published posts)
- [ ] **Domain / DNS:** find out where hypedup.uk is registered and where DNS is hosted (probably GoDaddy)
- [ ] **Email (info@hypedup.uk):** check MX records / who hosts the mailbox — must not break when DNS changes
- [ ] **Search Console:** re-add the HTML verification tag on the new site, or switch to DNS verification first
- [ ] **GA4 `G-PZPFNLV5SW`** on every page (still not live on GoDaddy — publish never clicked)
- [ ] **GTM** container on every page (or move schema into the HTML and retire the GTM workaround)
- [ ] **Schema:** move LocalBusiness/AutomotiveBusiness JSON-LD into page HTML natively; add FAQ schema per service page/blog post; real logo URL
- [ ] New sitemap.xml + robots.txt; submit the new sitemap in Search Console
- [ ] Keep NAP identical to Google Business Profile
- [ ] Mobile speed check (Core Web Vitals) before and after

## Fixes from the current homepage (bake into the redesign)
- "Experties" → "Expertise" in the trust bar
- Broken icons in "Why Choose Us"
- Starting prices on every service block (from `pricing.md`)
- Add Number Plates as a homepage service

## Proposed site structure (draft — to agree with Hypa)
- Home
- Services hub + one page per service (security, trackers, Ghost, dash cams, CarPlay/multimedia, audio,
  wrapping, PPF/ceramic, tinting, chrome delete, ECU remap, air suspension, number plates, bodykits/wheels/calipers)
- Blog (all posts, categorised by the two pillars)
- About (Hypa's story, McLaren roots, the Mini and 1 Series builds)
- Gallery / builds (Instagram-fed or curated)
- Contact (map, WhatsApp button, phone, form)
- Prices page (optional — all "from" prices in one place)

## Open questions for Hypa
1. Where is the domain registered and who manages DNS?
2. Is info@hypedup.uk on GoDaddy email, Microsoft 365, Google Workspace or something else?
3. Who will edit the site day to day — does Hypa need an easy editor for blog posts, or will Claude publish them via this repo?
4. Any must-have features: online booking, quote form, WhatsApp chat, price calculator, gallery?
5. Brand assets: logo files, colours, fonts, photos — where are they?
6. Budget for hosting (free/static hosting vs. a paid CMS)?

## Platform options (to decide — no choice made yet)
- **Static site in this repo** (e.g. Astro) on Netlify / Cloudflare Pages / Vercel — fast, free hosting, full SEO control; blog posts as Markdown, Claude can write + publish via git
- **WordPress** (managed host) — familiar editor, plugins; more maintenance
- **Webflow / Framer** — visual editor, paid monthly
