# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-26 00:18_

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

- Current-params net profit (full sample): **-10.87%**, PF 0.551, 74 trades, max DD -1264.6
- Optimizer out-of-sample: net **-5.27%**, PF 0.501, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-24 12:11 | 5000 | -11.0 | 0.548 | -5.96 | 0.465 | False |
| 2026-11-24 16:08 | 5000 | -10.93 | 0.551 | -5.45 | 0.489 | False |
| 2026-11-24 20:07 | 5000 | -11.0 | 0.548 | -5.44 | 0.489 | False |
| 2026-11-25 00:19 | 5000 | -11.0 | 0.548 | -4.87 | 0.518 | False |
| 2026-11-25 04:09 | 5000 | -11.0 | 0.548 | -4.87 | 0.518 | False |
| 2026-11-25 08:10 | 5000 | -11.0 | 0.548 | -5.83 | 0.47 | False |
| 2026-11-25 12:11 | 5000 | -11.0 | 0.548 | -4.87 | 0.518 | False |
| 2026-11-25 16:09 | 5000 | -10.99 | 0.548 | -5.97 | 0.467 | False |
| 2026-11-25 20:07 | 5000 | -10.87 | 0.551 | -5.96 | 0.468 | False |
| 2026-11-26 00:18 | 5000 | -10.87 | 0.551 | -5.27 | 0.501 | False |
