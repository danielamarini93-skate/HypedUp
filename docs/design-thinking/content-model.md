# Content model: what every page type contains, in what order

_9 Nov 2026 · The rule book for writing pages. Every page: Hypa's voice (first person, direct, UK English), each fact once per
screen, "from £" only, one primary action (**Contact us**), dark only. Meta title ≤ 65 characters, description 155–160._

## 1. Service page (the most important template: 21 pages)
**Job:** answer "can you do this for my car, how much, can I trust you?" for someone who landed from Google, Maps, ChatGPT or a partner.

| # | Block | Content | Rules / source |
|---|---|---|---|
| 1 | Breadcrumb | Home › Group › Service | |
| 2 | **Hero** | H1 = the service in search words (e.g. "Ghost immobiliser") · 1–2 line answer · **from £** + what's included in that price · **Contact us** (`?service=`) · one real photo | H1 matches keyword-map primary; price from `price-list-master.md` |
| 3 | **What you get / options** | 2–4 options (e.g. S7 vs S5; 1/2/3-channel; Stage 1/2/3; full/partial wrap) with one line each | from the price sheet and Hypa's blog |
| 4 | **How it works** | 3 steps, plain words | |
| 5 | **Proof** | 3–6 builds for this service + 1 Google review mentioning it + partner logo(s) | builds filtered by service |
| 6 | **Price detail** | "from £" per option · what changes the price · subscriptions if any · how long it takes | never exact quotes; wraps min 1 week |
| 7 | **Good to know** (legal) | only where needed: tint law, remaps and MOT/insurance, plates for road use, TfL rules | calm, 2–3 lines, Hypa approves wording |
| 8 | **FAQ** | 4–6 real questions | from `seo.md` question lists + Search Console; becomes FAQ schema |
| 9 | **Your car** | links to car-specific pages (if any) | tier 3 links |
| 10 | **Related** | 2–3 related services + 1–2 blog guides | |
| 11 | **Contact band** | one line + Contact us | |
**Schema:** Service + Offer (from price) + FAQPage + BreadcrumbList. **Photos needed:** 1 hero + 3–6 builds.

## 2. Group hub (Security, Upgrades, Styling: 3 pages)
**Job:** browse a group, compare, and rank for the broad term ("car security London"). Not in the menu.

| # | Block | Content |
|---|---|---|
| 1 | Hero | H1 = group name in search words ("Car security in South London") · 2 lines on what the group covers · Contact us |
| 2 | **All services in this group** | **every service in the footer column, in the same order** (Dani, 9 Nov): photo, name, one line, from £ |
| 3 | Which one do I need? | short comparison table (what it does · best for · from £) |
| 4 | Explainer | one topic people search for (e.g. Security: "S5 or S7?"; Upgrades: "Will CarPlay work in my car?"; Styling: "Wrap, PPF or ceramic?") |
| 5 | Proof | 3 builds + 1 review |
| 6 | FAQ | 4–6 group-level questions |
| 7 | Contact band | |
**Rule:** the hub's service list and the footer column come from one data list, so they can never differ.

## 3. Car-specific page (tier 3: e.g. CarPlay for BMW)
| # | Block | Content |
|---|---|---|
| 1 | Hero | H1 "CarPlay for BMW" · which models/years · from £ · Contact us |
| 2 | What fits | options for this make (screen vs interface, keeps steering controls…) |
| 3 | Proof | only real jobs on this make (minimum 2) |
| 4 | FAQ | make-specific questions |
| 5 | Links | back to the service page + 2 sibling makes |
**Publish only when there are 2+ real jobs with photos.**

## 4. Home
| # | Block | Content |
|---|---|---|
| 1 | Hero | "Protect it. Upgrade it. Style it." + one line + Contact us + Find us · workshop video |
| 2 | Three groups | Security · Upgrades · Styling, each with its top services and "from £" |
| 3 | Recent builds | 3–6, link to Builds |
| 4 | How a job works | 3 steps |
| 5 | Proof | Google rating + 1–2 reviews · Hypa and the workshop · partner logos |
| 6 | Visit | status, map link, hours |
| 7 | Contact band | |

## 5. Audience hub (Motorbikes, Business & fleet)
Hero (who it's for) → services that apply, linking to the service pages (no duplicate content) → proof → FAQ → contact.

## 6. Builds
Hero (one line) → featured build → filter (All · Security · Upgrades · Styling) → grid (car, work done, link to service) → contact.
**Build page (later):** car + work done + 4+ photos + service links + "want this?" contact. **Captions need Hypa's facts.**

## 7. Contact
Form v2 (`contact-flow.md`) → Find us (address, real map, Get directions) → hours → phone/WhatsApp/email → "Areas we cover" line (towns, for local SEO; no area pages).

## 8. Prices
**No Prices page** (Dani, 14 Nov): "from £" lives on each service page, the hubs and the homepage strip.

## 9. About
Hypa's story (how he started, his own cars, the Unit 22 mural) → how we work (fitted properly, priced clearly) → dealer/partner status → reviews → visit.
**Every claim confirmed by Hypa** (20+ years, McLaren, dealer wording).

## 10. Blog list + post
List: categories (Security · Upgrades · Styling · Law & guides) + newest first.
Post: question-led title · answer in the first 2 lines · body · "from £" box linking the service · FAQ · author (Hypa) · related posts.

## 11. Shop, legal
Shop: products, price, "Order on WhatsApp". Legal: plain text pages.

## Global rules
- One H1 per page; H1 ≠ meta title word-for-word.
- Every page has: breadcrumb (inner), one primary action, footer index.
- Every image: renamed, alt text, compressed, privacy-checked (`memory/media-guidelines.md`).
- No page goes live with placeholder copy or unconfirmed facts.
