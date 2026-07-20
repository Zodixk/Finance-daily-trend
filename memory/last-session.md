# Session Memory — 2026-07-20

## Regime
- Market environment: Tech-led selloff continuing from last week — Jul 17 close (last full session before today, Monday): NASDAQ 25,520.24 (-1.40%), S&P 500 7,457.69 (-1.01%), VIX 18.55 (-1.17%). Weekly recap: Nasdaq -2.9%, S&P -1.6% for the week, driven by AI-capex slowdown fears (competition from cheaper Chinese models e.g. Moonshot's "Kimi") and rotation into financials/industrials/energy.
- VIX: 18.55 (still below the 20 "fear threshold," but up sharply over the past week)
- Breadth score: N/A (market breadth CSV 403 error — persistent, many consecutive sessions, unchanged)
- Uptrend participation: 26.4% ratio (composite score 36.4/100 — moved back from Neutral into Cautious zone, down from 40.4 on Jul 17); 3/11 sectors uptrending (down from 4/11); sector rotation DEFENSIVE TILT (score 39/100, down from 43 on Jul 17) — Technology 9th of 11 (14.5%, marked "Up" trend despite low rank)
- Macro regime: FAILED (FMP legacy-endpoint 403, yfinance proxy blocked for RSP/SPY/TLT/SHY/HYG/LQD/XLY/XLP) — composite 0/100, insufficient data (same persistent issue, unchanged for many consecutive sessions)
- Distribution days (IBD monitor): SPY = SEVERE (d5/d15/d25 = 3/5/8, worse than Jul 17's 2/4/8); QQQ data failed to load again (persistent legacy-endpoint 403)
- Market top detector: composite 47.4/100, Orange (Elevated Risk), risk budget 60-75% — roughly flat vs 45.0 on Jul 17; Distribution Day Count component CRITICAL (90/100); other components used neutral defaults due to missing ETF data (VNQ, XLU, XLC, XLK, XLY, XLV all blocked). Follow-Through Day monitor: rally attempt Day 14 from 2026-06-26 low, FTD window (Day 4-7) passed without qualifying day. Closest historical analog: 2018 Q4 correction.
- Bubble score: N/A (not run)

## Portfolio
- VWCE.DE: €164.16, -0.27% (WebSearch fallback, Jul 17 close — FMP/yfinance both blocked again today for this ticker specifically, though FMP did return index-level quotes).
- SEC0.DE: **CONFIRMED below stop-loss.** Jul 17 close verified via WebSearch (stockanalysis.com/CNBC) at €16.92, -3.84% — the first non-stale, externally-confirmed price after two prior sessions of unverified/stale carryover data. Today's (Jul 20) live intraday quote ≈€17.62, -1.50% — also below the €18.50 stop. Entry ~€22.87-23.35, stop €18.50.
- **SEC0 stop-loss alert — LIKELY TRIGGERED, HIGHEST PRIORITY, ACTION NEEDED TONIGHT.** Jul 17's confirmed close (€16.92) was already well under €18.50. If tonight's (Jul 20) close is also below €18.50, that is 2 consecutive confirmed closes under the stop — the exit-and-reassess rule from the playbook (Section 8.2) is met. This needs verification on Trader 212 at today's close and, if confirmed, an actual exit decision — this routine can flag it but cannot execute the trade.
- **Notable wrinkle:** at €16.92/€17.62, SEC0 is also ~27% below its recent high (~€23.33), which crosses the *separate* "≥25% pullback re-entry trigger" threshold (≤€17.54) from Section 8.3 of the playbook. Do not conflate the two: the re-entry trigger is for deploying fresh capital later, not a reason to hold through or ignore the stop-loss on the existing position.
- Intel (SEC0 holding) reports Jul 23 — now inside the 3-day gap-risk window (was 6 days out on Jul 17).
- ASML raised FY2026 revenue guidance again, to €43-45bn (from €36-40bn) — second raise this year, on strong AI chip demand. A genuine positive counter-signal: demand looks intact, the market is repricing valuation/capex-return timing, not the growth thesis itself.
- TSMC down ~15% from its all-time high, NVIDIA >10% off its high, Broadcom >20% off its high, despite TSMC's own recent beat-and-raise — all three are SEC0 holdings and under direct pressure.
- Next catalyst: Alphabet (GOOGL) earnings Jul 21 — first major hyperscaler capex read-through, market-moving for the whole semiconductor complex even though GOOGL is not itself a SEC0/portfolio holding.

## Signals
- Sentiment: available (Adanos API worked). X/Twitter sentiment still net-bullish on every semiconductor-relevant ticker (NVDA, AAPL, MSFT, META, GOOG, AMZN, AMD, AVGO), but Reddit trend is "falling" across the board — social buzz cooling but not yet bearish. Continues to lag actual price action; do not treat as reassurance.
- Sector rotation: DEFENSIVE TILT, 39/100 (down from 43 on Jul 17) — Technology still 9th of 11 sectors. Energy and Real Estate lead; Technology, Consumer Cyclical, Industrials lag.
- Theme detector script: failed again this session (persistent finviz.com/finvizfinance connectivity block, even after fresh pip install of finvizfinance) — themes derived manually via WebSearch: (1) AI-capex sustainability debate, now with a genuine counter-signal (ASML's guidance raise) suggesting a valuation/positioning reset rather than the end of the AI infrastructure cycle, (2) Defensive rotation continuing (chips/growth → financials/industrials/energy).
- Key news: SMH (semiconductor ETF) down ~9% over the past month, third weekly decline in four weeks; ASML guidance raise a bright spot; next major catalyst is hyperscaler earnings starting with Alphabet Jul 21; no FOMC/CPI this week (next FOMC Jul 28-29).
- Economic calendar: FMP endpoint returned 0 events again (persistent failure, unchanged across many sessions) — supplemented via WebSearch: no FOMC or CPI this week.
- Earnings calendar (FMP, worked): GOOGL Jul 21, GM Jul 21, TSLA Jul 22, T Jul 22, INTC Jul 23, LMT Jul 23, NOK Jul 23, AAL Jul 23, VZ Jul 24, HCA Jul 24.

## Exposure Decision
- Posture: RESTRICT / REDUCE_ONLY (consistent with Jul 17's RESTRICT)
- Composite confidence: 45% (CB2 triggered — 4 skills failed/no-data: market-breadth-analyzer, macro-regime-detector, economic-calendar-fetcher (FMP leg), theme-detector; same persistent pattern as prior sessions)
- exposure-coach run (inputs: uptrend + regime + top-risk; breadth/institutional/sector/theme missing as formal JSON inputs): Exposure Ceiling 38% (down slightly from 40% on Jul 17), Recommendation REDUCE_ONLY, Bias NEUTRAL, Participation NARROW, Confidence MEDIUM
- Telegram notification failed again (pre-existing script bug: parses for Italian-language markers that don't match the English report structure, producing malformed Markdown that Telegram rejected with a 400 parse error — same failure mode flagged on Jul 17, still not fixed). Not a data issue — flagged for future fix, not blocking.

## Pending
- **SEC0 stop-loss decision — HIGHEST PRIORITY, ACTION NEEDED.** Jul 17 close (€16.92) confirmed below the €18.50 stop. Verify tonight's (Jul 20) close on Trader 212: if also below €18.50, the 2-consecutive-close exit rule is met — this should be treated as resolved/needing a real decision next session, not re-flagged as merely "unverified."
- **Intel Q2 earnings — Jul 23** — SEC0 holding, now inside the 3-day gap-risk window.
- **Alphabet (GOOGL) earnings — Jul 21** — not a portfolio holding, but first hyperscaler capex read-through; watch commentary for AI infrastructure spending signals that affect every SEC0 holding.
- Persistent data-source failures continuing across many sessions and should be considered structurally broken, not transient: market-breadth-analyzer (TraderMonty CSV 403), macro-regime-detector (FMP legacy endpoint 403 + yfinance proxy blocked), economic-calendar-fetcher (FMP returns 0 events), theme-detector (finvizfinance/finviz.com unavailable even after fresh pip install), ibd-distribution-day-monitor QQQ leg (FMP legacy endpoint 403), FMP/yfinance direct quotes for VWCE.DE/SEC0.DE (yfinance curl tunnel 403, FMP 402/403 on the DE-listed tickers) — WebSearch fallback is now the reliable path for these two tickers.
- **Telegram notify script bug** — still fails to parse the English-language briefing report format (looks for Italian section markers). Should be fixed to be language-structure-agnostic (e.g. match on numbered section headers instead of literal Italian phrases) — flagged for three consecutive sessions now, still unresolved.
