# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-08-10 12:18_

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

- Current-params net profit (full sample): **-13.02%**, PF 0.433, 71 trades, max DD -1303.28
- Optimizer out-of-sample: net **-6.0%**, PF 0.254, 32 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-09 00:19 | 5000 | -13.12 | 0.43 | -5.75 | 0.251 | False |
| 2026-08-09 04:29 | 5000 | -13.16 | 0.43 | -5.79 | 0.251 | False |
| 2026-08-09 08:15 | 5000 | -13.26 | 0.428 | -6.01 | 0.229 | False |
| 2026-08-09 12:11 | 5000 | -12.92 | 0.435 | -5.8 | 0.256 | False |
| 2026-08-09 16:09 | 5000 | -12.95 | 0.435 | -5.7 | 0.268 | False |
| 2026-08-09 20:09 | 5000 | -13.02 | 0.433 | -5.48 | 0.276 | False |
| 2026-08-10 00:21 | 5000 | -13.02 | 0.433 | -6.37 | 0.242 | False |
| 2026-08-10 04:33 | 5000 | -13.02 | 0.433 | -6.3 | 0.244 | False |
| 2026-08-10 08:34 | 5000 | -13.02 | 0.433 | -6.3 | 0.244 | False |
| 2026-08-10 12:18 | 5000 | -13.02 | 0.433 | -6.0 | 0.254 | False |
