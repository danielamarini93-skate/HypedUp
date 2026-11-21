# Moves downloaded Drive blobs into vsrc/<n>.<ext> (matched by byte size) and makes an 8-frame strip per clip.
import json, os, subprocess, glob, sys
S='/tmp/claude-0/-home-user/545d0e01-e697-5941-a49a-d293a211030b/scratchpad'
T='/root/.claude/projects/-home-user/545d0e01-e697-5941-a49a-d293a211030b/tool-results'
M=json.load(open(S+'/vmaster.json')); bysize={x['size']:x for x in M}
for f in glob.glob(T+'/mcp-Google_Drive-blob-*'):
    sz=os.path.getsize(f); x=bysize.get(sz)
    if not x: continue
    ext=os.path.splitext(f)[1].lower() or '.mov'
    dst='%s/vsrc/%03d%s'%(S,x['n'],ext); os.replace(f,dst)
for f in sorted(glob.glob(S+'/vsrc/*')):
    n=int(os.path.basename(f)[:3]); out='%s/vstrip/%03d.jpg'%(S,n)
    if os.path.exists(out): continue
    try: d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode().strip())
    except Exception: d=0
    M[n]['dur']=round(d,1)
    if d<=0: continue
    subprocess.run(['ffmpeg','-v','error','-y','-i',f,'-vf','fps=8/%f,scale=-2:180,pad=ceil(iw/2)*2:180,tile=8x1'%d,'-frames:v','1',out])
json.dump(M,open(S+'/vmaster.json','w'),indent=0)
have=len(glob.glob(S+'/vsrc/*')); print('have',have,'of',len(M),'strips',len(glob.glob(S+'/vstrip/*')))
