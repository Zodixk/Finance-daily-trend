# Session Memory — 2026-07-14

## Regime
- Market environment: risk-off tilt (indices down modestly); VIX 17.29 (+0.76%); S&P 500 7,515.34 (-0.79%); NASDAQ 25,873.18 (-1.55%). Geopolitical risk escalated — US-Iran fighting resumed (Trump notified Congress Jul 13), Strait of Hormuz blockade with 20% cargo fee begins today.
- VIX: 17.29
- Breadth score: N/A (market breadth CSV 403 error — persistent, many consecutive sessions)
- Uptrend participation: 24.9% ratio (composite score 34.2/100 — Cautious zone, up slightly from 31.8 on Jul 9); only 2/11 sectors uptrending; sector rotation DEFENSIVE TILT (score 38/100, Defensive leads Cyclical by 5.3pp) — Technology ranked 7th of 11 (17.8%, downtrending)
- Macro regime: FAILED (FMP legacy-endpoint 403, yfinance proxy blocked) — composite 0/100, insufficient data (same persistent issue, many consecutive sessions)
- Distribution days (IBD monitor): SPY = SEVERE (d5/d15/d25 = 2/4/8, well above thresholds); QQQ data failed to load
- Market top detector: composite 50.0/100, Orange (Elevated Risk), risk budget 60-75% — unchanged from Jul 9; Distribution Day Count component CRITICAL (100/100); other components used neutral defaults due to missing ETF data (XLP, XLY, XLV blocked)
- Sector rotation (separate skill): DEFENSIVE TILT (score 38/100, up from 33 on Jul 9); cycle-phase model leans "Late Cycle" (low confidence); Healthcare/Energy leading, Technology/Consumer Cyclical/Industrials lagging
- Bubble score: N/A (not run)

## Portfolio
- VWCE.DE: €165.78 (WebSearch fallback, -0.22% vs €166.14 prior close); FMP/yfinance both blocked for direct quote. Near 52w high (€167.08) but not at it.
- SEC0.DE: ≈€18.53 (WebSearch fallback, quote timestamp uncertain — may reflect Jul 13 close, not live Jul 14 intraday); entry ~€22.87-23.35, stop €18.50, P&L ≈-19 to -20%
- SEC0 status: recovered from Jul 9's confirmed sub-stop low (€17.49) back to approximately the €18.50 stop line — not a confirmed second breach, but essentially at the decision line. Live price should be verified directly on Trader 212 next session, since WebSearch data quality was uncertain today.
- SEC0 re-entry trigger check: Price pullback trigger requires ≤€17.54 — NOT currently met at ≈€18.53. VIX ❌ (17.29 vs >25 trigger). Base ❌ (no confirmed base).
- Two major gap-risk catalysts imminent: **ASML reports Jul 15 (tomorrow) before the open**, **TSMC reports Jul 16 (Thursday)** — both top SEC0 holdings, both within 48 hours of this session.

## Signals
- Sentiment: ⚠️ UNAVAILABLE — Adanos API monthly free-tier limit (250 req) exhausted; resets 2026-07-14T12:05:56Z (later today, after this session ran)
- Sector rotation: modest improvement vs Jul 9 (score 33→38) but Technology still lagging (7th of 11, downtrending)
- Theme detector: not run successfully this session (known persistent failure — finvizfinance unavailable); themes derived manually: (1) AI-capex valuation anxiety (bearish, chip-specific, unchanged from Jul 9), (2) Geopolitical risk premium — Strait of Hormuz blockade, escalated since Jul 9
- Key news: June CPI report due today 8:30am ET (last inflation read before Jul 28-29 FOMC); Strait of Hormuz blockade begins this afternoon (20% cargo fee, US-Iran fighting resumed); ASML/TSMC earnings previews cautiously bullish for AI-capex demand but nothing reported yet; SK Hynix (recent US IPO) falling since debut; Q2 bank earnings season opened (JPM, BAC, GS, WFC, C)
- Economic calendar: FMP endpoint returned 0 events again (persistent failure, same as prior sessions) — CPI (Jul 14) and FOMC (Jul 28-29) dates confirmed via WebSearch instead
- Earnings calendar: ASML reports Jul 15 before open (confirmed via WebSearch, not in FMP calendar window), TSMC reports Jul 16 (confirmed via FMP calendar) — both top SEC0 holdings, both within the week, major gap-risk catalysts for SEC0

## Exposure Decision
- Posture: RESTRICT (unchanged from Jul 9)
- Composite confidence: 45% (CB2 triggered — 5 skills failed/no-data: market-breadth-analyzer, macro-regime-detector, finance-sentiment, economic-calendar-fetcher, theme-detector)
- exposure-coach run (inputs: uptrend + regime + top-risk; breadth/institutional/sector/theme/ftd missing): Exposure Ceiling 36% (up slightly from 35% on Jul 9), Recommendation REDUCE_ONLY, Bias NEUTRAL, Participation NARROW, Confidence MEDIUM

## Pending
- **SEC0 price verification** — WebSearch-derived quote (≈€18.53) is uncertain in timing/accuracy; verify directly on Trader 212 next session before treating it as confirmed above/below the €18.50 stop.
- **ASML Q2 earnings — Jul 15, before market open** (tomorrow) — major SEC0 holding, gap risk.
- **TSMC Q2 earnings — Jul 16** — SEC0's largest single holding, biggest catalyst of the week.
- **June CPI report — today, 8:30am ET** — not yet released as of this session; check reaction next session.
- Adanos sentiment quota resets today at 12:05 UTC — sentiment check can be re-run later today if asked.
