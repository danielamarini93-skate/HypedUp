# Header

Sticky site header: logo chip, the three menus (Security · Upgrades · Styling), Builds, the "Open today" status and ONE red "Contact us" pill.

- Never add a plain "Contact" text link next to the pill: one call to action only (Dani, 21 Nov 2026).
- Desktop (1000 px+): menus open a dropdown with the services of that group. `aria-current` on the group of the page you are on (red underline).
- Phone: logo + "Menu" button only; the full-screen sheet lists the three groups as expandable doors, Builds, the small links (Community, Motorbikes, Business & fleet, Blog, About, Shop), today's hours and Contact us / WhatsApp / Call at the bottom. The floating WhatsApp button (`.hu-fab`, see Button) sits bottom-right on every phone screen.
- 68 px tall, `surface-raised` with a `rule` bottom border. Logo: white wordmark on a `radius-md` chip, 32–38 px tall.
- You provide: the current group, the hours line, the links.
