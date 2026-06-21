# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-21 12:45_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-10.74%**, PF 0.613, 75 trades, max DD -1302.94
- Optimizer out-of-sample: net **0.63%**, PF 1.15, 14 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-20 00:53 | 5000 | -10.61 | 0.615 | 0.96 | 1.204 | True |
| 2026-06-20 05:33 | 5000 | -10.59 | 0.615 | 1.8 | 1.456 | False |
| 2026-06-20 09:08 | 5000 | -10.59 | 0.615 | 1.68 | 1.426 | False |
| 2026-06-20 12:41 | 5000 | -11.67 | 0.589 | 1.11 | 1.282 | False |
| 2026-06-20 16:35 | 5000 | -10.64 | 0.614 | 0.92 | 1.236 | False |
| 2026-06-20 20:32 | 5000 | -11.36 | 0.597 | 0.9 | 1.236 | False |
| 2026-06-21 00:59 | 5000 | -11.41 | 0.597 | 0.08 | 1.018 | False |
| 2026-06-21 05:41 | 5000 | -11.34 | 0.599 | -0.05 | 0.99 | False |
| 2026-06-21 09:19 | 5000 | -10.74 | 0.613 | 0.64 | 1.153 | False |
| 2026-06-21 12:45 | 5000 | -10.74 | 0.613 | 0.63 | 1.15 | False |
