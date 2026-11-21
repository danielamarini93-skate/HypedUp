# Hyped Up

**Protect it. Upgrade it. Style it.**
Security, screens, audio, wraps and air ride for cars and bikes. Built in London by Hypa.

This is the Hyped Up brand, version 2: a **digital-first rebrand** that merges the original brand pack (made for print: cards, leaflets, signage) with the new website's look, Direction D "Workshop wall", approved by Hypa in November 2026. One system for everything Hypa puts out: the website (hypedup.uk), Instagram and TikTok, promotions, print, livery and apparel.

**What stayed:** the logo and all its lockups, Hyped Up Red, black grounds, the slogan GET HYPED! STAY HYPED!
**What's new:** the graffiti logo ("Hype Up" tag), Big Shoulders + Barlow + IBM Plex Mono as the working type, Graffiti City as the spray layer, the logo's red band turned into a red gradient for every button and accent, hand-drawn marks, real graffiti and real photos.
**What retired to "heritage":** BankGothic and Blacksword (now only inside the logo lockups and reprints of old print), the flat red #E30613 as a UI fill, THE JACATRA.

Sources: the Drive brand folder (logos, colour sheet, fonts, cards, leaflet) and the website repo (GitHub `HypedUp`, branch `claude/clever-ptolemy-6fu8zg`: `site.css`, `visual-direction.md`, `brand-voice.md`, `decisions.md`). Where the two disagreed, the website's newer decisions win, except the logo, which never changes.

## 1. The idea: Workshop wall

A clean, confident grid (the precision of the work) with the marks of the people who do it on top: one spray word, a hand-drawn circle, real graffiti, real cars. **Big clean type carries the message; graffiti is one layer on top.**

Every piece should pass two tests:
- **Cover the logo:** it still looks like Hyped Up (dark ground, condensed uppercase type, one red gradient accent, one graffiti touch, a real car).
- **Squint:** the headline reads first, then the car, then the graffiti. If the graffiti wins, take some away.

## 2. Voice (tone of voice v2)

Conversational, easy to understand, modification-focused, direct, assertive, knowledge-heavy. We know what we're talking about; it must never read like AI wrote it. The vibe is UK car culture: talk to the reader as one of the scene.

1. **Lead with the mod, not the business.** Say what goes on the car and what it does.
2. **Prove you know it.** One real technical detail per block: a brand, part, method or trade-off (Air Lift 3P, Prazis struts, tank and compressor outside the cabin, wiring loomed and hidden). Only real facts, never invented specs.
3. **Short sentences, plain words.** Explain jargon in five words or fewer.
4. **Assertive, not salesy.** No "we strive to", "high-quality solutions", "one-stop shop", "fitted properly, priced clearly".
5. **Talk to "you", speak as "we"** (the workshop). "I" only for Hypa's own story and builds. FAQ questions stay in the customer's voice ("Can I…?").
6. **Any car or bike, cheap or expensive:** first cars, vans, R6s, supercars.
7. **SEO without stuffing:** service + place once in the headline/lead ("car wrapping in Bermondsey"), then write for people.
8. **Honest trade-offs** build trust: say when something isn't worth it.
9. **CTAs are a nudge:** "What are we building?", "Show us the car", "Send the spec". The main action everywhere is **Contact us**.

| Write | Not |
| --- | --- |
| Ghost immobiliser: no code, no start, even with your key. | Your car won't start without your code. |
| Colour changes, camo, stripes, logos. A full wrap takes at least a week, because the prep is the job. | Colour changes, designed with you, fitted by hand. |
| Security, screens, audio, wraps and air ride for cars and bikes. | South London's one-stop workshop… fitted properly, priced clearly. |

**Facts that never bend:** every job is bespoke (we listen first, it's made for your car) · only number plates are "while you wait" · full wraps take at least one week · no dyno testing, never mention it · never name a competing shop (product brands are fine: Ghost, Pandora, Scorpion, MetaTrak, Xtrons, Autostyle, Pioneer, Kenwood, Rockford Fosgate, Air Lift, Prazis) · prices only from the master price list, shown as "from £", low-key · UK English.

The slogan **GET HYPED! STAY HYPED!** is the sign-off: footer, end cards, print. Always capitals, both exclamation marks.

## 3. Logo

Unchanged. HYPED with the "UP" arrow inside the D, the red dot, the three rounded red bars of the E, the slashed H. **Never redraw, retype, recolour or rearrange it.** Files: Assets → Logos.

| Version | Use |
| --- | --- |
| Wordmark, white (SVG/PNG) | Default. Website header (on a dark `radius-md` chip), social, video. |
| Wordmark, black | White grounds only (paper, white vans). |
| Slogan lockup | End cards, profile images, footer. |
| Tagline lockup (red band + "at its finest") | Print, posters, livery, top of a price list. |
| Badge | Stickers, decals, photo/video watermark. |
| Apparel lockup | Clothing and merch only. |
| **Graffiti logo** ("Hype Up" tag with the arrow) | The art mark: social posts and covers, stickers, apparel, merch, the website's art layer (hero, footer, About). Dark ink on light, light ink on dark. |

**Graffiti logo rules:** it's the brand's graffiti signature, not a replacement for the wordmark. The wordmark still does the identifying job (website header, invoices, livery, anywhere the name must read instantly); the graffiti logo brings the energy. Use it big, as art, with room around it; at least 200 px / 50 mm wide, below that it turns into a blob. It counts as the screen's one graffiti touch: don't put a Graffiti City spray word next to it. Keep its own colours (charcoal #232323 or light grey #E1E1E1 with its red #CB140D): don't recolour it to the gradient, outline it or add effects. Never place it over busy photo areas.

Clear space: the height of the red dot all round. Minimum width: wordmark 120 px (header uses 32–38 px tall), tagline lockup 240 px. On photos, put it on a dark area or use the badge.

## 4. Colour

Dark only on screen. Red is the accent, never the ground.

| Role | Tokens | Notes |
| --- | --- | --- |
| Grounds | `ink-950` #0D0C0C, `ink-900` #141212, `ink-850` #1A1717 | Website and social. Print uses Brand Black `hu-black` #1D1D1B. |
| Text | `bone` #F2EEE9, `bone-80` #D3CCC7, `stone` #A39C97 | Warm off-whites, not pure white. |
| Red fill gradient | `red-3` #DE0613 → `red-4` #B5030F → `red-5` #86010A, at 100° | Buttons, the WhatsApp button, red panels. White text (5:1). Sampled from the logo's band. |
| Red text gradient | `red-1` #FF4033 → `red-2` #EF1220 → `red-3` #DE0613 | Accent words on dark, the spray word, prices. 5.6:1 at the light end. |
| Solid red | `red-solid` #FF3B2F on screen · `hu-red` #E30613 in print and logo | Icons, link arrows, focus ring; the hand-drawn circle. |
| Status | `open-green` #3FBF6A | The "Open today" dot only. |

Rules: no blue, no orange (both tried and retired). Gradients run left to right, subtle and premium, never a rainbow. Photos behind text are faded and dark so text stays at AA contrast.

The **Paper** theme exists only for print on white (invoices, a printed price list, the black logo on a white van). The website and social are dark.

## 5. Typography

| Role | Font | Use |
| --- | --- | --- |
| Display | **Big Shoulders Display** 900 (Google Fonts) | Every headline. Uppercase, line-height .88–.95. |
| Body | **Barlow** 400/600/700 (Google Fonts) | Everything you read; buttons in 700. |
| Labels | **IBM Plex Mono** 500 (Google Fonts) | Captions, eyebrows, table heads. Uppercase, tracked .08em, small. |
| Spray | **Graffiti City** | ONE word per heading or screen ("Style it.", "styling"), in the red text gradient; and numerals 1 2 3. Never sentences. |
| Slogan | Original by fnkfrsh | GET HYPED! STAY HYPED! only. |
| Heritage | BankGothic, Blacksword | Inside the logo lockups and old print reprints only. |

**Licences to sort before launch:** Graffiti City is a personal-use demo (buy the commercial licence; the repo only has a 79 KB subset). Check BankGothic and Blacksword too if they're used outside the logo files. Big Shoulders, Barlow and Plex Mono are free (SIL OFL).

## 6. Graphic language

- **Real graffiti, not fake spray.** Use real graffiti photos and illustrations (the workshop mural, artwork made for Hyped Up), never clip-art splats, drips or code-drawn spray. Graffiti sits behind or beside headlines, faded and dark behind text. (Graffiti images and illustrations: Assets → Graffiti.)
- **Hand-drawn marks: only two.** The marker **circle** (around a place or a key word, in `hu-red`) and the marker **underline** (under a selected option or one key word, in `red-2`). No hand-drawn arrows, long lines, geometric bars or dots on screen.
- **One spray word + one hand mark per screen.** One primary action per screen.
- **Photos:** real Hyped Up work in full colour, high contrast, with a strong radial vignette; square corners. Faded photos can sit behind sections (dark enough for AA text).
- **Icons:** Lucide, 2px stroke. Brand icons (WhatsApp, Instagram, TikTok) from Simple Icons.
- **Buttons are pills** in the red fill gradient; photos and panels are square.
- **Hover is never red** (Dani, 21 Nov 2026): links, menu items, card titles and icons turn `ink` (bone) with an underline. Red stays on the pill buttons, the "you are here" marker in the menu and the focus ring.
- **Print and social can also use the heritage patterns:** the slanted red band from the logo (−1.5°), the tilted red services panel (−2.5°), the huge ghosted UP arrow in `hu-charcoal`.

## 7. Photos and video

- Real Hyped Up work only: no stock, no other shops' work. Mix cars and bikes.
- **Always blur customers' number plates**, following the plate outline only (soft 1 px edge, never a box over the car). Hyped Up's own cars and show plates are fine.
- **No customer faces.** Hypa and the team can appear.
- Hero videos: silent loops ≤ 15 s, ~1 MB, poster image, no autoplay with reduced motion.
- Files: descriptive names (`bmw-3-series-wireless-carplay-install-bermondsey.webp`), plain alt text, compressed, metadata and GPS stripped.

> **Security rule, no exceptions:** Autowatch Ghost, Meta Scorpion and Datatool units and installs are **never photographed or filmed**: not the unit, its location, the wiring or the inside of panels. Promote these services with type, the logo, graffiti and a generic car shot only.
>
> **Exception (Dani, 21 Nov 2026):** product branding in the customer's hand is fine: the MetaTrak leaflet, a tracker tag or a fob held up in front of the car. Still never the unit itself, where it's fitted, the wiring or inside panels.

## 8. Channels

| Channel | How the system applies |
| --- | --- |
| **Website** | Dark only. Sticky header with the logo chip, "Open today" status and a Contact us pill. Menu: Security · Upgrades · Styling. Floating red WhatsApp button on phones. "From £" prices on service pages only. Footer: outlined HYPED UP wordmark with a gradient stroke, slogan. |
| **Instagram post** 1080 × 1350 | Full-bleed car photo with vignette, Big Shoulders headline, one spray word or hand circle, wordmark or badge in the same corner every time. |
| **Story / Reel / TikTok cover** 1080 × 1920 | Text in the middle 1080 × 1420; wordmark top, "Contact us" / "Send the spec" bottom. |
| **Print** (leaflet, card, poster) | Tagline lockup, Brand Black ground, Big Shoulders headings, Barlow lists, red band or tilted panel, contact block with red icons, QR code. |
| **Livery and apparel** | Logo lockups as supplied; one-colour where possible. |

## 9. Website components

Added 21 Nov 2026 in the design build (Claude Design file: https://claude.ai/artifact/5cJ4xZwusEATjcqwoi8boT). Styles live in `components/bundle.css` (classes start `hu-`); each component has a guide and a live preview under Components.

| Component | Where |
| --- | --- |
| Header | Every page. Logo chip, Security · Upgrades · Styling, Builds, Open today, ONE red Contact us pill. Phone: Menu sheet. |
| Footer | Every page. Find us + four plain link columns (no accordion) + legal + outlined wordmark. |
| Hero | First screen. Headline, lead, CTA above the fold, photo or silent video with pause button. |
| Card | Service, build, blog and shop cards. |
| OfferPicker | "What we offer" on service pages: what it is, why choose it, best for. |
| Timeline | "How it works", Graffiti City numerals. |
| FAQ | Accordions + Explained box (hubs) + Good to know (services). |
| Review | One real Google review, one CTA to Google. |
| CommunityBand | "More than a workshop" on Home, Motorbikes, About. |
| PriceTable | "From £" tiers (bike wraps, business). |
| ContactForm | Need chips, car, photos, send by WhatsApp or email; empty, error, sent states. |
| Button, ServiceList (strip), HandMarks, SprayHeading, ContactBlock | From v2, unchanged. |

## 10. Merch and illustrations

The merch range carries the brand's fun side. First piece: **the cartoon Mini** (Hyped Up's own red F56 Mini JCW, slammed, in front of a graffiti wall with the logo's "UP" arrow), for T-shirts and keyrings. Files: Assets → Merch.

- **Light garments:** `mini-cartoon.png` as drawn.
- **Black and dark garments, keyrings, stickers:** `mini-cartoon-keyline.png` with the white die-cut outline, otherwise the black linework disappears into the fabric.
- **T-shirt:** centred on the chest, about 25–28 cm wide (adult). Small Hyped Up wordmark or graffiti logo on the back neck or sleeve, not crowding the illustration. Optional slogan GET HYPED! STAY HYPED! on the back.
- **Keyring:** die-cut acrylic along the white keyline, about 5–6 cm. The arrow and wall can be cropped tighter at this size if detail fills in.
- **Don't** recolour it, redraw parts of it, add effects or put text over it. The red stays as drawn.
- Apparel is ordered by WhatsApp request (no online checkout). Put the apparel lockup on swing tags and the shop page.
- New illustrations follow the same style: thick black outline, flat shading, Hyped Up red, real Hyped Up builds only, plates left off or shown as the HYPED plate.

## 11. Contact details (always written the same way)

Unit 22, Enterprise Industrial Estate, Bolina Road, London SE16 3LF
Mon–Fri 10:00–18:00 · Sat 09:00–16:00 · Sun closed
020 3340 0632 · WhatsApp 07713 735646 · info@hypedup.uk · hypedup.uk · @hypedup.ltd

## 12. Before anything goes out

Real logo file · dark ground · Big Shoulders uppercase headline · one red gradient accent · at most one spray word and one hand mark · real photo, plates blurred, no customer faces · **no Ghost / Meta Scorpion / Datatool unit or install shown** · voice v2 (we/you, one real detail, no filler) · no same-day promise except plates · prices "from £" from the master list · contact details as in §11.
