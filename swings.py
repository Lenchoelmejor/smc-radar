def detect_swings(candles, left=3, right=3):

    swing_highs = []
    swing_lows = []

    for i in range(left, len(candles) - right):

        high = candles[i]["high"]
        low = candles[i]["low"]

        is_high = True
        is_low = True

        for j in range(i - left, i + right + 1):

            if j == i:
                continue

            if candles[j]["high"] >= high:
                is_high = False

            if candles[j]["low"] <= low:
                is_low = False

        if is_high:

            swing_highs.append({

                "index": i,

                "price": high

            })

        if is_low:

            swing_lows.append({

                "index": i,

                "price": low

            })

    return swing_highs, swing_lows
