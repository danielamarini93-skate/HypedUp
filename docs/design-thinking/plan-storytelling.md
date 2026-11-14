# Plan: Round 3, storytelling rewrite (draft for Dani's OK)

_14 Nov 2026. Responds to Dani's feedback: too much price and keyword copy, too editorial and text-heavy, not enough photos,
graffiti/handmade marks or visible gradient. The site map and IA v2 stay as they are. What changes is how the content is told._

## What changes

### 1. Story first, prices last
- **Homepage A (brand-led)** opens on Hypa's story in three beats: *first Astra (early 2000s) → McLaren → Hyped Up, SE16
  (2022)*. Each beat is a big photo, a spray word and one line. No price on the homepage at all.
- **"No limits" wall:** a dense photo wall with every service as a sprayed or stencilled label on a photo, not a list. It tells
  the visitor "any car, any idea".
- **Service pages:**
  - The hero becomes a photo or video with one line in Hypa's voice.
  - "From £" moves down to a small tag beside the Contact button.
  - Removed or shortened: the option tables, the long FAQ and the keyword paragraphs.
  - The FAQ keeps only the 3 questions people actually ask.
  - The SEO text stays, but short and in Hypa's voice.
- **About** becomes a full story page: Astra → McLaren → Hyped Up, then "what I believe" (listen first, any car, no limits,
  done properly).

### 2. Projects (the 5 signature builds)
Builds becomes **Projects**. Each project gets its own story card on the Projects page, with *what they wanted → what I did →
the result*. Every story gets a photo strip and a handwritten note. The projects are also linked from the matching service
pages.
| Project | Services it proves | Photos found so far |
|---|---|---|
| Audi: the silent performer | Soundproofing, air suspension | Prazis air strut with the sound deadening visible (IMG_3017) |
| Friend's van, roof beacons | Van/business, lighting | Not found yet: Instagram or Dani |
| The red Mini (own) | Air, audio/boot builds, styling | Mini JCW (several), fibreglass boot mould in progress (IMG_1750, to confirm) |
| BMW 1 Series convertible (own) | Audio, next a wrap and bodykit | Interior with the Hyped Up keyring (IMG_0669); boot build photo still needed |
| Charity barber's motorbike | Custom audio, motorbikes | Not found yet: Instagram or Dani |

### 3. More services ("no limits")
Add as their own lines on the hub, plus small pages where people search for them:
- **Soundproofing / sound deadening** (proved by the Audi)
- **Custom builds and fabrication** (boot builds, fibreglass, speaker pods)
- **Motorbike audio and Bluetooth speakers**
- **Beacons and work lights** (vans)
- **Starlight headliners** (already under ambient lighting)
- **Car-meet / show prep**

All still TBC with Hypa: OBD port protection, catalytic converter protection.

### 4. Look: on brand, visible
- **Gradient everywhere it counts:**
  - the logo red gradient (#DE0613 → #86010A) on every button;
  - big gradient spray words;
  - gradient strokes on the handmade marks;
  - one gradient "paint drip" divider between sections.
  - All the reds become one token set (the audit found 7 different reds).
- **Graffiti layer:**
  - one Graffiti City spray word per screen (Protect / Upgrade / Style / No limits / Hypa);
  - handmade arrows, circles and underlines pointing at the real work in photos;
  - the workshop mural used as a background texture.
- **Photo- and video-led layouts:**
  - full-bleed photos, photo walls and before/after sliders (the Mini CarPlay before/after already exists);
  - short muted video loops on the homepage and project cards.
  - Text sits in short blocks over the photos.
- **Logo:** the real logo in the header and a large logo or show-plate moment in the footer. The show plates on customer cars
  ("HYPED UP") are a brand asset: use them.
- Review notes (TBC yellow, grey "photo needed" blocks) move to the review board only, never into the page look.

### 5. Media
- **Photos reviewed so far:** 38 of about 180.
- **New usable photos found today:**
  - the R8 in front of the mural with a Pioneer box (show plate);
  - the Mercedes E-Class with a Thinkware box (show plate);
  - the R6 motorbike at the unit entrance under the sign;
  - the Mini CarPlay before/after;
  - the R8 Pioneer screen;
  - the Prazis air strut;
  - the fibreglass mould.
- **Not usable as they are:** the car-meet photos (IMG_9935/36) show faces and customer plates. They would need blurring, or
  could be a faded background only.
- **Videos:** 120 in Drive, with no names.
  - First I check the 23 short MP4s: these are edited reels, 0.4–3 MB each.
  - I take one frame from each and pick the best 4–6 loops.
  - Then I look at the long MOVs only where a project is still missing.
- Every new photo gets logged in `docs/design-build/media-log.md`, with customer plates blurred.

## Order of work
1. Media pass (videos plus the remaining photos), with a contact sheet for Dani.
2. Rewrite `content.py` in story-first form (homepage, About, Projects, service heroes).
3. Build tokens and visuals: one red set, gradient, graffiti layer, photo layouts.
4. Rebuild, run the checks (links, 390 px, H1, meta lengths), and publish concept v5 to the same artifact link.
5. Commit and push; update the memory files.
