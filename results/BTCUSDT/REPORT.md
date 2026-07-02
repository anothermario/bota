# Finetune report -- BTCUSDT 15m

_Last run (UTC): 2026-07-02 21:05_

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

- Current-params net profit (full sample): **-4.26%**, PF 0.811, 65 trades, max DD -861.49
- Optimizer out-of-sample: net **-3.12%**, PF 0.583, 19 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-01 09:12 | 5000 | -4.57 | 0.795 | -4.9 | 0.437 | False |
| 2026-07-01 13:01 | 5000 | -4.59 | 0.794 | -4.92 | 0.436 | False |
| 2026-07-01 16:49 | 5000 | -4.23 | 0.809 | -4.11 | 0.484 | False |
| 2026-07-01 20:37 | 5000 | -4.23 | 0.809 | -4.12 | 0.483 | False |
| 2026-07-02 00:50 | 5000 | -3.72 | 0.831 | -2.96 | 0.595 | False |
| 2026-07-02 07:31 | 5000 | -3.72 | 0.831 | -2.96 | 0.595 | False |
| 2026-07-02 10:38 | 5000 | -3.72 | 0.831 | -2.96 | 0.595 | False |
| 2026-07-02 13:58 | 5000 | -3.75 | 0.831 | -2.98 | 0.596 | False |
| 2026-07-02 17:46 | 5000 | -4.57 | 0.8 | -3.65 | 0.543 | False |
| 2026-07-02 21:05 | 5000 | -4.26 | 0.811 | -3.12 | 0.583 | False |
