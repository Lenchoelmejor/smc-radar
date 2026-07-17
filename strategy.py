def evaluate_strategy(day, h4, h1):

    # LONG
    if (
        day["trend"] == "bullish"
        and h4["trend"] == "bullish"
        and h1["trend"] == "bullish"
        and h1["rsi"] > 50
    ):

        return {
            "signal": "LONG",
            "confidence": 9
        }

    # SHORT
    if (
        day["trend"] == "bearish"
        and h4["trend"] == "bearish"
        and h1["trend"] == "bearish"
        and h1["rsi"] < 50
    ):

        return {
            "signal": "SHORT",
            "confidence": 9
        }

    return {
        "signal": "SIN ENTRADA",
        "confidence": 3
    }
