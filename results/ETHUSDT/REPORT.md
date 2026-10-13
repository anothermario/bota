# Finetune report -- ETHUSDT 15m

_Last run (UTC): 2026-10-13 00:35_

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

- Current-params net profit (full sample): **-16.07%**, PF 0.479, 101 trades, max DD -1614.18
- Optimizer out-of-sample: net **-5.95%**, PF 0.204, 22 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-10-11 12:17 | 5000 | -14.25 | 0.52 | -5.56 | 0.213 | False |
| 2026-10-11 16:12 | 5000 | -14.28 | 0.52 | -5.6 | 0.213 | False |
| 2026-10-11 20:12 | 5000 | -14.45 | 0.517 | -6.19 | 0.195 | False |
| 2026-10-12 00:38 | 5000 | -14.65 | 0.513 | -6.18 | 0.195 | False |
| 2026-10-12 04:21 | 5000 | -15.73 | 0.486 | -6.21 | 0.195 | False |
| 2026-10-12 08:30 | 5000 | -15.39 | 0.493 | -6.24 | 0.195 | False |
| 2026-10-12 12:25 | 5000 | -15.26 | 0.508 | -6.4 | 0.191 | False |
| 2026-10-12 16:12 | 5000 | -15.36 | 0.506 | -6.66 | 0.216 | False |
| 2026-10-12 20:12 | 5000 | -16.06 | 0.479 | -5.95 | 0.204 | False |
| 2026-10-13 00:35 | 5000 | -16.07 | 0.479 | -5.95 | 0.204 | False |
