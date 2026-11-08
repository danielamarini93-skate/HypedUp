# Builds index.html from template.html: embeds reference thumbnails, photos, masks and the tag font.
import base64, os, re
S = '/tmp/claude-0/-home-user/545d0e01-e697-5941-a49a-d293a211030b/scratchpad'
A = '../assets'
d = lambda p, t: 'data:%s;base64,%s' % (t, base64.b64encode(open(p, 'rb').read()).decode())
s = open('template.html').read()
for k in ['play1', 'play2', 'pin', 'rage1', 'rage2', 'rage3', 'urb1', 'sams', 'kelsi']:
    src = os.path.join(S, 'refs', 't-%s.jpg' % k)
    if not os.path.exists(src):
        from PIL import Image
        im = Image.open(os.path.join(S, 'refs', {'rage3': 'rage3.webp'}[k])).convert('RGB'); im.thumbnail((640, 480)); im.save(src, quality=72)
    s = s.replace('{{ref:%s}}' % k, d(src, 'image/jpeg'))
s = s.replace('{{img:logo}}', d(S + '/img/logo-s.png', 'image/png')).replace('{{img:poster}}', d(S + '/vid/poster.jpg', 'image/jpeg')).replace('{{img:civic}}', d(S + '/img/civic.jpg', 'image/jpeg'))
masks = {'splat': '202417', 'spray': '213817', 'enso': '351243', 'circle': '318600'}
s = s.replace('{{maskvars}}', ':root{' + ''.join('--m-%s:url("%s");' % (k, d(os.path.join(A, 'paint', v + '.svg'), 'image/svg+xml')) for k, v in masks.items()) + '}')
s = s.replace('{{font:hoax}}', d(os.path.join(A, 'fonts', 'hoax-vandal.ttf'), 'font/ttf'))
assert '{{' not in s, s[s.index('{{'):s.index('{{') + 30]
open('index.html', 'w').write(s); print(len(s) // 1024, 'KB')
