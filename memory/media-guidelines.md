# Media guidelines: how photos and videos are prepared for the site

_Agreed 8 Nov 2026. Source media: Dani's Google Drive folders (see `website-migration.md`). Originals always stay in Drive, untouched._

## For every image
1. **Pick and check:** sharp, well lit, shows Hyped Up's own work. No stock, no other shops' work.
2. **Privacy check (decided by Dani, 8 Nov 2026):** always **blur customers' number plates**. **No customer faces**: skip or crop photos where a customer's face shows. Hypa and the team, Hyped Up's own cars (red Mini, 1 Series) and show plates are fine.
3. **Rename** to describe what it shows, lowercase with hyphens:
   `<car-or-bike>-<service>-<detail>-<area>.webp`, e.g. `bmw-3-series-wireless-carplay-install-bermondsey.webp`.
   No "IMG_4532", no keyword stuffing, max ~6 words.
4. **Alt text:** one plain sentence of what's in the picture (for screen readers first, Google second),
   e.g. "Wireless Apple CarPlay screen fitted in a BMW 3 Series dashboard". No "image of".
5. **Caption** where it helps: car + work done (the tape-label style in the concept).
6. **Compress and resize:** modern formats (AVIF/WebP with JPG fallback), several sizes so phones get small files,
   lazy-load anything below the first screen. Target under ~200 KB per image on mobile.
7. **Strip metadata:** remove camera/phone data (EXIF) and GPS from published files. Keep copyright/creator
   ("Hyped Up Ltd") in the file info.
8. **Structured data:** service pages and builds get `ImageObject` markup (name, caption, creator Hyped Up,
   license/copyright, content location "Bermondsey, London SE16"). Images go in the sitemap.

## For every video
- Short silent loops for heroes (≤ 15 s, ≤ ~1 MB, poster image, pause button, no autoplay with reduced motion).
- Longer videos: compressed MP4 (H.264) + poster, captions/subtitles file if there's speech, `VideoObject` markup
  (title, description, thumbnail, duration, upload date). Optionally also on YouTube for reach, embedded with a
  light, click-to-load player.
- Same naming and privacy rules as images.

## Location
- **Location goes in the text and structured data**, not in photo GPS. Google has said photo GPS data isn't used
  for ranking, and GPS in published files can leak private addresses (customers' homes, Hypa's).
- What does help: area names in captions and page copy ("fitted in Bermondsey"), the business's address in
  `LocalBusiness` markup, `contentLocation` on images, and the same photos posted to the Google Business Profile.

## Tracking
- A media log (`docs/design-build/media-log.md`, created when media is first used): original Drive file → new name,
  alt text, page used on, privacy check done.
