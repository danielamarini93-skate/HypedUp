# Design build plan: Hyped Up website

Stage 2 of Dani's process. Started 21 Nov 2026. **Status: approved 21 Nov; building.**

**Claude Design file:** https://claude.ai/artifact/5cJ4xZwusEATjcqwoi8boT

## Inputs

- Approved concept: site concept v5, https://claude.ai/artifact/Dy6NkZo1FRKuMtSNn7U4HF (copy source `docs/design-thinking/concept/pages/content.py`)
- Design system: **Hyped Up Brand** in Claude Design, https://claude.ai/artifact/JRh26Xr17rGo7XrjZ1virr (tokens, logos, fonts, 6 components, brand book)
- Brief, strategy, IA v2, menu and footer v4, contact flow: `docs/design-thinking/`

## Dani's answers (21 Nov)

| Question | Answer |
|---|---|
| Scope | **Every page: all 36** |
| Breakpoints | **Phone (390) first, then desktop (1440)** |
| Concept | Keep the structure and look. Copy and images change after the big Hypa review, so use the v5 copy and media as they are. |
| Security photo rule | **The MetaTrak leaflet and tag are fine** (product branding, no install location). Still never show a unit's fitting location, wiring or inside panels: the M1000RR tracker fitting video and the Ghost start-button crop get checked against this. Note the exception in the design system. |
| Done means | **Screens + developer handoff** |

## 1. Design system (Claude Design): done 21 Nov

11 website components added to Hyped Up Brand (Header, Footer, Hero, Card, OfferPicker, Timeline, FAQ, Review, CommunityBand, PriceTable, ContactForm). WhatsApp button and category strip already existed (Button, ServiceList); video controls live in Hero.

The system has print-led components (Button, ContactBlock, HandMarks, ServiceList, SlantBanner, SprayHeading). The website needs these too, proposed as additions to the system, not one-offs:

- [x] Header (logo chip, Security · Upgrades · Styling menus, Open today status, Contact us pill) and phone menu
- [x] Footer (service lists, contact, outlined HYPED UP wordmark, slogan)
- [x] Floating WhatsApp button (phone)
- [x] Hero: video and photo versions, breadcrumb, "from £" tag
- [x] Category strip with arrows
- [x] Service card and build card (with focal point and video)
- [x] "What we offer" picker (tabs + what / why / best for)
- [x] How it works timeline
- [x] FAQ accordion + Explained box + Good to know
- [x] Review block (one Google CTA)
- [x] Community band and story cards
- [x] Contact form with states: empty, filled, error, sending, sent (email or WhatsApp choice)
- [x] Video controls (pause button, poster, reduced motion)
- [x] Add the security-photo exception and any new tokens (spacing and layout widths) to the README

## 2. Pages (phone, then desktop)

Built in this order, so each template is set before it is repeated:

- [x] Home A (brand-led) and Home B (task-led)
- [x] Hubs: Security, Upgrades, Styling
- [x] Security services: Ghost immobiliser, Car trackers, Dash cams, Car alarms, Taxi cameras
- [x] Upgrades services: CarPlay, Car audio, Remapping, Reverse cameras, Ambient lighting, Exhausts & performance parts
- [x] Styling services: Car wrapping, PPF, Window tinting, Air suspension, Coilovers, Chrome delete, Bodykits, Wheel refurb, Interiors, Detailing, Number plates, Van signage
- [x] Audience: Motorbikes, Business & fleet
- [x] Brand and support: Builds, Contact (+ form states), About, Blog, Shop, Community
- [ ] Shared states: open menu, 404 page

First pass done 21 Nov: all 36 pages on the canvas, desktop + phone, linked so Play clicks through (videos show their poster). That's 36 pages + states × 2 sizes. The Design canvas holds them as artboards grouped by section.

## 3. Handoff (for building on Cloudflare)

- [ ] `docs/design-build/handoff.md`: tokens, layout grid and breakpoints, every component with its states, spacing and behaviour (video, picker, accordion, form), image sizes and focal points, accessibility notes
- [ ] `docs/design-build/summary.md`: Claude Design link, screens, decisions and why, new components and tokens
- [ ] Update `CLAUDE.md` (design system and design file links) and `memory/decisions.md`

## Skills used

- `frontend-design` and `bencium-controlled-ux-designer`: keep Direction D consistent; ask before changing anything approved
- `design-tokens`: layout and spacing tokens missing from the system
- `ui-ux-pro-max` + accessibility checks as I go: contrast, 44 px tap targets, focus states, readable sizes
- After each section: compare against the brief, the v5 concept and the design system

## Open questions

1. The 41 "still to confirm with Hypa" facts stay hidden in the designs. Copy and images get swapped after the Hypa review.
2. Graffiti City needs a commercial licence before launch (already flagged in the design system).
3. Ruff Ryders UK's OK for the Community page faces is still pending.
