"""
fetch_data.py
=============
Pulls OHLCV klines from Binance's PUBLIC market-data endpoint (no API key, no
account needed). Writes a CSV with columns time, open, high, low, close that the
backtester/optimizer consume directly.

We default to data-api.binance.vision (Binance's public data mirror) because it
is generally reachable from cloud IPs — the main api.binance.com host is
geo-blocked in some regions (e.g. US-hosted CI runners get HTTP 451). If one
host fails, pass --base to switch.

Usage:
    python fetch_data.py --symbol BTCUSDT --interval 4h --limit 1500 --out data/BTCUSDT_4h.csv
"""
import argparse
import sys
import time

import pandas as pd
import requests

PRIMARY = "https://data-api.binance.vision"
FALLBACK = "https://api.binance.com"


def fetch_klines(symbol, interval, limit=1000, base=PRIMARY):
    url = f"{base}/api/v3/klines"
    rows, remaining, end = [], limit, None
    while remaining > 0:
        n = min(1000, remaining)
        params = {"symbol": symbol.upper(), "interval": interval, "limit": n}
        if end is not None:
            params["endTime"] = end
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        rows = batch + rows
        end = batch[0][0] - 1          # page backwards in time
        remaining -= len(batch)
        if len(batch) < n:
            break
        time.sleep(0.25)               # be polite to the endpoint
    cols = ["open_time", "open", "high", "low", "close", "volume",
            "close_time", "qav", "trades", "tbav", "tqav", "ignore"]
    df = pd.DataFrame(rows, columns=cols)[["open_time", "open", "high", "low", "close"]]
    df.columns = ["time", "open", "high", "low", "close"]
    for c in ["open", "high", "low", "close"]:
        df[c] = df[c].astype(float)
    df["time"] = pd.to_datetime(df["time"], unit="ms", utc=True)
    return df.drop_duplicates("time").sort_values("time").reset_index(drop=True)


def fetch_with_fallback(symbol, interval, limit):
    for base in (PRIMARY, FALLBACK):
        try:
            df = fetch_klines(symbol, interval, limit, base=base)
            if len(df):
                print(f"[fetch] {len(df)} bars of {symbol} {interval} from {base}")
                return df
        except Exception as e:  # noqa: BLE001
            print(f"[fetch] {base} failed: {e}", file=sys.stderr)
    raise RuntimeError("All data hosts failed — check connectivity / geo-restrictions.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--interval", default="4h")
    ap.add_argument("--limit", type=int, default=1500)
    ap.add_argument("--out", default="data/BTCUSDT_4h.csv")
    ap.add_argument("--base", default=None, help="override data host")
    args = ap.parse_args()

    if args.base:
        df = fetch_klines(args.symbol, args.interval, args.limit, base=args.base)
    else:
        df = fetch_with_fallback(args.symbol, args.interval, args.limit)

    import os
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    df.to_csv(args.out, index=False)
    print(f"[fetch] wrote {args.out}")


if __name__ == "__main__":
    main()
