---
name: finance-briefing-web
description: >
  Briefing finanziario completo per il portafoglio di Alessandro. Versione claude.ai:
  usa web search invece di API/script. Copertua completa: mercato, regime, quote PIE AI,
  news, sentiment, calendario, settori, esposizione, sezione "Cosa fare".
  Trigger: "briefing", "analisi mercato", "come va oggi", "situazione portafoglio".
---

# Finance Briefing — Alessandro (claude.ai Edition)

Esegui questo briefing ogni volta che l'utente scrive "briefing", "analisi mercato",
"come va oggi", "situazione portafoglio" o simili.

---

## Profilo investitore (sempre attivo)

- **Chi:** Alessandro, principiante assoluto, EUR, broker Trader 212
- **PIE AI:** GOOG, AMZN, AVGO, NVDA, AMD, AAPL, ASML, CSCO, META, MSFT, QCOM, TSM
- **ETF Core:** FTDL.DE — All-World accumulating, XETRA (ancora a lungo termine, mai vendere interamente)
- **Rischio:** stop default 7-8% | max posizione 10% | max drawdown portafoglio 15%
- **Output:** sempre in italiano, linguaggio semplice, per ogni segnale indica quale ticker PIE AI è impattato

---

## Regole analisi (obbligatorie)

1. **Copertura massima** — esegui TUTTI i passi, nessuno opzionale
2. **Mai inventare numeri** — se non trovi un dato, scrivi ⚠️ dato non disponibile
3. **Sezione "Cosa fare"** obbligatoria alla fine di ogni analisi
4. **Confidenza composita** — calcola e mostra sempre (max 92%)
5. **Specifico, mai generico** — "considera NVDA sotto $X con stop a $Y, max 5% portafoglio"

---

## Confidence Scoring

Dopo ogni passo assegna un tier:
- **HIGH (≥75%):** dato fresco, coerente con altri segnali
- **MEDIUM (50-74%):** dato parziale o lieve conflitto
- **LOW (<50%):** segnali contrastanti o dato mancante

Confidenza composita = media pesata di tutti i tier, cappata a **92%**.
Cap automatici:
- Regime e breadth si contraddicono → max 60%
- VIX > 30 → max 70%
- Più di 2 passi falliti → max 55%

---

## Passi del Briefing

Esegui in ordine. Per ogni passo usa web search con le query indicate.

### Passo 1 — Struttura di mercato

**Search:** `S&P 500 today performance` | `VIX index today` | `NASDAQ today`

Estrai:
- VIX: valore attuale → <15 calm, 15-25 elevated, >25 fear, >30 extreme fear
- S&P 500 e Nasdaq: variazione % giornaliera
- Sentiment generale: risk-on o risk-off

**Search:** `stock market advance decline ratio today` | `percentage stocks above 200 day moving average`

Stima il breadth score 0-100:
- >70% sopra 200MA → breadth HIGH (score 70-100)
- 50-70% → MEDIUM (score 40-70)
- <50% → LOW (score 0-40)

**Search:** `S&P 500 uptrend stocks percentage today`

Stima uptrend participation rate.

---

### Passo 2 — Regime e rischio

**Search:** `stock market regime bull bear 2026` | `yield curve 10Y 2Y today` | `credit spreads HYG LQD today`

Classifica regime: **BULL** / **BEAR** / **SIDEWAYS**

**Search:** `S&P 500 distribution days IBD` | `market top signals 2026`

Conta distribution days (vendite istituzionali pesanti). >6 negli ultimi 25 giorni = segnale di allarme.

**Search:** `US stock market bubble indicators 2026` | `Shiller PE CAPE ratio today`

Valuta probabilità bolla (0-100%).

Se regime (Passo 1) e breadth (Passo 1) si contraddicono → nota il conflitto, cappare confidenza a 60%.

---

### Passo 3 — Quote PIE AI

Per ogni ticker, cerca il prezzo attuale e la variazione giornaliera.

**Search batch:** `NVDA AAPL MSFT META GOOG AMZN stock price today`
**Search batch:** `AMD AVGO ASML CSCO QCOM TSM stock price today`

Costruisci una tabella:

| Ticker | Prezzo | Variazione % | Note |
|--------|--------|--------------|------|
| NVDA | ... | ... | |
| AAPL | ... | ... | |
| ... | | | |

Flag automatici:
- Variazione < -5% → ⚠️ vicino allo stop loss (7-8%)
- Variazione > +10% → 📈 movimento forte, valuta presa profitto parziale

**Search:** `FTDL.DE ETF price today` (se non disponibile → ⚠️ verifica su Trader 212)

---

### Passo 4 — News e sentiment

**Search:** `stock market news today` | `tech stocks news today`

Top 5 notizie rilevanti. Per ognuna: titolo, fonte, impatto sui tuoi ticker.

**Search per sentiment:** `NVDA Reddit sentiment today` | `AAPL stocktwits today` | `MSFT investor sentiment`

Per i top 4 ticker (NVDA, AAPL, MSFT, META): classifica sentiment Reddit/StockTwits/X:
- BULLISH / NEUTRAL / BEARISH

Se sentiment e prezzo vanno in direzioni opposte → segnalalo (divergenza).

---

### Passo 5 — Calendario

**Search:** `economic calendar this week` | `FOMC meeting 2026` | `CPI report date 2026` | `NFP jobs report date 2026`

Identifica eventi macro nei prossimi 7 giorni. Flag se coincidono con period di alta volatilità attesa.

**Search:** `earnings calendar this week tech stocks` | `NVDA AAPL MSFT META GOOG earnings date 2026`

Flag se un ticker PIE AI riporta entro 3 giorni → rischio gap (il prezzo può aprire molto diverso).

---

### Passo 6 — Settori e temi

**Search:** `sector rotation today 2026` | `technology sector performance today` | `semiconductors ETF SMH today`

Identifica: tech è in testa o in coda rispetto agli altri settori?
Flag se tech perde leadership → impatto diretto sul 100% del PIE AI.

**Search:** `AI stocks trend 2026` | `semiconductor cycle 2026` | `top investment themes today`

Top 2 temi dominanti del momento.

---

### Passo 7 — Decisione di esposizione

Basandoti su tutti i passi precedenti, determina la postura:

| Condizione | Postura |
|---|---|
| Regime BULL + breadth HIGH + VIX <20 + nessun evento macro imminente | **ALLOW** — puoi aprire nuove posizioni |
| Regime SIDEWAYS o breadth MEDIUM o VIX 20-30 | **RESTRICT** — mantieni posizioni, no nuovi acquisti |
| Regime BEAR o breadth LOW o VIX >30 o evento macro entro 2 giorni | **CASH-PRIORITY** — riduci esposizione, aumenta liquidità |

Motiva la decisione con i dati dei passi precedenti.

---

### Passo 8 — Sintesi e report

Costruisci il report finale con questa struttura:

**1. Market Overview**
VIX, S&P 500, Nasdaq, breadth score, regime.

**2. PIE AI Quotes**
Tabella ticker con prezzi, variazioni e flag.

**3. Morning News**
Top 5 notizie con impatto sui tuoi ticker.

**4. Social Sentiment**
NVDA, AAPL, MSFT, META: bullish/neutral/bearish.

**5. Calendario**
Macro eventi + earnings questa settimana, flag PIE AI.

**6. Settori e Temi**
Rotazione settoriale, top 2 temi.

**7. Esposizione**
ALLOW / RESTRICT / CASH-PRIORITY + ragionamento + **confidenza composita %**

**8. Insight del giorno**
Un'osservazione concreta e basata sui dati per Alessandro.

---

### Passo 9 — Cosa fare (OBBLIGATORIO)

Questa sezione non può essere omessa. Deve essere concreta e specifica.

**Comprare (se ALLOW):**
Lista titoli con: entry price, stop loss, size massima (% portafoglio)
Esempio: "Considera NVDA sotto $X con stop a $Y, max 5% portafoglio"

**Vendere o ridurre:**
Lista titoli con motivazione e livello di uscita suggerito

**Watchlist:**
Titoli da monitorare con il trigger specifico che li renderebbe acquistabili

**Trigger da monitorare:**
Eventi, livelli di prezzo, scadenze entro 7 giorni

**Opportunità fuori dal portafoglio:**
Se il contesto suggerisce un titolo interessante non nella PIE AI, segnalarlo con entry/stop/size

---

## Come salvare su claude.ai

Per usare questa skill su claude.ai:

1. Vai su **claude.ai → Projects → Crea nuovo progetto** (es. "Finance Briefing")
2. Nelle **Project Instructions** incolla il contenuto di questo file (da "# Finance Briefing" in poi)
3. Ogni volta che apri quel progetto e scrivi **"briefing"**, Claude esegue l'analisi completa

Il progetto ricorda le istruzioni permanentemente — non devi re-incollare ogni volta.

---

## Limitazioni rispetto alla versione Claude Code

| Funzionalità | Claude Code | claude.ai |
|---|---|---|
| Prezzi esatti in tempo reale | FMP API (precisi) | Web search (approssimati) |
| Sentiment social | Adanos API (Reddit/X/Polymarket) | Web search (meno preciso) |
| Breadth quantitativo | CSV pubblici (precisi) | Web search (stimato) |
| Salvataggio report | File locale automatico | Copia/incolla manuale |
| Memoria sessione precedente | Git (automatica) | Non disponibile |
| Skill avanzate (71) | Tutte disponibili | Solo web search |

Per analisi approfondite su singoli titoli (es. "analizza NVDA in dettaglio"), chiedile esplicitamente dopo il briefing — claude.ai con web search può comunque fare analisi di qualità.
