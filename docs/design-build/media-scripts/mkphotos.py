# Web copies of the new photos: EXIF rotation applied, crops/plate blurs, max 1400 px, JPEG 80, metadata stripped.
from PIL import Image, ImageOps, ImageFilter, ImageDraw
S='/tmp/claude-0/-home-user/545d0e01-e697-5941-a49a-d293a211030b/scratchpad'
J=[('p-saab-wiring-hypa','carplay-saab-wiring-hypa',None,None),
 ('p-mini-conv-hypa','mini-convertible-hypa-screen',(0,0,1,.69),None),
 ('p-mt07-plate-hypa','mt07-tail-tidy-hypa',None,(.42,.48,.62,.60)),
 ('p-combo-heatgun-hypa','van-lettering-heat-gun-hypa',(0,.03,.43,.43),None),
 ('p-vauxhall-tint-hypa','rear-tint-hypa-mural',(0,0,1,.70),None),
 ('p-e88-boot-hypa','e88-boot-speaker-pods-hypa',None,None),
 ('p-streetfighter-hypa','hypa-carbon-streetfighter',None,None),
 ('p-snowfoam-hypa','bike-snow-foam-unit-22',None,None),
 ('p-subaru-camo-hypa','subaru-camo-fitting-hypa',None,None),
 ('p-workshop-aisle-hypa','workshop-aisle-hypa',None,None),
 ('p-meet-entrance-hypa','meet-entrance-hypa-ruff-ryders',(0,.25,1,.70),None),
 ('p-meet-crowd-sky','meet-unit-22-crowd',(0,.1,1,.72),None),
 ('p-meet-hayabusa-rr','meet-hayabusa-ruff-ryders',None,None),
 ('p-meet-mini-subs','meet-mini-sub-boot',None,None),
 ('p-s4-struts-people','s4-air-struts-hypa',None,None),
 ('p-cx5-tint-hypa','cx5-tint-hypa',None,None),
 ('p-giulia-tint-hypa','giulia-tint-hypa',None,None),
 ('p-e88-grilles-hypa','e88-grilles-hypa',None,None),
 ('p-a4-roof-deadening-hypa','a4-roof-deadening-hypa',None,None),
 ('p-911-hypa-mini-05','porsche-911-hypa-mini',None,None),
 ('p-mt07-red-mini','mt07-red-mini',None,None)]
for src,dst,crop,blur in J:
    im=ImageOps.exif_transpose(Image.open('%s/psrc/%s.jpg'%(S,src))).convert('RGB'); W,H=im.size
    if blur:
        box=(int(blur[0]*W),int(blur[1]*H),int(blur[2]*W),int(blur[3]*H))
        reg=im.crop(box).filter(ImageFilter.GaussianBlur(28)); m=Image.new('L',reg.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,reg.size[0]-1,reg.size[1]-1),radius=12,fill=255)
        im.paste(reg,box,m.filter(ImageFilter.GaussianBlur(3)))
    if crop: im=im.crop((int(crop[0]*W),int(crop[1]*H),int(crop[2]*W),int(crop[3]*H)))
    im.thumbnail((1400,1400))
    im.save('%s/pimg/%s.jpg'%(S,dst),quality=80,optimize=True,progressive=True)
print('ok')
