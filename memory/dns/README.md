# Domain records (DNS) for hypedup.uk

_Backup exported by Dani from GoDaddy on 8 Nov 2026: `hypedup.uk-zone-2026-11-08.txt` (keep; it's what we copy from at launch)._

## What each record does
| Record | Value | What it's for | At launch |
|---|---|---|---|
| A `@` | "WebsiteBuilder Site" (live: 13.248.243.5, 76.223.105.230) | Points hypedup.uk to the GoDaddy website | **The one record that changes** (to the new host) |
| CNAME `www` | `@` | www.hypedup.uk follows the main address | Keep / point to new host |
| MX `@` | hypedup-uk.mail.protection.outlook.com (0) | Delivers email to Microsoft 365 | **Never touch** |
| TXT `@` | `v=spf1 include:secureserver.net -all` | Says who may send email as @hypedup.uk. GoDaddy's list already includes Microsoft 365 (`spf.protection.outlook.com`), checked 8 Nov | Add the form's email service here at build time, keep the rest |
| TXT `@` | `NETORGFT11101442.onmicrosoft.com` | Proves the domain to Microsoft 365 | Never touch |
| TXT `@` | `google-site-verification=dI5Ggo…` | **Search Console verified by DNS**, so it survives the website move | Keep |
| TXT `@` | `pinterest-site-verification=…` | Pinterest | Keep |
| CNAME `autodiscover`, `msoid`, `lyncdiscover`, `sip` + 2 SRV | Microsoft 365 / Outlook / Teams set-up | Never touch |
| CNAME `email` | email.secureserver.net | GoDaddy webmail shortcut | Keep |
| CNAME `_domainconnect` | GoDaddy | GoDaddy's auto-setup helper | Keep |
| NS | ns23/ns24.domaincontrol.com | GoDaddy runs the DNS | Stays at GoDaddy (plan) |

## Gaps found (email deliverability, not urgent)
- **No DKIM** for Microsoft 365 (no `selector1._domainkey` / `selector2._domainkey`). DKIM signs outgoing mail; Gmail/Yahoo increasingly expect it. Turn on in Microsoft 365 Defender → DKIM, then add the 2 CNAMEs it shows.
- **No DMARC** (`_dmarc` TXT). Start with a monitoring record: `v=DMARC1; p=none; rua=mailto:<a reporting inbox>`. Protects the domain from spoofing and helps deliverability.
- Both can be done now or at build time (with the form's email setup). Changes are additive; nothing existing changes.
