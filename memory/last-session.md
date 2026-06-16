# Session Memory — 2026-06-16

## Regime
- Market environment: risk-on (US-Iran deal extended, oil <$80, NASDAQ +3.07%)
- VIX: 16.18 (▼ from 17.68 yesterday, −8.5%)
- Breadth score: ~56/100 (56% S&P 500 above 50dMA — slight dip from 61% yesterday)
- Uptrend participation: ~56%
- Macro regime: Transitional (bear steepening yield curve; 10Y yield 4.28%; BofA pre-top 70%)
- Distribution days: Elevated (persistent from 15/06 — no new count today)
- Bubble score: N/A (FMP news endpoint premium-only)

## Signals
- Sentiment bias: Reddit neutral across all PIE tickers; X/Twitter bullish on all — AMZN, AMD, AAPL, GOOG trending rising on Reddit. AVGO lowest buzz (69/100) and falling trend.
- Sector rotation: Tech (XLK +3.15%) leading; Energy (XLE −3.75%) sold on Iran deal. Favorable for PIE AI.
- Top themes: AI Supercycle ($750B hyperscaler capex 2026), Semiconductor Recovery (AMD +7% near 52w high; TSM $9 from 52w high; AVGO laggard)

## Portfolio highlights
- AMD: $547.26 (+6.98%) — $11 from 52w high ($558). Strongest performer.
- TSM: $441.40 (+4.12%) — $9 from 52w high ($450). Near breakout.
- META: $593.48 (+4.67%) — strong momentum.
- AVGO: $382.07 (−0.91%) — only semiconductor in red. June 5 miss still weighing on sentiment.
- CSCO: $120.17 (−0.77%) — mild red, not a concern.

## Exposure Decision
- Posture: RESTRICT
- Composite confidence: 65% (all APIs working; capped due to FOMC binary event tomorrow)

## Pending
- ⭐⭐⭐ **FOMC Decision + Dot Plot + Warsh press conference: 17 giugno (~2:30 PM ET / 8:30 PM IT)**
  - First meeting of Kevin Warsh as Fed Chair. Hold 97% prob (3.50–3.75%).
  - Key risk: Warsh tone on 4.2% CPI. New dot plot signals for 2026/2027.
  - After PC: reassess posture.
    - Neutral/dovish → ALLOW. Targets: AMD >$558, TSM >$450
    - Hawkish → CASH-PRIORITY
- 🕊️ US-Iran deal official signing: Friday June 19 (Switzerland) — risk if it falls apart
- 📊 QCOM Investor Day: June 24
- 📋 MSFT Earnings: July 25 (after close)
- 📋 NVDA Earnings: July 28 (after close)

## Infrastructure (resolved)
- FMP API: ✅ Working — migrated to /stable/quote (one ticker at a time; multi-symbol is premium)
- Adanos API: ✅ Working — correct endpoint /reddit/stocks/v1/stock/{ticker}, header X-API-Key
- yfinance: ✅ Working — fallback for VWCE.DE and GOOG/ASML (FMP 402 on some tickers)
- VWCE.DE change%: N/A from yfinance (price confirmed at €164.60)
