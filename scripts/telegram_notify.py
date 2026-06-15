#!/usr/bin/env python3
"""
Send the daily briefing report to Telegram.
Reads TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID from environment or .env file.
"""

import os
import sys
import requests
from pathlib import Path
from datetime import date

# ── Load .env ─────────────────────────────────────────────────────────────────
_env_path = Path(__file__).parent.parent / ".env"
if _env_path.exists():
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    sys.exit("ERROR: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set in .env")

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(text: str, parse_mode: str = "Markdown") -> bool:
    try:
        r = requests.post(
            f"{BASE_URL}/sendMessage",
            json={"chat_id": CHAT_ID, "text": text, "parse_mode": parse_mode},
            timeout=15,
        )
        if r.status_code == 200:
            return True
        print(f"WARN: Telegram {r.status_code}: {r.text[:200]}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"WARN: Telegram send failed: {e}", file=sys.stderr)
        return False


def briefing_to_telegram(report_path: Path) -> str:
    """Convert the markdown report to a concise Telegram message."""
    if not report_path.exists():
        return "⚠️ Report non trovato."

    text = report_path.read_text()
    lines = text.splitlines()

    # Extract key sections
    postura = next((l for l in lines if "POSTURA" in l or "RESTRICT" in l or "ALLOW" in l or "CASH-PRIORITY" in l), "")
    confidence = next((l for l in lines if "Composite Confidence" in l or "composite confidence" in l), "")
    vix_line = next((l for l in lines if "**VIX**" in l), "")
    sp_line = next((l for l in lines if "**S&P 500**" in l), "")
    nasdaq_line = next((l for l in lines if "**NASDAQ**" in l), "")
    insight = ""
    capture = False
    for l in lines:
        if "Insight del Giorno" in l:
            capture = True
            continue
        if capture and l.strip().startswith(">"):
            insight = l.strip().lstrip("> ").strip()
            break
        if capture and l.strip() and not l.startswith("#"):
            insight = l.strip()
            break

    today = date.today().strftime("%d/%m/%Y")

    msg = f"📊 *Finance Briefing — {today}*\n\n"
    if vix_line:
        msg += f"{vix_line.strip()}\n"
    if sp_line:
        msg += f"{sp_line.strip()}\n"
    if nasdaq_line:
        msg += f"{nasdaq_line.strip()}\n"
    msg += "\n"
    if postura:
        msg += f"🎯 {postura.strip()}\n"
    if confidence:
        msg += f"📈 {confidence.strip()}\n"
    if insight:
        msg += f"\n💡 _{insight}_\n"
    msg += "\n📁 Report completo: github.com/Zodixk/Finance-daily-trend"

    return msg


def main():
    today = date.today().isoformat()
    report_path = Path(__file__).parent.parent / "reports" / f"briefing-{today}.md"

    # Try to send a summary message
    msg = briefing_to_telegram(report_path)
    success = send_message(msg)

    if success:
        print(f"✓ Telegram notification sent for {today}", file=sys.stderr)
    else:
        print(f"✗ Telegram notification failed for {today}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
