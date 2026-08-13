# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-13 00:25_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-14.77%**, PF 0.428, 61 trades, max DD -1655.66
- Optimizer out-of-sample: net **-5.35%**, PF 0.183, 16 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-11 12:18 | 5000 | -15.06 | 0.418 | -6.65 | 0.129 | False |
| 2026-08-11 16:19 | 5000 | -15.07 | 0.417 | -7.26 | 0.118 | False |
| 2026-08-11 20:15 | 5000 | -14.35 | 0.431 | -6.65 | 0.129 | False |
| 2026-08-12 00:24 | 5000 | -14.35 | 0.431 | -5.58 | 0.151 | False |
| 2026-08-12 04:36 | 5000 | -14.35 | 0.431 | -4.78 | 0.27 | False |
| 2026-08-12 08:31 | 5000 | -14.35 | 0.431 | -5.51 | 0.153 | False |
| 2026-08-12 12:19 | 5000 | -14.37 | 0.431 | -5.54 | 0.153 | False |
| 2026-08-12 16:20 | 5000 | -14.9 | 0.422 | -6.11 | 0.14 | False |
| 2026-08-12 20:15 | 5000 | -14.92 | 0.422 | -6.14 | 0.14 | False |
| 2026-08-13 00:25 | 5000 | -14.77 | 0.428 | -5.35 | 0.183 | False |
