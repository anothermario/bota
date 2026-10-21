# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-10-21 16:11_

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
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-13.94%**, PF 0.468, 64 trades, max DD -1583.03
- Optimizer out-of-sample: net **-5.79%**, PF 0.347, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-20 04:13 | 5000 | -14.28 | 0.458 | -5.64 | 0.35 | False |
| 2026-10-20 08:15 | 5000 | -14.28 | 0.458 | -5.79 | 0.344 | False |
| 2026-10-20 12:17 | 5000 | -13.44 | 0.476 | -5.08 | 0.377 | False |
| 2026-10-20 16:13 | 5000 | -14.7 | 0.453 | -6.45 | 0.322 | False |
| 2026-10-20 20:11 | 5000 | -14.68 | 0.453 | -6.45 | 0.322 | False |
| 2026-10-21 00:28 | 5000 | -14.5 | 0.457 | -6.45 | 0.322 | False |
| 2026-10-21 04:13 | 5000 | -13.94 | 0.468 | -6.45 | 0.322 | False |
| 2026-10-21 08:15 | 5000 | -13.94 | 0.468 | -6.46 | 0.321 | False |
| 2026-10-21 12:16 | 5000 | -13.94 | 0.468 | -5.79 | 0.347 | False |
| 2026-10-21 16:11 | 5000 | -13.94 | 0.468 | -5.79 | 0.347 | False |
