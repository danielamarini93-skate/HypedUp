# Contact flow and quote form (draft for approval)

_9 Nov 2026 · From Dani + Hypa's feedback: not everyone should be pushed to WhatsApp; Hypa likes a form that arrives
by email. Status: **approved by Dani (photos: yes); drawn in the key pages concept** https://claude.ai/artifact/H2XetEmAA8gnXPLicnvFpt_

## The flow
| Where | Action | Goes to |
|---|---|---|
| Header (desktop + phone), service pages, homepage | **"Contact us"** (primary button, logo-red gradient, no WhatsApp icon) | `/contact` |
| Phone only | **Floating WhatsApp button** (always visible, bottom corner) | WhatsApp chat, opens with a short message |
| `/contact` | The quote form; at the end the customer picks **Send by email** or **Send on WhatsApp** | Email → info@hypedup.uk · WhatsApp → chat with the form text written in |
| Service pages | "Contact us" carries the service, so the form opens with it ticked (`/contact?service=ghost`) | `/contact` |

Replaces the earlier rule "main action = WhatsApp quote everywhere". WhatsApp stays one tap away on phones.

## The form (mix of the old site form + the concept form)
Order follows how Hypa quotes: what → which vehicle → details → who → how to reply.

| # | Field | Type | Required | Why Hypa needs it |
|---|---|---|---|---|
| 1 | **What do you need?** | Tick boxes: Security · CarPlay & screens · Audio · Wrap or tint · PPF · Air suspension · Remap · Number plates · Something else | at least 1 | Routes the quote; feeds "enquiries by service" |
| 2 | **Vehicle** | Text: "Make and model, e.g. BMW M140i" | yes | Parts and price depend on it |
| 3 | **Reg plate** | Text | optional | Exact spec and year (CarPlay, Ghost, remap) |
| 4 | **Tell me more** | Text area | optional | Budget, ideas, timing |
| 5 | **Photos** | Upload, up to 3 (email route only) | optional | Wraps, damage, interiors (Dani: yes) |
| 6 | **Name** | Text | yes | |
| 7 | **Phone** | Tel | yes for WhatsApp, else optional | Call-back, tracker column "Phone" |
| 8 | **Email** | Email | yes for email | Reply, tracker column "Email" |
| 9 | **How did you find us?** | Select: Google · Google Maps · Instagram · TikTok · Friend or family · Been before · Other | optional | Tracker columns "Referral Source", "Repeat Customer?" |
| 10 | **Send it** | Two buttons: **Send by email** · **Send on WhatsApp** | | Customer's choice |

- Under the buttons, one line: "WhatsApp opens with your message written. Nothing is sent until you press send."
- Labels above fields (not placeholders only), 16 px text, errors in words next to the field (WCAG 2.2 AA).
- Spam: Cloudflare Turnstile (invisible), no maths puzzle.
- Privacy line + link; the reg plate is only used for the quote.
- Email lands in Outlook with the customer as reply-to; each enquiry is also logged (service, source) for the dashboard (see `tech-setup.md`).
- Thank-you state: "Got it. Hypa usually replies within [TBC] on working days."
