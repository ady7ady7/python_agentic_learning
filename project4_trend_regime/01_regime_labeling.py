"""
Step 1: build M15 and H1 candles from M5 data, compute EMA144/EMA33 on high and low
separately, classify each timeframe into a trend regime, and plot for visual sanity check.

No target/pullback logic yet - this is purely about getting the regime label right before
building anything on top of it.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

RECROSS_WINDOW = 5   # candles - how long the "just crossed" uncertainty zone lasts

# ---------------------------------------------------------------- load
df = pd.read_csv("../xauusd_m5_et.csv", parse_dates=["et_time"])
df = df.set_index("et_time").sort_index()
df = df[["open", "high", "low", "close"]]

print(f"m5 rows: {len(df):,}  range: {df.index.min()} -> {df.index.max()}")


# ---------------------------------------------------------------- resample
def resample_ohlc(m5: pd.DataFrame, rule: str) -> pd.DataFrame:
    out = m5.resample(rule).agg(
        {"open": "first", "high": "max", "low": "min", "close": "last"}
    )
    return out.dropna()


m15 = resample_ohlc(df, "15min")
h1 = resample_ohlc(df, "1h")
print(f"m15 rows: {len(m15):,}   h1 rows: {len(h1):,}")


# ---------------------------------------------------------------- EMAs + ATR
def add_emas_and_atr(d: pd.DataFrame) -> pd.DataFrame:
    d = d.copy()
    d["ema144_high"] = d["high"].ewm(span=144, adjust=False).mean()
    d["ema144_low"] = d["low"].ewm(span=144, adjust=False).mean()
    d["ema33_high"] = d["high"].ewm(span=33, adjust=False).mean()
    d["ema33_low"] = d["low"].ewm(span=33, adjust=False).mean()

    tr = pd.concat([
        d["high"] - d["low"],
        (d["high"] - d["close"].shift(1)).abs(),
        (d["low"] - d["close"].shift(1)).abs(),
    ], axis=1).max(axis=1)
    d["atr14"] = tr.ewm(span=14, adjust=False).mean()
    return d


m15 = add_emas_and_atr(m15)
h1 = add_emas_and_atr(h1)


# ---------------------------------------------------------------- regime classification
def classify_regime(d: pd.DataFrame, recross_window: int = RECROSS_WINDOW) -> pd.DataFrame:
    d = d.copy()

    ema33_mid = (d["ema33_high"] + d["ema33_low"]) / 2
    ema144_mid = (d["ema144_high"] + d["ema144_low"]) / 2
    sign = np.sign(ema33_mid - ema144_mid)
    crossed = sign != sign.shift(1)
    # bars_since_recross: 0 on the crossing bar itself, counts up after
    bars_since_recross = pd.Series(np.nan, index=d.index)
    last_cross = None
    counts = []
    n = 0
    for c in crossed.values:
        if c:
            n = 0
        else:
            n += 1
        counts.append(n)
    d["bars_since_recross"] = counts
    in_recross_zone = d["bars_since_recross"] < recross_window

    # simplified two-zone definition: no separate midpoint threshold, which removed two
    # gaps (a strip between the midpoint and the strong-trend boundary, and the strip
    # physically inside the EMA144 channel). "retracement" is now just "everything on the
    # trend's side of EMA144 that isn't a strong trend and isn't a fresh recross".
    strong_bull = (d["close"] > d["ema144_high"]) & (d["close"] > d["ema33_low"])
    strong_bear = (d["close"] < d["ema144_low"]) & (d["close"] < d["ema33_high"])

    above_ema144_low = d["close"] > d["ema144_low"]     # bullish side of the channel or inside it
    below_ema144_high = d["close"] < d["ema144_high"]   # bearish side of the channel or inside it

    retr_bull = above_ema144_low & ~strong_bull & (sign > 0)
    retr_bear = below_ema144_high & ~strong_bear & (sign < 0)

    regime = pd.Series("undefined", index=d.index, dtype="object")
    regime[strong_bull] = "strong_bull"
    regime[strong_bear] = "strong_bear"
    regime[retr_bull] = "retracement_bull"
    regime[retr_bear] = "retracement_bear"
    regime[in_recross_zone] = "range_recross"   # overrides trend labels near a cross

    d["regime"] = regime
    return d


m15 = classify_regime(m15)
h1 = classify_regime(h1)

print("\nH1 regime distribution:")
print(h1["regime"].value_counts(normalize=True).round(3))
print("\nM15 regime distribution:")
print(m15["regime"].value_counts(normalize=True).round(3))


# ---------------------------------------------------------------- multi-timeframe alignment
# Separate from the regime label itself: a binary flag saying whether H1 and M15 agree on
# direction right now. Each H1 bar is matched to the M15 bar closing at the same timestamp
# (M15 candles are stamped at their close time after resampling, same as H1).
def add_alignment(h1_df: pd.DataFrame, m15_df: pd.DataFrame) -> pd.DataFrame:
    m15_regime_at_h1_close = m15_df["regime"].reindex(h1_df.index, method="ffill")

    bull_labels = {"strong_bull", "retracement_bull"}
    bear_labels = {"strong_bear", "retracement_bear"}

    h1_bull = h1_df["regime"].isin(bull_labels)
    h1_bear = h1_df["regime"].isin(bear_labels)
    m15_bull = m15_regime_at_h1_close.isin(bull_labels)
    m15_bear = m15_regime_at_h1_close.isin(bear_labels)

    out = h1_df.copy()
    out["m15_regime_at_close"] = m15_regime_at_h1_close
    out["mtf_aligned_bull"] = (h1_bull & m15_bull).astype(int)
    out["mtf_aligned_bear"] = (h1_bear & m15_bear).astype(int)
    return out


h1 = add_alignment(h1, m15)
print("\nMTF alignment (H1 rows):")
print(f"  aligned_bull: {h1['mtf_aligned_bull'].mean():.1%}")
print(f"  aligned_bear: {h1['mtf_aligned_bear'].mean():.1%}")
print(f"  either aligned: {(h1['mtf_aligned_bull'] | h1['mtf_aligned_bear']).mean():.1%}")


# ---------------------------------------------------------------- visual sanity check
def plot_regime(d: pd.DataFrame, title: str, n_bars: int = 400):
    sub = d.tail(n_bars)
    colors = {
        "strong_bull": "#1a9850", "retracement_bull": "#91cf60",
        "strong_bear": "#d73027", "retracement_bear": "#fc8d59",
        "range_recross": "#999999", "undefined": "#dddddd",
    }

    fig, ax = plt.subplots(figsize=(18, 7))
    ax.plot(sub.index, sub["close"], color="black", lw=1, zorder=3, label="close")
    ax.plot(sub.index, sub["ema144_high"], color="blue", lw=1, alpha=0.7, label="EMA144 high")
    ax.plot(sub.index, sub["ema144_low"], color="blue", lw=1, alpha=0.7, label="EMA144 low")
    ax.plot(sub.index, sub["ema33_high"], color="orange", lw=1, alpha=0.7, label="EMA33 high")
    ax.plot(sub.index, sub["ema33_low"], color="orange", lw=1, alpha=0.7, label="EMA33 low")

    for regime_name, color in colors.items():
        mask = sub["regime"] == regime_name
        if mask.any():
            ax.scatter(sub.index[mask], sub["close"][mask], color=color, s=10,
                       label=regime_name, zorder=4)

    ax.set_title(title)
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    plt.tight_layout()
    plt.savefig(f"regime_check_{title.replace(' ', '_')}.png", dpi=110)
    print(f"saved regime_check_{title.replace(' ', '_')}.png")
    plt.close()


plot_regime(h1, "H1 last 400 bars", n_bars=400)
plot_regime(m15, "M15 last 400 bars", n_bars=400)

# also a longer H1 view to see regime persistence over more time
plot_regime(h1, "H1 last 1500 bars", n_bars=1500)

m15.to_csv("m15_with_regime.csv")
h1.to_csv("h1_with_regime.csv")
print("\nsaved m15_with_regime.csv and h1_with_regime.csv")
