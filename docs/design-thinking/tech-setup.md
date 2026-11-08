# Technical setup: what GoDaddy did for us, and how we replace it

_Date: 2026-11-08 · Answers Dani's questions on cookies, forms → email, reviews, analytics and the dashboard.
Proposals, not built yet. Platform assumed: a code site in GitHub on free hosting (Cloudflare or Vercel)._

## Is it harder than GoDaddy?
GoDaddy bundled everything behind switches. Without it, each piece is a small service we connect **once**.
Claude can do almost all of it (code, settings files, DNS records written out step by step). Dani's part is
creating a few free accounts and approving each DNS change. After setup it runs by itself, and everything is
in our hands: the data, the look, the code.

| Job | GoDaddy today | New site | Who does what |
|---|---|---|---|
| Hosting | Included | Cloudflare (free) | Dani creates the account; Claude deploys |
| Cookie banner | GoDaddy's banner | Our own, on-brand (or none, see below) | Claude builds |
| Contact form → email | GoDaddy form | Form → email service → info@hypedup.uk | Dani: free account + approve 2–3 DNS records; Claude builds |
| Google reviews | Static, by hand | Pulled from Google automatically, daily | Dani: Google Cloud key; Claude builds the daily job |
| Analytics | GA4 tag in settings | GA4 + cookie-free stats + enquiry tracking | Claude adds; Dani grants access |
| Search Console | HTML tag | Same tag in the new site (or DNS) | Claude |
| Dashboard | None | Looker Studio + monthly Claude report | Claude builds; Dani views |
| Domain + Microsoft 365 email | GoDaddy | **Stay at GoDaddy, untouched** | Only the website record changes |

## 1. Cookie banner
- **The rule (UK):** you need consent before setting *non-essential* cookies. Google Analytics counts as non-essential, so GA4 needs a banner with a real "Reject" button. Cookie-free analytics need no banner. UK rules on simple analytics cookies are being relaxed; check the position again at launch.
- **Recommended:**
  - **Cookie-free stats** (Cloudflare Web Analytics, free) run for every visitor with no banner: visits, pages, countries, devices.
  - **GA4** loads only after "Accept", using Google Consent Mode, so we still get modelled data when people decline.
  - **Banner design:** small, bottom corner, on-brand, two equal buttons ("Accept" / "Reject"), never covering the hero or the main action. That fixes audit issue 2.
- Built with a small open-source consent script (no monthly fee) instead of a paid cookie platform.

## 2. Custom form that lands in the inbox
A website on free hosting has no mail server, so the form posts to a tiny **form handler** that sends the email.
- **How it works:** visitor fills in the form (name, phone, car/reg, service, message, optional photo) → our handler (a small Cloudflare function in the repo) checks it for spam → sends it to **info@hypedup.uk** through an email service (e.g. Resend or Brevo, free tier) → also saves a copy to a log (e.g. a Google Sheet) so enquiries feed the dashboard.
- **Spam:** Cloudflare Turnstile (free, invisible "are you human" check, no cookies).
- **Email setup (careful):** the domain's SPF record is currently `v=spf1 include:secureserver.net -all`, which is strict. To send from the website without landing in spam, we **add** the email service to SPF and add its DKIM records, in GoDaddy DNS. Microsoft 365 records stay exactly as they are. Claude writes the exact records; Dani pastes them in GoDaddy.
- **Reply flow:** the email arrives in Outlook with the customer as "reply-to", so Hypa just hits Reply. WhatsApp stays the main action; the form is for people who prefer email or need to send detail.
- **"Data from emails":** with the log above, every web enquiry is counted by service and source automatically. Reading *all* inbox email (not just web forms) would need a Microsoft 365 connection: possible later, more sensitive.

## 3. Google reviews, automated
- **Recommended:** a scheduled job (runs daily, free on GitHub/Cloudflare) asks **Google's Places API** for Hyped Up's rating, review count and latest reviews, and the site shows them. No third-party widget, no extra cookies, fast.
- **What Google returns:** the overall rating, the total count and up to **5 reviews** (Google picks them). Google requires showing the reviewer's name and a "Google" attribution, which suits our design.
- **Cost:** about 30 calls a month. That should sit inside Google's free monthly allowance (confirm when setting up).
- **Dani's part:** a Google Cloud account, enable Places API, create a key (Claude guides click by click). We also need the **Place ID** of the Google Business Profile.
- **Alternative:** widget services (Trustindex, Elfsight) are point-and-click, but add a third-party script, cookies and usually their branding on free plans. Not recommended.
- **More than 5 reviews:** the Google Business Profile API can read all reviews, but needs Google's approval for the business account. Worth applying later.

## 4. Analytics: what we track
| Source | What it tells us | Banner? |
|---|---|---|
| Cloudflare Web Analytics | Visits, top pages, referrers, devices | No |
| GA4 (`G-PZPFNLV5SW`, kept) | Journeys, events, conversions, Ads link | Yes (after consent) |
| Enquiry events | Every WhatsApp / call / email / form tap, by service and page | Counted in both |
| Search Console | Google searches, clicks, rankings, indexing | No (not on the site) |
| Google Business Profile | Calls, directions, profile views, reviews | No |
| Form log | Each web enquiry with service and source | No |

## 5. The dashboard
- **Always on:** a Looker Studio dashboard (free) linking GA4, Search Console and the form log. One page, five numbers: enquiries by channel and service · visitors and top pages · non-brand Google clicks · reviews and rating · site speed.
- **Monthly:** Claude reads the same sources and writes a short report with what changed and what to do next (Hypa's "personal assistant" use).

## 6. Order of setup (at build time)
1. Cloudflare account + site preview (hidden from Google)
2. Cookie-free stats + GA4 with consent + enquiry events
3. Form handler + email service + SPF/DKIM records (test email both ways)
4. Places API key + daily reviews job
5. Search Console on the new site, Looker Studio dashboard
6. Launch: switch the website record at GoDaddy, keep email records, 301 redirects live

## Open questions
- Which email service (Resend vs Brevo): decide at build time
- Form log: Google Sheet or a small database
- Who gets dashboard access (Dani, Hypa)
