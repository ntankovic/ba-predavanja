# 01 — Od raspodijeljenih do decentraliziranih sustava

- Status: hrvatski nacrt za nastavnikov pregled; owner: coordinating agent.
- Engleski izvori ostaju planski predlošci; prijevod nakon pregleda hrvatskog sadržaja.
- Trajanje: **116 minuta**, uključujući raspravu, zadatke i ponavljanje.
- Opseg: 48 slajdova uključujući naslov, ishode i literaturu; 37 ilustriranih slajdova (77%).
- `chapter.hr.qmd` je cjelovita skripta; `slides.hr.qmd` izvedeni su sažeci s bilješkama i vremenom za svaki slajd. `timing.json` evidentira intervale.
- Glavno pitanje: Tko odlučuje što vrijedi kada sudionici ne vjeruju istom koordinatoru?
- Primjer: zajednički digitalni budžet triju organizacija; F ima 100 jedinica, a konkurentne isplate iznose 80 i 60. Računi F/X/Y dio su iste evidencije, bez vanjske bankovne isplate.
- Predznanje: zapis podataka, uvjet i poziv funkcije. Nije potrebno prethodno poznavanje blockchaina.

## Ishodi

1. Razlikovati raspodijeljenost, decentralizaciju i P2P.
2. Pratiti promjene stanja kroz više replika.
3. Razlikovati kašnjenje, djelomičan ispad i bizantsko ponašanje.
4. Navesti pretpostavke povjerenja za predloženo rješenje.
5. Obrazložiti kada je zajednički koordinator dovoljan.

## Tijek i trajanje

| Slajdovi | Tema | Minute |
|---|---|---:|
| 1–4 | Institucije, cijena spora i moguća prevencija | 8 |
| 5–12 | Ishodi, budžet i koordinator | 24 |
| 13–23 | Replike i ispadi | 31 |
| 24–35 | Upravljanje i bizantsko ponašanje | 34 |
| 36–42 | Radionica, pregled i ponavljanje | 23 |

## Granice sadržaja

Model vremena, članstva, autentifikacije i ispada naveden je prije rasprave o jamstvima. Primjer „dva od tri” služi kao protuprimjer naivnom glasovanju, ne kao BFT protokol. Nema tehničkog uvoda u Bitcoin ni IPFS. Predavanje 02 preuzima formalne uvjete konsenzusa i bizantske generale.

## Pregled

Pogledati `design-review.md` za obavljene provjere i preostali problem headless HTML provjere. Status ostaje `draft` do vizualne HTML provjere i nastavnikova pregleda hrvatskog sadržaja.

Uvod u 01 motivira decentralizaciju isključivom administratorskom ovlašću jedne organizacije nad zajedničkim budžetom. Sukob isplata 80/60 služi tek kasnije za analizu stanja i konkurentnosti; sam po sebi ne opravdava decentralizaciju.

## Promjene

- 2026-10-20 (v1.3): verzija slajdova dodana u podnožje (`slides_version` u lecture.json).
- 2026-10-21 (v1.4): slajd „Provjerite uvjerljiv AI prijedlog” preimenovan je u „Što ne štima u ovom prijedlogu?” (nastavnik). Vježba je ponavljanje prije sažetka, bez AI okvira; poglavlje i timing.json su usklađeni.
- 2026-10-21 (v1.5): slajd „Što ne štima u ovom prijedlogu?”: pitanja u figure-37 sada navode scenarij (jedan administrator, suprotna potvrda drugog poslužitelja, dvostruka isplata nakon isteka roka); bilješke i poglavlje povezani su s ranijim slajdovima.
- 2026-10-21 (v1.6): vježba je podijeljena na dva slajda. „Ponavljanje: što ne štima u ovom prijedlogu?” postavlja prijedlog u primjer budžeta s tri istaknuta zaključka. „Tri zaključka, tri protuprimjera” (figure-37, način counter) za svaki zaključak daje protuprimjer i raniji slajd. Poglavlje i timing.json su usklađeni (2 + 2 min).
- 2026-10-21 (v1.7): sažetak preimenovan u „Sažetak: tri pojma koja ne smijemo izjednačiti”. figure-38 (način counter) za svaki par pojmova daje preciznu tvrdnju i raniji slajd; uvodna rečenica veže razlikovanja uz predavanja 02–04. Poglavlje i timing.json su usklađeni.
- 2026-10-21 (v1.8): slajd „Sljedeći izazov: dogovor bez zajedničkog šefa” preimenovan je u „Otvoreno pitanje za predavanje 02”. Slajd sada kaže da je prvi dio predavanja pretpostavljao jednog operatora, a drugi neovisne čvorove bez rješenja. Poglavlje i timing.json su usklađeni.
- 2026-10-21 (v1.9): u figure-28 kartica „Bizantsko ponašanje” označena je crveno kao zlonamjeran slučaj (oznaka danger u figures.json).
- 2026-10-21 (v1.10): „Što znači djelomičan ispad?”: figure-17 (način triangle) je trokut u kojem rade svi čvorovi, a prekinuta je samo veza A–B. Kartice kažu na koga se odnose. „Nema jednog zaslona” zamijenjeno je s „Nijedan čvor ne vidi stanje cijelog sustava”. Poglavlje je usklađeno.
- 2026-10-21 (v1.11): figure-15 („Zahtjev je izvršen, potvrda nije stigla”) ponovno je nacrtan u stilu RS 01 (assets/draw_sequences.py): kartice sudionika, traka čekanja, izgubljen odgovor i kartica za timeout. Uklonjen je iz figures.json.
- 2026-10-21 (v1.12): pregled koherentnosti. Uloge su usklađene: B predlaže T1, C predlaže T2, a A je poseban čvor (figure-04, slajd 41, poglavlje). U figure-17 C ne zna za prekid A–B. Slajd 24 ima prijelaznu rečenicu, a slajd 44 se vraća na pitanje banaka s početka.
- 2026-10-21 (v1.13): dodane su Definicija 1.1 (raspodijeljeni sustav, kao u RS 01) na slajdu 13 i Definicija 1.2 (decentralizirani sustav, preko ovlasti) na slajdu 28, uz rečenicu „Svaki decentralizirani sustav je raspodijeljen; obrnuto ne vrijedi.” Izvori su Buterin 2017 i van Steen i Tanenbaum 2023 (razlika u definiciji navedena je u bilješkama). Poglavlje je usklađeno.
- 2026-10-21 (v1.14): slajd 6 prikazuje jedan trenutak (v7): A sada samo čita saldo, a B i C sada predlažu. Potpis kaže da uloge nisu stalne. Poglavlje je usklađeno.
- 2026-10-21 (v1.15): slajd 6 pojašnjava protokol kao zajednička pravila koja svi moraju poštovati (dijagram, bilješke, poglavlje).
- 2026-10-21 (v1.16): slajd 6, kartica A: „Sada ne predlaže ništa” umjesto „Sada samo čita” (čitanje nije imalo svrhu i sugeriralo je posebnu ulogu).
- 2026-10-21 (v1.17): prijedlozi T1 i T2 pišu se „80 iz F na račun X” i „60 iz F na račun Y” (slajdovi 6 i 41, poglavlje), da se vidi odakle i kamo ide isplata.
- 2026-10-21 (v1.18): slajd 6 ima tablicu salda pri stanju v7 (F 100, X 0, Y 0); dijagram je smanjen da sve stane.
- 2026-10-21 (v1.19): stanje i transakcija vizualno su razdvojeni. Stanja su plave kartice s oznakom STANJE, a transakcije narančaste pilule s oznakom TRANSAKCIJA na strelici između stanja (figure-05 način transition, figure-06 način branch). Na slajdu 7 su oznake „Stanje S7” i „Transakcija T1”.
- 2026-10-27 (v1.20–v1.23): „Uz koji model tvrdimo da pravilo vrijedi?” imenuje jamstvo (saldo nikad negativan). Povjerenje se uvodi već na slajdu koordinatora; slajd 29 ima poveznicu i naslov „Povjerenje rastavljamo na konkretne ovlasti”; figure-27 pitanja vezana uz budžet (isplata, pravilo pokrića, primanje D / isključenje C).
- 2026-10-27 (v1.24–v1.25): primjer „Isti pošiljatelj govori dvije stvari” ide prije „Pad i proizvoljno ponašanje nisu isti kvar”; figure-28 posljedica „Treba drukčije pravilo prihvaćanja”. Rečenice-poveznice dodane na deset naglih prijelaza (slajdovi 13, 17, 19, 21, 24, 30, 33–36).
- 2026-10-27 (v1.26–v1.27): slajd 30: A je jedan od tri člana koji odobrava (ne koordinator), figure-29 „Odobravam T1/T2”; slajd 14 objašnjava oznake čvorova A, B, C; slajd 39 „Analiza: gdje je pravilo o saldu prekršeno?”, figure-35 „Protuprimjer”; slajdovi 30 i 33 navode pretpostavku nekrivotvorivih poruka i najavljuju digitalni potpis (03).
- 2026-10-27 (v1.28–v1.29): verzije v7/v8 kao obojeni čipovi u tekstu, tablicama i dijagramima (`assets/version_chips.py`, pozivaju ga oba generatora); slajd 41 „…u ovom prijedlogu protokola?”.
- 2026-10-27 (v1.30–v1.31): definicije s engleskim nazivom u zagradi (ledger, verzija, čvor, replika, idempotentan, mrežna particija, P2P, konsenzus, atomarnost, izolacija, bizantsko ponašanje); slajd 23 objašnjava zašto C preuzima upise; nova slika `figure-race` na slajdu 11; slajd 38 povezan sa slajdom 34. Izmjene ručno rađenih SVG-ova prenesene su u `figures.json` i generator.
- 2026-10-27 (v1.32–v1.36): slajd 16 „Korisnik ne vidi vlastitu isplatu” iz perspektive korisnika B, figure-14 (način staleread) s čvorovima A i C i dva izbora sučelja; Sustav 2 na slajdu 27 („poslužitelj, bazu i kod drži jedna tvrtka”); slajd 32 „obje ne mogu proći”; u case-1/case-2 C dobiva „T2 odbijen; prihvaćen T1, F:20”; u case-3 A označen kao bizantski.
- 2026-10-28 (v1.37): novi slajd 2 „Što je ledger?”: definicija (glavna knjiga), primjer s dva knjiženja Ana–Boris i dvojno knjigovodstvo; most prema isplati T1 (terećenje F, odobrenje X). Vrijeme: ledger 1–3, banke 3–5, sudovi 5–7, prevencija 7–9, ishodi 9–10 min.
- 2026-10-28 (v1.38): ledger na slajdu 2 prikazan kao dva izvoda Banke A (Ana, Boris), od salda 0,00 uz gotovinske uplate 100 i 20; stil `.statements` u lecture.css. Poglavlje zadržava običnu tablicu i objašnjava da gotovinska uplata ima drugu stranu na računu blagajne banke.
- 2026-10-28 (v1.39): novi slajd 3 „Ledger banke: sva knjiženja na jednom mjestu”: zajednička glavna knjiga Banke A s blagajnom, Ana i Boris; svako knjiženje u dva retka, zbrojevi 160 = 160, Anini retci istaknuti kao njezin izvod. Vrijeme: novi slajd 3–5 min; po 1 min manje na „Naivan kod ipak može pogriješiti” i „Dvije strane ne smiju obećati suprotno”.
- 2026-10-28 (v1.40): slajd ishoda u stilu WA („Ishodi i predznanje”, kartice s Bloomovom razinom, okvir predznanja).
- 2026-10-28 (v1.41): novi slajd 8 „Kako prikazujemo stanje i transakcije” (state-model, način chain): ledger kao lista transakcija U1, U2, K1, K2 i lanac stanja S0–S4 s verzijama; uvodi notaciju stanje/transakcija/verzija. Vrijeme 2 min; po 1 min manje na „Stanje zapisujemo izričito” i „Kopije nisu trenutačno jednake”.
- 2026-10-28 (v1.42): na slajdu 8 varijable S~n~, v~n~, S~n+1~ u stilu `.expr` (stil dodan u lecture.css); potpis slike bez formule; u poglavlju LaTeX ($S_n$, $\neq$). Pravilo za izraze i verzije zapisano u COURSE.md.
- 2026-10-28 (v1.43): figure-20 („Mreža se razdvojila”) precrtan: zasebne kućice za A, B i C, puna veza A–B, prekinute veze A–C i B–C, iscrtkani okviri za dvije strane particije.
- 2026-10-28 (v1.44): upućivanja na druga predavanja pišu se punim riječima („predavanje 02”, „predavanja 03–04”) na slajdu sažetka i u poglavlju.
- 2026-10-28 (v1.45): slajd „Tri organizacije, jedan digitalni budžet”: tablica salda i tri kućice zamijenjeni jednom slikom (figure-04, način budget): organizacije A, B, C, prijedlozi T1 i T2 kao transakcije, stanje S7 v7 s F:100, X:0, Y:0.
- 2026-10-28 (v1.46–v1.47): verzije v7/v8 zamijenjene oznakom stanja S~x~ u oba predavanja (čipovi S₇/S₈ u tekstu i slikama, naslovi kartica S₇; opća oznaka S~x~); figure-04 s protokolom koji pušta samo jednu isplatu; figure-12 bez iscrtkane strelice prema C; K42 u slici fontom stalne širine; diagram_style.box centrira jednoredni podnaslov.
- 2026-10-28 (v1.48): na slici „Pravilo koje mora ostati istinito” alternativno stanje nakon T2 nazvano S₈′; bilješke i poglavlje objašnjavaju da se prihvaća samo jedno od S₈ i S₈′.
- 2026-10-28 (v1.49): figure-21 („Dvije strane ne smiju obećati suprotno”, način split-history): dvije strane particije kao dva lanca stanja (S₇ → T1 → S₈ i S₇ → T2 → S₈′), čvorovi kao okrugle oznake, spajanje kao crvena pilula „140 iz 100”.
- 2026-10-28 (v1.50): slajd 2 „Evidencija prisutnosti” s QR kodom iz predavanja 00 (bit.ly/bc-tu-sam); naslov i QR dijele prvu minutu (0,5 + 0,5 min).
- 2026-10-28 (v1.51): slajd 15 „Naivan kod ipak može pogriješiti” → „Koordinator s dvije dretve: obje provjere prije promjene”: uvodna rečenica o dvije dretve istog koordinatora, objašnjenje da su provjera i promjena dva koraka, imenovana utrka (*race condition*); u bilješkama i poglavlju: zašto ni provjera verzije ne pomaže i najava rješenja u bazi. Slika utrke 780 px.
- 2026-10-28 (v1.52): povezana priča slajdova 10–18. Vidljivi mostovi prema sljedećem slajdu (`.bridge`) na 12, 14, 16 i 17; oznake koraka (`.step-tag`) „Korak 1 · jedan koordinator” (13), „Korak 2 · zahtjevi preko mreže” (17), „Korak 3 · više kopija” (18). Slajd 10 dobiva novu sliku `figure-orgs` (samo članovi i budžet); slajd 11 više ne ponavlja definiciju S~x~, nego uvodi T1 i T2 uz sliku `figure-06`; slika s protokolom (`figure-04`) prelazi na slajd 12. Slajd 13 i figure-07 kažu da koordinator radi na čvoru kod A (A ostaje čvor koji prihvaća upise u 18–42); potpis figure-12 usklađen. Slika `figure-11` maknuta sa slajda 17 (ne stane uz definiciju), ostaje u poglavlju. Poglavlje usklađeno.
- 2026-10-29 (v1.53): stanje ima vlastiti oblik, odvojen od čvora: plavo obojena kartica s punim rubom i trakom STANJE unutra, bez bočne crte (`state_box()` u `scripts/diagram_style.py`); vrijedi za sve slike sa stanjima, uključujući S₀–S₄ na slajdu 9. Kartica S₈ u figure-04: „samo T1 ili T2”. Oznake koraka: slajd 17 više nije korak (samo imenuje ono što sustav već jest); slajdovi 15 i 18 dijele „Korak 2 · skaliranje koordinatora” (više dretvi, više kopija). Slika utrke 680 px.
- 2026-10-29 (v1.54): transakcije tx₁/tx₂ umjesto T1/T2 (narančasti čip `.tx` na slajdima, čip u slikama, $\mathrm{tx}_{1}$ u poglavlju); kućice samo za čvorove: koraci i poruke kao pilule (`pill()`), scenariji i brojke kao otvoreni paneli (`panel()`) u figure-02, intro-courts, intro-prevention, race, 10, 16, 19, 28, 29, 30, 31, 35, 39; prekinuta veza kao bijeli krug s crvenim × na crti (`cut()`) u figure-15, 17, 20 i case-2. `version_chips.py` prepisan: jedan natpis smije imati više čipova (S₇, tx₁) i S_7.
- 2026-11-03 (v1.55): „Kašnjenje ili proturječje?”: oba slučaja ponovo navode što znače S₇/S₈ (F:100 / F:20, isplata 80 na X prihvaćena) i tx₁/tx₂ (80 na X, 60 na Y), jer su oznake uvedene 20 slajdova ranije. Poglavlje sada opisuje oba slučaja prije analize.
- 2026-11-03 (v1.56): „Kašnjenje ili proturječje?”: uz svaki slučaj stoji zaključak (kašnjenje: C je pošten i stanja će se izjednačiti; proturječje: neće se samo izjednačiti, treba protokol). case-1/2: okvir bilješke sada se širi prema stvarnoj širini teksta s čipovima (`measure()` u version_chips.py), a natpis je skraćen na „prihvaća tx₁, odbija tx₂”. figure-30: kartice su naslovljene „Slučaj 1: kašnjenje” i „Slučaj 2: proturječje”, a desna je crvena (danger).
- 2026-11-03 (v1.57): studija slučaja izričito navodi dva modela: izvođenja 1–2 su model 1 (koordinator kod A, s početka predavanja), izvođenje 3 je model 2 (bez koordinatora, dva od tri). Izvođenje 2 označeno je kao kašnjenje, a izvođenje 3 kao proturječje, uz povratnu poveznicu na „Kašnjenje ili proturječje?”. Poglavlje je usklađeno.
- 2026-11-03 (v1.58): studija slučaja preimenovana je u dva modela: „Model 1: pošten koordinator”, „Model 1, ali moguća su kašnjenja” (izgubljena potvrda kao primjer, bez dojma da je to jedina vrsta kašnjenja) i „Model 2: pravilo „dva od tri””. Potpisi case-1/2/3, timing.json, bilješke „Analize” i poglavlje su usklađeni.
- 2026-11-03 (v1.59): uklonjen je slajd „Analiza: gdje je pravilo o saldu prekršeno?” (figure-35). Odgovor je već vidljiv na slajdu Model 2, a vježba protuprimjera ponavlja se u „Ponavljanju”. Pitanje „na kojoj strelici nastaje 140 iz 100?” premješteno je u bilješke slajda Model 2. Trajanje je sada 116 min (−4), a timing.json, bilješke i poglavlje su pomaknuti.
- 2026-11-03 (v1.60): „Literatura za produbljivanje” preimenovana je u „Dodatna literatura” (slajd, poglavlje, timing.json).
- 2026-11-03 (v1.61): „Otvoreno pitanje za predavanje 02” je napisano akademskim registrom: bez upućivanja na slajdove, imenuje se naivno pravilo „dva od tri”, a „kada smiju prestati čekati” zamijenjeno je s „pod kojim uvjetima postupak mora završiti”. Poglavlje je usklađeno.
- 2026-11-03 (v1.62): sažetak je zamijenjen slajdom „Sažetak: od koordinatora do konsenzusa” sa šest poruka predavanja (od „Skup poslovnih pravila kao polazna točka” do „Granice naivne većine”) i zaključnom rečenicom o izričitom modelu. Na slajdu su sažete formulacije (klasa `.dense-list` u assets/lecture.css), a u poglavlju su pune rečenice. figure-38 se više ne koristi. Poglavlje i timing.json su usklađeni.
- 2026-11-04 (v1.63): slajd „Isti pošiljatelj govori dvije stvari” dobio je crvenu oznaku „Novi problem · proturječne poruke” (`.step-tag.problem-tag`), uz postojeće oznake koraka.
- 2026-11-04 (v1.64): potpisi ispod slika više nisu velik crni tekst, nego diskretni sivi opisi u kurzivu (19 px, `figcaption()` u build_diagrams.py). Na slikama koje uspoređuju dva slučaja (figure-19, 28, 30) treći element („Posljedica”, „B vidi”, „Provjera”) sada je okvir ispod obaju slučajeva.
- 2026-11-11 (v1.65): pregled prijelaza. Popravljeni artefakti zamjene (T2 i „v3.0” u bilješkama i poglavlju), sudionici u bilješkama „Tri zaključka” (B i C) i odgovori kviza za Sustav 2 (DA/NE, uz obrazloženje prema Def. 1.1 i 1.2). Definicija 1.2 sada dolazi prije P2P-a i kviza (slajd „Decentralizacija: tko ima ovlasti, a ne koliko računala”); promjena pretpostavke za budžet dolazi na slajdu „Povjerenje rastavljamo na konkretne ovlasti” (Korak 4). Oznake koraka: 1 koordinator, 2 dretve, 3 kopije, 4 bez operatora. „Identitet ne zamjenjuje pravilo prihvaćanja” stoji odmah iza „Isti pošiljatelj govori dvije stvari”, koji sada izričito navodi pravilo prihvaćanja. Banka iz uvoda zove se Banka Sjever (Sjever, Jug, Istok u figure-02), ID zahtjeva je Z42. Nove vrste oznaka u lecture.css: `.org` (organizacija/čvor), `.acct` (račun), `.post` (knjiženje), uz postojeće `.tx` i `.ver`; legenda na slajdu budžeta. Replika-tablica ima naslove „A · primarna baza” i vidljivo objašnjenje; dodan razlog čitanja s C; most prema kvorumu nakon particije. Slajd „Model 1, ali moguća su kašnjenja” uklonjen; završni blok nosi oznaku „Ponavljanje” (`.recap-tag`), vježba dobiva 4 min. Ukupno i dalje 116 min.
