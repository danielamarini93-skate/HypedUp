# Technical checklist: everything from leaving GoDaddy to launch

_Date: 2026-11-08 · Status: **proposal, Dani to decide the timing** · Details behind each item: `docs/design-thinking/tech-setup.md`
Timing key: **Now** = safe to do during design, no build needed · **Design** = during `/design-build` · **Build** = after the concept is approved · **Launch** · **After launch**_

## 1. Decisions
| # | Item | Proposed timing | Why then | Who |
|---|---|---|---|---|
| 1.1 | ✅ **Decided 8 Nov:** code site in GitHub, hosted on **Cloudflare** (framework picked at build) | Done | Shapes how editing, forms and the dashboard work; design doesn't depend on it | Dani (Claude recommends) |
| 1.2 | ✅ **Decided 8 Nov:** Claude via GitHub only (no CMS) | Done | Changes the build effort and Hypa's day-to-day | Dani + Hypa |
| 1.3 | Keep or retire Google Tag Manager | Build | Only matters once tracking is wired | Claude |
| 1.4 | Email sending service (Resend or Brevo) for the form | Build | Free tiers are similar; pick when wiring the form | Claude |
| 1.5 | Instagram: hand-picked builds at launch, automatic feed later? | Design | Affects the builds section layout | Dani |

## 2. Accounts and access (quick, safe)
| # | Item | Proposed timing | Who |
|---|---|---|---|
| 2.1 | ✅ `main` is the default branch | Done | Dani (2 clicks) |
| 2.2 | ✅ DNS zone exported and reviewed → `memory/dns/` (gaps: no DKIM/DMARC) | Done | Dani, Claude guides |
| 2.3 | ✅ Email plan confirmed separate from Website Builder | Done | Dani |
| 2.4 | ✅ Dani already admin on GA4, Search Console, Business Profile | Done | Hypa / Dani |
| 2.5 | ✅ Business Profile identifiers saved (`memory/marketing.md`); Place ID looked up with the API key | Build | Claude finds it |
| 2.6 | Old GoDaddy images: skipped (Dani is putting newer media in Drive); blog images pulled at migration while the old site is still live | Build | Claude |
| 2.7 | ✅ Instagram is already a Creator account (works with the official API) | Done | Hypa |
| 2.8 | Hosting account (Cloudflare or Vercel) in Hyped Up's name, two-step login | Build | Dani |
| 2.9 | Google Cloud project + Places API key (reviews) | Build | Dani, Claude guides |
| 2.10 | Meta developer app + token (Instagram feed) | After launch | Dani, Claude guides |
| 2.11 | Connectors: Microsoft 365 (email data), Cloudflare (hosting) | Build | Dani |

## 3. Site foundations
| # | Item | Proposed timing | Who |
|---|---|---|---|
| 3.1 | Page map + URL structure (service pages, car-specific pages) | Design | Dani + Claude |
| 3.2 | Old → new URL redirect map (all 11 pages + 15 posts, list already in `memory/current-site.md`) | Build | Claude |
| 3.3 | Design system as code: colours, type, components from Claude Design | Build | Claude |
| 3.4 | Price list → one data file, "from £" on the site (`memory/price-list-master.md`) | Build | Claude; Hypa confirms Ghost + head-unit table |
| 3.5 | Image and video pipeline: compression, modern formats, size budget per page | Build | Claude |
| 3.6 | Blog migration: 15 posts (text already archived) + images | Build | Claude |
| 3.7 | Preview site hidden from Google until launch | Build | Claude |

## 4. Forms, email, reviews, Instagram
| # | Item | Proposed timing | Who |
|---|---|---|---|
| 4.1 | WhatsApp quote links with service + car pre-filled | Build | Claude |
| 4.2 | Contact form → info@hypedup.uk, spam check (Turnstile), enquiry log | Build | Claude |
| 4.2b | ✅ DMARC (watch-only) live · ✅ DKIM signing enabled | Done | Dani |
| 4.3 | Email records in GoDaddy DNS (add SPF include + DKIM for the sending service; Microsoft 365 untouched) | Build | Claude writes, Dani pastes |
| 4.4 | Automatic Google reviews (daily job, rating + count + latest 5) | Build | Claude |
| 4.5 | Builds section: hand-picked from Drive at launch | Build | Dani picks, Claude builds |
| 4.6 | Automatic Instagram feed with a hide list | After launch | Claude |

## 5. Privacy and legal
| # | Item | Proposed timing | Who |
|---|---|---|---|
| 5.1 | Cookie banner (on-brand, Accept/Reject equal) + Google Consent Mode | Build | Claude |
| 5.2 | Privacy and cookie policy pages | Build | Claude drafts, Hypa approves |
| 5.3 | Claims wording decided (20+ years, Thatcham, insurance, tinted lights, shadow plates) | Before final copy (end of Design) | Hypa |

## 6. Search and AI visibility
| # | Item | Proposed timing | Who |
|---|---|---|---|
| 6.1 | Titles and descriptions per page (≤65 / 155–160 characters) | Design | Claude, Dani reviews |
| 6.2 | Structured data: business, services, FAQs, articles, reviews | Build | Claude |
| 6.3 | Sitemap (with blog posts), robots.txt, llms.txt | Build | Claude |
| 6.4 | Search Console: verify new site, submit sitemap | Launch | Claude |
| 6.5 | Directory listings with identical name/address/phone (Bing, Apple Maps, Yell…) | After launch | Dani |

## 7. Analytics and dashboard
| # | Item | Proposed timing | Who |
|---|---|---|---|
| 7.1 | Agree the 5 dashboard numbers and who reads them | Build | Dani |
| 7.2 | Cookie-free visitor stats | Build | Claude |
| 7.3 | GA4 (same ID) after consent + enquiry events (WhatsApp, call, email, form, by service) | Build | Claude |
| 7.4 | Looker Studio dashboard (GA4 + Search Console + enquiry log) | Launch | Claude |
| 7.5 | Monthly Claude report | After launch | Claude |

## 8. Quality checks (`/design-review`)
| # | Item | Proposed timing | Who |
|---|---|---|---|
| 8.1 | Accessibility: full WCAG 2.2 AA scan (AccessLint) + keyboard and screen-reader checks | Before launch | Claude (on Dani's computer if the tool is blocked here) |
| 8.2 | Speed: mobile Lighthouse ≥ 90, page weight budget | Before launch | Claude |
| 8.3 | Every old URL redirects; every form, link and button tested | Before launch | Claude |

## 9. Launch day
| # | Item | Who |
|---|---|---|
| 9.1 | Point the website record at the new host (only that record changes) | Dani with Claude |
| 9.2 | Test email in and out straight away | Dani |
| 9.3 | Remove "hidden from Google", submit sitemap | Claude |
| 9.4 | Watch Search Console and enquiries for 2 weeks | Claude |
| 9.5 | Keep GoDaddy Website Builder 1 month, then cancel **only** that plan (never the domain or email) | Dani |

## Summary: proposed "now" list
1. Choose the platform and the editing approach (1.1, 1.2)
2. Default branch on GitHub (2.1)
3. Export the DNS records and check the email plan (2.2, 2.3)
4. Admin access to GA4, Search Console, Business Profile; find the Place ID (2.4, 2.5)
5. Download all images from the GoDaddy site (2.6)
6. Instagram to Business/Creator (2.7)
7. Claims wording and the dashboard numbers (5.3, 7.1)

Everything else waits until the concept is approved.
