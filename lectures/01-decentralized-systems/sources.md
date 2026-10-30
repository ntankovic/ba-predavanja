# Izvori i provenijencija — predavanje 01

Pregledano 2026-10-08. Izvori podupiru označene tehničke tvrdnje; digitalni budžet, tragovi poruka, zadaci i svi dijagrami autorski su nastavni primjeri. Nema preuzetih slika ili dugih citata.

| Izvor | Pregledani dio | Primjena |
|---|---|---|
| Jim Waldo, Geoff Wyant, Ann Wollrath, Sam Kendall, *A Note on Distributed Computing*, SMLI TR-94-29, studeni 1994. [Harvardova stranica](https://waldo.scholars.harvard.edu/publications/note-distributed-computing), [cijeli PDF](https://waldo.scholars.harvard.edu/sites/g/files/omnuum6261/files/waldo/files/waldo-94.pdf) | §4.3, tiskane str. 7–8 | Djelomični ispadi, konkurentnost i neizvjesnost o ishodu udaljenog poziva. Slajdovi 15, 17, 19. Pronađen je cijeli rad, ne samo bibliografski zapis. |
| [RFC 5694: Peer-to-Peer (P2P) Architecture: Definition, Taxonomies, Examples, and Applicability](https://www.rfc-editor.org/rfc/rfc5694), studeni 2009. | §2–4 | Razlikovanje uloga traženja/pružanja resursa i mogućnost središnjih funkcija u P2P sustavu. Slajdovi 22–25. Nije tvrdnja da P2P automatski decentralizira upravljanje. |
| Leslie Lamport, Robert Shostak, Marshall Pease, [The Byzantine Generals Problem](https://lamport.azurewebsites.net/pubs/byz.pdf), ACM TOPLAS 4(3), 1982. | Uvod i formulacija problema | Proizvoljno ponašanje i proturječne informacije različitim primateljima. Slajdovi 28–32. Algoritmi i granice broja ispada ostavljeni su za 02. |
| Malcolm Featonby, [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), Amazon Builders’ Library | Client request identifiers, atomarnost i ista oznaka uz drukčiju namjeru | Slajd 16: ponavljanje iste namjere, stabilan identifikator i veza zapisa identifikatora s učinkom. Nema obećanja da svaki API automatski pruža idempotentnost. |
| [PostgreSQL 18: Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html) | §13.2.1, uvjet ažuriranja pri konkurentnom UPDATE-u | Pozadina za slajdove 9–10: provjera verzije i promjena moraju biti jedna atomarna odluka. Nastavni pseudokod nije univerzalna tvrdnja o svim izolacijskim razinama. |

## Nastavnikov prethodni PDF

Lokalni izvor: `/Users/ntankovic/Dropbox/1_UNIPU/1_NASTAVA/FIPU-BLOCKCHAIN/BA-01.pdf` (56 stranica).

Pregledani relevantni dijelovi: str. 39 (promjena stanja), 40–41 (centralizirani/raspodijeljeni prikaz), 45–49 (konzistentnost), 52 (replike za čitanje). Zadržana je problemska nit: stanje → koordinator → kopije → različiti pogledi. Tekst i crteži napisani su iznova oko zajedničkog stanja, uz izričite pretpostavke. Pojednostavljene tvrdnje o trenutačno jednakim kopijama i vezi konzistentnosti/konsenzusa nisu prenesene. CAP, Paxos/Raft i valuta nisu dio ovog uvoda.

## Opseg provjere

Ne citiramo radove kojima nije pregledan puni relevantni tekst. Nema neriješene tehničke tvrdnje oslonjene na nedostupan Harvardov PDF. Terminologija ostaje podložna nastavnikovu pregledu prema `references/terminology.md`.

## Institucije i cijena spora — dopuna uvoda

- [ECB: What is T2?](https://www.ecb.europa.eu/ecb-and-you/explainers/tell-me/html/what-is-t2.en.html): konkretan primjer poravnanja u novcu središnje banke u stvarnom vremenu. Ne prikazujemo sud kao redoviti korak poravnanja.
- [Europska komisija, 2025 Rule of Law Report — Croatia](https://commission.europa.eu/document/download/920cc4c5-ceef-4072-9d5c-95ef1bba1f78_en?filename=15_1_63948_coun_chap_croatia_en.pdf), str. 6, odjeljak Efficiency i bilješka 24: prosječno 1.147 dana u prvostupanjskim trgovačkim parnicama u 2024. Jasno navedena kategorija, godina i opseg; nije statistika međubankovnih sporova ili brzine plaćanja. Pregledan puni relevantni odjeljak 2026-10-08.
- [Europski portal e-pravosuđa: How to bring a case to court — Croatia](https://e-justice.europa.eu/topics/taking-legal-action/where-and-how/how-bring-case-court/hr_en): pristojbe i naknade za odvjetnički rad; nema univerzalne cijene postupka. Pregledan indeksirani izvadak službenog izvora.
- Iznos 15.000 € isključivo je autorski računski primjer: 100.000 × 0,05 × 3. Nije tarifa, sudska kamata, statistički podatak ili obećana ušteda.
- Smanjenje neslaganja o prihvaćenom digitalnom stanju postavljeno je kao projektni cilj uz pretpostavke protokola, ne tvrdnja da blockchain zamjenjuje sudove ili uvijek snižava ukupne troškove.

## Jedna baza i motivacija replikacije

Pregledano 2026-10-08: [PostgreSQL 18, Explicit Locking, §13.3.2](https://www.postgresql.org/docs/18/explicit-locking.html#LOCKING-ROWS) za zaključavanje retka do završetka transakcije; [PostgreSQL 18, Log-Shipping Standby Servers](https://www.postgresql.org/docs/18/warm-standby.html) za čitanja sa standby poslužitelja, oporavak i mogući gubitak potvrđenih promjena pri asinkronoj replikaciji. Nastavni slijed izričito je ograničen na jednu bazu i pouzdanog operatora.

- ECB, Eurosystem policy on access by non-bank PSPs to central bank payment systems (19. 7. 2024.), https://www.ecb.europa.eu/press/intro/news/html/ecb.mipnews240719.en.html
- ECB, TARGET Services Pricing Guide v3.0 (srpanj 2026.), https://www.ecb.europa.eu/paym/target/coco/shared/docs/ecb.pricingcoco_target_2026_v3.0.en.pdf. Iznosi RTGS-a provjereni u tekstu cjenika; nije potvrđeno odražavaju li reviziju cijena iz 2026.

## Definicije 1.1 i 1.2 (2026-10-21)

- Definicija 1.1 preuzeta je iz RS 01 (`FIPU-RS/rs-predavanja-v2/lectures/01-foundations/slides.hr.qmd`, Definicija 1.1).
- V. Buterin, „The Meaning of Decentralization”, Medium, veljača 2017., https://medium.com/@VitalikButerin/the-meaning-of-decentralization-a0c92b76a274: arhitekturna, politička i logička decentralizacija. Sažetak je provjeren sekundarnim izvorima 2026-10-21; izvorni tekst nije ponovno pročitan.
- M. van Steen i A. S. Tanenbaum, *Distributed Systems*, 4. izd. (v4.01, siječanj 2023.), §1.1: decentraliziran = procesi i resursi *nužno* raspoređeni na više računala; raspodijeljen = *dovoljno* raspoređeni. Provjereno 2026-10-21 prema autorskim slajdovima (https://ceres.cs.umd.edu/o/slides/Distributed_Systems_v4.pdf), ne prema tekstu knjige; točnu formulaciju treba provjeriti u knjizi.
