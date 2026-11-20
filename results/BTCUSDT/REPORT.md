# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-20 04:08_

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

- Current-params net profit (full sample): **-8.52%**, PF 0.641, 71 trades, max DD -1205.71
- Optimizer out-of-sample: net **2.84%**, PF 1.409, 17 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-18 16:07 | 5000 | -7.85 | 0.66 | 2.89 | 1.423 | True |
| 2026-11-18 20:07 | 5000 | -7.9 | 0.658 | 2.84 | 1.406 | True |
| 2026-11-19 00:19 | 5000 | -9.1 | 0.622 | 1.95 | 1.247 | True |
| 2026-11-19 04:08 | 5000 | -8.83 | 0.63 | 1.88 | 1.237 | True |
| 2026-11-19 08:10 | 5000 | -8.82 | 0.63 | 1.94 | 1.249 | True |
| 2026-11-19 12:10 | 5000 | -8.48 | 0.629 | 2.39 | 1.328 | True |
| 2026-11-19 16:08 | 5000 | -7.97 | 0.656 | 2.42 | 1.338 | True |
| 2026-11-19 20:07 | 5000 | -8.59 | 0.638 | 1.43 | 1.173 | True |
| 2026-11-20 00:17 | 5000 | -8.6 | 0.638 | 3.58 | 1.512 | True |
| 2026-11-20 04:08 | 5000 | -8.52 | 0.641 | 2.84 | 1.409 | True |
