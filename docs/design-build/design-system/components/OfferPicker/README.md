# OfferPicker

"What we offer" on every service page: the options under that service as tabs, and a panel that says what it is, why choose it and who it's best for.

- Heading "What we offer" + one intro line (e.g. "Four set-ups, from one camera to full cover while you're parked."). Not "Pick your setup" (Dani, 21 Nov 2026).
- Panel: the option name as a huge outlined ghost word (decorative, `aria-hidden`), the "what it is" line as a lead, then two facts: **Why choose it** and **Best for**, then "Ask about this".
- Desktop: tabs stacked on the left (Big Shoulders, the selected one in `ink` with a red bar and arrow), panel on the right with the service photo faded behind. Phone: tabs as a horizontal pill row.
- Real ARIA tabs: `role="tablist"`, `tab`, `tabpanel`, arrow keys move between tabs.
- You provide: per option name, what, why, best for; the service photo.
