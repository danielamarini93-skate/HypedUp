# Turns the approved v5 concept pages (pages-out/) into Claude Design artboards (.dc.html) + canvas.json.
# Desktop artboard = the page itself (fluid, 1440 frame). Phone artboard = a 390 frame that imports the same page.
import json, os, re, sys
from datetime import datetime, timezone
from bs4 import BeautifulSoup, NavigableString, Comment

S = '/tmp/claude-0/-home-user/545d0e01-e697-5941-a49a-d293a211030b/scratchpad'
SRC = S + '/pages-out/'
OUT = S + '/dc/root/project/'
os.makedirs(OUT, exist_ok=True)
B = json.load(open(S + '/dc/blobs.json'))
H = json.load(open(S + '/heights.json'))
CSS_BLOB = sys.argv[1] if len(sys.argv) > 1 else 'CSSBLOB'
DS = 'https://claude.ai/artifact/JRh26Xr17rGo7XrjZ1virr'

def blob(name):
    return '/_blob/' + B[name] if name in B else None

SECTIONS = [
    ('home', 'Homepage', [('home-a', 'Home A · brand-led'), ('home-b', 'Home B · task-led')]),
    ('hubs', 'Hubs', [('security', 'Security'), ('upgrades', 'Upgrades'), ('styling', 'Styling')]),
    ('security', 'Security services', [('ghost-immobiliser', 'Ghost immobiliser'), ('car-trackers', 'Car trackers'), ('dash-cams', 'Dash cams'), ('car-alarms', 'Car alarms'), ('taxi-cameras', 'Taxi cameras')]),
    ('upgrades', 'Upgrades services', [('carplay', 'CarPlay & Android Auto'), ('car-audio', 'Car audio'), ('remapping', 'Remapping'), ('reverse-cameras', 'Reverse cameras'), ('ambient-lighting', 'Ambient lighting'), ('performance-parts', 'Exhausts & performance')]),
    ('styling', 'Styling services', [('car-wrapping', 'Car wrapping'), ('paint-protection-film', 'Paint protection film'), ('window-tinting', 'Window tinting'), ('air-suspension', 'Air suspension'), ('coilovers', 'Coilovers'), ('chrome-delete', 'Chrome delete'), ('bodykits', 'Bodykits'), ('wheel-refurb', 'Wheel refurb'), ('interiors', 'Interiors'), ('detailing', 'Detailing'), ('number-plates', 'Number plates'), ('van-signage', 'Van signage')]),
    ('audience', 'Motorbikes and business', [('motorbikes', 'Motorbikes'), ('business', 'Business & fleet')]),
    ('brand', 'Brand and support', [('builds', 'Builds'), ('contact', 'Contact'), ('about', 'About'), ('community', 'Community'), ('blog', 'Blog'), ('shop', 'Shop')]),
]
SLUGS = {s for _, _, ps in SECTIONS for s, _ in ps}

HEAD = '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
<link rel="stylesheet" href="%s">
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900&amp;family=Barlow:wght@400;500;600;700&amp;family=IBM+Plex+Mono:wght@500;600&amp;display=swap">
<style>
@font-face{font-family:"Graffiti City";src:url(%s) format("woff2");font-display:block}
body{margin:0;background:#0d0c0c}
a{color:#f2eee9}a:hover{color:#ff3b2f}
%s
</style>
</helmet>
'''
TAIL = '''</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":%d,"height":%d}}'>
class Component extends DCLogic {
renderVals() { return {}; }
}
</script>
</body>
</html>
'''

def convert(slug):
    soup = BeautifulSoup(open(SRC + slug + '.html').read(), 'html.parser')
    title = soup.title.get_text() if soup.title else slug
    body = soup.body
    for t in body.find_all(['script', 'noscript']): t.decompose()
    for c in body.find_all(string=lambda x: isinstance(x, Comment)): c.extract()
    for v in body.find_all('video'):
        img = soup.new_tag('img')
        poster = (v.get('poster') or '').replace('img/', '')
        img['src'] = blob(poster) or ''
        img['alt'] = v.get('aria-label', '')
        for k in ('class', 'style'):
            if v.get(k): img[k] = v[k]
        v.replace_with(img)
    for i in body.find_all('img'):
        src = i.get('src', '')
        if src.startswith('img/'):
            b = blob(src[4:])
            if b: i['src'] = b
            else: i.decompose(); continue
        for k in ('loading', 'decoding', 'srcset', 'sizes', 'fetchpriority'):
            if i.has_attr(k): del i[k]
    for s in body.find_all('source'): s.decompose()
    for a in body.find_all('a', href=True):
        h = a['href']
        m = re.match(r'^([a-z0-9-]+)\.html(\?.*)?(#.*)?$', h)
        if m and m.group(1) in SLUGS: a['href'] = m.group(1) + '.dc.html'
        elif m: a['href'] = '#'
    extra, n = [], 0
    for el in body.find_all(style=re.compile(r'url\(')):
        def rep(mm):
            name = mm.group(1).replace('img/', '')
            return 'url(%s)' % (blob(name) or '')
        st = re.sub(r'url\(([^)]+)\)', rep, el['style'])
        n += 1; cls = 'dcbg%d' % n
        extra.append('.%s{%s}' % (cls, st))
        del el['style']
        el['class'] = (el.get('class') or []) + [cls]
    for f in body.find_all('form'):
        f['action'] = '#'
    inner = ''.join(str(c) for c in body.contents)
    inner = inner.replace('{{', '{ {').replace('}}', '} }')
    return title, inner, '\n'.join(extra)

boards, order, notes, pages = {}, [], {}, []
ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def clamp(h): return max(400, min(8000, h))

files = []
for pid, pname, ps in SECTIONS:
    pages.append({'id': pid, 'name': pname})
    x = 0
    notes['t-' + pid] = {'x': 0, 'y': -300, 'text': pname, 'kind': 'title1', 'page': pid, 'maxW': 3000}
    for slug, label in ps:
        title, inner, extra = convert(slug)
        hd, hp = clamp(H[slug + '.html']['1440']), clamp(H[slug + '.html']['390'])
        d = slug + '.dc.html'
        open(OUT + d, 'w').write(HEAD % (title, CSS_BLOB, blob('graffiti-city.woff2'), extra) + '<div class="dcroot">\n' + inner + '\n</div>\n' + TAIL % (1440, hd))
        p = slug + '.phone.dc.html'
        open(OUT + p, 'w').write(HEAD % (label + ' (phone)', CSS_BLOB, blob('graffiti-city.woff2'), extra) +
            '<div style="width: 390px; min-height: %dpx; background: #0d0c0c">\n<dc-import name="%s" hint-size="390px,%dpx"></dc-import>\n</div>\n' % (hp, slug, hp) + TAIL % (390, hp))
        boards[d] = {'x': x, 'y': 0, 'w': 1440, 'h': hd, 'title': label + ' · desktop', 'page': pid, 'expand': 'fill'}
        boards[p] = {'x': x + 1440 + 80, 'y': 0, 'w': 390, 'h': hp, 'title': label + ' · phone', 'page': pid}
        order += [d, p]; files += [d, p]
        x += 1440 + 80 + 390 + 200

# Entry board: a cover with links to every page
rows = ''.join('<section style="display: grid; gap: 12px"><h2 style="margin: 0; font: 900 28px/1 \'Big Shoulders Display\', sans-serif; text-transform: uppercase; color: #f2eee9">%s</h2><div style="display: flex; flex-wrap: wrap; gap: 8px">%s</div></section>'
               % (pname, ''.join('<a href="%s.dc.html" style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 16px; border: 1px solid rgba(242,238,233,.28); border-radius: 999px; color: #f2eee9; text-decoration: none; font: 600 15px Barlow, sans-serif">%s</a>' % (s, l) for s, l in ps))
               for _, pname, ps in SECTIONS)
main = (HEAD % ('Hyped Up website design', CSS_BLOB, blob('graffiti-city.woff2'), '') +
    '<div style="width: 1440px; height: 1100px; box-sizing: border-box; padding: 80px; background: #0d0c0c; color: #f2eee9; display: flex; flex-direction: column; gap: 40px; font-family: Barlow, sans-serif">'
    '<div style="display: flex; align-items: center; gap: 24px"><img src="%s" alt="Hyped Up" style="height: 56px; background: #141212; padding: 10px 14px; border-radius: 10px"><span style="font: 500 13px \'IBM Plex Mono\', monospace; letter-spacing: .08em; text-transform: uppercase; color: #a39c97">Design build v1 · 21 Nov 2026</span></div>'
    '<h1 style="margin: 0; font: 900 120px/.9 \'Big Shoulders Display\', sans-serif; text-transform: uppercase">Hyped Up website</h1>'
    '<p style="margin: 0; max-width: 70ch; font-size: 20px; line-height: 1.5; color: #d3ccc7">36 pages, each at desktop (1440) and phone (390). Built on the Hyped Up Brand design system, Direction D "Workshop wall". Copy and photos are the v5 drafts: they change after the review with Hypa. Videos show as their poster frame. Click a page to open it.</p>'
    '%s</div>\n' % (blob('logo.png'), rows) + TAIL % (1440, 1100))
open(OUT + 'Main.dc.html', 'w').write(main)
pages.insert(0, {'id': 'cover', 'name': 'Cover'})
boards = {'Main.dc.html': {'x': 0, 'y': 0, 'w': 1440, 'h': 1100, 'title': 'Cover', 'page': 'cover'}, **boards}
order = ['Main.dc.html'] + order
canvas = {'v': 3, 'createdOnFiles': {'v': 1, 'at': ts}, 'title': 'Hyped Up website design', 'launch': {'view': 'canvas', 'page': 'cover'},
          'pages': pages, 'boards': boards, 'order': order, 'notes': notes,
          'designSystems': [{'title': 'Hyped Up', 'namespace': 'hypedup', 'artifact': DS, 'version': '1795123857-9b58', 'copiedAt': ts}]}
json.dump(canvas, open(OUT + 'canvas.json', 'w'), indent=1)
json.dump(files, open(S + '/dc/files.json', 'w'))
print(len(files), 'artboards +Main', round(sum(os.path.getsize(OUT + f) for f in files) / 1e6, 2), 'MB')
