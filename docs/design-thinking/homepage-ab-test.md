# Homepage A/B test plan

_14 Nov 2026 · Dani: "Homepage: let's see and test how it works best, we could do an A/B test and find out."
Both versions are in the site concept (`home-a.html`, `home-b.html`)._

## The two versions
| | **A · Brand-led** | **B · Task-led** |
|---|---|---|
| Hero | "Protect it. Upgrade it. Style it." (with the font morph) + workshop video + Contact us + Find us | "Car and bike security, upgrades and styling" + 5.0 Google rating + **service finder** (Security / Upgrades / Styling tabs listing every service with "from £") + Contact us |
| Video | In the hero, autoplay, silent | Lower down, tap to play |
| Then | Three-group strip with "from £" → recent builds → how a job works → Built by Hypa → review → contact band | Recent builds → workshop video + brand line → how a job works → review → contact band |
| Bet | The brand and the work make people trust and ask | Showing every service and price straight away gets people to the right page faster |

## What we measure
- **Primary:** share of homepage visitors who reach `/contact` **or** tap WhatsApp/call (any page, same session).
- **Secondary:** clicks into a service page from the homepage · form sends · bounce from the homepage · scroll depth.
- **Guardrail:** no drop in calls and direction requests on Google Maps (Business Profile insights, monthly).

## How it runs (when the site is live)
1. Cloudflare splits homepage visitors 50/50 with a first-party cookie (same visitor always sees the same version; no third-party tool, no extra cookie banner category beyond analytics consent).
2. GA4 records the version as a custom dimension (`home_variant = A | B`) on every event.
3. Search engines always get version A (one canonical homepage, no SEO risk).
4. Paid traffic (Google Maps ads) is split the same way and reported separately.

## How long and when to decide
- Traffic today is about 500 site visitors a month (GA4 baseline), so the test needs time: **run 8 weeks or until each version has ~600 homepage visits**, whichever comes later.
- Decide on the primary metric; with this traffic only a clear gap (roughly 30% better or more) will be trustworthy. If the gap is small, pick the version Hypa prefers and keep the best block from the other (e.g. B's service finder as a section in A).
- Before launch, a cheap first signal: show both versions to 5 customers (5-second test: "what does this business do, where would you tap?").

## Status
- Both versions designed (site concept v4). To build: the Cloudflare split + GA4 dimension at `/design-build` / launch (added to `docs/tech-checklist.md`).
