# Decisions Log

Append new decisions at the bottom: `- YYYY-MM-DD — decision — why`.

## Carried over from earlier chats (before Nov 2026)
- Dyno testing removed from all content — not offered
- Full wraps quoted as minimum 1 week (not 3–5 days)
- Schema injected via GTM because GoDaddy has no native schema support
- Search Console verified with the HTML tag method
- Advertising: Google Maps ads first (£5/day, 5-mile radius); Search ads only after 2–3 months of results
- Content pillars: (1) Electronics & Security (priority), (2) Styling & Personalisation
- 2 blog posts per week, Monday and Thursday, Oct 2026 – Jan 2027
- Never name competing shops; product brands are fine
- AI used as a personal assistant, not full automation

## This project
- 2026-11-07 — Started this repo as the single home for Hyped Up memory + the new website — moving off GoDaddy
- 2026-11-07 — Domain and email confirmed as both on GoDaddy — website move must leave email DNS records untouched
- 2026-11-07 — Audited the live site and saved all 15 blog posts into the repo so nothing depends on GoDaddy for content
- 2026-11-07 — Reviewed a friend's Astro/Cloudflare concept site; kept out of the repo until Daniela decides whether to use it
- 2026-11-07 — Friend's concept site will NOT be used or copied into the repo; new site to be built from scratch with a different approach (platform still to choose)
- 2026-11-07 — Process: brief + strategy first, platform choice after (Dani)
- 2026-11-08 — Dani's way of working lives in the dani-studio repo; this repo holds only Hyped Up facts. Sessions should load both
- 2026-11-08 — Apparel shop kept, ordered via WhatsApp request instead of PayPal/checkout (Dani)
- 2026-11-08 — Positioning: electronics and electronic mods first, styling second (Dani)
- 2026-11-08 — Design thinking stage completed; homepage concept 'workshop wall' proposed (awaiting Dani's review)
- 2026-11-08 — Research and audit moved into an editable doc for Dani to review before the concept (https://claude.ai/artifact/1u8jZjGD9RU1c2pFWeULLg)
- 2026-11-08 — Concept v0.2 direction (Dani): minimal craft hero with video and one CTA; bolder palette (graphite + red + signal blue); positioning = one-stop modification shop, electronics and styling are starting points
- 2026-11-08 — Website shows generic 'from £' prices only; the master price sheet is the source (Dani)
- 2026-11-08 — Personas confirmed as right (Kemi, Jay, Marco) (Dani)
- 2026-11-08 — Opening hours confirmed; OK to show Google reviews on the site, ideally automated (Dani)
- 2026-11-08 — "We adapt the car to you" rejected as not professional enough; positioning must answer what clients want (Dani)
- 2026-11-08 — Content editing: Claude via GitHub only, no CMS (Dani)
- 2026-11-08 — Skip downloading old GoDaddy images; Dani puts newer media in Google Drive (Dani)
- 2026-11-08 — Positioning line = option A: "Protect it. Upgrade it. Style it." + "South London's one-stop workshop for car and bike electronics, security and styling. Fitted properly, priced clearly." (Dani)
- 2026-11-08 — Hosting = Cloudflare (code site in GitHub, edited by Claude only). Framework chosen at build time (Dani)
- 2026-11-08 — Media rules agreed: descriptive file names, alt text, compression, ImageObject/VideoObject schema, location in text + schema (not photo GPS), blur customer plates/faces without consent
- 2026-11-08 — Media privacy: always blur customer number plates; no customer faces on the site (Dani)
