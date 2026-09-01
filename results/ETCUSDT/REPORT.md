# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-01 08:17_

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

- Current-params net profit (full sample): **-5.27%**, PF 0.753, 53 trades, max DD -950.14
- Optimizer out-of-sample: net **3.08%**, PF 1.509, 16 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-30 20:10 | 5000 | -5.38 | 0.748 | 3.06 | 1.454 | True |
| 2026-08-31 00:34 | 5000 | -5.4 | 0.748 | 3.05 | 1.454 | True |
| 2026-08-31 04:15 | 5000 | -5.85 | 0.732 | 2.56 | 1.352 | True |
| 2026-08-31 08:18 | 5000 | -5.85 | 0.732 | 2.56 | 1.353 | True |
| 2026-08-31 12:18 | 5000 | -5.85 | 0.732 | 3.02 | 1.441 | True |
| 2026-08-31 16:12 | 5000 | -5.85 | 0.732 | 3.02 | 1.441 | True |
| 2026-08-31 20:11 | 5000 | -5.85 | 0.732 | 3.02 | 1.441 | True |
| 2026-09-01 00:37 | 5000 | -5.84 | 0.732 | 3.02 | 1.441 | True |
| 2026-09-01 04:13 | 5000 | -5.86 | 0.732 | 2.35 | 1.346 | True |
| 2026-09-01 08:17 | 5000 | -5.27 | 0.753 | 3.08 | 1.509 | True |
