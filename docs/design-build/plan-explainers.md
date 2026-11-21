# Plan: one explainer per page

21 Nov 2026 · Design build · **Status: approved 21 Nov. First batch of 6 in progress.**

## Why

Dani liked "Layer it" on the Security hub: one block built for that topic that makes it easier to understand. Today every service page has the same layout (hero → What we offer → How it works → FAQ → Related). Some topics need more context, so each page gets **one explainer that answers the question people really have before they buy**, in a layout that fits that answer. Goals: trust (we know our stuff), fewer "is it legal / will it work" messages, and SEO (these are the questions people search).

## The explainer types (built once in the design system, reused)

| Type | What it looks like | Good for |
|---|---|---|
| **A. Threat → fix** | Row per way cars get stolen, what stops it | Security |
| **B. Decision path** | "Which one is right for my car?" 2–3 routes with when to choose each | CarPlay, upgrades |
| **C. Law in one picture** | A real photo of the car with each window/plate marked with a hand-drawn circle and the legal figure | Tint, plates, exhausts |
| **D. What happens, step by step** | Numbered story (Graffiti City numerals) | Trackers, wraps, Ghost |
| **E. Side-by-side** | 2–3 columns, plain comparison | Air vs coilovers, PPF vs ceramic, factory alarm vs Scorpion |
| **F. Upgrade ladder** | Stages from small to full, what you notice at each | Audio, remaps, detailing |
| **G. Where on the car** | Real photo, hand-circled zones | PPF, bodykits, dash cams |
| **H. Before / after** | Two photos side by side | Chrome delete, ambient, wheels |

Hand-drawn marks only (Dani's taste): diagrams are **real photos marked with the brush circle**, not code-drawn lines.

## Page by page (first proposal)

| Page | Explainer | Type | Needs research or Hypa? |
|---|---|---|---|
| Security hub | Layer it (exists) + **How cars get stolen in London**: relay, key cloning through the OBD port, lifted onto a truck, and which layer stops each | A | Light research (methods only, no stats invented) |
| Upgrades hub | **Will it work in my car?** New screen, keep factory screen, or interface: by car age and screen | B | No |
| Styling hub | **Looks or protection?** Wrap, PPF, tint, ceramic on one grid: changes the look / protects / both | E | No |
| Ghost | **How relay theft works, and where Ghost stops it** (3 steps) | D | No |
| Car trackers | **What happens when your car is stolen**: alert → monitoring centre → police → recovery | D | Check wording with Hypa |
| Dash cams | **What each camera sees**: front, rear, cabin, parked (photo with zones) | G | No |
| Car alarms | **Factory alarm vs Scorpion** | E | Confirm Scorpion features with Hypa |
| Taxi cameras | **What TfL asks for** (checklist) | C/list | **Research TfL rules** |
| CarPlay | **Three routes** with pros and cons | B | No |
| Car audio | **The upgrade ladder**: speakers → deadening → amp + sub → custom build | F | No |
| Remapping | **Stage 1, 2, 3 explained** + "Is it safe? Insurance?" box | F | Hypa (insurance wording) |
| Reverse cameras | **Sensors or camera?** | E | No |
| Ambient lighting | **Lights off / lights on** | H | Photos exist (starlight) |
| Exhausts & parts | **What's legal: noise, MOT, insurance** (links the DVLA blog post, which already ranks 8.7) | C | **Research** |
| Car wrapping | **A week in the workshop**: strip, clean, wrap, edges, refit, check (why a full wrap takes at least a week) | D | Hypa to confirm stages |
| PPF | **Where chips happen** (front end circled) + PPF vs ceramic | G + E | No (search data: "clear bra vs ceramic" 110/mo) |
| Window tinting | **UK tint law in one picture**: windscreen 75%, front sides 70%, rear any | C | Law known; quick check |
| Air suspension | **How air ride works**: bags, tank, compressor, management + air vs coilovers vs springs | D + E | No |
| Coilovers | **Coilovers or springs?** (shares the comparison) | E | No |
| Chrome delete | **Before / after** | H | Need a before photo |
| Bodykits | **Parts on the car**: splitter, skirts, diffuser, spoiler (circled) | G | No |
| Wheel refurb | **From kerbed to new**: steps | D | No |
| Interiors | **Materials**: carbon, Alcantara, leather swatches | E | No |
| Detailing | **Correction levels 1 · 2 · 3** | F | Hypa (what each level includes) |
| Number plates | **What makes a plate legal**: font, spacing, BS AU 145e mark, show plates off-road | C | **Research DVLA rules** |
| Van signage | **Lettering, part wrap or full livery**: how much van each covers | E | No |

Motorbikes and Business already got theirs this morning (layers, who we fit for, how it works). About, Builds, Community, Contact: no change.

## Research I can do myself

- **Search questions:** WebSearch for "People also ask" style questions per topic, plus the keyword data we already have (`memory/seo.md`, `docs/design-thinking/keyword-map.md`, Search Console baseline).
- **Facts:** TfL taxi CCTV rules, DVLA number plate rules, UK tint law, exhaust noise/MOT, declaring mods to insurers: official sources only (gov.uk, TfL, DVLA), linked in the notes.
- **Not reachable from here:** AnswerThePublic (no connection), DataForSEO (not signed in).

## Order

1. Build the 8 explainer types into the design system (one component each).
2. Write the copy page by page (Hypa's voice, real facts only, anything unconfirmed goes on the review board, never on the page).
3. Add them to the concept + canvas, phone first. One explainer per page, placed right after "What we offer".
4. Tick, commit, publish, then show Dani.

## Dani's answers (21 Nov)

- **First batch of 6**, one of each kind: Styling hub, Ghost, Car trackers, Window tinting, Car wrapping, Car audio. Review, then the other 20.
- **Diagrams = real photo + brush circles** with short labels. No code-drawn lines.
- **Dani will send AnswerThePublic exports** (tint, wrap, Ghost, tracker, audio, PPF/ceramic). Build now with reachable data; fold the exports in when they arrive.
- **Unconfirmed facts: keep it general**, list the details for Hypa on the review board.

## Progress

- **21 Nov: first batch built** on the concept and the canvas, placed right after "What we offer" (services) and after the service cards (hub):
  - Styling hub: **What goes where** (map: R8 photo, 6 brush circles, numbered legend with links)
  - Ghost: **How keyless cars get taken, and where Ghost stops it** (story: 3 cards with icons)
  - Car trackers: **What happens when your car is stolen** (steps)
  - Window tinting: **How dark can you go?** (law: Macan photo, 3 circles, legal figures, GOV.UK source)
  - Car wrapping: **A full wrap, step by step** (steps + Hypa fitting photo)
  - Car audio: **The upgrade ladder** (ladder: staircase on desktop)
- For Hypa (hidden from pages, on the review board): tracker recovery wording, wrap stages and timing.
- Next: Dani's review → the other 20 pages → explainer types into the design system as one component.

- **21 Nov: the other 20 built** (all 26 pages now have one). New types: **compare** (table; stacks with labels on phones) and **checks** (tick list + official source).
  - Security hub: every theft method has a fix (compare) · Upgrades hub: pick by what you want (compare) · Dash cams: how a dash cam settles a claim (steps) · Car alarms: factory vs Scorpion (compare) · Taxi cameras: what TfL asks for (checks, TfL source) · CarPlay: three things we need to know (story) · Remapping: what to know first (checks) · Reverse cameras: sensors or camera (compare) · Ambient: a starlight headliner, by hand (steps) · Exhausts: exhausts and the law (checks, GOV.UK) · PPF: PPF, ceramic or wrap (compare) · Air suspension: four parts, one button (story) · Coilovers: springs, coilovers or air (compare) · Chrome delete: wrap or paint (compare) · Bodykits: how a bodykit goes on (steps) · Wheel refurb: what a refurb involves (steps) · Interiors: carbon or Alcantara (compare) · Detailing: correction levels (ladder) · Number plates: what makes a plate legal (checks, GOV.UK) · Van signage: from logo to van (steps)
- Checks: no image repeats on any page (fixed 5 incl. 2 old ones: hero video vs Related/Recent work), no review notes on customer pages.
- **For Hypa (review board):** our taxi camera systems vs TfL's current approved list (May 2025 list names Kasava, SmartWitness, Exeros, Nauto, SAFEsystems); Scorpion alarm features; remap process, warranty and insurance wording; coilover/spring prices; whether trims are painted too; bodykit and refurb methods; detailing level contents and prices; van design/proof step.
