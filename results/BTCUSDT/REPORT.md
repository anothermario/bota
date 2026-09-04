# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-04 00:28_

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

- Current-params net profit (full sample): **-7.48%**, PF 0.615, 70 trades, max DD -1183.25
- Optimizer out-of-sample: net **-1.66%**, PF 0.733, 17 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-02 12:18 | 5000 | -11.14 | 0.449 | -3.33 | 0.484 | False |
| 2026-09-02 16:13 | 5000 | -11.7 | 0.436 | -4.46 | 0.407 | False |
| 2026-09-02 20:11 | 5000 | -11.35 | 0.445 | -4.46 | 0.407 | False |
| 2026-09-03 00:32 | 5000 | -11.35 | 0.444 | -3.95 | 0.438 | False |
| 2026-09-03 05:15 | 5000 | -11.37 | 0.444 | -3.96 | 0.438 | False |
| 2026-09-03 08:16 | 5000 | -10.92 | 0.455 | -3.95 | 0.438 | False |
| 2026-09-03 12:18 | 5000 | -10.23 | 0.473 | -3.94 | 0.439 | False |
| 2026-09-03 16:12 | 5000 | -10.27 | 0.473 | -3.66 | 0.461 | False |
| 2026-09-03 20:10 | 5000 | -10.27 | 0.473 | -3.75 | 0.447 | False |
| 2026-09-04 00:28 | 5000 | -7.48 | 0.615 | -1.66 | 0.733 | False |
