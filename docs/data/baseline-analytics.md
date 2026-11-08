# Analytics baseline before the redesign (Google Analytics 4)

_Period: 10 Aug – 7 Nov 2026 (13 weeks) · Exports from Dani, 8 Nov 2026 · Raw CSVs in `ga4-2026-11-07/`._

## Headline numbers
| Measure | 13 weeks | Notes |
|---|---|---|
| Visitors (active users) | **~245** (226 UK) | ~19 a week, rising: 11–23/week in Aug → 25–31/week in Oct |
| Sessions | **~384** | |
| Page views | **828** | ~3.4 per visitor |
| Engagement rate | **69%** (UK) | Average engaged time ~74 s per visitor |
| Key events (conversions) | **0** | **Nothing is set up as a conversion** |

## Where visitors come from (sessions)
| Channel | Sessions | Notes |
|---|---|---|
| Google (organic search) | 142 | Bing 5 |
| Direct | 140 | Typed URL, QR codes, WhatsApp links |
| Referral | 50 | **autostyleuk.com 45**: the Autostyle partner page sends real traffic |
| **AI assistants** | **32** | **chatgpt.com 32**: ChatGPT already recommends Hyped Up |
| Organic social | 16 | Instagram 13–14, Facebook 2 |
| Paid (Google Ads) | 0 tracked | Maps ads aren't linked to GA4 |

## What people look at (views)
| Page | Views | Read |
|---|---|---|
| Home (`/` 315 + `/hyped-up` 139) | 454 | The same page counted under two addresses |
| **Multimedia / CarPlay** | **107** | The most-viewed service page |
| Contact | 72 | |
| Security | 51 | |
| Wraps / PPF / tint | 42 | |
| Air suspension | 37 | |
| Audio | 20 | Low, although Google shows it 2,500 times (see search baseline) |
| Remapping | 10 | |
| Apparel | 8 | |
| All blog posts together | ~25 | Blog brings very few visitors so far |

## Behaviour and devices
- **Form: 24 people started it, 1 sent it.** A 96% drop-off: the GoDaddy form is losing almost every email enquiry.
- **WhatsApp and phone taps aren't tracked at all** (only a generic "click" event: 50). We can't see the main enquiry channel.
- **Safari 134 of ~245 visitors** (mostly iPhones), Chrome 80, Samsung 12: design and test for iPhone Safari first.

## What this means for the redesign
1. **Track enquiries properly:** WhatsApp, call, email and form taps as key events, by service and page.
2. **Fix the form:** short, mobile-friendly, few fields; WhatsApp stays the main action.
3. **CarPlay/multimedia is the top service page** → strong case for car-specific CarPlay pages.
4. **AI visibility is already real** (ChatGPT 32 sessions): keep content answer-shaped and factual (FAQs, prices, structured data).
5. **Partners send traffic:** ask Xtrons, Air Lift, Prazis, MetaTrak and Scorpion for installer-finder listings like Autostyle's.
6. **One address per page** (home is split across two).
7. **Link Google Ads to GA4** so Maps ad visits show up.

## Targets after launch (proposal)
- Enquiry taps tracked from day one; baseline them in month 1, then grow
- Form completion from 1 in 24 to at least 1 in 3 starts
- Visitors from ~19/week to 50+/week within 6 months

## GoDaddy Conversations (screenshot from Dani, 8 Nov 2026)
GoDaddy's inbox for messages that arrive through the website (and any channels connected to it). **Last 12 months, all channels:**
| Measure | Value |
|---|---|
| Conversations | **73** (~6 a month) |
| Messages | **130** (~1.8 per conversation) |
| Average response time | **14.1 hours** |

- **This inbox disappears when we leave GoDaddy.** Its job moves to: WhatsApp (main), the new form → info@hypedup.uk, phone.
- **14 hours to reply is slow** for people comparing quotes. The new form email should land in Outlook where Hypa sees it, plus an instant auto-reply ("Got it, we'll reply today; for a faster answer WhatsApp 07713 735646").
- TBC: which channels feed it (website chat? form? Facebook/Instagram?): the "All Channels" dropdown shows the split.
