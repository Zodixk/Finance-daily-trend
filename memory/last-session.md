# Session Memory — 2026-07-13

## Regime
- Market environment: risk-on on the surface (VIX 16.41, +9.18% vs prior; S&P 500 7,575.39 +0.42%; NASDAQ 26,281.61 +0.29%), but internals remain narrow/defensive
- VIX: 16.41
- Breadth score: N/A (market-breadth-analyzer CSV proxy blocked — persistent failure, many consecutive sessions)
- Uptrend participation: composite 35.9/100 (Cautious zone), up from 31.8 on Jul 9; only 2/11 sectors uptrending (was 4/11); exposure guidance Defensive (30-60%)
- Macro regime: FAILED (yfinance proxy blocked, FMP legacy endpoints 403) — composite 0/100, insufficient data, same persistent issue
- Distribution days (IBD monitor): FAILED (FMP legacy endpoint 403, persistent issue)
- Market top detector: composite 45.0/100, Orange (Elevated Risk), risk budget 60-75% — improved from 50.0 on Jul 9; Distribution Day Count component still CRITICAL (90/100), other components neutral-default due to missing ETF data
- Sector rotation (separate skill): DEFENSIVE TILT score 38/100 (improved from 33 on Jul 9); cycle-phase model leans "Late Cycle" (moderate confidence); Healthcare (overbought, 47.5%)/Energy leading, Technology (7th of 11, up from 8th)/Consumer Cyclical/Industrials lagging
- Bubble score: N/A (not run)

## Portfolio
- VWCE.DE: €166.14 (WebSearch, Jul 10 close, +0.35%); direct FMP/yfinance quote blocked
- SEC0.DE: €19.07 (WebSearch, Jul 9 ~14:06 CET, +5.38%); entry ~€22.87-23.35, stop €18.50, P&L ≈ -17.5% (improved from ≈-23.5% on Jul 9)
- ✅ **SEC0 stop-loss scare resolved (for now):** Jul 8 close €17.82 and Jul 9 intraday €17.49 were both below the €18.50 hard stop (flagged urgent on Jul 9), but SEC0 rallied +5.38% intraday Jul 9 and the sector (SOX) has since reclaimed its 50-day moving average. The 2-consecutive-close exit rule did NOT confirm. No exit action taken. Re-verify next session with a fresh confirmed XETRA close — treat €18.50 as still live given how fast the round-trip happened.
- SEC0 re-entry trigger check: Price pullback — touched ≤€17.54 briefly intraday Jul 9 during an active decline (not a stable base, doesn't count per playbook), now back at €19.07 so trigger no longer active. VIX ❌ (16.41 vs >25). Base ❌ (no base forming, still volatile). Current recommendation unchanged: HOLD €50, do not add.

## Signals
- Sentiment: ⚠️ UNAVAILABLE — Adanos API monthly free-tier limit still exhausted, resets 2026-07-14 12:05 UTC (tomorrow)
- Sector rotation: improved slightly but still defensive; Technology 7th of 11, still downtrending
- Theme detector: not run this session (persistent failure); themes derived manually: (1) AI-capex valuation anxiety ahead of ASML/TSMC earnings, (2) semiconductor sector stabilizing post-Samsung-selloff (SOX back above 50DMA) but still ~11% below June peak
- Key news: Semiconductor sector stabilizing — SOX/NASDAQ reclaimed 50-day MAs after the Samsung-earnings-triggered selloff. SK Hynix's record $26.5bn Nasdaq listing jumped 12.8% on debut (bullish demand signal) but SK Hynix/Samsung shares still weak in Seoul on profit-taking. TSMC reported +67.9% YoY June sales ahead of its Jul 16 earnings.
- Economic calendar: CPI Tuesday Jul 14; Fed Chair Kevin Warsh testifies House Financial Services Committee Jul 14, Senate Banking Committee Jul 15. Next FOMC meeting date not freshly confirmed this session — carried over estimate Jul 28-29 from prior session, needs re-verification.
- Earnings calendar: ASML reports Jul 15 (before open); TSMC reports Jul 16 (14:00-15:30) — both top SEC0 holdings, both this week, major gap-risk catalysts for SEC0.

## Exposure Decision
- Posture: RESTRICT / REDUCE_ONLY (slightly less severe than Jul 9's near-cash-priority tone)
- Composite confidence: 45% (CB2 triggered — 4 skills failed/no-data: market-breadth-analyzer, macro-regime-detector, ibd-distribution-day-monitor, finance-sentiment)
- exposure-coach run (inputs: uptrend + regime + top-risk + sector): Exposure Ceiling 39% (up from 35% on Jul 9), Recommendation REDUCE_ONLY, Bias NEUTRAL, Participation NARROW, Confidence MEDIUM (missing breadth/institutional/ftd/theme inputs)

## Pending
- **Re-verify SEC0 stop status next session** with a fresh confirmed XETRA close — the Jul 8-9 stop breach did not confirm as a 2-day exit, but the position remains volatile; do not treat this as fully resolved.
- **Jul 14:** CPI release; Fed Chair Warsh House testimony; Adanos sentiment quota resets same day (12:05 UTC).
- **Jul 15:** ASML Q2 earnings (before open) — major SEC0 catalyst; Fed Chair Warsh Senate testimony.
- **Jul 16:** TSMC Q2 2026 earnings (14:00-15:30) — major SEC0 catalyst, largest single holding.
- **Jul 28-29 (unconfirmed this session):** Next FOMC meeting — re-verify exact date next check.
- **Data quality risk (persistent, unresolved):** market-breadth-analyzer (tradermonty.github.io CSV), macro-regime-detector (yfinance proxy + FMP legacy endpoints), ibd-distribution-day-monitor (FMP legacy endpoint), and direct FMP/yfinance quotes for VWCE.DE/SEC0.DE have now failed for many consecutive sessions. Recommend reviewing the FMP subscription tier (legacy endpoints deprecated Aug 31 2025) and the sandbox network egress allowlist for yfinance/tradermonty.github.io — this is a recurring network-policy/subscription-tier issue, not a one-off.
