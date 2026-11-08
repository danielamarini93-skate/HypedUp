# Builds index.html from template.html (embeds images, expands the menu accordion and footer).
import base64, sys
I = sys.argv[1].rstrip('/') + '/'; V = sys.argv[2].rstrip('/') + '/'
s = open('template.html').read()
d = lambda p, t: 'data:%s;base64,%s' % (t, base64.b64encode(open(p, 'rb').read()).decode())
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
        rows = ''.join('<li><a href="#"><span>%s</span><span class="from">%s</span></a></li>' % (t, ('from ' + p) if p != 'enquiry' else 'on enquiry') for t, p in items)
        out.append('<li><button aria-expanded="false" aria-controls="%s"><b>%s</b><span>{{lu:arrow-right}}</span></button><ul class="sub" id="%s" hidden>%s<li class="all"><a href="#">All %s services →</a></li></ul></li>' % (pid, g, pid, rows, g))
    return ''.join(out)
while '{{acc}}' in s: s = s.replace('{{acc}}', acc(), 1)
pdata = [
 ('Protect','t-protect','dashcam.jpg','BMW · front + rear dash cam',[('Ghost &amp; immobilisers','£495','The car won\'t start without your secret button code'),('Car trackers','£395','Thatcham-category S5 and S7, app alerts, recovery'),('Dash cams','£125','Front, rear and 3-channel, hardwired with parking mode'),('Paint protection film','enquiry','Clear film against stone chips and scratches')]),
 ('Upgrade','t-upgrade','carplay.jpg','Mini · wireless CarPlay screen',[('CarPlay &amp; Android Auto','£170','Wireless CarPlay on a new screen or your factory one'),('Car audio','£125','Speakers, amps, subs, boot builds, sound deadening'),('Remapping','£250','Stage 1 to 3 for cars and bikes, done properly')]),
 ('Style','t-style','wrap.jpg','London taxi · colour change',[('Car wrapping','£1,500','Full colour changes, roofs, stripes, chameleon'),('Window tinting','£150','Standard, carbon or ceramic film, legal fronts'),('Air suspension','£1,895','Air Lift and Prazis, set up for daily driving')]),
]
def panels():
    out=[]
    for i,(g,cls,img,cap,items) in enumerate(pdata):
        rows=''.join('<li><a href="#"><b>%s</b><em class="from">%s</em><span>%s</span></a></li>' % (t, ('from '+p) if p!='enquiry' else 'price on enquiry', dsc) for t,p,dsc in items)
        out.append('<div class="panel" id="pn%d"%s><div><span class="tag %s">%s</span><ul>%s</ul><a class="all" href="#">All %s services →<i class="mk" style="--m:var(--m-line)" aria-hidden="true"></i></a></div><div class="ph" style="background-image:url(\'{{img:%s}}\')"><i>%s</i></div><div class="idea"><i class="mk" style="--m:var(--m-splat)" aria-hidden="true"></i><h3>Not sure what you need?</h3><p>Send your car and your idea. Hypa replies with options and prices.</p><a class="btn" href="#quote">{{wa}}Ask on WhatsApp</a></div></div>' % (i, '' if i==0 else ' hidden', cls, g, rows, g, img.split('.')[0], cap))
    return ''.join(out)
s = s.replace('{{panels}}', panels())
cols = [
 ('Protect', ['Ghost &amp; immobilisers','Car trackers','Dash cams','Paint protection film','Taxi cameras (TfL)','Detailing &amp; ceramic']),
 ('Upgrade', ['CarPlay &amp; Android Auto','Car audio','Remapping','Reverse cameras &amp; sensors','Ambient lighting &amp; starlights']),
 ('Style',   ['Car wrapping','Window tinting','Air suspension','Chrome delete','Bodykits','Wheel refurb &amp; calipers','Interiors','Number plates','Van signage &amp; livery']),
 ('More',    ['Motorbikes','Business &amp; fleet','Builds','Blog','Shop']),
 ('Hyped Up',['About','Contact']),
]
circle = '<i class="mk sp" style="--m:var(--m-speck)" aria-hidden="true"></i><i class="mk" style="--m:var(--m-circle)" aria-hidden="true"></i>'
old_circle = '<svg class="circle" viewBox="0 0 300 200" preserveAspectRatio="none" aria-hidden="true"><path d="M40 30 C 120 -5, 260 5, 290 70 C 310 140, 230 195, 130 192 C 40 190, 2 140, 8 90 C 12 50, 60 22, 150 18" fill="none" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round" vector-effect="non-scaling-stroke" filter="url(#rough)"/></svg>'
def footer(mobile):
    c = ''.join('<div><h4>%s</h4><ul>%s</ul></div>' % (h, ''.join('<li><a href="#">%s</a></li>' % x for x in items)) for h, items in cols)
    find = ('<div class="findus"><h4>%sFind us</h4><p><b>Unit 22, Enterprise Industrial Estate,<br>Bolina Road, London SE16 3LF</b></p>'
            '<p>Mon–Fri 10:00–18:00<br>Sat 09:00–16:00 · Sun closed</p><p>020 3340 0632<br>WhatsApp 07713 735646<br>info@hypedup.uk</p>'
            '<div class="social"><a href="#" aria-label="Instagram">{{br:instagram}}</a><a href="#" aria-label="TikTok">{{br:tiktok}}</a><a href="#" aria-label="Facebook">{{br:facebook}}</a></div></div>') % circle
    grid = (find + c) if mobile else (c + find)
    return ('<footer class="ft%s"><div class="ft-grid">%s</div><div class="legal"><span>© 2026 Hyped Up Ltd · Company no. 14086991</span>'
            '<span>Privacy · Cookies · Terms · Cookie settings</span></div><div class="wm" aria-hidden="true"><i class="mk sp" style="--m:var(--m-speck)"></i><b>Hyped Up</b><i class="mk drips" style="--m:var(--m-drips)"></i></div></footer>') % (' ft-mobile' if mobile else '', grid)
s = s.replace('{{footer}}', footer(False)).replace('{{footer_m}}', footer(True))
s = s.replace('{{img:logo}}', d(I + 'logo-s.png', 'image/png')).replace('{{img:dashcam}}', d(I + 'dashcam.jpg', 'image/jpeg')).replace('{{img:carplay}}', d(I + 'carplay.jpg', 'image/jpeg')).replace('{{img:wrap}}', d(I + 'wrap.jpg', 'image/jpeg')).replace('{{img:poster}}', d(V + 'poster.jpg', 'image/jpeg'))
wa = '{{br:whatsapp}}'
s = s.replace('{{wa}}', wa).replace('{{brush}}', '<svg class="brush" viewBox="0 0 100 12" preserveAspectRatio="none" aria-hidden="true"><path d="M3 7 C 25 3, 55 10, 97 5" fill="none" stroke="url(#g)" stroke-width="6" stroke-linecap="round" filter="url(#rough)"/></svg>').replace('{{chev}}', '{{lu:chevron-down}}')
import re, os
L = os.environ['LUCIDE']; B = os.environ['BRANDS']; M = os.environ['MASKS']; F = os.environ['FONT']
def lucide(name):
    t = open(os.path.join(L, name + '.svg')).read()
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S).strip()
    return t.replace('class="lucide', 'aria-hidden="true" class="lu lucide', 1)
s = re.sub(r'\{\{lu:([a-z-]+)\}\}', lambda m: lucide(m.group(1)), s)
def brand(name):
    t = open(os.path.join(B, name + '.svg')).read()
    return t.replace('<svg ', '<svg fill="currentColor" width="16" height="16" aria-hidden="true" ', 1)
s = re.sub(r'\{\{br:([a-z]+)\}\}', lambda m: brand(m.group(1)), s)
masks = {'splat':'202417','drips':'213808','speck':'213823','line':'212674','circle':'318600','enso':'351243','brush':'211151','spray':'213817','smear':'213832'}
s = s.replace('{{maskvars}}', ':root{' + ''.join('--m-%s:url("%s");' % (k, d(os.path.join(M, v + '.svg'), 'image/svg+xml')) for k, v in masks.items()) + '}')
s = s.replace('{{font:hoax}}', d(F, 'font/ttf'))
assert '{{' not in s, s[s.index('{{'):s.index('{{')+30]
open('index.html', 'w').write(s); print(len(s) // 1024, 'KB')
