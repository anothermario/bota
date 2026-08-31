# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-31 12:18_

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

- Current-params net profit (full sample): **-10.51%**, PF 0.461, 70 trades, max DD -1050.84
- Optimizer out-of-sample: net **-2.01%**, PF 0.647, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-30 00:33 | 5000 | -10.85 | 0.45 | -1.03 | 0.788 | False |
| 2026-08-30 04:13 | 5000 | -10.78 | 0.453 | -1.42 | 0.721 | False |
| 2026-08-30 08:13 | 5000 | -10.78 | 0.453 | -1.41 | 0.723 | False |
| 2026-08-30 12:15 | 5000 | -10.78 | 0.453 | -1.23 | 0.75 | False |
| 2026-08-30 16:10 | 5000 | -10.81 | 0.453 | -1.27 | 0.75 | False |
| 2026-08-30 20:09 | 5000 | -10.93 | 0.449 | -1.4 | 0.724 | False |
| 2026-08-31 00:34 | 5000 | -10.82 | 0.453 | -1.44 | 0.724 | False |
| 2026-08-31 04:14 | 5000 | -11.21 | 0.443 | -1.89 | 0.661 | False |
| 2026-08-31 08:17 | 5000 | -10.51 | 0.461 | -1.89 | 0.661 | False |
| 2026-08-31 12:18 | 5000 | -10.51 | 0.461 | -2.01 | 0.647 | False |
