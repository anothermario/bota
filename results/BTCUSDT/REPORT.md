# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-09-03 08:16_

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

- Current-params net profit (full sample): **-10.92%**, PF 0.455, 70 trades, max DD -1170.74
- Optimizer out-of-sample: net **-3.95%**, PF 0.438, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-01 20:11 | 5000 | -11.1 | 0.449 | -2.79 | 0.564 | False |
| 2026-09-02 00:31 | 5000 | -11.11 | 0.449 | -3.67 | 0.455 | False |
| 2026-09-02 04:15 | 5000 | -11.1 | 0.449 | -3.29 | 0.484 | False |
| 2026-09-02 08:16 | 5000 | -11.11 | 0.449 | -3.29 | 0.484 | False |
| 2026-09-02 12:18 | 5000 | -11.14 | 0.449 | -3.33 | 0.484 | False |
| 2026-09-02 16:13 | 5000 | -11.7 | 0.436 | -4.46 | 0.407 | False |
| 2026-09-02 20:11 | 5000 | -11.35 | 0.445 | -4.46 | 0.407 | False |
| 2026-09-03 00:32 | 5000 | -11.35 | 0.444 | -3.95 | 0.438 | False |
| 2026-09-03 05:15 | 5000 | -11.37 | 0.444 | -3.96 | 0.438 | False |
| 2026-09-03 08:16 | 5000 | -10.92 | 0.455 | -3.95 | 0.438 | False |
