# Finetune report -- ETCUSDT 15m

_Last run (UTC): 2026-06-09 20:44_

## Current params (live)

```json
{
  "er_len": 20,
  "kama_fast": 2,
  "kama_slow": 30,
  "er_thresh": 0.3,
  "use_adx": true,
  "adx_len": 14,
  "adx_thresh": 20.0,
  "don_len": 20,
  "atr_len": 14,
  "atr_mult": 3.0,
  "chand_len": 22,
  "risk_pct": 1.0,
  "allow_short": true
}
```

## Latest cycle

- Current-params net profit (full sample): **-15.52%**, PF 0.479, 84 trades, max DD -1566.47
- Optimizer out-of-sample: net **-6.91%**, PF 0.301, 23 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-09 16:58 | 5000 | -15.55 | 0.478 | -5.61 | 0.35 | False |
| 2026-06-09 20:44 | 5000 | -15.52 | 0.479 | -6.91 | 0.301 | False |
