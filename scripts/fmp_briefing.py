#!/usr/bin/env python3
"""
Daily Finance Briefing — Alessandro's Portfolio
Financial Modeling Prep API | ~8 API calls per run
"""

import os
import sys
import time
import requests
from datetime import date, datetime, timedelta

FMP_API_KEY = os.getenv("FMP_API_KEY")
if not FMP_API_KEY:
    sys.exit("ERROR: FMP_API_KEY environment variable not set.")

BASE_V3 = "https://financialmodelingprep.com/api/v3"
BASE_STABLE = "https://financialmodelingprep.com/stable"

SESSION = requests.Session()

PIE = ["GOOG", "AMZN", "AVGO", "NVDA", "AMD", "AAPL", "ASML", "CSCO", "META", "MSFT", "QCOM", "TSM"]
ETF = "FTDL.DE"


def fmp(url, params=None):
    time.sleep(0.35)
    p = {"apikey": FMP_API_KEY, **(params or {})}
    try:
        r = SESSION.get(url, params=p, timeout=30)
        if r.status_code == 200:
            data = r.json()
            return data if data else None
        print(f"WARN: {url} → HTTP {r.status_code}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"WARN: {url} failed: {e}", file=sys.stderr)
        return None


def batch_quotes(tickers):
    results = {}
    for i in range(0, len(tickers), 5):
        batch = ",".join(tickers[i:i + 5])
        data = fmp(f"{BASE_V3}/quote/{batch}")
        if data:
            for q in data:
                results[q["symbol"]] = q
    return results


def index_quotes():
    data = fmp(f"{BASE_V3}/quote/%5EVIX,%5EGSPC,%5EIXIC")
    if not data:
        # fallback via proxies
        data = fmp(f"{BASE_V3}/quote/SPY,QQQ")
    results = {}
    if data:
        for q in data:
            results[q["symbol"]] = q
    return results


def recent_news(tickers, limit=15):
    symbols = ",".join(tickers)
    data = fmp(f"{BASE_V3}/stock_news", {"tickers": symbols, "limit": limit})
    return data or []


def earnings_calendar():
    today = date.today()
    week = today + timedelta(days=7)
    data = fmp(f"{BASE_V3}/earning_calendar", {
        "from": today.isoformat(),
        "to": week.isoformat(),
    })
    return data or []


def pct(val):
    if val is None:
        return "N/A"
    sign = "+" if val >= 0 else ""
    arrow = "▲" if val >= 0 else "▼"
    return f"{arrow} {sign}{val:.2f}%"


def price_str(val):
    if val is None:
        return "N/A"
    return f"{val:.2f}"


def main():
    today_str = date.today().strftime("%d %B %Y")
    today_file = date.today().isoformat()

    print("Fetching market data...", file=sys.stderr)

    pie_q = batch_quotes(PIE)                   # 3 API calls
    etf_data = fmp(f"{BASE_V3}/quote/{ETF}")    # 1 API call
    etf_q = etf_data[0] if etf_data else None
    idx_q = index_quotes()                       # 1 API call
    news = recent_news(PIE[:6]) + recent_news(PIE[6:])  # 2 API calls
    earnings = earnings_calendar()               # 1 API call
    # Total: ~8 calls

    lines = []
    lines.append(f"# Briefing del {today_str} — Buongiorno Alessandro\n")

    # ── Section 1: Market ──────────────────────────────────────────────────
    lines.append("## 1. Market Overview\n")

    vix = idx_q.get("^VIX")
    sp500 = idx_q.get("^GSPC") or idx_q.get("SPY")
    nasdaq = idx_q.get("^IXIC") or idx_q.get("QQQ")

    if vix:
        vix_val = vix.get("price", 0)
        regime = "risk-off (fear elevated)" if vix_val > 20 else "risk-on (calm)"
        lines.append(f"- **VIX:** {price_str(vix_val)} — {regime}")
    else:
        lines.append("- **VIX:** ⚠️ unavailable")

    if sp500:
        lines.append(f"- **S&P 500:** ${price_str(sp500.get('price'))} {pct(sp500.get('changesPercentage'))}")
    else:
        lines.append("- **S&P 500:** ⚠️ unavailable")

    if nasdaq:
        lines.append(f"- **NASDAQ:** ${price_str(nasdaq.get('price'))} {pct(nasdaq.get('changesPercentage'))}")
    else:
        lines.append("- **NASDAQ:** ⚠️ unavailable")

    if etf_q:
        lines.append(f"- **FTDL (ETF core):** €{price_str(etf_q.get('price'))} {pct(etf_q.get('changesPercentage'))}")
    else:
        lines.append("- **FTDL (ETF core):** ⚠️ unavailable — check XETRA manually")

    lines.append("")

    # ── Section 2: PIE AI Quotes ───────────────────────────────────────────
    lines.append("## 2. PIE AI — Quotes\n")
    lines.append("| Ticker | Price | Change % | 52w High | 52w Low |")
    lines.append("|--------|-------|----------|----------|---------|")

    for ticker in PIE:
        q = pie_q.get(ticker)
        if q:
            p = price_str(q.get("price"))
            chg = pct(q.get("changesPercentage"))
            hi = price_str(q.get("yearHigh"))
            lo = price_str(q.get("yearLow"))
            lines.append(f"| **{ticker}** | ${p} | {chg} | ${hi} | ${lo} |")
        else:
            lines.append(f"| **{ticker}** | ⚠️ N/A | — | — | — |")

    lines.append("")

    # ── Section 3: News ────────────────────────────────────────────────────
    lines.append("## 3. Morning News (last 24h)\n")

    cutoff = datetime.utcnow() - timedelta(hours=24)
    recent = []
    for item in news:
        pub_raw = item.get("publishedDate", "")
        try:
            pub_dt = datetime.strptime(pub_raw[:19], "%Y-%m-%d %H:%M:%S")
            if pub_dt >= cutoff:
                recent.append(item)
        except Exception:
            recent.append(item)

    if recent:
        for item in recent[:8]:
            tks = ", ".join(item.get("tickers") or [item.get("symbol", "?")])
            title = item.get("title", "")
            site = item.get("site", "")
            pub = (item.get("publishedDate") or "")[:16]
            lines.append(f"- **[{tks}]** {title}  \n  *{site} · {pub} UTC*")
    else:
        lines.append("- ⚠️ No news found in the last 24h")

    lines.append("")

    # ── Section 4: Earnings ────────────────────────────────────────────────
    lines.append("## 4. Earnings This Week\n")

    pie_set = set(PIE)
    pie_earnings = [e for e in earnings if e.get("symbol") in pie_set]
    other_earnings = [e for e in earnings if e.get("symbol") not in pie_set]

    if pie_earnings:
        lines.append("**PIE AI reporting:**")
        for e in pie_earnings:
            eps_est = e.get("epsEstimated")
            rev_est = e.get("revenueEstimated")
            eps_str = f"EPS est: ${eps_est:.2f}" if eps_est else ""
            rev_str = f"Rev est: ${rev_est / 1e9:.1f}B" if rev_est else ""
            extras = " · ".join(filter(None, [eps_str, rev_str]))
            lines.append(f"- **{e['symbol']}** — {e.get('date', 'TBD')} ({e.get('time', '')}){f' · {extras}' if extras else ''}")
    else:
        lines.append("- No PIE AI stocks reporting this week.")

    if other_earnings:
        lines.append("\n**Other notable reports:**")
        for e in other_earnings[:6]:
            lines.append(f"- {e['symbol']} — {e.get('date', 'TBD')}")

    lines.append("")
    lines.append("---")
    lines.append(f"*Source: Financial Modeling Prep · Generated {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC*")
    lines.append("\nHai domande su qualcosa di specifico di oggi?")

    output = "\n".join(lines)

    # Save to reports/
    os.makedirs("reports", exist_ok=True)
    out_path = f"reports/briefing-{today_file}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(output)
    print(f"\n✓ Saved to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
