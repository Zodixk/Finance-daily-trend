# Personal Glossary — Alessandro

Every term includes: technical definition → plain English explanation → practical example → why it matters to you.
Updated progressively session by session.

---

## MARKET & SENTIMENT

---

### VIX
**Technical definition:** Volatility index calculated by the Chicago Board Options Exchange (CBOE) from S&P 500 options expiring in 30 days. It measures how much the market expects prices to fluctuate over the next month.

**Plain English:** The market's "fear thermometer." When investors are nervous and buy protection (put options), VIX rises. When they're calm, it falls.

**Reference levels:**
- VIX < 15 → very calm market, euphoria
- VIX 15–20 → normal
- VIX 20–30 → growing uncertainty
- VIX > 30 → widespread fear
- VIX > 40 → panic (happened during COVID-2020, 2008 crisis)

**Practical example:** On June 16, 2026 VIX was 16.23 — calm market. But VIX9D (9-day version) was 22.14 — traders were buying protection specifically for the June 17 FOMC meeting. The market was calm in general but nervous about that specific event.

**Why it matters to you:** VIX > 25 for 2+ weeks → the briefing will say CASH-PRIORITY. VIX > 40 → opportunity to buy PIE AI at lows, but only when VIX starts declining.

---

### VIX9D
**Technical definition:** A variant of the VIX that measures implied volatility over the next 9 days instead of the standard 30.

**Plain English:** A zoom into the short term. If VIX9D is much higher than the regular VIX, the market fears a specific imminent event (FOMC, CPI data, major earnings), not the future in general.

**Practical example:** June 17, 2026: VIX30D = 20.25, VIX9D = 22.14. The gap (+1.89 points) signaled that traders were buying protection specifically for Warsh's press conference that evening.

**Why it matters to you:** When VIX9D > VIX30D by 2+ points ahead of a macro event (FOMC, CPI), wait for the event before making moves on the PIE AI.

---

### Bullish / Bearish
**Technical definition:** Terms describing the expected direction of a market or a stock. They derive from how a bull attacks (upward from below) and a bear attacks (downward from above).

**Plain English:**
- **Bullish** = optimistic, expecting prices to rise
- **Bearish** = pessimistic, expecting prices to fall

**Practical example:** On Reddit, GOOG had 38% bullish comments vs 19% bearish on June 17 — the community was optimistic on Alphabet. AMD instead had rising buzz but the stock was falling: the market was bearish, Reddit bullish — a conflicting signal.

**Why it matters to you:** The briefing gives you bullish/bearish sentiment for every PIE AI ticker. When price and sentiment move in opposite directions, it's a signal to watch closely.

---

### Breadth (Market Breadth)
**Technical definition:** A measure of market participation: how many stocks are advancing vs declining over a given period.

**Plain English:** Imagine a concert — breadth tells you whether everyone is dancing or just the people in the front row. A "narrow" rally (only 5 mega-caps rising while everything else falls) is fragile. A "broad" rally (most stocks rising) is healthy and lasting.

**How it's measured:** The briefing uses Monty's Uptrend Ratio: percentage of ~2,800 tracked stocks currently in an uptrend.
- < 9.7% → oversold market (possible bounce)
- 9.7–37% → normal zone
- > 37% → overbought market (possible pullback)

**Practical example:** On June 16, 2026, only 28.6% of 2,800 stocks were in an uptrend — low in absolute terms, but improving (10 days earlier it was 23.8%). The market was gaining breadth, not losing it.

**Why it matters to you:** If NVDA and GOOG are rising but breadth is low, your PIE AI is fragile — a few stocks are holding everything up. When breadth rises, the rally becomes more solid.

---

### Sentiment
**Technical definition:** A qualitative and quantitative measure of investors' collective mood toward an asset, obtained by analyzing social media, surveys, options flow, and capital flows.

**Plain English:** It's "what people think" about a stock right now. Measured on Reddit, X (Twitter), Polymarket, news articles, etc.

**Practical example:** AMD on June 17 had rising buzz on Reddit (74/100, trend rising) despite falling 7.3%. This is the classic "buy the dip" social behavior — people want to buy the pullback. It's not always right to follow sentiment: in that case ARK and the CEO had already sold $130M of AMD.

**Why it matters to you:** The briefing uses the Adanos API to give you sentiment for NVDA, AAPL, MSFT, META, GOOG, AMZN, AMD, AVGO every morning. Use it as a complementary signal, never a primary one.

---

### Buzz Score
**Technical definition:** A 0–100 score that quantifies the volume of mentions and discussions about a stock on a specific platform (Reddit, X, etc.) over a given period (default: 7 days).

**Plain English:** How much a stock is being talked about online. 100 = everyone's talking about it, 0 = nobody is. High buzz can mean genuine interest or pure speculative noise.

**Important:** High buzz ≠ good investment. GameStop in 2021 had extremely high Reddit buzz and then crashed 80%.

**Practical example:** On June 17, MSFT had buzz 82.1/100 and AVGO 72.8/100. AVGO was the least discussed in the PIE AI — consistent with it being the weakest performer after the June earnings miss.

**Why it matters to you:** Useful for understanding which PIE AI tickers are "in the spotlight." If a ticker has falling buzz and falling price, that's a double negative signal.

---

## CENTRAL BANKS & MONETARY POLICY

> The entries FOMC, Fed Funds Rate, Dot Plot, Fed Pivot, and CME FedWatch are specific to the **Federal Reserve** (US central bank). **Hawkish/Dovish** apply to **any central bank** (ECB, Bank of Japan, Bank of England, etc.).

---

### Hawkish / Dovish
**Technical definition:** Adjectives describing the stance of **any central bank** — not just the Fed — toward monetary policy. Used for the Federal Reserve (USA), the ECB (Europe), the Bank of Japan, the Bank of England, and any institution that controls interest rates.

**Plain English:**
- **Hawkish** (hawk): priority is fighting inflation → raises rates or keeps them high for longer. Bad for stocks, good for bonds.
- **Dovish** (dove): priority is stimulating growth → cuts rates or keeps them low. Good for stocks, less so for bonds.

**Practical examples:**
- **Fed (USA):** Kevin Warsh (president since May 2026) is hawkish — the market priced in fewer rate cuts compared to his predecessor Powell.
- **ECB (Europe):** Christine Lagarde was hawkish in 2022–2023 to fight European inflation, then turned more dovish in 2024–2025 when she started cutting rates.
- **Bank of Japan:** For 30 years it was ultra-dovish (negative rates). The shift to positive rates in 2024 was a significant hawkish change that shook global markets.

**Why it matters to you:** A hawkish central banker (anywhere) puts pressure on growth stocks in the PIE AI. A hawkish ECB weighs on ASML (sells in Europe). A hawkish Fed weighs on the entire PIE AI. A shift toward dovish = potential rally, especially for NVDA, AMD, ASML.

---

### FOMC
**Technical definition:** Federal Open Market Committee — the committee of the Federal Reserve (US central bank) composed of 12 voting members (7 governors + 5 rotating regional bank presidents) that decides US monetary policy, primarily the Federal Funds rate.

**Plain English:** The most powerful group for global financial markets. It meets 8 times a year and decides whether to raise, cut, or hold US interest rates. Their decision affects everything: mortgages, corporate loans, stock valuations, currency exchange rates.

**Practical example:** June 17, 2026 was Kevin Warsh's first FOMC as new Fed Chair. The decision (hold at 3.50–3.75%) was already priced in at 99%. The real unknown was the tone of the 2:30 PM ET press conference.

**Why it matters to you:** FOMC decisions can move markets 3–5% in a single day. FOMC day is always RESTRICT by default in your briefing — don't make moves before the press conference.

---

### Fed Funds Rate (Interest Rates)
**Technical definition:** The rate at which banks lend money to each other overnight, set by the Fed as its primary monetary policy tool.

**Plain English:** The "cost of money" in the American economy. When the Fed raises rates, borrowing becomes more expensive — for families (mortgages), for companies (financing growth), for everyone. When it cuts, money becomes cheaper and the economy accelerates.

**Practical examples:**
- Rate at 0% (2020–2022): very cheap to borrow → tech companies grew with leverage → NVDA, AMD exploded
- Rate at 5.25% (2023–2024): high cost → tech companies slow down → P/E multiple compression
- Rate at 3.50–3.75% (June 2026): still elevated but declining → market in transition

**Why it matters to you:** High rates penalize high-growth, high-P/E companies like those in your PIE AI (NVDA P/E >40x, AMD P/E >60x). When rates fall, these companies get repriced upward first.

---

### Dot Plot
**Technical definition:** A chart published by the Fed 4 times a year (Summary of Economic Projections) where each FOMC member anonymously indicates where they expect the Fed Funds rate to be at year-end, year+1, year+2, and in the long run.

**Plain English:** It's like asking all 19 Fed members "where do you think rates will be in 1 year?" and putting their votes on a chart. Each dot is a vote. The median of the dots is the official forecast.

**Practical example:** In March 2026 the dot plot still showed 1 cut expected by end of 2026. In June 2026, the market expected the new dot plot to remove that last cut — meaning the Fed was saying "we're not cutting this year." This was a hawkish signal and weighed on high-P/E tech stocks.

**Why it matters to you:** Every time a dot plot is released, the market reacts. If dots move up (more hikes) → bad for PIE AI. If they move down (cuts coming) → good for PIE AI. It comes out 4 times a year: March, June, September, December.

---

### Fed Pivot
**Technical definition:** The moment when the Federal Reserve changes direction in monetary policy — typically from a hiking cycle (tightening) to a cutting cycle (easing).

**Plain English:** The Fed's "turning point." Historically, markets anticipate the pivot 6–12 months before it actually happens, because they start discounting lower rates in the future.

**Practical example:** After the aggressive hikes of 2022–2023, the Fed started cutting in late 2024. Markets had already started rising in the second half of 2023, anticipating the pivot. Those who bought NVDA or AMD during the 2022–2023 downturn saw enormous gains afterward.

**Why it matters to you:** The window between the last hike and the first cut is historically one of the best times to build positions in growth stocks like those in your PIE AI. The Pattern Playbook (Section 7.2 of your profile) describes exactly this strategy.

---

### CME FedWatch
**Technical definition:** A tool from the Chicago Mercantile Exchange that calculates the implied probability of Fed Funds rate changes at each FOMC meeting, derived from the prices of Federal Funds futures contracts.

**Plain English:** It's like a real-time poll on what the market expects from the Fed — but instead of asking people, it looks at futures contracts where traders put real money. It's more accurate than surveys because being wrong costs money.

**Practical example:** On June 17, 2026, CME FedWatch showed: 99% probability of hold, 1% probability of a cut. It also showed 70% probability of at least one rate hike by end of 2026 — signaling the market expected Warsh to raise rates before cutting them.

**Why it matters to you:** It's the primary reference for understanding what the market is "pricing in" before each FOMC. If the market prices a hold (99%) and a surprise cut arrives → rally. If it prices cuts and a hold arrives → sell-off.

---

## TECHNICAL ANALYSIS

---

### 52 Week High / 52 Week Low (52w High / 52w Low)
**Technical definition:** The highest and lowest price recorded by a stock over the past 52 weeks (one calendar year) of trading.

**Plain English:** The "range" of the past year. Knowing where the current price sits relative to this range tells you a lot: near the high = strong momentum but risk of "selling at the top"; near the low = weakness, but possible bounce if fundamentals hold.

**Practical example:** On June 17, 2026:
- AMD: price $507, 52w high $558 → at 91% of its annual high. High, but had just lost 7.3% from the peak.
- MSFT: price $393, 52w high $555 → only at 71% of its high. Much further from highs — more upside potential but also more recent weakness.

**Briefing rule:** When a ticker is near its 52w high, the briefing always looks for the exact date that high was set and whether it coincides with the ATH (All-Time High).

**Why it matters to you:** Buying near the 52w high is fine if the stock is breaking out to the upside. Buying near the 52w low is risky unless there's a clear reason for a bounce.

---

### ATH (All-Time High)
**Technical definition:** The highest price ever reached by a stock since the beginning of its stock market listing.

**Plain English:** The absolute record. Different from the 52w high — the ATH is the all-time maximum, the 52w high is the maximum of the past year. A stock can have a 52w high of $200 but an ATH of $400 (if it crashed 2 years ago).

**Practical example:** NVDA hit its ATH above $140 (adjusted for splits) in June 2024. AMD had its 52w high at $558 in June 2026, but its ATH was higher — so $558 was NOT an absolute record.

**Why it matters to you:** A stock breaking its ATH has no technical resistance above it — theoretically it can rise without historical limits. It's a very bullish signal when accompanied by solid fundamentals.

---

### Stop Loss
**Technical definition:** A conditional order that automatically sells a stock when it reaches a predefined price below the purchase price, limiting the maximum loss on that position.

**Plain English:** Your "emergency exit plan." Before buying, you decide: "If this stock falls X%, I exit automatically." It protects capital from catastrophic losses.

**Practical example:** You have AMD at $547. Your stop loss is 7–8%. So:
- Stop at 7%: $547 × (1 - 0.07) = **$509** → automatic sell
- Stop at 8%: $547 × (1 - 0.08) = **$503** → automatic sell

On June 17, 2026, AMD was at $507 — exactly in the stop zone. That's why the briefing flagged 🔴 NEAR STOP.

**Why it matters to you:** Your personal limit is 7–8% per position. The PIE AI manages weights automatically, so you can't set a direct stop loss on AMD inside the PIE — you have to monitor manually and decide whether to reduce the PIE or add more funds.

---

### Support and Resistance
**Technical definition:** Historical price levels where a stock has repeatedly found buyers (support = floor) or sellers (resistance = ceiling).

**Plain English:**
- **Support**: price where the stock has stopped falling in the past and bounced. Buyers step in at that level.
- **Resistance**: price where the stock struggles to rise above. Sellers step in at that level.

**Practical example:** AMD had key support around $490–500: it was an area where it had consolidated for weeks before the rally to $558. If it breaks $490, the next support was further down, around $450.

**Key rule:** When a support is broken it becomes resistance (and vice versa). It's one of the most important principles in technical analysis.

**Why it matters to you:** The briefing gives you key support/resistance levels for PIE AI tickers in the "Watchlist" section. These are the prices to watch when deciding whether to add to or reduce positions.

---

### P/E Ratio (Price-to-Earnings)
**Technical definition:** The ratio between a stock's current price and its earnings per share (EPS) over the past 12 months (trailing P/E) or the next 12 estimated months (forward P/E).

**Plain English:** It tells you how much you're paying for every dollar of profit the company generates. P/E 20x = you pay $20 for $1 of annual earnings. P/E 100x = you pay $100 for $1 of earnings — you believe very strongly in future growth.

**Practical examples:**
- AMD in June 2026: trailing P/E >100x, forward P/E >60x. The market expected enormous future earnings growth. When ARK and Lisa Su sold, the market said "maybe 100x is too much" and the stock lost 7.3% in one day.
- A bank like JPMorgan: P/E ~12x. Low — mature company, limited growth, but stable.

**Why it matters to you:** Your entire PIE AI has high P/E ratios (growth stocks). In a high-rate environment, high P/E stocks get penalized more — because future profits are worth less today when discounted at a high rate. When rates fall, P/E can expand → stocks rise.

---

### VCP (Volatility Contraction Pattern)
**Technical definition:** A technical pattern developed by Mark Minervini: a series of consolidations (stalls) with progressively narrowing price range and declining volume, culminating in a breakout on elevated volume.

**Plain English:** The stock "compresses like a spring" — price swings become smaller and smaller, volume dries up. Then, when the right catalyst or moment arrives, it explodes upward on high volume. It's one of the most reliable patterns for growth stocks.

**How to recognize it:**
1. The stock makes a high, then corrects (e.g., -20%)
2. Then bounces but doesn't return to the high (e.g., +15%)
3. Then corrects again but less (e.g., -10%)
4. Another smaller bounce, smaller correction...
5. The range narrows more and more (from -20% to -5%)
6. Volume declines during corrections
7. Breakout on volume 3x the average → entry signal

**Why it matters to you:** The briefing uses `vcp-screener` to find stocks in the VCP phase. When one of your PIE AI tickers is forming a VCP, it's a potential accumulation point before the next rally.

---

### Breakout
**Technical definition:** A price move above a key resistance level (or below support, in the case of a breakdown), generally accompanied by increased trading volume.

**Plain English:** When a stock "punches through" a ceiling that was blocking it. Like a boxer finally beating the opponent. To be valid, it must happen on high volume (at least 50% above average) — otherwise it's a "false breakout" and the stock falls back.

**Practical example:** TSM had its 52w high at $450. If the stock surpasses $450 with high volume, that's a breakout — a bullish signal that could anticipate a further rally toward $470–480.

**Alessandro's rule:** Never enter on a false breakout. The price must close above the pivot level, not just touch it intraday.

**Why it matters to you:** The Pattern Playbook describes breakout entries for VCP, Cup & Handle, and Flat Base. It's the main strategy for adding to your PIE AI positions at the right moment.

---

### PEAD (Post-Earnings Announcement Drift)
**Technical definition:** An academically documented phenomenon (Ball & Brown, 1968) where stocks that beat analyst estimates tend to continue rising for 30–60 days after earnings, while those that disappoint continue to fall.

**Plain English:** When a company publishes better-than-expected results, the market doesn't fully incorporate the information immediately — it takes weeks. You can take advantage of this "delay" by buying in the 1–3 days after an earnings beat and holding for 1–2 months.

**Practical example:** If NVDA beats estimates on July 28 and rises 5% the next day, PEAD suggests it may continue rising in the following weeks. The ideal entry is the first pullback day after the gap up — not the day itself (too emotional).

**Why it matters to you:** NVDA, META, MSFT are the best PEAD candidates in your PIE AI due to high institutional ownership. After July earnings, watch these three for accumulation opportunities.

---

## MACRO & ECONOMICS

---

### CPI (Consumer Price Index)
**Technical definition:** A statistical index that measures the average change over time in prices paid by urban consumers for a fixed basket of goods and services (food, energy, rent, medical services, transportation, etc.).

**Plain English:** The main inflation thermometer. If CPI rises 4.2% in a year, it means everything costs on average 4.2% more than a year ago. The Fed wants to keep it around 2%.

**Practical example:** In June 2026 US CPI was at 4.2% — more than double the Fed's 2% target. This is the main reason Warsh couldn't cut rates: cutting with inflation at 4.2% would risk pushing prices even higher.

**Why it matters to you:** High CPI → hawkish Fed → high rates → pressure on PIE AI. CPI declining toward 2% → dovish Fed → rate cuts coming → PIE AI rally. It's released once a month, always a market mover.

---

### Inflation
**Technical definition:** A generalized and sustained increase in the price level of goods and services in an economy over time, which reduces the purchasing power of money.

**Plain English:** Money is worth less over time. €100 today buys fewer things than €100 ten years ago. A little inflation (2%) is healthy — it means the economy is growing. Too much inflation (>4%) is a problem because it erodes savings and forces the Fed to raise rates.

**Why rate cuts cause it to rise:** Lower rates → cheaper credit → families and companies spend more → demand exceeds supply → prices rise. It's an intentional side effect of rate cuts, but if inflation is already high, you risk making the problem worse.

**Why it matters to you:** High inflation = high rates = bad for PIE AI (see P/E Ratio). Low inflation = Fed can cut = good for PIE AI.

---

### Yield (Bond Yield)
**Technical definition:** The annual rate of return on a bond, expressed as a percentage of its current price. Inversely correlated with bond price: if the price falls, the yield rises, and vice versa.

**Plain English:** How much a bond pays you each year. The US 10-year Treasury yield (10Y yield) is the global benchmark. If it yields 4.5%, it means you lend money to the US government for 10 years and they pay you 4.5% per year.

**The relationship with stocks:** If the 10Y yield rises to 5%, many investors prefer bonds (safe 5% return) over stocks (risky). This shifts capital from stocks to bonds → stocks fall.

**Practical example:** In June 2026 the 10Y yield was at 4.28%. Not extremely high, but enough to create pressure on high P/E stocks in the PIE AI.

**Why it matters to you:** When the 10Y yield rises → watch the PIE AI, especially ASML and NVDA (high P/E). When it falls → tailwind for growth stocks.

---

### Yield Curve
**Technical definition:** A graphical representation of the yields of bonds from the same issuer (typically the US government) at different maturities (from 3 months to 30 years).

**Plain English:** In normal conditions, lending money for longer should be paid more (more risk = more return). So normally: 10Y yield > 2Y yield. When it inverts (2Y > 10Y), it's a historical signal of a coming recession.

**The three shapes:**
- **Normal** (10Y > 2Y): healthy economy, growth expected
- **Flat** (10Y ≈ 2Y): uncertainty, transition
- **Inverted** (2Y > 10Y): recession signal (has occurred before every US recession in the past 50 years)

**Practical example:** In June 2026 the curve was "bear steepening": the 10Y was rising faster than the 2Y. Not an inversion, but a transition signal — the market is pricing persistent inflation in the long term.

**Why it matters to you:** Inverted curve for 2+ months → reduce AMD and QCOM (more cyclical), increase cash. The briefing monitors the 10Y-2Y spread every day.

---

### Bear Steepening
**Technical definition:** A movement in the yield curve where long-term rates (10Y, 30Y) rise faster than short-term rates (2Y), widening the spread, but in a context where both rates are rising.

**Plain English:** The curve becomes steeper, but in the "wrong way" — not because the economy is healthy (bull steepening) but because markets expect persistent long-term inflation. Buyers of 10-year bonds want to be compensated more for the risk of future inflation.

**Why it's negative for growth stocks:** Companies like those in the PIE AI derive most of their value from profits they'll make over the next 5–10 years. If long-term rates rise, those future profits are "worth less" today (the discount rate increases → present value falls).

**Why it matters to you:** The macro regime detector was monitoring this signal in June 2026 as a risk factor for the PIE AI.

---

### DXY (Dollar Index)
**Technical definition:** An index that measures the value of the US dollar against a basket of 6 major currencies (EUR 57.6%, JPY 13.6%, GBP 11.9%, CAD 9.1%, SEK 4.2%, CHF 3.6%).

**Plain English:** Measures how much the dollar is "worth" relative to other major currencies. High DXY = strong dollar. Low DXY = weak dollar.

**The effect on PIE AI:**
- **ASML** earns in euros but is quoted in dollars → a strong dollar hurts it (European profits worth less in USD)
- **TSM** earns in Taiwanese dollars/USD but has costs in TWD → mixed impact
- **NVDA, AMD, MSFT**: most revenues in USD, less vulnerable to DXY

**Why it matters to you:** If DXY rises above 105 → watch ASML and TSM in the PIE. The briefing monitors DXY as part of macro analysis.

---

## SECTORS & ROTATION

---

### Sector Rotation
**Technical definition:** A systematic movement of capital from one sector of the economy to another, driven by the economic cycle, monetary policies, or specific events.

**Plain English:** Institutional investors (funds, banks, insurance companies) continuously move money between sectors. When tech is "in favor" (risk-on, low rates, growth), capital flows toward NVDA, AMD, MSFT. When the market turns defensive (high rates, recession), capital goes toward Utilities, Healthcare, Consumer Staples.

**The classic cycle:**
1. **Early cycle** (recovery): Financials, Industrials
2. **Mid cycle** (expansion): Tech, Consumer Cyclical
3. **Late cycle** (slowdown): Energy, Materials
4. **Recession**: Utilities, Healthcare, Consumer Staples

**Practical example:** June 16, 2026: XLK (tech) -2.79%, Dow Jones +0.64%, JPMorgan +3.7%. Capital was leaving tech and entering financials — a classic late-cycle rotation.

**Why it matters to you:** 100% of the PIE AI is in tech/semiconductors. A sector rotation against tech hits YOUR ENTIRE PORTFOLIO simultaneously. The briefing monitors XLK every day for this reason.

---

### XLK
**Technical definition:** SPDR Technology Select Sector ETF — a passive replicator of the technology sector within the S&P 500. Contains mainly Apple, NVDA, Microsoft, Broadcom, etc.

**Plain English:** The "US tech sector ETF." If XLK rises, your PIE AI is probably rising. If XLK falls, your PIE AI is probably falling. It's the direct thermometer of your sector.

**Why it matters to you:** The briefing compares XLK against other sectors every day to understand whether tech is in favor or not. XLK -3% while the Dow is flat = rotation against you.

---

### Broadening Regime
**Technical definition:** A market phase in which gains expand from a narrow group of mega-caps (concentration) to broader participation that includes mid-caps, small-caps, and value/cyclical stocks.

**Plain English:** In a concentration regime, only the "Magnificent 7" (Apple, NVDA, Microsoft, etc.) rise while everything else is flat. In a broadening regime, growth widens — industrials, financials, small caps start rising too.

**Is it positive or negative?** For the economy it's positive (healthier, more distributed growth). For your PIE AI it can be temporarily negative because capital leaves mega-cap tech and moves toward more diversified sectors.

**Practical example:** In June 2026 the Macro Regime Detector was signaling Broadening with 70-90% probability of transition. 5 out of 6 components confirmed: small-cap IWM outperforming SPY, RSP/SPY rising, credit expanding.

**Why it matters to you:** In a broadening regime, consider whether it's worth adding a small-cap or value ETF to balance the PIE AI which is 100% large-cap tech.

---

## PORTFOLIO & RISK

---

### ALLOW / RESTRICT / CASH-PRIORITY
**Technical definition:** The operational posture framework of the daily briefing that synthesizes all market signals into an action recommendation.

**Plain English:**
- **ALLOW**: the market context supports new investments. You can add to the PIE AI or to VWCE with confidence.
- **RESTRICT**: caution. Don't sell what you have, but don't make major new purchases. Wait for clarity.
- **CASH-PRIORITY**: signals are negative. Reduce exposure, accumulate liquidity. It's not "sell everything" — it's "be careful and have cash ready for better opportunities."

**Practical example:** On June 17, 2026 the posture was RESTRICT pre-FOMC. The post-FOMC framework was clear: Warsh neutral/dovish → shift to ALLOW; Warsh hawkish → shift to CASH-PRIORITY.

**Why it matters to you:** It's the most practical recommendation of the briefing. As a beginner, following it prevents you from making emotional moves at the wrong time.

---

### Drawdown
**Technical definition:** Percentage loss from the most recent peak of a portfolio or stock's value. Calculated as: (Peak Value - Current Value) / Peak Value × 100.

**Plain English:** If your portfolio was worth €1,000 and is now worth €850, the drawdown is -15%. It's different from total return — it only measures the loss from the recent peak.

**Practical example:** If you bought AMD at $547 and it's now at $507, the drawdown on that position is -7.3%. Your personal limit is -15% on the total portfolio and -7-8% on each individual position.

**Why it matters to you:** Max drawdown of 15% on the total is your limit. If the PIE AI is worth €500 and drops to €425, you're at -15% — time to review exposure. For individual positions, the 7-8% stop loss prevents any one position from doing too much damage to the total.

---

### Exposure
**Technical definition:** The percentage of total capital invested in risky assets (stocks, equity ETFs) relative to cash held.

**Plain English:** If you have €1,000 and have invested €800 in stocks and hold €200 in cash, your exposure is 80%. High exposure = more gains if the market rises, more losses if it falls. Low exposure = more safety but less return.

**What the briefing suggests for each zone:**
- ALLOW → 90-100% invested
- RESTRICT → 70-80% invested
- CASH-PRIORITY → 50% or less invested

**Why it matters to you:** As a beginner building your portfolio, you don't need to think about reducing exposure yet — you're still adding. But it's important to understand the concept for when the market becomes more volatile.

---

### Insider Selling
**Technical definition:** Sale of shares by company executives (CEO, CFO, CTO) or major shareholders (>10%) who must publicly declare these transactions to the SEC (Securities and Exchange Commission) within 2 business days.

**Plain English:** When the CEO or a senior executive sells shares in their own company, they must announce it publicly. It's not always a negative signal (sometimes they sell to pay taxes or diversify), but when they sell large amounts near all-time highs, it's a reason for caution.

**Practical example:** On June 15, 2026, Lisa Su (AMD's CEO) sold 125,000 shares for $57.6 million while the stock was near its 52w high of $558. The same day ARK (Cathie Wood) sold 141,000 shares for $72.3 million. Two major sellers at the same time near the highs — a signal the stock was overvalued.

**Why it matters to you:** When the briefing flags insider selling on a PIE AI ticker, it's one more reason not to add to that position at that moment.

---

### Composite Confidence
**Technical definition:** An aggregated 0-92% score that synthesizes the reliability of the daily briefing, calculated as a weighted average of the confidence levels of each skill run (HIGH ≥75%, MEDIUM 50-74%, LOW <50%), with automatic caps for binary events or conflicting signals.

**Plain English:** A measure of how reliable the briefing itself is on a given day. If all tools work and signals are consistent → high confidence (~80-90%). If data is missing or signals contradict each other → low confidence (~50-60%).

**Automatic caps:**
- FOMC day → max 60% (too much uncertainty)
- VIX > 30 → max 70%
- Regime Steps 1+2 contradict each other → max 60%
- More than 2 skills fail → max 55%

**Practical example:** On June 17, 2026 confidence was 60% — capped by the FOMC. Meaning: "the data we have is good, but there's an unpredictable event today that makes any forecast unreliable."

**It never reaches 100%** by design — markets are inherently uncertain.

**Why it matters to you:** Use confidence as the "volume" of the recommendations. Confidence 85% + ALLOW = invest with confidence. Confidence 55% + RESTRICT = really wait.

---

## TOOLS & PLATFORMS

---

### Trader 212
**Technical definition:** An online broker regulated by FCA (UK) and CySEC (EU) that offers zero-commission trading of stocks, ETFs, and CFDs, available in Italy via the mobile app.

**Plain English:** Your broker — the platform where you buy and sell stocks and ETFs. It has a special feature called PIE that lets you create automatic portfolios with predefined weights.

**Why it matters to you:** All your positions are on Trader 212. The PIE AI weights are managed automatically by the platform according to the percentages you've set (NVDA 12%, others 8%).

---

### PIE (Trader 212)
**Technical definition:** A Trader 212 feature that allows creating a thematic portfolio with predefined percentage allocations. Funds added are automatically distributed among the stocks according to the set weights. Rebalancing happens automatically.

**Plain English:** It's an "automatic basket" of stocks. You say "I want 12% NVDA and 8% of everything else" and Trader 212 handles it every time you add money. You don't have to buy each stock manually.

**Important to understand:** When you add €100 to the PIE, it gets distributed across ALL 12 tickers according to the weights. You can't say "put these €100 only in GOOG."

**Why it matters to you:** Every time you want to add funds, the briefing tells you whether it's a good time based on market conditions. But the distribution is decided automatically by Trader 212.

---

### VWCE.DE
**Technical definition:** Vanguard FTSE All-World UCITS ETF Accumulating, listed on the German XETRA exchange with ticker VWCE.DE. It replicates the FTSE All-World index covering ~4,000 stocks from developed and emerging market countries.

**Plain English:** Your long-term "safe investment." Instead of betting on individual companies, you buy a piece of almost every major company in the world in a single ticker.

**Key characteristics:**
- **Accumulating**: doesn't pay cash dividends — reinvests them automatically (great for taxes in Italy: taxed only when you sell)
- **Diversified**: ~60-65% USA, ~10% Europe, ~8% Japan, rest of the world
- **Low cost**: TER (annual cost) ~0.22% — almost free
- **Currency**: quoted in EUR, but holds stocks in all currencies

**FTSE All-World**: the index that VWCE replicates. "FTSE" stands for Financial Times Stock Exchange (the company that builds the index). "All-World" means global, developed + emerging markets.

**Why it matters to you:** It's your "anchor" — never sell it except in extreme macro events. While the PIE AI is your bet on tech growth, VWCE is your long-term global safety net.

---

### FMP (Financial Modeling Prep)
**Technical definition:** A financial API that provides real-time and historical data on stocks, ETFs, indices, earnings, company financials, and macroeconomic data.

**Plain English:** The "financial database" the briefing uses to get PIE AI prices every morning. Free plan: 250 calls per day, one ticker at a time.

**Why it matters to you:** If the briefing shows "FMP HTTP 402" for a ticker, it means that ticker requires a premium plan. In that case the briefing uses yfinance as a backup.

---

### Adanos Finance API
**Technical definition:** A sentiment analysis API that aggregates and quantifies discussions on Reddit, X (Twitter), news articles, and Polymarket for individual stock tickers, producing metrics like buzz_score, bullish_pct, trend.

**Plain English:** The tool the briefing uses to measure "what the internet thinks" about your stocks. It analyzes thousands of posts on Reddit and X every day and turns them into numbers (buzz 0-100, % bullish, % bearish, rising/falling trend).

**Why it matters to you:** Adanos sentiment is a complementary signal — not a primary one. Useful for understanding if there's "buy the dip" or "sell the rally" behavior happening on your PIE AI.

---

### Polymarket
**Technical definition:** A decentralized blockchain-based prediction market platform where users bet with cryptocurrency on future events (political, economic, sports). Probabilities reflect the aggregation of participants' expectations.

**Plain English:** A market where people bet real money on what will happen. If 99% of the money is bet on "the Fed won't cut in June," that's the best available collective estimate. It's more reliable than surveys because being wrong costs real money.

**Practical example:** On June 17, 2026: Polymarket showed 99% probability of a Fed hold. This was the strongest signal that the market had already "priced in" the hold — there would be no surprise, and the market movement depended only on Warsh's tone.

**Why it matters to you:** The briefing uses Polymarket probabilities to calibrate uncertainty around macro events (FOMC, CPI, elections). High probability = event already priced in = little surprise expected.

---

*Last updated: 2026-06-17*
*Next addition: add here the terms you want to learn in upcoming sessions.*
