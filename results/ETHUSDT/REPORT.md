# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-27 00:19_

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

- Current-params net profit (full sample): **-11.24%**, PF 0.543, 74 trades, max DD -1322.28
- Optimizer out-of-sample: net **-6.16%**, PF 0.461, 24 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-25 12:11 | 5000 | -11.0 | 0.548 | -4.87 | 0.518 | False |
| 2026-11-25 16:09 | 5000 | -10.99 | 0.548 | -5.97 | 0.467 | False |
| 2026-11-25 20:07 | 5000 | -10.87 | 0.551 | -5.96 | 0.468 | False |
| 2026-11-26 00:18 | 5000 | -10.87 | 0.551 | -5.27 | 0.501 | False |
| 2026-11-26 04:08 | 5000 | -10.87 | 0.551 | -5.57 | 0.486 | False |
| 2026-11-26 08:10 | 5000 | -11.44 | 0.537 | -5.57 | 0.486 | False |
| 2026-11-26 12:10 | 5000 | -10.86 | 0.551 | -5.57 | 0.486 | False |
| 2026-11-26 16:08 | 5000 | -11.45 | 0.538 | -6.16 | 0.461 | False |
| 2026-11-26 20:07 | 5000 | -10.94 | 0.551 | -6.16 | 0.461 | False |
| 2026-11-27 00:19 | 5000 | -11.24 | 0.543 | -6.16 | 0.461 | False |
