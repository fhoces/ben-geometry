"""Preview of what the laser will produce: the cut disc in light plywood, with burn marks.

Approximate look only: real burn color and pit depth depend on the wood and the
laser settings. Every mark comes straight from 17gon-laser.svg, so positions are exact.

    /opt/anaconda3/bin/python3 make_preview.py 17gon-laser.svg preview.png 6
    /opt/anaconda3/bin/python3 make_preview.py 17gon-laser.svg preview-closeup.png 20 86 80 98 54
    /opt/anaconda3/bin/python3 make_preview.py 17gon-laser-back.svg preview-back.png 6

Arguments: input SVG, output PNG, pixels per mm, then optionally a window in mm
(x, y, width, height) for a close-up.
"""
import re, sys, numpy as np, fitz
from PIL import Image, ImageFilter
src, out, PX = sys.argv[1], sys.argv[2], float(sys.argv[3])
win = [float(v) for v in sys.argv[4:8]] if len(sys.argv) > 4 else None   # x0 y0 w h in mm
svg=open(src).read()
m=re.search(r'id="cut"[^>]* r="([\d.]+)"',svg)
if m is None:   # the back side has no cut line: take the disc size from the front file
    import os
    m=re.search(r'id="cut"[^>]* r="([\d.]+)"',open(os.path.join(os.path.dirname(os.path.abspath(src)),"17gon-laser.svg")).read())
cut_r=float(m.group(1))
size_mm=float(re.search(r'width="([\d.]+)mm"',svg).group(1))
x0,y0,wmm,hmm = win if win else (0,0,size_mm,size_mm)
W,H=int(wmm*PX),int(hmm*PX)
k=72/25.4
def render(s):
    pdf=fitz.open("pdf", fitz.open("svg", s.encode()).convert_to_pdf())
    pix=pdf[0].get_pixmap(matrix=fitz.Matrix(PX/k, PX/k), alpha=True,
                          clip=fitz.Rect(x0*k, y0*k, (x0+wmm)*k, (y0+hmm)*k))
    a=np.frombuffer(pix.samples,np.uint8).reshape(pix.h,pix.w,pix.n)
    return np.pad(a[...,3],((0,max(0,H-pix.h)),(0,max(0,W-pix.w))))[:H,:W].astype(np.float32)/255
no_cut=re.sub(r'<circle id="(cut|align-guide-do-not-cut)"[^>]*/>','',svg)   # cut line and guide are not burned
engrave=render(re.sub(r'<g id="needle-holes">.*?</g>','',no_cut,flags=re.S))
holes=render(re.sub(r'<g id="engrave-(lines|text)">.*?</g>','',no_cut,flags=re.S))
y,x=np.mgrid[0:H,0:W].astype(np.float32)/PX; x+=x0; y+=y0
# plywood: long, gently drifting grain lines plus fine fibre noise (deterministic in board mm)
rng=np.random.default_rng(7)
coef=rng.normal(size=(6,3))
drift=sum(a*np.sin(x/(40+30*i)+b) for i,(a,b,_) in enumerate(coef))*0.9
lines=0.5+0.5*np.sin((y+drift)*2*np.pi/2.3)
bands=0.5+0.5*np.sin((y+1.7*drift)*2*np.pi/17.0)
fib=rng.random((max(2,H//2),max(2,W//6))).astype(np.float32)
fib=np.array(Image.fromarray((fib*255).astype(np.uint8)).resize((W,H),Image.BILINEAR),np.float32)/255
shade=0.93+0.03*lines**4+0.035*bands+0.02*fib
wood=np.array([228,196,152],np.float32)[None,None,:]*shade[...,None]
burn=np.array([88,54,30],np.float32); pit=np.array([35,20,10],np.float32)
img=wood*(1-0.88*engrave[...,None])+burn*0.88*engrave[...,None]
img=img*(1-holes[...,None])+pit*holes[...,None]
c=size_mm/2; r=np.hypot(x-c,y-c); inside=r<=cut_r
edge=np.clip(1-(cut_r-r)/0.6,0,1)*inside
img=img*(1-0.6*edge[...,None])+np.array([65,40,22],np.float32)*0.6*edge[...,None]
table=np.full((H,W,3),[206,206,201],np.float32)
sh=((np.hypot(x-c-1.5,y-c-2.5)<=cut_r)*255).astype(np.uint8)
shadow=np.array(Image.fromarray(sh).filter(ImageFilter.GaussianBlur(1.6*PX)),np.float32)/255
table=table*(1-0.35*shadow[...,None])
Image.fromarray(np.clip(np.where(inside[...,None],img,table),0,255).astype(np.uint8)).save(out)
print(out, W, H)
