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
