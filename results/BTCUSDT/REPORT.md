# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-11-25 04:09_

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

- Current-params net profit (full sample): **-6.69%**, PF 0.713, 71 trades, max DD -1038.63
- Optimizer out-of-sample: net **3.55%**, PF 1.569, 18 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-23 16:07 | 5000 | -6.18 | 0.728 | 1.9 | 1.256 | True |
| 2026-11-23 20:06 | 5000 | -6.2 | 0.728 | 1.89 | 1.256 | True |
| 2026-11-24 00:18 | 5000 | -6.19 | 0.728 | 2.03 | 1.279 | True |
| 2026-11-24 04:09 | 5000 | -6.19 | 0.728 | 2.02 | 1.278 | True |
| 2026-11-24 08:10 | 5000 | -5.95 | 0.738 | 2.83 | 1.416 | True |
| 2026-11-24 12:11 | 5000 | -6.52 | 0.72 | 2.08 | 1.274 | True |
| 2026-11-24 16:08 | 5000 | -6.52 | 0.72 | 2.08 | 1.275 | True |
| 2026-11-24 20:07 | 5000 | -6.52 | 0.72 | 2.67 | 1.381 | True |
| 2026-11-25 00:19 | 5000 | -6.52 | 0.72 | 2.63 | 1.373 | True |
| 2026-11-25 04:09 | 5000 | -6.69 | 0.713 | 3.55 | 1.569 | True |
