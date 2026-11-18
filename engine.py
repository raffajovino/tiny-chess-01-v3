import json,os,sys,time,urllib.request
V=os.environ.get('MAKEFUN_ENV_URL')or sys.exit(1)
def P(p,d):
 q=urllib.request.Request(V+p,data=json.dumps(d).encode(),headers={'content-type':'application/json'})
 try:
  with urllib.request.urlopen(q)as r:return json.load(r)
 except Exception:return None
N=(-21,-19,-12,-8,8,12,19,21);K=(-11,-10,-9,-1,1,9,10,11);D=(-11,-9,9,11,-10,-1,1,10)
MV=(20,84,91,119,256,0);WV=(24,70,74,128,234,0);PH=(0,1,1,2,4,0)
T=[ord(c)-74 for c in "JJJJJJJJblYb[jRGHLPRZXPEFMLOPMNDCJIMNLLDDIIHKKRGAJEDFPTDJJJJJJJJ 4B>Y2F/8@\\SPZLF>YSZ_j\\UHNOWS[NPGKNMQOOHDHMLONPFC=GIJNFE0E<BFCEDCK6AD@LHDNFGRYN>FSUTSVSJIKOVSSLJHMMPRMLKJNNNNQNLKNNJLORJBIFEGG@ERTRWZLRUQRXZ^[PUIOPSNUYNDGLPPSHEADGJLHLD?DFFKJIB?FEHJMH8EGJNNLADCJQMYUUUD@IJFXQXGFLLQXVXCCFFJNJJHDHHJIKIFJGJIJNKAHMJLNIJJFHLFDB>:PNF<BJMQJEHHI@CHPJFELPDFEGCBDFA>JC@>?B=FFD>?BFCJLH:?FLLFSM<LCPNJJJJJJJJvurloksybc_[XW^_RPMKJKNNMLIHHHKJKLHJJIJHMLLLMJJHJJJJJJJJ<@GCBC:1DHDJHDD=DELLJHE@FKPPPMLFFHNPNNKFDIJNLIED@EHIJED?C=DFDF>:FEGHHHFDHILGIGIFJHJJJLJKILMLNLKJHKMOLLIHGILLMKHFFFHJKHFCDHDIHFIFMLNNMMLKMMMMIKLKLLLKKIIIKKMJJJJJKKLKIHHGIJIJHGHFHHJJHHGIHJKJIGKEHPPQQOLOFORTXPRJELLVVSOLKPPUXTXSFQOVRRTPFCNLLNLKDDBFFDABBCD?IBE@8AFFGNKFGNNNNTPMLNPNOUUMHPPQPRPKFIOPQPLGEIMOPNLHCGKMNKIF=BEGCFD?"]
Y=[7 if i%10 in(0,9)or i<21 or i>98 else 0 for i in range(120)]
M=[((i//10-2)*8+i%10-1)if 20<i<99 and 0<i%10<9 else 0 for i in range(120)]
CS=((25,1,(26,27),27),(25,2,(24,23,22),23),(95,4,(96,97),97),(95,8,(94,93,92),93))
B=Y[:];KW=25;KB=95;TT={};ND=0;NL=60000;T0=0;GH={};KL={};HI={}
class TO(Exception):pass
def A(q,s):
 if B[q-9*s]==s or B[q-11*s]==s:return 1
 for o in N:
  if B[q+o]==s*2:return 1
 for o in K:
  if B[q+o]==s*6:return 1
 for o in D[:4]:
  t=q+o
  while B[t]==0:t+=o
  if B[t]==s*3 or B[t]==s*5:return 1
 for o in D[4:]:
  t=q+o
  while B[t]==0:t+=o
  if B[t]==s*4 or B[t]==s*5:return 1
 return 0
def G(s,ca,ep):
 m=[]
 for i in range(21,99):
  p=B[i]
  if p==7 or p*s<=0:continue
  a=p if p>0 else -p
  if a==1:
   d=10*s;t=i+d
   if B[t]==0:
    if t>90 or t<30:
     for q in(5,4,3,2):m.append(i+t*120+q*14400)
    else:
     m.append(i+t*120)
     if 30<i<39 and s>0 or 80<i<89 and s<0:
      if B[i+2*d]==0:m.append(i+(i+2*d)*120)
   for t in(i+d-1,i+d+1):
    if B[t]*s<0 and B[t]<7:
     if t>90 or t<30:
      for q in(5,4,3,2):m.append(i+t*120+q*14400)
     else:m.append(i+t*120)
    elif t==ep:m.append(i+t*120)
  elif a==2 or a==6:
   for o in(N if a==2 else K):
    t=i+o
    if B[t]==0 or B[t]*s<0 and B[t]<7:m.append(i+t*120)
   if a==6:
    for ks,bt,es,tg in CS:
     if i==ks and ca&bt and all(B[x]==0 for x in es) and not A(ks,-s) and not A(es[0],-s) and not A(tg,-s):m.append(i+tg*120)
  else:
   ds=D[:4] if a==3 else D[4:] if a==4 else D
   for o in ds:
    t=i+o
    while B[t]==0:
     m.append(i+t*120);t+=o
    if B[t]*s<0 and B[t]<7:m.append(i+t*120)
 return m
def mk(m,s,ca,ep):
 global KW,KB
 f=m%120;t=(m//120)%120;p=m//14400
 v=B[f];w=B[t];cs=0;cp=0;rf=0;rt=0
 if abs(v)==1 and t==ep and w==0:
  cs=t-10*s;cp=B[cs];B[cs]=0
 if abs(v)==6 and t-f in(2,-2):
  rf=f+3 if t>f else f-4;rt=f+1 if t>f else f-1;B[rt]=B[rf];B[rf]=0
 B[t]=p*s if p else v;B[f]=0
 if abs(v)==6:
  if s>0:KW=t
  else:KB=t
 c=ca
 if abs(v)==6:c=c&12 if s>0 else c&3
 if f==28 or t==28:c&=~1
 if f==21 or t==21:c&=~2
 if f==98 or t==98:c&=~4
 if f==91 or t==91:c&=~8
 e=f+10*s if abs(v)==1 and abs(t-f)==20 else -1
 return (f,t,v,w,cs,cp,rf,rt),c,e
def uk(m,u):
 global KW,KB
 f,t,v,w,cs,cp,rf,rt=u
 B[f]=v;B[t]=w
 if cs:B[cs]=cp
 if rf:B[rf]=B[rt];B[rt]=0
 if abs(v)==6:
  if v>0:KW=f
  else:KB=f
def E(s):
 mg=0;eg=0;ph=0;wb=0;bb=0;wk=0;bk=0;W=[0]*10;X=[0]*10
 for i in range(21,99):
  p=B[i]
  if not p or p==7:continue
  a=p if p>0 else -p
  x=M[i];y=x^56
  if p>0:
   mg+=MV[a-1]+T[(a-1)*64+y];eg+=WV[a-1]+T[(a+5)*64+y]
  else:
   mg-=MV[a-1]+T[(a-1)*64+x];eg-=WV[a-1]+T[(a+5)*64+x]
  ph+=PH[a-1]
  if a==3:
   if p>0:wb+=1
   else:bb+=1
  if a==1:
   if p>0:W[i%10]+=1
   else:X[i%10]+=1
   if i//10==8 and p>0:mg+=20
   if i//10==3 and p<0:mg-=20
  if a==2:
   if p>0:wk+=1
   else:bk+=1
   if p>0 and i//10>=6 and B[i+9]!=-1 and B[i+11]!=-1:mg+=12
   if p<0 and i//10<=5 and B[i-9]!=1 and B[i-11]!=1:mg-=12
  if a==3:
   if p>0 and i//10>=6 and B[i+9]!=-1 and B[i+11]!=-1:mg+=8
   if p<0 and i//10<=5 and B[i-9]!=1 and B[i-11]!=1:mg-=8
 if wb>1:mg+=8;eg+=12
 if bb>1:mg-=8;eg-=12
 np=sum(W)+sum(X)
 mg+=(wk-bk)*3 if np>11 else (wb-bb)*3 if np<7 else 0
 for f in range(1,9):
  if W[f]:
   if not W[f-1] and not W[f+1]:mg-=9
   if W[f]>1:mg-=7*(W[f]-1)
  if X[f]:
   if not X[f-1] and not X[f+1]:mg+=9
   if X[f]>1:mg+=7*(X[f]-1)
 for i in range(21,99):
  p=B[i]
  if abs(p)==4 and not W[i%10] and not X[i%10]:mg+=14 if p>0 else -14
  if p==4 and i//10==8:mg+=15
  if p==-4 and i//10==3:mg-=15
  if p==5 and i//10==8:mg+=12
  if p==-5 and i//10==3:mg-=12
 if ph>24:ph=24
 return (mg*ph+eg*(24-ph))//24*s
def S(s,d,a,be,ca,ep,h,pl,ph):
 global ND
 ND+=1
 if ND>NL:raise TO
 if ND&2047==0 and time.perf_counter()-T0>8:raise TO
 if h>=100:return 0
 k=(tuple(B),s,ca,ep)
 if k in ph:return 0
 if GH.get(k,0)>=2:return 0
 a=max(a,-100000+pl);be=min(be,100000-pl)
 if a>=be:return a
 if d<=0:
  ks=KW if s>0 else KB
  ic=A(ks,-s)
  if not ic:
   st=E(s)
   if st>=be:return be
   if st>a:a=st
   if pl>8:return st
  lm=0
  ph.add(k)
  for m in G(s,ca,ep):
   t=(m//120)%120;v=B[m%120]
   if not ic and not(B[t]*s<0 and B[t]<7 or m//14400 or t==ep and abs(v)==1):continue
   if not ic and B[t]*s<0 and not m//14400 and st+MV[abs(B[t])-1]<a:continue
   u,c2,e2=mk(m,s,ca,ep)
   if A(KW if s>0 else KB,-s):
    uk(m,u);continue
   lm=1
   sc=-S(-s,-1,-be,-a,c2,e2,0 if abs(u[2])==1 or u[3] or u[4] else h+1,pl+1,ph)
   uk(m,u)
   if sc>a:a=sc
   if a>=be:break
  ph.discard(k)
  if ic and not lm:return -100000+pl
  return a
 e=TT.get(k);bm=0
 if e and e[0]>=d:
  if e[2]==0:return e[1]
  if e[2]==1 and e[1]>=be:return e[1]
  if e[2]==2 and e[1]<=a:return e[1]
  bm=e[3]
 if d>=3 and not A(KW if s>0 else KB,-s) and any(B[i]*s>0 and 1<abs(B[i])<7 for i in range(21,99)):
  if -S(-s,d-3,-be,-be+1,ca,-1,h+1,pl+1,ph)>=be:return be
 ms=G(s,ca,ep)
 kl=KL.get(pl,(0,0))
 def os(m):
  t=(m//120)%120;w=B[t]
  return (m==bm)*10000+(m==kl[0])*4000+(m==kl[1])*3000+(w*s<0 and w<7)*(abs(w)*20-abs(B[m%120]))+(m//14400)*100+HI.get(m,0)//8
 ms.sort(key=os,reverse=True)
 ic=0;st=0
 if d==1:
  ic=A(KW if s>0 else KB,-s)
  st=E(s) if not ic else 0
  if not ic and st+250<a:return S(s,0,a,be,ca,ep,h,pl,ph)
 ph.add(k)
 best=-100000;fl=2;bv=0;fi=1;mi=0
 for m in ms:
  u,c2,e2=mk(m,s,ca,ep)
  if A(KW if s>0 else KB,-s):
   uk(m,u);continue
  mi+=1
  h2=0 if abs(u[2])==1 or u[3] or u[4] else h+1
  if d==1 and mi>1 and not ic and not(u[3] or u[4] or m//14400) and st+150<a:
   uk(m,u);continue
  ex=1 if A(KB if s>0 else KW,s) else 0
  dd=d-1+ex
  if fi:
   sc=-S(-s,dd,-be,-a,c2,e2,h2,pl+1,ph);fi=0
  else:
   r=1+(mi>8) if d>=3 and mi>3 and not(u[3] or u[4] or m//14400) else 0
   sc=-S(-s,dd-r,-a-1,-a,c2,e2,h2,pl+1,ph)
   if a<=sc<be:sc=-S(-s,dd,-be,-a,c2,e2,h2,pl+1,ph)
  uk(m,u)
  if sc>best:best=sc;bv=m
  if sc>a:a=sc;fl=0
  if a>=be:
   if not(u[3] or u[4] or m//14400):
    KL[pl]=[m,KL.get(pl,(0,0))[0]];HI[m]=HI.get(m,0)+d
   fl=1;break
 ph.discard(k)
 if best==-100000:
  if A(KW if s>0 else KB,-s):return -100000+pl
  return 0
 if len(TT)>50000:TT.clear()
 TT[k]=(d,best,fl,bv)
 return best
def parse(f):
 global B,KW,KB
 a=f.split();B=Y[:]
 r=9;c=1
 for ch in a[0]:
  if ch=='/':r-=1;c=1
  elif ch.isdigit():c+=int(ch)
  else:
   v='PNBRQK'.find(ch)+1 if ch.isupper() else -('pnbrqk'.find(ch)+1)
   B[r*10+c]=v
   if v==6:KW=r*10+c
   elif v==-6:KB=r*10+c
   c+=1
 s=1 if a[1]=='w' else -1
 ca=('K' in a[2])+('Q' in a[2])*2+('k' in a[2])*4+('q' in a[2])*8
 ep=-1 if a[3]=='-' else (int(a[3][1])+1)*10+ord(a[3][0])-96
 return s,ca,ep,int(a[4])
def U(u):
 f=(int(u[1])+1)*10+ord(u[0])-96
 t=(int(u[3])+1)*10+ord(u[2])-96
 return f+t*120+(5-'qrbn'.find(u[4]))*14400 if len(u)==5 else f+t*120
def I(m):
 f=m%120;t=(m//120)%120;p=m//14400
 u=chr(f%10+96)+str(f//10-1)+chr(t%10+96)+str(t//10-1)
 return u+'qrbn'[5-p] if p else u
def hist(ms):
 d={}
 s,ca,ep,h=parse('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
 kk=(tuple(B),s,ca,ep)
 d[kk]=1
 for u in ms:
  m=U(u)
  uu,ca,ep=mk(m,s,ca,ep)
  s=-s
  kk=(tuple(B),s,ca,ep)
  d[kk]=d.get(kk,0)+1
 return d
def RT(d,legal,s,ca,ep,h,al=-1000000,be=1000000):
 ph=set();k=(tuple(B),s,ca,ep);ph.add(k)
 rs=[];a=al;fi=1
 for u in legal:
  m=U(u)
  uu,c2,e2=mk(m,s,ca,ep)
  if A(KW if s>0 else KB,-s):
   uk(m,uu);rs.append((-10**9,u));continue
  h2=0 if abs(uu[2])==1 or uu[3] or uu[4] else h+1
  if fi:
   sc=-S(-s,d-1,-be,-al,c2,e2,h2,1,ph);fi=0
  else:
   sc=-S(-s,d-1,-a-1,-a,c2,e2,h2,1,ph)
   if sc>=a:sc=-S(-s,d-1,-1000000,1000000,c2,e2,h2,1,ph)
  uk(m,uu)
  rs.append((sc,u))
  if sc>a:a=sc
 ph.discard(k)
 rs.sort(reverse=True)
 return [u for sc,u in rs],a
def CH(legal,s,ca,ep,h):
 global ND,T0
 ND=0;T0=time.perf_counter()
 rk=legal[:];ps=0;fi=1
 for d in range(1,9):
  try:
   if fi:
    rk,ps=RT(d,legal,s,ca,ep,h);fi=0
   else:
    rk,ns=RT(d,legal,s,ca,ep,h,ps-25,ps+25)
    if ns<=ps-25 or ns>=ps+25:
     rk,ns=RT(d,legal,s,ca,ep,h)
    ps=ns
  except TO:break
 return rk
while True:
 g=P('/game',{})
 if not g or g.get('status')=='done':break
 while g.get('status')=='your_move':
  s,ca,ep,h=parse(g['fen'])
  GH=hist(g['moves'])
  s,ca,ep,h=parse(g['fen'])
  rk=CH(g['legal_moves'],s,ca,ep,h) if len(g['legal_moves'])>1 else g['legal_moves']
  ok=0
  for mv in rk:
   r=P('/move',{'game':g['game'],'move':mv})
   if r and r.get('status') in('your_move','over'):
    g=r;ok=1;break
  if not ok:sys.exit(1)
