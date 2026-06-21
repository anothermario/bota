# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-06-21 05:40_

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

- Current-params net profit (full sample): **-6.37%**, PF 0.685, 62 trades, max DD -680.48
- Optimizer out-of-sample: net **-4.67%**, PF 0.395, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-19 16:51 | 5000 | -7.08 | 0.658 | -5.01 | 0.376 | False |
| 2026-06-19 20:34 | 5000 | -7.07 | 0.658 | -4.09 | 0.427 | False |
| 2026-06-20 00:53 | 5000 | -6.9 | 0.666 | -4.13 | 0.427 | False |
| 2026-06-20 05:33 | 5000 | -6.48 | 0.68 | -4.46 | 0.406 | False |
| 2026-06-20 09:07 | 5000 | -6.48 | 0.68 | -4.46 | 0.406 | False |
| 2026-06-20 12:41 | 5000 | -5.92 | 0.7 | -4.46 | 0.406 | False |
| 2026-06-20 16:35 | 5000 | -5.92 | 0.7 | -4.46 | 0.406 | False |
| 2026-06-20 20:31 | 5000 | -5.92 | 0.7 | -4.45 | 0.406 | False |
| 2026-06-21 00:58 | 5000 | -5.92 | 0.7 | -4.22 | 0.42 | False |
| 2026-06-21 05:40 | 5000 | -6.37 | 0.685 | -4.67 | 0.395 | False |
