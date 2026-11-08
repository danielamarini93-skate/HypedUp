# Hyped Up: UX strategy

_Version: 0.2 · Date: 2026-11-08 · Based on: brief v0.1 + research (audit, competitors, Mobbin, personas)_

## The problem
Hyped Up does creative, high-skill work, but its website is a generic template. It doesn't
show the workshop's personality, doesn't rank for the services people search for, and can't
be updated or measured the way the business needs.

## Positioning
- **For:** drivers and riders in South and South East London
- **Who need:** their car or bike protected, upgraded or made to look like theirs, by someone they can trust with it
- **We offer:** one workshop for electronics (security, trackers, dash cams, CarPlay screens, custom audio) and styling (wraps, carbon interiors, air, plates), built around what *you* want: "we adapt the car to you"
- **Unlike:** single-service fitters and faceless chains that sell a box and leave
- **Proof:** real builds (photos and video), Google reviews, Hypa's motorsport background, partner brands (Ghost, MetaTrak, Air Lift, Prazis, Xtrons…), honest prices up front

## Positioning line: options (v0.3, after Dani's feedback)
Dani: "We adapt the car to you" isn't professional enough; the line must **answer what clients want**.
Clients want: their car **protected**, **upgraded** and **styled**, **done properly**, by someone they can **trust**, with a **clear price**, in **one place**.

| Option | Headline | Supporting line |
|---|---|---|
| **A (recommended)** | **Protect it. Upgrade it. Style it.** | South London's one-stop workshop for car and bike electronics, security and styling. Fitted properly, priced clearly. |
| B | Every upgrade your car needs. One workshop. | Security, CarPlay, audio, wraps, tint, air and more, in Bermondsey. |
| C | Car electronics and styling, done properly. | From Ghost immobilisers to full wraps: one team, one place, one clear price. |
| D | Your next upgrade starts here. | South London's one-stop modification workshop, for cars and bikes. |

Why A: three verbs = the three things people come for (security, tech, looks), in the order of priority; the
supporting line carries the professional claim (one-stop, fitted properly, priced clearly) and the search terms
(South London, car electronics, security, styling). **Decided 8 Nov 2026: option A (Dani).**

## Strategic priorities
1. **Make electronics the front door.** Serves: grow electronics work. Why: highest search demand (car tracker 14,800/mo, Ghost 14,800/mo, front and rear dash cam 4,800/mo) and Hyped Up's priority.
2. **Show the work, show the person.** Serves: trust + brand. Why: this kind of work is bought on proof. Photos, video, reviews and Hypa himself beat any claim.
3. **One fast way to ask.** Serves: more enquiries. Why: customers already use WhatsApp; a pre-written message with service and car removes friction on mobile.
4. **Built to be found by Google and AI.** Serves: rank + AI citations. Why: today almost all search traffic is brand searches; each service needs its own answer-shaped page.
5. **Run from Claude, measured by default.** Serves: run from Claude, own the data. Why: Dani and Hypa have limited time; updates and reports must be a chat message, and decisions must come from data.

## What we won't do (for now)
- Online checkout or payments, because WhatsApp requests are enough for merch and quotes, with no payment admin
- Online booking calendar, because jobs need a chat first (car, spec, parts)
- Customer accounts, because there's no need yet
- Heavy animation or video autoplay everywhere, because phone speed and accessibility come first
- Claims we can't prove ("insurance approved", "up to 30% off"), because trust is the product

## Experience principles
1. **Feels like the workshop.** Graffiti, craft, grease and colour, but the information stays clean and legible.
2. **Proof before promise.** Every service shows real work and a real price ("from £…").
3. **One tap to talk.** WhatsApp is always one tap away; never a dead end.
4. **Straight answers.** Plain words, real prices, honest pros and cons: Hypa's voice.
5. **Mobile first, fast always.** Built at phone width, works on a slow connection.

## Riskiest assumptions & how we'll test them
| Assumption | Risk if wrong | Test |
|------------|---------------|------|
| Customers prefer WhatsApp to forms | Lost enquiries from people who won't use WhatsApp | Track WhatsApp vs call vs email clicks; add a simple form if others matter |
| A graffiti/art look builds trust for security work | Looks less serious to the "worried owner" | Show the concept to 3–5 customers; check security pages feel calm and credible |
| Electronics-first lifts enquiries | Styling customers feel second | Track enquiries by service before/after |
| Showing "from" prices helps | Price shoppers bounce | Compare engagement on priced vs unpriced services |
| AI assistants will cite a small local site | Effort without visibility | Monthly AI visibility check after launch |

---

## Technical strategy
_How the technology serves the goals above. Proposals; platform decision after Dani approves this strategy._

### Requirements (from the intake)
| # | Requirement | Why |
|---|-------------|-----|
| R1 | **Creative freedom**: any layout, texture, motion, no template limits | Brand that feels like Hyped Up |
| R2 | **Run from Claude**: edit pages, prices, publish posts, deploy, from chat | Limited time, no browser needed |
| R3 | **SEO and AI-ready**: clean HTML, structured data, fast, sitemap, redirects, llms.txt | Rank + AI citations |
| R4 | **Own the data**: analytics, Search Console, enquiry clicks, email data | Decisions from data |
| R5 | **Easy dashboard**: a few clear numbers, readable by Dani and Hypa, and by Claude | Know what's working |
| R6 | **Low cost and low maintenance** | Side project budget |
| R7 | **Safe migration**: domain at GoDaddy, Microsoft 365 email untouched, 301s for every old URL | No lost email or rankings |

### Data and analytics (proposal)
- **Enquiry tracking:** every WhatsApp, call and email button sends an event (which service, which page). This is the core metric.
- **GA4** (keep `G-PZPFNLV5SW` for continuity) + **Search Console** (keep verification via DNS). Claude can read both through their APIs (`seo-google` skill) and report in chat.
- Optional privacy-friendly second source (e.g. Cloudflare Web Analytics, free) if we want numbers without cookie banners.
- **Email data** (TBC what Dani means):
  - (a) *Enquiries to info@hypedup.uk*: count and tag them via Microsoft 365 (Microsoft Graph) or by routing a contact form through a form service that logs entries.
  - (b) *Email marketing*: only if a newsletter is wanted; a tool with an API (e.g. Brevo, MailerLite) so Claude can read stats.
- **Google Business Profile:** reviews, calls, direction requests (already a big source; see memory). Include in the dashboard.

### Dashboard (proposal, TBC with Dani)
- **Audience:** Dani weekly, Hypa monthly (TBC)
- **5 numbers:** enquiries by channel and service · visitors and top pages · non-brand Google clicks and top queries · Google Business Profile calls/directions/reviews · speed and errors
- **Options:** (1) **Looker Studio** (free, connects GA4 + Search Console, shareable link); (2) a **private dashboard artifact** Claude refreshes from the APIs; (3) both: Looker for always-on, Claude for a monthly written summary with recommendations.

### Platform shortlist (to score after strategy approval)
| Option | R1 Creative | R2 Run from Claude | R3 SEO/AI | R6 Cost | Notes |
|---|---|---|---|---|---|
| **Code site in GitHub** (e.g. Next.js), free hosting (Vercel or Cloudflare) | ●●● | ●●● | ●●● | ●●● | Everything is files Claude edits; can grow (booking, dashboard page); no visual editor |
| **Code site + headless CMS** (e.g. Sanity, Payload) | ●●● | ●●○ | ●●● | ●●○ | Adds a login to edit posts without Claude; more moving parts |
| **Webflow** | ●●○ | ●●○ | ●●○ | ●○○ | Visual editor, API/MCP for Claude; monthly fee; some limits |
| **WordPress** (managed) | ●●○ | ●●○ | ●●○ | ●●○ | Huge plugin choice; updates and security upkeep; theme constraints |
| **Framer** | ●●● | ●○○ | ●●○ | ●○○ | Beautiful, fast to design; weak for running from Claude |

Early read: the **code site in GitHub** fits R1, R2, R3 and R6 best, which matches "do everything in Claude". Final call after research.

## What the research added (v0.2)
- **Personality is the gap:** no competitor in security/electronics feels human or creative (competitors.md) → priority 2 confirmed.
- **Two doors, electronics first:** three proto-personas split into Electronics (Kemi, Jay) and Styling (Marco) (personas.md).
- **Car-specific pages** ("CarPlay for BMW/Mini/Mercedes", "Ghost for Range Rover"), borrowed from a competitor pattern: high intent, low local competition → add to priority 4.
- **Performance is a priority, not polish:** live homepage ~12.9 MB on mobile (audit.md) → page weight budget in the design system.
- **Google reviews high on the page**, with permission; never invented.
- **Security pages stay calmer** inside the graffiti brand (riskiest assumption #2).

## Next steps
1. Dani reviews this strategy (and answers TBCs: email data, dashboard audience/numbers)
2. Research (audit, competitors, Mobbin, personas) → update to v0.2
3. Homepage concept
4. Platform decision → `/design-build`
