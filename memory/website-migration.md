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
- [x] **Inventory every current URL** → `current-site.md` (11 pages + 15 posts)
- [ ] **301 redirects** from every old URL to its new URL (old sitemap: `/sitemap.website.xml`)
- [x] Export blog post text → `content/blog-archive/` (images still hosted on GoDaddy's `img1.wsimg.com` — download before cancelling)
- [ ] Apparel shop (4 products): keep, move to a shop platform, or drop?
- [ ] **Domain / DNS:** hypedup.uk is registered **and** DNS-hosted at GoDaddy (confirmed 7 Nov 2026). Plan: keep the domain at GoDaddy for now and only change the website records (A/CNAME); a registrar transfer can come later, separately
- [ ] **Email (info@hypedup.uk):** hosted on **GoDaddy** (confirmed 7 Nov 2026). Before touching DNS, export a copy of every DNS record and **do not change MX, SPF/TXT, DKIM or autodiscover records**. Check whether it's GoDaddy's own email or Microsoft 365 via GoDaddy — if the GoDaddy website plan is cancelled, make sure the email plan is separate and stays active
- [ ] **Search Console:** re-add the HTML verification tag on the new site, or switch to DNS verification first
- [ ] **GA4 `G-PZPFNLV5SW`** on every page (still not live on GoDaddy — publish never clicked)
- [ ] **GTM** container on every page (or move schema into the HTML and retire the GTM workaround)
- [ ] **Schema:** move LocalBusiness/AutomotiveBusiness JSON-LD into page HTML natively; add FAQ schema per service page/blog post; real logo URL
- [ ] New sitemap.xml + robots.txt; submit the new sitemap in Search Console
- [ ] Keep NAP identical to Google Business Profile
- [ ] Mobile speed check (Core Web Vitals) before and after

## Fixes from the current homepage (bake into the redesign)
- Broken icons in "Why Choose Us" ("Experties" typo already fixed on live site)
- Starting prices on every service block — after Hypa resolves the price clashes
- Number Plates already on the homepage; give it its own page

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
1. ~~Where is the domain registered and who manages DNS?~~ → GoDaddy
2. ~~Who hosts info@hypedup.uk?~~ → **Microsoft 365 bought through GoDaddy** (MX points to Outlook; full record list in `friend-concept.md`)
3. Who will edit the site day to day — does Hypa need an easy editor for blog posts, or will Claude publish them via this repo?
4. Any must-have features: online booking, quote form, WhatsApp chat, price calculator, gallery?
5. Brand assets: logo files, colours, fonts, photos — where are they?
6. Budget for hosting (free/static hosting vs. a paid CMS)?

## Platform options (to decide — no choice made yet)
- **Friend's concept site** (Astro on Cloudflare, see `friend-concept.md`) — already ~80% of the static option below: pages, redirects, schema, photos, blog. Missing GA4/GTM and confirmed prices
- **Static site in this repo** (e.g. Astro) on Netlify / Cloudflare Pages / Vercel — fast, free hosting, full SEO control; blog posts as Markdown, Claude can write + publish via git
- **WordPress** (managed host) — familiar editor, plugins; more maintenance
- **Webflow / Framer** — visual editor, paid monthly
