# Builds the full site concept (Direction D, IA v2) into OUT from content.py: every service page, the three group hubs,
# two homepage versions for the A/B test, audience hubs, Builds, Contact, About, Blog, Shop, plus a review board (index.html).
# Media and the personal-use font come from the scratchpad and are not committed. Run: python3 build.py
# Previous version (5 key pages): build-v3.py
import os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from content import GROUPS, MENU, S as SV, HUBS, TBC, DESCS
import html as _html
S = '/tmp/claude-0/-home-user/545d0e01-e697-5941-a49a-d293a211030b/scratchpad'
OUT = S + '/pages-out'
L = S + '/lucide/pkg/package/icons/'
def lu(n): return re.sub(r'<!--.*?-->', '', open(L + n + '.svg').read(), flags=re.S).strip().replace('class="lucide', 'aria-hidden="true" class="lucide', 1)
def br(n): return open(S + '/brands/' + n + '.svg').read().replace('<svg ', '<svg fill="currentColor" width="18" height="18" aria-hidden="true" ', 1)
def icons(s):
    s = re.sub(r'\{\{lu:([a-z-]+)\}\}', lambda m: lu(m.group(1)), s)
    return re.sub(r'\{\{br:([a-z]+)\}\}', lambda m: br(m.group(1)), s)
GNAME = {k: n for k, n, _ in GROUPS}
CHIP = dict((k, v.get('chip', 'other')) for k, v in SV.items()); CHIP['paint-protection-film'] = CHIP['window-tinting'] = 'ppf'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900&family=Barlow:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&family=Instrument+Serif:ital@1&display=swap">'
def h(slug): return slug + '.html'

def head(title, desc, name=''):
    desc = DESCS.get(name[:-5], desc)
    title, desc = _html.escape(_html.unescape(title)), _html.escape(_html.unescape(desc))
    return ('<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><meta name="description" content="%s">%s<link rel="stylesheet" href="site.css"></head><body>' % (title, desc, FONTS))

def header(cur):
    groups = ''.join('<div class="dd"><button type="button" aria-expanded="false" aria-controls="dd-%s"%s>%s{{lu:chevron-down}}</button><ul class="ddp" id="dd-%s" hidden>%s</ul></div>'
                     % (g, ' aria-current="page"' if g == cur else '', GNAME[g], g, ''.join('<li><a href="%s">%s</a></li>' % (h(s), SV[s]['short']) for s in MENU[g])) for g, _, _ in GROUPS)
    plain = ''.join('<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if n == cur else '', n) for n, u in [('Builds', 'builds.html'), ('Contact', 'contact.html')])
    doors = ''.join('<li><button type="button" aria-expanded="false" aria-controls="sd-%s">%s<span>{{lu:chevron-down}}</span></button><ul class="sub" id="sd-%s" hidden>%s</ul></li>'
                    % (g, GNAME[g], g, ''.join('<li><a href="%s">%s</a></li>' % (h(s), SV[s]['short']) for s in MENU[g])) for g, _, _ in GROUPS)
    return ('<header class="hd"><div class="wrap"><a class="chip" href="home-a.html"><img src="img/logo.png" alt="Hyped Up home"></a><nav aria-label="Main" class="mainnav">' + groups + plain + '</nav>'
            '<span class="mono status"><i></i>Open today<br>10:00–18:00</span><a class="pill sm" href="contact.html">Contact us</a>'
            '<button class="menu-btn" data-menu="open" aria-label="Open menu">Menu {{lu:menu}}</button></div></header>'
            '<div class="sheet" id="sheet" hidden><div class="top"><span class="chip"><img src="img/logo.png" alt="Hyped Up"></span><button class="menu-btn" data-menu="close" aria-label="Close menu">Close {{lu:x}}</button></div>'
            '<ul class="doors">' + doors + '<li><a href="builds.html">Builds</a></li></ul>'
            '<nav class="small" aria-label="More"><a href="motorbikes.html">Motorbikes</a><a href="business.html">Business &amp; fleet</a><a href="blog.html">Blog</a><a href="about.html">About</a><a href="shop.html">Shop</a></nav>'
            '<p class="mono hours"><i style="display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--ok);margin-right:.45rem"></i>Open today 10:00–18:00 · London SE16</p>'
            '<div class="bottom"><a class="pill" href="contact.html">Contact us</a><a class="pill ghost ico" href="#wa" aria-label="WhatsApp">{{br:whatsapp}}</a><a class="pill ghost ico" href="tel:+442033400632" aria-label="Call 020 3340 0632">{{lu:phone}}</a></div></div>'
            '<main id="main">')

def footer():
    def col(g, name, slugs):
        return ('<details class="fcol"><summary class="mono">%s{{lu:plus}}</summary><ul><li class="hub"><a href="%s">All %s services →</a></li>%s</ul></details>'
                % (name, h(g), name, ''.join('<li><a href="%s">%s</a></li>' % (h(s), SV[s]['short']) for s in slugs)))
    more = '<details class="fcol"><summary class="mono">More{{lu:plus}}</summary><ul>%s</ul></details>' % ''.join(
        '<li><a href="%s">%s</a></li>' % (u, n) for n, u in [('Motorbikes', 'motorbikes.html'), ('Business &amp; fleet', 'business.html'), ('Builds', 'builds.html'), ('Blog', 'blog.html'), ('About', 'about.html'), ('Shop', 'shop.html')])
    return ('</main><footer class="ft"><div class="wrap"><div class="ft-grid"><div class="findus"><span class="find">Find us</span>'
            '<p><b>Unit 22, Enterprise Industrial Estate, Bolina Road, London SE16 3LF</b></p><p class="mono">Mon–Fri 10–18 · Sat 9–16 · Sun closed</p>'
            '<div class="social"><a class="ci" href="tel:+442033400632" aria-label="Call 020 3340 0632">{{lu:phone}}</a><a class="ci" href="#wa" aria-label="WhatsApp 07713 735646">{{br:whatsapp}}</a><a class="ci" href="mailto:info@hypedup.uk" aria-label="Email info@hypedup.uk">{{lu:mail}}</a>'
            '<a href="#" aria-label="Instagram">{{br:instagram}}</a><a href="#" aria-label="TikTok">{{br:tiktok}}</a><a href="#" aria-label="Facebook">{{br:facebook}}</a></div>'
            '<p class="ftcontact">020 3340 0632 · WhatsApp 07713 735646 · info@hypedup.uk</p></div>' + ''.join(col(*g) for g in GROUPS) + more + '</div>'
            '<div class="legal mono"><span>© 2026 Hyped Up Ltd · Company no. 14086991</span><span>Privacy · Cookies · Terms · Cookie settings</span></div>'
            '<div class="wm"><svg class="wmsvg" aria-hidden="true" preserveAspectRatio="xMinYMax meet"><defs><linearGradient id="wmg" x1="0" x2="1"><stop offset="0" stop-color="#ff4033"/><stop offset=".6" stop-color="#ef1220"/><stop offset="1" stop-color="#de0613"/></linearGradient></defs>'
            '<text x="0" y="0" font-size="200" fill="none" stroke="url(#wmg)">HYPED UP</text></svg><span class="mono">Est. 2022</span></div></div></footer>'
            '<a class="fab" href="#wa" aria-label="WhatsApp Hyped Up">{{br:whatsapp}}</a><script src="site.js"></script></body></html>')

PAGES = []  # (file, label, section) for the review board
def page(name, title, desc, cur, body, label, section):
    PAGES.append((name, label, section))
    open(os.path.join(OUT, name), 'w').write(icons(head(title, desc, name) + header(cur) + body + footer()))

def media(img, alt, need='', cls='media vig', lazy=True):
    if img:
        return '<div class="%s"><img src="img/%s" alt="%s"%s></div>' % (cls, img, alt, ' loading="lazy"' if lazy else '')
    return '<div class="%s need"><span class="mono">Photo needed: %s</span></div>' % (cls.replace(' vig', ''), need)
def band(title, line, chip=''):
    return ('<section class="band"><div class="wrap"><div><h2>%s</h2><p class="lead" style="margin-top:14px">%s</p></div><a class="pill" href="contact.html%s">Contact us</a></div></section>'
            % (title, line, ('?service=' + chip) if chip else ''))
def scard(s):
    v = SV[s]
    return ('<a class="card" href="%s">%s<div class="row"><h3>%s</h3><span class="from g">%s</span></div><p>%s</p></a>'
            % (h(s), media(v['img'], v['alt'], v.get('need', '')), v['name'], v['price'], v['line']))
def faq(items, first_open=True):
    return '<div class="faq">' + ''.join('<details%s><summary>%s{{lu:plus}}</summary><p>%s</p></details>' % (' open' if i == 0 and first_open else '', q, a) for i, (q, a) in enumerate(items)) + '</div>'
def builds_strip(items):
    return '<div class="cards">' + ''.join('<a class="card" href="builds.html">%s<h3>%s</h3><p>%s</p></a>' % (media(i, a), n, w) for i, n, w, a in items) + '</div>'

BUILDS = [
    ('audi-r8-carplay.jpg', 'Audi R8', 'New CarPlay screen', 'upgrades', 'Audi R8 dashboard with a new CarPlay screen'),
    ('abarth-pink-wrap.jpg', 'Abarth 595', 'Pink wrap, gold wheels', 'styling', 'Pink Abarth 595 with gold wheels'),
    ('mini-jcw-low.jpg', 'Mini JCW', 'Air suspension', 'styling', 'Red Mini JCW sitting low on air suspension'),
    ('tracker.jpg', 'Mercedes', 'MetaTrak tracker', 'security', 'MetaTrak tracker card in front of a Mercedes'),
    ('abarth-ambient.jpg', 'Abarth 595', 'Ambient lighting', 'upgrades', 'Abarth interior with purple ambient lighting'),
    ('audi-r8-unit.jpg', 'Audi R8', 'Work <span class="tbc">TBC</span>', 'upgrades', 'Black Audi R8 outside the Hyped Up unit'),
    ('porsche-macan-unit.jpg', 'Porsche Macan', 'Work <span class="tbc">TBC</span>', 'styling', 'Black Porsche Macan outside the Hyped Up unit'),
    ('boot-build.jpg', 'Boot build', 'Subwoofer enclosure', 'upgrades', 'Custom boot with a red and black subwoofer enclosure'),
    ('dashcam.jpg', 'BMW', 'Front and rear dash cam', 'security', 'Dash cam fitted behind a BMW mirror'),
    ('bentley-unit.jpg', 'Bentley Flying Spur', 'Work <span class="tbc">TBC</span>', 'styling', 'Bentley outside the Hyped Up unit'),
    ('mercedes-screen.jpg', 'Mercedes', 'Screen upgrade', 'upgrades', 'Mercedes dashboard with a large new screen'),
    ('wrap.jpg', 'London taxi', 'Purple colour change', 'styling', 'London taxi wrapped in purple inside the workshop'),
    ('carplay.jpg', 'Mini', 'Wireless CarPlay screen', 'upgrades', 'Mini dashboard with a new CarPlay screen'),
    ('alfa-keys-wheel.jpg', 'Alfa Romeo', 'Security <span class="tbc">TBC</span>', 'security', 'Alfa Romeo steering wheel and keys'),
    ('volvo-xc90-satin.jpg', 'Volvo XC90', 'Satin finish, gold details <span class="tbc">TBC</span>', 'styling', 'Satin grey Volvo XC90 with gold wheel details'),
    ('fiat-500-red.jpg', 'Fiat 500', 'Work <span class="tbc">TBC</span>', 'upgrades', 'Red Fiat 500 inside the workshop'),
    ('ford-transit-yellow.jpg', 'Ford Transit Custom', 'Work <span class="tbc">TBC</span>', 'styling', 'Yellow Ford Transit Custom van in the workshop'),
    ('civic.jpg', 'Honda Civic Type R', 'Work <span class="tbc">TBC</span>', 'upgrades', 'Yellow Honda Civic Type R in the workshop'),
]
SVC_BUILDS = {'car-wrapping': [0 + 1, 11, 14], 'air-suspension': [2], 'car-trackers': [3], 'ambient-lighting': [4], 'carplay': [0, 12, 10], 'car-audio': [7],
              'dash-cams': [8], 'ghost-immobiliser': [13, 3], 'taxi-cameras': [11], 'van-signage': [16], 'wheel-refurb': [14]}

def service_page(slug):
    v = SV[slug]; g = v['group']; chip = CHIP[slug]
    opts = ''.join('<div class="opt"><h3>%s</h3>%s</div>' % (t, ('<p>%s</p>' % d) if d else '') for t, d in v['options'])
    steps = ''.join('<li><span class="mono">%s</span><h3>%s</h3><p>%s</p></li>' % (('Step one', 'Step two', 'Step three')[i], t, d) for i, (t, d) in enumerate(v['steps']))
    proof = [i for i in SVC_BUILDS.get(slug, []) if BUILDS[i][0] != v['img']]
    proof_html = (builds_strip([(BUILDS[i][0], BUILDS[i][1], BUILDS[i][2], BUILDS[i][4]) for i in proof]) if proof else
                  '<div class="need-row"><span class="mono">Builds for this service: photos needed (Drive upload)</span></div>')
    makes = ('<div style="display:grid;gap:12px"><span class="mono">%s for your car</span><div class="chips">%s</div></div>' % (v['name'], ''.join('<a href="%s">%s</a>' % (u, m) for m, u in v['makes']))) if v.get('makes') else ''
    rel = ''.join(scard(s) for s in v['related'])
    blog = ('<div style="display:grid;gap:12px"><span class="mono">Guides</span><div class="chips">%s</div></div>' % ''.join('<a href="%s">%s</a>' % (u, t) for t, u in v['blog'])) if v.get('blog') else ''
    good = ('<div class="good"><span class="mono">Good to know</span><p>%s</p></div>' % v['good']) if v.get('good') else ''
    body = '''
<section class="hero flip"><div class="wrap">
  <nav class="crumbs mono" aria-label="Breadcrumb"><a href="home-a.html">Home</a><span>/</span><a href="%(gh)s">%(gn)s</a><span>/</span><span aria-current="page">%(name)s</span></nav>
  <div class="grid">
    <div class="copy">
      <h1>%(name)s</h1>
      <p class="lead">%(lead)s</p>
      <div class="price"><b class="g">%(price)s</b><span class="mono">%(note)s</span></div>
      <div class="act"><a class="pill" href="contact.html?service=%(chip)s">Contact us</a></div>
    </div>
    <figure>%(media)s</figure>
  </div>
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Options</h2></div><div class="opts">%(opts)s</div></div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>How it works</h2></div><ol class="steps">%(steps)s</ol></div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Recent work</h2><a class="link" href="builds.html">All builds {{lu:arrow-right}}</a></div>%(proof)s</div></section>
<section class="sec"><div class="wrap"><div class="narrow"><div class="sec-head" style="margin-bottom:0"><h2>Questions</h2></div>%(good)s%(faq)s%(makes)s%(blog)s</div></div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Related</h2><a class="link" href="%(gh)s">All %(gn)s services {{lu:arrow-right}}</a></div><div class="cards">%(rel)s</div></div></section>
''' % dict(gh=h(g), gn=GNAME[g], name=v['name'], lead=v['lead'], price=v['price'], note=v['price_note'], chip=chip, media=media(v['img'], v['alt'], v.get('need', ''), lazy=False),
           opts=opts, steps=steps, proof=proof_html, good=good, faq=faq(v['faq']) if v['faq'] else '', makes=makes, blog=blog, rel=rel)
    page(h(slug), v['title'], v['desc'], g, body + band('Want a price for your car?', 'Send me the make and model. I\'ll come back with options and a straight price.', chip), v['name'], GNAME[g])

def hub_page(g, name, slugs):
    d = HUBS[g]
    layers = ('<section class="sec"><div class="wrap"><div class="sec-head"><h2>Layer it</h2><p>One system does one job. Thieves get past one layer; they rarely get past three.</p></div><ol class="steps steps4">%s</ol></div></section>'
              % ''.join('<li><span class="mono">%s</span><h3>%s</h3></li>' % x for x in d['layers'])) if d.get('layers') else ''
    rows = ''.join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td><span class="from g">%s</span></td></tr>' % r for r in d['compare'])
    body = '''
<section class="hero flip"><div class="wrap"><div class="grid">
  <div class="copy"><h1>%(h1)s</h1><p class="lead">%(lead)s</p><div class="act"><a class="pill" href="contact.html">Contact us</a></div></div>
  <figure>%(media)s</figure>
</div></div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>All %(name)s services</h2><p>%(n)d services, the same list as the footer.</p></div><div class="cards hubcards">%(cards)s</div></div></section>
%(layers)s
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Which one do I need?</h2></div>
  <div class="scrollx"><table class="compare"><thead><tr><th>Service</th><th>What it does</th><th>Best for</th><th>Price</th></tr></thead><tbody>%(rows)s</tbody></table></div></div></section>
<section class="sec"><div class="wrap"><div class="narrow"><div class="vsbox"><span class="mono">Explained</span><h2>%(et)s</h2><p class="lead">%(eb)s</p></div>%(faq)s</div></div></section>
''' % dict(h1=d['h1'], lead=d['lead'], media=media(d['img'], d['alt'], lazy=False), name=name, n=len(slugs), cards=''.join(scard(s) for s in slugs), layers=layers, rows=rows,
           et=d['explainer'][0], eb=d['explainer'][1], faq=faq(d['faq'], False))
    page(h(g), d['title'], d['desc'], g, body + band('Not sure what your car needs?', 'Send me the make and model. I\'ll tell you what\'s worth doing and what it costs.'), name + ' (hub)', 'Hubs')

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT + '/img'); os.makedirs(OUT + '/fonts')
    for f in os.listdir(S + '/pimg'): shutil.copy(S + '/pimg/' + f, OUT + '/img/' + f)
    shutil.copy(os.path.join(HERE, '..', 'assets', 'paint', '318600.svg'), OUT + '/img/circle.svg')
    shutil.copy(S + '/fz/graffiti_city/Graffiti City.otf', OUT + '/fonts/graffiti-city.otf')
    for f in ['site.css', 'site.js']: shutil.copy(os.path.join(HERE, f), OUT + '/' + f)

    strip = ''.join('<a href="%s"><b>%s</b><span class="from g">%s</span><p>%s</p></a>' % (h(g), n, p, t) for (g, n, _), p, t in zip(GROUPS, ['from £125', 'from £125', 'from £30'],
            ['Ghost, trackers, alarms, dash cams', 'CarPlay, audio, remaps, lighting', 'Wraps, PPF, tint, air, wheels, plates']))
    recent = builds_strip([(BUILDS[i][0], BUILDS[i][1], BUILDS[i][2], BUILDS[i][4]) for i in (2, 1, 0)])
    how = '''<ol class="steps"><li><span class="mono">Step one</span><h3>Tell me what you want</h3><p>Pick the job and write the car on the contact page, or WhatsApp me. Photos help.</p></li>
<li><span class="mono">Step two</span><h3>Get a straight price</h3><p>I come back with options, a price and how long it takes. You pick a date.</p></li>
<li><span class="mono">Step three</span><h3>Drop it off, drive it home</h3><p>Small jobs are often done while you wait; a full wrap takes at least a week. <span class="tbc">(TBC: Hypa)</span></p></li></ol>'''
    about = '''<div class="split"><figure>%s</figure><div style="display:grid;gap:18px;justify-items:start"><span class="mono">The workshop</span><h2>Built by Hypa</h2>
<p class="lead">I started Hyped Up in 2022 to do this work properly: the right parts, fitted neatly, and a straight price before anything starts. My own Mini has run on air every day for over four years. <span class="tbc">(Copy: Hypa to approve)</span></p>
<a class="link" href="about.html">About Hyped Up {{lu:arrow-right}}</a></div></div>''' % media('workshop.jpg', "Hyped Up's red Mini in front of the graffiti mural inside the workshop")
    review = '''<div style="display:grid;gap:14px;max-width:820px"><span class="mono">Google reviews · 5.0 from 47 reviews <span class="tbc">(Maps, 9 Nov)</span></span>
<p style="font:900 clamp(1.8rem,4vw,2.6rem)/1.05 var(--f-display);text-transform:uppercase" class="tbc">[A real review, picked by Hypa]</p><span class="mono">Customer first name · Service</span></div>'''

    # ---------- HOME A: brand-led (Direction D hero) ----------
    page('home-a.html', 'Car Security, Upgrades & Styling in London | Hyped Up', 'Ghost immobilisers, trackers, CarPlay, car audio, remaps, wraps, PPF, tint and air suspension, fitted properly in Bermondsey, South London. Clear "from" prices.', '', '''
<section class="hero home"><div class="wrap">
  <div class="mono" style="display:flex;justify-content:space-between;margin-bottom:18px"><span>Bermondsey, South London</span><span>Est. 2022</span></div>
  <div class="grid">
    <div class="copy">
      <h1>Protect it.<br>Upgrade it.<span class="wet" id="morph" role="text" aria-label="Style it.">Style it.</span></h1>
      <p class="lead">South London's one-stop workshop for car and bike security, upgrades and styling. Fitted properly, priced clearly.</p>
      <div class="act"><a class="pill" href="contact.html">Contact us</a><span class="find">Find us</span><span class="mono">Unit 22, Bolina Rd<br>SE16 3LF</span></div>
    </div>
    <figure><div class="media vig"><video src="img/hero.mp4" poster="img/poster.jpg" autoplay muted loop playsinline aria-label="Short silent reel of work inside the Hyped Up workshop"></video></div><figcaption class="mono" style="text-align:right">@hypedup.ltd</figcaption></figure>
  </div>
  <div class="strip" style="margin-top:32px">''' + strip + '''</div>
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Recent builds</h2><a class="link" href="builds.html">See all builds {{lu:arrow-right}}</a></div>''' + recent + '''</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>How a job works</h2></div>''' + how + '''</div></section>
<section class="sec"><div class="wrap">''' + about + '''</div></section>
<section class="sec"><div class="wrap">''' + review + '''</div></section>
''' + band('Got a car in mind?', 'Tell me the car and the idea. I\'ll come back with options and a price.'), 'Home A · brand-led', 'Homepage (A/B test)')

    # ---------- HOME B: task-led (service finder first) ----------
    tabs = ''.join('<button type="button" role="tab" aria-selected="%s" data-ftab="%s">%s</button>' % ('true' if i == 0 else 'false', g, n) for i, (g, n, _) in enumerate(GROUPS))
    panels = ''.join('<div class="fpanel" data-fpanel="%s"%s>%s</div>' % (g, '' if i == 0 else ' hidden', ''.join('<a href="%s"><b>%s</b><span class="from g">%s</span></a>' % (h(s), SV[s]['short'], SV[s]['price']) for s in sl))
                     for i, (g, n, sl) in enumerate(GROUPS))
    page('home-b.html', 'Car Security, Upgrades & Styling in London | Hyped Up', 'Ghost immobilisers, trackers, CarPlay, car audio, remaps, wraps, PPF, tint and air suspension, fitted properly in Bermondsey, South London. Clear "from" prices.', '', '''
<section class="hero"><div class="wrap" style="display:grid;gap:26px">
  <div class="copy" style="max-width:900px">
    <span class="mono">Bermondsey, South London · 5.0 on Google <span class="tbc">(47 reviews, Maps)</span></span>
    <h1>Car and bike security, upgrades and styling</h1>
    <p class="lead">Fitted properly, priced clearly, by Hypa and the team at Unit 22. Pick what you need.</p>
  </div>
  <div class="finder"><div class="ftabs" role="tablist" aria-label="Service groups">''' + tabs + '</div>' + panels + '''</div>
  <div class="act"><a class="pill" href="contact.html">Contact us</a><a class="link" href="builds.html">See the work {{lu:arrow-right}}</a></div>
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Recent builds</h2><a class="link" href="builds.html">See all builds {{lu:arrow-right}}</a></div>''' + recent + '''</div></section>
<section class="sec"><div class="wrap split"><figure><div class="media vig"><video src="img/hero.mp4" poster="img/poster.jpg" muted loop playsinline controls aria-label="Short silent reel of work inside the Hyped Up workshop"></video></div></figure>
<div style="display:grid;gap:18px;justify-items:start"><span class="mono">Inside the workshop</span><h2>Protect it. Upgrade it. <span class="g">Style it.</span></h2><p class="lead">One workshop for the lot, from a Ghost immobiliser to a full colour change.</p></div></div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>How a job works</h2></div>''' + how + '''</div></section>
<section class="sec"><div class="wrap">''' + review + '''</div></section>
''' + band('Got a car in mind?', 'Tell me the car and the idea. I\'ll come back with options and a price.'), 'Home B · task-led', 'Homepage (A/B test)')

    for g, n, sl in GROUPS: hub_page(g, n, sl)
    for g, n, sl in GROUPS:
        for s in sl: service_page(s)

    # ---------- AUDIENCE HUBS ----------
    def audience(file, title, desc, h1, lead, img, alt, items, label):
        rows = ''.join('<a class="card" href="%s">%s<div class="row"><h3>%s</h3><span class="from g">%s</span></div><p>%s</p></a>' % (u, media(i, '', nd), t, p, d) for t, d, p, u, i, nd in items)
        body = ('<section class="hero flip"><div class="wrap"><div class="grid"><div class="copy"><h1>%s</h1><p class="lead">%s</p><div class="act"><a class="pill" href="contact.html">Contact us</a></div></div><figure>%s</figure></div></div></section>'
                '<section class="sec"><div class="wrap"><div class="sec-head"><h2>What I do for you</h2></div><div class="cards">%s</div></div></section>') % (h1, lead, media(img, alt, 'a bike in the workshop', lazy=False), rows)
        page(file, title, desc, '', body + band('Tell me what you ride or drive', 'I\'ll tell you what\'s worth fitting and what it costs.'), label, 'Audience hubs')
    audience('motorbikes.html', 'Motorbike Security, Wraps & Remaps in London | Hyped Up', 'Motorbike security, trackers, wraps and remaps in Bermondsey, South London: Ghost for bikes, Datatool S5 trackers, bike alarms and wraps from £900.',
             'Motorbikes', 'Bikes get lifted into vans in a minute, so they need tracking as well as an immobiliser. I also wrap and remap them.', None, '',
             [('Ghost for motorbikes', 'PIN on the bike\'s own buttons.', 'from £400', 'ghost-immobiliser.html', None, 'a bike Ghost fit'), ('Datatool S5 tracker', 'Hidden under the seat, monitored 24/7.', 'from £395', 'car-trackers.html', None, 'a bike tracker'),
              ('Bike alarms', 'Siren with motion and shock sensors.', 'on enquiry', 'car-alarms.html', None, 'a bike alarm'), ('Motorbike wraps', 'Mopeds, nakeds and super sports.', 'from £900', 'car-wrapping.html', None, 'a bike wrap'),
              ('Bike remaps', 'More response, done safely.', 'on enquiry', 'remapping.html', None, 'a bike remap')], 'Motorbikes')
    audience('business.html', 'Fleet Tracking, Taxi Cameras & Van Signage London | Hyped Up', 'For London businesses, taxis and fleets: trackers, TfL-approved taxi cameras, van reverse cameras and sensors, and van signage, fitted in Bermondsey.',
             'Business &amp; fleet', 'Trackers, cameras and signage for taxis, vans and company cars, fitted around your working day.', 'ford-transit-yellow.jpg', 'Yellow Ford Transit Custom van in the workshop',
             [('Fleet trackers', 'Know where every vehicle is.', 'from £395', 'car-trackers.html', 'tracker.jpg', ''), ('TfL taxi cameras', 'Approved systems for cabs and PHVs.', 'from £395', 'taxi-cameras.html', 'wrap.jpg', ''),
              ('Van cameras and sensors', 'Reverse cameras and parking sensors.', 'from £125', 'reverse-cameras.html', None, 'a van camera'), ('Van signage and livery', 'Your logo on the road.', 'on enquiry', 'van-signage.html', 'ford-transit-yellow.jpg', ''),
              ('Dash cams', 'Front, rear and 3-channel for drivers.', 'from £125', 'dash-cams.html', 'dashcam.jpg', '')], 'Business & fleet')

    # ---------- BUILDS ----------
    figs = ''.join('<figure data-tags="%s"><div class="media vig"><img src="img/%s" alt="%s" loading="lazy"></div><figcaption><b>%s</b><span class="mono">%s</span></figcaption></figure>' % (t, i, a, n, w) for i, n, w, t, a in BUILDS)
    page('builds.html', 'Builds: Wraps, Air Suspension, CarPlay & More | Hyped Up', 'Real cars and bikes from the Hyped Up workshop in Bermondsey: wraps, air suspension, CarPlay, audio, lighting and security installs. See the work, then contact us.', 'Builds', '''
<section class="hero"><div class="wrap" style="display:grid;gap:22px">
  <h1>Builds</h1><p class="lead">Real work from the workshop: security, upgrades and styling.</p>
  <div class="feature" style="margin-top:12px"><figure>''' + media('workshop.jpg', "Hyped Up's red Mini JCW in front of the workshop mural", lazy=False) + '''</figure>
    <div style="display:grid;gap:12px;justify-items:start"><span class="mono">Our own car</span><h2>Mini JCW</h2><p class="lead">Air Lift 3P, wheels and styling, daily driven for over four years. <span class="tbc">(Spec TBC: Hypa)</span></p></div></div>
</div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
  <div class="chips" role="group" aria-label="Filter builds" style="margin-bottom:28px"><button type="button" data-filter="all" aria-pressed="true">All</button><button type="button" data-filter="security" aria-pressed="false">Security</button><button type="button" data-filter="upgrades" aria-pressed="false">Upgrades</button><button type="button" data-filter="styling" aria-pressed="false">Styling</button></div>
  <div class="gal">''' + figs + '''</div>
</div></section>''' + band('Want yours on this wall?', 'Tell me the car and the idea. I\'ll come back with options and a price.'), 'Builds', 'Brand & support')

    # ---------- CONTACT ----------
    needs = [('security', 'Security'), ('screens', 'Screens &amp; audio'), ('remap', 'Remap &amp; tuning'), ('wrap', 'Wrap'), ('ppf', 'PPF or tint'), ('air', 'Air &amp; coilovers'), ('plates', 'Plates'), ('other', 'Other')]
    ticks = ''.join('<label><input type="checkbox" name="need" value="%s" data-label="%s"><span>{{lu:check}}%s</span></label>' % (v, l.replace('&amp;', '&'), l) for v, l in needs)
    srcs = ['Google', 'Google Maps', 'Instagram', 'TikTok', 'A friend', 'Been before']
    MAPQ = 'Hyped%20Up%2C%20Unit%2022%2C%20Enterprise%20Industrial%20Estate%2C%20Bolina%20Road%2C%20London%20SE16%203LF'
    page('contact.html', 'Contact Hyped Up: Bermondsey Workshop, London SE16', 'Contact Hyped Up in Bermondsey, South London. Pick the job, tell us the car, add photos if you like, and send it by WhatsApp or email. Open Monday to Saturday.', 'Contact', '''
<div class="wrap contact">
  <div style="display:grid;gap:24px;align-content:start">
    <div style="display:grid;gap:12px"><h1>Contact us</h1><p class="lead">Tell me what you're after. I'll come back with options and a straight price.</p></div>
    <form class="form" id="quote" novalidate>
      <fieldset class="fs"><legend>What do you need?</legend><div class="tick">''' + ticks + '''</div></fieldset>
      <div class="field"><label for="vehicle">Your car</label><input id="vehicle" name="vehicle" placeholder="e.g. BMW 1 Series 2019, reg if you have it" autocomplete="off" required></div>
      <div class="field"><label for="more">Anything else? <span>(optional)</span></label><textarea id="more" name="more" rows="2" placeholder="Ideas, budget, timing"></textarea>
        <label class="addph">{{lu:camera}}<span id="ph-label">Add photos</span><input type="file" accept="image/*" multiple id="photos"></label></div>
      <div class="send"><button class="pill ghost" type="submit" value="whatsapp">{{br:whatsapp}}Send on WhatsApp</button><button class="pill" type="button" id="by-email" aria-expanded="false" aria-controls="emailbox">{{lu:mail}}Send by email</button></div>
      <div class="emailbox" id="emailbox" hidden>
        <div class="row2"><div class="field"><label for="name">Name</label><input id="name" name="name" autocomplete="name" required aria-describedby="name-err"><p class="err" id="name-err" hidden>Add your name so I know who to reply to.</p></div><div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required aria-describedby="email-err"><p class="err" id="email-err" hidden>I need your email to reply, e.g. name@example.com</p></div></div>
        <div class="field"><label for="phone">Phone <span>(optional)</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
        <button class="pill" type="submit" value="email">Send</button>
      </div>
      <p class="note">WhatsApp opens with your message written; nothing is sent until you press send. <a href="#" style="text-decoration:underline">Privacy</a></p>
    </form>
    <div class="done" id="sent" tabindex="-1" hidden><h3>Thanks</h3><p id="sent-msg"></p><div class="preview" id="sent-preview" hidden></div>
      <div style="display:grid;gap:10px;margin-top:8px"><span class="mono">How did you find us? <span style="text-transform:none;letter-spacing:0">(optional, one tap)</span></span><div class="chips" data-src>''' + ''.join('<button type="button" aria-pressed="false">%s</button>' % x for x in srcs) + '''</div></div>
      <button class="link" id="sent-back" type="button" style="background:none;border:0;color:inherit;padding:0;cursor:pointer;justify-self:start;margin-top:6px">Back to the form {{lu:arrow-right}}</button></div>
  </div>
  <aside class="aside">
    <div><span class="find">Find us</span></div>
    <p><b>Unit 22, Enterprise Industrial Estate,<br>Bolina Road, London SE16 3LF</b></p>
    <div class="map"><iframe src="https://maps.google.com/maps?q=''' + MAPQ + '''&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map showing Hyped Up on Bolina Road, London SE16 3LF"></iframe></div>
    <a class="pill sm" style="justify-self:start" href="https://maps.google.com/?cid=1418041190124790308" target="_blank" rel="noopener">{{lu:map-pin}}Get directions</a>
    <table class="compare" style="max-width:360px"><tbody><tr><td>Mon–Fri</td><td>10:00–18:00</td></tr><tr><td>Saturday</td><td>09:00–16:00</td></tr><tr><td>Sunday</td><td>Closed</td></tr></tbody></table>
    <p>Call <a href="tel:+442033400632"><b>020 3340 0632</b></a><br>WhatsApp <a href="#wa"><b>07713 735646</b></a><br>Email <a href="mailto:info@hypedup.uk"><b>info@hypedup.uk</b></a></p>
    <p class="note">Customers come from across South and East London: Bermondsey, Rotherhithe, Peckham, Lewisham, Greenwich, Croydon, Bromley and beyond. <span class="tbc">(Areas TBC: Hypa)</span></p>
  </aside>
</div>
''', 'Contact', 'Brand & support')

    # ---------- ABOUT ----------
    page('about.html', 'About Hyped Up: Hypa and the Bermondsey Workshop', 'Hyped Up is Hypa\'s vehicle security, upgrades and styling workshop at Unit 22, Bolina Road, Bermondsey: real parts, fitted properly, priced clearly since 2022.', '', '''
<section class="hero flip"><div class="wrap"><div class="grid">
  <div class="copy"><h1>About Hyped Up</h1><p class="lead">I'm Hypa. I started Hyped Up in 2022 to do car and bike work properly: the right parts, fitted neatly, and a straight price before anything starts.</p></div>
  <figure>''' + media('workshop.jpg', "Hyped Up's red Mini in front of the workshop mural", lazy=False) + '''</figure>
</div></div></section>
<section class="sec"><div class="wrap split"><div style="display:grid;gap:16px"><h2>Why I do this</h2>
<p class="lead">I got into air suspension after seeing a bagged GTR at Silverstone. My red F56 Mini has run on Air Lift 3P every day for over four years, and the BMW 1 Series show build is on its third boot rebuild. Before that there was the R53 Mini, "Lil Punisher".</p>
<p class="lead">That's the standard I hold customer cars to. <span class="tbc">(20+ years and McLaren motorsport background: Hypa to confirm before use)</span></p></div>
<figure>''' + media('mini-jcw-low.jpg', 'Hypa\'s red Mini JCW sitting low on Air Lift') + '''</figure></div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>How I work</h2></div><div class="opts">
<div class="opt"><h3>Fitted properly</h3><p>Wiring hidden, trims back as they were, everything tested before you leave.</p></div>
<div class="opt"><h3>Priced clearly</h3><p>A "from" price on every page, and your exact price before I start.</p></div>
<div class="opt"><h3>Honest advice</h3><p>If something isn't worth it on your car, or isn't road legal, I'll say so.</p></div></div></div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Brands I fit</h2><p class="tbc">Partner and dealer wording TBC: Hypa</p></div>
<div class="chips">''' + ''.join('<span class="brandchip">%s</span>' % b for b in ['Ghost', 'MetaTrak', 'Scorpion', 'Air Lift', 'Prazis', 'Xtrons', 'Autostyle', 'Pioneer', 'Kenwood', 'Rockford Fosgate', 'FineVu', 'Thinkware']) + '''</div></div></section>
''' + band('Come and see the workshop', 'Unit 22, Bolina Road, SE16. Open Monday to Saturday.'), 'About', 'Brand & support')

    # ---------- BLOG ----------
    posts = [('Security', 'Ghost immobiliser South London: cost, fitting and is it worth it?', 'ghost-immobiliser'), ('Security', 'Why every London car owner needs security right now', 'car-trackers'),
             ('Security', 'Best dash cam 2026: front and rear, GPS and why you need one', 'dash-cams'), ('Security', 'Number plate cloning is surging: how to protect yourself', 'number-plates'),
             ('Upgrades', 'Apple CarPlay installation in South London', 'carplay'), ('Upgrades', 'Car audio upgrade: subwoofers, amps and lighting', 'car-audio'),
             ('Upgrades', 'ECU remapping: more power, done properly', 'remapping'), ('Upgrades', 'Car tuning in London: how to pick a safe tuner', 'remapping'),
             ('Styling', 'How much does a car wrap cost in the UK? Real prices', 'car-wrapping'), ('Styling', 'Vehicle wrapping, PPF, tints, dechroming and signage', 'paint-protection-film'),
             ('Styling', 'Why ceramic coating became my secret weapon', 'detailing'), ('Styling', 'Air suspension and bodykit fitting: perfect your stance', 'air-suspension'),
             ('Styling', 'The low life chose me: why air suspension changed everything', 'air-suspension'), ('Styling', 'Your custom number plate in 10 minutes', 'number-plates'),
             ('Law & guides', 'The legal reality of car mods in the UK: what the DVLA actually cares about', 'performance-parts')]
    cats = ['All', 'Security', 'Upgrades', 'Styling', 'Law & guides']
    lis = ''.join('<li data-cat="%s"><a href="#"><span class="mono">%s</span><b>%s</b></a><a class="link" href="%s">%s {{lu:arrow-right}}</a></li>' % (c, c, t, h(s), SV[s]['short']) for c, t, s in posts)
    page('blog.html', 'Blog: Car Security, Upgrades & Styling Guides | Hyped Up', 'Straight answers from Hypa\'s Bermondsey workshop: Ghost immobilisers, trackers, dash cams, CarPlay, remaps, wraps, air suspension and the law on car mods.', '', '''
<section class="hero"><div class="wrap" style="display:grid;gap:20px"><h1>Blog</h1><p class="lead">Straight answers from the workshop. Every guide links to the service it's about.</p>
<div class="chips" role="group" aria-label="Filter posts">''' + ''.join('<button type="button" data-blogcat="%s" aria-pressed="%s">%s</button>' % (c, 'true' if c == 'All' else 'false', c.replace('&', '&amp;')) for c in cats) + '''</div></div></section>
<section class="sec" style="padding-top:24px"><div class="wrap"><ul class="postlist">''' + lis + '''</ul></div></section>''', 'Blog', 'Brand & support')

    # ---------- SHOP ----------
    prods = [('Graffiti T-shirt', '£20'), ('Hyped Up T-shirt', '£20'), ('Hyped Up jumper', '£40'), ('The keyring', '£10')]
    page('shop.html', 'Hyped Up Apparel: Tees, Jumpers & Keyrings', 'Hyped Up apparel from the Bermondsey workshop: graffiti tees, Hyped Up jumpers and keyrings. Order on WhatsApp and collect at Unit 22 or ask about delivery.', '', '''
<section class="hero"><div class="wrap" style="display:grid;gap:20px"><h1>Shop</h1><p class="lead">Workshop gear. Order on WhatsApp, collect at Unit 22. <span class="tbc">(Delivery: Hypa)</span></p></div></section>
<section class="sec" style="padding-top:24px"><div class="wrap"><div class="cards">''' + ''.join('<div class="card">%s<div class="row"><h3>%s</h3><span class="from g">%s</span></div><a class="pill ghost sm" href="#wa">{{br:whatsapp}}Order on WhatsApp</a></div>' % (media(None, '', 'product photo'), n, p) for n, p in prods) + '''</div></div></section>''', 'Shop', 'Brand & support')

    # ---------- BOARD ----------
    sections = []
    for name, label, sec in PAGES:
        if sec not in [x[0] for x in sections]: sections.append((sec, []))
        dict(sections)[sec].append((name, label))
    nav = ''.join('<div class="bgroup"><span class="mono">%s</span><div class="blist">%s</div></div>' % (sec, ''.join('<button type="button" data-page="%s">%s</button>' % (n, l) for n, l in items)) for sec, items in sections)
    board = ('<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hyped Up Site Concept</title>' + FONTS + '''
<style>
:root{color-scheme:dark}body{margin:0;background:#141212;color:#f2eee9;font:400 16px/1.5 Barlow,sans-serif;overflow-x:clip}
.page{max-width:1500px;margin:0 auto;padding:28px 16px 64px;display:grid;gap:20px}
h1{font-family:"Big Shoulders Display",sans-serif;font-weight:900;text-transform:uppercase;line-height:.9;margin:0;font-size:clamp(2.6rem,7vw,4.4rem)}
.mono{font:500 .7rem/1.4 "IBM Plex Mono",monospace;letter-spacing:.08em;text-transform:uppercase;color:#a39c97}
.intro{display:grid;gap:10px;max-width:84ch}.intro p{margin:0;color:#a39c97}
.nav{display:grid;gap:12px;border:1px solid rgba(242,238,233,.14);padding:14px;background:#1a1717}
.bgroup{display:grid;gap:6px}.blist{display:flex;flex-wrap:wrap;gap:6px}
.blist button{background:none;border:1px solid rgba(242,238,233,.28);color:#f2eee9;border-radius:999px;padding:.4rem .8rem;font:600 .85rem Barlow,sans-serif;cursor:pointer}
.blist button[aria-pressed="true"]{background:#f2eee9;color:#0d0c0c}
.frames{display:grid;gap:24px}@media(min-width:1100px){.frames{grid-template-columns:1fr 392px;align-items:start}}
.fdesk,.fphone{display:grid;gap:8px}
.scaler{position:relative;width:100%;aspect-ratio:1280/860;overflow:hidden;border:1px solid rgba(242,238,233,.2);border-radius:6px;background:#0d0c0c}
.scaler iframe{position:absolute;top:0;left:0;width:1280px;height:860px;border:0;transform-origin:0 0}
.fphone iframe{width:390px;max-width:100%;height:844px;border:1px solid rgba(242,238,233,.2);border-radius:28px;background:#0d0c0c;justify-self:center}
.bar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between}
.pill{display:inline-flex;align-items:center;min-height:40px;padding:0 1rem;border-radius:999px;background:linear-gradient(100deg,#de0613,#b5030f 55%,#86010a);color:#fff;font:700 .9rem Barlow,sans-serif;text-decoration:none}
details{border:1px solid rgba(242,238,233,.14);padding:12px 14px;background:#1a1717}summary{cursor:pointer;font-weight:700}
details ul{margin:10px 0 0;padding-left:1.1rem;color:#e6b84a;font-size:.92rem}
:focus-visible{outline:3px solid #ff3b2f;outline-offset:2px}
</style></head><body><div class="page">
<header class="intro"><span class="mono">Design thinking · Round 2 · Steps 7–8 · Full site concept · IA v2</span><h1>Site concept</h1>
<p>Every page rewritten from the content model: 23 services, 3 hubs (each listing every footer service), two homepage versions for the A/B test, Motorbikes, Business &amp; fleet, Builds, Contact, About, Blog and Shop. Pick a page; scroll inside the frames. Yellow = still to confirm with Hypa. Grey "Photo needed" blocks = no real photo yet.</p></header>
<nav class="nav" aria-label="Pages">''' + nav + '''</nav>
<div class="bar"><span class="mono" id="cur"></span><a class="pill" id="open" href="#" target="_blank" rel="noopener">Open full page</a></div>
<div class="frames"><div class="fdesk"><span class="mono">Desktop · 1280</span><div class="scaler"><iframe id="fd" title="Page at desktop width"></iframe></div></div>
<div class="fphone"><span class="mono">Phone · 390</span><iframe id="fp" title="Page at phone width"></iframe></div></div>
<details><summary>Still to confirm with Hypa (''' + str(len(TBC)) + ''')</summary><ul>''' + ''.join('<li>%s</li>' % t for t in TBC) + '''</ul></details>
<p class="mono" style="text-transform:none;letter-spacing:0">The contact map is a live Google Maps embed: the artifact viewer may block it; it works on the real site (after cookie consent).</p>
</div>
<script>
(function(){
  var bs=[].slice.call(document.querySelectorAll('[data-page]'));
  function fit(){var s=document.querySelector('.scaler');document.getElementById('fd').style.transform='scale('+(s.clientWidth/1280)+')'}
  function show(b){bs.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});var p=b.dataset.page;
    document.getElementById('fd').src=p;document.getElementById('fp').src=p;document.getElementById('open').href=p;document.getElementById('cur').textContent=b.textContent;fit()}
  bs.forEach(function(b){b.addEventListener('click',function(){show(b)})});
  show(bs[0]);addEventListener('resize',fit);
})();
</script></body></html>''')
    open(OUT + '/index.html', 'w').write(board)
    print(len(PAGES), 'pages')

build()
