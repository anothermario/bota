# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-01 16:49_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.35,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 30,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-4.23%**, PF 0.809, 63 trades, max DD -861.49
- Optimizer out-of-sample: net **-4.11%**, PF 0.484, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-30 05:26 | 5000 | -6.07 | 0.735 | -6.6 | 0.339 | False |
| 2026-06-30 09:11 | 5000 | -6.07 | 0.735 | -7.47 | 0.271 | False |
| 2026-06-30 12:45 | 5000 | -6.11 | 0.733 | -7.48 | 0.27 | False |
| 2026-06-30 16:46 | 5000 | -5.07 | 0.777 | -6.44 | 0.367 | False |
| 2026-06-30 20:41 | 5000 | -5.07 | 0.777 | -5.56 | 0.404 | False |
| 2026-07-01 00:54 | 5000 | -5.07 | 0.777 | -5.16 | 0.423 | False |
| 2026-07-01 05:36 | 5000 | -5.0 | 0.779 | -5.16 | 0.424 | False |
| 2026-07-01 09:12 | 5000 | -4.57 | 0.795 | -4.9 | 0.437 | False |
| 2026-07-01 13:01 | 5000 | -4.59 | 0.794 | -4.92 | 0.436 | False |
| 2026-07-01 16:49 | 5000 | -4.23 | 0.809 | -4.11 | 0.484 | False |
