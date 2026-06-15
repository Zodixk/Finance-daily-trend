# Finance Daily Briefing — Alessandro's Portfolio

## Portfolio

**ETF Core:** FTDL.DE — FTDL All-World Accumulating, listed on XETRA (German stock exchange)

**PIE AI on Trader 212:**
GOOG, AMZN, AVGO, NVDA, AMD, AAPL, ASML, CSCO, META, MSFT, QCOM, TSM

## Routine Instructions

Run the daily briefing with these exact steps:

1. Install dependency: `pip install -q requests`
2. Run the briefing script: `python scripts/fmp_briefing.py`
3. The script saves the report automatically to `reports/briefing-YYYY-MM-DD.md`
4. Print the report content to stdout

## Environment Variables

- `FMP_API_KEY` — Financial Modeling Prep API key (must be set in Routine env config)

## API Budget

~8 FMP API calls per run. Free tier allows 250/day — no risk of exceeding.

## Fallback Rules

- If any data section returns ⚠️ unavailable, skip it — do not retry or invent numbers
- FTDL.DE may not be available on FMP free tier; note it explicitly if missing
- If the script exits with an error, report the error and stop
