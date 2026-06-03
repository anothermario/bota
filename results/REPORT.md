# Finetune report — BTCUSDT 4h

_Last run (UTC): 2026-06-03 05:42_

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

- Current-params net profit (full sample): **-6.53%**, PF 0.578, 35 trades, max DD -969.81
- Optimizer out-of-sample: net **-5.34%**, PF 0.006, 10 trades
- Decision: **kept current params**

![equity curve](equity_curve.png)

## Recent runs

| time (UTC) | data bars | live net% | live PF | OOS net% | OOS PF | accepted |
|---|---|---|---|---|---|---|
| 2026-06-02 18:39 | 1500 | -6.21 | 0.601 | -5.34 | 0.006 | False |
| 2026-06-02 21:07 | 1500 | -6.27 | 0.597 | -5.34 | 0.006 | False |
| 2026-06-03 01:01 | 1500 | -6.03 | 0.614 | -5.34 | 0.006 | False |
| 2026-06-03 05:42 | 1500 | -6.53 | 0.578 | -5.34 | 0.006 | False |
