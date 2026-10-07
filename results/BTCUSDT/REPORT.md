# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-07 04:14_

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

- Current-params net profit (full sample): **-10.56%**, PF 0.557, 70 trades, max DD -1291.01
- Optimizer out-of-sample: net **-9.01%**, PF 0.191, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-05 12:19 | 5000 | -9.83 | 0.574 | -5.48 | 0.456 | False |
| 2026-10-05 16:13 | 5000 | -9.83 | 0.574 | -5.48 | 0.456 | False |
| 2026-10-06 00:33 | 5000 | -9.65 | 0.579 | -5.84 | 0.441 | False |
| 2026-10-06 04:14 | 5000 | -9.65 | 0.579 | -6.35 | 0.42 | False |
| 2026-10-06 08:16 | 5000 | -9.65 | 0.579 | -5.8 | 0.444 | False |
| 2026-10-06 12:17 | 5000 | -9.69 | 0.579 | -5.9 | 0.442 | False |
| 2026-10-06 16:13 | 5000 | -10.27 | 0.564 | -7.34 | 0.322 | False |
| 2026-10-06 20:12 | 5000 | -10.27 | 0.564 | -8.66 | 0.192 | False |
| 2026-10-07 00:34 | 5000 | -10.38 | 0.561 | -8.7 | 0.187 | False |
| 2026-10-07 04:14 | 5000 | -10.56 | 0.557 | -9.01 | 0.191 | False |
