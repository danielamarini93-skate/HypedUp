# Generates the hand-drawn marker marks used as CSS masks (drawn for this project, no licence needed):
# hand-underline.svg (already in use), hand-arrow.svg (curved arrow pointing right), hand-line.svg (long wobbly stroke).
# Tapered strokes with slight wobble = a marker pen, not a code-drawn line. Run: python3 make_hand_marks.py
import math, os
HERE = os.path.dirname(os.path.abspath(__file__))

def stroke(pts_fn, wmax, wmin, n=90, taper=0.35):
    top, bot = [], []
    for i in range(n + 1):
        t = i / n
        x, y = pts_fn(t); x2, y2 = pts_fn(min(1, t + 1e-3))
        if t >= 1: x0, y0 = pts_fn(t - 1e-3); x2, y2 = x + (x - x0), y + (y - y0)
        w = wmin + (wmax - wmin) * (math.sin(math.pi * t) ** taper)
        dx, dy = x2 - x, y2 - y; L = math.hypot(dx, dy) or 1; nx, ny = -dy / L, dx / L
        top.append((x + nx * w / 2, y + ny * w / 2)); bot.append((x - nx * w / 2, y - ny * w / 2))
    return 'M' + ' L'.join('%.1f %.1f' % p for p in top + bot[::-1]) + 'Z'

def save(name, w, h, paths):
    open(os.path.join(HERE, name), 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="none">%s</svg>' % (w, h, ''.join('<path d="%s"/>' % p for p in paths)))

# curved arrow: a sweeping shaft + two quick head strokes
shaft = stroke(lambda t: (8 + 170 * t, 62 - 34 * math.sin(math.pi * t * .9) + 6 * t + 1.2 * math.sin(t * 13)), 7, 2)
head1 = stroke(lambda t: (179 - 27 * t, 57 - 1 * t + 1.2 * math.sin(t * 7)), 6.5, 2, n=30, taper=.2)
head2 = stroke(lambda t: (179 - 13 * t, 57 - 24 * t + 1 * math.sin(t * 9)), 6.5, 2, n=30, taper=.2)
save('hand-arrow.svg', 200, 80, [shaft, head1, head2])

# long timeline stroke: gentle wobble, thicker in the middle, plus a short second pass near the start
line = stroke(lambda t: (4 + 992 * t, 14 + 2.6 * math.sin(t * 9.5 + .4) + 1.2 * math.sin(t * 31)), 7, 2.4, n=220, taper=.25)
back = stroke(lambda t: (40 + 260 * t, 17 + 1.5 * math.sin(t * 6)), 3, 1, n=60)
save('hand-line.svg', 1000, 30, [line, back])
# vertical version of the timeline stroke (phones)
vline = stroke(lambda t: (14 + 2.6 * math.sin(t * 9.5 + .4) + 1.2 * math.sin(t * 31), 4 + 992 * t), 7, 2.4, n=220, taper=.25)
save('hand-line-v.svg', 30, 1000, [vline])
print('ok')
