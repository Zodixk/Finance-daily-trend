#!/usr/bin/env python3
"""
Daily Finance Briefing — Alessandro's Portfolio
Primary: Financial Modeling Prep API (~8 calls/run)
Fallback: yfinance (if FMP unreachable or returns 4xx)
Env: loaded from .env in repo root if present
"""

import os
import sys
import time
import json
import requests
from datetime import date, datetime, timedelta
from pathlib import Path

# ── Load .env from repo root ──────────────────────────────────────────────────
_env_path = Path(__file__).parent.parent / ".env"
if _env_path.exists():
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

FMP_API_KEY = os.getenv("FMP_API_KEY")

BASE_V3 = "https://financialmodelingprep.com/api/v3"
SESSION = requests.Session()

PIE = ["GOOG", "AMZN", "AVGO", "NVDA", "AMD", "AAPL", "ASML", "CSCO", "META", "MSFT", "QCOM", "TSM"]
ETF = "FTDL.DE"

_FMP_OK = True  # set False on first network block


# ── FMP helpers ───────────────────────────────────────────────────────────────

def fmp(url, params=None):
    global _FMP_OK
    if not _FMP_OK or not FMP_API_KEY:
        return None
    time.sleep(0.35)
    p = {"apikey": FMP_API_KEY, **(params or {})}
    try:
        r = SESSION.get(url, params=p, timeout=30)
        if r.status_code == 200:
            data = r.json()
            return data if data else None
        if r.status_code in (403, 401):
            body = r.text[:200]
            if "allowlist" in body.lower() or "not in allowlist" in body.lower():
                print(f"WARN: FMP blocked by network policy ({url}). Switching to yfinance fallback.", file=sys.stderr)
                _FMP_OK = False
                return None
        print(f"WARN: {url} → HTTP {r.status_code}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"WARN: {url} failed: {e}", file=sys.stderr)
        return None


# ── yfinance fallback ─────────────────────────────────────────────────────────

def _yf_quotes(tickers):
    """Return dict {symbol: {price, changesPercentage, yearHigh, yearLow}} via yfinance."""
    try:
        import yfinance as yf
        results = {}
        for t in tickers:
            try:
                tk = yf.Ticker(t)
                hist = tk.history(period="5d", auto_adjust=True)
                if hist.empty:
                    continue
                p = float(hist["Close"].iloc[-1])
                prev = float(hist["Close"].iloc[-2]) if len(hist) >= 2 else p
                chg = ((p - prev) / prev) * 100 if prev else 0.0
                info = tk.fast_info
                hi = float(getattr(info, "year_high", 0) or 0)
                lo = float(getattr(info, "year_low", 0) or 0)
                results[t] = {"price": p, "changesPercentage": chg, "yearHigh": hi, "yearLow": lo}
            except Exception as e:
                print(f"WARN: yfinance {t}: {e}", file=sys.stderr)
        return results
    except ImportError:
        print("WARN: yfinance not installed. Run: pip install yfinance", file=sys.stderr)
        return {}


def _yf_index():
    """Return {^VIX, ^GSPC, ^IXIC} via yfinance."""
    try:
        import yfinance as yf
        results = {}
        for sym, key in [("^VIX", "^VIX"), ("^GSPC", "^GSPC"), ("^IXIC", "^IXIC")]:
            try:
                hist = yf.Ticker(sym).history(period="5d")
                if hist.empty:
                    continue
                p = float(hist["Close"].iloc[-1])
                prev = float(hist["Close"].iloc[-2]) if len(hist) >= 2 else p
                chg = ((p - prev) / prev) * 100 if prev else 0.0
                results[key] = {"price": p, "changesPercentage": chg}
            except Exception as e:
                print(f"WARN: yfinance {sym}: {e}", file=sys.stderr)
        return results
    except ImportError:
        return {}


# ── Data fetchers (FMP first, yfinance fallback) ───────────────────────────────

def batch_quotes(tickers):
    results = {}
    for i in range(0, len(tickers), 5):
        batch = ",".join(tickers[i:i + 5])
        data = fmp(f"{BASE_V3}/quote/{batch}")
        if data:
            for q in data:
                results[q["symbol"]] = q
    if len(results) < len(tickers):
        missing = [t for t in tickers if t not in results]
        print(f"INFO: FMP missing {missing}, trying yfinance...", file=sys.stderr)
        yf_data = _yf_quotes(missing)
        results.update(yf_data)
    return results


def index_quotes():
    data = fmp(f"{BASE_V3}/quote/%5EVIX,%5EGSPC,%5EIXIC")
    if not data:
        data = fmp(f"{BASE_V3}/quote/SPY,QQQ")
    results = {}
    if data:
        for q in data:
            results[q["symbol"]] = q
    if not results:
        results = _yf_index()
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


# ── Formatting ────────────────────────────────────────────────────────────────

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


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if not FMP_API_KEY:
        print("WARN: FMP_API_KEY not set — running in yfinance-only mode.", file=sys.stderr)

    today_str = date.today().strftime("%d %B %Y")
    today_file = date.today().isoformat()

    print("Fetching market data...", file=sys.stderr)

    pie_q = batch_quotes(PIE)
    etf_data = fmp(f"{BASE_V3}/quote/{ETF}")
    etf_q = etf_data[0] if etf_data else None
    if etf_q is None:
        yf_etf = _yf_quotes([ETF])
        etf_q = yf_etf.get(ETF)
    idx_q = index_quotes()
    news = recent_news(PIE[:6]) + recent_news(PIE[6:])
    earnings = earnings_calendar()

    used_fallback = not _FMP_OK or not FMP_API_KEY
    source_note = "yfinance (FMP network-blocked)" if used_fallback else "Financial Modeling Prep"

    lines = []
    lines.append(f"# Briefing del {today_str} — Buongiorno Alessandro\n")
    if used_fallback:
        lines.append("> ⚠️ **FMP API bloccato dalla network policy** — prezzi da yfinance (meno precisi).\n")

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
        price_key = "price" if "price" in etf_q else "price"
        chg_key = "changesPercentage"
        lines.append(f"- **FTDL (ETF core):** €{price_str(etf_q.get(price_key))} {pct(etf_q.get(chg_key))}")
    else:
        lines.append("- **FTDL (ETF core):** ⚠️ unavailable — verifica manualmente su XETRA/Trader 212")

    lines.append("")

    # ── Section 2: PIE AI Quotes ───────────────────────────────────────────
    lines.append("## 2. PIE AI — Quotes\n")
    lines.append("| Ticker | Price | Change % | 52w High | 52w Low | Flag |")
    lines.append("|--------|-------|----------|----------|---------|------|")

    for ticker in PIE:
        q = pie_q.get(ticker)
        if q:
            p_val = q.get("price")
            chg_val = q.get("changesPercentage")
            p = price_str(p_val)
            chg = pct(chg_val)
            hi = price_str(q.get("yearHigh"))
            lo = price_str(q.get("yearLow"))
            flag = ""
            if chg_val is not None:
                if chg_val <= -5:
                    flag = "⚠️ NEAR STOP"
                elif chg_val >= 10:
                    flag = "📈 LIMIT REVIEW"
            lines.append(f"| **{ticker}** | ${p} | {chg} | ${hi} | ${lo} | {flag} |")
        else:
            lines.append(f"| **{ticker}** | ⚠️ N/A | — | — | — | — |")

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
        lines.append("- ⚠️ No news found in the last 24h (FMP news endpoint unavailable)")

    lines.append("")

    # ── Section 4: Earnings ────────────────────────────────────────────────
    lines.append("## 4. Earnings This Week\n")

    pie_set = set(PIE)
    pie_earnings = [e for e in earnings if e.get("symbol") in pie_set]
    other_earnings = [e for e in earnings if e.get("symbol") not in pie_set]

    if pie_earnings:
        lines.append("**⚠️ PIE AI reporting:**")
        for e in pie_earnings:
            eps_est = e.get("epsEstimated")
            rev_est = e.get("revenueEstimated")
            eps_str = f"EPS est: ${eps_est:.2f}" if eps_est else ""
            rev_str = f"Rev est: ${rev_est / 1e9:.1f}B" if rev_est else ""
            extras = " · ".join(filter(None, [eps_str, rev_str]))
            lines.append(f"- **{e['symbol']}** — {e.get('date', 'TBD')} ({e.get('time', '')}){f' · {extras}' if extras else ''}")
    else:
        lines.append("- ✅ No PIE AI stocks reporting this week.")

    if other_earnings:
        lines.append("\n**Other notable reports:**")
        for e in other_earnings[:6]:
            lines.append(f"- {e['symbol']} — {e.get('date', 'TBD')}")

    lines.append("")
    lines.append("---")
    lines.append(f"*Source: {source_note} · Generated {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC*")
    lines.append("\nHai domande su qualcosa di specifico di oggi?")

    output = "\n".join(lines)

    os.makedirs("reports", exist_ok=True)
    out_path = f"reports/briefing-{today_file}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(output)
    print(f"\n✓ Saved to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
