def detect_swings(candles, left=2, right=2):

    highs = []
    lows = []

    for i in range(left, len(candles) - right):

        high = candles[i]["high"]
        low = candles[i]["low"]

        swing_high = True
        swing_low = True

        for j in range(i - left, i + right + 1):

            if j == i:
                continue

            if candles[j]["high"] >= high:
                swing_high = False

            if candles[j]["low"] <= low:
                swing_low = False

        if swing_high:
            highs.append({
                "index": i,
                "price": high
            })

        if swing_low:
            lows.append({
                "index": i,
                "price": low
            })

    return highs, lows
