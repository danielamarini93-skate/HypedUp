# Design assets: sources and licences

_Collected 8 Nov 2026 for the Hyped Up concepts. Check again before launch._

| Asset | File(s) | Source | Licence |
|---|---|---|---|
| Paint marks (splat, drips, speckle, brush line, marker circle, brush circle, brush strokes, dry spray, smear) | `paint/*.svg` (Openclipart IDs 202417, 213808, 213823, 212674, 318600, 351243, 211151, 213817, 213832) | openclipart.org | Public domain (CC0). Cleaned with `paint/clean_svgs.py` (metadata removed, unwanted fills hidden, numbers rounded); used as CSS masks, so colour comes from CSS |
| Hand-drawn marker underline | `paint/hand-underline.svg` | Drawn for this project (generated tapered strokes) | Ours, no licence needed |
| Graffiti tag font: Hoax Vandal | `fonts/hoax-vandal.ttf` | 1001fonts.com (Sipanji x Figuree) | 1001Fonts Free For Commercial Use (FFC) |
| Spray wordmark font: Rubik Spray Paint | loaded from Google Fonts | fonts.google.com | SIL Open Font License |
| UI icons: Lucide | inlined from `lucide-static` 1.61.0 | lucide.dev / npm | ISC |
| Brand logos: WhatsApp, Instagram, TikTok, Facebook | `brands/*.svg` | Simple Icons 13.21.0 | CC0 (brand marks remain trademarks of their owners) |

**Not usable without buying a licence** (personal use only on 1001fonts): Marseloup, VTKS Smash, Bastrad.
Noun Project icons need a paid licence or attribution (CC BY): not used.

## Graffiti fonts Dani sent (8 Nov 2026), tested in `font-test.jpg`
**All are personal-use demos: a commercial licence is needed before any of them go on the live site.**
Font files are kept out of the repo (licence); re-download from the source if needed. The demos of Decipher and
Aerosoldier replace numbers with "personal use" watermarks: don't set digits in them.

| Font | Designer / source | Licence | Verdict |
|---|---|---|---|
| **Aerosoldier** (Regular, Drip, Spray, Basic, Symbols) | Måns Grebäck, mansgreback.com | Personal only, licence for sale | **Best real spray lettering → direction B** |
| **Decipher** (+ Symbols) | Måns Grebäck, mansgreback.com/fonts/decipher | Personal only, licence for sale | **Best handstyle tag → direction A** |
| Jraot (Regular, Extrude, Outline, Hollow) | Cikareotype / Sipanji21 (MyFonts) | Personal only | Bold, readable, more logo than tag |
| Gemstone | Blankids Studio, blankidsfonts.com | Personal only | Bold, readable |
| Graffiti City | Woodcutter (Etsy) | Personal only | Readable handstyle |
| Blank River | Colllab Studio | Personal only | Quick tag |
| Hesorder | Ronny Studio, ronnystudio.com | Personal only | Hard to read |
| Brick | Sesohq | Personal only | Handwritten, thin |
| Street Wars | Semuthitam (Creative Market) | Personal only | Too thin |
| Sister Spray | Imagex | Personal only | Demo missing letters |
| **Sedgwick Ave Display** | Google Fonts | **Free (SIL OFL)** | Free fallback/accent → direction C |
