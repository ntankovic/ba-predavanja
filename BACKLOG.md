# Backlog

Ideje i zadaci koje je nastavnik odgodio. Stavka se ne radi dok je nastavnik ne pokrene.

## Praćenje dokle se stiglo s predavanjima (redovni i online studenti)

Dodano 2026-10-28; nastavnik: „za sada ništa od ovoga”.

Cilj: za svaku grupu znati zadnji obrađeni slajd i od kojeg slajda nastaviti.

- **Ručno:** `just stop <predavanje> <grupa> <slajd> "<bilješka>"` upisuje redak u `teaching-log.md`/`.json` (datum, grupa, predavanje, broj i naslov slajda, verzija decka); `just where` ispisuje gdje svaka grupa nastavlja. Bilježiti naslov, ne samo broj, jer se brojevi mijenjaju kad umetnemo slajdove.
- **Automatski u decku:** `schedule.json` s terminima grupa; deck u terminu nastave pri svakom prelasku slajda bilježi grupu, zadnji i najdalji slajd. Pri sljedećem otvaranju u terminu iste grupe pokazuje traku „prošli put do …, nastavi →”; izvan termina ne bilježi ništa.
  - Razina 1: localStorage u pregledniku (radi offline, ali samo na računalu s kojeg se predaje).
  - Razina 2 (preporuka): `just present <predavanje>` pokreće lokalni poslužitelj koji prikazuje deck i upisuje prelaske u `teaching-log.json`, pa `just where` i agent vide stanje.
- **Alternativa:** stranica za praćenje (Artifact s bazom) za upis s mobitela.

Potrebno prije izrade: termini redovnih i online studenata (dan, sat), predaje li se s istog računala i iz istog decka, odabir razine.
