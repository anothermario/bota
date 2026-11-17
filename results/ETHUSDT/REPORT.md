# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-11-17 12:10_

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

- Current-params net profit (full sample): **-12.37%**, PF 0.49, 77 trades, max DD -1415.57
- Optimizer out-of-sample: net **-2.95%**, PF 0.692, 27 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-11-16 00:24 | 5000 | -12.41 | 0.487 | -1.73 | 0.794 | False |
| 2026-11-16 04:09 | 5000 | -12.4 | 0.487 | -2.01 | 0.767 | False |
| 2026-11-16 08:22 | 5000 | -11.5 | 0.509 | -1.73 | 0.794 | False |
| 2026-11-16 12:14 | 5000 | -11.5 | 0.509 | -1.5 | 0.816 | False |
| 2026-11-16 16:08 | 5000 | -11.5 | 0.509 | -1.5 | 0.816 | False |
| 2026-11-16 20:07 | 5000 | -11.5 | 0.509 | -1.5 | 0.817 | False |
| 2026-11-17 00:19 | 5000 | -11.5 | 0.509 | -1.5 | 0.816 | False |
| 2026-11-17 04:08 | 5000 | -11.5 | 0.509 | -1.5 | 0.817 | False |
| 2026-11-17 08:09 | 5000 | -11.88 | 0.5 | -2.36 | 0.739 | False |
| 2026-11-17 12:10 | 5000 | -12.37 | 0.49 | -2.95 | 0.692 | False |
