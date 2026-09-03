# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-03 08:16_

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

- Current-params net profit (full sample): **-6.42%**, PF 0.695, 52 trades, max DD -851.5
- Optimizer out-of-sample: net **1.26%**, PF 1.186, 16 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-09-01 20:11 | 5000 | -6.39 | 0.713 | 3.08 | 1.509 | True |
| 2026-09-02 00:31 | 5000 | -6.75 | 0.688 | 3.08 | 1.509 | True |
| 2026-09-02 04:15 | 5000 | -7.3 | 0.665 | 2.25 | 1.327 | True |
| 2026-09-02 08:16 | 5000 | -7.55 | 0.657 | 2.25 | 1.327 | True |
| 2026-09-02 12:18 | 5000 | -7.52 | 0.665 | 1.26 | 1.186 | True |
| 2026-09-02 16:13 | 5000 | -7.29 | 0.666 | 1.26 | 1.186 | True |
| 2026-09-02 20:11 | 5000 | -6.75 | 0.684 | 1.26 | 1.186 | True |
| 2026-09-03 00:32 | 5000 | -6.75 | 0.684 | 1.26 | 1.186 | True |
| 2026-09-03 05:15 | 5000 | -6.28 | 0.7 | 1.26 | 1.185 | True |
| 2026-09-03 08:16 | 5000 | -6.42 | 0.695 | 1.26 | 1.186 | True |
