#!/usr/bin/env python3
"""
Adanos sentiment for PIE AI tickers.
Fetches Reddit + X (Twitter) sentiment scores.
API docs: api.adanos.org — requires X-API-Key header.
"""

import os
import sys
import time
import requests
from pathlib import Path

# ── Load .env ─────────────────────────────────────────────────────────────────
_env_path = Path(__file__).parent.parent / ".env"
if _env_path.exists():
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

API_KEY = os.getenv("ADANOS_API_KEY")
BASE = "https://api.adanos.org"
HEADERS = {"X-API-Key": API_KEY} if API_KEY else {}

TICKERS = ["NVDA", "AAPL", "MSFT", "META", "GOOG", "AMZN", "AMD", "AVGO"]


def fetch(platform, ticker):
    """Fetch sentiment for one ticker from one platform. Returns dict or None."""
    if not API_KEY:
        return None
    time.sleep(0.3)
    url = f"{BASE}/{platform}/stocks/v1/stock/{ticker}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            return r.json()
        print(f"WARN: Adanos {platform}/{ticker} → {r.status_code}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"WARN: Adanos {platform}/{ticker}: {e}", file=sys.stderr)
        return None


def sentiment_label(score, bullish_pct, bearish_pct):
    """Convert raw numbers to a human-readable label."""
    if score is None:
        return "neutral"
    if score > 0.15 or (bullish_pct and bullish_pct > 45):
        return "bullish"
    if score < -0.05 or (bearish_pct and bearish_pct > 35):
        return "bearish"
    return "neutral"


def main():
    if not API_KEY:
        print("⚠️ ADANOS_API_KEY not set.", file=sys.stderr)
        return {}

    results = {}
    for ticker in TICKERS:
        reddit = fetch("reddit", ticker)
        x = fetch("x", ticker)

        r_label = sentiment_label(
            reddit.get("sentiment_score") if reddit else None,
            reddit.get("bullish_pct") if reddit else None,
            reddit.get("bearish_pct") if reddit else None,
        )
        x_label = sentiment_label(
            x.get("sentiment_score") if x else None,
            x.get("bullish_pct") if x else None,
            x.get("bearish_pct") if x else None,
        )

        results[ticker] = {
            "reddit": {
                "label": r_label,
                "score": reddit.get("sentiment_score") if reddit else None,
                "bullish_pct": reddit.get("bullish_pct") if reddit else None,
                "bearish_pct": reddit.get("bearish_pct") if reddit else None,
                "buzz": reddit.get("buzz_score") if reddit else None,
                "trend": reddit.get("trend") if reddit else None,
            },
            "x": {
                "label": x_label,
                "score": x.get("sentiment_score") if x else None,
                "bullish_pct": x.get("bullish_pct") if x else None,
                "bearish_pct": x.get("bearish_pct") if x else None,
                "buzz": x.get("buzz_score") if x else None,
                "trend": x.get("trend") if x else None,
            },
        }

    # Print markdown table
    print("## Social Sentiment (Reddit + X)\n")
    print("| Ticker | Reddit | X/Twitter | Reddit Buzz | X Buzz | Reddit Trend |")
    print("|--------|--------|-----------|-------------|--------|--------------|")
    for ticker, d in results.items():
        r = d["reddit"]
        x = d["x"]
        r_label = f"{'🟢' if r['label']=='bullish' else '🔴' if r['label']=='bearish' else '⚪'} {r['label']}"
        x_label = f"{'🟢' if x['label']=='bullish' else '🔴' if x['label']=='bearish' else '⚪'} {x['label']}"
        r_buzz = f"{r['buzz']:.0f}/100" if r['buzz'] else "N/A"
        x_buzz = f"{x['buzz']:.0f}/100" if x['buzz'] else "N/A"
        r_trend = r.get("trend") or "N/A"
        print(f"| **{ticker}** | {r_label} | {x_label} | {r_buzz} | {x_buzz} | {r_trend} |")

    return results


if __name__ == "__main__":
    main()
