# Pregled hrvatskog nacrta 01 — 2026-10-08

## Provjereno

- [x] Cjelovita hrvatska skripta prethodi izvedenim slajdovima; bilješke sadrže objašnjenja i pitanja za nastavnika.
- [x] Pet ishoda; 40 ukupnih slajdova, od kojih 37 sadržajnih (bez naslova, ishoda i literature).
- [x] 117 minuta; 40 uzastopnih intervala u `timing.json`, usklađenih s bilješkama.
- [x] Primjer digitalnog budžeta postupno prolazi kroz koordinatora, konkurentne promjene, replike, gubitak potvrde, razdvajanje mreže i neovisno upravljanje.
- [x] Razlikuju se raspodijeljenost, decentralizacija i P2P; model članstva, vremena, autentifikacije i ispada prethodi jamstvima.
- [x] Provjeren trag konkurentnih isplata 80 i 60 iz salda 100 i verzije 7 i ponavljanje istog identifikatora bez dodatne promjene stanja. Preklapanje skupova glasova A+B i A+C ne daje ispravnog zajedničkog glasača ako A odstupa.
- [x] Nema ranog tehničkog uvoda u Bitcoin/IPFS, univerzalne tvrdnje o nemogućnosti konsenzusa ili tvrdnje da potpis bira povijest.
- [x] Primarni izvori provjereni i evidentirani, uključujući puni Harvardov PDF. Stari BA-01 evidentiran kao nastavni predložak.
- [x] 32 originalna izmjenjiva dijagrama s SVG/PDF parovima i alternativnim tekstom (80% slajdova).
- [x] `just slides 01-decentralized-systems hr` i `just lecture 01-decentralized-systems hr` uspješni. Koristi se privremeni Quarto launcher preko `QUARTO_BIN`, opisan u radnoj sesiji; standardno je dovoljan instalirani Quarto.
- [x] Pregledani PDF dijagrami i stranice skripte kroz rasterizirane kontaktne listove. Nisu uočeni odrezani dijagrami ili tekst izvan stranice.
- [x] Registar, brief, izvori, ilustracije i metapodaci usklađeni s hrvatskim nacrtom; engleski predlošci ostaju planned.

## Otvoreno prije statusa ready

- [ ] Vizualni HTML pregled svih slajdova i provjera preljeva: `just browser-check 01-decentralized-systems hr` pokušan, ali headless Chrome završava SIGTRAP pri pokretanju, prije učitavanja prezentacije. macOS javlja `bootstrap_check_in ... MachPortRendezvousServer: Permission denied (1100)`. Ovo nije prolazna provjera sadržaja niti dokaz da HTML nema preljeva. Nije korištena desktop automatizacija.
- [ ] Nastavnikov pregled hrvatskog teksta, primjera i tempa; terminologija koja nije potvrđena ostaje prijedlog.
- [ ] Prijevod i pregled engleskog nakon prihvaćanja hrvatske verzije.

## Promijenjeni materijali

U direktoriju 01: `chapter.hr.qmd`, `slides.hr.qmd`, `lecture.json`, `timing.json`, `README.md`, `sources.md`, `illustrations.md`, ovaj pregled te `assets/` (CSS, generator, specifikacija i 32 SVG/PDF para). Zajednički `COURSE.md`, korijenski `README.md` i `lectures/README.md` ažurirani su samo radi statusa 01. Izgrađeni hrvatski HTML, PDF skripta i zbirna knjiga su nacrti, ne odobreni izvozi.

## Revizija primjera prema nastavnikovoj odluci

Fizički izložak zamijenjen je digitalnim budžetom od 100 jedinica i isplatama 80/60 u skripti, slajdovima, bilješkama, zadacima, vremenskim naslovima i ilustracijama. Model uključuje račune primatelja i očuvanje zbroja, ovlasti, nenegativan saldo i odvojenu provjeru verzije. Provjereni su oba redoslijeda nespojivih isplata, ponovljeni zahtjev bez dvostruke isplate, odbijanje stare verzije/nedostatka pokrića te dopušteni slijed 30+40. Pretragom izvora nema ostataka R17, muzeja, izloška ili držatelja. Izvozi ponovno izgrađeni, promijenjeni dijagrami i relevantne PDF stranice pregledani. Headless provjera ponovno blokirana istom macOS pogreškom prije učitavanja HTML-a; status ostaje draft.

Slajd 2 revidiran prema nastavnikovu komentaru: motivacija je nepovjerenje u isključivu administratorsku kontrolu A, čak i uz serijske zahtjeve. Skripta, bilješke, dijagram i naslov u timing.json usklađeni. Konkurentnost je odvojena kao kasniji tehnički problem.

## Institucionalna motivacija — posljednja revizija

Uvod sada razdvaja zasebne ledgere, redoviti obračun/poravnanje i eventualni pravni spor. Dodani su dva ilustrirana slajda: vrijeme/trošak postupka i mogućnost prethodne provjere i zajedničkog prihvaćanja. Aktualno: 42 slajda (39 sadržajnih), 34 ilustrirana, 120 minuta; povijesni brojevi provjera iznad odnose se na prethodne revizije. Timing i bilješke ponovno usklađeni. Provjereno 1.147/365 ≈ 3,1 i 100.000 × 0,05 × 3 = 15.000. Nema tvrdnje da se redovito bankovno poravnanje čeka godinama ili da protokol ukida sudsku zaštitu.

Razjašnjeni su atomarnost i izolacija te slijed BEGIN → zaključavanje/provjera → ažuriranje → COMMIT → odgovor, uz izričitu granicu jedne baze kod pouzdanog koordinatora. Replike motivirane opterećenjem čitanja i oporavkom, uz odvojene pretpostavke o preuzimanju upisa, kašnjenju i istom operatoru. Dijagram replika dobio je dodatni prostor za podnaslov.
