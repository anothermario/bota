# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-06 00:33_

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

- Current-params net profit (full sample): **-9.65%**, PF 0.579, 67 trades, max DD -1293.09
- Optimizer out-of-sample: net **-5.84%**, PF 0.441, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-04 10:09 | 5000 | -10.6 | 0.545 | -5.6 | 0.414 | False |
| 2026-10-04 13:57 | 5000 | -10.41 | 0.551 | -5.36 | 0.435 | False |
| 2026-10-04 17:28 | 5000 | -10.41 | 0.551 | -5.36 | 0.435 | False |
| 2026-10-04 20:47 | 5000 | -10.08 | 0.566 | -5.39 | 0.436 | False |
| 2026-10-05 00:35 | 5000 | -10.07 | 0.566 | -4.61 | 0.499 | False |
| 2026-10-05 04:19 | 5000 | -9.83 | 0.574 | -5.54 | 0.452 | False |
| 2026-10-05 08:24 | 5000 | -9.83 | 0.574 | -5.65 | 0.448 | False |
| 2026-10-05 12:19 | 5000 | -9.83 | 0.574 | -5.48 | 0.456 | False |
| 2026-10-05 16:13 | 5000 | -9.83 | 0.574 | -5.48 | 0.456 | False |
| 2026-10-06 00:33 | 5000 | -9.65 | 0.579 | -5.84 | 0.441 | False |
