# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-23 06:29_

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

- Current-params net profit (full sample): **-17.55%**, PF 0.492, 95 trades, max DD -2019.59
- Optimizer out-of-sample: net **-10.74%**, PF 0.152, 28 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-21 17:18 | 5000 | -16.5 | 0.517 | -10.33 | 0.155 | False |
| 2026-07-21 21:08 | 5000 | -16.53 | 0.517 | -9.92 | 0.161 | False |
| 2026-07-22 02:33 | 5000 | -16.97 | 0.51 | -10.21 | 0.158 | False |
| 2026-07-22 06:27 | 5000 | -17.91 | 0.485 | -10.78 | 0.15 | False |
| 2026-07-22 10:24 | 5000 | -17.69 | 0.489 | -11.0 | 0.148 | False |
| 2026-07-22 13:50 | 5000 | -18.34 | 0.479 | -11.35 | 0.144 | False |
| 2026-07-22 17:17 | 5000 | -18.36 | 0.478 | -11.35 | 0.144 | False |
| 2026-07-22 21:06 | 5000 | -18.0 | 0.484 | -11.35 | 0.144 | False |
| 2026-07-23 02:38 | 5000 | -18.01 | 0.484 | -10.74 | 0.152 | False |
| 2026-07-23 06:29 | 5000 | -17.55 | 0.492 | -10.74 | 0.152 | False |
