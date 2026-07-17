def detect_market_structure(candles):

    if len(candles) < 40:
        raise Exception("No hay suficientes velas")

    highs = [c["high"] for c in candles]
    lows = [c["low"] for c in candles]

    recent_high = max(highs[-10:])
    previous_high = max(highs[-20:-10])

    recent_low = min(lows[-10:])
    previous_low = min(lows[-20:-10])

    hh = recent_high > previous_high
    hl = recent_low > previous_low

    lh = recent_high < previous_high
    ll = recent_low < previous_low

    if hh and hl:
        trend = "bullish"

    elif lh and ll:
        trend = "bearish"

    else:
        trend = "ranging"

    return {
        "trend": trend,
        "hh": hh,
        "hl": hl,
        "lh": lh,
        "ll": ll,
    }
