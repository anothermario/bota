# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-11 09:28_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-11.43%**, PF 0.55, 67 trades, max DD -1142.64
- Optimizer out-of-sample: net **-4.73%**, PF 0.141, 13 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-09 21:22 | 5000 | -12.37 | 0.535 | -5.32 | 0.327 | False |
| 2026-07-10 02:56 | 5000 | -12.38 | 0.535 | -5.74 | 0.262 | False |
| 2026-07-10 07:34 | 5000 | -12.45 | 0.534 | -5.66 | 0.272 | False |
| 2026-07-10 10:52 | 5000 | -11.59 | 0.555 | -6.29 | 0.108 | False |
| 2026-07-10 14:24 | 5000 | -12.86 | 0.517 | -6.29 | 0.108 | False |
| 2026-07-10 17:47 | 5000 | -11.95 | 0.537 | -6.33 | 0.107 | False |
| 2026-07-10 21:05 | 5000 | -11.81 | 0.546 | -6.29 | 0.191 | False |
| 2026-07-11 02:33 | 5000 | -11.49 | 0.548 | -5.22 | 0.128 | False |
| 2026-07-11 06:12 | 5000 | -11.43 | 0.55 | -4.73 | 0.141 | False |
| 2026-07-11 09:28 | 5000 | -11.43 | 0.55 | -4.73 | 0.141 | False |
