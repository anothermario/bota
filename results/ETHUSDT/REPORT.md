# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-21 16:07_

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

- Current-params net profit (full sample): **-9.34%**, PF 0.586, 73 trades, max DD -1101.99
- Optimizer out-of-sample: net **-4.23%**, PF 0.544, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-20 04:08 | 5000 | -10.92 | 0.527 | -4.36 | 0.543 | False |
| 2026-11-20 08:10 | 5000 | -10.93 | 0.527 | -4.35 | 0.544 | False |
| 2026-11-20 12:10 | 5000 | -10.83 | 0.529 | -4.35 | 0.544 | False |
| 2026-11-20 16:08 | 5000 | -10.84 | 0.529 | -4.37 | 0.543 | False |
| 2026-11-20 20:07 | 5000 | -10.84 | 0.529 | -4.36 | 0.544 | False |
| 2026-11-21 00:19 | 5000 | -9.92 | 0.569 | -4.41 | 0.531 | False |
| 2026-11-21 04:08 | 5000 | -9.93 | 0.569 | -4.43 | 0.531 | False |
| 2026-11-21 08:09 | 5000 | -9.35 | 0.586 | -4.19 | 0.545 | False |
| 2026-11-21 12:10 | 5000 | -9.35 | 0.586 | -4.18 | 0.546 | False |
| 2026-11-21 16:07 | 5000 | -9.34 | 0.586 | -4.23 | 0.544 | False |
