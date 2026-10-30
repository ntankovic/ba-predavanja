# Izvori i odluke — 2026-10-08

## Nastavnikovi izvori

Točne lokalne lokacije: ../../references/course-examples.md.

- BA-01.pdf, str. 3–7: autor/kontakt, cilj, projekt, individualna obrana i rokovi. Novi naslov i titula prema aktualnom projektu.
- BA-01.pdf, str. 19–32: ideje za projekt (budžet, prikupljanje sredstava, glasovanje, transparentnost). Povijesne cijene, hype krivulje i proizvodi nisu predstavljeni kao aktualni.
- COURSE.md: plan od 12 tjedana, nastavni registar, postupno uvođenje protokola, testne mreže i AI odgovornost.
- Izravne upute nastavnika u razgovoru 2026-10-08: prosjek predavanja/vježbi; 5 i 2 daju 4; vježbe 1/nedostaje → usmeni; ocjena usmenog je konačna; zadržati AI slajdove i hodogram, primijeniti zajednička pravila.
- Izravne upute nastavnika 2026-10-12: zaokruživanje 3,5 → 4 (polovica naviše); rezervacija obrane na https://ntankovic.unipu.hr/termin prema RS uvodu; AI pravila preuzeta iz RS/WA ai-policy.hr.md u lokalni ai-policy.hr.md.
- RS: lectures/00-course-introduction/slides.hr.qmd, sources.md i assets/hodogram_rs.png. Sources.md sadrži kasnije ispravke: uklanjanje 7 dana, 3 radna dana do obrane, oslobođenje i prijava roka. Izvorni PNG arhiviran kao assessment-flow.original.png, ponovno prikazan na izričiti zahtjev nastavnika.
- WA: lectures/00-course-introduction/slides.hr.qmd i sources.md: zajednički način rada, nadogradnja prethodnog projekta, 12 AI ideja, AI alati, kalendar i Git primjer. Korisnik je izričito odobrio primjenu zajedničkih sadržaja. Nisu preneseni WA kurikulum, URL predmeta ni WA/RS QR.

## Primarni tehnički izvori, pregledani 2026-10-08

- https://ethereum.org/en/developers/docs/smart-contracts/ — ugovor kao kod i stanje, vanjski podaci zahtijevaju dodatni izvor; uvod i projektne odgovornosti.
- https://docs.ipfs.tech/concepts/what-is-ipfs/ — pohrana/adresiranje sadržaja; samo najava teme u planu.
- https://code.claude.com/docs/en/overview — pomoć pri izmjenama koda.
- https://claude.com/product/design — vizualni prototipovi; zadržan alat iz referentnog slajda.
- https://learn.chatgpt.com/docs/code-review — pregled koda uz Codex.
- https://github.com/QwenLM/Qwen3-Coder i https://github.com/deepseek-ai/DeepSeek-Coder-V2 — modeli s dostupnim težinama; licence ovise o modelu. Ne tvrdi se besplatna usluga, određeni hardverski minimum niti rang-lista kvalitete.

## Podrijetlo preuzetih vizuala

- ai-responsibility.hr.svg/.pdf: originalni diagram iz RS/WA; nastavnikova politika odgovornosti.
- github-history.hr.svg/.pdf, submission-calendar.hr.svg/.pdf, academic-year.hr.svg/.pdf: prilagođene originalne ilustracije iz WA; Git poruke izmijenjene za BA registar, kalendarski primjer preciziran na termin obrane bez blagdana i datumi koje je nastavnik naveo u referentnom kolegiju te sada odobrio zajednička pravila.
- undraw-teaching.svg/.pdf: Katerina Limpitsouni / unDraw, https://undraw.co/illustration/teaching_58yg, licenca https://undraw.co/license. Izvorni SVG sačuvan; plavi akcent preuzet iz referentnog projekta.
- claude-app.png i codex-app.png: ikone bez grafičkih izmjena iz instaliranih Claude.app/Codex.app, prema WA sources.md; koriste se za identifikaciju proizvoda, žigovi pripadaju vlasnicima.
- Novi dijagrami shared-record, project-path i assessment-flow: autorski, izvor assets/build_diagrams.py i zajednički scripts/diagram_style.py; SVG i vektorski PDF. Hodogram je adaptacija nastavnikova referentnog procesa, s novim BA pravilima.

## Korekcija projektnih ideja — 2026-10-08

Uklonjena sva tri slajda s 12 generičkih AI/web ideja bez opravdane uloge blockchaina (uključujući hladnjak). Preostale četiri teme precizirane su kroz pravila raspolaganja sredstvima ili zajedničku provjeru zapisa više organizacija; pretpostavke i ograničenja u bilješkama. AI alati i odgovornost za kod ostaju. Aktualno: 27 slajdova / 32.5 minuta. Timing i metadata usklađeni; prethodni brojevi opisuju raniju verziju.

2026-10-08 — Nastavnik je zatražio povratak svojeg izvornog dijagrama. Slajd koristi assessment-flow.original.png bez izmjena, s lightbox povećanjem i vidljivim pojašnjenjem aktualnog roka i uvjeta oslobođenja. Novi SVG hodogram ostaje neupotrijebljena radna inačica.

2026-10-08 — Vraćen izvorni nastavnikov hodogram. Smanjen natpis OBRANA u kalendaru s 34 na 26 px radi unutarnjeg razmaka. Kontaktni slajd sada upućuje na asinkroni Google Chat; e-pošta uklonjena prema izričitoj nastavnikovoj preferenciji. Točan naziv/poveznica grupe još nije dostavljen.

## WA stil i dopune, 2026-10-12

Uspoređeni aktualni lokalni `FIPU-WA/wa-predavanja-v2/lectures/00-course-introduction/slides.hr.qmd`, `assets/lecture.css` i `assets/build_orientation_visuals.py`. Prenesena je vizualna struktura predznanja, kartica projektnih ideja, doprinosa i vizualnog objašnjenja obrane. Tri nedostajuća tematska slajda prilagođena su BA programu i ranije odobrenim pravilima. WA pitanja za usmeni nisu BA izvor ispitnih pitanja. Nove ilustracije course-focus, ba-evidence i ba-change autorske su BA prilagodbe; izmjenjivi izvor je assets/build_diagrams.py, izvozi SVG/PDF.
- RS uvod, `FIPU-RS/rs-predavanja-v2/lectures/00-course-introduction/slides.hr.qmd` (slajdovi 4–5, „Commitovi i individualni doprinos”, „Dorada projekta: objasnite izmjenu”) i `assets/lecture.css`, pregledano 2026-10-13. Nastavnik je za BA potvrdio da nisu sva predavanja snimljena te odobrio pravilo o commitovima, doradu umjesto izmjene uživo, AI redoslijed s neobaveznim README odjeljkom i RS tipografiju/dijagrame. Formulacije su prilagođene BA-u (bez snimki, Google Chat „FIPU BA”, primjeri pametnih ugovora).
- google-chat.svg (+ PDF): službena ikona Google Chata, Wikimedia Commons, „File:Google Chat icon (2023).svg”, https://commons.wikimedia.org/wiki/File:Google_Chat_icon_(2023).svg, preuzeto 2026-10-13 bez grafičkih izmjena; koristi se samo za identifikaciju kanala, žig pripada Googleu.
- Zakon o visokom obrazovanju i znanstvenoj djelatnosti, NN 119/22, čl. 67. st. 2. (https://narodne-novine.nn.hr/clanci/sluzbeni/2022_10_119_1834.html, provjereno 2026-10-14): „Jedan ECTS bod predstavlja 30 sati procijenjenog prosječno utrošenog studentskog rada pri ostvarivanju ishoda učenja.” Osnova za 6 ECTS ≈ 180 h i 30 ECTS ≈ 900 h na slajdu o diplomskom radu.
- UNIPU Pravilnik o studiranju, pročišćeni tekst rujan 2019. (https://www.unipu.hr/_download/repository/2019-09-30-Pravilnik_o_studiranju-procisceni_tekst%5B1%5D.pdf) i izmjene do 7. 12. 2021. (popis na https://student.unipu.hr/dokumenti/dokumenti_za_studente): pregledan tekst; broj sati po ECTS bodu nije propisan. Stari Pravilnik o studiju (pročišćeni tekst 26. 9. 2011., čl. 28.) navodio je 1 ECTS = 28 sati; zamijenjen je pa se ne koristi.
- attendance-ba.png: QR kod za evidenciju prisutnosti, dostavio nastavnik 2026-10-14; dekodirani sadržaj je https://bit.ly/bc-tu-sam (zxing-cpp). Raspored slajda preuzet iz WA uvoda.
- assets/tech/*.svg (+ PDF): Solidity, OpenZeppelin, Vite, Vue.js, IPFS i Python iz Simple Icons 13.21.0 (CC0, https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/), obojeni službenim hex bojama iz podataka Simple Icons. Pinia je kopija tech-pinia.svg iz WA uvoda (pojednostavljena oznaka). viem i Foundry su pojednostavljene autorske oznake u build_orientation_visuals.py, ne službeni logotipi. Žigovi pripadaju vlasnicima; ikone služe samo za identifikaciju.
- Stanje biblioteka, provjereno 2026-10-14: web3.js je arhiviran 4. 3. 2025.; ChainSafe preporučuje viem ili ethers.js (https://blog.chainsafe.io/web3-js-sunset/). web3.py: aktualna stabilna 7.16.0 (svibanj 2026.), autor Ethereum Foundation (https://pypi.org/project/web3).
- K. Wüst, A. Gervais, „Do you need a Blockchain?”, IEEE CVCBT 2018; preprint https://eprint.iacr.org/2017/375 (tekst i Fig. 1 provjereni 2026-10-14 iz UCL kopije https://discovery.ucl.ac.uk/10182342/1/2017-375.pdf). Osnova slajda 15 i usporedbe cijene na slajdu 16.
- EDPB, Smjernice 02/2025 o obradi osobnih podataka putem blockchain tehnologija (travanj 2025., javno savjetovanje do 9. 6. 2025.), https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-022025-processing-personal-data_hr. Sadržaj preporuke (osobne podatke držati izvan *blockchaina*; sažetak nije anonimizacija) provjeren samo kroz sekundarne sažetke; konačno usvajanje nije potvrđeno.
- RFC 9162, Certificate Transparency Version 2.0 (primjer javnog dnevnika koji samo dodaje zapise).
- V. Buterin, Z. Hitzig, E. G. Weyl, „A Flexible Design for Funding Public Goods”, Management Science 65(11), 2019 (kvadratno financiranje).
- BA-01.pdf, str. 9–11 (stari dijagram „Do you need a blockchain”, izvor nije naveden), 20–21, 26–32 (kategorije, istraživanje, misao vodilja).
- K. Croman et al., „On Scaling Decentralized Blockchains (A Position Paper)”, FC 2016 Workshops (BITCOIN), LNCS 9604: propusnost Bitcoina oko 7 transakcija/s; cilj od 10 min po bloku prema Bitcoin dokumentaciji. Koristi se kao primjer na slajdu 17.
