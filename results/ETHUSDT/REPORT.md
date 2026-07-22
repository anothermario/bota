# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-22 10:24_

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

- Current-params net profit (full sample): **-17.69%**, PF 0.489, 97 trades, max DD -1957.11
- Optimizer out-of-sample: net **-11.0%**, PF 0.148, 29 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-20 21:11 | 5000 | -17.84 | 0.483 | -11.44 | 0.119 | False |
| 2026-07-21 02:34 | 5000 | -17.51 | 0.49 | -11.54 | 0.118 | False |
| 2026-07-21 06:27 | 5000 | -17.52 | 0.49 | -11.32 | 0.121 | False |
| 2026-07-21 10:24 | 5000 | -17.49 | 0.49 | -11.32 | 0.121 | False |
| 2026-07-21 13:46 | 5000 | -16.5 | 0.517 | -10.96 | 0.147 | False |
| 2026-07-21 17:18 | 5000 | -16.5 | 0.517 | -10.33 | 0.155 | False |
| 2026-07-21 21:08 | 5000 | -16.53 | 0.517 | -9.92 | 0.161 | False |
| 2026-07-22 02:33 | 5000 | -16.97 | 0.51 | -10.21 | 0.158 | False |
| 2026-07-22 06:27 | 5000 | -17.91 | 0.485 | -10.78 | 0.15 | False |
| 2026-07-22 10:24 | 5000 | -17.69 | 0.489 | -11.0 | 0.148 | False |
