---
name: finance-profile
description: "Alessandro's investor profile — style, risk, portfolio, watchlist"
metadata: 
  node_type: memory
  type: project
  updated: 2026-06-18
  originSessionId: e0c50a76-f17e-4dbe-8d3b-38d41d863a92
---

# Investor Profile — Alessandro

## Section 1 — Identity and Style

- **investment_style:** growth (learning phase — open to evolving)
- **time_horizon:** position trading (weeks to months) — to be refined with experience
- **markets_covered:** US stocks (primary), ETFs (primary), EU (open)
- **broker:** Trader 212
- **portfolio_currency:** EUR
- **experience:** absolute beginner — recently started

## Section 2 — Risk Profile

*Conservative defaults for a beginner. Update as experience grows.*

- **max_tolerated_drawdown:** 15% on total portfolio
- **max_single_position:** 10% of portfolio per individual position
- **max_sector_concentration:** 30% per sector
- **default_stop_loss:** 7-8% (calibrate case by case — user prefers flexibility)
- **leverage:** none

## Section 3 — Current Portfolio

**Individual positions (manually managed):**
| Ticker | Company | Entry price | Stop loss | Size | Date | Notes |
|--------|---------|-------------|-----------|------|------|-------|
| SEC0 | iShares MSCI Global Semiconductors UCITS ETF USD (Acc) | ~€22.87–23.35 | ~€18.50 (-20% from entry) | €50 | 2026-06-18 | ISIN IE000I8KRLL9. XETRA: SEC0.DE. 261 holdings, 10% single-stock cap (NVIDIA capped). Entry near 52-week high after +98% YTD rally. HOLD €50, do NOT add until re-entry triggers confirmed (see Section 8). |

**T212 micro-positions (pie — scheduled closure 2026-06-20):**
LRCX, NVDA, AMD, QCOM, AVGO, TSM, MSFT, ASML, AAPL, META, GOOG, CSCO, AMZN — posizioni da €1–10 in pie T212. Alessandro li vende il 2026-06-20. **Escludere da ogni cross-check di portafoglio e analisi di concentrazione settoriale.** Dopo la vendita il portafoglio attivo è: VWCE (core) + SEC0.DE (satellite).

**Core ETF (accumulation plan):**
- **VWCE** — Vanguard FTSE All-World UCITS ETF (accumulating), listed on multiple exchanges | Replaced VUAA (S&P 500 only) | Switch made: 2026-06-15
  - Coverage: ~4,000 stocks, developed + emerging markets, ~60-65% US, ~35-40% rest of world
  - Index tracked: FTSE All-World
  - Tax treatment: accumulating → no tax on reinvested dividends, taxed only at exit

**Excluded sectors:**
- none at this time

## Section 4 — Operative Preferences

- **preferred_screeners:** to be defined (beginner — use simple screening initially)
- **current_focus:** learning + building base portfolio (individual picks + core ETF)
- **minimum_confidence_threshold:** 50%
- **output_language:** English
- **notes:** user is an absolute beginner — always add a contextual glossary explaining every technical term used in the output

## Section 5 — Investment Thesis History (last 12 months)

*No trades recorded — portfolio in construction phase.*

---

## Section 5b — Watchlist (organized by sector)

Monitor these tickers in every relevant analysis. Flag any that approach key levels or re-entry triggers.

### ETF
| Ticker | Name | Description |
|--------|------|-------------|
| VWCE.DE | Vanguard FTSE All-World Accumulating | Core holding. ~4,000 titoli globali, developed + emerging markets. Strumento principale di accumulo a lungo termine. |
| SEC0.DE | iShares MSCI Global Semiconductors | Satellite holding. 261 titoli del settore semiconduttori globale. Re-entry triggers in §8.3. |
| SMH | VanEck Semiconductor ETF | ETF semi US-listed. Top 25 aziende semi per market cap. Utile come benchmark tecnico per confrontare con SEC0. |

### AI Infrastructure
| Ticker | Name | Description |
|--------|------|-------------|
| NVDA | Nvidia | Leader assoluto nelle GPU per AI. Principale beneficiario del boom dell'AI infrastructure. Benchmark del settore. |
| AMD | Advanced Micro Devices | CPU e GPU ad alte prestazioni. Sfida Intel nei server e NVDA nell'AI con chip MI-series. |
| AVGO | Broadcom | Semiconduttori + software infrastrutturale. Revenue diversificato, free cash flow molto elevato. |
| TSM | Taiwan Semiconductor | Più grande foundry al mondo. Produce i chip di Apple, NVDA, AMD. Termometro dell'intera industria semi. |
| ASML | ASML Holding | Monopolio mondiale sulle macchine EUV per la litografia. Senza ASML non si producono chip avanzati. Bellwether del ciclo semi. |
| KLAC | KLA Corporation | Strumenti di process control per la produzione di wafer. Margini alti, revenue ricorrente. |
| LRCX | Lam Research | Apparecchiature di etch e deposition. Ciclico, alto leverage ai capex dei produttori di chip. |
| MU | Micron Technology | DRAM e NAND flash. Competitor diretto di SNDK nella memoria. Indicatore del ciclo memory. |
| SNDK | SanDisk | Pure-play NAND flash. Spin-off da Western Digital (feb 2025). +800% YTD 2026 — in watchlist, NON comprare ora. Entry possibile su pullback $1,200–1,400 + base di 5 settimane. |
| CSCO | Cisco Systems | Hardware e software di rete. Presenza nei data center e infrastruttura AI. Revenue stabile, dividendo solido. |
| META | Meta Platforms | Facebook, Instagram, WhatsApp. Uno dei maggiori investitori in AI e data center al mondo. Monetizzazione via advertising potenziata da AI. |
| GOOGL | Alphabet Class A | Google, YouTube, Google Cloud. Pioniere dell'AI (TPU, Gemini). Cloud in crescita, dominio nella search. Classe A = diritto di voto. |

## Section 6 — Analysis Preferences (global)

These preferences apply in EVERY context where finance, markets, or investing is discussed, regardless of the active project.

### Skill coverage
Use ALL relevant skills for every analysis, even if the marginal contribution is minimal (+1% quality).
Do not filter skills by relevance threshold — always maximize coverage.

### Mandatory output structure
Every financial analysis must end with a **"What to do"** section containing:
- Specific tickers to consider buying — with entry price, stop loss, suggested size (% of portfolio)
- Tickers to sell or reduce (if applicable)
- Watchlist additions with motivation
- Triggers to monitor in the next hours/days (events, price levels, news)
- Opportunities outside the current portfolio if the context suggests them

Always be specific and concrete. Never generic ("consider buying X") — always precise ("consider X below $Y with stop at $Z, max 5% portfolio").

## Section 7 — Pattern Playbook

Recognize and apply these patterns in every analysis. For each signal, indicate which open position is involved and the concrete action suggested.

---

### 7.1 — Chart Patterns (technical)

Always use in combination with volume. Patterns without volume confirmation carry less weight.

| Pattern | Signal | Entry | Stop | Related skills |
|---|---|---|---|---|
| **VCP** (Volatility Contraction) | 3+ stalls with contracting price range and volume | Breakout above last pivot on volume >50% of average | Below the low of the last stall | `vcp-screener`, `breakout-trade-planner` |
| **Cup & Handle** | U-shaped base (5-65 weeks) + handle < 1/3 of cup depth | Breakout from handle pivot | Below handle low | `technical-analyst` |
| **Flat Base** | 5+ weeks sideways, range < 15% | Breakout above the upper band of the base | Below base low | `technical-analyst` |
| **Flag / Pennant** | 3-5 day consolidation after a sharp rally | Breakout above upper band of the flag | Below flag low | `breakout-trade-planner` |
| **Double Bottom (W)** | Two nearby lows, second slightly higher | Breakout above the middle peak (neckline) | Below the second low | `technical-analyst` |
| **Head & Shoulders** | Three peaks, middle highest — reversal signal | For Alessandro: use as EXIT signal, not to short | Above right shoulder (if exit was late) | `market-top-detector` |
| **3-Weeks Tight** | 3 consecutive weeks closing within 1-1.5% of each other | Breakout above the highest week | Below the 3-week low | `vcp-screener` |

**Application rules:**
- For growth ETFs (SEC0 and future positions): prioritize VCP, Flag, Cup & Handle
- Head & Shoulders on any open position → immediately analyze with `market-top-detector`
- Never enter on a false breakout: price must close above the pivot, not just touch it intraday

---

### 7.2 — Macro Patterns (economic cycle)

| Pattern | Activation signal | Typical duration | Portfolio action |
|---|---|---|---|
| **Yield Curve Inversion** | 10Y-2Y spread < 0 (2Y exceeds 10Y) | Recession on average 12-18 months later | Reduce cyclical positions, increase cash |
| **Fed Pivot** | Pause between last hike and first cut | 3-9 month window | Build growth positions during the pause — market anticipates the cut |
| **VIX Spike > 40** | VIX rises > 40 in < 5 days | Peak lasts 1-3 weeks | Wait for the first day VIX declines — then look for entries at support levels |
| **VIX Structurally > 25** | VIX stays > 25 for 2+ weeks | Weeks to months | Cash-priority: no new purchases until VIX < 20 |
| **Dollar Strength (DXY +)** | DXY rises > 3% in 1 month | Variable | Pressure on EU-listed and Asian stocks, US multinationals less affected |
| **Late-Cycle Rotation** | Tech loses leadership, Energy/Materials/Utilities rise | Months | Reduce tech exposure, consider hedge with defensive ETFs |
| **Sector rotation by phase** | Monitor which sector leads each quarter | Quarterly | Early: Financials → Mid: Tech (now) → Late: Energy → Recession: Utilities |

**Weekly monitoring checklist:**
- 10Y-2Y spread (target > 0 = healthy curve)
- DXY (above 105 → pressure on EU/Asian holdings)
- Sectors leading vs lagging (tech must be in the top 3)

---

### 7.3 — Earnings Patterns

| Pattern | When it applies | Action |
|---|---|---|
| **PEAD** (Post-Earnings Drift) | Beat + raised guidance | Enter 1-3 days after earnings on first pullback. Trend typically continues 30-60 days |
| **Pre-Earnings Run-Up** | 2-3 weeks before earnings date | Buy 3 weeks before, exit the day before earnings. Do not hold through the report |
| **Buy Rumor / Sell News** | Stock at all-time high + very bullish sentiment pre-earnings | Do not buy pre-earnings. Wait for post-report confirmation |
| **Earnings Gap & Hold** | Gap up > 5% on volume 3x+ post-earnings | Entry on the first red day after the gap. Stop: below the gap day low |
| **Guidance > Beat** | Report release | Market rewards raised guidance more than the current beat. Miss + raised guidance → possible rally |
| **Whisper vs Consensus** | Days before earnings | If price already up 15%+ pre-earnings, the market already "knows" — beat is partially priced in |

---

**How to use the Pattern Playbook in every analysis:**
1. Identify the current cycle phase (Section 7.2) → determines overall posture
2. For each open position near a key level: apply chart patterns (Section 7.1)
3. For each ticker with earnings within 3 weeks: apply earnings patterns (Section 7.3)
4. Always flag which pattern triggered and the specific level (price + volume)

---

## Section 8 — Portfolio Structure & Active Theses

### 8.1 — Portfolio Architecture

Target allocation (confirmed by Alessandro 2026-06-19): **90% VWCE / 10% SEC0**

- **Core (90%):** VWCE.DE — Vanguard FTSE All-World Accumulating. Every new capital injection goes here by default (85-90% of each deposit).
- **Satellite (10%):** SEC0.DE — iShares MSCI Global Semiconductors. Add only when re-entry triggers confirmed (§8.3). Cap strictly at 10% of total portfolio.

**Key correlation note:** VWCE already contains semiconductors (~5% of the index via tech allocation). Adding SEC0 is a **deliberate overweight** on semiconductors, not true diversification. In a semiconductor correction, both VWCE and SEC0 will fall together. This is intentional and acceptable as long as SEC0 stays ≤10% of total portfolio.

**Alternative satellite candidates** (to evaluate when more capital is available):
- **IUIT.DE** (iShares S&P 500 IT, TER 0.15%) — broader tech exposure, lower concentration than SEC0
- **LGTG** (L&G Global Technology Index, TER 0.22%) — tech + chips + software, lower semiconductor-only risk

---

### 8.2 — SEC0 Active Thesis

**Core thesis (Alessandro's own reasoning):**
Semiconductors have reached a point of irreversibility — they are no longer a technology sector, they are foundational infrastructure, like electricity in the 20th century. Three structural drivers underpin this:

**1. Pervasiveness across all sectors**
Chips are now embedded in every industry: military systems, surveillance, healthcare devices, automotive (EVs and autonomous driving), industrial automation, smart grids, 5G/6G networks, consumer electronics. A slowdown in one sector does not kill demand — others absorb it. This cross-sector application makes semiconductors structurally different from previous tech cycles.

**2. Geopolitical necessity — the arms race argument**
The US and Europe cannot afford to fall behind China and Russia in semiconductor capability. This is not a market thesis — it is a national security imperative. Governments are funding the industry regardless of the economic cycle:
- US CHIPS Act: $52 billion in subsidies + tax credits
- EU Chips Act: €43 billion target
- TSMC fabs in Arizona, Intel in Ohio, Samsung in Texas — onshoring of critical supply chains
This government-backed demand provides a structural floor that pure market cycles cannot eliminate.

**3. AI explosion as accelerant**
The AI boom of 2024–2026 has compressed years of semiconductor demand into months. GPUs, memory (HBM, NAND), networking chips, custom ASICs — all in shortage simultaneously. But unlike previous booms, this demand is driven by sovereign investments (governments, militaries) and hyperscalers (Microsoft, Google, Meta, Amazon) with multi-year capex commitments, not speculative consumer demand.

**Applications (current and future):**
- Military: autonomous weapons, missile guidance, battlefield AI, electronic warfare
- Surveillance: facial recognition, smart city infrastructure, border control
- Healthcare: AI diagnostics, robotic surgery, wearables, genomics
- Automotive: ADAS, EV powertrains, V2X communication
- Industrial: factory automation, robotics, predictive maintenance
- Energy: smart grid management, battery management systems
- Space & defense: satellite constellations, quantum computing

**Thesis validity:** 2025–2030+ as long as AI capex continues and geopolitical competition persists. The thesis does NOT depend on any single company or product cycle.

**Entry context (2026-06-18):** Entry near 52-week high after +98% YTD rally. Valuation stretched. Michael Burry has placed put options on semiconductor ETFs (SOXX), warning of a dot-com style bubble. The thesis is intact but the timing of the initial €50 entry was suboptimal.

**Status:** HOLD €50. Do NOT add more until at least one re-entry trigger is confirmed (see below).

**Stop loss:** ~€18.50 (-20% from entry ~€22.87). If SEC0 closes below €18.50 for 2 consecutive days → exit and reassess.

---

### 8.3 — SEC0 Re-entry Triggers (confirmed 2026-06-19)

Add to SEC0 only when at least ONE of these is confirmed:

| Trigger | What to look for | Why it creates opportunity |
|---|---|---|
| **Price pullback ≥25%** | SEC0/SEMI.AS price reaches €17–18 range (25% below recent high of ~€23.39) | Buys at a rational price after the parabolic run. Same ETF, 25% cheaper. |
| **VIX spike above 25** | VIX index rises above 25 (currently 16.4 — watch for spike) | Panic causes forced selling by leveraged investors, pushing prices below fair value. Patient cash buyers benefit. |
| **New base formation** | SEC0 moves sideways for ≥5 consecutive weeks with daily price swings getting progressively smaller (VCP pattern) | Confirms sellers are exhausted. Institutional buyers are quietly accumulating. Safe to enter before the next breakout. |

**Decision tree for re-entry:**
1. Is SEC0 down ≥25% from high (≤€17.54)? → YES: check if VIX > 25 or base formed → both confirm = strong entry
2. Is VIX > 25 without a price pullback? → Possible forced-selling dip — evaluate case by case
3. Is a 5-week base forming at current price? → Only valid if semiconductors have cooled meaningfully from peak

**Weekly check:** Every Monday, note SEC0 price and VIX level. Update the table below.

### SEC0 Trigger Status (update every Monday)

| Trigger | Level required | Last checked | Current value | Status |
|---|---|---|---|---|
| Price pullback ≥25% | SEC0 ≤ €17.54 | 2026-06-19 | €23.33 | ❌ |
| VIX > 25 | VIX > 25 | 2026-06-19 | 16.40 | ❌ |
| Base formation (VCP) | ≥5 weeks sideways | 2026-06-19 | 0 weeks | ❌ |

**Current recommendation: HOLD €50. Do NOT add.**

---

### 8.4 — Macro Regime Summary (last updated 2026-06-19)

| Indicator | Value | Signal |
|---|---|---|
| Regime | BROADENING (RSP outperforming SPY by ~5% YTD) | Leadership expanding beyond mega-caps |
| Yield curve (10Y-2Y) | +0.29–0.39% | Positive — no recession signal |
| VIX | 16.4 | Risk-on, below long-term average |
| Credit spreads (HYG/LQD) | NEUTRAL | No credit stress |
| Semiconductor sector | Pulled back ~12% from highs | Correction underway — do not add to SEC0 |

Update this table whenever a portfolio review is run.
