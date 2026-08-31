# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-31 00:34_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-19.66%**, PF 0.299, 99 trades, max DD -1965.54
- Optimizer out-of-sample: net **-6.34%**, PF 0.143, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-29 12:14 | 5000 | -19.22 | 0.325 | -5.51 | 0.062 | False |
| 2026-08-29 16:11 | 5000 | -19.76 | 0.318 | -5.52 | 0.061 | False |
| 2026-08-29 20:10 | 5000 | -19.74 | 0.318 | -5.35 | 0.063 | False |
| 2026-08-30 00:33 | 5000 | -19.23 | 0.325 | -5.35 | 0.063 | False |
| 2026-08-30 04:13 | 5000 | -19.23 | 0.325 | -5.59 | 0.061 | False |
| 2026-08-30 08:13 | 5000 | -19.18 | 0.326 | -5.59 | 0.061 | False |
| 2026-08-30 12:15 | 5000 | -18.55 | 0.335 | -5.62 | 0.06 | False |
| 2026-08-30 16:10 | 5000 | -18.6 | 0.335 | -5.39 | 0.063 | False |
| 2026-08-30 20:10 | 5000 | -18.75 | 0.335 | -5.54 | 0.064 | False |
| 2026-08-31 00:34 | 5000 | -19.66 | 0.299 | -6.34 | 0.143 | False |
