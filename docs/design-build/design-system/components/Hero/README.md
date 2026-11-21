# Hero

First screen of every page: headline (Big Shoulders, one spray word at most), a lead, ONE "Contact us" pill, and a real photo or silent video loop with the vignette.

- The CTA sits right under the lead and must be above the fold on desktop (1440 × 900) and phone (390 × 844) (Dani, 21 Nov 2026). On the homepage the video is capped at `min(560px, 100vh − 260px)` on desktop and 16:9 on phones.
- Homepage: video first on phones, text first on desktop (1.2fr / 0.8fr). Service pages: breadcrumb, H1 = service name, lead, pill + low-key "from £" price, a one-line price note.
- Video: muted, looping, `playsinline`, poster image, pause button (`.hu-vpause`, 44 px), never autoplays with reduced motion, plays only while on screen.
- You provide: H1, lead, media (photo or video + poster + alt), optional price.
