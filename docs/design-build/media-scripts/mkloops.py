# Cuts silent square loops (720x720, H.264, no audio) from reviewed clips. Each loop = list of (clip#, seconds, vertical focus 0..1).
import json, glob, os, subprocess, sys
S='/tmp/claude-0/-home-user/545d0e01-e697-5941-a49a-d293a211030b/scratchpad'
M=json.load(open(S+'/vmaster.json'))
def src(n): return glob.glob('%s/vsrc/%03d.*'%(S,n))[0]
L={
 'hyped-up-workshop-reel': [(32,2,.05),(121,2,.5),(223,2,.45),(243,2,.45),(92,2,.4),(232,2,.5),(63,2.2,.5)],
 'unit-22-meet-ruff-ryders': [(19,3.5,.5),(65,3,.5),(66,3,.5)],
 'window-tint-hypa-fitting': [(20,3.5,.45),(32,3,.05)],
 'evoque-satin-wrap': [(232,3,.5),(230,2.5,.5),(234,3,.55)],
 'audi-s4-air-struts-hypa': [(121,2.5,.5),(124,3,.5),(125,2.5,.5)],
 'carplay-screen-fitting-hypa': [(223,3,.45),(151,2.5,.5),(248,3,.5)],
 'boot-build-audio-hypa': [(243,3.5,.45),(110,2.5,.5),(120,2.5,.5)],
 'starlight-headliner': [(87,2.5,.5),(92,3,.4),(93,3.5,.45)],
 'dash-cam-mirror': [(185,4,.5),(194,4,.5)],
 'van-reverse-camera': [(265,2.6,.5,'slow')],
 'van-lettering-hypa': [(126,3,.5),(251,2.5,.5),(255,3,.5)],
 'm1000rr-tracker': [(168,3,.5),(172,3.5,.5)],
 'ppf-headlights': [(58,2.6,.4,'end')],
 'lexus-splitter-fitting': [(43,2.5,.5),(44,3.5,.5)],
 'volvo-wheel-detail': [(257,5,.5)],
 'hypa-in-the-workshop': [(34,2.8,.5),(36,3.5,.5)],
 'porsche-911-outside-unit': [(63,5,.5),(62,3,.5)],
 'audi-a4-soundproofing-build': [(109,2.5,.5),(110,3,.5),(111,2.5,.5)],
 'bmw-e88-build': [(147,2.5,.5),(151,2.5,.5),(159,2.5,.5),(136,2.5,.5)],
 'bdg-van-livery': [(126,3,.5),(130,3,.5)],
 'audi-r8-carplay-reel': [(182,3,.5),(190,3,.5)],
 'mini-stripes-reel': [(187,3,.5),(205,2.5,.5)],
 'bentayga-reel': [(202,5,.5)],
 'hypa-engine-bay': [(140,3,.5),(36,3,.5)],
 'e88-grille-black': [(13,4,.5)],
}
only=sys.argv[1:]
for name,segs in L.items():
    if only and name not in only: continue
    out='%s/vout/%s.mp4'%(S,name)
    ins=[];fil=[]
    for i,seg in enumerate(segs):
        n,d,fy=seg[:3]; opt=seg[3] if len(seg)>3 else ''
        dur=M[n]['dur']; st=max(0,dur-d-0.1) if opt=='end' else max(0,(dur-d)/2)
        ins+=['-ss','%.2f'%st,'-t','%.2f'%d,'-i',src(n)]
        slow='setpts=1.6*PTS,' if opt=='slow' else ''
        fil.append('[%d:v]crop=min(iw\\,ih):min(iw\\,ih):(iw-min(iw\\,ih))/2:(ih-min(iw\\,ih))*%.2f,scale=720:720,%sfps=30,setsar=1,format=yuv420p[v%d]'%(i,fy,slow,i))
    fc=';'.join(fil)+';'+''.join('[v%d]'%i for i in range(len(segs)))+'concat=n=%d:v=1:a=0[o]'%len(segs)
    subprocess.run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc,'-map','[o]','-an','-c:v','libx264','-preset','slow','-crf','30','-movflags','+faststart','-pix_fmt','yuv420p',out],check=True)
    subprocess.run(['ffmpeg','-v','error','-y','-ss','0.6','-i',out,'-frames:v','1','-q:v','4',out[:-4]+'.jpg'],check=True)
    print(name, round(os.path.getsize(out)/1e6,2),'MB')
