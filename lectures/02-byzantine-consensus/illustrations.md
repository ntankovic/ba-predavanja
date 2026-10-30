# Ilustracije predavanja 02

27 od 39 slajdova (69%) ima originalnu objašnjavajuću ilustraciju; bez slike su naslov, ishodi, definicija konsenzusa, dvije vježbe s tablicom, tablice modela i pragova, „Što FLP ne kaže”, „Brojimo identitete…”, usporedna tablica, ponavljanje i literatura.

Izmjenjivi izvor: `assets/build_diagrams.py` (jedna funkcija po slici), uz zajednički stil `scripts/diagram_style.py`. Ponovno generiranje: `python3 lectures/02-byzantine-consensus/assets/build_diagrams.py` (zahtijeva `rsvg-convert` i Pillow). Verzije stanja (v7, v8) crtaju se kao obojeni čipovi preko `assets/version_chips.py` (kopija iz 01; boje odgovaraju `.ver.v7/.v8` u `lecture.css`).

Vizualna gramatika (nastavnik, 2026-10-27, preuzeto iz 01): kućice su samo čvorovi (organizacije, identiteti); ovalni oblici su koraci, izbori i poruke; obojeni redovi nabrajaju pojmove. Crveno označava člana koji odstupa od protokola, sivo i isprekidano člana koji je stao.

| Datoteka (SVG i PDF) | Slajd | Objašnjenje |
|---|---|---|
| recap-two-of-three.hr | Gdje smo stali | Lekcija 01: pravilo „dva od tri” dalo je 140 iz 100 |
| two-questions.hr | Dva pitanja | Dva dijela predavanja, isti budžet F:100 |
| consensus-task.hr | Prvo zadatak (samo poglavlje) | Od različitih prijedloga do jedne zajedničke odluke |
| agreement-broken.hr | Dogovor | Dva ispravna člana, dvije različite odluke |
| validity-trivial.hr | Valjanost | „Uvijek odbij sve” ispunjava dogovor, ali je beskoristan |
| termination-wait.hr | Okončanje | „Čekaj sve” može zauvijek čekati |
| properties.hr | Sigurnost i živost | Tri svojstva i njihova podjela |
| timing-models.hr | Tri modela vremena | Sinkrono, asinkrono, djelomično sinkrono (GST) |
| flp-dilemma.hr | FLP | B ne može razlikovati spor i zaustavljen čvor |
| quorum-majority.hr | Kvorum | Dvije većine od tri dijele člana |
| crash-threshold.hr | n ≥ 2f + 1 | Kvorum n − f uz n = 3 i n = 5 |
| byz-overlap.hr | Većina uz lažljivca | Presjek sadrži samo bizantskog A |
| generals.hr | Bizantski generali | Zapovjednik i dva poručnika |
| generals-two-views.hr | Tri generala | Poručnik 1 u oba slučaja vidi isto (prema LSP 1982, sl. 1–2) |
| byz-threshold.hr | n ≥ 3f + 1 | Dva kvoruma od tri među četiri dijele dva člana |
| four-orgs.hr | Četiri organizacije | Pošten D ne glasa dvaput, tx2 ne skupi kvorum |
| silent-member.hr | Bizantski član šuti | B, C, D sami čine kvorum |
| timing-algorithms.hr | Što model vremena mijenja | Sinkroni i djelomično sinkroni algoritam za isto opažanje |
| bft-phases.hr | BFT protokol | Prijedlog, priprema, potvrda, izvrši; zamjena vođe (shema prema PBFT 1999) |
| bft-cost.hr | Cijena BFT-a | Potpun graf: 12 i 56 poruka po koraku |
| known-membership.hr | Poznato članstvo | Popis A, B, C, D unaprijed |
| open-identities.hr | Otvorena mreža | Identiteti bez znanja tko je iza |
| sybil.hr | Sybil napad | M s tri identiteta među sedam |
| limit-identities.hr | Ograničiti identitete | Središnji upis nasuprot cijeni po identitetu |
| counter.hr | Protuprimjeri | Tri zaključka i tri protuprimjera |
| recap.hr | Sažetak | Konsenzus, prag, članstvo |
| next-question.hr | Otvoreno pitanje | Potpis i povezani zapisi → 03 |

Svi dijagrami su autorski; konceptualni izvori navedeni su u `sources.md`. Pregledani su u HTML slajdovima (headless Chrome) i u PDF poglavlju.
