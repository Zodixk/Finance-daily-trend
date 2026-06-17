# Session Memory — 2026-06-17

## Regime
- Market environment: risk-on surface (VIX 16.23) but FOMC event risk priced (VIX9D 22.14)
- VIX: 16.23 (▼ -1.10% from 16.18 — essentially flat)
- Breadth score: N/A (TraderMonty CSV returned 403 Forbidden — unavailable)
- Uptrend participation: 28.6% of ~2,800 stocks (60.2/100 composite, Bull-Lower zone, trend up)
- Macro regime: Broadening (transitional — 5/6 components signaling shift, 70-90% probability)
- Distribution days: Elevated (persistent, no new count confirmed)
- Bubble score: N/A (FMP premium endpoint)

## Market Levels (June 16, 2026 close)
- NASDAQ: 26,376 (-1.15%)
- S&P 500: 7,511 (-0.57%)
- VWCE: €164.44 (+0.17%)
- Gold: ~$4,165 (down 25% from Jan ATH $5,589)
- Oil (WTI): ~$80.75 (Iran deal drop)

## Signals
- Sentiment bias: Reddit broadly neutral; X/Twitter bullish on all; GOOG most bullish (38% bull, 19% bear); META showing bearish shift (24% bull vs 25% bear)
- Sector rotation: XLK -2.79% while Dow at record high — capital rotating OUT of tech/semiconductors, INTO financials (JPMorgan +3.7%), industrials (SpaceX +4.8%). DIRECT headwind for PIE AI.
- Top themes: FOMC Communication Pivot (dominant today — 70% prob rate hike by year-end 2026), AI Supercycle ($750B hyperscaler capex intact structurally)

## Portfolio (June 16 close)
- AMD: $507.29 (-7.30%) — 🔴 AT STOP THRESHOLD. ARK sold 141K shares ($72M), CEO Lisa Su sold 125K ($57M) on June 15. 52w high $558.37 set ~June 15.
- AVGO: $376.71 (-4.37%) — continuing June 5 miss weakness, -24% from 52w high $495
- ASML: $1,803.89 (-4.69%) — China restrictions + delayed High-NA EUV adoption
- TSM: $425.83 (-3.53%) — pulled back from near-52w-high $450.16
- NVDA: $207.41 (-2.37%) — sector drag
- QCOM: $214.07 (-3.05%) — Investor Day June 24
- GOOG: $367.11 (+2.50%) — OUTPERFORMER, most bullish Reddit skew
- AAPL: $299.24 (+0.95%) — resilient
- META: $600.21 (+1.13%) — holding
- AMZN: $246.00 (-0.01%) — flat

## Exposure Decision
- Posture: RESTRICT (pre-FOMC)
- Composite confidence: 60% (hard-capped due to FOMC binary event today)
- Post-FOMC framework: Neutral/dovish → ALLOW; Hawkish → CASH-PRIORITY

## Pending
- ⭐⭐⭐ **FOMC Rate Decision 2:00 PM ET + Warsh Press Conference 2:30 PM ET TODAY Jun 17**
  - Rate hold 99% prob (3.50-3.75% unchanged)
  - Dot plot: may remove last 2026 cut. 70% prob of rate hike by year-end per CME FedWatch
  - Warsh may withhold his own dot (first meeting). More hawkish committee.
  - After PC: reassess posture. Neutral/dovish → ALLOW (AMD >$520, TSM >$430, GOOG leading). Hawkish → CASH-PRIORITY (AMD stop may trigger, reduce tech 20-30%)
- 🕊️ US-Iran deal official signing: Friday June 19 (Switzerland) — risk if it falls apart → oil spike
- 📊 QCOM Investor Day: June 24
- 📋 MSFT Earnings: July 25 (after close)
- 📋 NVDA Earnings: July 28 (after close)

## Infrastructure
- FMP API: ✅ Working — /stable/quote one ticker at a time; some tickers 402 (GOOG, AVGO, ASML, QCOM) → yfinance fallback
- Adanos API: ✅ Working — /reddit/stocks/v1/compare with tickers param, header X-API-Key
- yfinance: ✅ Working — fallback active
- Market Breadth CSV: ❌ 403 Forbidden (TraderMonty GitHub) — excluded from confidence score
- Uptrend Analyzer CSV: ✅ Working — Monty GitHub, 18,044 rows
- Macro Regime Detector: ✅ Working — some FMP 403s for legacy endpoints but yfinance fallback succeeded
- Telegram: ✅ Sent successfully
