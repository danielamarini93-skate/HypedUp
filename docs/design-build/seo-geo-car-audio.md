# Car audio: search research and GEO (21 Nov 2026)

Source: AnswerThePublic export from Dani, "car audio", UK, 21 Nov 2026 (`docs/data/answerthepublic/car-audio-2026-11-21.csv`, 761 rows, 343 real terms). Method: Dani's seo-geo skill (Google's position: optimising for AI search is still SEO: clear answers, structure, real facts, authority).

## What people search (data)

| Need | Terms (monthly UK searches) | What the page does |
|---|---|---|
| The job, not the parts | car audio shop 880 · fitting 590 · fitters 590 · upgrade 590 · system 590 | Title, H1 lead and meta lead with "car audio fitting"; ladder titled "How to upgrade your car audio" |
| Screens and cameras | car audio for android 590 · with reverse camera 90 · 2din 170 · usb bluetooth adapter 480 | FAQ "CarPlay and a reverse camera at the same time?" + CarPlay stays in Related |
| Questions | how to upgrade 30 · how to make it sound better 10 · what is DSP 10 · what is a crossover 110 · active vs passive 10 · capacitors worth it / drain battery 10+10 · without subwoofer 10 · without head unit 10 | New FAQs + "The jargon, explained" (DSP, crossover, active/passive, capacitor) |
| Local | car audio bromley 260 · in london 170 · near me open now 20 | London + Bermondsey in title/lead; areas line waits for Hypa |
| Repair | car audio repair 590 · repairs 590 · not working 260 | **Not on the page:** we don't know if Hypa does audio repairs (on the review board) |
| Brands | kenwood car audio 320 · pioneer in car audio 390 | Kenwood and Pioneer already on CarPlay; Rockford Fosgate on audio |

Not used: other shops' names in the data (never name competing installers), "will audi buy my car" (noise).

## GEO changes made (observed → change)

1. **Answer first:** the lead now defines the service in the first sentence ("Car audio fitting means…").
2. **Definitions in "X is…" form:** 4 jargon entries, each self-contained, so AI answers can quote one cleanly.
3. **Question FAQs in the customer's words**, each answer standalone with one real detail (fused power cable, factory signal amp, prices).
4. **Prices on the ladder** from the price list (£125 speakers, £145 a door deadening, £225 amp and sub): specific, quotable facts.
5. **Author + date line** above the FAQ: "Answers from Hypa, modding cars since the early 2000s · Updated November 2026" (authority and freshness).

## For the build (recommendations)

- **Schema:** `Service` (provider = the `AutoRepair`/`LocalBusiness` already planned, areaServed London, offers with "from" prices) + `FAQPage` for the questions (rich results are limited for commercial sites, but the markup still helps machines read Q&A) + `BreadcrumbList`. Person schema for Hypa on About, linked from the byline.
- **Server-rendered HTML** (the Cloudflare static build already does this), so AI crawlers that don't run JavaScript see every answer. FAQ answers must be in the HTML, not loaded by script.
- **robots.txt:** allow Googlebot, OAI-SearchBot, Claude-SearchBot and PerplexityBot (search citability). Training bots (GPTBot, ClaudeBot, Google-Extended, CCBot) are a licensing choice for Hypa, separate from visibility.
- **Refresh:** update the byline date when FAQs change; AI answers favour recent pages.
- **Off-site:** brand mentions (YouTube, Reddit, Instagram/TikTok) count more for AI visibility than links: the reels already made could go to YouTube Shorts with "car audio fitting London" titles.

## Next topics (when exports arrive)

Same method for window tint, car wrap, Ghost immobiliser, car tracker, PPF/ceramic.
