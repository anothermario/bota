# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-19 00:19_

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
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 26,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-9.1%**, PF 0.622, 72 trades, max DD -1315.66
- Optimizer out-of-sample: net **1.95%**, PF 1.247, 21 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-17 12:10 | 5000 | -7.53 | 0.668 | 1.98 | 1.257 | True |
| 2026-11-17 16:08 | 5000 | -7.53 | 0.668 | 2.13 | 1.281 | True |
| 2026-11-17 20:07 | 5000 | -7.53 | 0.668 | 2.16 | 1.287 | True |
| 2026-11-18 00:19 | 5000 | -7.56 | 0.668 | 2.52 | 1.355 | True |
| 2026-11-18 04:08 | 5000 | -7.93 | 0.656 | 2.1 | 1.276 | True |
| 2026-11-18 08:10 | 5000 | -7.66 | 0.665 | 1.57 | 1.193 | True |
| 2026-11-18 12:10 | 5000 | -7.66 | 0.665 | 1.59 | 1.196 | True |
| 2026-11-18 16:07 | 5000 | -7.85 | 0.66 | 2.89 | 1.423 | True |
| 2026-11-18 20:07 | 5000 | -7.9 | 0.658 | 2.84 | 1.406 | True |
| 2026-11-19 00:19 | 5000 | -9.1 | 0.622 | 1.95 | 1.247 | True |
