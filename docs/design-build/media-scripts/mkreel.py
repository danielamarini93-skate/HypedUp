# Homepage hero reel v3: clean finished cars and bikes, close-ups, two tidy Hypa shots, soft crossfades, one colour grade.
import json, glob, subprocess, os
S = '/tmp/claude-0/-home-user/545d0e01-e697-5941-a49a-d293a211030b/scratchpad'
M = json.load(open(S + '/vmaster.json'))
def src(n): return glob.glob('%s/vsrc/%03d.*' % (S, n))[0]
GRADE = 'eq=contrast=1.07:saturation=1.12:brightness=0.01'
XF = 0.3  # crossfade seconds
# (clip#, seconds, vertical focus, start offset or None = middle)
SEGS = [(63, 2.4, .5, None),        # classic 911 under the HYPD sign
        (234, 2.0, .55, None),      # Evoque satin wrap, RANGE ROVER letters close
        (32, 1.9, .05, None),       # Hypa tinting, HYPD gilet
        (190, 2.0, .5, None),       # Audi R8 outside the unit, lights on
        (182, 1.9, .5, None),       # R8 CarPlay screen working
        ('alloygator', 2.0, .5, None),  # AlloyGator on a clean Tesla wheel (photo push-in)
        (172, 2.0, .5, None),       # BMW M1000RR in the workshop
        (65, 2.0, .5, None),        # R1 rides out of the unit
        (93, 1.9, .45, None),       # starlight headliner
        (223, 1.9, .45, None),      # Hypa fitting a screen, close
        (257, 1.9, .5, None),       # Volvo wheel pinstripe
        (187, 1.9, .5, None),       # red Mini, black stripes, HYPD plate
        (202, 2.2, .5, None),       # Bentley Bentayga outside the unit
        (62, 2.4, .5, None)]        # 911 satin wrap pan, end
ins, fil = [], []
for i, (n, d, fy, st) in enumerate(SEGS):
    if n == 'alloygator':
        fr = int(d * 30)
        ins += ['-loop', '1', '-framerate', '30', '-t', '%.2f' % d, '-i', S + '/psrc/alloygator.jpg']
        fil.append("[%d:v]crop=iw:iw:0:(ih-iw)*0.55,scale=1440:1440,zoompan=z='1+0.10*on/%d':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=720x720:fps=30,%s,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v%d]" % (i, fr, GRADE, i))
        continue
    dur = M[n]['dur']; s0 = st if st is not None else max(0, (dur - d) / 2)
    ins += ['-ss', '%.2f' % s0, '-t', '%.2f' % d, '-i', src(n)]
    fil.append('[%d:v]crop=min(iw\\,ih):min(iw\\,ih):(iw-min(iw\\,ih))/2:(ih-min(iw\\,ih))*%.2f,scale=720:720,fps=30,%s,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v%d]' % (i, fy, GRADE, i))
# crossfade chain
prev, t = '[v0]', SEGS[0][1]
for i in range(1, len(SEGS)):
    out = '[x%d]' % i
    fil.append('%s[v%d]xfade=transition=fade:duration=%.2f:offset=%.2f%s' % (prev, i, XF, t - XF, out))
    t = t + SEGS[i][1] - XF; prev = out
OUT = S + '/vout/hyped-up-workshop-reel.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y'] + ins + ['-filter_complex', ';'.join(fil), '-map', prev, '-an', '-c:v', 'libx264', '-preset', 'slow', '-crf', '31',
                '-movflags', '+faststart', '-pix_fmt', 'yuv420p', OUT], check=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '0.8', '-i', OUT, '-frames:v', '1', '-q:v', '3', OUT[:-4] + '.jpg'], check=True)
print(round(os.path.getsize(OUT) / 1e6, 2), 'MB', round(t, 1), 's')
