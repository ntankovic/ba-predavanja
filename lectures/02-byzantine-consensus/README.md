# 02 — Konsenzus i problem bizantskih generala

- Status: hrvatski nacrt za nastavnikov pregled; owner: coordinating agent (2026-10-27).
- Engleski izvori (`slides.qmd`, `chapter.qmd`) ostaju planski predlošci; prijevod nakon pregleda hrvatskog sadržaja.
- Trajanje: **110 minuta**, uključujući dvije vježbe, raspravu i ponavljanje.
- Opseg: 37 slajdova uključujući naslov, ishode i literaturu; 25 ilustriranih slajdova (26 originalnih dijagrama; jedan samo u poglavlju).
- `chapter.hr.qmd` je cjelovita skripta; `slides.hr.qmd` izvedeni su sažeci s bilješkama i vremenom za svaki slajd. `timing.json` evidentira intervale.
- Glavno pitanje: Kako postići dogovor ako neki sudionici lažu, a identiteti se mogu stvarati?
- Primjer: isti budžet kao u 01 (F:100, T1 = 80 iz F na X, T2 = 60 iz F na Y, stanje v7); A se ponaša bizantski; dodaje se organizacija D; u drugom dijelu strana M s tri identiteta.
- Predznanje: predavanje 01 (model, replike, spor i zaustavljen čvor, bizantsko ponašanje, „dva od tri”).

## Ishodi

1. Razlikovati dogovor, valjanost i okončanje te ih povezati sa sigurnošću i živošću.
2. Objasniti kako model vremena određuje što protokol može jamčiti (FLP intuicija).
3. Izračunati i obrazložiti n ≥ 2f + 1 uz padove i n ≥ 3f + 1 uz bizantske članove.
4. Objasniti Sybil napad: broj identiteta nije broj neovisnih članova.
5. Obrazložiti zašto klasični BFT sam ne rješava otvorenu mrežu.

## Tijek i trajanje

| Slajdovi | Tema | Minute |
|---|---|---:|
| 1–4 | Naslov, gdje smo stali, dva pitanja, ishodi | 8 |
| 5–11 | Zadatak konsenzusa: dogovor, valjanost, okončanje, sigurnost/živost, vježba, model | 22 |
| 12–14 | Modeli vremena i FLP | 11 |
| 15–18 | Kvorum, n ≥ 2f + 1, vježba, presjek uz lažljivca | 14 |
| 19–26 | Bizantski generali, n ≥ 3f + 1, četiri organizacije, prag po modelu, BFT i cijena | 26 |
| 27–32 | Članstvo, otvorena mreža, Sybil napad, ograničavanje identiteta, usporedba | 16 |
| 33–37 | Ponavljanje, protuprimjeri, sažetak, otvoreno pitanje, literatura | 13 |

## Granice sadržaja

Model vremena, kvarova, broja neispravnih, članstva i potpisa naveden je prije pragova. FLP je prikazan kao rezultat za potpuno asinkroni deterministički model, ne kao nemogućnost konsenzusa općenito. Pragovi su vezani uz model (DLS 1988, Tablica I). BFT pretpostavke odvojene su od otpornosti na Sybil napad u otvorenoj mreži. Potpise samo imenujemo (predavanje 03); Bitcoin se ne spominje, a cijena po identitetu najavljuje se kao tema predavanja 04. PBFT se prikazuje samo kao shema faza, bez detalja promjene pogleda.

## Pregled

Status ostaje `draft` do nastavnikova pregleda hrvatskog sadržaja. Provjereno: izgradnja HTML slajdova i PDF poglavlja; svih 37 slajdova vizualno u headless Chromeu (bez prelijevanja); svih 22 stranice PDF-a; nema nedostajućih znakova u PDF-u (≥ je u poglavlju zapisan kao matematika). `just browser-check` nije pokrenut jer `.tools/qa-venv` ne postoji.

Otvoreno za nastavnika:
- Pojmovi u `references/terminology.md` dodani su kao *provisional* (dogovor, valjanost, okončanje, sigurnost, živost, kvorum, djelomično sinkroni model, Sybil napad, BFT, ispravan član, otvorena mreža).
- Randomizirani protokoli (okončanje s vjerojatnošću 1) spomenuti su bez izvora; ako ostaje, dodati Ben-Or (1983).
- Valjanost je definirana aplikacijski („valjan prijedlog nekog člana”); DLS koristi jaku jednoglasnost — razlika je navedena u skripti.

## Promjene

- 2026-10-27 (v1.0): prvi cjeloviti hrvatski nacrt (poglavlje, 37 slajdova, timing.json, 26 dijagrama u `assets/build_diagrams.py`).
- 2026-10-27 (v1.1): ishodi s *safety*/*liveness*, objašnjenjem FLP-a i BFT-a kao protokola za konsenzus.
- 2026-10-27 (v1.2): „FLP” pod navodnicima (inicijali autora) u naslovima, tekstu, tablici i slici.
- 2026-10-27 (v1.3): Definicija 2.1 prema Dwork, Lynch i Stockmeyer (1988), §2.4; „završavanje” → „okončanje”; valjanost: formalna inačica u definiciji, aplikacijska na slajdu 7.
- 2026-10-27 (v1.4): slika maknuta sa slajda s definicijom (ostaje u poglavlju); redak valjanosti na slici „Sigurnost i živost” usklađen s definicijom.
- 2026-10-27 (v1.5): varijable i izrazi (n, f, n ≥ 3f + 1 …) u stilu `.expr`.
- 2026-10-27 (v1.6): „Tri modela vremena” kao prostorno-vremenski dijagram; GST objašnjen na slajdu i u poglavlju.
- 2026-10-28 (v1.7): novi slajd „GST: pretpostavka za dokaz, ne postavka mreže” sa slikom rastućeg isteka roka.
- 2026-10-28 (v1.8): natpisi kosih strelica na slikama bizantskih generala uz strelicu, s bijelim rubom.
- 2026-10-28 (v1.9): slajd ishoda u stilu WA („Ishodi i predznanje”, Bloomove razine, predznanje).
- 2026-10-28 (v1.10): upućivanja na predavanja 03 i 04 punim riječima na slici i potpisu otvorenog pitanja.
- 2026-10-28 (v1.11): oznake stanja S₇/S₈ umjesto verzija v7/v8 (čipovi, slike, poglavlje).
- 2026-10-28 (v1.12): novi slajd „GST: pretpostavka za dokaz, ne postavka mreže” (growing-timeouts) i „Što model vremena mijenja u algoritmu” (timing-algorithms): sinkroni algoritam istek roka koristi kao dokaz pada, djelomično sinkroni samo za novi krug, a odlučuje kvorumom 2f + 1. Ukupno 39 slajdova, 110 min.
- 2026-10-28 (v1.13): slajd 2 „Evidencija prisutnosti” s QR kodom iz predavanja 00 (bit.ly/bc-tu-sam); naslov i QR dijele prvu minutu (0,5 + 0,5 min).
- 2026-10-29 (v1.14): transakcije tx₁/tx₂ umjesto T1/T2 na slajdovima, u poglavlju i na slikama (čip `.tx`; `version_chips.py` preuzet iz 01).
- 2026-11-03 (v1.15): „sinkronija” nije hrvatska riječ (nastavnik). Zamijenjena je s „djelomično sinkroni model” (*partial synchrony*), a gdje je riječ o vremenu, s „vremenske pretpostavke” (slajdovi, poglavlje).
- 2026-11-03 (v1.16): „Kvorum: dovoljno glasova za odluku”: umjesto apstraktnog „Dva kvoruma moraju dijeliti poštenog člana” slajd navodi „Uvjet sigurnosti: svaka dva moguća kvoruma dijele poštenog člana”, upućuje na kvorume {A, B} i {B, C} sa slike (zajednički je B) te ih suprotstavlja predavanju 01 (ondje je zajednički član A glasao dvaput). Slika je smanjena na 680 px, a poglavlje je usklađeno.
- 2026-11-03 (v1.17): slika quorum-majority više ne sugerira da je B glasao za oba prijedloga. Sada prikazuje ishod: B glasa samo za tx₁, pa je kvorum za tx₁ (A + B) skupljen, a za tx₂ ostaje samo C i kvorum je nepotpun. Potpis glasi „Dvije većine od tri dijele člana; pošten član omogućuje samo jednu odluku”.
- 2026-11-03 (v1.18): kako znamo da kvorumi dijele poštenog člana. „Uz padove” sada kaže da ne znamo koji članovi padaju, nego samo koliko ih najviše može pasti (f), te bira n i kvorum u dva koraka (živost: čekamo n − f; sigurnost: presjek n − 2f). „Zašto većina ne pomaže uz lažljivca” se nadovezuje na to („uz padove je bio dovoljan jedan zajednički član”), a „Uz bizantske članove” ponavlja ista dva koraka uz stroži uvjet presjeka. Slajd „Kvorum” nije mijenjan, a crash-threshold je smanjen na 740 px. Poglavlje je usklađeno.
- 2026-11-03 (v1.19): „Kad bizantski član šuti”: dodana je rečenica da f broji sve neispravne članove (pad poštenog člana troši isti f kao laž) i da sustav, kad su neispravna dva, staje, ali ne donosi proturječne odluke. Primjer (A laže, B padne) i napomena o trajnom zapisu glasa nalaze se u bilješkama i poglavlju.
