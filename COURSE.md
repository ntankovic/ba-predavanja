# Blockchain Applications — course foundation

## Identity and status

- English course title: **Blockchain Applications** (lecturer supplied).
- Croatian course title: **Blockchain aplikacije** (lecturer confirmed, 2026-10-08).
- Retained foundation identity: Nikola Tanković, Faculty of Informatics, Juraj Dobrila University of Pula. Confirm teaching staff before publication; no teaching assistant assigned here.
- Croatian first, then translate reviewed content into English. English lecture titles/scopes below were supplied by the lecturer and are planning input, not reviewed teaching translations.
- Lecture 00 is a Croatian slides-only **draft**; lecture 01 has a Croatian chapter/slides **draft** (120 minutes, 48 slides, 37 illustrations); lecture 02 has a Croatian chapter/slides **draft** (110 minutes, 37 slides, 25 illustrated). Lectures 03–12 are **planned scaffolds**. A structural build is not content completion.
- Developed lectures: 90–120 minutes, 3–6 outcomes, roughly 30–40 substantive slides. Scaffold planning budget: 105 minutes.

## Pedagogical sequence

Distributed systems → lack of trusted coordinator → Byzantine consensus → cryptographic building blocks → blockchain → Bitcoin → Ethereum → smart contracts → Solidity → Web3 → IPFS → complete decentralized applications.

Weeks 1–3 establish why decentralization changes agreement and trust; week 4 introduces Bitcoin as a response to that problem. Do not introduce Bitcoin in weeks 1–2. Weeks 4–6 explain Bitcoin/UTXO/PoW and Ethereum/accounts/execution/PoS. Weeks 7–12 become increasingly practical. Introduce IPFS only after Solidity and Web3, in response to the need to store files and large application data.

Never equate distributed, decentralized and peer-to-peer. State timing, failure, membership and adversary assumptions before consensus guarantees. FLP intuition must not be presented as universal impossibility of consensus. Separate BFT fault assumptions from Sybil resistance in open membership. Hashes and signatures do not themselves choose a shared history. Explain immutability as conditional guarantees, not absolute impossibility of change. Compare chains by cumulative work where appropriate, not raw block count. Teach current Ethereum execution separately from current PoS consensus; historical PoW must be clearly labelled. Validate version-dependent claims when authoring.

## One evolving application

**Lecturer-approved opening example (2026-10-08):** Lecture 01 uses a shared digital budget: 100 units, competing internal transfers of 80 and 60. Teach agreement on digitally defined state without a physical-truth/oracle dependency. A/B/C are organizations; F/X/Y are accounts. The later application below remains provisional and does not determine the introductory example.

**Provisional later teaching example:** a collaborative registry of creative works/exhibits and provenance, not a prescribed assessed-project topic. Start with shared records and disputed authorship among organizations. Weeks 1–6 compare trust/state/consensus models without forcing a running blockchain app prematurely.

Week 7: Solidity registry → week 8: tests, permissions and deployment → week 9: Web3 frontend and wallet → week 10: IPFS media/metadata → week 11: indexer/backend and complete architecture → week 12: evaluate L1/L2 or no blockchain. Demonstrate NFTs as an optional metadata/provenance example, without requiring a tradeable token or real-money economics. Do not imply on-chain provenance proves truth of an off-chain claim. Build local-first; use test networks for teaching. Never require students to expose seed phrases or use real funds.

## Authoring and review

Read references/terminology.md. Write chapter.hr.qmd as the complete script and student-readable explanation, derive slides.hr.qmd, then translate after Croatian review. Use problem → naive design → failure → reason → improvement. Include step-by-step state transitions, misconceptions, discussion, recap and an open design challenge. Plan original editable diagrams alongside content; export SVG for HTML and vector PDF for chapters, preserve attribution, and visually inspect both. Use scripts/diagram_style.py for cards and arrows.

Every deck (00–12 and `lectures/_template`) has the attendance slide „Evidencija prisutnosti” directly after the title slide: the lecturer's QR code `assets/attendance-ba.png` linking to https://bit.ly/bc-tu-sam, with the same `.attendance-slide` style as lecture 00 (lecturer, 2026-10-28). In developed lectures the title and QR slides share the first minute (0.5 + 0.5 min).

Every `slides_version` bump in a lecture's `lecture.json` gets one dated line in the `## Promjene` changelog of that lecture's `README.md` (`- YYYY-MM-DD (v1.x): what changed`), so the footer version always maps to a recorded change (lecturer, 2026-10-28). Deferred ideas go to `BACKLOG.md`.

Use 90–120-minute lecture timing in the brief, notes, lecture.json and timing.json when fully authored. Scaffolds must stay planned and do not claim complete slide timing. The scaffold files carry visible planning labels and must not be distributed as finished teaching material. Keep lecture directories, registry and book order aligned.

AI may help write code, but students must explain and test results. Include review of plausible defects: trust in RPC/indexer, unchecked access, unsafe external calls, incorrect transaction-state UI, missing availability plan, and unwarranted guarantees. Distinguish concepts, patterns and products. Verify all technical references when drafting against primary sources; lists in sources.md are research targets, not verified citations.

### Terminal commands on slides — lecturer decision, 2026-10-28

Shell commands on slides use a terminal look, not ordinary inline code.

- **Inline command:** `` `npm start`{.cmd} `` renders as a dark pill with a green `$ ` prompt added automatically; do not type `$` yourself. Example: ``Run `cd code/01-introduction`{.cmd} then `npm start`{.cmd}.``
- **Terminal session or output (several lines):** use a fenced block ```` ```{.terminal code-line-numbers="false"} ````. Type `$ ` before each command; output lines have no prompt. It renders as a dark terminal window with three dots.
- Use `.cmd` / `.terminal` only for commands a person types in a shell (`npm`, `node`, `curl`, `nc`, `git`, `docker`, `PORT=3001 npm start` …). File names, URLs, identifiers, HTTP messages and program code keep ordinary code formatting (` ```http `, ` ```javascript `).
- Syntax highlighting is switched off inside terminal styling; colour must not split a command.
- Speaker notes and PDF chapters keep ordinary code formatting; the shared CSS lives in `publishing/slides/revealjs.yml`.

### Variables, expressions and versions on slides — lecturer decision, 2026-10-27/28

- **Variables and expressions** (n, f, v, Δ, S~x~, moments t~0~, t~1~ …, n − f, 2f + 1, n ≥ 3f + 1, n(n − 1) …) are always marked as mathematics on slides: `[n ≥ 3f + 1]{.expr}`; subscripts with `~…~`, e.g. `[S~n+1~]{.expr}`. The `.expr` style (math italic, violet ink, light violet background, no line break) lives in each lecture's `assets/lecture.css`; copy it from lecture 02 when a lecture does not have it yet. Inside headings the background is dropped. In `chapter.hr.qmd` use LaTeX math (`$n \geq 3f + 1$`), because the PDF font lacks symbols such as ≥ and ≠.
- **States** are always written S with the index as a subscript; there is no separate version symbol (v7, v8 are no longer used). A concrete state is a chip `[S~7~]{.ver .v7}` on slides and `$S_{7}$` in chapters; in diagrams write `v7` inside running text (drawn as an S₇ chip by `version_chips.py`) and `S_7` in state-card titles (drawn as S₇). The general symbol is `[S~x~]{.expr}`, with x the number of accepted transactions; code may still call that number `verzija` (lecturer, 2026-10-28).
- **Diagram shapes** (lecturer, 2026-10-29): the node card (white, blue side bar, `box()`) is **only for nodes** (organizations, servers, replicas, processes). A **state** is `state_box()` (blue-tinted card, solid rim, STANJE band); a **transaction** an amber pill; a **protocol** a violet dashed frame; **steps, actions and messages** are pills (`pill()`, numbered when they form a sequence, description below); **scenarios, cases and facts** are open panels with a coloured top rule (`panel()`); **lists of concepts** are coloured rows. A **cut link** is `cut()`: a white disc with a red × centred on the line. All in `scripts/diagram_style.py`.
- **Transactions** are written tx with a subscript index: `[tx~1~]{.tx}` on slides (amber chip, `.tx` in `lecture.css`), tx~1~ in speaker notes, `$\mathrm{tx}_{1}$` in chapters, `tx1` in diagram sources and fig-alt (drawn as an amber chip by `version_chips.py`). T1/T2 are no longer used; the bank example keeps U1, U2, K1, K2 (lecturer, 2026-10-29).
- Account names (F, X, Y), transaction names (T1, U1, K1) and organizations (A, B, C) are labels, not variables; leave them as ordinary text.

## Administrative decisions still open

Confirm teaching staff, prerequisites, credits, assessment, project teams, deadlines, reuse of previous projects, approved tools/networks, student URLs, attendance and communication channels. Do not import other courses’ rules, QR codes, holidays, grades or links. Lecture 00 is an orientation draft. Current lecturer decisions are recorded in its README.md and sources.md. On 2026-10-08 the lecturer authorized shared AI slides and assessment workflow from the reference courses, with BA-specific grading taking precedence. Reference locations: references/course-examples.md.

## Lecturer-supplied 12-week syllabus

| Week | Lecture | Core concepts |
|---|---|---|
| 01 | From Distributed to Decentralized Systems | Distributed vs decentralized vs peer-to-peer; trusted coordinator; replication; fault models; partial failures; Byzantine faults; why decentralization changes the problem |
| 02 | Consensus and the Byzantine Generals Problem | Agreement, validity, termination; Byzantine Generals; FLP intuition; quorum; BFT; Sybil attacks; why classical distributed consensus is not enough for permissionless networks |
| 03 | Blockchain Foundations | Hash functions; hash pointers; Merkle trees; digital signatures; public/private keys; transactions; blocks; append-only ledgers; immutability; blockchain as replicated state |
| 04 | Bitcoin and Proof of Work | Bitcoin architecture; UTXO model; transactions; mining; PoW; difficulty; longest/heaviest-chain rule; forks; confirmations; double spending; incentives; 51% attacks |
| 05 | Ethereum and Programmable Blockchains | From Bitcoin to Ethereum; account model vs UTXO; EVM; world state; transactions; gas; smart contracts; blocks; events; Ethereum execution model |
| 06 | Proof of Stake and Modern Ethereum | Validators; staking; proposer/attester model; finality; slashing; PoS vs PoW; consensus vs execution; L1 scalability; introduction to L2/rollups |
| 07 | Smart Contracts with Solidity | Solidity syntax; contract structure; state/storage; mappings; structs; functions; modifiers; events; inheritance/interfaces; deploying and interacting with a simple contract |
| 08 | Smart Contract Design and Security | Checks-effects-interactions; reentrancy; access control; integer/economic errors; oracle problem; front-running/MEV; upgradeability; testing; why immutable code changes software engineering |
| 09 | Web3 Application Development | dApp architecture; wallets; signing; RPC; JSON-RPC; ABI; ethers/web3 libraries; reading blockchain state; submitting transactions; events; connecting frontend ↔ wallet ↔ smart contract |
| 10 | Decentralized Storage and IPFS | Why blockchain is poor storage; content addressing; CIDs; DAGs/Merkle DAGs; IPFS nodes; pinning; availability vs permanence; IPFS + Ethereum; metadata and NFTs as a practical example |
| 11 | Blockchain Application Architectures | On-chain vs off-chain computation/storage; oracles; indexers; IPFS; backend services; identity; tokens; NFTs; DAOs; supply chain; provenance; DeFi; hybrid architectures |
| 12 | Scaling, Limitations and When to Use Blockchain | L2s and rollups; bridges; interoperability; privacy; performance/cost trade-offs; decentralization–scalability–security trade-offs; permissioned blockchains; evaluating whether an application actually needs blockchain |

### Week 1: From Distributed to Decentralized Systems

**Scope:** Distributed vs decentralized vs peer-to-peer; trusted coordinator; replication; fault models; partial failures; Byzantine faults; why decentralization changes the problem.

**Teaching question:** Tko odlučuje što vrijedi kada sudionici ne vjeruju istom koordinatoru?

**Approved scenario:** Tri organizacije vode digitalni budžet od 100 jedinica; konkurentne isplate traže 80 i 60. Jedna replika kasni, a neispravan sudionik može potvrđivati nespojive isplate.

**Handoff:** Granice povjerenja i model ispada, bez Bitcoina.

### Week 2: Consensus and the Byzantine Generals Problem

**Scope:** Agreement, validity, termination; Byzantine Generals; FLP intuition; quorum; BFT; Sybil attacks; why classical distributed consensus is not enough for permissionless networks.

**Teaching question:** Kako postići dogovor ako neki sudionici lažu, a identiteti se mogu stvarati?

**Provisional scenario:** Usporediti glasovanje poznatih sudionika s otvorenom mrežom u kojoj jedna osoba stvara više identiteta.

**Handoff:** Problem članstva, Sybil napada i uvjeta konsenzusa; bez Bitcoina.

### Week 3: Blockchain Foundations

**Scope:** Hash functions; hash pointers; Merkle trees; digital signatures; public/private keys; transactions; blocks; append-only ledgers; immutability; blockchain as replicated state.

**Teaching question:** Kako povezati provjerljive zapise i otkriti naknadnu izmjenu?

**Provisional scenario:** Promijeniti zapis u nastavnom lancu i pratiti koje se provjere mijenjaju.

**Handoff:** Blockchain kao replicirano stanje; hash sam ne osigurava konsenzus.

### Week 4: Bitcoin and Proof of Work

**Scope:** Bitcoin architecture; UTXO model; transactions; mining; PoW; difficulty; longest/heaviest-chain rule; forks; confirmations; double spending; incentives; 51% attacks.

**Teaching question:** Kako otvorena mreža bira povijest bez glasovanja po identitetu?

**Provisional scenario:** Dvije transakcije pokušavaju potrošiti isti izlaz; pratiti privremene grane i potvrde.

**Handoff:** Bitcoin model i probabilistička potvrda; precizirati kumulativni rad.

### Week 5: Ethereum and Programmable Blockchains

**Scope:** From Bitcoin to Ethereum; account model vs UTXO; EVM; world state; transactions; gas; smart contracts; blocks; events; Ethereum execution model.

**Teaching question:** Što se mijenja kada transakcija izvršava program?

**Provisional scenario:** Poziv jednostavnog ugovora mijenja stanje; usporediti uspjeh i prekinuto izvršavanje.

**Handoff:** Izvršni model prije Solidity sintakse; odvojiti izvršavanje od konsenzusa.

### Week 6: Proof of Stake and Modern Ethereum

**Scope:** Validators; staking; proposer/attester model; finality; slashing; PoS vs PoW; consensus vs execution; L1 scalability; introduction to L2/rollups.

**Teaching question:** Tko predlaže blokove i kada odluku smatramo konačnom?

**Provisional scenario:** Pratiti prijedlog bloka, glasove validatora i finalnost; usporediti s PoW modelom.

**Handoff:** Uvod u ograničenja L1 i L2; dubina rollupa u tjednu 12.

### Week 7: Smart Contracts with Solidity

**Scope:** Solidity syntax; contract structure; state/storage; mappings; structs; functions; modifiers; events; inheritance/interfaces; deploying and interacting with a simple contract.

**Teaching question:** Kako poslovna radnja postaje provjerljiva promjena stanja ugovora?

**Provisional scenario:** Izraditi registar radova/izložaka s vlasnikom, identifikatorom i događajem pri dodavanju.

**Handoff:** Prvi izvršivi dApp ugovor; lokalni lanac ili odobren testnet.

### Week 8: Smart Contract Design and Security

**Scope:** Checks-effects-interactions; reentrancy; access control; integer/economic errors; oracle problem; front-running/MEV; upgradeability; testing; why immutable code changes software engineering.

**Teaching question:** Što se događa kada nepouzdan poziv utječe na zajedničko stanje?

**Provisional scenario:** Testirati dozvole registra; odvojeno pokazati namjerno ranjiv primjer ponovnog ulaska.

**Handoff:** Testiran ugovor i reproducibilan deployment; ranjivi primjer odvojen od ispravljenog.

### Week 9: Web3 Application Development

**Scope:** dApp architecture; wallets; signing; RPC; JSON-RPC; ABI; ethers/web3 libraries; reading blockchain state; submitting transactions; events; connecting frontend ↔ wallet ↔ smart contract.

**Teaching question:** Kako korisnikov klik postaje potpisana transakcija?

**Provisional scenario:** Frontend registra čita zapise; korisnik potpisuje dodavanje rada i prati ishod.

**Handoff:** Sučelje povezano s provjerenim ugovorom; datoteke još nisu riješene.

### Week 10: Decentralized Storage and IPFS

**Scope:** Why blockchain is poor storage; content addressing; CIDs; DAGs/Merkle DAGs; IPFS nodes; pinning; availability vs permanence; IPFS + Ethereum; metadata and NFTs as a practical example.

**Teaching question:** Gdje čuvamo datoteke i velike podatke aplikacije?

**Provisional scenario:** Dodati sliku i metapodatke rada na IPFS, a referencu u registar; provjeriti dostupnost.

**Handoff:** dApp s vanjskim sadržajem i planom pinninga; NFT kao moguća nadogradnja.

### Week 11: Blockchain Application Architectures

**Scope:** On-chain vs off-chain computation/storage; oracles; indexers; IPFS; backend services; identity; tokens; NFTs; DAOs; supply chain; provenance; DeFi; hybrid architectures.

**Teaching question:** Koji dio aplikacije treba zajednički konsenzus, a koji ne?

**Provisional scenario:** Dodati pretragu/indexer i prikaz izvora podataka; usporediti scenarije provenijencije, DAO-a i DeFi-ja.

**Handoff:** Cjelovit registar s UI-jem, ugovorom, IPFS-om i izričitim vanjskim ovisnostima.

### Week 12: Scaling, Limitations and When to Use Blockchain

**Scope:** L2s and rollups; bridges; interoperability; privacy; performance/cost trade-offs; decentralization–scalability–security trade-offs; permissioned blockchains; evaluating whether an application actually needs blockchain.

**Teaching question:** Treba li ovoj aplikaciji blockchain i koju cijenu zbog toga plaćamo?

**Provisional scenario:** Usporediti isti registar na L1, L2 i običnoj bazi; obrazložiti trošak, povjerenje i dostupnost.

**Handoff:** Završna arhitekturna odluka; blockchain nije automatski najbolje rješenje.

## Communication preference — lecturer confirmed 2026-10-08

Use asynchronous Google Chat as the primary channel for course questions and project discussion. The lecturer strongly prefers it over consultations and email. Do not promote email or consultation appointments as the normal first contact. The Google Chat group is **FIPU BA** (lecturer confirmed 2026-10-12); exam-defence booking is a separate administrative step.

Uvod u 01 motivira decentralizaciju isključivom administratorskom ovlašću jedne organizacije nad zajedničkim budžetom. Sukob isplata 80/60 služi tek kasnije za analizu stanja i konkurentnosti; sam po sebi ne opravdava decentralizaciju.
