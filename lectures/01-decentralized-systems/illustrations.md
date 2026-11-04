# Ilustracije predavanja 01

36 od 49 slajdova (73%) ima originalnu objašnjavajuću ilustraciju. Vizuali prate stanje, poruke, granice upravljanja i ispade; nisu ukrasne fotografije.

Izmjenjivi izvori: `assets/figures.json` i `assets/build_diagrams.py`, uz zajednički stil `scripts/diagram_style.py`. Svaki crtež ima SVG za HTML i vektorski PDF za skriptu; ponovno generiranje: `python3 lectures/01-decentralized-systems/assets/build_diagrams.py` (zahtijeva `rsvg-convert` i Python paket Pillow). Verzije stanja (v7, v8) crtaju se kao obojeni čipovi preko `assets/version_chips.py`, koji pozivaju i `build_diagrams.py` i `draw_sequences.py`; boje odgovaraju klasama `.ver.v7` i `.ver.v8` u `lecture.css`. Autorski nastavni dijagrami; konceptualni izvori i adaptacija BA-01 navedeni su u `sources.md`.

| Datoteka (SVG i PDF) | Objašnjenje |
|---|---|
| figure-02.hr | Redovito poravnanje i sudsko rješavanje spora različiti su postupci |
| intro-courts.hr | Hrvatska, 2024.: prosjek prvostupanjskih trgovačkih parnica |
| intro-prevention.hr | Hipoteza: manje sporova o prihvaćenom stanju; trošak koordinacije ostaje |
| state-model.hr | Svaka transakcija vodi u sljedeće stanje; isti ledger uvijek daje isto stanje |
| figure-orgs.hr | Svi čitaju isti saldo; svaki član smije predložiti isplatu (slajd 10) |
| figure-04.hr | Članovi predlažu transakcije; protokol odlučuje koja mijenja stanje |
| figure-05.hr | Jedna isplata: terećenje F i odobrenje X (samo u poglavlju od v1.52) |
| figure-06.hr | Dvije moguće povijesti, a prihvaćamo samo jednu |
| figure-07.hr | Svi prihvaćaju autoritet istog operatora |
| figure-race.hr | Obje provjere prošle su prije prve promjene |
| figure-10.hr | Jedna baza kod pouzdanog koordinatora |
| figure-11.hr | Poruka prelazi granicu procesa (samo u poglavlju od v1.52) |
| figure-12.hr | Više kopija za čitanje i oporavak; isti operator |
| figure-14.hr | Za korisnika B staro čitanje izgleda kao poništena isplata |
| figure-15.hr | Timeout: isplata upisana, odgovor izgubljen (draw_sequences.py, stil RS 01) |
| figure-16.hr | ID zahtjeva nije broj mrežne dostave |
| figure-17.hr | Dostupnost promatramo za određenog sudionika i radnju |
| figure-19.hr | Isto opažanje, različiti stvarni uzroci |
| figure-20.hr | Sva tri čvora rade; prekinute su samo veze preko particije |
| figure-21.hr | Svaka strana poštuje pravilo nad svojom kopijom; zajedno to je dvostruko trošenje |
| figure-22.hr | Jedan sustav opisujemo po više osi |
| figure-23.hr | Jedna upravljačka granica obuhvaća sve kopije |
| figure-24.hr | Razmjena podataka ≠ pravilo prihvaćanja |
| figure-25.hr | Tko može sam promijeniti važno pravilo? |
| figure-26.hr | Dogovor mora povezati neovisne operatore |
| figure-27.hr | Za svaku ovlast: kome je dajemo i što ako je zloupotrijebi? |
| figure-28.hr | Protokol ovisi o dopuštenim vrstama odstupanja |
| figure-29.hr | Poruka je stvarno od A, ali to ne čini odluku ispravnom |
| figure-30.hr | Različit prikaz nije automatski bizantski kvar |
| figure-31.hr | Ovlašten član također može predložiti nedopuštenu isplatu |
| figure-32.hr | Dva lokalna skupa glasova, dva različita zaključka |
| figure-33.hr | Više procesa ne daje više odobrenih glasova |
| figure-34.hr | Poruka → lokalna odluka → izričita potvrda |
| figure-35.hr | Odgovor mora pokazati konkretan korak izvođenja (ne koristi se od 2026-11-03, slajd uklonjen) |
| figure-37.hr | Tražite trag koji pobija tvrdnju, pa precizniju specifikaciju |
| figure-38.hr | Svako jamstvo ima pretpostavke i komponentu koja ga pruža (ne koristi se od 2026-11-03, sažetak je tekstualni popis) |
| figure-39.hr | Dobra specifikacija prethodi izboru protokola |

## Provjera

Svi PDF dijagrami pregledani su kroz rasterizirane kontaktne listove. Provjeren je i prijelom skripte u PDF-u. SVG/PDF parovi postoje za svih 34 crteža. Headless Chrome nije pokrenut zbog macOS ograničenja MachPortRendezvousServer; vizualna provjera HTML slajdova ostaje otvorena. Ne koristiti desktop automatizaciju kao zamjenu.

2026-10-19: figure-02.hr, srednja kućica „Obračun i poravnanje” sada glasi „Plaća se razlika; svi vjeruju središnjoj banci” (nastavnik). Izvor: figures.json.

2026-10-19: figure-06.hr i ostali dijagrami u načinu fork/equivocation dobili su višu sliku (385), da potpis ne prekriva donju kućicu.

2026-10-19: figure-20.hr prikazuje saldo F:100 · v7 na obje strane particije; figure-21.hr: oznake „A i B potvrđuju” / „C potvrđuje” i „140 isplaćeno iz fonda od 100”.

2026-10-19: radionica (figure-34.hr) zamijenjena je studijom slučaja: case-1.hr, case-2.hr i case-3.hr (SVG i PDF) su dijagrami slijeda poruka (model 1: pošten koordinator; model 1 uz izgubljenu potvrdu; model 2: pravilo „dva od tri”, preimenovano 2026-11-03). Izvor: build_diagrams.py, funkcija seq. figure-34.hr se više ne koristi.
