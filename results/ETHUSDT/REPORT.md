# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-06-10 05:36_

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
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-15.85%**, PF 0.387, 87 trades, max DD -1712.7
- Optimizer out-of-sample: net **-4.73%**, PF 0.509, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-09 16:58 | 5000 | -15.12 | 0.405 | -3.98 | 0.563 | False |
| 2026-06-09 20:44 | 5000 | -15.62 | 0.397 | -4.93 | 0.498 | False |
| 2026-06-10 00:55 | 5000 | -15.61 | 0.398 | -5.01 | 0.494 | False |
| 2026-06-10 05:36 | 5000 | -15.85 | 0.387 | -4.73 | 0.509 | False |
