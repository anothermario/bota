# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-15 16:12_

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

- Current-params net profit (full sample): **-10.97%**, PF 0.505, 62 trades, max DD -1148.16
- Optimizer out-of-sample: net **-3.78%**, PF 0.347, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-14 04:14 | 5000 | -12.91 | 0.437 | -3.83 | 0.275 | False |
| 2026-10-14 08:15 | 5000 | -12.63 | 0.443 | -4.0 | 0.265 | False |
| 2026-10-14 12:17 | 5000 | -12.63 | 0.443 | -3.99 | 0.266 | False |
| 2026-10-14 16:12 | 5000 | -12.65 | 0.443 | -3.86 | 0.275 | False |
| 2026-10-14 20:11 | 5000 | -12.65 | 0.443 | -3.86 | 0.275 | False |
| 2026-10-15 00:28 | 5000 | -12.65 | 0.443 | -3.58 | 0.291 | False |
| 2026-10-15 04:12 | 5000 | -12.2 | 0.462 | -2.99 | 0.401 | False |
| 2026-10-15 08:15 | 5000 | -11.75 | 0.472 | -2.99 | 0.402 | False |
| 2026-10-15 12:16 | 5000 | -10.14 | 0.526 | -2.99 | 0.402 | False |
| 2026-10-15 16:12 | 5000 | -10.97 | 0.505 | -3.78 | 0.347 | False |
