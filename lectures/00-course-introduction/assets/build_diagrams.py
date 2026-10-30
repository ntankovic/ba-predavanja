"""Editable orientation diagrams; BA teaching example and confirmed assessment rules."""
from pathlib import Path
import sys, subprocess
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/'scripts'))
from diagram_style import box, text, arrow, markers
OUT=Path(__file__).parent

def save(name,body,height):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{height}" viewBox="0 0 1040 {height}">'+markers()+f'<rect width="1040" height="{height}" fill="white"/>'+body+'</svg>'
 p=OUT/(name+'.hr.svg');p.write_text(svg)
 subprocess.run(['rsvg-convert','-f','pdf','-o',str(p.with_suffix('.pdf')),str(p)],check=True)

s=''
for x,title,sub in [(20,'Organizacija A','Vlastita evidencija'),(380,'Organizacija B','Vlastita evidencija'),(740,'Organizacija C','Vlastita evidencija')]:s+=box(x,35,280,145,title,sub)
s+=text(520,245,'Zajednički budžet: koje isplate svi prihvaćamo?',26,weight=600)
save('shared-record',s,280)
s=''
for x,title,sub in [(10,'Problem','Korisnici i njihove potrebe'),(275,'Arhitektura','Podaci i pravila'),(540,'Implementacija','Ugovor i aplikacija'),(805,'Provjera','Testovi i objašnjenje')]:
 s+=box(x,30,225,150,title,sub)
 if x<805:s+=arrow(x+230,105,x+255,105)
s+=text(520,235,'Nakon provjere doradite zahtjeve, odluke ili kod.',24)
save('project-path',s,270)
# A simplified flow retaining parallel work, a lecturer decision, two outcomes and retry.
s=box(10,10,245,90,'Projekt','Prijava teme i rad')+box(10,130,245,90,'Vježbe','Rad i ocjena')
s+=arrow(265,55,300,55)+arrow(265,175,300,175)
s+='<path d="M300,55 V175" stroke="#3886ad" stroke-width="3" fill="none"/>'
s+=arrow(300,115,335,115)+box(350,60,290,110,'Predaja i provjera','Projekt bez spornih dijelova')
s+=arrow(650,115,715,115)+box(735,60,290,110,'Prijava ispita','Na oba puta polaganja')
s+=arrow(880,185,880,235)
s+=box(680,250,345,90,'Odluka nastavnika','Uvjeti za oslobođenje od usmenog')
s+=arrow(665,295,570,295,'DA')+box(255,250,295,90,'Bez usmenog','Prosjek ocjena → unos u ISVU')
s+=arrow(850,350,850,385)+text(890,376,'NE',19)+box(680,400,345,90,'Obrana i usmeni','Ocjena usmenog je konačna')
s+=arrow(665,445,570,445)+box(255,400,295,90,'Ishod','Pozitivno: unos ocjene u ISVU')
s+=text(515,535,'Negativan ishod → ponovna prijava ispitnog roka.',23)
save('assessment-flow',s,560)

# BA adaptation of WA request/evidence/change orientation layouts.
for name,nodes,caption in [
 ('course-focus',[('Korisnik','Predlaže radnju'),('Ugovor','Provjerava pravila'),('Mreža','Prihvaća zajedničko stanje')],'Kod, stanje i dogovor sudionika'),
 ('ba-evidence',[('Predvidi','Očekivani rezultat'),('Pokaži','Sučelje, ugovor i stanje'),('Objasni','Zašto je prihvaćeno ili odbijeno')],'Povežite očekivanje, kod i opaženo ponašanje'),
]:
 s=''
 for x,(title,sub) in zip([20,375,730],nodes):s+=box(x,35,290,150,title,sub)
 s+=arrow(325,110,360,110)+arrow(680,110,715,110)+text(520,245,caption,24)
 save(name,s,280)
# Explaining a change on one's own code replaces a live code change (RS, confirmed for BA 2026-10-13).
s=''
for x,(title,sub) in zip([20,375,730],[('Gdje?','Ugovor, sučelje, pohrana'),('Kako?','Koraci izmjene'),('Posljedice?','Stanje, ovlasti, testiranje')]):s+=box(x,12,290,130,title,sub)
s+=arrow(325,77,360,77)+arrow(680,77,715,77)+text(520,190,'Slijeva nadesno: objašnjenje dorade na vlastitom kodu, uz potpitanja nastavnika.',20,'#536b7b')
save('design-change',s,210)

# "Do you need a blockchain?" after Wüst & Gervais (2018), Fig. 1, reworked by the lecturer (2026-10-20).
def outcome(x,y,w,h,lines,chain):
 fill,line='#dfedf5','#9cc4da' if chain else ('#f0f1f3','#d3d8dd')
 if chain: fill,line='#dfedf5','#9cc4da'
 else: fill,line='#f0f1f3','#d3d8dd'
 r=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{line}" stroke-width="1.2"/>'
 for i,l in enumerate(lines):r+=text(x+w/2,y+h/2+7-(len(lines)-1)*12+i*24,l,19,'#20384d',600 if chain else 400)
 return r
# Each step is a group; the inline copy marks groups as Reveal fragments so boxes appear one by one.
# Split over two slides (lecturer, 2026-10-14): 1) sharing, mutual trust; 2) intermediary, known parties.
import re
def chip(cx,cy,lab):
 fill='#3886ad' if lab=='DA' else '#c2410c'
 return (f'<rect x="{cx-17}" y="{cy-11}" width="34" height="22" rx="11" fill="{fill}"/>'
         f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="700" fill="#fff">{lab}</text>')
def ital(v): return re.sub(r'<text ([^>]*)>([Bb]lockchain)</text>',r'<text \1 font-style="italic">\2</text>',v)
def emit(name,groups,h,label):
 groups=[ital(g) for g in groups]
 save(name,''.join(groups),h)
 body=''.join(f'<g class="fragment">{g}</g>' if k else f'<g>{g}</g>' for k,g in enumerate(groups))
 svg_inline=f'<svg class="need-blockchain" xmlns="http://www.w3.org/2000/svg" width="1040" height="{h}" viewBox="0 0 1040 {h}" role="img" aria-label="{label}">'+markers()+body+'</svg>'
 (OUT/f'_{name}.hr.qmd').write_text('```{=html}\n'+svg_inline+'\n```\n')
W,QH,QY=250,150,10
def q(x,t,sub): return box(x,QY,W,QH,t,sub)
def down(x,lab,lines,chain): return arrow(x+W/2,QY+QH+3,x+W/2,QY+QH+42)+chip(x+W/2+32,QY+QH+22,lab)+outcome(x,QY+QH+47,W,84,lines,chain)
def right(x1,x2,lab): return arrow(x1+2,QY+QH/2,x2-3,QY+QH/2)+chip((x1+x2)/2,QY+QH/2-24,lab)
# Part 1
# Lecturer's tree (2026-10-20): sharing → mutual trust → one trusted party → known parties.
xs=[10,395]
g=[q(xs[0],'Dijeljenje','Treba li sustav čuvati stanje za više dionika?'),
   down(xs[0],'NE',['SQLite ili','datoteka'],False),
   right(xs[0]+W,xs[1],'DA')+q(xs[1],'Povjerenje','Vjeruju li si svi dionici međusobno?'),
   down(xs[1],'DA',['Baza kod','bilo koga'],False),
   right(xs[1]+W,780,'NE')+outcome(780,QY+QH/2-42,150,84,['Dalje','→'],True)]
emit('need-blockchain-1',g,300,'Stablo odluke, prvi dio: dijeljenje, međusobno povjerenje')
# Part 2
g=[outcome(10,QY+QH/2-42,150,84,['Nema','povjerenja'],False),
   arrow(162,QY+QH/2,227,QY+QH/2)+q(230,'Posrednik','Vjeruju li svi barem jednom dioniku?'),
   down(230,'DA',['Baza kod','njega'],False),
   right(230+W,550,'NE')+q(550,'Poznati','Poznaju li se svi dionici?'),
   down(550,'DA',['Privatni','blockchain'],True),
   right(550+W,860,'NE')+outcome(860,QY+QH/2-42,170,84,['Javni','blockchain'],True)]
emit('need-blockchain-2',g,300,'Stablo odluke, drugi dio: posrednik i poznati dionici')
