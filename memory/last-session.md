# Session Memory — 2026-07-17

## Regime
- Market environment: Tech-led selloff extending — Jul 16 close: NASDAQ -1.6%, S&P -0.5% on TSMC capex-guidance-driven chip selloff (TSMC -4%, Broadcom -5%, NVIDIA -2%). Jul 17 session (as of 08:09 UTC): VIX 17.95 (+7.29%), NASDAQ 25,881.95 (-1.47%), S&P 500 7,533.77 (-0.51%).
- VIX: 17.95 (+7.29%)
- Breadth score: N/A (market breadth CSV 403 error — persistent, many consecutive sessions, unchanged)
- Uptrend participation: 26.7% ratio (composite score 40.4/100 — moved from Cautious into Neutral zone, up from 34.0 on Jul 16); 4/11 sectors uptrending; sector rotation DEFENSIVE TILT (score 43/100, unchanged from Jul 16) — Technology 9th of 11 (14.0%, marked "Up" trend despite low rank)
- Macro regime: FAILED (FMP legacy-endpoint 403, yfinance proxy blocked for RSP/SPY/HYG/LQD/IWM/TLT/XLY/XLP) — composite 0/100, insufficient data (same persistent issue, unchanged for many consecutive sessions)
- Distribution days (IBD monitor): SPY = SEVERE (d5/d15/d25 = 2/4/8, worse than Jul 16's 2/4/7); QQQ data failed to load again (persistent)
- Market top detector: composite 45.0/100, Orange (Elevated Risk), risk budget 60-75% — essentially flat vs 46.6 on Jul 16; Distribution Day Count component CRITICAL (90/100); other components used neutral defaults due to missing ETF data (VNQ, XLY, XLK all blocked)
- Bubble score: N/A (not run)

## Portfolio
- VWCE.DE: ≈€165.80 (WebSearch fallback, +0.08% — STALE data from Jul 15 close; FMP/yfinance both blocked again today, live price NOT verified for 2nd consecutive session).
- SEC0.DE: ≈€18.53 (WebSearch fallback, STALE — same Jul 15 close carried over from yesterday's memory, NOT a live Jul 17 quote. FMP returned 402 subscription-limit error, yfinance blocked). entry ~€22.87-23.35, stop €18.50.
- **SEC0 stop-loss alert — ESCALATING, HIGH PRIORITY.** Yesterday's close (€18.53) was already only 3 cents above the €18.50 stop after piercing it intraday (€18.12 low). Since then, SEC0's top holdings (TSMC -4%, Broadcom -5%, NVIDIA -2%) have sold off further on TSMC's capex-guidance news (Jul 16), and Jul 17 pre-market shows NASDAQ -1.47% with VIX +7.29%. **Live price still NOT verified for the second session running — this must be checked directly on Trader 212 immediately.** If SEC0 has now closed below €18.50 for a 2nd consecutive session, the stop-loss exit rule is triggered.
- TSMC Q2 2026 earnings reaction confirmed: record profit beat, raised FY26 revenue growth guidance to slightly above 40%, but raised capex guidance to $60-64B (from $56B ceiling) — market sold the stock ~4% on margin/return-on-spend concerns. This is the key new catalyst driving today's continued semiconductor weakness.
- ASML also fell despite raising 2026 sales outlook — same theme.
- Intel reports Jul 23 — SEC0 holding, next gap-risk event (6 days out, outside 3-day window today).

## Signals
- Sentiment: available (Adanos API worked). Reddit/X sentiment on NVDA/AMD/AVGO still shows bullish% > bearish% on every platform despite the actual chip selloff — sentiment continues to lag price action (same pattern as Jul 16). Do not treat bullish social buzz as reassurance.
- Sector rotation: DEFENSIVE TILT unchanged (43/100) — Technology still 9th of 11 sectors.
- Theme detector script: not run successfully again this session (persistent finvizfinance/finviz.com connectivity failure, tried both cached and freshly pip-installed finvizfinance) — themes derived manually via WebSearch: (1) AI-capex sustainability doubts, now company-specific (TSMC's own capex raise triggered the selloff, not just macro fear), (2) Defensive rotation continuing (Real Estate/Energy leading).
- Key news: TSMC beat-and-raise sold off ~4% on capex concerns (Jul 16); ASML same pattern; NVIDIA -2%, Broadcom -5%; Netflix -8% after hours (not a holding, but confirms fragile mega-cap tech tone); no FOMC/CPI this week (next FOMC Jul 28-29).
- Economic calendar: FMP endpoint returned 0 events again (persistent failure, unchanged across many sessions) — supplemented via WebSearch: no FOMC or CPI this week.
- Earnings calendar (FMP, worked): GOOGL Jul 21, GM Jul 21, TSLA Jul 22, T Jul 22, INTC Jul 23, LMT Jul 23, NOK Jul 23, AAL Jul 23, VZ Jul 24, HCA Jul 24.

## Exposure Decision
- Posture: RESTRICT / REDUCE_ONLY (consistent with Jul 16's RESTRICT)
- Composite confidence: 45% (CB2 triggered — 4 skills failed/no-data: market-breadth-analyzer, macro-regime-detector, economic-calendar-fetcher (FMP leg), theme-detector; same persistent pattern as prior sessions)
- exposure-coach run (inputs: uptrend + regime + top-risk; breadth/institutional/sector/theme missing as formal JSON inputs): Exposure Ceiling 40% (up slightly from 38% on Jul 16), Recommendation REDUCE_ONLY, Bias NEUTRAL, Participation NARROW, Confidence MEDIUM
- Telegram notification failed (pre-existing script bug: parses for Italian-language markers "POSTURA"/"Insight del Giorno" that don't match the English report structure, producing malformed Markdown that Telegram rejected with a 400 parse error). Not a data issue — flagged for future fix, not blocking.

## Pending
- **SEC0 price verification — ESCALATING, HIGHEST PRIORITY.** Verify live price directly on Trader 212 next session (2nd consecutive session unverified). If closed below €18.50 for a second consecutive session, the stop-loss exit rule is triggered.
- **Intel Q2 earnings — Jul 23** — SEC0 holding, gap risk, now 6 days out.
- Persistent data-source failures continuing across many sessions and should be considered structurally broken, not transient: market-breadth-analyzer (TraderMonty CSV 403), macro-regime-detector (FMP legacy endpoint 403 + yfinance proxy blocked), economic-calendar-fetcher (FMP returns 0 events), theme-detector (finvizfinance/finviz.com unavailable even after fresh pip install), ibd-distribution-day-monitor QQQ leg (FMP legacy endpoint 403), FMP direct quotes for VWCE.DE/SEC0.DE (yfinance curl tunnel 403, FMP 402 subscription limit on SEC0).
- **Telegram notify script bug** — fails to parse the English-language briefing report format (looks for Italian section markers). Should be fixed to be language-structure-agnostic (e.g. match on numbered section headers instead of literal Italian phrases) next time this is touched.
