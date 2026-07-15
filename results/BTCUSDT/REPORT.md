# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-15 13:41_

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
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-7.3%**, PF 0.692, 65 trades, max DD -1303.27
- Optimizer out-of-sample: net **-4.07%**, PF 0.395, 21 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-14 02:24 | 5000 | -8.84 | 0.637 | -4.54 | 0.326 | False |
| 2026-07-14 06:10 | 5000 | -8.84 | 0.637 | -4.54 | 0.326 | False |
| 2026-07-14 09:57 | 5000 | -9.29 | 0.617 | -4.54 | 0.326 | False |
| 2026-07-14 13:40 | 5000 | -9.43 | 0.612 | -4.58 | 0.326 | False |
| 2026-07-14 17:13 | 5000 | -8.98 | 0.625 | -4.58 | 0.326 | False |
| 2026-07-14 20:59 | 5000 | -8.98 | 0.625 | -4.58 | 0.326 | False |
| 2026-07-15 02:22 | 5000 | -7.5 | 0.685 | -2.81 | 0.583 | False |
| 2026-07-15 06:12 | 5000 | -7.27 | 0.692 | -2.81 | 0.584 | False |
| 2026-07-15 10:01 | 5000 | -7.27 | 0.692 | -3.05 | 0.547 | False |
| 2026-07-15 13:41 | 5000 | -7.3 | 0.692 | -4.07 | 0.395 | False |
