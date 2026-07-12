# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-07-12 13:17_

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

- Current-params net profit (full sample): **-10.59%**, PF 0.592, 69 trades, max DD -1204.03
- Optimizer out-of-sample: net **-3.42%**, PF 0.38, 13 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-07-11 02:33 | 5000 | -11.49 | 0.548 | -5.22 | 0.128 | False |
| 2026-07-11 06:12 | 5000 | -11.43 | 0.55 | -4.73 | 0.141 | False |
| 2026-07-11 09:28 | 5000 | -11.43 | 0.55 | -4.73 | 0.141 | False |
| 2026-07-11 13:16 | 5000 | -11.46 | 0.55 | -4.41 | 0.151 | False |
| 2026-07-11 16:57 | 5000 | -12.8 | 0.519 | -5.51 | 0.129 | False |
| 2026-07-11 20:45 | 5000 | -12.5 | 0.526 | -5.5 | 0.13 | False |
| 2026-07-12 02:39 | 5000 | -11.31 | 0.571 | -3.32 | 0.392 | False |
| 2026-07-12 06:32 | 5000 | -10.49 | 0.592 | -3.38 | 0.38 | False |
| 2026-07-12 09:50 | 5000 | -11.03 | 0.579 | -3.38 | 0.38 | False |
| 2026-07-12 13:17 | 5000 | -10.59 | 0.592 | -3.42 | 0.38 | False |
