# Site concept v5: media-led rework (plan)

_20 Nov 2026. From Dani's brief: Hypa in more than half the media, about 50/50 video and photo, montages where one clip
isn't enough, show the community (meets, Ruff Ryders UK), and still sell first. Source: the sorted Drive Media folder._

## What I reviewed
- **Videos:** 315 in Drive, 142 reviewed frame by frame. The other 173 are over the connector's 10 MB download limit
  (mostly long raw clips and the Prazis brand films), so they can't be pulled from here. Notes are in
  `drive-sort/video-review.md`.
- **Photos:** every file tagged Hypa, "check if Hypa" or meet, on top of the 66 already in use.

## What the footage says about the business (and changes the content)
1. **Hypa is on the tools in most of it.** Tinting, air struts, screens, boot builds, wraps, van lettering, starlight
   headliners. The site should show his hands and face, not just finished cars.
2. **The workshop is the brand.** The red/grey floor, the Mini mural and the HYPD plates appear in almost every shot,
   so the media is recognisable as Hyped Up without a logo.
3. **Unit 22 is a meeting place.** Bike meets with Ruff Ryders UK, a coffee black cab, a car-meet line-up, bikes
   ridden off the estate. That is the "be part of it" story, so it gets its own page and a homepage band.
4. **Bikes matter more than the old site shows:** M1000RR tracker, R1, MT-07 CarPlay and carbon, Kawasaki decals,
   Hypa's carbon streetfighter.
5. **Craft work deserves a spotlight:** fibreglass boot mould, starlight fibres, custom speaker pods.

## Rules for every page
- **One moving piece per screen at most.** The hero or one feature loop. Everything else is photo.
- **Video:** silent loop, 6–14 s, square 720 px, under ~1.5 MB, poster image, paused for reduced motion, pause
  button. No baked-in text, no music.
- **Hypa share and video share are counted** by the build from the media manifest and shown on the review board.
- **Privacy:** customer plates blurred or cropped out. Meet faces only small, from behind, or with the club's OK
  (TBC: Hypa to ask Ruff Ryders UK). No children. No vans carrying other garages' names.

## Montages (made with ffmpeg: hard cuts, no music)
| Loop | Clips | Used on |
|---|---|---|
| Workshop reel | Hypa tinting, Hypa on air struts, Hypa fitting a screen, Hypa on a boot build, starlight, Evoque wrap, 911 outside the unit | Home hero (A and B) |
| Community | Ruff Ryders meet at the unit, R1 riding out of the estate | Home band, Community, Motorbikes |
| Per service | 2–3 clips of the same job | Service heroes (see manifest) |
| Builds | A4, E88, Stelvio starlight, Evoque, BDG | Builds page stories |

## Page changes
- **Home A/B:** reel hero. Builds as before. New band, "Unit 22 on a Sunday" (community loop + Hypa at the door).
  Services tiles become Hypa-at-work photos.
- **Services:** hero becomes a short loop of that job where we have one (14 of 23), with a Hypa photo as poster or
  second image.
- **Community (new page):** meets, Ruff Ryders UK, coffee cab, bikes. One CTA: follow on Instagram, or come by.
  Linked from the footer "More" and Motorbikes.
- **About:** Hypa on the streetfighter as hero, workshop loop, "What I believe" over the aisle shot.
- **Builds:** each signature story leads with its montage.

## Still needed from Dani/Hypa
- OK from Ruff Ryders UK to show members' faces (or we keep to wide shots, which is what this version does).
- The 173 large videos: for the real build, export the best ones at a smaller size or share them another way.
- Facts still TBC as before (prices, years, partner wording).
