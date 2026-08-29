# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-29 20:10_

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

- Current-params net profit (full sample): **-4.55%**, PF 0.778, 51 trades, max DD -944.37
- Optimizer out-of-sample: net **3.97%**, PF 1.678, 16 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-28 06:36 | 5000 | -2.55 | 0.862 | 6.46 | 2.757 | False |
| 2026-08-28 11:54 | 5000 | -2.55 | 0.862 | 5.47 | 2.197 | True |
| 2026-08-28 16:11 | 5000 | -3.41 | 0.824 | 5.52 | 2.195 | True |
| 2026-08-28 21:58 | 5000 | -3.58 | 0.817 | 5.33 | 2.11 | True |
| 2026-08-29 00:28 | 5000 | -3.58 | 0.817 | 5.33 | 2.11 | True |
| 2026-08-29 04:12 | 5000 | -3.58 | 0.817 | 5.5 | 2.143 | True |
| 2026-08-29 08:13 | 5000 | -3.58 | 0.817 | 5.5 | 2.143 | True |
| 2026-08-29 12:15 | 5000 | -3.58 | 0.817 | 5.02 | 2.048 | True |
| 2026-08-29 16:11 | 5000 | -3.58 | 0.817 | 5.02 | 2.048 | True |
| 2026-08-29 20:10 | 5000 | -4.55 | 0.778 | 3.97 | 1.678 | True |
