def detect_market_structure(df):

    highs = df["high"].tolist()
    lows = df["low"].tolist()

    last_high = max(highs[-10:])
    prev_high = max(highs[-20:-10])

    last_low = min(lows[-10:])
    prev_low = min(lows[-20:-10])

    if last_high > prev_high and last_low > prev_low:
        return {
            "trend": "bullish",
            "hh": True,
            "hl": True,
            "lh": False,
            "ll": False,
        }

    elif last_high < prev_high and last_low < prev_low:
        return {
            "trend": "bearish",
            "hh": False,
            "hl": False,
            "lh": True,
            "ll": True,
        }

    return {
        "trend": "ranging",
        "hh": False,
        "hl": False,
        "lh": False,
        "ll": False,
    }
