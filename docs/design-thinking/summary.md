# Design thinking: summary

_Date: 2026-11-08 · Hyped Up website redesign · Stage 1 of 3_

## The problem
Hyped Up does creative, high-skill work on cars and bikes, but its website is a heavy GoDaddy
template that looks like every other installer, makes claims it can't back up, hides its
priority services (electronics) inside two broad pages, and gets almost no non-brand search
traffic. It also can't be run from Claude or measured properly.

## Key insights
1. **Nobody in this space has a personality.** Security and electronics competitors look like locksmiths or parts shops; wrap shops show empty cinematic heroes. A workshop with a face, colour and graffiti energy is an open position. *(competitors.md)*
2. **Electronics is where the demand is.** Car tracker and Ghost (14,800/mo each), front and rear dash cam (4,800/mo). Today these have no dedicated pages. *(audit.md, seo.md)*
3. **Proof beats claims.** Real builds, Google reviews and Hypa himself are stronger and safer than "insurance approved" and "up to 30% off". *(audit.md)*
4. **The phone experience is the experience.** The current homepage is ~12.9 MB on mobile, and the cookie banner covers the first screen. Customers enquire on WhatsApp from their phone. *(audit.md)*
5. **Three different visitors need two doors.** The worried owner and the tech upgrader (electronics) need calm clarity; the enthusiast (styling) needs inspiration and culture. *(personas.md)*
6. **"Clean structure, wild surface" works with cars.** Mobbin examples (Freshman) show hand-drawn marks over strong type and car imagery without losing clarity. *(mobbin.md)*

## Direction and why
- **Positioning:** "We adapt the car to you." One workshop for electronics and styling, cars and bikes, in Bermondsey.
- **Structure:** electronics first, styling second, as two clear doors; a page per key service; car-specific pages later (CarPlay for BMW/Mini/Mercedes, Ghost for Range Rover).
- **Look:** "Workshop wall": a strict grid and big condensed type, covered in hand-drawn marks, stickers and tape labels, on workshop black with Hyped red (#E30513) for actions. Calmer on security content. *(visual-direction.md)*
- **Action:** one primary action everywhere, "Get a quote on WhatsApp", with service and car pre-filled; call and email as backups; every tap tracked.
- **Tech:** a code site in GitHub that Claude runs (early read, to confirm), native schema, fast pages, analytics + dashboard you own. *(strategy.md)*

## What the concept shows
A mobile-first homepage, low-to-mid fidelity, using real Hyped Up photos from the current site:
1. Hero with the positioning line, a hand-drawn circle and arrow to the WhatsApp quote button
2. Two doors: Electronics and Styling
3. Electronics services with "from" prices (from `memory/pricing.md`), then styling services
4. Work rail with tape-label captions
5. Google reviews row (placeholders: real reviews TBC, never invented)
6. Meet Hypa
7. Moving tagline strip, merch (request on WhatsApp), visit block on red
8. Sticky WhatsApp + Call bar on mobile

**Not in the concept:** final type, colour and components (that's the design system in `/design-build`),
Dani's new photos and videos, real reviews, confirmed hours and the final price list.

## Open items before /design-build
- Price list confirmed by Hypa (live site vs memory clash)
- Content-rule decisions (20+ years, Thatcham/insurance wording, tinted lights, shadow plates)
- Email data meaning and dashboard numbers (strategy TBCs)
- Photo and video handover from Dani
- Permission to show Google reviews

## Concept v0.2 (8 Nov 2026, after Dani's feedback)
- Hero: workshop video, "Your car. Any way you want it.", one line, one action ("Start your build"). Nothing else above the fold.
- Positioning: one-stop modification and styling shop; electronics and styling are two starting points, plus "Anything else".
- Palette: graphite scale + Hyped red (styling) + signal blue (electronics); chalk white for "anything else".
- Prices: generic "from £" only (master sheet still to reconcile).
- v0.1 kept as `concept/index-v0.1.html`.
