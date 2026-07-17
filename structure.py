from swings import detect_swings


def detect_market_structure(candles):

    highs, lows = detect_swings(candles)

    if len(highs) < 2 or len(lows) < 2:

        return {
            "trend": "unknown",
            "hh": False,
            "hl": False,
            "lh": False,
            "ll": False,
        }

    last_high = highs[-1]["price"]
    prev_high = highs[-2]["price"]

    last_low = lows[-1]["price"]
    prev_low = lows[-2]["price"]

    hh = last_high > prev_high
    hl = last_low > prev_low

    lh = last_high < prev_high
    ll = last_low < prev_low

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

        "last_high": last_high,
        "last_low": last_low,

        "previous_high": prev_high,
        "previous_low": prev_low,
    }
