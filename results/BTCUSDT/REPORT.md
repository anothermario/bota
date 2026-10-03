# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-10-03 04:17_

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

- Current-params net profit (full sample): **-11.27%**, PF 0.527, 69 trades, max DD -1278.28
- Optimizer out-of-sample: net **-4.07%**, PF 0.607, 31 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-01 16:12 | 5000 | -10.35 | 0.543 | -3.17 | 0.624 | False |
| 2026-10-01 20:13 | 5000 | -10.38 | 0.543 | -3.21 | 0.624 | False |
| 2026-10-02 00:33 | 5000 | -10.82 | 0.533 | -3.6 | 0.594 | False |
| 2026-10-02 04:14 | 5000 | -10.85 | 0.533 | -3.64 | 0.594 | False |
| 2026-10-02 08:16 | 5000 | -11.44 | 0.52 | -4.23 | 0.565 | False |
| 2026-10-02 12:18 | 5000 | -12.08 | 0.503 | -4.23 | 0.565 | False |
| 2026-10-02 16:12 | 5000 | -11.48 | 0.518 | -4.23 | 0.565 | False |
| 2026-10-02 20:11 | 5000 | -11.51 | 0.518 | -4.27 | 0.565 | False |
| 2026-10-03 00:30 | 5000 | -11.25 | 0.527 | -3.93 | 0.596 | False |
| 2026-10-03 04:17 | 5000 | -11.27 | 0.527 | -4.07 | 0.607 | False |
