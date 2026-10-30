# Pregled nacrta — 2026-10-08

## Provedeno

- Pregled izvornog BA PDF-a: tekst svih 56 stranica i kontaktni list slajdova; pregledani hrvatski uvodi RS i WA te zapisi ispravaka hodograma.
- Izvezen HTML predavanja 00 (30 slajdova, 35.5 minuta). Broj slajdova, naslovi, bilješke, timing i metadata usklađeni.
- Slike ugrađene u HTML (uključujući Reveal data-src), lokalni izvori postoje. BA-00 naslov kartice i hrvatski naziv provjereni.
- Ocjenjivanje usklađeno s izravnim uputama; stari postoci nisu u studentskom sadržaju. Engleski je još scaffold, nije prijevod.
- Vizualno pregledani PDF prikazi dijagrama; ispravljeno mjesto oznake NE u hodogramu. Git primjer prilagođen BA registru; kalendar preciziran na obranu. SVG izvori ostaju uređivi.
- U svih 14 CSS datoteka uklonjeni RS komentari i nekorišteni Firebase/DNS/webshop/HTTP stilovi. Predavanje 00 ima samo dodatne stilove za ponovno uključene sadržaje.
- Ponovno izvezeni postojeći HTML 01 i hrvatska knjiga radi čišćenja. Tekst i metapodaci knjige koriste hrvatski naziv.

## Ograničenje provjere

Headless Chrome launch u `just browser-check 01-decentralized-systems hr` blokiran je prije učitavanja dokumenta: `bootstrap_check_in org.chromium.Chromium.MachPortRendezvousServer: Permission denied (1100)`. Zbog istog pokretačkog ograničenja nije moguće pregledati novi HTML 00. Nije korištena desktop automatizacija. Nije potvrđeno prelamanje, prelijevanje ni ukupni izgled HTML slajdova. PDF slajdova nije izvezen; postoje vektorske PDF inačice ilustracija.

Quarto iz referentnog WA projekta ima cache putanju u tom projektu, koja ovdje nije zapisiva. Za izvoz je korištena izolirana kopija launchera i quarto.js u `/private/tmp/ba-quarto`, s cacheom `/private/tmp/ba-quarto-cache`; alati i resursi čitani su iz postojeće instalacije. Referentni projekti nisu mijenjani. Redovita lokalna Quarto instalacija može se koristiti preko QUARTO_BIN.

## Za završni pregled

- Pokrenuti headless browser provjeru predavanja 00 u okruženju koje dopušta pokretanje Chromea.
- Nastavnik pregledava sadržaj i otvorene stavke u README.md.
- Potom prijevod na engleski. Status ostaje draft, ne ready.

## Korekcija projektnih ideja — 2026-10-08

Uklonjena sva tri slajda s 12 generičkih AI/web ideja bez opravdane uloge blockchaina (uključujući hladnjak). Preostale četiri teme precizirane su kroz pravila raspolaganja sredstvima ili zajedničku provjeru zapisa više organizacija; pretpostavke i ograničenja u bilješkama. AI alati i odgovornost za kod ostaju. Aktualno: 27 slajdova / 32.5 minuta. Timing i metadata usklađeni; prethodni brojevi opisuju raniju verziju.

2026-10-08 — Nastavnik je zatražio povratak svojeg izvornog dijagrama. Slajd koristi assessment-flow.original.png bez izmjena, s lightbox povećanjem i vidljivim pojašnjenjem aktualnog roka i uvjeta oslobođenja. Novi SVG hodogram ostaje neupotrijebljena radna inačica.

2026-10-08 — Vraćen izvorni nastavnikov hodogram. Smanjen natpis OBRANA u kalendaru s 34 na 26 px radi unutarnjeg razmaka. Kontaktni slajd sada upućuje na asinkroni Google Chat; e-pošta uklonjena prema izričitoj nastavnikovoj preferenciji. Točan naziv/poveznica grupe još nije dostavljen.

## WA oblikovanje i dopune — 2026-10-12

30 slajdova, 35,5 minuta. Usklađene bilješke, timing.json i lecture.json. Uspoređene WA i BA cjeline, prenesen WA CSS uz lokalne BA dodatke za ocjenu i izvorni hodogram. Dodani tehnologije, znanje za usmeni i izmjena koda; zadržani BA opseg i pravila. Novi dijagrami pregledani u PDF izvozu. HTML uspješno izgrađen. Headless browser-check ponovno ne uspijeva pokrenuti Chrome (MachPortRendezvousServer, Permission denied, SIGTRAP); nije korištena desktop automatizacija. Vizualni pregled cjelokupnog HTML-a ostaje otvoren. Status draft. QR i podatci o nastavniku vježbi/Chat grupi čekaju nastavnikovu informaciju.

## Dopune i headless provjera — 2026-10-12

Izmijenjeni slajdovi 21 (AI pravila), 24 (rezervacija obrane), 25 (zaokruživanje) i 30 (novi završni slajd); timing.json usklađen (naslov slajda 30), broj slajdova i trajanje nepromijenjeni. HTML izgrađen izoliranim Quartom (`QUARTO_BIN=/private/tmp/ba-quarto/bin/quarto`). `just browser-check 00-course-introduction hr` prošao (PASS, 30 slajdova, bez prelijevanja) uz `CHROME_BIN` na instalirani Chrome u headless načinu i `COURSE_QA_PYTHON` iz WA `.tools/qa-venv`; desktop automatizacija nije korištena. Pregledane snimke slajdova 21, 24, 25 i 30. Raniji launch blocker u ovom pokretanju nije se pojavio. Status ostaje draft do nastavnikova pregleda; engleski odgođen.

## RS prilagodbe — 2026-10-13

Promjene su opisane u README.md. `just slides 00-course-introduction hr` izgrađen je s `QUARTO_BIN` na WA `.tools/quarto` i cacheom u scratchpadu; privremena kopija u `/private/tmp/ba-quarto` više ne postoji. `just browser-check 00-course-introduction hr`: PASS, 32/32 slajda, bez runtime pogrešaka i prelijevanja (CHROME_BIN headless, WA qa-venv). Pregledane su snimke slajdova 3, 4, 9, 17, 19, 23, 24, 25 i 31. Status ostaje draft.
