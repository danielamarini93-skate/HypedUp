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
        out.append('<li><button aria-expanded="false" aria-controls="%s"><b>%s</b><span>→</span></button><ul class="sub" id="%s" hidden>%s<li class="all"><a href="#">All %s services →</a></li></ul></li>' % (pid, g, pid, rows, g))
    return ''.join(out)
while '{{acc}}' in s: s = s.replace('{{acc}}', acc(), 1)
cols = [
 ('Protect', ['Ghost &amp; immobilisers','Car trackers','Dash cams','Paint protection film','Taxi cameras (TfL)','Detailing &amp; ceramic']),
 ('Upgrade', ['CarPlay &amp; Android Auto','Car audio','Remapping','Reverse cameras &amp; sensors','Ambient lighting &amp; starlights']),
 ('Style',   ['Car wrapping','Window tinting','Air suspension','Chrome delete','Bodykits','Wheel refurb &amp; calipers','Interiors','Number plates','Van signage &amp; livery']),
 ('More',    ['Motorbikes','Business &amp; fleet','Builds','Blog','Shop','Prices']),
 ('Hyped Up',['About','Google reviews','Visit']),
]
circle = '<svg class="circle" viewBox="0 0 300 200" preserveAspectRatio="none" aria-hidden="true"><path d="M40 30 C 120 -5, 260 5, 290 70 C 310 140, 230 195, 130 192 C 40 190, 2 140, 8 90 C 12 50, 60 22, 150 18" fill="none" stroke="#e30513" stroke-width="3" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>'
def footer(mobile):
    c = ''.join('<div><h4>%s</h4><ul>%s</ul></div>' % (h, ''.join('<li><a href="#">%s</a></li>' % x for x in items)) for h, items in cols)
    find = ('<div class="findus"><h4>%sFind us</h4><p><b>Unit 22, Enterprise Industrial Estate,<br>Bolina Road, London SE16 3LF</b></p>'
            '<p>Mon–Fri 10:00–18:00<br>Sat 09:00–16:00 · Sun closed</p><p>020 3340 0632<br>WhatsApp 07713 735646<br>info@hypedup.uk</p>'
            '<div class="social"><a href="#" aria-label="Instagram">IG</a><a href="#" aria-label="TikTok">TT</a><a href="#" aria-label="Facebook">FB</a><a href="#" aria-label="LinkedIn">IN</a></div></div>') % circle
    grid = (find + c) if mobile else (c + find)
    return ('<footer class="ft%s"><div class="ft-grid">%s</div><div class="legal"><span>© 2026 Hyped Up Ltd · Company no. 14086991</span>'
            '<span>Privacy · Cookies · Terms · Cookie settings</span></div><div class="wordmark" aria-hidden="true">Hyped Up</div></footer>') % (' ft-mobile' if mobile else '', grid)
s = s.replace('{{footer}}', footer(False)).replace('{{footer_m}}', footer(True))
s = s.replace('{{img:logo}}', d(I + 'logo-s.png', 'image/png')).replace('{{img:dashcam}}', d(I + 'dashcam.jpg', 'image/jpeg')).replace('{{img:poster}}', d(V + 'poster.jpg', 'image/jpeg'))
wa = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.6a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'
s = s.replace('{{wa}}', wa).replace('{{chev}}', '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>')
assert '{{' not in s, s[s.index('{{'):s.index('{{')+30]
open('index.html', 'w').write(s); print(len(s) // 1024, 'KB')
