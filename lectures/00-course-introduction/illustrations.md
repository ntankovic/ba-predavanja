# Ilustracije predavanja 00

| Vizual | Svrha | Izvor / format |
|---|---|---|
| shared-record.hr | Proturječni zapisi triju organizacija | build_diagrams.py; SVG/PDF |
| project-path.hr | Od problema do provjere projekta | build_diagrams.py; SVG/PDF |
| assessment-flow.hr | Paralelni rad i dva puta ocjenjivanja | build_diagrams.py; SVG/PDF; BA pravila |
| ai-responsibility.hr | Odgovornost studenta za AI kod | RS/WA SVG/PDF |
| github-history.hr | Individualni doprinos | WA SVG/PDF, izmišljeni primjer |
| submission-calendar.hr | Tri radna dana | WA SVG/PDF |
| academic-year.hr | Rok akademske godine i godišnji odmor | WA SVG/PDF |
| undraw-teaching | Sudjelovanje u nastavi | unDraw preko referentnog projekta |
| Claude/Codex ikone | Identifikacija alata | PNG, podrijetlo u sources.md |

Izvorni hodogram assessment-flow.original.png prikazan je na nastavnikov zahtjev, uz pojašnjenje aktualnih pravila. SVG i PDF novih dijagrama stvaraju se naredbom `python3 lectures/00-course-introduction/assets/build_diagrams.py`. Vizualna provjera PDF dijagrama odvojena je od blokirane headless HTML provjere.

2026-10-08 — Nastavnik je zatražio povratak svojeg izvornog dijagrama. Slajd koristi assessment-flow.original.png bez izmjena, s lightbox povećanjem i vidljivim pojašnjenjem aktualnog roka i uvjeta oslobođenja. Novi SVG hodogram ostaje neupotrijebljena radna inačica.

2026-10-12: WA raspored prenesen na BA kartice i vizualne slajdove. Novi SVG/PDF parovi: course-focus.hr (radnja, ugovor, mreža), ba-evidence.hr (predviđanje, prikaz, objašnjenje), ba-change.hr (odredi, izmijeni, provjeri). shared-record.hr sada prikazuje organizacije i zajednički digitalni budžet. Pregledani rasterizirani PDF izvozi svih četiriju ilustracija; bez odrezanog teksta. Izvorni hodogram i BA kalendar ostaju sačuvani.

2026-10-13: ba-change.hr zamijenjen je s design-change.hr (Gdje? → Kako? → Posljedice?), izvor build_diagrams.py. github-history.hr dobio je datume i oznaku „nekoliko commitova tjedno, 3 tjedna”; novi izmjenjivi izvor je build_orientation_visuals.py, prilagođen iz RS-a, s BA porukama commitova. Oba dijagrama koriste WA/RS stil kartica. Pregledane su snimke HTML-a iz headless Chromea.

2026-10-14: ikone project-app.svg, project-contract.svg i project-chain.svg (+ PDF) jednostavni su autorski linijski crteži u naglasnoj boji decka; izvor je build_orientation_visuals.py. Pregledano u HTML snimci slajda 14.

2026-10-14: need-blockchain.hr (SVG i PDF) je stablo odluke s pet pitanja i šest ishoda. Izvor je build_diagrams.py, a autorski je prikaz prema Wüst i Gervais (2018, Fig. 1). Ishodi s *blockchainom* su plavi, a oni s bazom sivi; riječ *blockchain* je u kurzivu. Pregledano u HTML snimci slajda 15.

2026-10-14: need-blockchain.hr zamijenjen je s need-blockchain-1.hr i need-blockchain-2.hr (SVG i PDF, statično za PDF) te inline kopijama _need-blockchain-1/2.hr.qmd u kojima je svaki korak Reveal fragment. Sve generira build_diagrams.py. Oznake DA/NE su chipovi (DA plavo, NE sivo). Pregledano u headless snimkama početnog, srednjeg i završnog stanja.
2026-10-19: iz need-blockchain-1.hr uklonjen je korak „Više strana” (NE → obična baza); prvi dio sada ima stanje → posrednik → dalje. Izvor je build_diagrams.py.
2026-10-20: stablo need-blockchain-1/2.hr preuređeno je prema nastavniku. Prvi dio: dijeljenje (NE → SQLite ili datoteka) → međusobno povjerenje (DA → baza kod bilo koga) → dalje. Drugi dio: jedan dionik od povjerenja (DA → baza kod njega) → poznati dionici (DA → privatni *blockchain*, NE → javni *blockchain*). Izvor je build_diagrams.py.
