# Hyped Up — Project Memory

This repo is the home for everything Hyped Up: the new website (replacing GoDaddy) and the
business/marketing memory that every Claude session should start from.

**Read this file first, then open the relevant file in `memory/` for detail.**

## Who I'm working with

**Dani** is a **UX/UI designer** who leads this project: the website redesign, the brief and the strategy.
Talk to Dani as a designer: design and UX language is fine and welcome; explain code and infrastructure in plain words.
Hyped Up is Dani's partner's company. Hypa (the owner) gives the final OK on business facts, prices and claims.

**How Dani works lives in the `dani-studio` repo** (github.com/danielamarini93-skate/dani-studio):
Dani's profile, process, design principles, working agreements, skills (`design-thinking`,
`design-build`, `design-review`, SEO, accessibility…) and templates (brief, strategy, research plan).
Add it to every session alongside this repo. If it isn't loaded, ask Dani to add it before design work.
Rule of thumb: **anything about Hyped Up goes here; anything about how Dani works goes in dani-studio.**
Use dani-studio's `templates/brief.md` and `templates/strategy.md` for this project's brief and strategy.

## Design system

TBC: to be created in **Claude Design** during `/design-build`. Link it here once it exists.

## Where outputs go

Following Dani's process: `docs/design-thinking/` (brief, strategy, research, concept),
`docs/design-build/`, `docs/design-review/`. Business memory stays in `memory/`.

## Design thinking (stage 1): done 8 Nov 2026
Outputs in `docs/design-thinking/`: tech-setup (cookies, forms, reviews, analytics), brief, strategy v0.2, audit, competitors, Mobbin, personas, visual direction, summary, concept.
- **Positioning line (decided):** "Protect it. Upgrade it. Style it." + "South London's one-stop workshop for car and bike electronics, security and styling. Fitted properly, priced clearly."
- **Platform (decided):** code site in GitHub, edited only by Claude, hosted on Cloudflare
- **Look:** "Workshop wall": strict grid + condensed type + hand-drawn marks/stickers, workshop black + Hyped red `#E30513`
- **Main action:** WhatsApp quote with service and car pre-filled
- **Research & audit doc (Dani edits here first):** https://claude.ai/artifact/1u8jZjGD9RU1c2pFWeULLg
- **Concept:** https://claude.ai/artifact/NdsiSfKjKAG2a1tVQ3VXcX · **Mobbin:** collection "Hyped Up website redesign"
- **Next:** Dani reviews → platform decision → `/design-build`

## The business in one paragraph

Hyped Up is a vehicle modification, security and styling workshop in Bermondsey, South London,
run by **Hypa** (founded 2022, 20+ years experience, McLaren motorsport roots). Services span
security (Ghost immobiliser, MetaTrak trackers, dash cams), multimedia (CarPlay, cameras),
audio, wrapping/PPF/tint, ECU remapping, air suspension, custom number plates and bodywork.

- Address: Unit 22, Enterprise Industrial Estate, Bolina Road, London SE16 3LF
- Phone: 020 3340 0632 · WhatsApp: 07713 735646 · Email: info@hypedup.uk
- Website: https://hypedup.uk/ (GoDaddy Website Builder; domain + email also on GoDaddy)
- Socials: Instagram + TikTok @hypedup.ltd · LinkedIn /company/hypedupltd

## Current goal

1. **Redesign the website and move off GoDaddy.** Brief, strategy and platform done; next: concept approval → `/design-build`. See `memory/website-migration.md`.
2. Keep the SEO/content engine running (2 blog posts/week, Google Maps ads, GBP).

## Memory map

| File | What's in it |
|---|---|
| `memory/business.md` | Services, partner brands, Hypa's background and cars |
| `memory/price-list-master.md` | **Master price list** from Dani's sheet, with website "from £" prices (wins over pricing.md) |
| `memory/pricing.md` | Older confirmed prices; plates, remaps, Ghost still from here |
| `memory/brand-voice.md` | Writing style guide + competitor-mention rules |
| `memory/seo.md` | Technical SEO done (GTM, schema, GA4, Search Console) + keyword data |
| `memory/content.md` | Blog posts: published, ready, to write; news angles |
| `memory/marketing.md` | Google Maps ads, Google Business Profile, AI visibility (GEO) |
| `memory/operations.md` | Customer tracker (Google Sheets), tools, how Hypa wants AI to help |
| `memory/current-site.md` | Audit of the live GoDaddy site: every URL, tracking IDs, price clashes |
| `memory/friend-concept.md` | Review of a friend's Astro/Cloudflare concept site (not adopted yet) + rule clashes |
| `memory/website-migration.md` | Redesign + leaving GoDaddy: what must carry over, open questions |
| `docs/data/baseline-search.md` | Search Console "before" numbers (Aug–Nov 2026) and targets |
| `docs/data/baseline-analytics.md` | GA4 "before" numbers: visitors, sources (incl. ChatGPT, Autostyle), pages, form drop-off |
| `docs/tech-checklist.md` | Every technical step to launch, with proposed timing (now / design / build / launch) |
| `memory/todo.md` | Every pending item, grouped |
| `memory/decisions.md` | Log of decisions made (append new ones with a date) |
| `memory/source/` | The original memory export, kept verbatim for reference |
| `content/blog-archive/` | Full text of all 15 live blog posts, exported 7 Nov 2026 |

## Hard rules (always apply)

- **Prices:** only use prices in `memory/price-list-master.md` (then `memory/pricing.md`). On the website show generic "from £" only. Write them with £. If a price isn't there, say "price on enquiry" or ask.
- **No dyno testing** — Hyped Up does not offer it. Never mention it.
- **Full wraps take a minimum of 1 week** (never "3–5 days").
- **Never name competing installation shops.** Product brands are fine (Ghost, Pandora, Scorpion, MetaTrak, Xtrons, Autostyle, Pioneer, Kenwood, Rockford Fosgate, Air Lift, Prazis).
- Write in **Hypa's voice** (see `memory/brand-voice.md`): first person, direct, honest, South London, no corporate fluff.
- Meta titles ≤ 65 characters; meta descriptions 155–160 characters.
- UK English (colour, tyre, licence, organise).
- Hypa wants AI as a **personal assistant** (organise, remind, draft) — not full automation.

## Keeping memory up to date

When something changes (a post is published, a price changes, a decision is made, a task is done):
update the relevant `memory/*.md` file, tick/remove it in `memory/todo.md`, add a dated line to
`memory/decisions.md` if it was a decision, and bump the "Last updated" date in that file.
