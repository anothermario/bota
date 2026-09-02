# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-09-02 08:16_

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

- Current-params net profit (full sample): **-7.55%**, PF 0.657, 53 trades, max DD -962.23
- Optimizer out-of-sample: net **2.25%**, PF 1.327, 17 trades
- Decision: **PROMOTED new params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-31 20:11 | 5000 | -5.85 | 0.732 | 3.02 | 1.441 | True |
| 2026-09-01 00:37 | 5000 | -5.84 | 0.732 | 3.02 | 1.441 | True |
| 2026-09-01 04:13 | 5000 | -5.86 | 0.732 | 2.35 | 1.346 | True |
| 2026-09-01 08:17 | 5000 | -5.27 | 0.753 | 3.08 | 1.509 | True |
| 2026-09-01 12:17 | 5000 | -5.13 | 0.76 | 3.08 | 1.509 | True |
| 2026-09-01 16:33 | 5000 | -5.0 | 0.766 | 3.08 | 1.509 | True |
| 2026-09-01 20:11 | 5000 | -6.39 | 0.713 | 3.08 | 1.509 | True |
| 2026-09-02 00:31 | 5000 | -6.75 | 0.688 | 3.08 | 1.509 | True |
| 2026-09-02 04:15 | 5000 | -7.3 | 0.665 | 2.25 | 1.327 | True |
| 2026-09-02 08:16 | 5000 | -7.55 | 0.657 | 2.25 | 1.327 | True |
