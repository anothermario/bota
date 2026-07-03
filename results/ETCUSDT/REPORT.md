# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-03 02:53_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.25,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 15,
  "atr_len": 14,
  "atr_mult": 3.5,
  "chand_len": 18,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-12.43%**, PF 0.567, 80 trades, max DD -1322.06
- Optimizer out-of-sample: net **-6.97%**, PF 0.269, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-01 13:01 | 5000 | -10.0 | 0.657 | -6.85 | 0.272 | False |
| 2026-07-01 16:50 | 5000 | -10.4 | 0.642 | -5.15 | 0.442 | False |
| 2026-07-01 20:37 | 5000 | -10.4 | 0.642 | -4.55 | 0.474 | False |
| 2026-07-02 00:51 | 5000 | -10.4 | 0.642 | -3.88 | 0.516 | False |
| 2026-07-02 07:31 | 5000 | -10.39 | 0.642 | -5.45 | 0.427 | False |
| 2026-07-02 10:38 | 5000 | -10.13 | 0.652 | -5.35 | 0.432 | False |
| 2026-07-02 13:58 | 5000 | -10.19 | 0.651 | -4.92 | 0.455 | False |
| 2026-07-02 17:46 | 5000 | -10.39 | 0.646 | -5.14 | 0.443 | False |
| 2026-07-02 21:05 | 5000 | -10.48 | 0.643 | -7.77 | 0.246 | False |
| 2026-07-03 02:53 | 5000 | -12.43 | 0.567 | -6.97 | 0.269 | False |
