# Finetune report -- ETCUSDT 15m

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

- Current-params net profit (full sample): **-15.14%**, PF 0.486, 83 trades, max DD -1567.39
- Optimizer out-of-sample: net **-5.34%**, PF 0.363, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-09 16:58 | 5000 | -15.55 | 0.478 | -5.61 | 0.35 | False |
| 2026-06-09 20:44 | 5000 | -15.52 | 0.479 | -6.91 | 0.301 | False |
| 2026-06-10 00:56 | 5000 | -15.15 | 0.486 | -5.35 | 0.362 | False |
| 2026-06-10 05:36 | 5000 | -15.14 | 0.486 | -5.34 | 0.363 | False |
