# Current Live Site (GoDaddy) — Audit

_Audited 7 Nov 2026 from https://hypedup.uk/ · GoDaddy Website Builder ("Starfield Technologies") · images on `img1.wsimg.com`_

## Every URL on the live site (all need a 301 to their new address)

### Pages (from `/sitemap.website.xml`)
| Old URL | Page title |
|---|---|
| `/` = `/hyped-up` (same page, two URLs) | Vehicle Security & Modifications South London \| Hyped Up |
| `/vehicle-security` | Vehicle Security South London \| GPS Tracking & Immobilisers |
| `/multimedia-upgrade` | Apple CarPlay Installation & Multimedia Upgrades London |
| `/audio-upgrade-electronics` | Audio Upgrade Electronics ⚠️ weak title |
| `/wrapping-ppf-tinting` | Wrapping PPF Tinting ⚠️ weak title |
| `/vehicle-remapping-tuning` | ECU Remapping London - Boost Your Vehicle Performance |
| `/air-suspension` | Air Suspension Installation by Hyped Up London |
| `/contact-us` | Car Modifications in Bermondsey \| Hyped Up London |
| `/hyped-up-apparel` | HypedUp Merchandise \| Car Enthusiast Clothing & Accessories |
| `/blog` | Vehicle Security & Car Mods Blog \| Hyped Up South London |
| `/privacy-policy` | — |

### Blog posts — pattern `/hyped-up/f/<slug>` (15 live)
Full text of every post is saved in `content/blog-archive/<slug>.md` (with `old_url` in each file).
Also feeds: `/blog/f.rss`, `/blog/f.atom`, `/blog/f.json`.

| Slug | Title |
|---|---|
| the-low-life-chose-me-why-air-suspension-changed-everything | The Low Life Chose Me: Why Air Suspension Changed Everything |
| car-tuning-in-london-how-to-pick-a-safe-tuner | Car Tuning in London: How to Pick a Safe Tuner |
| why-every-london-car-owner-needs-security-right-now | Why Every London Car Owner Needs Security Right Now |
| the-legal-reality-of-car-mods-in-the-uk--what-dvla-actually-cares | The Legal Reality of Car Mods in the UK – What DVLA Actually Cares |
| car-detailing-paint-correction-ceramic-coating | Why Ceramic Coating Became My Secret Weapon |
| custom-number-plates-in-london-same-day-service-styles | Your Custom Number Plate in 10 Minutes |
| air-suspension-bodykit-fitting-perfect-your-stance | Air Suspension & Bodykit Fitting: Perfect Your Stance |
| apple-carplay-installation-south-london-%7C-hyped-up | Apple CarPlay Installation South London ⚠️ "\|" encoded in URL |
| number-plate-cloning-is-surging-how-to-protect-yourself | Number Plate Cloning Is Surging |
| vehicle-wrapping-ppf-window-tints-dechroming-signage | Vehicle Wrapping & PPF South London |
| ecu-remapping-boost-power-efficiency-safely | ECU Remapping South London: More Power Done Properly |
| car-audio-upgrade-premium-sound-with-subwoofers-lighting | Car Audio Upgrade South London |
| ghost-immobiliser-south-london-cost-fitting-is-it-worth-it | Ghost Immobiliser South London: Cost, Fitting & Is It Worth It? |
| how-much-does-a-car-wrap-cost-uk-real-prices-not-marketing | How Much Does A Car Wrap Cost UK? |
| best-dash-cam-2026-front-rear-gps-why-you-need-one | Best Dash Cam 2026: Front & Rear, GPS & Why You Need One |

⚠️ Search Console (8 Nov 2026) shows posts indexed under **three** patterns: `/hyped-up/f/<slug>`, `/f/<slug>` and `/blog/f/<slug>`, plus the homepage at both `www.` and bare domain. Redirect all variants.

⚠️ Blog posts are **not** in the sitemap — Google only finds them via the blog page. Fix in the new site.

## Tracking found in the live HTML
- GA4 `G-PZPFNLV5SW` — **present**, so the site does appear to have been published. Confirm in GA4 → Realtime.
- GTM container `GTM-M8LSHHLK`
- Search Console verification meta tag: `google-site-verification` = `fw2dNGYmTQ0Su2Bj7whtf1dZsBVkyQ-RI08cZZ7589s` (copy this into the new site's `<head>`)

## Things on the live site that aren't in the memory file
- **Socials:** TikTok `@hypedup.ltd`, LinkedIn `linkedin.com/company/hypedupltd`, as well as Instagram
- **Apparel shop:** Graffiti T-shirt £20 · Hyped Up T-shirt £20 · Hyped Up Jumper £40 · The Keyring £10
- **Security brands also listed:** Quartix, Datatool, Cobra (on top of MetaTrak, Scorpion). "TfL London approved CCTV for taxi drivers"
- **Tuning extras:** RaceChip, cold air induction kits, quick shifters; **mobile** Stage 1 remaps (engine and gearbox)
- **Wrap/tint extras:** headlight and rear light tinting, chameleon windscreens, sunstrips, sign writing, branded livery
- **Audio extras:** tweeters, ambient lighting, starlights, under-car lighting
- **Suspension:** static setups too — performance coilovers, lowering springs
- **Areas served:** Bermondsey, Peckham, **Canada Water**, Camberwell, all SE postcodes
- Claims: "Reduce premiums up to 30%", "the only shop in the area offering same-hour number plate service", "Customers rate us 5 stars"
- Trust bar now says "20+ Years **Expertise**" — the "Experties" typo is already fixed

## ⚠️ Prices on the live site that clash with `pricing.md` — Hypa to confirm
| Where | Live site says | pricing.md says |
|---|---|---|
| Homepage: security | GPS tracker & dash cam **from £395** | dash cam from £150; Ghost from £400; tracker on enquiry |
| Homepage: multimedia | Apple CarPlay **from £195** | CarPlay **from £600** installed |
| Homepage: number plates | **from £35** | from £30 |
| Homepage: wraps/PPF/tints | from £150 | tint from £150 ✓ |
| Homepage: ECU remap | **from £435** | Stage 1 £250–400 |
| Remap page | mobile Stage 1 **from £199** | Stage 1 £250–400 |

## Weaknesses to fix in the redesign
- Duplicate homepage (`/` and `/hyped-up`)
- Weak titles on audio and wrapping pages; meta descriptions missing location on some pages
- No dedicated pages for Ghost, trackers, dash cams, tinting, number plates, PPF, detailing
- Blog post URLs live under `/hyped-up/f/` rather than `/blog/`
- Lots of text is duplicated in the page HTML (the builder renders sections several times)
