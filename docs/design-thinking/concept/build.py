# Builds index.html from template.html by embedding images and the hero video as data URIs.
# Usage: python3 build.py <images dir> <video dir>
import base64, sys
I, V = sys.argv[1].rstrip('/') + '/', sys.argv[2].rstrip('/') + '/'
s = open('template.html').read()
def d(p, t): return 'data:%s;base64,%s' % (t, base64.b64encode(open(p, 'rb').read()).decode())
imgs = {'logo': 'logo-s.png', 'carplay': 'carplay.jpg', 'wrap': 'wrap.jpg', 'civic': 'civic.jpg', 'porsche': 'porsche.jpg',
        'mini': 'workshop.jpg', 'remap': 'remap.jpg', 'dashcam': 'dashcam.jpg'}
for k, f in imgs.items(): s = s.replace('{{img:%s}}' % k, d(I + f, 'image/png' if f.endswith('png') else 'image/jpeg'))
s = s.replace('{{img:poster}}', d(V + 'poster.jpg', 'image/jpeg')).replace('{{vid}}', d(V + 'hero.mp4', 'video/mp4'))
wa = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.6a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'
s = s.replace('{{wa}}', wa).replace('{{pause}}', '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 2h3v12H4zM9 2h3v12H9z" fill="currentColor"/></svg>')
assert '{{' not in s
open('index.html', 'w').write(s)
print(len(s) // 1024, 'KB')
