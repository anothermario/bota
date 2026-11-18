# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-18 20:07_

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

- Current-params net profit (full sample): **-11.47%**, PF 0.512, 75 trades, max DD -1302.23
- Optimizer out-of-sample: net **-3.84%**, PF 0.619, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-17 08:09 | 5000 | -11.88 | 0.5 | -2.36 | 0.739 | False |
| 2026-11-17 12:10 | 5000 | -12.37 | 0.49 | -2.95 | 0.692 | False |
| 2026-11-17 16:08 | 5000 | -12.02 | 0.498 | -2.87 | 0.698 | False |
| 2026-11-17 20:07 | 5000 | -12.02 | 0.498 | -2.87 | 0.698 | False |
| 2026-11-18 00:19 | 5000 | -11.64 | 0.507 | -2.87 | 0.698 | False |
| 2026-11-18 04:08 | 5000 | -11.21 | 0.517 | -2.71 | 0.71 | False |
| 2026-11-18 08:10 | 5000 | -11.21 | 0.517 | -2.71 | 0.71 | False |
| 2026-11-18 12:10 | 5000 | -11.21 | 0.517 | -2.71 | 0.711 | False |
| 2026-11-18 16:07 | 5000 | -11.23 | 0.517 | -2.73 | 0.711 | False |
| 2026-11-18 20:07 | 5000 | -11.47 | 0.512 | -3.84 | 0.619 | False |
