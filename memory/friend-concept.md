# Friend's Concept Site (reviewed 7 Nov 2026)

_Status: **under consideration — not adopted, not in this repo.** Source: two zips Daniela uploaded
(`2Archive.zip` = config + public files, `1Archive1.zip` = `src/`). Together they form one project, "hypedup-site", concept v2 dated 6 Nov 2026._

## What it is
- **Astro 7** static site, hosted free on **Cloudflare Workers** (static assets), `npm run deploy` via wrangler
- Built as a surprise for Hypa; a preview link was meant to come with it (Daniela to find it)
- Pages: home, 7 service pages (security, carplay, audio, wraps, air-suspension, performance, number-plates),
  `/build/` spec builder, `/shop/` (merch), `/journal/` (blog, 14 posts), privacy, 404, plus hidden `/whats-new/` (note to Hypa) and `/guide/` (GoDaddy move plan)
- All business facts, prices, hours and service copy live in one file: `src/data/site.ts`
- ~40 real workshop photos (from Instagram 2023–24), real logo, workshop video reel, Archivo font
- Design: "motorsport technical": sharp corners, hairlines, condensed uppercase headings, red accent
- Claimed Lighthouse: 96–98 mobile speed, 100 accessibility (not verified — we couldn't build it here)

## What's good
- `public/_redirects` already maps **every** old GoDaddy URL (pages + all 15 posts) to the new ones with 301s
- JSON-LD schema built in (LocalBusiness in the layout, FAQ schema per service, Article per post) — no GTM hack needed
- Sitemap generated automatically; `noindex` everywhere until launch (safe preview)
- No data collection: quote form, spec builder and shop just open WhatsApp with a pre-written message
- Code is small, clean and readable; no third-party scripts or tracking
- `/guide/` is a sound, careful migration plan (keep domain at GoDaddy, copy every DNS record to Cloudflare, email records "DNS only", test email straight away, keep GoDaddy builder a month)
- Fixed bugs found on the live site: two "Call us" buttons dialling a US (+1) number, WhatsApp link on the contact page with an extra 0

## What's missing or needs work
- **No GA4 (`G-PZPFNLV5SW`), no GTM, no Search Console meta tag.** (DNS already has a `google-site-verification` TXT record, so Search Console may survive via DNS — confirm.)
- No `.git` history and no `.claude/commands` (`/preview`, `/check`, `/new-post`, `/publish`) despite HANDOVER.md mentioning them: they weren't in the zips
- Uses the **old live-site prices** (security £395, CarPlay £195, plates £35, remap £435) + air suspension "from £1,800" (not in our pricing list)
- Posts 16–22 not included (not written yet in their version); DVLA post deliberately left out
- Hours (Mon–Fri 10–18, Sat 9–16) come from a directory listing, not confirmed
- Mentions a second phone number from LinkedIn (020 3727 7271) and a Facebook page
- Uses "Journal" instead of "Blog" and `/journal/` URLs (fine, but a choice)
- Photos are mostly low-res Instagram screenshots
- Running the code here was blocked by the session's safety check (external code). To build it,
  Daniela would need to allow it, or run it on her own computer.

## ⚠️ Content rules that clash with our memory — need a decision
The friend's `CLAUDE.md` bans claims our memory/blog voice currently uses:
| Friend's rule | Our memory says | Friend's reason |
|---|---|---|
| No "20+ years" | "20+ years experience" | LinkedIn: McLaren motorsport technician 2017–2020, driving instructor (ADI) before |
| No "Thatcham Approved" for the business | Live site says "Thatcham Approved" | Thatcham approves products, not workshops |
| No "insurance approved" / "up to 30% off premiums" | Live site says both | Unsourced; insurers decide individually |
| No chameleon windscreens or tinted lights | Live site sells them | Illegal on UK roads (75% windscreen / 70% front sides) |
| Shadow/magnetic plates = show/off-road only | Price list includes them | Not British Standard compliant |
| Remaps: "tell your insurer", never "declare to DVLA" | — | DVLA doesn't need telling about remaps |
| Colour-change wraps must be declared on the V5C | — | DVLA requirement |
| Hypa never named by real name anywhere | — | Privacy |
These look legally sensible; they also matter for blog posts we write. **Hypa/Daniela to decide**, then update `brand-voice.md`.

## Facts learned from it (also copied into the relevant memory files)
- Company: **Hyped Up Limited, company no. 14086991**
- Email is **Microsoft 365 bought through GoDaddy** (MX → `hypedup-uk.mail.protection.outlook.com`)
- DNS records from a public lookup (6 Nov 2026): MX (Outlook), SPF `v=spf1 include:secureserver.net -all`,
  MS verification TXT, google-site-verification TXT, pinterest-site-verification TXT, CNAMEs autodiscover / lyncdiscover / sip / msoid / email, SRV _sip._tls + _sipfederationtls._tcp
- Brands also fitted: Thinkware dash cams, Datatool trackers, JB4 modules, KESS3 remap tool; films from 3M, Avery Dennison, Oracal, Hexis
- Facebook: facebook.com/p/Hyped-Up-100086498654920/
