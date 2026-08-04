# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-08-04 06:26_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-16.82%**, PF 0.492, 101 trades, max DD -2031.39
- Optimizer out-of-sample: net **-5.04%**, PF 0.478, 30 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-08-02 16:57 | 5000 | -16.98 | 0.477 | -5.5 | 0.415 | False |
| 2026-08-02 20:54 | 5000 | -16.94 | 0.479 | -5.65 | 0.415 | False |
| 2026-08-03 02:41 | 5000 | -17.75 | 0.465 | -7.09 | 0.259 | False |
| 2026-08-03 06:58 | 5000 | -17.75 | 0.465 | -7.09 | 0.259 | False |
| 2026-08-03 11:21 | 5000 | -16.13 | 0.504 | -4.45 | 0.526 | False |
| 2026-08-03 14:35 | 5000 | -16.16 | 0.504 | -4.46 | 0.527 | False |
| 2026-08-03 17:49 | 5000 | -16.16 | 0.504 | -4.5 | 0.525 | False |
| 2026-08-03 21:01 | 5000 | -16.26 | 0.502 | -3.92 | 0.561 | False |
| 2026-08-04 02:25 | 5000 | -16.62 | 0.496 | -5.04 | 0.478 | False |
| 2026-08-04 06:26 | 5000 | -16.82 | 0.492 | -5.04 | 0.478 | False |
