# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-21 08:09_

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

- Current-params net profit (full sample): **-8.18%**, PF 0.651, 72 trades, max DD -1174.06
- Optimizer out-of-sample: net **1.05%**, PF 1.154, 17 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-19 20:07 | 5000 | -8.59 | 0.638 | 1.43 | 1.173 | True |
| 2026-11-20 00:17 | 5000 | -8.6 | 0.638 | 3.58 | 1.512 | True |
| 2026-11-20 04:08 | 5000 | -8.52 | 0.641 | 2.84 | 1.409 | True |
| 2026-11-20 08:10 | 5000 | -8.52 | 0.641 | 2.84 | 1.409 | True |
| 2026-11-20 12:10 | 5000 | -8.92 | 0.629 | 2.28 | 1.304 | True |
| 2026-11-20 16:07 | 5000 | -8.74 | 0.623 | 2.83 | 1.409 | True |
| 2026-11-20 20:07 | 5000 | -8.21 | 0.65 | 3.21 | 1.462 | True |
| 2026-11-21 00:19 | 5000 | -8.17 | 0.651 | 4.17 | 1.592 | True |
| 2026-11-21 04:07 | 5000 | -8.19 | 0.651 | 1.05 | 1.156 | True |
| 2026-11-21 08:09 | 5000 | -8.18 | 0.651 | 1.05 | 1.154 | True |
