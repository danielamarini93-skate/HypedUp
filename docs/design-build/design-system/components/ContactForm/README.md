# ContactForm

The main action of the site: pick what you need, tell us the car, optionally add more and photos, then send by WhatsApp or by email. Spec: `docs/design-thinking/contact-flow.md` in the website repo.

- Order on the Contact page: H1 + lead, the Google map (above the fold, Dani 21 Nov 2026), the form, then Find us details.
- Fields: need chips (multi-select), Your car (required), Anything else + Add photos (optional). Two send buttons: "Send on WhatsApp" (ghost) and "Send by email" (red), which reveals Name, Email, Phone (optional) and Send.
- States: **empty**, **filled**, **error** (red line under the field + a message that says how to fix it, e.g. "We need your email to reply, e.g. name@example.com"), **sending**, **sent** (Thanks panel, preview of what was sent, optional "How did you find us?" chips, "Back to the form").
- WhatsApp opens with the message written; nothing is sent until the customer presses send. Privacy link under the buttons.
- Labels always visible (not placeholder-only), 44 px chips, errors announced with `aria-describedby`.
