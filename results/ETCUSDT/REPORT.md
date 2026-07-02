# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-02 07:31_

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

- Current-params net profit (full sample): **-10.39%**, PF 0.642, 79 trades, max DD -1322.42
- Optimizer out-of-sample: net **-5.45%**, PF 0.427, 20 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-30 16:47 | 5000 | -9.64 | 0.665 | -2.56 | 0.689 | False |
| 2026-06-30 20:42 | 5000 | -9.5 | 0.669 | -2.26 | 0.728 | False |
| 2026-07-01 00:54 | 5000 | -9.5 | 0.669 | -4.56 | 0.472 | False |
| 2026-07-01 05:36 | 5000 | -9.79 | 0.665 | -5.13 | 0.443 | False |
| 2026-07-01 09:13 | 5000 | -9.85 | 0.662 | -7.39 | 0.256 | False |
| 2026-07-01 13:01 | 5000 | -10.0 | 0.657 | -6.85 | 0.272 | False |
| 2026-07-01 16:50 | 5000 | -10.4 | 0.642 | -5.15 | 0.442 | False |
| 2026-07-01 20:37 | 5000 | -10.4 | 0.642 | -4.55 | 0.474 | False |
| 2026-07-02 00:51 | 5000 | -10.4 | 0.642 | -3.88 | 0.516 | False |
| 2026-07-02 07:31 | 5000 | -10.39 | 0.642 | -5.45 | 0.427 | False |
