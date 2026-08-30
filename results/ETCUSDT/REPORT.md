# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-08-30 20:10_

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

- Current-params net profit (full sample): **-5.38%**, PF 0.748, 53 trades, max DD -944.37
- Optimizer out-of-sample: net **3.06%**, PF 1.454, 18 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-29 08:13 | 5000 | -3.58 | 0.817 | 5.5 | 2.143 | True |
| 2026-08-29 12:15 | 5000 | -3.58 | 0.817 | 5.02 | 2.048 | True |
| 2026-08-29 16:11 | 5000 | -3.58 | 0.817 | 5.02 | 2.048 | True |
| 2026-08-29 20:10 | 5000 | -4.55 | 0.778 | 3.97 | 1.678 | True |
| 2026-08-30 00:34 | 5000 | -4.55 | 0.778 | 4.55 | 1.773 | True |
| 2026-08-30 04:13 | 5000 | -4.55 | 0.778 | 4.55 | 1.773 | True |
| 2026-08-30 08:13 | 5000 | -4.78 | 0.771 | 3.72 | 1.622 | True |
| 2026-08-30 12:15 | 5000 | -5.38 | 0.748 | 3.06 | 1.454 | True |
| 2026-08-30 16:11 | 5000 | -5.38 | 0.748 | 3.06 | 1.454 | True |
| 2026-08-30 20:10 | 5000 | -5.38 | 0.748 | 3.06 | 1.454 | True |
