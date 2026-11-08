# Design thinking: plan

_Hyped Up website redesign · Stage 1 of 3 · Depth: medium · Status: **approved by Dani 8 Nov 2026, in progress**_
_Inputs: `intake.md`, `CLAUDE.md`, `memory/`, live site hypedup.uk_

## Steps

- [x] **1. Brief** → `brief.md` (dani-studio template)
  Project summary, business goals with measures, audiences, scope (incl. WhatsApp-request
  shop), constraints (budget, GoDaddy domain + Microsoft 365 email, legal claims), success
  metrics, stakeholders (Dani leads, Hypa signs off facts), milestones. Unknowns = `TBC`.

- [x] **2. Strategy** → `strategy.md` (dani-studio template + a **technical strategy** section)
  - UX strategy: problem, positioning (electronics first, styling second, "we adapt the car
    to you"), priorities, what we won't do, experience principles, riskiest assumptions.
  - Technical strategy, joined to the UX goals:
    - **Run from Claude:** publish posts, change prices and pages from chat, no browser needed
    - **Search + AI:** structured data, page per service, FAQ blocks, llms.txt, local SEO
    - **Data you own:** analytics options (GA4, plus a privacy-friendly alternative), Search
      Console, enquiry tracking (WhatsApp / call / email clicks), email data (see questions)
    - **Dashboard:** what it shows, who reads it, how often; built so Claude can report on it too
    - **Platform shortlist** scored against these requirements (decided after the brief, as agreed)

- [x] **3. Preliminary audit of hypedup.uk** → `audit.md`
  UX heuristic review (Claude) + `accessibility-scan` on the homepage + `seo-audit` (medium).
  Top issues ranked by impact, each labelled *observed / data / recommendation*.

- [x] **4. Competitor analysis** → `competitors.md` (internal only, never named on the site)
  4–5 London/UK installers (security + electronics + styling), plus 2 best-in-class brand-led
  sites from outside the sector (custom motorbike/garage culture, creative studio). Table stakes,
  opportunities, avoid.

- [x] **5. Mobbin research (web)** → `mobbin.md` (+ key screens in `mobbin/`)
  Homepage heroes for creative/brand-led sites · service grids · portfolio/gallery and
  before–after · reviews/trust sections · quote/contact flows · small merch shop sections.

- [ ] **6. Proto-personas (3)** → `personas.md`
  E.g. the worried owner (security), the tech upgrader (CarPlay/audio/dash cam), the
  enthusiast/stylist (wraps, air, show car). Marked unvalidated, with what to check.

- [ ] **7. Visual direction** → `visual-direction.md`
  Brand red/black/white + graffiti, art and craft, car + motorbike spirit, workshop energy,
  Hypa's creative and happy personality. Keywords, do/don't, type and texture ideas,
  with accessibility guardrails (contrast, legibility over graffiti).

- [ ] **8. Summary** → `summary.md`: problem, key insights, direction and why, what the concept shows.

- [ ] **9. Quick HTML concept: homepage, mobile first** → artifact + `concept/index.html`
  Low-to-mid fidelity: structure, hierarchy, real content, one primary action (WhatsApp quote).

- [ ] **10. Hand over**: check every output against this plan, update `CLAUDE.md`, open **one
  pull request** for this stage, ranked next steps (→ review concept → `/design-build`).

## Assumptions (TBC)
- Research picks: I've proposed **all four** (audit, competitors, Mobbin, proto-personas).
- Brand colours = logo red, black and white; no formal brand guidelines exist.
- Concept uses existing photos for now; your new photos and videos replace them later.

## Answers (8 Nov 2026)
- Research: all four ✓ · Competitors: Claude proposes ✓ · Mobbin: save picks to a collection ✓
- Q4–6 (email data, dashboard, photo sharing): not answered yet. Proposals marked TBC in the strategy

## Questions for Dani
1. **Research:** OK with all four (steps 3–6), or drop any?
2. **Competitors:** any shops you want in? Otherwise I'll propose them.
3. **Mobbin:** save the picks to a Mobbin collection for Hyped Up?
4. **"Data from emails":** do you mean (a) enquiries that arrive at info@hypedup.uk,
   (b) newsletter/email marketing stats, or (c) both?
5. **Dashboard:** who looks at it (you, Hypa, both) and what are the 3–5 numbers you most
   want to see? (e.g. visitors, enquiries by service, top pages, Google ranking, reviews)
6. **New photos and videos:** how will you share them (upload here, Google Drive link,
   Instagram)? Not needed until the concept; I'll use existing ones until then.
