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

## Fixing the gaps: steps given to Dani (8 Nov 2026)
**1. DKIM (do first)**
1. Sign in to Microsoft Defender as the Microsoft 365 admin: https://security.microsoft.com/dkimv2
   (if GoDaddy manages the Microsoft 365 account and blocks this, GoDaddy support can switch DKIM on).
2. Click **hypedup.uk** → copy the two CNAME records it shows (selector1 and selector2). Use Microsoft's exact values; don't type them from memory.
3. GoDaddy → My Products → hypedup.uk → DNS → **Add New Record**, twice:
   - Type **CNAME**, Name `selector1._domainkey`, Value = Microsoft's selector1 value, TTL 1 hour
   - Type **CNAME**, Name `selector2._domainkey`, Value = Microsoft's selector2 value, TTL 1 hour
4. Wait 15–60 minutes, back in Defender switch **Sign messages for this domain with DKIM signatures** to **Enabled**.

**2. DMARC (after DKIM)**
GoDaddy DNS → Add New Record: Type **TXT**, Name `_dmarc`, Value
`v=DMARC1; p=none; rua=mailto:info@hypedup.uk; fo=1`, TTL 1 hour.
`p=none` = watch only, nothing gets blocked. Daily reports arrive at info@ (set an Outlook rule to file them).
Tighten to `p=quarantine` only after the website form's sender is added at build time and reports look clean.

**Rules:** add only; never edit or delete existing records. Claude checks both records by DNS lookup afterwards.

## DKIM values from Microsoft (8 Nov 2026)
| Type | Name | Value |
|---|---|---|
| CNAME | `selector1._domainkey` | `selector1-hypedup-uk._domainkey.NETORGFT11101442.k-v1.dkim.mail.microsoft` |
| CNAME | `selector2._domainkey` | `selector2-hypedup-uk._domainkey.NETORGFT11101442.k-v1.dkim.mail.microsoft` |
Status (8 Nov 2026): both CNAMEs live in GoDaddy DNS (checked). Microsoft's Enable switch first returned an error (usually key sync / propagation delay); **retry signing later**.

**DMARC live (checked 8 Nov 2026):** `v=DMARC1; p=none; rua=mailto:info@hypedup.uk; fo=1`
