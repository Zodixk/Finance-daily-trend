# Glossario Personale — Alessandro

Ogni termine ha: definizione tecnica → spiegazione semplice → esempio pratico → perché ti riguarda.
Aggiornato progressivamente sessione per sessione.

---

## MERCATO & SENTIMENT

---

### VIX
**Definizione tecnica:** Indice di volatilità implicita calcolato dal Chicago Board Options Exchange (CBOE) sulle opzioni dell'S&P 500 a 30 giorni. Misura quanto il mercato si aspetta che i prezzi oscillino nel prossimo mese.

**In parole semplici:** È il "termometro della paura" del mercato. Quando gli investitori sono nervosi e comprano protezione (opzioni put), il VIX sale. Quando sono tranquilli, scende.

**Scale di riferimento:**
- VIX < 15 → mercato molto calmo, euforia
- VIX 15–20 → normalità
- VIX 20–30 → incertezza crescente
- VIX > 30 → paura diffusa
- VIX > 40 → panico (è successo durante COVID-2020, crisi 2008)

**Esempio pratico:** Il 16 giugno 2026 il VIX era 16.23 — mercato calmo. Ma il VIX9D (versione a 9 giorni) era 22.14 — significava che i trader stavano comprando protezione specifica per l'FOMC del 17 giugno. Il mercato era calmo in generale ma nervoso per quell'evento preciso.

**Perché ti riguarda:** VIX > 25 per 2+ settimane → il briefing ti dirà CASH-PRIORITY. VIX > 40 → opportunità di comprare il PIE AI ai minimi, ma solo quando il VIX inizia a scendere.

---

### VIX9D
**Definizione tecnica:** Variante del VIX che misura la volatilità implicita sui prossimi 9 giorni invece dei 30 standard.

**In parole semplici:** Zoom sul breve termine. Se il VIX9D è molto più alto del VIX normale, vuol dire che il mercato teme un evento specifico imminente (FOMC, dati CPI, earnings importanti), non il futuro in generale.

**Esempio pratico:** Il 17 giugno 2026: VIX30D = 20.25, VIX9D = 22.14. La differenza (+1.89 punti) segnalava che i trader stavano comprando protezione proprio per la conferenza stampa di Warsh quella sera.

**Perché ti riguarda:** Quando VIX9D > VIX30D di 2+ punti prima di un evento macro (FOMC, CPI), aspetta l'evento prima di fare mosse sul PIE AI.

---

### Bullish / Bearish
**Definizione tecnica:** Termini che descrivono la direzione attesa del mercato o di un titolo. Derivano da come attaccano un toro (dal basso verso l'alto) e un orso (dall'alto verso il basso).

**In parole semplici:**
- **Bullish** = ottimista, ci si aspetta che i prezzi salgano
- **Bearish** = pessimista, ci si aspetta che i prezzi scendano

**Esempio pratico:** Su Reddit, GOOG aveva il 38% di commenti bullish vs 19% bearish il 17 giugno — segnale che la community era ottimista su Alphabet. AMD invece aveva buzz in salita ma il titolo scendeva: il mercato era bearish, Reddit bullish — conflitto di segnali.

**Perché ti riguarda:** Il briefing ti dà il sentiment bullish/bearish per ogni ticker del PIE AI. Quando prezzo e sentiment vanno in direzioni opposte, è un segnale da monitorare attentamente.

---

### Breadth (Ampiezza di mercato)
**Definizione tecnica:** Misura della partecipazione al mercato: quante azioni stanno salendo vs quante stanno scendendo in un dato periodo.

**In parole semplici:** Immagina un concerto — breadth ti dice se stanno ballando tutti o solo quelli in prima fila. Un rally "stretto" (solo 5 mega-cap salgono mentre tutto il resto scende) è fragile. Un rally "ampio" (la maggioranza delle azioni sale) è sano e duraturo.

**Come si misura:** Il briefing usa l'Uptrend Ratio di Monty: percentuale delle ~2.800 azioni tracciate attualmente in uptrend.
- < 9.7% → mercato ipervenduto (possibile rimbalzo)
- 9.7–37% → zona normale
- > 37% → mercato surriscaldato (possibile calo)

**Esempio pratico:** Il 16 giugno 2026, solo il 28.6% delle 2.800 azioni era in uptrend — basso in assoluto, ma in miglioramento (10 giorni prima era 23.8%). Il mercato stava recuperando larghezza, non perdendola.

**Perché ti riguarda:** Se NVDA e GOOG salgono ma la breadth è bassa, il tuo PIE AI è fragile — pochi titoli tengono su tutto. Quando la breadth sale, il rally diventa più solido.

---

### Sentiment
**Definizione tecnica:** Misura qualitativa e quantitativa dell'umore collettivo degli investitori verso un asset, ottenuta analizzando social media, survey, opzioni e flussi di capitali.

**In parole semplici:** È "cosa pensa la gente" di un titolo in questo momento. Si misura su Reddit, X (Twitter), Polymarket, articoli di news, ecc.

**Esempio pratico:** AMD il 17 giugno aveva buzz in salita su Reddit (74/100, trend rising) nonostante fosse scesa del 7.3%. Questo è il classico "buy the dip" social — la gente vuole comprare il calo. Non è sempre giusto seguire il sentiment: in quel caso ARK e la CEO avevano già venduto $130M di AMD.

**Perché ti riguarda:** Il briefing usa Adanos API per darti sentiment su NVDA, AAPL, MSFT, META, GOOG, AMZN, AMD, AVGO ogni mattina. Usalo come segnale complementare, mai primario.

---

### Buzz Score
**Definizione tecnica:** Punteggio 0–100 che quantifica il volume di menzioni e discussioni attorno a un titolo su una piattaforma specifica (Reddit, X, ecc.) in un periodo dato (default: 7 giorni).

**In parole semplici:** Quanto si parla di un titolo online. 100 = tutti ne parlano, 0 = nessuno. Alto buzz può significare interesse genuino o semplice rumore speculativo.

**Importante:** Buzz alto ≠ buon investimento. GameStop nel 2021 aveva buzz altissimo su Reddit e poi è crollata dell'80%.

**Esempio pratico:** Il 17 giugno, MSFT aveva buzz 82.1/100 e AVGO 72.8/100. AVGO era il meno discusso del PIE AI — coerente con il fatto che è il più debole del gruppo dopo la miss degli earnings di giugno.

**Perché ti riguarda:** Utile per capire quali ticker del PIE AI sono "in evidenza" sul mercato. Se un ticker del tuo PIE ha buzz in calo e prezzo in calo, è un doppio segnale negativo.

---

## FEDERAL RESERVE & TASSI

---

### FOMC
**Definizione tecnica:** Federal Open Market Committee — comitato della Federal Reserve (banca centrale USA) composto da 12 membri votanti (7 governatori + 5 presidenti di banche regionali a rotazione) che decide la politica monetaria USA, principalmente il tasso sui Federal Funds.

**In parole semplici:** È il gruppo di persone più potente per i mercati finanziari mondiali. Si riunisce 8 volte l'anno e decide se alzare, tagliare o mantenere i tassi di interesse negli USA. La loro decisione influenza tutto: mutui, prestiti aziendali, valore delle azioni, cambi valutari.

**Esempio pratico:** Il 17 giugno 2026 era il primo FOMC di Kevin Warsh come nuovo presidente della Fed. La decisione (hold a 3.50–3.75%) era già scontata al 99%. La vera incognita era il tono della conferenza stampa delle 14:30 ET.

**Perché ti riguarda:** Le decisioni FOMC muovono i mercati anche del 3–5% in un giorno. Il giorno di FOMC è sempre RESTRICT per default nel tuo briefing — non fare mosse prima della conferenza stampa.

---

### Tassi di Interesse (Fed Funds Rate)
**Definizione tecnica:** Tasso al quale le banche si prestano denaro overnight tra loro, stabilito dalla Fed come strumento principale di politica monetaria.

**In parole semplici:** È il "costo del denaro" nell'economia americana. Quando la Fed alza i tassi, diventa più caro prendere soldi in prestito — per le famiglie (mutui), per le aziende (finanziare la crescita), per tutti. Quando li taglia, il denaro diventa più economico e l'economia accelera.

**Esempio pratico:**
- Tasso al 0% (2020–2022): era facilissimo prendere prestiti → aziende tech crescevano a leva → NVDA, AMD esplodevano
- Tasso al 5.25% (2023–2024): costo alto → aziende tech frenano → crollo dei multipli P/E
- Tasso al 3.50–3.75% (giugno 2026): ancora elevato ma in discesa → mercato in transizione

**Perché ti riguarda:** Tassi alti penalizzano le aziende ad alta crescita e alto P/E come quelle nel tuo PIE AI (NVDA P/E >40x, AMD P/E >60x). Quando i tassi scendono, queste aziende vengono rivalutate per prime.

---

### Dot Plot
**Definizione tecnica:** Grafico pubblicato dalla Fed 4 volte l'anno (Summary of Economic Projections) dove ogni membro del FOMC indica anonimamente dove prevede che il tasso Fed Funds sarà a fine anno, fine anno+1, fine anno+2 e nel lungo periodo.

**In parole semplici:** È come chiedere a tutti i 19 membri della Fed "dove pensi che saranno i tassi tra 1 anno?" e mettere i loro voti su un grafico. Ogni punto (dot) è un voto. La mediana dei punti è la previsione ufficiale.

**Esempio pratico:** A marzo 2026 il dot plot mostrava ancora 1 taglio atteso per fine 2026. A giugno 2026, il mercato si aspettava che il nuovo dot plot rimuovesse quell'ultimo taglio — ovvero la Fed diceva "non tagliamo più quest'anno." Questo era un segnale hawkish e pesava sui titoli tech ad alto P/E.

**Perché ti riguarda:** Ogni volta che esce un dot plot, il mercato reagisce. Se i dot salgono (più rialzi) → male per il PIE AI. Se scendono (tagli in arrivo) → bene per il PIE AI. Arriva 4 volte l'anno: marzo, giugno, settembre, dicembre.

---

### Hawkish / Dovish
**Definizione tecnica:** Aggettivi che descrivono l'orientamento di un banchiere centrale o di una politica monetaria rispetto all'inflazione e alla crescita.

**In parole semplici:**
- **Hawkish** (falco): priorità a combattere l'inflazione → alza i tassi o li mantiene alti a lungo. Male per le azioni, bene per i bond.
- **Dovish** (colomba): priorità a stimolare la crescita → taglia i tassi o li mantiene bassi. Bene per le azioni, meno per i bond.

**Esempio pratico:** Kevin Warsh è storicamente considerato hawkish. Quando ha preso il posto di Powell nel maggio 2026, il mercato ha iniziato a prezzare meno tagli perché si aspettava un approccio più aggressivo sull'inflazione.

**Perché ti riguarda:** Un Fed Chair hawkish = pressione sui titoli growth del tuo PIE AI. Un cambio di tono verso il dovish = potenziale rally, specialmente per NVDA, AMD, ASML.

---

### Fed Pivot
**Definizione tecnica:** Momento in cui la Federal Reserve cambia direzione nella politica monetaria — tipicamente dalla fase di rialzi (tightening) a quella di tagli (easing).

**In parole semplici:** Il "punto di svolta" della Fed. Storicamente, i mercati anticipano il pivot anche 6–12 mesi prima che avvenga davvero, perché iniziano a scontare tassi più bassi nel futuro.

**Esempio pratico:** Dopo i rialzi aggressivi del 2022–2023, la Fed ha iniziato a tagliare a fine 2024. I mercati avevano già iniziato a salire nella seconda metà del 2023, anticipando il pivot. Chi ha comprato NVDA o AMD durante il ribasso del 2022–2023 ha poi visto guadagni enormi.

**Perché ti riguarda:** La finestra tra l'ultimo rialzo e il primo taglio è storicamente uno dei migliori momenti per costruire posizioni su titoli growth come quelli del tuo PIE AI. Il Pattern Playbook (Sezione 7.2 del tuo profilo) descrive esattamente questa strategia.

---

### CME FedWatch
**Definizione tecnica:** Strumento del Chicago Mercantile Exchange che calcola la probabilità implicita di variazioni del tasso Fed Funds a ogni riunione FOMC, derivandola dai prezzi dei futures sui Fed Funds (contratti 30-day Federal Funds futures).

**In parole semplici:** È come un sondaggio in tempo reale su cosa si aspetta il mercato dalla Fed — ma invece di chiedere alle persone, guarda i contratti futures dove i trader mettono soldi veri. È più accurato dei sondaggi perché costa sbagliare.

**Esempio pratico:** Il 17 giugno 2026, CME FedWatch mostrava: 99% probabilità di hold, 1% probabilità di taglio. Mostrava anche 70% probabilità di almeno un rialzo entro fine 2026 — segnale che il mercato si aspettava che Warsh tornasse ad alzare i tassi prima di tagliarli.

**Perché ti riguarda:** È il riferimento principale per capire cosa "prezza" il mercato prima di ogni FOMC. Se il mercato prezza hold (99%) e arriva un taglio a sorpresa → rally. Se prezza tagli e arriva un hold → sell-off.

---

## ANALISI TECNICA

---

### 52 Week High / 52 Week Low (52w High / 52w Low)
**Definizione tecnica:** Il prezzo massimo e minimo registrato da un titolo negli ultimi 52 settimane (un anno di calendario) di contrattazioni.

**In parole semplici:** È il "range" dell'ultimo anno. Sapere dove si trova il prezzo attuale rispetto a questo range ti dice molto: vicino al massimo = momentum forte ma rischio di "vendita sui massimi"; vicino al minimo = debolezza, ma possibile rimbalzo se i fondamentali reggono.

**Esempio pratico:** Il 17 giugno 2026:
- AMD: prezzo $507, 52w high $558 → era all'91% del suo massimo annuale. Alto, ma aveva appena perso il 7.3% dal picco.
- MSFT: prezzo $393, 52w high $555 → era solo al 71% del suo massimo. Molto lontano dai massimi — più upside potenziale ma anche più debolezza recente.

**Regola del briefing:** Quando un ticker è vicino al 52w high, il briefing cerca sempre la data esatta in cui quel massimo è stato toccato e se coincide con l'ATH (All-Time High).

**Perché ti riguarda:** Comprare vicino al 52w high va bene se il titolo sta rompendo al rialzo (breakout). Comprare vicino al 52w low è rischioso a meno che ci sia un chiaro motivo per un rimbalzo.

---

### ATH (All-Time High)
**Definizione tecnica:** Il prezzo più alto mai raggiunto da un titolo dall'inizio della sua quotazione in borsa.

**In parole semplici:** Il record assoluto. Diverso dal 52w high — l'ATH è il massimo di sempre, il 52w high è il massimo dell'ultimo anno. Un titolo può avere un 52w high di $200 ma un ATH di $400 (se è crollato 2 anni fa).

**Esempio pratico:** NVDA ha toccato l'ATH a giugno 2024 sopra $140 (aggiustato per i frazionamenti). AMD aveva il 52w high a $558 a giugno 2026, ma il suo ATH era superiore — quindi $558 NON era un record assoluto.

**Perché ti riguarda:** Un titolo che rompe l'ATH non ha "resistenze" tecniche sopra — teoricamente può salire senza limiti storici. È un segnale molto bullish se accompagnato da fondamentali solidi.

---

### Stop Loss
**Definizione tecnica:** Ordine condizionato che vende automaticamente un titolo quando raggiunge un prezzo predefinito inferiore al prezzo di acquisto, limitando così la perdita massima su quella posizione.

**In parole semplici:** È il tuo "piano di uscita di emergenza". Prima di comprare decidi: "Se questo titolo scende del X%, esco automaticamente." Protegge il capitale da perdite catastrofiche.

**Esempio pratico:** Hai AMD a $547. Il tuo stop loss è 7–8%. Quindi:
- Stop a 7%: $547 × (1 - 0.07) = **$509** → vendi automaticamente
- Stop a 8%: $547 × (1 - 0.08) = **$503** → vendi automaticamente

Il 17 giugno 2026, AMD era a $507 — esattamente in zona stop. Per questo il briefing segnalava 🔴 NEAR STOP.

**Perché ti riguarda:** Il tuo limite personale è 7–8% per ogni posizione. Il PIE AI però gestisce i pesi automaticamente, quindi non puoi impostare uno stop loss diretto su AMD dentro la PIE — devi monitorare manualmente e decidere se ridurre la PIE o aggiungere fondi.

---

### Supporto e Resistenza
**Definizione tecnica:** Livelli di prezzo storici dove un titolo ha ripetutamente trovato acquirenti (supporto = pavimento) o venditori (resistenza = soffitto).

**In parole semplici:**
- **Supporto**: prezzo dove in passato l'azione ha smesso di scendere e ha rimbalzato. I compratori si fanno avanti a quel livello.
- **Resistenza**: prezzo dove l'azione fatica a salire oltre. I venditori si fanno avanti a quel livello.

**Esempio pratico:** AMD aveva un supporto importante intorno a $490–500: era un'area dove era consolidata per settimane prima del rally verso $558. Se rompe $490, il prossimo supporto era più in basso, intorno a $450.

**Regola pratica:** Quando un supporto viene rotto diventa resistenza (e viceversa). È uno dei principi più importanti dell'analisi tecnica.

**Perché ti riguarda:** Il briefing ti dà i livelli chiave di supporto/resistenza per i ticker del PIE AI nella sezione "Watchlist". Sono i prezzi a cui fare attenzione per decidere se aggiungere o ridurre.

---

### P/E Ratio (Price-to-Earnings)
**Definizione tecnica:** Rapporto tra il prezzo corrente di un'azione e gli utili per azione (EPS) degli ultimi 12 mesi (trailing P/E) o dei prossimi 12 mesi stimati (forward P/E).

**In parole semplici:** Ti dice quanto stai pagando per ogni euro/dollaro di profitto che l'azienda genera. P/E 20x = paghi $20 per $1 di utile annuale. P/E 100x = paghi $100 per $1 di utile — ci credi molto nella crescita futura.

**Esempio pratico:**
- AMD a giugno 2026: trailing P/E >100x, forward P/E >60x. Significa che il mercato si aspettava una crescita enorme degli utili futuri. Quando ARK e Lisa Su hanno venduto, il mercato ha detto "forse 100x è troppo" e il titolo ha perso il 7.3% in un giorno.
- Una banca come JPMorgan: P/E ~12x. Basso — azienda matura, crescita limitata, ma stabile.

**Perché ti riguarda:** Tutto il tuo PIE AI ha P/E elevati (growth stocks). In un ambiente di tassi alti, i titoli ad alto P/E vengono penalizzati di più — perché i profitti futuri valgono meno oggi se devi scontarli a un tasso alto. Quando i tassi scendono, il P/E può espandersi → i titoli salgono.

---

### VCP (Volatility Contraction Pattern)
**Definizione tecnica:** Pattern tecnico sviluppato da Mark Minervini: una serie di consolidamenti (stalls) con range di prezzo progressivamente più stretto e volume in calo, che culmina in un breakout su volume elevato.

**In parole semplici:** Il titolo "si comprime come una molla" — le oscillazioni di prezzo diventano sempre più piccole, il volume si secca. Poi, quando arriva la notizia giusta o il momento giusto, esplode al rialzo con volume alto. È uno dei pattern più affidabili per i titoli growth.

**Come riconoscerlo:**
1. Il titolo fa un massimo, poi corregge (es. -20%)
2. Poi rimbalza ma non torna al massimo (es. +15%)
3. Poi corregge ancora ma meno (es. -10%)
4. Ancora rimbalzo più piccolo, correzione più piccola...
5. Il range si stringe sempre di più (da -20% a -5%)
6. Volume cala durante le correzioni
7. Breakout su volume 3x la media → segnale di entrata

**Perché ti riguarda:** Il briefing usa `vcp-screener` per trovare titoli in fase di VCP. Quando un tuo ticker PIE AI è in VCP, è un potenziale punto di accumulo prima del prossimo rally.

---

### Breakout
**Definizione tecnica:** Movimento del prezzo di un titolo al di sopra di un livello di resistenza chiave (o al di sotto di un supporto, in caso di breakdown), generalmente accompagnato da un aumento del volume di negoziazione.

**In parole semplici:** È quando l'azione "sfonda" un tetto che la bloccava. Come un pugile che finalmente supera l'avversario. Per essere valido, deve avvenire su volume alto (almeno 50% sopra la media) — altrimenti è un "falso breakout" e il titolo torna indietro.

**Esempio pratico:** TSM aveva il 52w high a $450. Se il titolo supera $450 con volume alto, è un breakout — segnale bullish che potrebbe anticipare un ulteriore rally verso $470–480.

**Regola di Alessandro:** Mai entrare su un falso breakout. Il prezzo deve chiudere sopra il livello pivot, non solo toccarlo intraday.

**Perché ti riguarda:** Il Pattern Playbook descrive l'entry su breakout per VCP, Cup & Handle, Flat Base. È la strategia principale per aggiungere posizioni ai tuoi titoli del PIE AI al momento giusto.

---

### PEAD (Post-Earnings Announcement Drift)
**Definizione tecnica:** Fenomeno documentato accademicamente (Ball & Brown, 1968) secondo cui i titoli che battono le stime degli analisti tendono a continuare a salire per 30–60 giorni dopo la pubblicazione degli earnings, mentre quelli che deludono continuano a scendere.

**In parole semplici:** Quando un'azienda pubblica risultati migliori del previsto, il mercato non incorpora subito tutta l'informazione — ci mette settimane. Puoi approfittare di questo "ritardo" comprando nei 1–3 giorni dopo l'earnings beat e mantenendo per 1–2 mesi.

**Esempio pratico:** Se NVDA batte le stime il 28 luglio e sale il 5% il giorno dopo, il PEAD suggerisce che potrebbe continuare a salire nelle settimane successive. L'entry ideale è il primo giorno di pullback dopo il gap up — non il giorno stesso (troppo emozionale).

**Perché ti riguarda:** NVDA, META, MSFT sono i migliori candidati PEAD nel tuo PIE AI per via dell'alto institutional ownership. Dopo gli earnings di luglio, monitora questi tre per opportunità di accumulo.

---

## MACRO & ECONOMIA

---

### CPI (Consumer Price Index)
**Definizione tecnica:** Indice statistico che misura la variazione media nel tempo dei prezzi pagati dai consumatori urbani per un paniere fisso di beni e servizi (alimentari, energia, affitti, servizi medici, trasporti, ecc.).

**In parole semplici:** È il principale termometro dell'inflazione. Se il CPI sale del 4.2% in un anno, significa che in media tutto costa il 4.2% in più rispetto all'anno scorso. La Fed vuole tenerlo intorno al 2%.

**Esempio pratico:** A giugno 2026 il CPI USA era al 4.2% — più del doppio del target Fed del 2%. Questo è il motivo principale per cui Warsh non poteva tagliare i tassi: tagliare con inflazione al 4.2% avrebbe rischiato di far risalire ulteriormente i prezzi.

**Perché ti riguarda:** CPI alto → Fed hawkish → tassi alti → pressione sul PIE AI. CPI in discesa verso 2% → Fed dovish → tagli in arrivo → rally del PIE AI. Esce una volta al mese, sempre un market-mover.

---

### Inflazione
**Definizione tecnica:** Aumento generalizzato e sostenuto del livello dei prezzi di beni e servizi in un'economia nel tempo, che riduce il potere d'acquisto della moneta.

**In parole semplici:** I soldi valgono meno nel tempo. €100 oggi comprano meno cose di €100 dieci anni fa. Un po' di inflazione (2%) è sana — significa che l'economia cresce. Troppa inflazione (>4%) è un problema perché erode i risparmi e costringe la Fed ad alzare i tassi.

**Perché i tagli dei tassi la fanno salire:** Tassi bassi → credito più economico → famiglie e aziende spendono di più → domanda supera l'offerta → i prezzi salgono. È un effetto collaterale intenzionale dei tagli, ma se l'inflazione è già alta, rischi di peggiorare il problema.

**Perché ti riguarda:** Inflazione alta = tassi alti = male per il PIE AI (vedi P/E Ratio). Inflazione bassa = Fed può tagliare = bene per il PIE AI.

---

### Yield (Rendimento Obbligazionario)
**Definizione tecnica:** Tasso di rendimento annuo di un'obbligazione, espresso come percentuale del prezzo corrente. Inversamente correlato al prezzo dell'obbligazione: se il prezzo scende, il rendimento sale, e viceversa.

**In parole semplici:** È quanto ti paga un'obbligazione (bond) ogni anno. Il Treasury USA a 10 anni (10Y yield) è il riferimento globale. Se rende il 4.5%, significa che presti soldi al governo USA per 10 anni e ti restituiscono il 4.5% all'anno.

**La relazione con le azioni:** Se il 10Y yield sale al 5%, molti investitori preferiscono i bond (rendimento sicuro al 5%) alle azioni (rischiose). Questo sposta capitali dalle azioni ai bond → le azioni scendono.

**Esempio pratico:** A giugno 2026 il 10Y yield era al 4.28%. Non altissimo, ma abbastanza da creare pressione sui titoli ad alto P/E del PIE AI.

**Perché ti riguarda:** Quando il 10Y yield sale → attenzione al PIE AI, soprattutto ASML e NVDA (alto P/E). Quando scende → tailwind per i titoli growth.

---

### Curva dei Rendimenti (Yield Curve)
**Definizione tecnica:** Rappresentazione grafica dei rendimenti di obbligazioni dello stesso emittente (tipicamente il governo USA) a diverse scadenze (da 3 mesi a 30 anni).

**In parole semplici:** In condizioni normali, prestare soldi per più tempo dovrebbe essere pagato di più (più rischio = più rendimento). Quindi normalmente: 10Y yield > 2Y yield. Quando si inverte (2Y > 10Y), è un segnale storico di recessione in arrivo.

**Le tre forme:**
- **Normale** (10Y > 2Y): economia sana, crescita attesa
- **Piatta** (10Y ≈ 2Y): incertezza, transizione
- **Invertita** (2Y > 10Y): segnale di recessione (si è verificata prima di ogni recessione USA degli ultimi 50 anni)

**Esempio pratico:** A giugno 2026 la curva si stava "bear steepening": il 10Y saliva più velocemente del 2Y. Non è un'inversione, ma è un segnale di transizione — il mercato prezza inflazione persistente nel lungo termine.

**Perché ti riguarda:** Curva invertita per 2+ mesi → riduci AMD e QCOM (più ciclici), aumenta cash. Il briefing monitora lo spread 10Y-2Y ogni giorno.

---

### Bear Steepening
**Definizione tecnica:** Movimento della curva dei rendimenti in cui i tassi a lungo termine (10Y, 30Y) salgono più velocemente dei tassi a breve termine (2Y), causando un aumento dello spread, ma in un contesto in cui entrambi i tassi salgono.

**In parole semplici:** La curva diventa più ripida, ma "nel modo sbagliato" — non perché l'economia sia in salute (bull steepening) ma perché i mercati si aspettano inflazione persistente nel lungo termine. Chi compra bond a 10 anni vuole essere compensato di più per il rischio inflazione futura.

**Perché è negativo per le azioni growth:** Le aziende come quelle del PIE AI valgono principalmente per i profitti che faranno nei prossimi 5–10 anni. Se i tassi a lungo termine salgono, quei profitti futuri "valgono meno" oggi (il tasso di sconto aumenta → il valore presente scende).

**Perché ti riguarda:** Il macro regime detector monitorava questo segnale a giugno 2026 come fattore di rischio per il PIE AI.

---

### DXY (Dollar Index)
**Definizione tecnica:** Indice che misura il valore del dollaro USA rispetto a un paniere di 6 valute principali (EUR 57.6%, JPY 13.6%, GBP 11.9%, CAD 9.1%, SEK 4.2%, CHF 3.6%).

**In parole semplici:** Misura quanto "vale" il dollaro rispetto alle altre valute principali. DXY alto = dollaro forte. DXY basso = dollaro debole.

**L'effetto sul PIE AI:**
- **ASML** guadagna in euro ma è quotata in dollari → dollaro forte la penalizza (gli utili europei valgono meno in USD)
- **TSM** guadagna in dollari taiwanese/USD ma ha costi in TWD → impatto misto
- **NVDA, AMD, MSFT**: gran parte dei ricavi in USD, meno vulnerabili al DXY

**Perché ti riguarda:** Se DXY sale > 105 → attenzione a ASML e TSM nel PIE. Il briefing monitora DXY come parte dell'analisi macro.

---

## SETTORI & ROTAZIONE

---

### Sector Rotation (Rotazione Settoriale)
**Definizione tecnica:** Movimento sistematico di capitali da un settore dell'economia a un altro, guidato dal ciclo economico, dalle politiche monetarie o da eventi specifici.

**In parole semplici:** Gli investitori istituzionali (fondi, banche, assicurazioni) spostano continuamente i soldi tra settori. Quando tech è "in favore" (risk-on, tassi bassi, crescita), i capitali fluiscono verso NVDA, AMD, MSFT. Quando il mercato diventa difensivo (tassi alti, recessione), i capitali vanno verso Utilities, Healthcare, Consumer Staples.

**Il ciclo classico:**
1. **Early cycle** (ripresa): Finanziari, Industriali
2. **Mid cycle** (espansione): Tech, Consumer Cyclical
3. **Late cycle** (rallentamento): Energy, Materials
4. **Recession**: Utilities, Healthcare, Consumer Staples

**Esempio pratico:** Il 16 giugno 2026: XLK (tech) -2.79%, Dow Jones +0.64%, JPMorgan +3.7%. I capitali uscivano da tech ed entravano nei finanziari — classica rotazione late-cycle.

**Perché ti riguarda:** Il 100% del PIE AI è in tech/semiconduttori. Una rotazione settoriale contro tech colpisce TUTTO il portafoglio contemporaneamente. Il briefing monitora XLK ogni giorno per questo motivo.

---

### XLK
**Definizione tecnica:** SPDR Technology Select Sector ETF — replicatore passivo del settore tecnologico nell'S&P 500. Contiene principalmente Apple, NVDA, Microsoft, Broadcom, ecc.

**In parole semplici:** È il "ETF del settore tech USA". Se XLK sale, il tuo PIE AI probabilmente sale. Se XLK scende, il tuo PIE AI probabilmente scende. È il termometro diretto del tuo settore.

**Perché ti riguarda:** Il briefing confronta XLK con gli altri settori ogni giorno per capire se il tech è in favore o meno. XLK -3% mentre il Dow è flat = rotazione contro di te.

---

### Broadening Regime (Regime di Allargamento)
**Definizione tecnica:** Fase del mercato in cui i guadagni si espandono da un gruppo ristretto di mega-cap (concentrazione) a una partecipazione più ampia che include mid-cap, small-cap e titoli value/ciclici.

**In parole semplici:** In un regime di concentrazione, salgono solo i "Magnificent 7" (Apple, NVDA, Microsoft, ecc.) mentre tutto il resto è piatto. In un regime di broadening, la crescita si allarga — industriali, finanziari, small cap iniziano a salire anche loro.

**È positivo o negativo?** Per l'economia è positivo (crescita più sana e distribuita). Per il tuo PIE AI può essere temporaneamente negativo perché i capitali escono dai mega-cap tech per andare verso settori più diversificati.

**Esempio pratico:** A giugno 2026 il Macro Regime Detector segnalava Broadening con 70-90% di probabilità di transizione. 5 su 6 componenti confermavano: small-cap IWM sovraperformava SPY, RSP/SPY in risalita, credit in espansione.

**Perché ti riguarda:** In un broadening regime, considera se vale la pena aggiungere un ETF small-cap o value per bilanciare il PIE AI che è 100% large-cap tech.

---

## PORTFOLIO & RISCHIO

---

### ALLOW / RESTRICT / CASH-PRIORITY
**Definizione tecnica:** Framework di postura operativa del briefing giornaliero che sintetizza tutti i segnali di mercato in una raccomandazione d'azione.

**In parole semplici:**
- **ALLOW**: il contesto di mercato supporta nuovi investimenti. Puoi aggiungere al PIE AI o a VWCE con fiducia.
- **RESTRICT**: prudenza. Non vendere quello che hai, ma non fare nuovi acquisti importanti. Aspetta chiarezza.
- **CASH-PRIORITY**: i segnali sono negativi. Riduci l'esposizione, accumula liquidità. Non è "vendi tutto" — è "sii cauto e hai cash pronto per opportunità migliori."

**Esempio pratico:** Il 17 giugno 2026 la postura era RESTRICT pre-FOMC. Il framework post-FOMC era chiaro: Warsh neutro/dovish → passa ad ALLOW; Warsh hawkish → passa a CASH-PRIORITY.

**Perché ti riguarda:** È la raccomandazione più pratica del briefing. Come principiante, seguirla ti evita di fare mosse emotive in momenti sbagliati.

---

### Drawdown
**Definizione tecnica:** Perdita percentuale dal picco più recente del valore di un portafoglio o di un titolo. Calcolato come: (Valore Picco - Valore Attuale) / Valore Picco × 100.

**In parole semplici:** Se il tuo portafoglio valeva €1.000 e ora vale €850, il drawdown è -15%. È diverso dal rendimento totale — misura solo la perdita dal massimo recente.

**Esempio pratico:** Se hai comprato AMD a $547 e ora vale $507, il drawdown su quella posizione è -7.3%. Il tuo limite personale è -15% sul portafoglio totale e -7-8% su ogni singola posizione.

**Perché ti riguarda:** Max drawdown del 15% sul totale è il tuo limite. Se il PIE AI vale €500 e scende a €425, sei al -15% — momento di rivedere l'esposizione. Per le singole posizioni, lo stop loss del 7-8% previene che una posizione faccia troppo danno al totale.

---

### Esposizione (Exposure)
**Definizione tecnica:** Percentuale del capitale totale investita in asset rischiosi (azioni, ETF azionari) rispetto alla liquidità detenuta.

**In parole semplici:** Se hai €1.000 e hai investito €800 in azioni e €200 in cash, la tua esposizione è 80%. Alta esposizione = più guadagni se il mercato sale, più perdi se scende. Bassa esposizione = più sicurezza ma meno rendimento.

**Cosa suggerisce il briefing per ogni zona:**
- ALLOW → 90-100% investito
- RESTRICT → 70-80% investito
- CASH-PRIORITY → 50% o meno investito

**Perché ti riguarda:** Come principiante che sta costruendo il portafoglio, non devi ancora pensare a ridurre l'esposizione — stai ancora investendo. Ma è importante capire il concetto per quando il mercato diventerà più volatile.

---

### Insider Selling (Vendita degli Insider)
**Definizione tecnica:** Vendita di azioni da parte di dirigenti aziendali (CEO, CFO, CTO) o grandi azionisti (>10%) che devono dichiarare pubblicamente queste transazioni alla SEC (Securities and Exchange Commission) entro 2 giorni lavorativi.

**In parole semplici:** Quando il CEO o un grande dirigente vende azioni della propria azienda, deve dirlo pubblicamente. Non è sempre un segnale negativo (a volte vendono per pagare le tasse o diversificare), ma quando vendono grandi quantità vicino ai massimi storici, è un segnale di cautela.

**Esempio pratico:** Il 15 giugno 2026, Lisa Su (CEO di AMD) ha venduto 125.000 azioni per $57.6 milioni mentre il titolo era vicino al 52w high di $558. Lo stesso giorno ARK (Cathie Wood) ha venduto 141.000 azioni per $72.3 milioni. Due grandi venditori allo stesso tempo vicino ai massimi — segnale che il titolo era sopravvalutato.

**Perché ti riguarda:** Quando il briefing segnala insider selling su un ticker del PIE AI, è un motivo in più per non aggiungere in quel momento.

---

### Composite Confidence
**Definizione tecnica:** Punteggio aggregato 0-92% che sintetizza l'affidabilità del briefing giornaliero, calcolato come media ponderata dei livelli di fiducia di ogni skill eseguita (HIGH ≥75%, MEDIUM 50-74%, LOW <50%), con cap automatici in caso di eventi binari o segnali contrastanti.

**In parole semplici:** È una misura di quanto il briefing stesso è affidabile quel giorno. Se tutti gli strumenti funzionano e i segnali sono coerenti → confidence alta (~80-90%). Se mancano dati o i segnali si contraddicono → confidence bassa (~50-60%).

**Cap automatici:**
- FOMC day → max 60% (troppa incertezza)
- VIX > 30 → max 70%
- Regime Steps 1+2 si contraddicono → max 60%
- Più di 2 skill falliscono → max 55%

**Esempio pratico:** Il 17 giugno 2026 la confidence era 60% — capped dal FOMC. Significa: "i dati che abbiamo sono buoni, ma c'è un evento imprevedibile oggi che rende qualsiasi previsione poco affidabile."

**Non arriva mai al 100%** per principio — i mercati sono intrinsecamente incerti.

**Perché ti riguarda:** Usa la confidence come "volume" delle raccomandazioni. Confidence 85% + ALLOW = investi con fiducia. Confidence 55% + RESTRICT = aspetta davvero.

---

## STRUMENTI & PIATTAFORME

---

### Trader 212
**Definizione tecnica:** Broker online regolamentato (FCA UK, CySEC EU) che offre trading di azioni, ETF e CFD con commissioni zero, disponibile anche in Italia tramite l'app mobile.

**In parole semplici:** È il tuo broker — la piattaforma dove compri e vendi azioni ed ETF. Ha una funzione speciale chiamata PIE che permette di creare portafogli automatici con pesi predefiniti.

**Perché ti riguarda:** Tutte le tue posizioni sono su Trader 212. I pesi del PIE AI vengono gestiti automaticamente dalla piattaforma secondo le percentuali che hai impostato (NVDA 12%, gli altri 8%).

---

### PIE (Trader 212)
**Definizione tecnica:** Funzionalità di Trader 212 che permette di creare un portafoglio tematico con allocazioni percentuali predefinite. I fondi aggiunti vengono automaticamente distribuiti tra i titoli secondo i pesi impostati. Il ribilanciamento avviene automaticamente.

**In parole semplici:** È un "cestino automatico" di azioni. Tu dici "voglio 12% NVDA e 8% di tutto il resto" e Trader 212 ci pensa lui ogni volta che aggiungi soldi. Non devi comprare manualmente ogni titolo.

**Importante capire:** Quando aggiungi €100 al PIE, vengono distribuiti su TUTTI i 12 ticker secondo i pesi. Non puoi dire "metti questi €100 solo su GOOG."

**Perché ti riguarda:** Ogni volta che vuoi aggiungere fondi, il briefing ti dice se è un buon momento per farlo in base al mercato. Ma la distribuzione la decide Trader 212 automaticamente.

---

### VWCE.DE
**Definizione tecnica:** Vanguard FTSE All-World UCITS ETF Accumulating, quotato sulla borsa tedesca XETRA con ticker VWCE.DE. Replica l'indice FTSE All-World che copre ~4.000 azioni di paesi sviluppati ed emergenti.

**In parole semplici:** È il tuo "investimento sicuro" a lungo termine. Invece di scommettere su singole aziende, compri un pezzo di quasi tutte le grandi aziende del mondo in un solo titolo.

**Caratteristiche chiave:**
- **Accumulante**: non paga dividendi in cash — li reinveste automaticamente (ottimo fiscalmente in Italia: tassato solo quando vendi)
- **Diversificato**: ~60-65% USA, ~10% Europa, ~8% Giappone, resto del mondo
- **Costo basso**: TER (costo annuale) ~0.22% — quasi gratis
- **Valuta**: quotato in EUR, ma contiene azioni in tutte le valute

**FTSE All-World**: è l'indice che VWCE replica. "FTSE" sta per Financial Times Stock Exchange (l'azienda che costruisce l'indice). "All-World" significa globale, sviluppati + emergenti.

**Perché ti riguarda:** È il tuo "ancoraggio" — non venderlo mai a meno di eventi macro estremi. Mentre il PIE AI è la tua scommessa sulla crescita tech, VWCE è la tua assicurazione sul lungo termine globale.

---

### FMP (Financial Modeling Prep)
**Definizione tecnica:** API finanziaria che fornisce dati in tempo reale e storici su azioni, ETF, indici, earnings, bilanci aziendali e dati macroeconomici.

**In parole semplici:** È il "database finanziario" che il briefing usa per ottenere i prezzi del PIE AI ogni mattina. Piano gratuito: 250 chiamate al giorno, un ticker alla volta.

**Perché ti riguarda:** Se il briefing segnala "FMP HTTP 402" su un ticker, significa che quel ticker richiede un piano premium. In quel caso il briefing usa yfinance come backup.

---

### Adanos Finance API
**Definizione tecnica:** API di sentiment analysis che aggrega e quantifica le discussioni su Reddit, X (Twitter), articoli di news e Polymarket per singoli ticker azionari, producendo metriche come buzz_score, bullish_pct, trend.

**In parole semplici:** È lo strumento che il briefing usa per misurare "cosa dice Internet" sui tuoi titoli. Analizza migliaia di post su Reddit e X ogni giorno e li trasforma in numeri (buzz 0-100, % bullish, % bearish, trend in salita/discesa).

**Perché ti riguarda:** Il sentiment da Adanos è un segnale complementare — non primario. Utile per capire se c'è "buy the dip" o "sell the rally" in atto sul tuo PIE AI.

---

### Polymarket
**Definizione tecnica:** Piattaforma di prediction market decentralizzata basata su blockchain dove gli utenti scommettono con criptovalute su eventi futuri (politici, economici, sportivi). Le probabilità riflettono l'aggregazione delle aspettative dei partecipanti.

**In parole semplici:** È un mercato dove le persone scommettono con soldi veri su cosa accadrà. Se il 99% dei soldi è scommesso su "la Fed non taglia a giugno", quella è la migliore stima collettiva disponibile. È più affidabile dei sondaggi perché chi sbaglia perde denaro reale.

**Esempio pratico:** Il 17 giugno 2026: Polymarket mostrava 99% probabilità di hold Fed. Questo era il segnale più forte che il mercato aveva già "prezzato" il hold — non ci sarebbe stata sorpresa e il movimento di mercato dipendeva solo dal tono di Warsh.

**Perché ti riguarda:** Il briefing usa le probabilità di Polymarket per calibrare l'incertezza su eventi macro (FOMC, CPI, elezioni). Alta probabilità = evento già prezzato = poca sorpresa attesa.

---

*Ultimo aggiornamento: 2026-06-17*
*Prossima aggiunta: aggiungi qui i termini che vuoi imparare nelle prossime sessioni.*
