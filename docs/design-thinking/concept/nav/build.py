# Builds index.html from template.html (v4, Direction D): embeds images, icons, the circle mark and the
# Graffiti City font; expands the desktop panels, phone accordions and footer. Previous version: build-v3.py.
import base64, os, re
S = '/tmp/claude-0/-home-user/545d0e01-e697-5941-a49a-d293a211030b/scratchpad'   # local media + font files (not committed)
A = '../assets'
d = lambda p, t: 'data:%s;base64,%s' % (t, base64.b64encode(open(p, 'rb').read()).decode())
s = open('template.html').read()
price = lambda p, long=False: ('from ' + p) if p != 'enquiry' else ('price on enquiry' if long else 'on enquiry')

menu = [
 ('Protect', [('Ghost &amp; immobilisers','£495'),('Car trackers','£395'),('Dash cams','£125'),('Paint protection film','enquiry')]),
 ('Upgrade', [('CarPlay &amp; Android Auto','£170'),('Car audio','£125'),('Remapping','£250')]),
 ('Style',   [('Car wrapping','£1,500'),('Window tinting','£150'),('Air suspension','£1,895')]),
]
n = [0]
def acc():
    n[0] += 1; out = []
    for i, (g, items) in enumerate(menu):
        pid = 'p%d_%d' % (n[0], i)
        rows = ''.join('<li><a href="#"><span>%s</span><span class="from g">%s</span></a></li>' % (t, price(p)) for t, p in items)
        out.append('<li><button aria-expanded="false" aria-controls="%s"><em class="g">0%d</em><b>%s</b><span>{{lu:arrow-right}}</span></button>'
                   '<ul class="sub" id="%s" hidden>%s<li class="all"><a href="#">All %s services →</a></li></ul></li>' % (pid, i + 1, g, pid, rows, g))
    return ''.join(out)
while '{{acc}}' in s: s = s.replace('{{acc}}', acc(), 1)

pdata = [
 ('Protect','dashcam','BMW · front + rear dash cam',[('Ghost &amp; immobilisers','£495','The car won\'t start without your secret button code'),('Car trackers','£395','Thatcham-category S5 and S7, app alerts, recovery'),('Dash cams','£125','Front, rear and 3-channel, hardwired with parking mode'),('Paint protection film','enquiry','Clear film against stone chips and scratches')]),
 ('Upgrade','carplay','Mini · wireless CarPlay screen',[('CarPlay &amp; Android Auto','£170','Wireless CarPlay on a new screen or your factory one'),('Car audio','£125','Speakers, amps, subs, boot builds, sound deadening'),('Remapping','£250','Stage 1 to 3 for cars and bikes, done properly')]),
 ('Style','wrap','London taxi · colour change',[('Car wrapping','£1,500','Full colour changes, roofs, stripes, chameleon'),('Window tinting','£150','Standard, carbon or ceramic film, legal fronts'),('Air suspension','£1,895','Air Lift and Prazis, set up for daily driving')]),
]
def panels():
    out = []
    for i, (g, img, cap, items) in enumerate(pdata):
        rows = ''.join('<li><a href="#"><b>%s</b><em class="from g">%s</em><span>%s</span></a></li>' % (t, price(p, True), dsc) for t, p, dsc in items)
        out.append('<div class="panel" id="pn%d"%s><div><p class="lab"><em class="g">0%d</em><span class="mono">%s</span></p><ul>%s</ul>'
                   '<a class="all" href="#">All %s services {{lu:arrow-right}}</a></div>'
                   '<figure><div class="ph" style="background-image:url(\'{{img:%s}}\')"></div><figcaption class="mono"><span>%s</span><span>Unit 22</span></figcaption></figure>'
                   '<div class="idea"><span class="mono">Not on the list?</span><h3>Not sure what you need?</h3><p>Send your car and your idea. Hypa replies with options and prices.</p>'
                   '<a class="pill" href="#quote">{{br:whatsapp}}Ask on WhatsApp</a></div></div>'
                   % (i, '' if i == 0 else ' hidden', i + 1, g, rows, g, img, cap))
    return ''.join(out)
s = s.replace('{{panels}}', panels())

cols = [
 ('01','Protect', ['Ghost &amp; immobilisers','Car trackers','Dash cams','Paint protection film','Taxi cameras (TfL)','Detailing &amp; ceramic']),
 ('02','Upgrade', ['CarPlay &amp; Android Auto','Car audio','Remapping','Reverse cameras &amp; sensors','Ambient lighting &amp; starlights']),
 ('03','Style',   ['Car wrapping','Window tinting','Air suspension','Chrome delete','Bodykits','Wheel refurb &amp; calipers','Interiors','Number plates','Van signage &amp; livery']),
 ('','More',      ['Motorbikes','Business &amp; fleet','Builds','Blog','Shop']),
 ('','Hyped Up',  ['About','Contact']),
]
def footer(mobile):
    c = ''.join('<div><h4 class="mono">%s%s</h4><ul>%s</ul></div>' % (('<em class="g">%s</em>' % num) if num else '', h, ''.join('<li><a href="#">%s</a></li>' % x for x in items)) for num, h, items in cols)
    find = ('<div class="findus"><span class="find">Find us</span><p><b>Unit 22, Enterprise Industrial Estate,<br>Bolina Road, London SE16 3LF</b></p>'
            '<p>Mon–Fri 10:00–18:00<br>Sat 09:00–16:00 · Sun closed</p><p>020 3340 0632<br>WhatsApp 07713 735646<br>info@hypedup.uk</p>'
            '<div class="social"><a href="#" aria-label="Instagram">{{br:instagram}}</a><a href="#" aria-label="TikTok">{{br:tiktok}}</a><a href="#" aria-label="Facebook">{{br:facebook}}</a></div></div>')
    grid = (find + c) if mobile else (c + find)
    return ('<footer class="ft%s"><div class="ft-grid">%s</div><div class="legal mono"><span>© 2026 Hyped Up Ltd · Company no. 14086991</span>'
            '<span>Privacy · Cookies · Terms · Cookie settings</span></div><div class="wm"><svg class="wmsvg" aria-hidden="true" preserveAspectRatio="xMinYMax meet"><defs><linearGradient id="wmg%s" x1="0" x2="1"><stop offset="0" stop-color="#d4280f"/><stop offset=".55" stop-color="#e8501a"/><stop offset="1" stop-color="#f26f22"/></linearGradient></defs><text x="0" y="0" font-size="200" fill="none" stroke="url(#wmg%s)">HYPED UP</text></svg>'
            '<span class="mono">Bermondsey · SE16<br>Cars + bikes · Est. 2022</span></div></footer>') % (' ft-mobile' if mobile else '', grid, 'm' if mobile else 'd', 'm' if mobile else 'd')
s = s.replace('{{footer}}', footer(False)).replace('{{footer_m}}', footer(True))

for k in ['logo', 'dashcam', 'carplay', 'wrap']:
    f = 'logo-s.png' if k == 'logo' else k + '.jpg'
    s = s.replace('{{img:%s}}' % k, d(S + '/img/' + f, 'image/png' if k == 'logo' else 'image/jpeg'))
s = s.replace('{{img:poster}}', d(S + '/vid/poster.jpg', 'image/jpeg'))
L = S + '/lucide/pkg/package/icons/'
s = re.sub(r'\{\{lu:([a-z-]+)\}\}', lambda m: re.sub(r'<!--.*?-->', '', open(L + m.group(1) + '.svg').read(), flags=re.S).strip().replace('class="lucide', 'aria-hidden="true" class="lu lucide', 1), s)
s = re.sub(r'\{\{br:([a-z]+)\}\}', lambda m: open(S + '/brands/' + m.group(1) + '.svg').read().replace('<svg ', '<svg fill="currentColor" width="16" height="16" aria-hidden="true" ', 1), s)
s = s.replace('{{maskvars}}', ':root{--m-circle:url("%s")}' % d(os.path.join(A, 'paint', '318600.svg'), 'image/svg+xml'))
s = s.replace('{{font:gcity}}', d(S + '/fz/graffiti_city/Graffiti City.otf', 'font/otf'))
assert '{{' not in s, s[s.index('{{'):s.index('{{') + 30]
open('index.html', 'w').write(s); print(len(s) // 1024, 'KB')
