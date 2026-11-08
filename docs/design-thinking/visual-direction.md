# Visual direction (concept stage)

_Date: 2026-11-08 · Brief from Dani: "reflect the workshop; Hypa is very creative and happy;
follow the brand colours; add graffiti style, art and craft, with automotive and motorbike spirit."
This is a direction for the concept. The design system is built in Claude Design during `/design-build`._

## In one line
**"Workshop wall."** A clean, confident grid (the precision of the work) covered in the marks of
the people who do it: tags, stickers, tape, hand-drawn arrows, spray, paint pen (the creativity).

## Keywords
Workshop · spray paint · paint pen · stickers and tape · garage wall · track day · moto culture ·
hand-made · loud but friendly · precise · South London

## Colour (from the logo)
| Token idea | Colour | Use |
|---|---|---|
| Ink | near-black `#0E0E0F` | main background (workshop dark) |
| Bone | off-white `#F4F1EA` | text on dark, paper-like light sections |
| Hyped red | logo red `#E1251B` (to sample exactly from the logo) | primary action, highlights, spray marks |
| Concrete | mid grey `#8A8A85` | secondary text on light only (check contrast) |
| Accent (optional, sparing) | hi-vis yellow `#FFD400` | stickers/tape, "new" tags; never body text |

Contrast guardrails (WCAG 2.2 AA): bone on ink and ink on bone pass easily. White on Hyped red needs
checking at small sizes (use bold/large text or a darker red for small text). Yellow only with ink text.

## Type
- **Display:** a condensed, heavy sans in uppercase (motorsport, livery numbers), e.g. *Anton*, *Bebas Neue*, *Archivo Black/Condensed*. Big, tight, confident.
- **Marker/hand layer:** a marker or paint-pen script for short notes and tags only (2–4 words), e.g. *Permanent Marker*, *Rock Salt*. Never for body or buttons.
- **Body:** a friendly, very legible sans, e.g. *Inter*, *Manrope*. 16 px minimum on mobile.
- (Avoid the friend's "motorsport technical" look: thin hairlines, numbered labels, desaturated photos. Ours is warmer and messier.)

## Graphic language
- **Hand-drawn marks** on top of layout: circles around key words, arrows to buttons, underlines, crossed-out words ("~~template~~ → custom"). Drawn as SVG strokes so they're light and sharp.
- **Stickers:** brand badges ("Electronics", "Est. 2022", "SE16", "Air Lift dealer"), slightly rotated, as accents (not navigation).
- **Tape and labels:** masking-tape style labels on photos ("Abarth 595 · Hexis pink").
- **Spray texture:** subtle overspray edges behind section titles or the hero, using a small image or CSS mask, not huge files.
- **Real photos first:** full colour, high contrast (not desaturated). The workshop mural, cars, bikes, tools, Hypa at work.
- **Moto + auto:** mix cars and bikes in the work, icons (helmet, wheel, plug) only as tiny sticker details.

## Motion (light)
- A slow tagline marquee; marks "drawing in" once on load; hover lift on cards.
- All motion off with `prefers-reduced-motion`. No autoplay video on mobile; tap to play.

## Do / don't
| Do | Don't |
|---|---|
| Let one hand-drawn mark guide the eye to the main action | Cover text with graffiti or put marks behind body copy |
| Keep the grid strict so the chaos feels intentional | Use more than one marker font, or marker font for paragraphs |
| Use Hyped red for actions and a few highlights | Turn everything red |
| Show Hypa and real customers' cars | Use stock photos or other shops' work |
| Keep security pages calmer (less marks, more clarity) | Make the "worried owner" feel it's not serious |

## References
- Mobbin: Freshman (hand marks on car footage), YLLW (photo service cards), Slush (sticker tiles), Monte (visit block). See `mobbin.md`.
- Real world (to collect into a board in `/design-build`): workshop mural photos, Hypa's Instagram, sticker culture at car meets, motorsport livery numbers.

## To confirm with Dani
- Exact logo red (sample from the original logo file)
- Whether yellow is welcome as a small accent
- Font licences: Google Fonts suggested above are free

---

## v0.2 feedback from Dani (8 Nov 2026), applied in concept v0.2
- Hero was **too crowded, too many CTAs**. Wanted: **craft, minimal, straight to the point**.
- **Above the fold must be clear and minimal, with a video.**
- **Challenge the brand more:** more creativity; allowed to add another accent colour and to play with shades of black and grey.
- **Message:** Hyped Up is a **full modification and styling shop, one stop for anything you like**. Electronics and styling are **two starting points, not the limit**.

### What changed in response
- Hero: full-bleed workshop video (silent loop), one headline, one line, **one action**. No stickers, rating or second button above the fold.
- Palette: graphite scale (asphalt → concrete) + Hyped red + a new **signal blue** that codes electronics (red codes styling, chalk white codes "anything else").
- Type: industrial condensed display (Big Shoulders) instead of Anton; marker used once per screen at most.
- Homepage: "start anywhere" (Electronics · Styling · Anything else), builds, how a build works, one review, Hypa, visit. Prices move to service pages.

---

## v0.3 feedback from Dani (8 Nov 2026, on the menu & footer concept)
- **No blue.** Use shades of grey and shades of red; **add orange**; **gradients are welcome** (red → orange).
- **More graffiti, more art:** brush strokes, paint splashes, spray-can texture and drips.
- Applies to every concept from now on (the homepage concept still has signal blue: update it at the homepage step).

## v0.4 feedback from Dani (8 Nov 2026, menu & footer v2)
- Code-drawn marks aren't good enough: **use real graffiti assets** (PNG/SVG splatters, spray lines), recoloured to the palette.
- **Real graffiti fonts** for the art layer (references: Marseloup, Hoax Vandal, VTKS Smash, Bastrad; source 1001fonts "spray paint").
  The footer "HYPED UP" should use one.
- **Icons: Lucide**, everywhere, for consistency.
- **More spray circles and spray lines to highlight** key things (e.g. "Find us" in the footer).
- **CTA gradient must be subtle** (premium), not a strong red → orange.
- **Likes the orange** in the menu.
- Try a version with **rounded, smooth corners on some elements only (e.g. images)**.

### What v0.4 uses (menu & footer v3)
- Graffiti fonts: **Hoax Vandal** (tags: "Find us", "Not sure…") and **Rubik Spray Paint** (HYPED UP wordmark). Both free for commercial use.
- Real paint marks from Openclipart (public domain), recoloured with CSS: splat, drips, speckle, brush line, marker circle.
- Icons: Lucide; brand logos: Simple Icons.
- Button gradient: subtle (#c2040f → #cf1a0d). Logo 44 px (phone) / 52 px (desktop).
- Rounded corners: offered as a toggle for images (14 px). Sources and licences: `concept/assets/SOURCES.md`.

## v0.5 feedback from Dani (8 Nov 2026, menu & footer v3)
- Splash: not good. Brush line: terrible. Graffiti fonts: not legible. "You can do better."
- Lesson: decorative graffiti built from generic clip-art and display fonts reads cheap. Next step is to agree a
  direction (and references) before building again.

## Style moodboard (8 Nov 2026): https://claude.ai/artifact/3zP6kfZV8cBYNNGFqDimgc
Built from Dani's references (Rage Machine and Kelsi fonts, Playlist Edition #6 magazine, Air Max poster, SAMS by Cuberto,
URBANTH). Shared principle: **big clean type carries the message; graffiti is one layer on top**.
- **A · Street editorial:** grey paper, wide Archivo Expanded, mono labels, B/W photos with an orange tag, stickers, barcodes.
- **B · Spray machine:** dark, Big Shoulders headlines, one Rubik Wet Paint spray word in orange, spray-blob CTA.
- **C · Gallery gesture:** light and calm, Instrument Serif, rounded photos, one hand-painted circle/stroke per screen.
Decision pending (Dani). Source: `concept/moodboard/`.

### Moodboard feedback (Dani, 8 Nov 2026)
- References for all 3 are very good; **execution needs more craft**.
- **B: no fake spray** (code/clip-art spray looks bad). Graffiti energy must come from real things: the spray *font* and real photos.
- **Try dark mode for A and C.**
- **Pick the right photo for each style.**

### Moodboard v2 (8 Nov 2026)
- **A · Street editorial:** dark by default (light toggle); B/W halftone show photo (Mini JCW + person in hoodie); orange Hoax Vandal tag over the photo; issue/meta line; crop marks; numbered Protect/Upgrade/Style columns; barcode.
- **B · Spray machine:** no fake spray. Real graffiti = the workshop mural photo behind the red Mini; one Rubik Wet Paint word "Style it."; **Big Shoulders + Barlow** (the menu/footer fonts Dani liked); pill buttons with subtle gradient; Protect/Upgrade/Style strip with "from" prices.
- **C · Gallery gesture:** light by default (dark toggle); SAMS-style thin column header; Instrument Serif headline with one hand-drawn circle around "Style it."; Porsche 964 as a framed print.

### Moodboard v3 (8 Nov 2026): Dani's fonts applied
- A tag: **Decipher** · B spray word: **Aerosoldier Spray** · C accent: **Sedgwick Ave Display** (free). Font test + licences: `concept/assets/SOURCES.md`, `font-test.jpg`.
- Before launch: buy the commercial licence for whichever paid font is chosen.

### Moodboard v4 feedback (Dani, 8 Nov 2026)
- **C:** square image corners; **drop orange, red only** as accent; "Style it." marked with a different shape, e.g. just a line.
- **A:** photo **in colour** with a **very strong vignette**.
- **B:** accent = **red into orange**, dark and subtle gradient for depth, used on **all accents and CTAs**; spray word in **Graffiti City** (font 02).
