# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-20 12:16_

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

- Current-params net profit (full sample): **-12.3%**, PF 0.483, 65 trades, max DD -1244.38
- Optimizer out-of-sample: net **-2.8%**, PF 0.435, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-19 00:31 | 5000 | -12.42 | 0.464 | -3.24 | 0.364 | False |
| 2026-10-19 04:13 | 5000 | -12.42 | 0.464 | -3.24 | 0.364 | False |
| 2026-10-19 08:19 | 5000 | -11.57 | 0.499 | -2.22 | 0.559 | False |
| 2026-10-19 12:18 | 5000 | -11.59 | 0.498 | -2.22 | 0.56 | False |
| 2026-10-19 16:12 | 5000 | -11.59 | 0.498 | -2.58 | 0.502 | False |
| 2026-10-19 20:11 | 5000 | -11.59 | 0.498 | -2.42 | 0.518 | False |
| 2026-10-20 00:29 | 5000 | -12.01 | 0.488 | -2.43 | 0.517 | False |
| 2026-10-20 04:12 | 5000 | -12.31 | 0.483 | -3.17 | 0.443 | False |
| 2026-10-20 08:15 | 5000 | -12.31 | 0.483 | -3.54 | 0.376 | False |
| 2026-10-20 12:16 | 5000 | -12.3 | 0.483 | -2.8 | 0.435 | False |
