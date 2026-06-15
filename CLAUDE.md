# Finance Daily Briefing — Alessandro's Portfolio

## Portfolio

**Investor profile:** Growth investor, beginner, EUR-based, broker Trader 212.
**Risk:** max 7-8% stop loss, max 10% per position, max drawdown 15%.

**ETF Core:** FTDL.DE — All-World Accumulating, XETRA

**PIE AI (Trader 212):**
GOOG, AMZN, AVGO, NVDA, AMD, AAPL, ASML, CSCO, META, MSFT, QCOM, TSM

## Environment Variables

- `FMP_API_KEY` — Financial Modeling Prep (quotes, earnings, macro)
- `ADANOS_API_KEY` — Adanos Finance (Reddit/X/Polymarket sentiment)

## Available Skills

All skills are in `skills/`. Read the relevant SKILL.md before executing each step.

| Skill | File | Data source |
|---|---|---|
| `market-environment-analysis` | skills/market-environment-analysis/SKILL.md | Web search |
| `market-breadth-analyzer` | skills/market-breadth-analyzer/SKILL.md | Public CSV |
| `uptrend-analyzer` | skills/uptrend-analyzer/SKILL.md | Public CSV |
| `macro-regime-detector` | skills/macro-regime-detector/SKILL.md | FMP + yfinance |
| `market-top-detector` | skills/market-top-detector/SKILL.md | FMP |
| `ibd-distribution-day-monitor` | skills/ibd-distribution-day-monitor/SKILL.md | FMP |
| `market-news-analyst` | skills/market-news-analyst/SKILL.md | Web search |
| `finance-sentiment` | skills/finance-sentiment/SKILL.md | Adanos API |
| `sector-analyst` | skills/sector-analyst/SKILL.md | FMP + web |
| `theme-detector` | skills/theme-detector/SKILL.md | Web + FMP |
| `economic-calendar-fetcher` | skills/economic-calendar-fetcher/SKILL.md | FMP |
| `earnings-calendar` | skills/earnings-calendar/SKILL.md | FMP |
| `earnings-trade-analyzer` | skills/earnings-trade-analyzer/SKILL.md | FMP |
| `exposure-coach` | skills/exposure-coach/SKILL.md | Upstream outputs |
| `us-stock-analysis` | skills/us-stock-analysis/SKILL.md | FMP |

## Routine Instructions

Run this sequence every weekday morning. Read each SKILL.md before executing the step.

### Step 1 — Market Structure (always run)
1. Read and run `market-environment-analysis` → global risk-on/off, VIX, indices
2. Read and run `market-breadth-analyzer` → breadth score 0-100
3. Read and run `uptrend-analyzer` → uptrend participation rate

### Step 2 — Regime & Risk (always run)
4. Read and run `macro-regime-detector` → structural regime (bull/bear/sideways)
5. Read and run `market-top-detector` → topping signals
6. Read and run `ibd-distribution-day-monitor` → distribution day count

### Step 3 — Portfolio Quotes (always run)
7. Install requests: `pip install -q requests`
8. Run: `python scripts/fmp_briefing.py` → quotes for FTDL.DE + 12 PIE tickers

### Step 4 — News & Sentiment (always run)
9. Read and run `market-news-analyst` → market-moving news last 24h
10. Read and run `finance-sentiment` for tickers: NVDA, AAPL, MSFT, META, GOOG, AMZN, AMD, AVGO → Reddit/X/Polymarket sentiment scores

### Step 5 — Forward Calendar (always run)
11. Read and run `economic-calendar-fetcher` → FOMC, CPI, NFP this week
12. Read and run `earnings-calendar` → earnings next 7 days, flag PIE tickers

### Step 6 — Sector & Themes (run if Step 1 score is not critical)
13. Read and run `sector-analyst` → tech sector rotation
14. Read and run `theme-detector` → trending themes (focus: AI, semiconductors)

### Step 7 — Exposure Decision
15. Read and run `exposure-coach` using outputs from Steps 1-6 → posture: allow / restrict / cash-priority

### Step 8 — Synthesis
Produce a single markdown report saved to `reports/briefing-YYYY-MM-DD.md`.

**Report structure:**
1. **Market Overview** — risk-on/off, VIX, breadth score, regime
2. **PIE AI Quotes** — table with price, change%, 52w high/low
3. **Morning News** — top 5 market-moving events with impact rating
4. **Social Sentiment** — Reddit/X/Polymarket scores for top PIE tickers
5. **Calendar** — macro events + earnings this week
6. **Sector & Themes** — rotation signal, top 2 themes
7. **Exposure Decision** — allow / restrict / cash-priority with reasoning
8. **Insight of the Day** — one concrete, data-backed observation for Alessandro

**Always end with:** "Hai domande su qualcosa di specifico di oggi?"

## Fallback Rules

- If a skill script fails → fall back to web search replicating the skill's logic
- If Adanos API unavailable → skip sentiment, note ⚠️ in report
- If FMP rate limit reached → use yfinance as fallback for quotes
- Never invent or estimate numbers — skip the section and flag it
