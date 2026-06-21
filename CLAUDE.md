# Finance Daily Briefing — Alessandro's Portfolio

## ⚠️ LANGUAGE RULE

**Conversational responses:** mirror the user's language. If the user writes in Italian, reply in Italian. If in English, reply in English.

**Everything written to the repository must be in English.** This includes:
- Daily briefing reports (`reports/briefing-YYYY-MM-DD.md`)
- Memory files (`memory/last-session.md`, `memory/finance-profile.md`, `memory/glossary.md`)
- Commit messages
- Any other file committed to the repo

No exceptions for repo content.

## Portfolio

**Investor profile:** Growth investor, beginner, EUR-based, broker Trader 212.
**Risk:** max 7-8% stop loss, max 10% per position, max drawdown 15%.

**ETF Core:** VWCE (VWCE.DE su XETRA) — Vanguard FTSE All-World Accumulating. Long-term anchor — never recommend selling entirely.

**Individual positions:**
| Ticker | Entry | Stop | Size | Notes |
|--------|-------|------|------|-------|
| SEC0 | TBC | TBD (7-8% default) | €50 | iShares MSCI Global Semiconductors UCITS ETF USD (Acc). XETRA: SEC0.DE. ISIN IE000I8KRLL9. Order placed 2026-06-18. |

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
4. **Portfolio relevance:** when any signal fires, immediately flag which open positions are directly affected.
5. **Semiconductor bias:** SEC0 tracks global semiconductors (NVDA, TSMC, ASML and peers). Flag when semiconductor sector rotation is negative or when macro headwinds hit capex cycles.
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

All skills in `skills/` are local script-based skills — read their `SKILL.md` before executing.
Bigdata.com skills (marked `bigdata-com:`) are cloud plugin skills — invoke via the Skill tool (no local script).

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
| `earnings-preview` | Pre-earnings setup for a ticker (local fallback) |
| `earnings-recap` | Post-earnings analysis (local fallback) |
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

### Bigdata.com Research (Cloud Plugin)

These skills use [bigdata.com](https://bigdata.com) MCP data. They are **cloud plugin skills** — not local scripts. Invoke with the Skill tool (`bigdata-com:<name>`). All produce structured output with Bigdata.com attribution.

**Redundancy note:** `bigdata-com:earnings-preview` supersedes the local `earnings-preview` skill when bigdata MCP is available. Same for `bigdata-com:earnings-digest` vs `earnings-recap`. All other bigdata-com skills are complementary (different depth or angle) — not redundant.

#### Company analysis (public)
| Skill | Purpose |
|---|---|
| `bigdata-com:company-brief` | Structured company overview: business model, financials, estimates |
| `bigdata-com:quick-take` | Fast 2-min institutional opinion: thesis, risk, catalyst |
| `bigdata-com:investment-memo` | Full institutional memo: EPIC + FaVeS + scenarios + recommendation |
| `bigdata-com:valuation-snapshot` | Valuation multiples + DCF snapshot with MCP data |
| `bigdata-com:peer-comparables` | Valuation multiples vs peer group (EV/EBITDA, P/E, P/S) |
| `bigdata-com:risk-assessment` | Company risks: operational, financial, regulatory, ESG |
| `bigdata-com:scenario-analysis` | Bull/base/bear with probability-weighted expected value |
| `bigdata-com:moat-governance-review` | Competitive moat type/strength + ESG/governance quality |
| `bigdata-com:catalyst-monitor` | Upcoming catalysts: earnings, conferences, regulatory, product |
| `bigdata-com:variant-perception` | Where your thesis differs from consensus (EPIC + FaVeS) |
| `bigdata-com:earnings-quality-screen` | OCF/NI ratio, accruals, DSO, Beneish M-Score |

#### Earnings
| Skill | Purpose |
|---|---|
| `bigdata-com:earnings-preview` | Pre-earnings: consensus, EPIC table, FaVeS, scenarios ← **preferred over local** |
| `bigdata-com:earnings-digest` | Post-earnings: beat/miss, guidance, reaction ← **preferred over local** |
| `bigdata-com:earnings-reaction` | Post-earnings price reaction: gap, volume, momentum |

#### IPO analysis
| Skill | Purpose |
|---|---|
| `bigdata-com:pre-ipo-analysis` | S-1/F-1 analysis, upcoming listing, balanced bull/bear |
| `bigdata-com:post-ipo-day1` | Day-1 listing reaction note |
| `bigdata-com:post-ipo-day14` | NASDAQ-100 inclusion impact (14 days post-IPO) |
| `bigdata-com:post-ipo-day179` | 180-day lock-up expiry analysis |
| `bigdata-com:post-ipo-day365` | 366-day founder lock-up / float expansion |

#### Macro, sector & thematic
| Skill | Purpose |
|---|---|
| `bigdata-com:sector-analysis` | Deep sector analysis with MCP data |
| `bigdata-com:sector-playbook` | Sector investment playbook: themes, leaders, rotation triggers |
| `bigdata-com:thematic-research` | Thematic analysis with data + source attribution |
| `bigdata-com:cross-sector` | Cross-sector rotation analysis |
| `bigdata-com:country-analysis` | Country economic profile + investment implications |
| `bigdata-com:country-sector-analysis` | Country-specific sector analysis |
| `bigdata-com:regional-comparison` | Regional comparison (e.g. Europe vs Asia) |
| `bigdata-com:g7-comparison` | G7 economies comparison |

## Circuit Breakers

Check these conditions at the **start of every session**, before Step 0. If any fires, follow the protocol.

| CB | Condition | Protocol |
|---|---|---|
| **CB1 — Market Crisis** | VIX > 35 OR S&P 500 session down >3% | Skip Steps 4–7. Report only: cause, open positions most affected. Posture = CASH-PRIORITY automatically. |
| **CB2 — Insufficient Data** | More than 3 skills fail or return no data | Cap composite confidence at 45%. Note which skills failed. Continue with remaining data only. |

---

## Daily Briefing Routine

Run every weekday morning. Steps 0–8 are mandatory. Step 9 writes memory.

### Step 0 — Load Memory (always run first)

Read both `memory/finance-profile.md` and `memory/last-session.md` if they exist.

From `memory/finance-profile.md` extract: ETF core ticker, individual positions, risk limits, pattern playbook.
Note: core ETF is **VWCE.DE** (Vanguard FTSE All-World, tracks FTSE All-World index — switched from VUAA on 2026-06-15).

Extract and display:
- Last session date
- Regime, breadth score, uptrend participation
- Exposure posture and composite confidence
- Any pending macro events flagged yesterday

Use this as the baseline for all comparisons today. Flag explicitly if any key value shifted significantly.

If the file does not exist, note "First session — no prior memory."

### Step 1 — Market Structure
Read and run (assign confidence tier to each output):
1. `market-environment-analysis` → global risk-on/off signal, VIX, major indices
2. `market-breadth-analyzer` → breadth score 0–100
   Script: `PYTHONIOENCODING=utf-8 python skills/market-breadth-analyzer/scripts/market_breadth_analyzer.py --detail-url "https://tradermonty.github.io/market-breadth-analysis/market_breadth_data.csv" --summary-url "https://tradermonty.github.io/market-breadth-analysis/market_breadth_summary.csv" --output-dir reports/`
3. `uptrend-analyzer` → uptrend participation rate

Compare each output with yesterday's memory values and flag any shifts.

### Step 2 — Regime & Risk
Read and run (assign confidence tier to each output):
4. `macro-regime-detector` → structural regime (bull/bear/sideways)
   Script: `PYTHONIOENCODING=utf-8 python skills/macro-regime-detector/scripts/macro_regime_detector.py --api-key $FMP_API_KEY --output-dir reports/`
5. `market-top-detector` → topping signals score
6. `ibd-distribution-day-monitor` → distribution day count

If Steps 1 and 2 contradict, flag the conflict explicitly and cap composite confidence at 60%.

### Step 3 — Portfolio Quotes
7. `pip install -q -r requirements.txt`
8. `PYTHONIOENCODING=utf-8 python scripts/fmp_briefing.py` → quotes for VWCE.DE + SEC0.DE

If FMP is blocked, use WebSearch to find prices for each ticker. Always search for VWCE.DE price.
For each individual position, flag if it is down >5% (approaching stop) or up >10% (approaching position size limit review).

### Step 4 — News & Sentiment
Read and run:
9. `market-news-analyst` → top market-moving news last 24h
10. `finance-sentiment` for tickers: NVDA, AAPL, MSFT, META, GOOG, AMZN, AMD, AVGO → Reddit/X/Polymarket sentiment scores (market context)

Flag any news that directly affects the semiconductor sector (SEC0 top holdings: NVDA, TSMC, ASML, AVGO). Note if sentiment contradicts price action.

### Step 5 — Forward Calendar
Read and run:
11. `economic-calendar-fetcher` → FOMC, CPI, NFP this week
12. `earnings-calendar` → earnings next 7 days

Flag any major semiconductor company (NVDA, TSMC, ASML, AVGO) reporting earnings within 3 days — risk of gap in SEC0.

### Step 6 — Sector & Themes
Run if Step 1 regime is not critical:
13. `sector-analyst` → tech/semiconductor sector rotation signal
    Script: `PYTHONIOENCODING=utf-8 python skills/sector-analyst/scripts/analyze_sector_rotation.py --save --output-dir reports/`
14. `theme-detector` → trending themes (focus: AI, semiconductors)

Flag if semiconductor sector rotation is negative — directly impacts SEC0.

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
3. **Your portfolio** — SEC0.DE: price and change%. VWCE.DE: price and change%. Flag anything near stop.
4. **Today's news** — top 3–5 real news items from WebSearch. One line each + "what it means for you".
5. **Social sentiment** — Reddit/X/Polymarket scores for key semiconductor tickers (if available).
6. **Key dates this week** — FOMC, CPI, NFP, earnings. Only the things that matter this week.
7. **Sector & themes** — are semiconductors rotating? Top 2 themes. One sentence each.
8. **What to do** — ALLOW / RESTRICT / CASH-PRIORITY with plain-English reasoning. Confidence %.
9. **Idea of the day** — one concrete, data-backed observation. One memorable sentence.
10. **Glossary** — define every technical term used in today's report. One plain-English sentence per term.

**Always end with:** "Any questions about something specific today?"

### Step 9b — Telegram Notification (after saving report)

Run after the report is saved:
```bash
python scripts/telegram_notify.py
```

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
- Sector rotation: [leading/lagging for semiconductors]
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
git add memory/last-session.md "reports/briefing-$(date +%Y-%m-%d).md"
git commit -m "briefing: $(date +%Y-%m-%d)"
git push origin main
```

**⚠️ CRITICAL — git add rules:**
- ONLY ever stage the two files above: `memory/last-session.md` and `reports/briefing-YYYY-MM-DD.md`.
- NEVER use `git add -A`, `git add .`, or `git add reports/` — these would accidentally commit intermediate skill output files.
- Skill scripts (macro-regime-detector, uptrend-analyzer, exposure-coach, sector-analyst, market-breadth-analyzer) write temporary files to `reports/`. These are excluded by `.gitignore` and must NEVER be committed.
- If in doubt: run `git status` first and verify only the two intended files appear under "Changes to be committed".

**IMPORTANT:** Always push to `main`. Never push to any other branch.

Intermediate skill output files must NOT be committed as separate files — collapse them inline into the briefing report.

If `GITHUB_TOKEN` is not set, save the file locally and note ⚠️ memory will not persist to next session.

---

## On-Demand Skills

After the briefing, Alessandro may ask follow-up questions. Use any skill in `skills/` to answer. Always apply User-Aware Framing Rules.

**Local skills** — invoke by reading `skills/<name>/SKILL.md` and executing the defined script or steps.
**Bigdata.com skills** — invoke via the Skill tool with prefix `bigdata-com:`. Use bigdata-com variants as the **preferred** choice wherever both exist (earnings-preview, earnings-recap).

Examples:
- "analizza NVDA" → `us-stock-analysis` + `technical-analyst`
- "screena breakout VCP" → `vcp-screener`
- "quante azioni tenere ora?" → `exposure-coach` + `position-sizer`
- "mostrami gli earnings di AAPL" → `bigdata-com:earnings-preview` (preferred) or `earnings-preview` (fallback)
- "è un buon momento per entrare?" → `breakout-trade-planner` + `position-sizer`
- "brief su LRCX" → `bigdata-com:company-brief`
- "quanto vale NVDA?" → `bigdata-com:valuation-snapshot`
- "rischi su LRCX" → `bigdata-com:risk-assessment`
- "earnings LRCX ieri?" → `bigdata-com:earnings-digest` (preferred) or `earnings-recap` (fallback)
- "reaction al report NVDA" → `bigdata-com:earnings-reaction`
- "analisi settore semiconduttori" → `bigdata-com:sector-analysis`
- "investment memo ASML" → `bigdata-com:investment-memo`
- "IPO [company]" → `bigdata-com:pre-ipo-analysis`
- "cross-sector rotation" → `bigdata-com:cross-sector`
- "moat NVDA" → `bigdata-com:moat-governance-review`
- "catalysts LRCX" → `bigdata-com:catalyst-monitor`

---

## Fallback Rules

- If a skill script fails → fall back to web search replicating the skill's logic
- If Adanos API unavailable → skip sentiment, note ⚠️ in report
- If FMP rate limit reached → use yfinance as fallback for quotes
- If bigdata.com MCP unavailable → fall back to local equivalent skill (see redundancy notes above)
- Never invent or estimate numbers — skip the section and flag it
