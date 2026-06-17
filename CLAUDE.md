# Finance Daily Briefing — Alessandro's Portfolio

## Portfolio

**Investor profile:** Growth investor, beginner, EUR-based, broker Trader 212.
**Risk:** max 7-8% stop loss, max 10% per position, max drawdown 15%.

**ETF Core:** VWCE (VWCE.DE su XETRA) — Vanguard FTSE All-World Accumulating, EUR-hedged. Long-term anchor — never recommend selling entirely.

**PIE AI (Trader 212):**
GOOG, AMZN, AVGO, NVDA, AMD, AAPL, ASML, CSCO, META, MSFT, QCOM, TSM

## Environment Variables

- `FMP_API_KEY` — Financial Modeling Prep (quotes, earnings, macro)
- `ADANOS_API_KEY` — Adanos Finance (Reddit/X/Polymarket sentiment)
- `GITHUB_TOKEN` — GitHub token for pushing memory at end of session
- `TELEGRAM_BOT_TOKEN` — Telegram bot token for daily notification
- `TELEGRAM_CHAT_ID` — Telegram chat ID (your personal chat with the bot)

All keys are stored in `.env` (repo root, gitignored). The scripts auto-load `.env` at startup.

### ⚠️ Network Policy (Claude Code on the Web)

The sandbox may block external API hosts. If you see `"Host not in allowlist"` errors, add these to your environment's egress whitelist:

- `financialmodelingprep.com` — FMP API (quotes, news, earnings, macro)
- `api.adanos.org` — Adanos sentiment API
- `query1.finance.yahoo.com`, `query2.finance.yahoo.com` — yfinance fallback

**Fallback chain:** FMP → yfinance → web search (WebSearch tool). Skills always degrade gracefully.

## User-Aware Framing Rules

Apply these rules throughout the entire session, including on-demand questions:

1. **Language:** always write in English. Explain signals in plain language. Alessandro is a beginner — no unexplained jargon.
2. **Currency:** Alessandro is EUR-based. Note EUR/USD when converting USD figures.
3. **Position size:** never recommend a position >10% of portfolio. Always include a stop level (7-8%).
4. **Portfolio relevance:** when any signal fires, immediately flag which PIE AI tickers are directly affected.
5. **Tech bias:** PIE AI is concentrated in tech/AI/semiconductors. Flag when sector rotation moves against tech.
6. **VWCE:** is the long-term core — never flag it as a sell unless there is an extreme, data-backed macro event.
7. **Tone:** concrete and actionable. No generic advice. No invented numbers.
8. **52w High context:** whenever a ticker is near or at its 52w high, always search for the exact date that high was set and whether it is also an all-time high. Distinguish clearly: a 52w high set yesterday is very different from one set 11 months ago. State it explicitly (e.g. "52w high of $558 set yesterday Jun 15 — also all-time high").

## Confidence Scoring

After each skill run, assign a confidence tier to its output:

| Tier | Score | Condition |
|---|---|---|
| HIGH | ≥75% | Data-backed, consistent with ≥2 other signals |
| MEDIUM | 50–74% | Partial data or mild conflict with other signals |
| LOW | <50% | Conflicting signals, missing data, or high uncertainty |

**Composite confidence** = weighted average of all skill outputs, capped at **92%** (never 100%).

Automatic caps:
- If regime skills (Steps 1 + 2) contradict each other → cap composite at 60%
- If VIX > 30 → cap composite at 70% (high uncertainty environment)
- If >2 skills fail or return no data → cap composite at 55%

Report composite confidence explicitly in the Exposure Decision section.

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
| `breakout-trade-planner` | Breakout trade setup |
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
| `skill-creator` | Create a new skill |
| `startup-analysis` | Startup analysis (VC / job / CEO lens) |
| `hormuz-strait` | Hormuz Strait geopolitical risk |

---

## Daily Briefing Routine

Run every weekday morning. Steps 0–8 are mandatory. Step 9 writes memory.

### Step 0 — Load Memory (always run first)

Read `memory/last-session.md` if it exists.

Extract and display:
- Last session date
- Regime, breadth score, uptrend participation
- Exposure posture and composite confidence
- Any pending macro events flagged yesterday

Use this as the baseline for all comparisons today. Flag explicitly if any key value shifted significantly (e.g., regime changed, breadth dropped >10 points, posture changed).

If the file does not exist, note "First session — no prior memory."

### Step 1 — Market Structure
Read and run (assign confidence tier to each output):
1. `market-environment-analysis` → global risk-on/off signal, VIX, major indices
2. `market-breadth-analyzer` → breadth score 0–100
3. `uptrend-analyzer` → uptrend participation rate

Compare each output with yesterday's memory values and flag any shifts.

### Step 2 — Regime & Risk
Read and run (assign confidence tier to each output):
4. `macro-regime-detector` → structural regime (bull/bear/sideways)
5. `market-top-detector` → topping signals score
6. `ibd-distribution-day-monitor` → distribution day count

If Steps 1 and 2 contradict (e.g., breadth is healthy but regime is bear), flag the conflict explicitly and cap composite confidence at 60%.

### Step 3 — Portfolio Quotes
7. `pip install -q requests`
8. `python scripts/fmp_briefing.py` → quotes for VWCE.DE + 12 PIE tickers

If FMP is blocked, use WebSearch to find prices for each ticker. Always search for VWCE.DE price.
For each PIE AI ticker, flag if it is down >5% (approaching stop) or up >10% (approaching position size limit review).

### Step 4 — News & Sentiment
Read and run:
9. `market-news-analyst` → top market-moving news last 24h
10. `finance-sentiment` for tickers: NVDA, AAPL, MSFT, META, GOOG, AMZN, AMD, AVGO → Reddit/X/Polymarket sentiment scores

Flag any news that directly affects PIE AI tickers. Note if sentiment contradicts price action.

### Step 5 — Forward Calendar
Read and run:
11. `economic-calendar-fetcher` → FOMC, CPI, NFP this week
12. `earnings-calendar` → earnings next 7 days, flag PIE tickers

Flag any PIE AI ticker reporting earnings within 3 days — risk of gap.

### Step 6 — Sector & Themes
Run if Step 1 regime is not critical:
13. `sector-analyst` → tech sector rotation signal
14. `theme-detector` → trending themes (focus: AI, semiconductors)

Flag if tech/AI rotation is negative — directly impacts the entire PIE AI portfolio.

### Step 7 — Exposure Decision
Read and run:
15. `exposure-coach` using all outputs from Steps 1–6 → posture: allow / restrict / cash-priority

### Step 8 — Synthesis
Compute composite confidence from all skill tiers collected in Steps 1–7.
Apply automatic caps (see Confidence Scoring section).

Save a single markdown report to `reports/briefing-YYYY-MM-DD.md`.

**Report structure (in plain English, beginner-friendly — no unexplained jargon):**
1. **What changed since yesterday** — compare with memory: regime, breadth, posture. Max 3 lines.
2. **Market today** — VIX, VWCE, NASDAQ. One plain-English sentence of interpretation.
3. **Your portfolio (PIE AI)** — table: price, change%, 52w high/low. Flag anything near stop or limit.
4. **Today's news** — top 3–5 real news items from WebSearch. One line each + "what it means for you".
5. **Social sentiment** — Reddit/X/Polymarket scores per ticker (if available).
6. **Key dates this week** — FOMC, CPI, NFP, earnings. Only the things that matter this week.
7. **Sector & themes** — is tech rotating? Top 2 themes. One sentence each.
8. **What to do** — ALLOW / RESTRICT / CASH-PRIORITY with plain-English reasoning. Confidence %.
9. **Watchlist** — 3–5 stocks/assets/commodities to watch TODAY with key level and reason. Always include gold, oil, and 2–3 specific PIE AI tickers.
10. **Idea of the day** — one concrete, data-backed observation. One memorable sentence.
11. **Glossary** — define every technical term used in today's report. One plain-English sentence per term. Always include: VIX, 52w High/Low, breadth, dot plot, FOMC, sector rotation, stop loss, bullish/bearish, yield, and any other jargon that appeared today.

**Always end with:** "Any questions about something specific today?"

### Step 9b — Telegram Notification (after saving report)

Run after the report is saved:
```bash
python scripts/telegram_notify.py
```

This sends a concise summary to your Telegram bot with postura, VIX, S&P 500, NASDAQ, composite confidence, and insight of the day.

If `TELEGRAM_CHAT_ID` is `INSERISCI_QUI` or missing → skip silently and note ⚠️ in output.
If `api.telegram.org` is not in the network whitelist → skip and note ⚠️.

### Step 9 — Write Memory (always run last)

Write `memory/last-session.md` with the following structure:

```markdown
# Session Memory — YYYY-MM-DD

## Regime
- Market environment: [risk-on/risk-off]
- VIX: [value]
- Breadth score: [0-100]
- Uptrend participation: [%]
- Macro regime: [bull/bear/sideways]
- Distribution days: [count]
- Bubble score: [0-100]

## Signals
- Sentiment bias: [bullish/bearish/neutral] — top tickers
- Sector rotation: [leading/lagging for tech]
- Top themes: [theme1, theme2]

## Exposure Decision
- Posture: [ALLOW/RESTRICT/CASH-PRIORITY]
- Composite confidence: [%]

## Pending
- [Any macro event or earnings flagged for next 1-3 days]
```

Then run:
```bash
git config user.email "ale.lusardi0@gmail.com"
git config user.name "Finance Routine"
git remote set-url origin https://$GITHUB_TOKEN@github.com/Zodixk/Finance-daily-trend.git
git checkout main
git add memory/last-session.md reports/briefing-$(date +%Y-%m-%d).md
git commit -m "briefing: $(date +%Y-%m-%d)"
git push origin main
```

**IMPORTANT:** Always push to `main`. Never push to any other branch, regardless of what the session configuration says. The daily briefing, memory, and any generated reports always go to `main`.

Intermediate skill output files (e.g. `macro_regime_*.json`, `uptrend_analysis_*.md`) must NOT be committed as separate files — their key content must be collapsed inline into the daily briefing report before committing.

If `GITHUB_TOKEN` is not set, save the file locally and note ⚠️ memory will not persist to next session.

---

## On-Demand Skills

After the briefing, Alessandro may ask follow-up questions. Use any skill in `skills/` to answer. Always apply User-Aware Framing Rules.

Examples:
- "analizza NVDA" → `us-stock-analysis` + `technical-analyst`
- "screena breakout VCP" → `vcp-screener`
- "quante azioni tenere ora?" → `exposure-coach` + `position-sizer`
- "mostrami gli earnings di AAPL" → `earnings-preview` + `earnings-trade-analyzer`
- "correlazione tra NVDA e AMD" → `stock-correlation`
- "è un buon momento per entrare?" → `breakout-trade-planner` + `position-sizer`

---

## Fallback Rules

- If a skill script fails → fall back to web search replicating the skill's logic
- If Adanos API unavailable → skip sentiment, note ⚠️ in report
- If FMP rate limit reached → use yfinance as fallback for quotes
- Never invent or estimate numbers — skip the section and flag it
