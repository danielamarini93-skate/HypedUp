# Builds the key-pages concept (Direction D) into OUT: one HTML file per page + a review board (index.html)
# that shows each page at desktop and phone width. Media and the personal-use font are copied from the
# scratchpad and are not committed. Run: python3 build.py
import os, re, shutil
S = '/tmp/claude-0/-home-user/545d0e01-e697-5941-a49a-d293a211030b/scratchpad'
OUT = S + '/pages-out'
HERE = os.path.dirname(os.path.abspath(__file__))
L = S + '/lucide/pkg/package/icons/'
def lu(n): return re.sub(r'<!--.*?-->', '', open(L + n + '.svg').read(), flags=re.S).strip().replace('class="lucide', 'aria-hidden="true" class="lucide', 1)
def br(n): return open(S + '/brands/' + n + '.svg').read().replace('<svg ', '<svg fill="currentColor" width="18" height="18" aria-hidden="true" ', 1)
def icons(s):
    s = re.sub(r'\{\{lu:([a-z-]+)\}\}', lambda m: lu(m.group(1)), s)
    return re.sub(r'\{\{br:([a-z]+)\}\}', lambda m: br(m.group(1)), s)

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900&family=Barlow:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&family=Instrument+Serif:ital@1&display=swap">'

def head(title, desc):
    return ('<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><meta name="description" content="%s">%s<link rel="stylesheet" href="site.css"></head><body>' % (title, desc, FONTS))

MENU = [('Protect', [('Ghost &amp; immobilisers', 'ghost.html'), ('Car trackers', '#'), ('Dash cams', '#')]),
        ('Upgrade', [('CarPlay &amp; Android Auto', '#'), ('Car audio', '#'), ('Remapping', '#')]),
        ('Style', [('Car wrapping', '#'), ('Paint protection film', '#'), ('Window tinting', '#'), ('Air suspension', '#')])]
HUB = {'Protect': 'protect.html', 'Upgrade': '#', 'Style': '#'}
def header(cur):
    # Menu groups open straight onto the services (no hub links in the menu: hubs live in the footer, for SEO).
    groups = ''.join('<div class="dd"><button type="button" aria-expanded="false" aria-controls="dd-%d"%s>%s{{lu:chevron-down}}</button><ul class="ddp" id="dd-%d" hidden>%s</ul></div>'
                     % (i, ' aria-current="page"' if g == cur else '', g, i, ''.join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in it)) for i, (g, it) in enumerate(MENU))
    plain = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if n == cur else '', n) for n, h in [('Builds', 'builds.html'), ('Contact', 'contact.html')])
    doors = ''.join('<li><button type="button" aria-expanded="false" aria-controls="sd-%d">%s<span>{{lu:chevron-down}}</span></button><ul class="sub" id="sd-%d" hidden>%s</ul></li>'
                    % (i, g, i, ''.join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in it)) for i, (g, it) in enumerate(MENU))
    return ('<header class="hd"><div class="wrap"><a class="chip" href="home.html"><img src="img/logo.png" alt="Hyped Up home"></a><nav aria-label="Main" class="mainnav">' + groups + plain + '</nav>'
            '<span class="mono status"><i></i>Open today<br>10:00–18:00</span><a class="pill sm" href="contact.html">Contact us</a>'
            '<button class="menu-btn" data-menu="open" aria-label="Open menu">Menu {{lu:menu}}</button></div></header>'
            '<div class="sheet" id="sheet" hidden><div class="top"><span class="chip"><img src="img/logo.png" alt="Hyped Up"></span><button class="menu-btn" data-menu="close" aria-label="Close menu">Close {{lu:x}}</button></div>'
            '<ul class="doors" data-acc>' + doors + '<li><a href="builds.html">Builds</a></li></ul>'
            '<nav class="small" aria-label="More"><a href="#">Motorbikes</a><a href="#">Business &amp; fleet</a><a href="#">Blog</a><a href="#">About</a><a href="#">Shop</a></nav>'
            '<p class="mono hours"><i style="display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--ok);margin-right:.45rem"></i>Open today 10:00–18:00 · London SE16</p>'
            '<div class="bottom"><a class="pill" href="contact.html">Contact us</a><a class="pill ghost ico" href="#wa" aria-label="WhatsApp">{{br:whatsapp}}</a><a class="pill ghost ico" href="tel:+442033400632" aria-label="Call 020 3340 0632">{{lu:phone}}</a></div></div>'
            '<main id="main">')

COLS = [('Protect', ['Ghost &amp; immobilisers', 'Car trackers', 'Alarms', 'Dash cams', 'Taxi cameras (TfL)', 'Detailing &amp; ceramic']),
        ('Upgrade', ['CarPlay &amp; Android Auto', 'Car audio', 'Remapping', 'Reverse cameras &amp; sensors', 'Ambient lighting &amp; starlights']),
        ('Style', ['Car wrapping', 'Paint protection film', 'Window tinting', 'Air suspension', 'Chrome delete', 'Bodykits', 'Wheel refurb &amp; calipers', 'Interiors', 'Number plates', 'Van signage &amp; livery']),
        ('More', ['Motorbikes', 'Business &amp; fleet', 'Builds', 'Blog', 'Shop', 'About'])]
def footer():
    # Phone: each column is a collapsed row (details); desktop: site.js opens them all.
    def col(h, it):
        hub = ('<li class="hub"><a href="%s">All %s services →</a></li>' % (HUB[h], h)) if h in HUB else ''
        return '<details class="fcol"><summary class="mono">%s{{lu:plus}}</summary><ul>%s%s</ul></details>' % (h, hub, ''.join('<li><a href="#">%s</a></li>' % x for x in it))
    c = ''.join(col(h, it) for h, it in COLS)
    return ('</main><footer class="ft"><div class="wrap"><div class="ft-grid"><div class="findus"><span class="find">Find us</span>'
            '<p><b>Unit 22, Enterprise Industrial Estate, Bolina Road, London SE16 3LF</b></p><p class="mono">Mon–Fri 10–18 · Sat 9–16 · Sun closed</p>'
            '<div class="social"><a class="ci" href="tel:+442033400632" aria-label="Call 020 3340 0632">{{lu:phone}}</a><a class="ci" href="#wa" aria-label="WhatsApp 07713 735646">{{br:whatsapp}}</a><a class="ci" href="mailto:info@hypedup.uk" aria-label="Email info@hypedup.uk">{{lu:mail}}</a>'
            '<a href="#" aria-label="Instagram">{{br:instagram}}</a><a href="#" aria-label="TikTok">{{br:tiktok}}</a><a href="#" aria-label="Facebook">{{br:facebook}}</a></div>'
            '<p class="ftcontact">020 3340 0632 · WhatsApp 07713 735646 · info@hypedup.uk</p></div>' + c + '</div>'
            '<div class="legal mono"><span>© 2026 Hyped Up Ltd · Company no. 14086991</span><span>Privacy · Cookies · Terms · Cookie settings</span></div>'
            '<div class="wm"><svg class="wmsvg" aria-hidden="true" preserveAspectRatio="xMinYMax meet"><defs><linearGradient id="wmg" x1="0" x2="1"><stop offset="0" stop-color="#ff4033"/><stop offset=".6" stop-color="#ef1220"/><stop offset="1" stop-color="#de0613"/></linearGradient></defs>'
            '<text x="0" y="0" font-size="200" fill="none" stroke="url(#wmg)">HYPED UP</text></svg><span class="mono">Est. 2022</span></div></div></footer>'
            '<a class="fab" href="#wa" aria-label="WhatsApp Hyped Up">{{br:whatsapp}}</a><script src="site.js"></script></body></html>')

def page(name, title, desc, cur, body):
    open(os.path.join(OUT, name), 'w').write(icons(head(title, desc) + header(cur) + body + footer()))

def card(img, name, line, price, href='#', tbc=False):
    return ('<a class="card" href="%s"><div class="media vig"><img src="img/%s" alt="" loading="lazy"></div><div class="row"><h3>%s</h3><span class="from g">%s</span></div><p>%s</p>%s</a>'
            % (href, img, name, price, line, '<span class="mono tbc">Photo TBC</span>' if tbc else ''))
def band(title, line, svc=''):
    return ('<section class="band"><div class="wrap"><div><h2>%s</h2><p class="lead" style="margin-top:14px">%s</p></div><a class="pill" href="contact.html%s">Contact us</a></div></section>'
            % (title, line, ('?service=' + svc) if svc else ''))

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT + '/img'); os.makedirs(OUT + '/fonts')
    for f in os.listdir(S + '/pimg'): shutil.copy(S + '/pimg/' + f, OUT + '/img/' + f)
    shutil.copy(os.path.join(HERE, '..', 'assets', 'paint', '318600.svg'), OUT + '/img/circle.svg')
    shutil.copy(S + '/fz/graffiti_city/Graffiti City.otf', OUT + '/fonts/graffiti-city.otf')
    for f in ['site.css', 'site.js']: shutil.copy(os.path.join(HERE, f), OUT + '/' + f)

    # ---------- HOME ----------
    page('home.html', 'Car & Bike Electronics, Security & Styling | Hyped Up', 'Ghost immobilisers, trackers, CarPlay, audio, wraps, tint and air suspension, fitted properly in Bermondsey, South London. Clear "from" prices. Contact us for a quote.', '', '''
<section class="hero home"><div class="wrap">
  <div class="mono" style="display:flex;justify-content:space-between;margin-bottom:18px"><span>Bermondsey, South London</span><span>Est. 2022</span></div>
  <div class="grid">
    <div class="copy">
      <h1>Protect it.<br>Upgrade it.<span class="wet" id="morph" role="text" aria-label="Style it.">Style it.</span></h1>
      <p class="lead">South London's one-stop workshop for car and bike electronics, security and styling. Fitted properly, priced clearly.</p>
      <div class="act"><a class="pill" href="contact.html">Contact us</a><span class="find">Find us</span><span class="mono">Unit 22, Bolina Rd<br>SE16 3LF</span></div>
    </div>
    <figure><div class="media vig"><video src="img/hero.mp4" poster="img/poster.jpg" autoplay muted loop playsinline aria-label="Short silent reel of work inside the Hyped Up workshop"></video></div><figcaption class="mono" style="text-align:right">@hypedup.ltd</figcaption></figure>
  </div>
  <div class="strip" style="margin-top:32px">
    <a href="protect.html"><b>Protect</b><span class="from g">from £125</span><p>Ghost, trackers, dash cams</p></a>
    <a href="#"><b>Upgrade</b><span class="from g">from £125</span><p>CarPlay, audio, remapping</p></a>
    <a href="#"><b>Style</b><span class="from g">from £50</span><p>Wraps, PPF, tint, air suspension</p></a>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><h2>Recent builds</h2><a class="link" href="builds.html">See all builds {{lu:arrow-right}}</a></div>
  <div class="cards">
    <a class="card" href="builds.html"><div class="media vig"><img src="img/mini-jcw-low.jpg" alt="Red Mini JCW sitting low on air suspension" loading="lazy"></div><h3>Mini JCW</h3><p>Air suspension</p></a>
    <a class="card" href="builds.html"><div class="media vig"><img src="img/abarth-pink-wrap.jpg" alt="Abarth 595 in a pink wrap with gold wheels" loading="lazy"></div><h3>Abarth 595</h3><p>Pink wrap, gold wheels</p></a>
    <a class="card" href="builds.html"><div class="media vig"><img src="img/abarth-ambient.jpg" alt="Abarth interior lit with purple ambient lighting" loading="lazy"></div><h3>Abarth 595</h3><p>Ambient lighting</p></a>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><h2>How a job works</h2></div>
  <ol class="steps">
    <li><span class="mono">Step one</span><h3>Tell me what you want</h3><p>Send the car and the idea through the form or WhatsApp. Photos help.</p></li>
    <li><span class="mono">Step two</span><h3>Get a straight price</h3><p>I come back with options, a price and how long it takes. You pick a date.</p></li>
    <li><span class="mono">Step three</span><h3>Drop it off, drive it home</h3><p>Small jobs are often same-visit; a full wrap takes at least a week. <span class="tbc">(TBC: Hypa)</span></p></li>
  </ol>
</div></section>
<section class="sec"><div class="wrap split">
  <figure><div class="media vig"><img src="img/workshop.jpg" alt="Hyped Up's red Mini in front of the graffiti mural inside the workshop" loading="lazy"></div></figure>
  <div style="display:grid;gap:18px;justify-items:start">
    <span class="mono">The workshop</span><h2>Built by Hypa</h2>
    <p class="lead">I set up Hyped Up in 2022 to do this work properly: the right parts, fitted neatly, and a straight price before anything starts. Daily drivers, show cars and bikes. <span class="tbc">(Copy draft: Hypa to approve)</span></p>
    <a class="link" href="#">About Hyped Up {{lu:arrow-right}}</a>
  </div>
</div></section>
<section class="sec"><div class="wrap" style="display:grid;gap:16px;max-width:820px">
  <span class="mono">Google review</span>
  <p style="font:900 clamp(1.8rem,4vw,2.6rem)/1.05 var(--f-display);text-transform:uppercase" class="tbc">[A real 5-star review, picked by Hypa]</p>
  <span class="mono">Customer first name · Service</span>
</div></section>
''' + band('Got a car in mind?', 'Tell me the car and the idea. I\'ll come back with options and a price.'))

    # ---------- PROTECT HUB (v2: full range, layered, SEO questions) ----------
    groups = [
        ('immobilisers', 'Immobilisers', 'from £400', 'alfa-keys-wheel.jpg', 'Alfa Romeo steering wheel buttons, start button and keys',
         'Stop the car starting, even with a cloned key or a relay kit.',
         [('Ghost II immobiliser', 'PIN on the buttons your car already has. No fob, no LED. Cars and motorbikes.', 'ghost.html'),
          ('Metablok and Metablok-e', 'CAN bus immobiliser with a key-fob tag; the e version adds app control.', '#'),
          ('Scorpion X-series', 'Immobiliser that pairs with Scorpion tracking and alarms.', '#')]),
        ('trackers', 'GPS trackers', 'from £395', 'tracker.jpg', 'MetaTrak tracker card in front of a Mercedes',
         'See where the car is, get an alert if it moves, help the police recover it.',
         [('S7 trackers (SmartTrack Trident)', 'Live GPS tracking with 24/7 monitoring and battery backup.', '#'),
          ('S5 trackers (MetaTrak, Scorpion)', 'Everything S7 does, plus driver recognition: it knows if the car moves without your tag.', '#'),
          ('Motorbike trackers (Datatool S5)', 'Compact unit hidden under the seat or tail.', '#')]),
        ('alarms', 'Alarms', 'price on enquiry', 'audi-r8-unit.jpg', 'Black Audi R8 outside the Hyped Up unit',
         'Make noise and send an alert the moment someone tries.',
         [('Scorpion alarms', 'Shock, tilt and glass-break sensors, app arm and disarm, tamper alerts.', '#'),
          ('Motorbike alarms', 'Loud siren with motion and shock sensors, built for bikes.', '#')]),
        ('dashcams', 'Dash cams', 'from £125', 'dashcam.jpg', 'Dash cam fitted behind a BMW mirror',
         'Record the road, and the car while it is parked.',
         [('Front, front + rear, or 3-channel', 'Hardwired with parking mode and battery protection, wiring hidden.', '#'),
          ('FineVu and Thinkware', 'Supplied and fitted, or I fit the one you already have.', '#')]),
        ('taxi', 'Taxi cameras (TfL)', 'from £395', 'wrap.jpg', 'London taxi in the workshop',
         'TfL-approved camera systems for licensed taxis and private hire.',
         [('2-channel TfL cameras', 'Approved systems for black cabs and PHVs, fitted and tested.', '#')]),
    ]
    jump = ''.join('<a href="#%s">%s</a>' % (k, n) for k, n, *_ in groups)
    def grp(k, n, price, img, alt, line, items):
        rows = ''.join('<li><a href="%s"><b>%s</b><span>%s</span>{{lu:arrow-right}}</a></li>' % (h, t, d) for t, d, h in items)
        return ('<article class="pgroup" id="%s"><figure><div class="media vig"><img src="img/%s" alt="%s" loading="lazy"></div></figure>'
                '<div class="pbody"><div class="phead"><h3>%s</h3><span class="from g">%s</span></div><p class="lead">%s</p><ul class="plist">%s</ul></div></article>'
                % (k, img, alt, n, price, line, rows))
    page('protect.html', 'Car Security South London: Ghost, Trackers, Alarms | Hyped Up', 'Car and motorbike security fitted in Bermondsey: Ghost immobilisers, S5 and S7 trackers, alarms, dash cams and TfL taxi cameras. Clear "from" prices.', 'Protect', '''
<section class="hero flip"><div class="wrap"><div class="grid">
  <div class="copy">
    <h1>Protect it.</h1>
    <p class="lead">Keyless cars and bikes get taken in South London every week, with relay kits, cloned keys and OBD hacks. I fit the security that stops them, finds them, and puts it all on record. Cars, vans and motorbikes.</p>
    <div class="act"><a class="pill" href="contact.html?service=security">Contact us</a><a class="link" href="#compare">Which one do I need? {{lu:arrow-down}}</a></div>
  </div>
  <figure><div class="media vig"><img src="img/porsche-macan-unit.jpg" alt="Black Porsche Macan outside the Hyped Up unit"></div></figure>
</div>
<nav class="chips jump" aria-label="On this page" style="margin-top:28px">''' + jump + '''<a href="#bikes">Motorbikes</a></nav>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><h2>Layer it</h2><p>One system does one job. Thieves get past one layer; they rarely get past three.</p></div>
  <ol class="steps steps4">
    <li><span class="mono">Stop it</span><h3>Immobiliser</h3><p>No PIN, no start. Beats relay attacks and cloned keys.</p></li>
    <li><span class="mono">Warn them</span><h3>Alarm</h3><p>Tilt, shock and glass-break sensors, with an alert on your phone.</p></li>
    <li><span class="mono">Find it</span><h3>Tracker</h3><p>Live location and 24/7 monitoring if it goes anyway.</p></li>
    <li><span class="mono">Prove it</span><h3>Dash cam</h3><p>Footage of the road, and of the car while it's parked.</p></li>
  </ol>
</div></section>
<section class="sec"><div class="wrap" style="display:grid;gap:56px">
  <div class="sec-head" style="margin-bottom:0"><h2>Everything I fit</h2></div>
''' + ''.join(grp(*g) for g in groups) + '''
</div></section>
<section class="sec" id="compare"><div class="wrap">
  <div class="sec-head"><h2>Which one do I need?</h2><p>Start with how your car would be stolen. Most keyless cars need an immobiliser first.</p></div>
  <table class="compare"><thead><tr><th>Type</th><th>What it does</th><th>Best for</th><th>Price</th></tr></thead><tbody>
    <tr><td><b>Ghost immobiliser</b></td><td>Engine won't start without your PIN</td><td>Keyless cars, relay and cloned-key theft</td><td><span class="from g">from £400</span></td></tr>
    <tr><td><b>Metablok / Scorpion immobiliser</b></td><td>Blocks starting unless your tag or app says so</td><td>Owners who prefer a tag to a PIN</td><td><span class="from g">from £495</span></td></tr>
    <tr><td><b>S7 tracker</b></td><td>Live GPS, 24/7 monitoring, battery backup</td><td>Recovery if the car is taken</td><td><span class="from g">from £395</span></td></tr>
    <tr><td><b>S5 tracker</b></td><td>S7 plus driver recognition tag</td><td>High-value cars; insurer asks for S5 <span class="tbc">(TBC)</span></td><td><span class="from g">from £395</span></td></tr>
    <tr><td><b>Alarm</b></td><td>Siren and phone alert on tilt, shock or glass-break</td><td>Street parking, smash-and-grab</td><td><span class="from g">on enquiry</span></td></tr>
    <tr><td><b>Dash cam</b></td><td>Records driving and parked events</td><td>Crashes, cash-for-crash, damage</td><td><span class="from g">from £125</span></td></tr>
  </tbody></table>
  <p class="note" style="margin-top:12px">Some trackers have a monthly subscription for monitoring. I'll tell you which, and how much, before you book.</p>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div style="display:grid;gap:10px"><span class="mono">Trackers explained</span><h2>S5 or S7?</h2></div><p>Both are approved tracking categories with live GPS, 24/7 monitoring and battery backup. The difference is driver recognition.</p></div>
  <div class="vs">
    <div><h3>S7</h3><p>Tracks the car and alerts the monitoring centre if it's moved or the battery is cut.</p><span class="from g">from £395</span></div>
    <div><h3>S5</h3><p>All of S7, plus a small tag you carry. If the car moves without it, an alert goes out straight away.</p><span class="from g">from £395</span></div>
  </div>
  <p class="note" style="margin-top:14px">Some insurers ask for a specific category: send me your policy wording and I'll match it. <span class="tbc">(Insurance wording TBC: Hypa)</span></p>
</div></section>
<section class="sec" id="bikes"><div class="wrap">
  <div class="sec-head"><div style="display:grid;gap:10px"><span class="mono">Motorbikes</span><h2>Bikes get lifted into vans</h2></div><p>A bike can be gone in a minute without starting it, so bikes need tracking as well as an immobiliser.</p></div>
  <div class="chips"><a href="ghost.html">Ghost for motorbikes</a><a href="#">Datatool S5 tracker</a><a href="#">Bike alarms</a><a href="#">All motorbike work</a></div>
</div></section>
<section class="sec"><div class="wrap" style="max-width:900px">
  <div class="sec-head"><h2>Questions</h2></div>
  <div class="faq">
    <details open><summary>Can thieves bypass a Ghost immobiliser?{{lu:plus}}</summary><p>It has no fob to clone and no signal to relay, and it isn't reached through the OBD port, so the usual tools don't work. Nothing is unbeatable, which is why I recommend pairing it with a tracker.</p></details>
    <details><summary>Ghost, Metablok or Scorpion: which immobiliser?{{lu:plus}}</summary><p>Ghost uses a PIN on your own buttons; Metablok and Scorpion use a tag or app. All three stop the car starting. Tell me how you use the car and I'll recommend one.</p></details>
    <details><summary>Do I need a tracker if I have an immobiliser?{{lu:plus}}</summary><p>An immobiliser stops it being driven away; a tracker finds it if it's towed or lifted. For high-value cars and bikes, I'd fit both.</p></details>
    <details><summary>Is there a monthly fee?{{lu:plus}}</summary><p>Trackers with 24/7 monitoring have a subscription. Immobilisers, alarms and dash cams don't. You'll know the full cost before you book.</p></details>
    <details><summary>My car alarm keeps going off. Can you fix it?{{lu:plus}}</summary><p>Usually it's a badly set sensor or a weak battery. I can check it, or replace it with an alarm that sends an alert to your phone instead. <span class="tbc">(TBC: Hypa offers this)</span></p></details>
  </div>
</div></section>
''' + band('Not sure what your car needs?', 'Send me the make and model. I\'ll tell you what\'s worth fitting and what it costs.', 'security'))

    # ---------- GHOST ----------
    page('ghost.html', 'Ghost Immobiliser Fitting in South London | Hyped Up', 'Ghost immobiliser fitted in Bermondsey, South London, from £400. A PIN on your car\'s own buttons stops relay theft and cloned keys. Cars and motorbikes.', 'Protect', '''
<section class="hero flip"><div class="wrap">
  <nav class="crumbs mono" aria-label="Breadcrumb"><a href="protect.html">Protect</a><span>/</span><span aria-current="page">Ghost immobiliser</span></nav>
  <div class="grid">
    <div class="copy">
      <h1>Ghost immobiliser</h1>
      <p class="lead">Your car won't start without a PIN you enter on buttons it already has. No fob to clone, no signal to relay, nothing for a thief to find.</p>
      <div class="price"><b class="g">from £400</b><span class="mono">fitted · exact price depends on the car <span class="tbc">(TBC: Hypa)</span></span></div>
      <div class="act"><a class="pill" href="contact.html?service=security">Contact us</a></div>
    </div>
    <figure><div class="media vig"><img src="img/alfa-keys-wheel.jpg" alt="Alfa Romeo steering wheel buttons, start button and keys"></div></figure>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><h2>How it works</h2></div>
  <ol class="steps">
    <li><span class="mono">Step one</span><h3>Get in</h3><p>Unlock the car as normal, with your own key.</p></li>
    <li><span class="mono">Step two</span><h3>Enter your PIN</h3><p>A sequence on the steering wheel, window or door buttons. Only you know it.</p></li>
    <li><span class="mono">Step three</span><h3>Drive</h3><p>No PIN, no start, even with the key in the car.</p></li>
  </ol>
</div></section>
<section class="sec"><div class="wrap split">
  <div style="display:grid;gap:22px">
    <h2>What's included</h2>
    <ul class="ticks">
      <li>{{lu:check}}The Ghost unit</li><li>{{lu:check}}Fitting, about 2–3 hours</li><li>{{lu:check}}Your PIN, set up with you</li>
      <li>{{lu:check}}A full test before you leave</li><li>{{lu:check}}Paperwork for your insurer</li><li>{{lu:check}}Warranty on the fitting</li>
    </ul>
  </div>
  <div style="display:grid;gap:14px">
    <span class="mono">Ghost for your car</span>
    <div class="chips"><a href="#">BMW</a><a href="#">Mercedes</a><a href="#">Audi</a><a href="#">VW</a><a href="#">Range Rover</a><a href="#">Motorbikes</a></div>
  </div>
</div></section>
<section class="sec"><div class="wrap" style="max-width:900px">
  <div class="sec-head"><h2>Questions</h2></div>
  <div class="faq">
    <details open><summary>How much does a Ghost cost?{{lu:plus}}</summary><p>From £400 fitted. The exact price depends on the car, so send me the make and model and I'll confirm.</p></details>
    <details><summary>How long does fitting take?{{lu:plus}}</summary><p>About 2–3 hours, depending on the car.</p></details>
    <details><summary>Can a thief find it?{{lu:plus}}</summary><p>It sits behind the dash, wired into the car's own data network, with no LED and no extra fob to spot.</p></details>
    <details><summary>Does it work on motorbikes?{{lu:plus}}</summary><p>Yes, I fit Ghost to cars and motorcycles.</p></details>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><h2>Pair it with</h2><a class="link" href="protect.html">All Protect services {{lu:arrow-right}}</a></div>
  <div class="cards">''' + card('tracker.jpg', 'Car trackers', 'If it goes anyway, you can see where it is.', 'from £395') + card('dashcam.jpg', 'Dash cams', 'Everything on record, parked or driving.', 'from £125') + '''</div>
</div></section>
''' + band('Book your Ghost', 'Tell me the car. I\'ll confirm the price and a date.', 'security'))

    # ---------- BUILDS ----------
    items = [
        ('audi-r8-unit.jpg', 'Audi R8', 'Work <span class="tbc">TBC</span>', 'upgrade', 'Black Audi R8 outside the Hyped Up unit'),
        ('abarth-pink-wrap.jpg', 'Abarth 595', 'Pink wrap, gold wheels', 'style', 'Pink Abarth 595 with gold wheels'),
        ('audi-r8-carplay.jpg', 'Audi R8', 'New CarPlay screen', 'upgrade', 'Audi R8 dashboard with a new CarPlay screen'),
        ('porsche-macan-unit.jpg', 'Porsche Macan', 'Work <span class="tbc">TBC</span>', 'style', 'Black Porsche Macan outside the Hyped Up unit'),
        ('bentley-unit.jpg', 'Bentley Flying Spur', 'Work <span class="tbc">TBC</span>', 'style', 'Bentley outside the Hyped Up unit'),
        ('mercedes-screen.jpg', 'Mercedes', 'Screen upgrade', 'upgrade', 'Mercedes dashboard with a large new screen'),
        ('fiat-500-red.jpg', 'Fiat 500', 'Work <span class="tbc">TBC</span>', 'upgrade', 'Red Fiat 500 inside the workshop'),
        ('ford-transit-yellow.jpg', 'Ford Transit Custom', 'Work <span class="tbc">TBC</span>', 'style', 'Yellow Ford Transit Custom van in the workshop'),
        ('mini-jcw-low.jpg', 'Mini JCW', 'Air suspension', 'style', 'Red Mini JCW sitting low on air suspension'),
        ('abarth-ambient.jpg', 'Abarth 595', 'Ambient lighting', 'upgrade', 'Abarth interior with purple ambient lighting'),
        ('volvo-xc90-satin.jpg', 'Volvo XC90', 'Satin finish, gold details <span class="tbc">TBC</span>', 'style', 'Satin grey Volvo XC90 with gold wheel details'),
        ('boot-build.jpg', 'Boot build', 'Subwoofer enclosure', 'upgrade', 'Custom boot with a red and black subwoofer enclosure'),
        ('wrap.jpg', 'London taxi', 'Purple colour change', 'style', 'London taxi wrapped in purple inside the workshop'),
        ('carplay.jpg', 'Mini', 'Wireless CarPlay screen', 'upgrade', 'Mini dashboard with a new CarPlay screen'),
        ('tracker.jpg', 'Mercedes', 'MetaTrak tracker', 'protect', 'MetaTrak tracker card in front of a Mercedes'),
        ('dashcam.jpg', 'BMW', 'Front and rear dash cam', 'protect', 'Dash cam fitted behind a BMW mirror'),
        ('civic.jpg', 'Honda Civic Type R', 'Work <span class="tbc">TBC</span>', 'upgrade', 'Yellow Honda Civic Type R in the workshop'),
    ]
    figs = ''.join('<figure data-tags="%s"><div class="media vig"><img src="img/%s" alt="%s" loading="lazy"></div><figcaption><b>%s</b><span class="mono">%s</span></figcaption></figure>' % (t, i, a, n, w) for i, n, w, t, a in items)
    page('builds.html', 'Builds: Wraps, Air Suspension, Audio & More | Hyped Up', 'Real cars and bikes from the Hyped Up workshop in Bermondsey: wraps, air suspension, CarPlay, audio, ambient lighting and security installs. See the work, then get a quote.', 'Builds', '''
<section class="hero"><div class="wrap" style="display:grid;gap:22px">
  <h1>Builds</h1>
  <p class="lead">Real work from the workshop: wraps, air, audio, lighting and security.</p>
  <div class="feature" style="margin-top:12px">
    <figure><div class="media vig"><img src="img/workshop.jpg" alt="Hyped Up's red Mini JCW in front of the workshop mural"></div></figure>
    <div style="display:grid;gap:12px;justify-items:start"><span class="mono">Our own car</span><h2>Mini JCW</h2><p class="lead">Air Lift suspension, wheels and styling. The car on the workshop wall. <span class="tbc">(Spec TBC: Hypa)</span></p></div>
  </div>
</div></section>
<section class="sec" style="padding-top:40px"><div class="wrap">
  <div class="chips" role="group" aria-label="Filter builds" style="margin-bottom:28px">
    <button type="button" data-filter="all" aria-pressed="true">All</button><button type="button" data-filter="protect" aria-pressed="false">Protect</button><button type="button" data-filter="upgrade" aria-pressed="false">Upgrade</button><button type="button" data-filter="style" aria-pressed="false">Style</button>
  </div>
  <div class="gal">''' + figs + '''</div>
</div></section>
''' + band('Want yours on this wall?', 'Tell me the car and the idea. I\'ll come back with options and a price.'))

    # ---------- CONTACT ----------
    needs = [('security', 'Security'), ('screens', 'Screens &amp; audio'), ('wrap', 'Wrap'), ('ppf', 'PPF or tint'), ('air', 'Air suspension'), ('remap', 'Remap'), ('plates', 'Plates'), ('other', 'Other')]
    ticks = ''.join('<label><input type="checkbox" name="need" value="%s" data-label="%s"><span>{{lu:check}}%s</span></label>' % (v, l.replace('&amp;', '&'), l) for v, l in needs)
    srcs = ['Google', 'Google Maps', 'Instagram', 'TikTok', 'A friend', 'Been before']
    MAPQ = 'Hyped%20Up%2C%20Unit%2022%2C%20Enterprise%20Industrial%20Estate%2C%20Bolina%20Road%2C%20London%20SE16%203LF'
    page('contact.html', 'Contact Hyped Up: Get a Quote | Bermondsey, London', 'Get a quote from Hyped Up in Bermondsey, South London. Pick the job, tell us the car, add photos if you like, and send it by WhatsApp or email. Open Mon–Sat.', 'Contact', '''
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
  </aside>
</div>
''')

    # ---------- BOARD ----------
    pages = [
        ('contact', 'Contact', 'contact.html?service=security', ['<b>Short form v2:</b> pick the job, write the car, optional note + photos, then send. That\'s it on a phone.', '<b>Send on WhatsApp</b> needs nothing else (WhatsApp knows the number). <b>Send by email</b> opens name + email (both <b>required</b>, with a clear message if missing; phone optional).', '"How did you find us?" moved to the thank-you screen as one optional tap.', 'Opened from a Protect page, so <b>Security</b> is pre-ticked.', '<b>Real Google Map</b> with Get directions to the Business Profile.'], ['Reply time in the thank-you (Hypa)', 'Live site: load the map only after cookie consent (Google sets cookies)']),
        ('protect', 'Protect (hub)', 'protect.html', ['<b>v2, full range:</b> immobilisers (Ghost, Metablok, Scorpion), S7 / S5 / bike trackers, alarms, dash cams, TfL taxi cameras, motorbikes.', '"Layer it": stop it · warn them · find it · prove it.', 'Bigger "Which one do I need?" table, an S5 vs S7 explainer and an FAQ built from real search questions (seo.md).', 'Jump links under the hero so the long page stays easy on a phone.'], ['Insurance / Thatcham wording (S5 vs S7)', 'Alarm repair offer and alarm price', 'A bike install photo (bike section is text-only for now)']),
        ('ghost', 'Ghost immobiliser', 'ghost.html', ['The service-page template: breadcrumb, H1 with the search term, price block, one action.', 'How it works in 3 steps, what\'s included, links to car-specific pages, FAQ (becomes FAQ schema), pair-with cards.', 'All facts from Hypa\'s own Ghost blog post.'], ['Ghost price: "from £400" (pricing.md; not in the master sheet)', 'Warranty and insurer paperwork wording']),
        ('builds', 'Builds', 'builds.html', ['Featured build (our own Mini), then a filterable grid: All / Protect / Upgrade / Style.', 'New from your Drive upload: Audi R8 (outside + CarPlay), Porsche Macan, Bentley, Mercedes screen, Fiat 500, yellow Transit.', 'Customer plates blurred, no faces.'], ['Captions marked TBC: what work was done on the R8, Macan, Bentley, Fiat, Transits, Volvo, Civic (Hypa)', 'More builds as the Drive upload continues']),
        ('home', 'Homepage', 'home.html', ['Direction D hero with the reel and the "Style it." morph (3 loops).', 'Service strip → recent builds → how a job works → the workshop → one review → contact band.', 'Every button says "Contact us"; on phones WhatsApp floats.', '<b>Menu v3 (all pages):</b> Protect / Upgrade / Style open straight onto their services; the hub pages are only in the footer ("All Protect services →") for SEO.', '<b>Footer v3:</b> on phones the columns fold into Protect / Upgrade / Style / More rows; contact as icon buttons.'], ['A real Google review (Hypa picks)', '"Built by Hypa" copy (Hypa approves)', 'Step three timing wording']),
    ]
    tabs = ''.join('<button type="button" role="tab" aria-selected="%s" data-p="%s">%s</button>' % ('true' if i == 0 else 'false', k, n) for i, (k, n, u, a, b) in enumerate(pages))
    panels = ''.join(
        '<section class="bp" id="p-%s"%s><div class="bnotes"><div><h3>What\'s on it</h3><ul>%s</ul></div><div><h3>Still TBC</h3><ul>%s</ul></div><a class="pill sm" href="%s" target="_blank" rel="noopener">Open full page</a></div>'
        '<div class="frames"><div class="fdesk"><span class="mono">Desktop · 1280</span><div class="scaler"><iframe data-src="%s" title="%s, desktop" loading="lazy"></iframe></div></div>'
        '<div class="fphone"><span class="mono">Phone · 390</span><iframe data-src="%s" title="%s, phone" loading="lazy"></iframe></div></div></section>'
        % (k, '' if i == 0 else ' hidden', ''.join('<li>%s</li>' % x for x in a), ''.join('<li>%s</li>' % x for x in b), u, u, n, u, n) for i, (k, n, u, a, b) in enumerate(pages))
    board = ('<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hyped Up Key Pages</title>' + FONTS + '''
<style>
:root{color-scheme:dark}body{margin:0;background:#141212;color:#f2eee9;font:400 16px/1.5 Barlow,sans-serif;overflow-x:clip}
.page{max-width:1500px;margin:0 auto;padding:32px 16px 64px}
h1,h3{font-family:"Big Shoulders Display",sans-serif;font-weight:900;text-transform:uppercase;line-height:.9;margin:0}
h1{font-size:clamp(2.6rem,7vw,4.4rem)} h3{font-size:1.25rem;margin-bottom:.4rem}
.mono{font:500 .7rem/1.4 "IBM Plex Mono",monospace;letter-spacing:.08em;text-transform:uppercase;color:#a39c97}
.intro{display:grid;gap:10px;max-width:78ch;margin-bottom:24px}.intro p{margin:0;color:#a39c97}
.tabs{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 22px}
.tabs button{background:none;border:1px solid rgba(242,238,233,.28);color:#f2eee9;border-radius:999px;padding:.6rem 1rem;font:600 .92rem Barlow,sans-serif;cursor:pointer}
.tabs button[aria-selected="true"]{background:#f2eee9;color:#0d0c0c}
.bp[hidden]{display:none}
.bnotes{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));align-items:start;background:#1a1717;border:1px solid rgba(242,238,233,.14);padding:18px;margin-bottom:20px}
.bnotes ul{margin:0;padding-left:1.1rem;color:#d3ccc7;font-size:.92rem;display:grid;gap:4px}
.bnotes div+div ul{color:#e6b84a}
.pill{display:inline-flex;align-items:center;justify-content:center;min-height:42px;padding:0 1.05rem;border-radius:999px;background:linear-gradient(100deg,#de0613,#b5030f 55%,#86010a);color:#fff;font:700 .95rem Barlow,sans-serif;text-decoration:none;justify-self:start;align-self:center}
.frames{display:grid;gap:24px;grid-template-columns:1fr}
@media(min-width:1100px){.frames{grid-template-columns:1fr 392px;align-items:start}}
.fdesk,.fphone{display:grid;gap:8px}
.scaler{position:relative;width:100%;aspect-ratio:1280/860;overflow:hidden;border:1px solid rgba(242,238,233,.2);border-radius:6px;background:#0d0c0c}
.scaler iframe{position:absolute;top:0;left:0;width:1280px;height:860px;border:0;transform-origin:0 0}
.fphone iframe{width:390px;max-width:100%;height:844px;border:1px solid rgba(242,238,233,.2);border-radius:28px;background:#0d0c0c;justify-self:center}
:focus-visible{outline:3px solid #ff3b2f;outline-offset:2px}
</style></head><body><div class="page">
<header class="intro"><span class="mono">Design thinking · Round 2 · Step 7–8 · Key pages · Direction D</span><h1>Key pages</h1>
<p>Five pages built as real, clickable pages: scroll inside each frame, tap the menu on the phone, try the form. Every button now says <b>Contact us</b> and goes to the contact page; on phones a WhatsApp button floats. Yellow notes = still to confirm.</p></header>
<div class="tabs" role="tablist" aria-label="Pages">''' + tabs + '</div>' + panels + '''</div>
<script>
(function(){
  function fit(){document.querySelectorAll('.scaler').forEach(function(s){var f=s.querySelector('iframe');f.style.transform='scale('+(s.clientWidth/1280)+')'})}
  function load(p){p.querySelectorAll('iframe[data-src]').forEach(function(f){if(!f.src)f.src=f.dataset.src})}
  var tabs=[].slice.call(document.querySelectorAll('[role=tab]'));
  tabs.forEach(function(t){t.addEventListener('click',function(){tabs.forEach(function(x){x.setAttribute('aria-selected',x===t?'true':'false');document.getElementById('p-'+x.dataset.p).hidden=x!==t});load(document.getElementById('p-'+t.dataset.p));fit()})});
  load(document.querySelector('.bp:not([hidden])'));fit();addEventListener('resize',fit);
})();
</script></body></html>''')
    open(OUT + '/index.html', 'w').write(board)
    print('built', sorted(os.listdir(OUT)))

build()
