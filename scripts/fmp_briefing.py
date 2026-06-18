#!/usr/bin/env python3
"""
Daily Finance Briefing — Alessandro's Portfolio
FMP stable API (one ticker at a time — multi-symbol is premium)
Fallback: yfinance for VWCE.DE and any ticker FMP can't serve
"""

import os
import sys
import time
import requests
from datetime import date, datetime, timedelta
from pathlib import Path

# ── Load .env ─────────────────────────────────────────────────────────────────
_env_path = Path(__file__).parent.parent / ".env"
if _env_path.exists():
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

FMP_API_KEY = os.getenv("FMP_API_KEY")
BASE = "https://financialmodelingprep.com/stable"
SESSION = requests.Session()

INDIVIDUAL_POSITIONS = ["SECO"]
ETF = "VWCE.DE"
INDICES = {"VIX": "^VIX", "NASDAQ": "^IXIC", "SP500": "^GSPC"}


# ── FMP single-ticker quote ───────────────────────────────────────────────────

def fmp_quote(symbol):
    """Fetch a single quote from FMP stable API. Returns dict or None."""
    if not FMP_API_KEY:
        return None
    time.sleep(0.25)
    try:
        r = SESSION.get(
            f"{BASE}/quote",
            params={"symbol": symbol, "apikey": FMP_API_KEY},
            timeout=20,
        )
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, list) and data:
                return data[0]
            if isinstance(data, dict) and data.get("price"):
                return data
        if r.status_code in (402, 403):
            print(f"WARN: FMP {symbol} → HTTP {r.status_code} (subscription limit)", file=sys.stderr)
        else:
            print(f"WARN: FMP {symbol} → HTTP {r.status_code}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"WARN: FMP {symbol} error: {e}", file=sys.stderr)
        return None


def fmp_earnings(from_date, to_date):
    if not FMP_API_KEY:
        return []
    try:
        r = SESSION.get(
            f"{BASE}/earning-calendar",
            params={"from": from_date, "to": to_date, "apikey": FMP_API_KEY},
            timeout=20,
        )
        if r.status_code == 200:
            return r.json() or []
    except Exception as e:
        print(f"WARN: FMP earnings: {e}", file=sys.stderr)
    return []


# ── yfinance fallback ─────────────────────────────────────────────────────────

def yf_quote(ticker):
    """Single ticker via yfinance. Returns dict or None."""
    try:
        import yfinance as yf
        tk = yf.Ticker(ticker)
        hist = tk.history(period="5d", auto_adjust=True)
        if hist.empty:
            return None
        hist = hist["Close"].dropna()
        if hist.empty:
            return None
        p = float(hist.iloc[-1])
        prev = float(hist.iloc[-2]) if len(hist) >= 2 else p
        chg = ((p - prev) / prev) * 100 if prev else 0.0
        info = tk.fast_info
        hi = float(getattr(info, "year_high", 0) or 0)
        lo = float(getattr(info, "year_low", 0) or 0)
        return {"symbol": ticker, "price": p, "changePercentage": chg, "yearHigh": hi, "yearLow": lo}
    except Exception as e:
        print(f"WARN: yfinance {ticker}: {e}", file=sys.stderr)
        return None


# ── Normalise quote dict ──────────────────────────────────────────────────────

def norm(q):
    """Return (price, change_pct, year_high, year_low) from any quote dict."""
    if not q:
        return None, None, None, None
    price = q.get("price")
    chg = q.get("changePercentage") or q.get("changesPercentage")
    hi = q.get("yearHigh") or q.get("year_high")
    lo = q.get("yearLow") or q.get("year_low")
    return price, chg, hi, lo


# ── Formatting ────────────────────────────────────────────────────────────────

def fmt_pct(val):
    if val is None:
        return "N/A"
    arrow = "▲" if val >= 0 else "▼"
    sign = "+" if val >= 0 else ""
    return f"{arrow} {sign}{val:.2f}%"


def fmt_price(val, currency="€"):
    if val is None:
        return "N/A"
    return f"{currency}{val:.2f}"


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    today_str = date.today().strftime("%B %d, %Y")
    today_file = date.today().isoformat()
    print("Fetching market data...", file=sys.stderr)

    # Indices: FMP first, yfinance fallback
    idx = {}
    for key, sym in INDICES.items():
        q = fmp_quote(sym)
        if q:
            idx[key] = q
        else:
            q = yf_quote(sym)
            if q:
                idx[key] = q

    # ETF (VWCE.DE): yfinance directly (FMP doesn't support European ETFs on free plan)
    etf_q = yf_quote(ETF)

    # Individual positions: FMP first, yfinance fallback
    positions_q = {}
    for ticker in INDIVIDUAL_POSITIONS:
        q = fmp_quote(ticker)
        if q:
            positions_q[ticker] = q
        else:
            q = yf_quote(ticker)
            if q:
                positions_q[ticker] = q

    # Earnings calendar
    today = date.today()
    earnings = fmp_earnings(today.isoformat(), (today + timedelta(days=7)).isoformat())
    position_earnings = [e for e in earnings if e.get("symbol") in set(INDIVIDUAL_POSITIONS)]

    # ── Build report ──────────────────────────────────────────────────────────
    lines = []
    lines.append(f"# Daily Briefing — {today_str}\n")

    # Market overview
    lines.append("## Market Overview\n")
    vix_q = idx.get("VIX")
    nasdaq_q = idx.get("NASDAQ")
    sp_q = idx.get("SP500")

    if vix_q:
        vix_val = vix_q.get("price", 0)
        p, chg, _, _ = norm(vix_q)
        regime = "risk-off (fear elevated)" if vix_val > 20 else "risk-on (calm)"
        lines.append(f"- **VIX:** {fmt_price(p, '')} {fmt_pct(chg)} — {regime}")
    else:
        lines.append("- **VIX:** ⚠️ unavailable")

    if nasdaq_q:
        p, chg, _, _ = norm(nasdaq_q)
        lines.append(f"- **NASDAQ:** {fmt_price(p, '')} {fmt_pct(chg)}")
    else:
        lines.append("- **NASDAQ:** ⚠️ unavailable")

    if sp_q:
        p, chg, _, _ = norm(sp_q)
        lines.append(f"- **S&P 500:** {fmt_price(p, '')} {fmt_pct(chg)}")
    else:
        lines.append("- **S&P 500:** ⚠️ unavailable")

    if etf_q:
        p, chg, _, _ = norm(etf_q)
        lines.append(f"- **VWCE (core ETF):** {fmt_price(p)} {fmt_pct(chg)}")
    else:
        lines.append("- **VWCE:** ⚠️ unavailable — check on Trader 212 / XETRA")

    lines.append("")

    # Individual positions
    lines.append("## Individual Positions — Quotes\n")
    lines.append("| Ticker | Price | Change | 52w High | 52w Low | Flag |")
    lines.append("|--------|-------|--------|----------|---------|------|")  

    for ticker in INDIVIDUAL_POSITIONS:
        q = positions_q.get(ticker)
        if q:
            p, chg, hi, lo = norm(q)
            flag = ""
            if chg is not None:
                if chg <= -5:
                    flag = "⚠️ NEAR STOP"
                elif chg >= 10:
                    flag = "📈 LIMIT REVIEW"
            lines.append(
                f"| **{ticker}** | {fmt_price(p)} | {fmt_pct(chg)} | {fmt_price(hi)} | {fmt_price(lo)} | {flag} |"
            )
        else:
            lines.append(f"| **{ticker}** | ⚠️ N/A | — | — | — | — |")

    lines.append("")

    # Earnings
    lines.append("## Earnings This Week\n")
    if position_earnings:
        lines.append("**⚠️ Individual positions reporting:**")
        for e in position_earnings:
            eps = e.get("epsEstimated")
            rev = e.get("revenueEstimated")
            eps_s = f"EPS est: ${eps:.2f}" if eps else ""
            rev_s = f"Rev est: ${rev/1e9:.1f}B" if rev else ""
            extra = " · ".join(filter(None, [eps_s, rev_s]))
            lines.append(f"- **{e['symbol']}** — {e.get('date','TBD')} {e.get('time','')} {f'· {extra}' if extra else ''}")
    else:
        lines.append("- ✅ No individual positions reporting this week.")

    other_e = [e for e in earnings if e.get("symbol") not in set(INDIVIDUAL_POSITIONS)]
    if other_e:
        lines.append("\n**Other notable reports:**")
        for e in other_e[:5]:
            lines.append(f"- {e['symbol']} — {e.get('date','TBD')}")

    lines.append("")
    lines.append("---")
    lines.append(f"*Source: FMP stable API + yfinance · Generated {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC*")
    lines.append("\nAny questions about something specific today?")

    output = "\n".join(lines)

    os.makedirs("reports", exist_ok=True)
    out_path = f"reports/briefing-{today_file}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(output)
    print(f"\n✓ Saved to {out_path}", file=sys.stderr)
    return {
        "vix": idx.get("VIX"), "nasdaq": idx.get("NASDAQ"),
        "sp500": idx.get("SP500"), "vwce": etf_q,
        "positions": positions_q, "position_earnings": position_earnings,
    }


if __name__ == "__main__":
    main()
