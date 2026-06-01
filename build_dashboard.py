"""
build_dashboard.py
==================
Renders a single self-contained docs/index.html for GitHub Pages.
No external JS/CSS/CDN — everything (including the equity curve, drawn as inline
SVG) is embedded, so the page works the instant Pages serves it.

Called at the end of run_cycle.py. Inputs are plain dicts/lists already in memory,
so this never re-runs the backtest.
"""
import datetime as dt
import html
import json


def _fmt(x, suffix="", dash="–"):
    if x is None:
        return dash
    if isinstance(x, float):
        return f"{x:,.2f}{suffix}"
    return f"{x}{suffix}"


def _equity_svg(curve, w=920, h=240, pad=8):
    """Tiny dependency-free line chart of the equity curve."""
    if not curve or len(curve) < 2:
        return '<div class="muted">No equity data yet.</div>'
    lo, hi = min(curve), max(curve)
    rng = (hi - lo) or 1.0
    n = len(curve)
    pts = []
    for i, v in enumerate(curve):
        x = pad + (w - 2 * pad) * (i / (n - 1))
        y = pad + (h - 2 * pad) * (1 - (v - lo) / rng)
        pts.append(f"{x:.1f},{y:.1f}")
    line = " ".join(pts)
    base_y = pad + (h - 2 * pad) * (1 - (curve[0] - lo) / rng)
    area = f"{pad:.1f},{h - pad:.1f} " + line + f" {w - pad:.1f},{h - pad:.1f}"
    up = curve[-1] >= curve[0]
    stroke = "#34d399" if up else "#f87171"
    fill = "rgba(52,211,153,0.12)" if up else "rgba(248,113,113,0.12)"
    return f'''<svg viewBox="0 0 {w} {h}" width="100%" preserveAspectRatio="none" role="img" aria-label="Equity curve">
      <polyline points="{area}" fill="{fill}" stroke="none"/>
      <line x1="{pad}" y1="{base_y:.1f}" x2="{w - pad}" y2="{base_y:.1f}" stroke="rgba(255,255,255,0.18)" stroke-dasharray="4 4"/>
      <polyline points="{line}" fill="none" stroke="{stroke}" stroke-width="2" stroke-linejoin="round"/>
    </svg>'''


def _metric_card(label, value, tone="neutral"):
    color = {"pos": "#34d399", "neg": "#f87171", "neutral": "#e5e7eb"}[tone]
    return f'''<div class="card">
      <div class="card-label">{html.escape(label)}</div>
      <div class="card-value" style="color:{color}">{value}</div>
    </div>'''


def _trade_rows(trades):
    if not trades:
        return '<tr><td colspan="6" class="muted" style="text-align:center;padding:24px">No trades in this window.</td></tr>'
    rows = []
    for i, t in enumerate(reversed(trades), 1):  # newest first
        pnl = t["pnl"]
        cls = "pos" if pnl >= 0 else "neg"
        side = "LONG" if t["side"] == "L" else "SHORT"
        side_cls = "long" if t["side"] == "L" else "short"
        rows.append(
            f'<tr>'
            f'<td class="muted">{i}</td>'
            f'<td><span class="pill {side_cls}">{side}</span></td>'
            f'<td>{html.escape(str(t.get("entry_time") or "–"))}</td>'
            f'<td>{html.escape(str(t.get("exit_time") or "–"))}</td>'
            f'<td class="num">{t["entry"]:,.2f} → {t["exit"]:,.2f}</td>'
            f'<td class="num {cls}">{pnl:+,.2f}</td>'
            f'</tr>'
        )
    return "\n".join(rows)


def build_html(*, symbol, interval, params, live, window_metrics, window_trades,
               months, accepted, oos, generated_utc, repo_url=None):
    net_tone = "pos" if (live.get("net_profit_pct") or 0) >= 0 else "neg"
    wnet_tone = "pos" if (window_metrics.get("net") or 0) >= 0 else "neg"
    decision = "Promoted new params" if accepted else "Kept current params"
    decision_tone = "pos" if accepted else "neutral"

    repo_link = f'<a href="{html.escape(repo_url)}" target="_blank" rel="noopener">repository ↗</a>' if repo_url else ""

    cards = "".join([
        _metric_card("Net profit (full sample)", _fmt(live.get("net_profit_pct"), "%"), net_tone),
        _metric_card("Profit factor", _fmt(live.get("profit_factor")), "neutral"),
        _metric_card("Total trades", _fmt(live.get("total_trades")), "neutral"),
        _metric_card("Win rate", _fmt(live.get("win_rate_pct"), "%"), "neutral"),
        _metric_card("Max drawdown", _fmt(live.get("max_drawdown")), "neg"),
        _metric_card("Sharpe-like", _fmt(live.get("sharpe_like")), "neutral"),
    ])

    win_cards = "".join([
        _metric_card(f"Net P&L (last {months}m)", _fmt(window_metrics.get("net")), wnet_tone),
        _metric_card(f"Trades (last {months}m)", _fmt(window_metrics.get("count")), "neutral"),
        _metric_card(f"Win rate (last {months}m)", _fmt(window_metrics.get("win_rate"), "%"), "neutral"),
    ])

    params_json = html.escape(json.dumps(params, indent=2))
    equity = _equity_svg(live.get("equity_curve") or [])
    trade_rows = _trade_rows(window_trades)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="900">
<title>KAMA Trend Bot — {html.escape(symbol)} {html.escape(interval)}</title>
<style>
  :root {{
    --bg:#0b0f17; --panel:#121826; --panel2:#0f1420; --line:#1f2937;
    --text:#e5e7eb; --muted:#8b95a7; --accent:#60a5fa;
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text);
    font:15px/1.5 ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,sans-serif; }}
  .wrap {{ max-width:980px; margin:0 auto; padding:28px 18px 64px; }}
  header {{ display:flex; flex-wrap:wrap; align-items:baseline; gap:10px 16px; margin-bottom:6px; }}
  h1 {{ font-size:22px; margin:0; letter-spacing:.2px; }}
  .sym {{ color:var(--accent); font-weight:600; }}
  .sub {{ color:var(--muted); font-size:13px; margin:0 0 22px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; }}
  .card {{ background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:14px 16px; }}
  .card-label {{ color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:.5px; }}
  .card-value {{ font-size:22px; font-weight:600; margin-top:6px; }}
  section {{ margin-top:28px; }}
  h2 {{ font-size:14px; text-transform:uppercase; letter-spacing:.6px; color:var(--muted);
    border-bottom:1px solid var(--line); padding-bottom:8px; margin:0 0 14px; }}
  .panel {{ background:var(--panel2); border:1px solid var(--line); border-radius:12px; padding:14px; }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; }}
  th, td {{ text-align:left; padding:9px 10px; border-bottom:1px solid var(--line); }}
  th {{ color:var(--muted); font-weight:500; font-size:12px; text-transform:uppercase; letter-spacing:.4px; }}
  td.num {{ font-variant-numeric:tabular-nums; }}
  .pos {{ color:#34d399; }} .neg {{ color:#f87171; }} .muted {{ color:var(--muted); }}
  .pill {{ display:inline-block; padding:2px 8px; border-radius:999px; font-size:12px; font-weight:600; }}
  .pill.long {{ background:rgba(52,211,153,.14); color:#34d399; }}
  .pill.short {{ background:rgba(248,113,113,.14); color:#f87171; }}
  pre {{ margin:0; white-space:pre-wrap; color:#cbd5e1; font-size:13px;
    background:var(--panel2); border:1px solid var(--line); border-radius:12px; padding:14px; }}
  .badge {{ display:inline-block; padding:4px 10px; border-radius:8px; font-size:13px; font-weight:600; }}
  .badge.pos {{ background:rgba(52,211,153,.14); color:#34d399; }}
  .badge.neutral {{ background:rgba(148,163,184,.14); color:#cbd5e1; }}
  .scroll {{ max-height:520px; overflow:auto; border:1px solid var(--line); border-radius:12px; }}
  .scroll table th {{ position:sticky; top:0; background:var(--panel); }}
  footer {{ margin-top:40px; color:var(--muted); font-size:12px; line-height:1.7; }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>Adaptive KAMA Trend-Follower</h1>
    <span class="sym">{html.escape(symbol)} · {html.escape(interval)}</span>
  </header>
  <p class="sub">
    Last cycle (UTC): {html.escape(generated_utc)} · auto-refreshes every 15 min ·
    decision: <span class="badge {decision_tone}">{decision}</span>
    {(" · OOS net " + _fmt(oos.get("net_profit_pct"), "%") + ", PF " + _fmt(oos.get("profit_factor"))) if oos else ""}
    {(" · " + repo_link) if repo_link else ""}
  </p>

  <section>
    <h2>Performance (current live params, full sample)</h2>
    <div class="grid">{cards}</div>
  </section>

  <section>
    <h2>Equity curve</h2>
    <div class="panel">{equity}</div>
  </section>

  <section>
    <h2>Last {months} months</h2>
    <div class="grid">{win_cards}</div>
  </section>

  <section>
    <h2>Trades — last {months} months ({len(window_trades)})</h2>
    <div class="scroll">
      <table>
        <thead><tr><th>#</th><th>Side</th><th>Entry time</th><th>Exit time</th><th>Entry → Exit</th><th>P&amp;L</th></tr></thead>
        <tbody>{trade_rows}</tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Current parameters</h2>
    <pre>{params_json}</pre>
  </section>

  <footer>
    Backtest includes 0.04% per-fill fees. Figures are simulated on historical OHLCV and
    are not a live brokerage statement. Past results do not guarantee future returns.
    This page is not financial advice.
  </footer>
</div>
</body>
</html>"""
