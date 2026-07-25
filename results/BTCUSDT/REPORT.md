# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-25 16:55_

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

- Current-params net profit (full sample): **-15.09%**, PF 0.441, 72 trades, max DD -1674.84
- Optimizer out-of-sample: net **-6.84%**, PF 0.331, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-24 06:24 | 5000 | -12.53 | 0.553 | -8.1 | 0.249 | False |
| 2026-07-24 10:15 | 5000 | -14.32 | 0.479 | -8.45 | 0.241 | False |
| 2026-07-24 13:42 | 5000 | -14.35 | 0.479 | -8.15 | 0.249 | False |
| 2026-07-24 17:36 | 5000 | -14.35 | 0.479 | -7.71 | 0.26 | False |
| 2026-07-24 21:02 | 5000 | -13.69 | 0.501 | -7.0 | 0.325 | False |
| 2026-07-25 02:32 | 5000 | -13.67 | 0.502 | -7.0 | 0.325 | False |
| 2026-07-25 06:16 | 5000 | -13.09 | 0.527 | -7.0 | 0.325 | False |
| 2026-07-25 09:45 | 5000 | -13.59 | 0.506 | -7.34 | 0.314 | False |
| 2026-07-25 13:22 | 5000 | -14.27 | 0.477 | -6.84 | 0.331 | False |
| 2026-07-25 16:55 | 5000 | -15.09 | 0.441 | -6.84 | 0.331 | False |
