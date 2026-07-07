# Session Memory — 2026-07-07

## Regime
- Market environment: risk-on, calm (VIX 15.94, +2.38%); S&P 500 fresh record high 7,537.43 (+0.72%); NASDAQ 26,121.16 (+1.12%)
- VIX: 15.94
- Breadth score: N/A (market breadth CSV 403 error — 13th consecutive session)
- Uptrend participation: 29.8% (composite score 50.7/100 — Neutral zone, up slightly from 50.8 on Jul 3); 7/11 sectors uptrending; sector rotation component improved to BALANCED (Cyclical-Defensive gap -3.0pp, was DEFENSIVE TILT)
- Macro regime: FAILED (FMP legacy-endpoint 403, no yfinance module) — composite 0/100, insufficient data
- Distribution days (IBD monitor): FAILED (same FMP legacy-endpoint issue) — no data
- Market top detector: composite 32.1/100, Yellow (Early Warning), risk budget 80-90% — several sub-components used neutral defaults due to missing breadth/sentiment data
- Sector rotation (separate skill): BALANCED (score 45/100); Technology ranked 8th of 11 sectors (18.0%, downtrending) — improved from dead-last on Jul 3 but still weak; cycle-phase model leans "Recession" (low confidence)
- Bubble score: N/A (not run)

## Portfolio
- VWCE.DE: ~€166.60 (WebSearch fallback, +0.43%); FMP/yfinance both blocked for direct quote
- SEC0.DE: ~€19.42 (WebSearch fallback, +0.23%); entry ~€22.87, stop €18.50, P&L **≈-15.1%**, distance to stop **≈4.7%** — 🔴 escalated sharply from ~8% on Jul 3, watch daily
- Two-consecutive-close rule: NOT triggered (cannot confirm without historical closes — not available today). SEC0 above hard stop.
- SEC0 re-entry trigger check: Price pullback ❌ (~€19.42 vs ≤€17.54 trigger — closer than before), VIX ❌ (15.94 vs >25 trigger), Base ❌ (no confirmed base)

## Signals
- Sentiment: ⚠️ UNAVAILABLE — Adanos API monthly free-tier limit (250 req) still exhausted; resets 2026-07-14
- Sector rotation: IMPROVED but still negative-leaning for semiconductors — Technology 8th of 11 (was dead last), still downtrending
- Theme detector: FAILED (finvizfinance client unavailable)
- Key news: Broadcom's cautious AI chip guidance ($16B vs $17.2B est.), deepening memory-chip crisis, and smartphone-demand fears drove June's SOX selloff — directly relevant to SEC0 (Broadcom is a top holding). Long-term fundamentals still strong: TSMC +55.5% and ASML +93.3% in H1 2026, broader tech sector +19.4% H1; TSMC reiterating US/Japan/Germany fab expansion. FOMC minutes from June meeting due Jul 8 (tomorrow) — watch tone on hawkish dot plot (2026 hike, not cut).
- Economic calendar: FMP endpoint returned 0 events even for known past dates (broken) — replaced with WebSearch. No CPI/NFP this week; FOMC minutes Jul 8; next full FOMC meeting Jul 28-29 (no SEP).

## Exposure Decision
- Posture: RESTRICT (maintained — continuing multi-session pattern)
- Composite confidence: 45% (CB2 triggered — 6 skills failed/no-data: market-breadth-analyzer, macro-regime-detector, ibd-distribution-day-monitor, finance-sentiment, theme-detector, economic-calendar-fetcher)
- exposure-coach run (inputs: uptrend + regime + top-risk): Exposure Ceiling 49%, Recommendation REDUCE_ONLY, Bias NEUTRAL, Confidence MEDIUM (missing breadth/institutional/sector-json/theme/ftd inputs)

## Pending
- **Active risk — SEC0 approaching stop (escalated):** ~-15.1% from entry, distance to hard stop (€18.50) now only ~4.7% (was ~8% on Jul 3). This is the top watch item — a single bad session in semiconductors could bring SEC0 within range of the two-consecutive-close exit rule. Check daily this week.
- **Jul 8 (tomorrow):** FOMC minutes from June meeting — watch for detail on the hawkish dot plot shift (2026 hike vs cut).
- **Jul 14:** Q2 earnings season begins (JPM, BAC, GS, WFC) — no direct SEC0 impact but sets market tone.
- **Jul 16:** TSMC Q2 2026 earnings — major SEC0 catalyst, watch closely.
- **Jul 28-29:** Next full FOMC meeting (no Summary of Economic Projections).
- **~Jul 29:** PCE release still the primary posture-upgrade trigger flagged in prior sessions — confirm exact date next session.
- **Data quality risk (persistent, escalating further):** FMP's historical-price endpoints now return "Legacy Endpoint" 403 errors across macro-regime-detector, ibd-distribution-day-monitor, market-top-detector (partial), and sector rotation candidate scans — this is a broader FMP plan/tier issue, not a one-off. No yfinance module installed as fallback. market-breadth-analyzer blocked 13 consecutive sessions (tradermonty.github.io proxy). Adanos sentiment still exhausted (resets Jul 14). Finviz-dependent theme-detector still blocked. Recommend reviewing FMP subscription tier and installing yfinance as a working fallback.
- **SEC0 hard stop:** Close below EUR 18.50 for 2 consecutive days → EXIT. Currently NOT triggered, but buffer is thin (~4.7%).
