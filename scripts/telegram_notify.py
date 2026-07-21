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


def send_message(text: str) -> bool:
    try:
        r = requests.post(
            f"{BASE_URL}/sendMessage",
            json={"chat_id": CHAT_ID, "text": text},
            timeout=15,
        )
        if r.status_code == 200:
            return True
        print(f"WARN: Telegram {r.status_code}: {r.text[:200]}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"WARN: Telegram send failed: {e}", file=sys.stderr)
        return False


def _plain(line: str) -> str:
    """Strip markdown emphasis markers so plain-text Telegram messages read cleanly."""
    return line.strip().replace("**", "").replace("__", "").replace("*", "").strip()


def briefing_to_telegram(report_path: Path) -> str:
    """Convert the markdown report to a concise, plain-text Telegram message."""
    if not report_path.exists():
        return "Report not found."

    text = report_path.read_text()
    lines = text.splitlines()

    # Extract key sections (report is always in English per CLAUDE.md)
    postura = next((l for l in lines if "RESTRICT" in l or "ALLOW" in l or "CASH-PRIORITY" in l), "")
    confidence = next((l for l in lines if "Composite Confidence" in l or "composite confidence" in l or "Confidence:" in l), "")
    vix_line = next((l for l in lines if "VIX" in l and ("**" in l or ":" in l)), "")
    sp_line = next((l for l in lines if "S&P 500" in l), "")
    nasdaq_line = next((l for l in lines if "NASDAQ" in l), "")
    insight = ""
    capture = False
    for l in lines:
        if "Idea of the day" in l:
            capture = True
            continue
        if capture and l.strip().startswith(">"):
            insight = _plain(l.lstrip("> ").strip())
            break
        if capture and l.strip() and not l.strip().startswith("#"):
            insight = _plain(l)
            break

    today = date.today().strftime("%d/%m/%Y")

    msg = f"Finance Briefing — {today}\n\n"
    if vix_line:
        msg += f"{_plain(vix_line)}\n"
    if sp_line:
        msg += f"{_plain(sp_line)}\n"
    if nasdaq_line:
        msg += f"{_plain(nasdaq_line)}\n"
    msg += "\n"
    if postura:
        msg += f"Posture: {_plain(postura)}\n"
    if confidence:
        msg += f"{_plain(confidence)}\n"
    if insight:
        msg += f"\nIdea of the day: {insight}\n"
    msg += "\nFull report: github.com/Zodixk/Finance-daily-trend"

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
