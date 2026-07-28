# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-07-28 21:06_

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

- Current-params net profit (full sample): **-19.98%**, PF 0.439, 98 trades, max DD -2144.23
- Optimizer out-of-sample: net **-8.38%**, PF 0.285, 33 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-27 11:19 | 5000 | -19.26 | 0.436 | -9.93 | 0.175 | False |
| 2026-07-27 14:30 | 5000 | -19.4 | 0.436 | -10.72 | 0.164 | False |
| 2026-07-27 17:41 | 5000 | -19.41 | 0.436 | -10.4 | 0.169 | False |
| 2026-07-27 21:09 | 5000 | -20.02 | 0.428 | -11.07 | 0.16 | False |
| 2026-07-28 02:27 | 5000 | -20.06 | 0.427 | -10.72 | 0.166 | False |
| 2026-07-28 06:26 | 5000 | -20.02 | 0.428 | -9.98 | 0.179 | False |
| 2026-07-28 10:33 | 5000 | -19.68 | 0.44 | -9.18 | 0.193 | False |
| 2026-07-28 14:03 | 5000 | -19.69 | 0.439 | -9.18 | 0.193 | False |
| 2026-07-28 17:26 | 5000 | -19.71 | 0.439 | -9.21 | 0.192 | False |
| 2026-07-28 21:06 | 5000 | -19.98 | 0.439 | -8.38 | 0.285 | False |
