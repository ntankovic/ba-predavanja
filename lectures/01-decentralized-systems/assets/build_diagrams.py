"""Original editable BA 01 illustrations, exported to SVG and vector PDF."""
from pathlib import Path
import sys,json,subprocess,re
from html import escape
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/'scripts'))
from diagram_style import box,state_box,cut,pill,panel,text,arrow,markers,BLUE,RED,INK
from version_chips import chips,measure
P=Path(__file__).parent

def line(x,y,x2,y2,color=BLUE,dash=False):
 return f'<path d="M{x},{y} L{x2},{y2}" stroke="{color}" stroke-width="2" fill="none"'+(' stroke-dasharray="6 6"' if dash else '')+'/>'
def wraptext(x,y,value,size=22,width=28,color='#20384d'):
 import textwrap
 return ''.join(text(x,y+i*(size+7),v,size,color) for i,v in enumerate(textwrap.wrap(value,width=width,break_long_words=False)))
def figcaption(x,y,value,width=100):
 # Figure captions read as a quiet note under the figure, not a second heading (lecturer, 2026-11-04).
 return wraptext(x,y,value,19,width,'#5d7282').replace('<text ','<text font-style="italic" ')
def card(x,y,w,h,node):
 title,sub=node.split('|',1)
 result=box(x,y,w,h,title,sub)
 return result.replace('font-size="25"', 'font-size="22"') if title=='Obračun i poravnanje' else result
def danger(svg):
 svg=svg.replace('fill="#f8fbfd" stroke="#c6dbe8"','fill="#fdf1f2" stroke="#e3a9ae"').replace(f'fill="{BLUE}"/>',f'fill="{RED}"/>')
 return svg.replace('fill="#20384d">','fill="'+RED+'">',1)
AMBER,AMBER_FILL,AMBER_LINE,AMBER_INK='#bc8439','#fff6ea','#ebcf9f','#8a5a1c'
def tag(x,y,label,color='#6b7f8e'):
 return text(x,y,label,14,color,700)
def state(x,y,w,h,node):
 # States have their own shape, distinct from node cards (lecturer, 2026-10-29).
 title,sub=node.split('|',1)
 return state_box(x,y,w,h,title,sub)
def tx(cx,cy,w,title,sub):
 # Transactions are amber pills on the edge between two states.
 return (tag(cx,cy-44,'TRANSAKCIJA',AMBER)+f'<rect x="{cx-w/2}" y="{cy-32}" width="{w}" height="64" rx="32" fill="{AMBER_FILL}" stroke="{AMBER_LINE}" stroke-width="1.6"/>'
         +text(cx,cy-4,title,20,AMBER_INK,700)+text(cx,cy+20,sub,16,AMBER_INK))
def edge(x,y,x2,y2,head=False):
 r=f'<path d="M{x},{y} L{x2},{y2}" stroke="{AMBER}" stroke-width="3.2" fill="none" stroke-linecap="round"/>'
 if head:r+=f'<path d="M{x2-14},{y2-8} L{x2+2},{y2} L{x2-14},{y2+8} Z" fill="{AMBER}"/>'
 return r
def vedge(x,y,x2,y2):
 # Vertical amber connector with a downward head.
 return (f'<path d="M{x},{y} L{x2},{y2-8}" stroke="{AMBER}" stroke-width="3.2" fill="none" stroke-linecap="round"/>'
         f'<path d="M{x2-8},{y2-12} L{x2},{y2+2} L{x2+8},{y2-12} Z" fill="{AMBER}"/>')
def background(x,y,w,h,label,color=BLUE):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="7 5"/>'+text(x+w/2,y+28,label,20,color)
def steps3(nodes,y=40,w=290,h=64,numbered=True,arrows=True):
 # Three steps or concepts in a row: pills with the description below, not node cards (lecturer, 2026-10-29).
 r=''
 for i,(x,node) in enumerate(zip([20,375,730],nodes)):
  title,sub=node.split('|',1)
  r+=pill(x,y,w,h,title,'',i+1 if numbered else None)+wraptext(x+w/2,y+h+34,sub,19,30,'#536b7b')
 if arrows:r+=arrow(316,y+h/2,369,y+h/2)+arrow(671,y+h/2,724,y+h/2)
 return r
def three(nodes,y=45,w=290,h=145):
 return ''.join(card(x,y,w,h,n) for x,n in zip([20,375,730],nodes))
for fig in json.loads((P/'figures.json').read_text()):
 mode=fig['mode'];n=fig['nodes'];s='';height=315
 if mode=='transaction':
  height=350
  s=background(5,5,1030,260,'BEGIN → transakcija s zaključavanjem')+steps3(n,y=85)
 elif mode=='timeout':
  height=340
  s=text(190,25,'Klijent',25,weight=600)+text(840,25,'Koordinator',25,weight=600)
  s+=line(190,45,190,270)+line(840,45,840,270)
  s+=arrow(200,85,830,85,'1. zahtjev tx1')+text(840,133,'2. F:20 · X:80 · v8',20)
  s+=arrow(830,165,480,165,'3. odgovor',color=RED,dash=True)
  s+=cut(440,165)+text(190,245,'4. timeout',22,RED)
 elif mode=='transition':
  # One transaction moves the system from one state to the next.
  height=270
  a,t1,b=n;tt,ts=t1.split('|',1)
  s=state(20,60,250,130,a)+state(770,60,250,130,b)
  s+=edge(272,125,330,125)+tx(520,125,380,tt,ts)+edge(710,125,764,125,True)
 elif mode=='branch':
  # Two transactions from the same state lead to two incompatible next states.
  height=425
  a,t1,t2,b1,b2=n
  s=state(20,130,240,130,a)+state(790,40,230,120,b1)+state(790,245,230,120,b2)
  s+=edge(262,195,320,195)+edge(320,100,320,305)
  for y,t in [(100,t1),(305,t2)]:
   tt,ts=t.split('|',1);s+=edge(320,y,355,y)+tx(560,y,400,tt,ts)+edge(760,y,784,y,True)
 elif mode in ['fork','equivocation']:
  height=385  # keeps the caption clear of the lower card
  left=n[0] if mode=='fork' else 'Čvor A|Jedan od tri člana'
  right=n[1:] if mode=='fork' else n[:2]
  s=card(20,90,300,145,left)
  if mode=='equivocation':
   # The two right-hand items are messages, so they are pills (lecturer, 2026-10-29).
   for yy,m in [(40,right[0]),(205,right[1])]:
    tt,ts=m.split('|',1);s+=pill(660,yy,350,90,tt,ts)
  else:s+=card(660,15,350,140,right[0])+card(660,180,350,140,right[1])
  s+=line(330,160,450,160)+line(450,85,450,250)
  s+=arrow(450,85,645,85,'tx1')+arrow(450,250,645,250,'tx2',color=RED)
 elif mode=='race':
  # Two requests interleave: both checks pass before either debit (slide „Naivan kod”, lecturer 2026-10-27).
  height=400
  s=text(55,85,'tx1 · B',22,weight=600)+text(55,232,'tx2 · C',22,weight=600)
  for i,node in enumerate(n):
   x=120+i*228;y=15 if i%2==0 else 162
   tt,ts=node.split('|',1)
   s+=pill(x,y+20,212,86,tt,ts,tone='red' if i==len(n)-1 else 'blue')
   s+=text(x+106,335,str(i+1)+'.',20,'#6b7f8e',600)
  s+=arrow(120,307,1025,307,color='#6b7f8e')+text(1000,335,'vrijeme',18,'#6b7f8e')
 elif mode=='staleread':
  # Cards stay nodes; the reader and the interface choices get their own shapes (lecturer, 2026-10-27).
  height=440
  s=card(40,20,320,125,n[0])+card(680,20,320,125,n[1])
  s+=arrow(370,82,670,82,'promjena v8 još putuje',dash=True)
  s+=f'<rect x="700" y="195" width="280" height="50" rx="25" fill="#ffffff" stroke="#9fb3c2" stroke-width="1.6"/>'+text(840,227,'Korisnik B osvježi prikaz',20,weight=600)
  s+=arrow(840,190,840,152)
  s+=text(520,290,n[2],20,'#536b7b')
  for x,label in [(40,n[3]),(540,n[4])]:
   s+=f'<rect x="{x}" y="310" width="460" height="54" rx="27" fill="#f3f8fb" stroke="#c6dbe8" stroke-width="1.4"/>'+text(x+230,344,label,20,weight=600)
 elif mode=='chain':
  # Abstract notation: ledger = ordered list of transactions; state Sn = result of applying them in order (lecturer, 2026-10-28).
  height=355
  s=text(520,26,'LEDGER: lista transakcija, redom',15,AMBER,700)
  txs=fig['txs']
  for i,t in enumerate(txs):
   tt,ts=t.split('|',1)
   cx=130+i*260
   s+=f'<rect x="{cx-118}" y="40" width="236" height="56" rx="28" fill="{AMBER_FILL}" stroke="{AMBER_LINE}" stroke-width="1.6"/>'+text(cx,64,tt,18,AMBER_INK,700)+text(cx,86,ts,15,AMBER_INK)
  s+=text(520,150,'STANJA: rezultat primjene transakcija',15,BLUE,700)
  w,gap,x0=160,55,10
  for i,node in enumerate(n):
   x=x0+i*(w+gap)
   s+=state(x,170,w,110,node)
   if i<len(n)-1:
    xa=x+w+4; xb=x+w+gap-4
    s+=edge(xa,225,xb,225,True)+text((xa+xb)/2,212,txs[i].split(':',1)[0],15,AMBER_INK,700)
 elif mode=='orgs':
  # Members and the shared budget only; the protocol appears later, on the rule slide (lecturer, 2026-10-28).
  height=400
  for x,node,end in zip([20,375,730],n[:3],[430,520,610]):
   s+=card(x,20,290,110,node)+line(x+145,132,end,229,'#9fb3c2')
  s+=state(370,230,300,105,n[3])
 elif mode=='budget':
  # Start state -> protocol -> next state; proposals enter the protocol from above, only one passes (lecturer, 2026-10-28).
  height=420
  s=card(20,15,230,95,n[0])+card(300,15,170,95,n[1])+card(570,15,170,95,n[2])
  for cx,t in zip([385,655],fig['txs']):
   tt,ts=t.split('|',1)
   s+=vedge(cx,112,cx,128)+re.sub(r'<text[^>]*>TRANSAKCIJA</text>','',tx(cx,168,230,tt,ts))+vedge(cx,202,cx,226)
  s+=f'<rect x="300" y="230" width="470" height="100" rx="16" fill="#f5f3fa" stroke="#7770a5" stroke-width="2" stroke-dasharray="7 5"/>'
  s+=text(535,262,'PROTOKOL',15,'#7770a5',700)+text(535,298,'provjeri pokriće u v7 · pusti samo jednu',19,INK,600)
  s+=state(20,232,230,96,n[3])+arrow(254,280,296,280)
  s+=arrow(774,280,806,280)+state(810,232,210,96,n[4])
  s+=text(535,356,'druga isplata: odbijena',17,RED,600)
 elif mode=='replicas':
  height=395;s=card(20,85,300,150,n[0])+card(685,10,330,140,n[1])+card(685,175,330,140,n[2])
  s+=line(330,160,485,160)+line(485,80,485,245)+arrow(485,80,670,80,'promjena v8')+arrow(485,245,670,245,'promjena v8')
 elif mode=='peers':
  height=350;s=three(n,y=100)
  s+=arrow(325,160,360,160)+arrow(360,205,325,205)+arrow(680,160,715,160)+arrow(715,205,680,205)+line(165,85,165,50)+line(165,50,875,50)+arrow(875,50,875,85)
  s+=text(520,37,'Traženje i pružanje podataka',22)
 elif mode in ['control','independent']:
  height=330
  if mode=='control':s=background(5,5,1030,265,'Jedan operator X')
  else:
   for x in [5,360,715]:s+=background(x,5,320,265,'Neovisno upravljanje')
  s+=three(n,y=75)
 elif mode=='partition':
  height=330
  if fig.get('layout')=='three-nodes':
   # Three separate node cards; only links that cross the partition are cut (lecturer, 2026-10-28).
   height=360
   s=background(15,10,575,290,'strana 1: A i B komuniciraju')+background(705,10,320,290,'strana 2: C je odvojen',RED)
   s+=card(50,80,215,115,n[0])+card(335,80,215,115,n[1])+card(760,80,215,115,n[2])
   s+=f'<path d="M265,137 L335,137" stroke="{BLUE}" stroke-width="3.2"/>'
   s+=f'<path d="M550,137 L760,137" stroke="{RED}" stroke-width="2.6" stroke-dasharray="7 6" fill="none"/>'+cut(647,137)
   s+=f'<path d="M157,195 L157,250 L867,250 L867,195" stroke="{RED}" stroke-width="2.6" stroke-dasharray="7 6" fill="none"/>'+cut(647,250)
  else:
   s=three(n,y=65)+line(325,140,355,140,RED,True)+cut(340,140,13)+arrow(685,140,715,140)
 elif mode=='triangle':
  # Triangle of nodes: every node is up, only link A–B is cut (lecturer, 2026-10-21).
  height=395
  s+=f'<path d="M430,110 L250,210" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" fill="none"/>'+cut(340,160,17)
  s+=f'<path d="M610,110 L790,210" stroke="{BLUE}" stroke-width="3" fill="none"/>'+f'<path d="M310,262 L730,262" stroke="{BLUE}" stroke-width="3" fill="none"/>'
  s+=card(390,10,260,100,n[0])+card(50,212,260,100,n[1])+card(730,212,260,100,n[2])
 elif mode=='split-history':
  # Each side of the partition runs its own state chain; nodes are round badges, not cards (lecturer, 2026-10-28).
  height=440
  rows=fig['rows']
  for i,r in enumerate(rows):
   y0=12+i*190; col=BLUE if i==0 else RED
   s+=background(10,y0,740,175,'',col)
   s+=text(70,y0+30,r['side'],16,col,700)
   for k,nd in enumerate(r['nodes']):
    cy=y0+72+k*52 if len(r['nodes'])>1 else y0+98
    s+=f'<circle cx="70" cy="{cy}" r="20" fill="#f8fbfd" stroke="{col}" stroke-width="2.2"/>'+text(70,cy+7,nd,18,col,700)
   cy=y0+100
   s+=state(130,cy-45,170,90,r['from'])+edge(302,cy,330,cy)
   tt,ts=r['tx'].split('|',1)
   s+=re.sub(r'<text[^>]*>TRANSAKCIJA</text>','',tx(440,cy,220,tt,ts))+edge(550,cy,566,cy,True)
   s+=state(572,cy-45,165,90,r['to'])
   s+=f'<path d="M739,{cy} L800,{cy} L800,220 L812,220" stroke="{RED}" stroke-width="2.6" fill="none" stroke-dasharray="7 5"/>'
  s+=f'<rect x="815" y="170" width="215" height="100" rx="50" fill="#fbeaec" stroke="#e3a5ad" stroke-width="1.6"/>'
  s+=text(922,212,fig['merge'][0],20,RED,700)+text(922,240,fig['merge'][1],17,RED,600)
 elif mode in ['compare','conflict']:
  # Two cases side by side are open panels; 'danger' marks the right one as the hostile case (lecturer, 2026-10-21/29).
  height=340;s=''
  for x,node,col in [(30,n[0],BLUE),(550,n[1],RED if fig.get('danger') else BLUE)]:
   tt,ts=node.split('|',1);s+=panel(x,20,460,165,tt,ts,col)
  # Both cases lead into one conclusion box (lecturer, 2026-11-04).
  title,sub=n[2].split('|',1)
  s+=f'<path d="M260,190 L260,206 L330,206" stroke="#9fb3c2" stroke-width="2" fill="none"/>'
  s+=f'<path d="M780,190 L780,206 L710,206" stroke="#9fb3c2" stroke-width="2" fill="none"/>'
  s+='<rect x="190" y="204" width="660" height="58" rx="29" fill="#f2f6f9" stroke="#b9cbd7" stroke-width="1.5"/>'
  s+=(f'<text x="520" y="241" text-anchor="middle" font-family="Arial, sans-serif" font-size="21" fill="{INK}">'
      f'<tspan font-weight="700">{escape(title)}:</tspan> {escape(sub)}</text>')
 elif mode=='votes':
  height=345
  s=f'<ellipse cx="385" cy="145" rx="185" ry="105" fill="#e7f3fb" stroke="{BLUE}" stroke-width="2"/><ellipse cx="655" cy="145" rx="185" ry="105" fill="#fff2df" fill-opacity=".75" stroke="{RED}" stroke-width="2"/>'
  s+=text(330,153,'B',34,BLUE,600)+text(520,153,'A',34,RED,600)+text(710,153,'C',34,BLUE,600)
  s+=text(265,280,'tx1: potvrde A + B',24)+text(775,280,'tx2: potvrde A + C',24)+text(520,25,'A potvrđuje oba prijedloga',23,RED,600)
 elif mode=='membership':
  height=330;s=background(10,10,400,235,'Jedna organizacija A')
  for i in range(3):
   x=25+i*125
   s+=f'<rect x="{x}" y="65" width="115" height="130" rx="12" fill="#f3f8fb" stroke="#c6dbe8"/>'+text(x+57.5,137,'Proces '+str(i+1),18,weight=600)
  s+=card(455,60,260,150,n[1])+card(755,60,260,150,n[2])
 elif mode in ['axes','permissions','recap','review']:
  height=340
  colors=[BLUE,'#7770a5','#b38337']
  for i,node in enumerate(n):
   title,sub=node.split('|',1);y=15+i*90
   s+=f'<rect x="25" y="{y}" width="990" height="75" rx="12" fill="#f3f8fb"/>'+f'<rect x="25" y="{y}" width="7" height="75" fill="{colors[i]}"/>'
   s+=text(245,y+45,title,24,colors[i],600)+text(715,y+45,sub,22)
 elif mode=='counter':
  # Recap rows: claim | counterexample | earlier slide that covered it (lecturer, 2026-10-21).
  height=400
  colors=[BLUE,'#7770a5','#b38337']
  for i,node in enumerate(n):
   title,sub,ref=node.split('|',2);y=15+i*112
   s+=f'<rect x="25" y="{y}" width="990" height="96" rx="12" fill="#f3f8fb"/>'+f'<rect x="25" y="{y}" width="7" height="96" fill="{colors[i]}"/>'
   s+=text(180,y+56,title,24,colors[i],600)+text(665,y+44,sub,21)+text(665,y+75,ref,16,'#6b7f8e')
 elif fig.get('shape')=='panel':
  # Facts and figures: open panels (lecturer, 2026-10-29).
  height=250
  for x,node in zip([20,375,730],n):
   tt,ts=node.split('|',1);s+=panel(x,15,290,175,tt,ts,BLUE,22)
 elif mode in ['steps','handoff','roles'] and fig.get('shape')!='node':
  height=250;s=steps3(n,numbered=mode!='roles',arrows=mode!='roles')
 else:
  s=three(n)
  if mode in ['central','states','steps','handoff']:
   s+=arrow(325,117,360,117)+arrow(680,117,715,117)
  elif mode=='claims':s+=text(520,235,'?',42,RED,600)
  elif mode=='activity':s+=text(520,235,'Zapisujte poruke, lokalno stanje i potvrde.',22)
  elif mode=='roles' and fig['name']=='figure-04':s+=text(520,235,'Članovi predlažu; o prihvaćanju odlučuje protokol: zajednička pravila koja svi moraju poštovati.',22)
 s+=figcaption(520,height-22,fig['caption'])
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{height}" viewBox="0 0 1040 {height}">'+markers()+f'<rect width="1040" height="{height}" fill="white"/>'+s+'</svg>'
 # Request IDs such as K42 are identifiers: monospace, as on the slides (lecturer, 2026-10-28). rsvg cannot see Menlo, so use Courier New.
 svg=re.sub(r'\bK42\b','<tspan font-family="Courier New, monospace">K42</tspan>',svg)
 path=P/(fig['name']+'.hr.svg');path.write_text(chips(svg))
 subprocess.run(['rsvg-convert','-f','pdf','-o',str(path.with_suffix('.pdf')),str(path)],check=True)
print('Exported',len(json.loads((P/'figures.json').read_text())),'SVG/PDF pairs')

# Case study replacing the paper workshop (lecturer, 2026-10-19): three runs as message sequence diagrams.
LANE={'A':180,'B':520,'C':860}
def seq(name,heads,msgs,ends,caption):
 s=''
 for k,x in LANE.items():
  # A (label, True) head marks a lane that deviates from the protocol (lecturer, 2026-10-27).
  label,bad=(heads[k],False) if isinstance(heads[k],str) else heads[k]
  fill,stroke,col=('#fbeaec','#e3a5ad',RED) if bad else ('#f8fbfd','#c6dbe8','#20384d')
  s+=f'<rect x="{x-110}" y="10" width="220" height="56" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'+text(x,46,label,21,col,600)
  s+=line(x,66,x,318,'#9fb3c2',True)
 y=105
 for m in msgs:
  if m[0]=='note':
   for k,label in zip(m[1::2],m[2::2]):
    x=LANE[k]
    w=max(300,measure(label,16,True)+32)  # chips widen the label, so size the note to its rendered width
    s+=f'<rect x="{x-w/2:.1f}" y="{y-24}" width="{w:.1f}" height="36" rx="8" fill="#fff7ed" stroke="#e8c39e"/>'+text(x,y,label,16,'#7c3a0e',600)
  else:
   a,b,label,color,lost=m;x1,x2=LANE[a],LANE[b];d=1 if x2>x1 else -1
   if lost:
    xm=(x1+x2)/2
    s+=line(x1+d*6,y,xm,y,RED,True)+cut(xm,y,13)
    s+=text((x1+xm)/2,y-12,label,17,RED)
   else:
    lx=(x1+x2)/2 if abs(x2-x1)<400 else 690  # keep long-arrow labels off lane B
    s+=arrow(x1+d*6,y,x2-d*8,y,color=color)+text(lx,y-12,label,17,color)
  y+=46
 for k,(label,bad) in ends.items():
  x=LANE[k];fill,stroke,col=('#fbeaec','#e3a5ad',RED) if bad else ('#eef6fa','#9cc4da','#20384d')
  s+=f'<rect x="{x-140}" y="322" width="280" height="50" rx="12" fill="{fill}" stroke="{stroke}"/>'+text(x,354,label,19,col,600)
 s+=figcaption(520,410,caption)
 h=425
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{h}" viewBox="0 0 1040 {h}">'+markers()+f'<rect width="1040" height="{h}" fill="white"/>'+s+'</svg>'
 path=P/(name+'.hr.svg');path.write_text(chips(svg))
 subprocess.run(['rsvg-convert','-f','pdf','-o',str(path.with_suffix('.pdf')),str(path)],check=True)
H={'A':'A · koordinator','B':'B · predlaže tx1','C':'C · predlaže tx2'}
seq('case-1',H,[('B','A','tx1: 80 → X · v7',BLUE,False),('C','A','tx2: 60 → Y · v7',BLUE,False),
 ('note','A','prihvaća tx1, odbija tx2'),('A','B','tx1 prihvaćen · v8',BLUE,False),('A','C','tx2 odbijen; prihvaćen tx1, F:20 · v8',BLUE,False)],
 {'A':('F:20 · v8',False),'B':('F:20 · v8',False),'C':('F:20 · v8',False)},
 'Model 1: jedan koordinator, jedna prihvaćena isplata')
seq('case-2',H,[('B','A','tx1: 80 → X · v7',BLUE,False),('C','A','tx2: 60 → Y · v7',BLUE,False),
 ('note','A','prihvaća tx1, odbija tx2'),('A','B','tx1 prihvaćen · v8',RED,True),('A','C','tx2 odbijen; prihvaćen tx1, F:20 · v8',BLUE,False)],
 {'A':('F:20 · v8',False),'B':('F:100 · v7 · čeka?',True),'C':('F:20 · v8',False)},
 'Model 1 uz izgubljenu potvrdu: stanje je ispravno, ali B to ne zna')
H3={'A':('A · bizantski',True),'B':'B · predlaže tx1','C':'C · predlaže tx2'}
seq('case-3',H3,[('B','A','glasaj za tx1 · v7',BLUE,False),('C','A','glasaj za tx2 · v7',BLUE,False),
 ('A','B','DA za tx1',BLUE,False),('A','C','DA za tx2',RED,False),('note','B','B + A = 2 glasa → tx1 konačan','C','C + A = 2 glasa → tx2 konačan')],
 {'A':('rekao DA obojici',True),'B':('F:20 · tx1 konačan',True),'C':('F:40 · tx2 konačan',True)},
 'Model 2: pravilo „dva od tri” daje dvije konačne odluke, 140 iz 100')
