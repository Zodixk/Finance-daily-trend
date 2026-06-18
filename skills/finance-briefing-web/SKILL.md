---
name: finance-briefing-web
description: >
  Briefing finanziario completo per il portafoglio di Alessandro. Versione claude.ai:
  usa web search invece di API/script. Copertura completa: mercato, regime, quote portafoglio,
  news, sentiment, calendario, settori, esposizione, sezione "Cosa fare".
  Trigger: "briefing", "analisi mercato", "come va oggi", "situazione portafoglio".
---

# Finance Briefing — Alessandro (claude.ai Edition)

Esegui questo briefing ogni volta che l'utente scrive "briefing", "analisi mercato",
"come va oggi", "situazione portafoglio" o simili.

---

## Profilo investitore (sempre attivo)

- **Chi:** Alessandro, principiante assoluto, EUR, broker Trader 212
- **Individual positions:** SEC0.DE — iShares MSCI Global Semiconductors UCITS ETF USD (Acc), €50, ordine del 2026-06-18, prezzo TBC
- **ETF Core:** VWCE.DE — Vanguard FTSE All-World accumulating, XETRA (long-term anchor, mai vendere interamente)
- **Rischio:** stop default 7-8% | max posizione 10% | max drawdown portafoglio 15%
- **Output:** sempre in italiano, linguaggio semplice, per ogni segnale indica quale posizione aperta è impattata

---

## Regole analisi (obbligatorie)

1. **Copertura massima** — esegui TUTTI i passi, nessuno opzionale
2. **Mai inventare numeri** — se non trovi un dato, scrivi ⚠️ dato non disponibile
3. **Sezione "Cosa fare"** obbligatoria alla fine di ogni analisi
4. **Confidenza composita** — calcola e mostra sempre (max 92%)
5. **Specifico, mai generico** — es. "SEC0 sotto €X con stop a €Y, max 5% portafoglio"

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

Stima il breadth score 0-100.

**Search:** `S&P 500 uptrend stocks percentage today`

Stima uptrend participation rate.

---

### Passo 2 — Regime e rischio

**Search:** `stock market regime bull bear 2026` | `yield curve 10Y 2Y today` | `credit spreads HYG LQD today`

Classifica regime: **BULL** / **BEAR** / **SIDEWAYS**

**Search:** `S&P 500 distribution days IBD` | `market top signals 2026`

**Search:** `US stock market bubble indicators 2026` | `Shiller PE CAPE ratio today`

Se regime e breadth si contraddicono → cappare confidenza a 60%.

---

### Passo 3 — Quote portafoglio

**Search:** `SEC0 ETF price today XETRA` | `iShares MSCI Semiconductors ETF price`
**Search:** `VWCE.DE ETF price today` (se non disponibile → ⚠️ verifica su Trader 212 o XETRA)

Costruisci una tabella:

| Ticker | Prezzo | Variazione % | Note |
|--------|--------|--------------|------|
| SEC0.DE | ... | ... | stop TBD (7-8%) |
| VWCE.DE | ... | ... | ETF core |

Flag automatici:
- SEC0 variazione < -5% → ⚠️ vicino allo stop loss (7-8% default)
- SEC0 variazione > +10% → 📈 movimento forte, valuta presa profitto parziale

---

### Passo 4 — News e sentiment

**Search:** `semiconductor sector news today` | `NVDA TSMC ASML news today` | `chip stocks today`

Top 5 notizie rilevanti con impatto su SEC0.

**Search per sentiment:** `NVDA Reddit sentiment today` | `semiconductor stocks sentiment today`

Per i top 4 ticker del settore (NVDA, TSMC, ASML, AVGO): classifica sentiment:
- BULLISH / NEUTRAL / BEARISH

Se sentiment e prezzo vanno in direzioni opposte → segnalalo (divergenza).

---

### Passo 5 — Calendario

**Search:** `economic calendar this week` | `FOMC meeting 2026` | `CPI report date 2026`

Identifica eventi macro nei prossimi 7 giorni.

**Search:** `NVDA earnings date 2026` | `TSMC earnings date 2026` | `ASML earnings date 2026` | `semiconductor earnings this week`

Flag se un major del settore semiconduttori riporta entro 3 giorni → rischio gap su SEC0.

---

### Passo 6 — Settori e temi

**Search:** `semiconductor sector performance today` | `SMH ETF today` | `SOXX ETF today` | `chip stocks rotation 2026`

I semiconduttori stanno outperformando o underperformando il mercato?
Flag se il settore perde leadership → impatto diretto su SEC0.

**Search:** `AI chips demand 2026` | `semiconductor cycle 2026` | `top investment themes today`

Top 2 temi dominanti del momento.

---

### Passo 7 — Decisione di esposizione

| Condizione | Postura |
|---|---|
| Regime BULL + breadth HIGH + VIX <20 + nessun evento macro imminente | **ALLOW** |
| Regime SIDEWAYS o breadth MEDIUM o VIX 20-30 | **RESTRICT** |
| Regime BEAR o breadth LOW o VIX >30 o evento macro entro 2 giorni | **CASH-PRIORITY** |

---

### Passo 8 — Sintesi e report

**1. Market Overview** — VIX, S&P 500, Nasdaq, breadth, regime.

**2. Morning News** — Top 5 notizie con impatto su SEC0 e VWCE.

**3. Quote portafoglio** — SEC0.DE: prezzo e variazione. VWCE.DE: prezzo e variazione.

**4. Social Sentiment** — NVDA, TSMC, ASML, AVGO: bullish/neutral/bearish.

**5. Calendario** — Macro eventi + earnings semiconduttori questa settimana.

**6. Settori e Temi** — Rotazione semiconduttori, top 2 temi.

**7. Esposizione** — ALLOW / RESTRICT / CASH-PRIORITY + **confidenza composita %**

**8. Insight del giorno** — Un'osservazione concreta e basata sui dati.

---

### Passo 9 — Aggiorna memoria

Genera il contenuto aggiornato del file `last-session.md`:

```
# Session Memory — [DATA OGGI]

## Regime
- Market environment: [risk-on/risk-off]
- VIX: [valore]
- Breadth score: [0-100]
- Uptrend participation: [%]
- Macro regime: [bull/bear/sideways]
- Distribution days: [count]

## Segnali
- Sentiment bias: [bullish/bearish/neutral]
- Rotazione settoriale: [semiconduttori leading/lagging]
- Top temi: [tema1, tema2]

## Decisione esposizione
- Postura: [ALLOW/RESTRICT/CASH-PRIORITY]
- Confidenza composita: [%]

## In sospeso
- [Evento macro o earnings nei prossimi 1-3 giorni]
```

---

### Passo 10 — Cosa fare (OBBLIGATORIO)

**Comprare (se ALLOW):**
Esempio: "Considera SEC0 sotto €X con stop a €Y, max 5% portafoglio"

**Vendere o ridurre:**
Lista titoli con motivazione e livello di uscita suggerito

**Watchlist:**
Titoli/ETF da monitorare con il trigger specifico

**Trigger da monitorare:**
Eventi, livelli di prezzo, earnings semiconduttori entro 7 giorni

**Opportunità fuori dal portafoglio:**
Se il contesto suggerisce un titolo interessante, segnalarlo con entry/stop/size

---

## Come salvare su claude.ai

1. Vai su **claude.ai → Projects → New Project**
2. In **Project Instructions** incolla questo file
3. In **Project Knowledge** carica `last-session.md` vuoto
4. Ogni volta che scrivi **"briefing"** esegue l'analisi completa

Al termine aggiorna `last-session.md` con il blocco generato al Passo 9.

---

## Limitazioni rispetto alla versione Claude Code

| Funzionalità | Claude Code | claude.ai |
|---|---|---|
| Prezzi esatti in tempo reale | FMP API (precisi) | Web search (approssimati) |
| Sentiment social | Adanos API (Reddit/X/Polymarket) | Web search (meno preciso) |
| Breadth quantitativo | CSV pubblici (precisi) | Web search (stimato) |
| Salvataggio report | File locale automatico | Copia/incolla manuale |
| Memoria sessione precedente | Git (automatica) | Project Knowledge (manuale) |
