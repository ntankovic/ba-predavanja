"""Fictional commit history for the BA orientation deck, adapted from the RS lecture 00 visual."""
from pathlib import Path
from html import escape
import subprocess
D=Path(__file__).resolve().parent
DARK='#18344b'; LINE='#d4e3ec'
def svg(name,body,w,h):
 p=D/(name+'.svg');p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'+body+'</svg>')
 subprocess.run(['rsvg-convert','-f','pdf','-o',str(p.with_suffix('.pdf')),str(p)],check=True)
def t(x,y,v,size=22,color=DARK,weight=400,anchor='start'):
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(v)}</text>'

# Dates illustrate a few commits a week over three weeks; names and hashes are invented.
body=f'<rect x="1" y="1" width="1038" height="358" rx="16" fill="#fff" stroke="{LINE}"/><path d="M1 55 H1039" stroke="{LINE}"/>'
body+=t(24,36,'projekt / Povijest commitova',24,weight=700)+t(1016,36,'Ilustrativni primjer · nekoliko commitova tjedno, 3 tjedna',18,'#637585',anchor='end')
rows=[('Ana','A','Dodaje prikaz radova','3. 11.','a31f902','#dceef9'),
 ('Marko','M','Dodaje zapis u ugovor','5. 11.','b62e140','#e3f2e8'),
 ('Iva','I','Testira ovlasti za izmjenu','10. 11.','c83a215','#f1e8fa'),
 ('Ana','A','Ispravlja prikaz praznog popisa','12. 11.','d94b326','#dceef9'),
 ('Marko','M','Sprječava dupli zapis','17. 11.','e15c437','#e3f2e8'),
 ('Ana','A','Dodaje poruku o pogrešci','20. 11.','f26d548','#dceef9')]
for i,(name,initial,msg,date,sha,color) in enumerate(rows):
 y=83+i*44
 body+=f'<circle cx="38" cy="{y-6}" r="15" fill="{color}"/>'+t(38,y,initial,16,weight=700,anchor='middle')+t(65,y,name,18,weight=700)+t(140,y,msg,18)+t(520,y,date,16,'#637585')+t(590,y,sha,16,'#637585')
body+=f'<path d="M681 71 V333" stroke="{LINE}"/>'+t(711,91,'Commitovi po autoru',20,weight=700)
for i,(name,count,color) in enumerate([('Ana',3,'#3886ad'),('Marko',2,'#58a074'),('Iva',1,'#9d7abe')]):
 y=132+i*65
 body+=t(711,y,name,20)+t(1001,y,str(count),20,weight=700,anchor='end')+f'<rect x="711" y="{y+10}" width="290" height="10" rx="5" fill="#edf2f6"/><rect x="711" y="{y+10}" width="{count*90}" height="10" rx="5" fill="{color}"/>'
svg('github-history.hr',body,1040,360)

# Simple line icons for the three project types; original drawings in the deck's accent colour.
S='fill="none" stroke="#3886ad" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
BG='<rect x="2" y="2" width="96" height="96" rx="20" fill="#e4eff7"/>'
svg('project-app',BG+f'<rect x="18" y="24" width="64" height="46" rx="6" {S}/><path d="M40 82 H60 M50 70 V82" {S}/><path d="M30 40 H54 M30 52 H46" {S}/><circle cx="66" cy="47" r="7" {S}/>',100,100)
svg('project-contract',BG+f'<path d="M28 14 H60 L74 28 V86 H28 Z" {S}/><path d="M60 14 V28 H74" {S}/><path d="M38 44 H64 M38 56 H58" {S}/><path d="M38 72 L45 78 L60 66" {S}/>',100,100)
svg('project-chain',BG+f'<rect x="10" y="38" width="22" height="24" rx="5" {S}/><rect x="39" y="38" width="22" height="24" rx="5" {S}/><rect x="68" y="38" width="22" height="24" rx="5" {S}/><path d="M32 50 H39 M61 50 H68" {S}/>',100,100)

# Simplified lettermark identifiers where Simple Icons has no glyph; not official logo files.
def mark(name,label,bg,fg='#fff',size=40):
 svg(f'tech/{name}',f'<rect x="4" y="4" width="92" height="92" rx="20" fill="{bg}"/>'+t(50,50+size*.35,label,size,fg,700,'middle'),100,100)
mark('viem','viem','#1e1e20',size=30)
mark('foundry','F','#2b2b2b','#f0b33a',54)
