"""
Grid trading backtest — buy low, sell high, repeat.
Compares the strategy against simple buy & hold.
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def run_backtest(ticker: str, capital: float, sell_pct: float, rebuy_pct: float, years: int = 2):
    end = datetime.today()
    start = end - timedelta(days=365 * years)

    df = yf.download(ticker, start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d"),
                     auto_adjust=True, progress=False)
    if df.empty:
        print(f"No data for {ticker}")
        return

    prices = df["Close"].squeeze().dropna()

    # --- Grid strategy ---
    cash = capital
    shares = 0.0
    buy_price = None
    trades = []
    state = "waiting"  # waiting → buy on first day

    for date, price in prices.items():
        price = float(price)

        if state == "waiting":
            # First day: buy
            shares = cash / price
            buy_price = price
            cash = 0.0
            state = "holding"
            trades.append({"date": date, "action": "BUY", "price": price, "shares": shares})

        elif state == "holding":
            # Sell if price rose enough
            if price >= buy_price * (1 + sell_pct / 100):
                cash = shares * price
                trades.append({"date": date, "action": "SELL", "price": price,
                                "shares": shares, "pnl": cash - capital})
                sell_price = price
                shares = 0.0
                buy_price = None
                state = "sold"

        elif state == "sold":
            # Rebuy if price fell enough from last sell
            if price <= sell_price * (1 - rebuy_pct / 100):
                shares = cash / price
                buy_price = price
                cash = 0.0
                state = "holding"
                trades.append({"date": date, "action": "BUY", "price": price, "shares": shares})

    # Final portfolio value
    last_price = float(prices.iloc[-1])
    final_value = cash + shares * last_price

    # --- Buy & hold ---
    first_price = float(prices.iloc[0])
    bh_shares = capital / first_price
    bh_final = bh_shares * last_price

    # --- Results ---
    print(f"\n{'='*55}")
    print(f"  BACKTEST: {ticker} — last {years} years")
    print(f"  Sell target: +{sell_pct}% | Rebuy trigger: -{rebuy_pct}%")
    print(f"  Starting capital: €{capital:,.0f}")
    print(f"{'='*55}")

    print(f"\n  GRID STRATEGY")
    print(f"  Number of trades   : {len(trades)}")
    n_buy  = sum(1 for t in trades if t["action"] == "BUY")
    n_sell = sum(1 for t in trades if t["action"] == "SELL")
    print(f"  Buys / Sells       : {n_buy} / {n_sell}")
    print(f"  Final value        : €{final_value:,.0f}")
    grid_return = (final_value - capital) / capital * 100
    print(f"  Total return       : {grid_return:+.1f}%")
    if shares > 0:
        print(f"  Status at end      : HOLDING {shares:.4f} shares at €{last_price:.2f}")
    else:
        print(f"  Status at end      : CASH (waiting for rebuy)")

    print(f"\n  BUY & HOLD")
    print(f"  First price        : €{first_price:.2f}")
    print(f"  Last price         : €{last_price:.2f}")
    print(f"  Final value        : €{bh_final:,.0f}")
    bh_return = (bh_final - capital) / capital * 100
    print(f"  Total return       : {bh_return:+.1f}%")

    print(f"\n  VERDICT")
    diff = final_value - bh_final
    if diff > 0:
        print(f"  Grid beat buy & hold by €{diff:,.0f} ✅")
    else:
        print(f"  Buy & hold beat grid by €{abs(diff):,.0f} ❌")

    print(f"\n  TRADE LOG (last 15)")
    print(f"  {'Date':<12} {'Action':<6} {'Price':>8}  {'Note'}")
    print(f"  {'-'*50}")
    for t in trades[-15:]:
        note = f"PnL: €{t['pnl']:+,.0f}" if "pnl" in t else ""
        print(f"  {str(t['date'].date()):<12} {t['action']:<6} €{t['price']:>7.2f}  {note}")

    print(f"\n  Worst case shown: what if {ticker} drops and never recovers to your buy price?")
    max_price = float(prices.max())
    min_after_max = float(prices[prices.index > prices.idxmax()].min()) if prices.idxmax() < prices.index[-1] else last_price
    drawdown = (min_after_max - max_price) / max_price * 100
    print(f"  Peak: €{max_price:.2f} | Worst drop after peak: {drawdown:.1f}%")
    print(f"  If you had bought at peak, you'd be at {drawdown:.1f}% — waiting to recover.")
    print()


if __name__ == "__main__":
    # Scenario 1: aggressive (sell +5%, rebuy -5%)
    run_backtest("NVDA", capital=1000, sell_pct=5, rebuy_pct=5, years=2)

    # Scenario 2: patient (sell +10%, rebuy -10%)
    run_backtest("NVDA", capital=1000, sell_pct=10, rebuy_pct=10, years=2)

    # Scenario 3: same on VWCE (more stable asset)
    run_backtest("VWCE.DE", capital=1000, sell_pct=5, rebuy_pct=5, years=2)
