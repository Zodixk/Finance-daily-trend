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

All skills are in `skills/`. Always read the SKILL.md before executing a skill.

### Market Structure
| Skill | Purpose |
|---|---|
| `market-environment-analysis` | Global risk-on/off, VIX, indices |
| `market-breadth-analyzer` | Breadth score 0–100 (public CSV) |
| `breadth-chart-analyst` | Breadth chart interpretation |
| `uptrend-analyzer` | Uptrend participation rate |

### Regime & Risk
| Skill | Purpose |
|---|---|
| `macro-regime-detector` | Structural regime: bull/bear/sideways |
| `market-top-detector` | Topping signals |
| `ibd-distribution-day-monitor` | IBD distribution day count |
| `us-market-bubble-detector` | Bubble probability score |
| `downtrend-duration-analyzer` | Downtrend depth and age |

### News & Sentiment
| Skill | Purpose |
|---|---|
| `market-news-analyst` | Market-moving news last 24h |
| `finance-sentiment` | Reddit/X/Polymarket sentiment per ticker (Adanos API) |

### Sector & Themes
| Skill | Purpose |
|---|---|
| `sector-analyst` | Tech sector rotation |
| `theme-detector` | Trending investment themes |
| `institutional-flow-tracker` | Institutional money flow signals |
| `ftd-detector` | Follow-Through Day detection |

### Calendar & Earnings
| Skill | Purpose |
|---|---|
| `economic-calendar-fetcher` | FOMC, CPI, NFP this week |
| `earnings-calendar` | Earnings next 7 days |
| `earnings-preview` | Pre-earnings setup for a ticker |
| `earnings-recap` | Post-earnings analysis |
| `earnings-trade-analyzer` | Earnings trade structure |

### Stock & ETF Analysis
| Skill | Purpose |
|---|---|
| `us-stock-analysis` | Full analysis of a US ticker |
| `technical-analyst` | Chart pattern + technicals |
| `fundamental-analysis` | Fundamentals (yfinance) |
| `company-valuation` | DCF and valuation multiples |
| `estimate-analysis` | EPS/Rev estimate revisions |
| `etf-premium` | ETF premium/discount to NAV |
| `stock-correlation` | Correlation matrix |
| `stock-liquidity` | Liquidity and spread analysis |
| `saas-valuation-compression` | SaaS multiple compression |
| `stanley-druckenmiller-investment` | Druckenmiller-style macro read |

### Portfolio & Exposure
| Skill | Purpose |
|---|---|
| `exposure-coach` | Posture: allow / restrict / cash-priority |
| `position-sizer` | Position size given stop |
| `portfolio-manager` | Portfolio-level risk view |
| `scenario-analyzer` | What-if scenario modeling |

### Screeners
| Skill | Purpose |
|---|---|
| `vcp-screener` | VCP breakout candidates |
| `canslim-screener` | CAN SLIM screen |
| `finviz-screener` | Finviz-style filter |
| `pead-screener` | Post-earnings drift candidates |
| `value-dividend-screener` | Value + dividend screen |
| `dividend-growth-pullback-screener` | Dividend growth on pullback |
| `pair-trade-screener` | Pair trade candidates |

### Trade Strategy
| Skill | Purpose |
|---|---|
| `sepa-strategy` | SEPA trend-following strategy |
| `options-payoff` | Options P&L at expiry |
| `options-strategy-advisor` | Options strategy recommendation |
| `parabolic-short-trade-planner` | Parabolic short setup |
| `trade-hypothesis-ideator` | Trade idea generation |

### Edge Development
| Skill | Purpose |
|---|---|
| `edge-candidate-agent` | Find edge candidates |
| `edge-concept-synthesizer` | Synthesize edge concept |
| `edge-hint-extractor` | Extract edge hints from data |
| `edge-pipeline-orchestrator` | Orchestrate edge pipeline |
| `edge-signal-aggregator` | Aggregate multiple signals |
| `edge-strategy-designer` | Design a full edge strategy |
| `edge-strategy-reviewer` | Review and stress-test strategy |
| `backtest-expert` | Backtest a strategy |
| `strategy-pivot-designer` | Pivot existing strategy |

### Performance & Memory
| Skill | Purpose |
|---|---|
| `trader-memory-core` | Store and recall trade memory |
| `trade-performance-coach` | Trade performance review |
| `signal-postmortem` | Postmortem on a signal |

### Dividend (Kanchi)
| Skill | Purpose |
|---|---|
| `kanchi-dividend-review-monitor` | Dividend watchlist review |
| `kanchi-dividend-sop` | Dividend SOP execution |
| `kanchi-dividend-us-tax-accounting` | US dividend tax accounting |

### Meta / Utilities
| Skill | Purpose |
|---|---|
| `trading-skills-navigator` | Find the right skill for a task |
| `skill-designer` | Design a new skill |
| `skill-idea-miner` | Mine skill ideas from trades |
| `skill-integration-tester` | Test skill integration |
| `dual-axis-skill-reviewer` | Dual-axis skill review |
| `data-quality-checker` | Check data quality |

---

## Daily Briefing Routine

Run every weekday morning. Steps 1–7 are mandatory. Step 8 produces the report.

### Step 1 — Market Structure
Read and run:
1. `market-environment-analysis` → global risk-on/off signal, VIX, major indices
2. `market-breadth-analyzer` → breadth score 0–100
3. `uptrend-analyzer` → uptrend participation rate

### Step 2 — Regime & Risk
Read and run:
4. `macro-regime-detector` → structural regime (bull/bear/sideways)
5. `market-top-detector` → topping signals score
6. `ibd-distribution-day-monitor` → distribution day count

### Step 3 — Portfolio Quotes
7. `pip install -q requests`
8. `python scripts/fmp_briefing.py` → quotes for FTDL.DE + 12 PIE tickers

### Step 4 — News & Sentiment
Read and run:
9. `market-news-analyst` → top market-moving news last 24h
10. `finance-sentiment` for tickers: NVDA, AAPL, MSFT, META, GOOG, AMZN, AMD, AVGO → Reddit/X/Polymarket sentiment scores

### Step 5 — Forward Calendar
Read and run:
11. `economic-calendar-fetcher` → FOMC, CPI, NFP this week
12. `earnings-calendar` → earnings next 7 days, flag PIE tickers

### Step 6 — Sector & Themes
Run if Step 1 regime is not critical:
13. `sector-analyst` → tech sector rotation signal
14. `theme-detector` → trending themes (focus: AI, semiconductors)

### Step 7 — Exposure Decision
Read and run:
15. `exposure-coach` using all outputs from Steps 1–6 → posture: allow / restrict / cash-priority

### Step 8 — Synthesis
Save a single markdown report to `reports/briefing-YYYY-MM-DD.md`.

**Report structure:**
1. **Market Overview** — risk-on/off, VIX, breadth score, regime
2. **PIE AI Quotes** — table: price, change%, 52w high/low
3. **Morning News** — top 5 market-moving events with impact rating
4. **Social Sentiment** — Reddit/X/Polymarket scores for top PIE tickers
5. **Calendar** — macro events + earnings this week
6. **Sector & Themes** — rotation signal, top 2 themes
7. **Exposure Decision** — allow / restrict / cash-priority with reasoning
8. **Insight of the Day** — one concrete, data-backed observation for Alessandro

**Always end with:** "Hai domande su qualcosa di specifico di oggi?"

---

## On-Demand Skills

After the briefing, Alessandro may ask follow-up questions. Use any skill in `skills/` to answer.

Examples:
- "analizza NVDA" → `us-stock-analysis` + `technical-analyst`
- "screena breakout VCP" → `vcp-screener`
- "quante azioni tenere ora?" → `exposure-coach` + `position-sizer`
- "mostrami gli earnings di AAPL" → `earnings-preview` + `earnings-trade-analyzer`
- "correlazione tra NVDA e AMD" → `stock-correlation`

---

## Fallback Rules

- If a skill script fails → fall back to web search replicating the skill's logic
- If Adanos API unavailable → skip sentiment, note ⚠️ in report
- If FMP rate limit reached → use yfinance as fallback for quotes
- Never invent or estimate numbers — skip the section and flag it
