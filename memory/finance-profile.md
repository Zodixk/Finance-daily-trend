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

**Open positions:**

PIE "AI Companies" on Trader 212 — composition:
| Ticker | Company | Notes |
|--------|---------|-------|
| GOOG | Alphabet (Class C) | Big Tech / AI |
| AMZN | Amazon | Cloud (AWS) / AI |
| AVGO | Broadcom | AI semiconductors |
| NVDA | NVIDIA | GPU / AI infrastructure |
| AMD | Advanced Micro Devices | GPU / semiconductors |
| AAPL | Apple | Big Tech |
| ASML | ASML Holding | Chip lithography (EU-listed) |
| CSCO | Cisco Systems | Networking / AI infra |
| META | Meta Platforms | Social / AI |
| MSFT | Microsoft | Cloud (Azure) / AI (OpenAI) |
| QCOM | Qualcomm | Mobile chips / AI edge |
| TSM | Taiwan Semiconductor | Foundry — manufactures chips for all |

Individual weights: unspecified (automatically managed by Trader 212 PIE)
Estimated sector concentration: ~100% Technology/Semiconductors — monitor closely

**Core ETF (accumulation plan):**
- **VWCE.DE** (Vanguard FTSE All-World UCITS ETF Acc) — tracks the FTSE All-World index, listed on XETRA | Replaced VUAA (S&P 500 only) | Switch made: 2026-06-15
  - Coverage: ~4,000 stocks, developed + emerging markets, ~60-65% US, ~35-40% rest of world
  - Tax treatment: accumulating → no tax on reinvested dividends, taxed only at exit

**Excluded sectors:**
- none at this time

## Section 4 — Operative Preferences

- **preferred_screeners:** to be defined (beginner — use simple screening initially)
- **current_focus:** learning + building base portfolio (AI stocks + core ETF)
- **minimum_confidence_threshold:** 50%
- **output_language:** English
- **notes:** user is an absolute beginner — always add a contextual glossary explaining every technical term used in the output

## Section 5 — Investment Thesis History (last 12 months)

*No trades recorded — portfolio in construction phase.*

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

Recognize and apply these patterns in every analysis. For each signal, indicate which PIE AI ticker is involved and the concrete action suggested.

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
- For PIE AI (growth stocks): prioritize VCP, Flag, Cup & Handle
- Head & Shoulders on any PIE AI ticker → immediately analyze with `market-top-detector`
- Never enter on a false breakout: price must close above the pivot, not just touch it intraday

---

### 7.2 — Macro Patterns (economic cycle)

| Pattern | Activation signal | Typical duration | Portfolio action |
|---|---|---|---|
| **Yield Curve Inversion** | 10Y-2Y spread < 0 (2Y exceeds 10Y) | Recession on average 12-18 months later | Reduce cyclical positions (AMD, QCOM), increase cash |
| **Fed Pivot** | Pause between last hike and first cut | 3-9 month window | Build growth positions during the pause — market anticipates the cut |
| **VIX Spike > 40** | VIX rises > 40 in < 5 days | Peak lasts 1-3 weeks | Wait for the first day VIX declines — then buy PIE AI at support levels |
| **VIX Structurally > 25** | VIX stays > 25 for 2+ weeks | Weeks to months | Cash-priority: no new purchases until VIX < 20 |
| **Dollar Strength (DXY +)** | DXY rises > 3% in 1 month | Variable | Pressure on ASML (EU), TSM (Taiwan, FX), US multinationals less affected |
| **Late-Cycle Rotation** | Tech loses leadership, Energy/Materials/Utilities rise | Months | Reduce PIE AI, consider hedge with defensive ETFs |
| **Sector rotation by phase** | Monitor which sector leads each quarter | Quarterly | Early: Financials → Mid: Tech (now) → Late: Energy → Recession: Utilities |

**Weekly monitoring checklist:**
- 10Y-2Y spread (target > 0 = healthy curve)
- DXY (above 105 → pressure on ASML/TSM)
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

**Application to PIE AI tickers:**
- NVDA, META, MSFT → high institutional ownership → good PEAD candidates after beat
- AAPL, GOOG → often "buy rumor sell news" when already at highs
- AMD, QCOM → more volatile post-earnings → wait for stabilization before entering
- ASML → reports in EUR, analyze FX impact separately
- TSM → monthly report (not quarterly) — monitor shipment data every month

---

## Notes for Daily Briefing Routine

- Always read this file at Step 0 alongside `memory/last-session.md`
- Core ETF is **VWCE.DE** (Vanguard FTSE All-World, tracks FTSE All-World index) — replaced VUAA on 2026-06-15
- PIE AI weights are auto-managed by Trader 212 — adding funds distributes across all 12 tickers automatically
- Pattern Playbook (Section 7) must be checked for every PIE AI ticker near a key level
