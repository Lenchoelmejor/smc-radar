def evaluate_strategy(day, h4, h1):

    if (
        day["trend"] == "bullish"
        and h4["trend"] == "bullish"
        and h1["trend"] == "bullish"
        and h1["rsi"] >= 55
    ):

        return {
            "signal": "LONG",
            "confidence": 9
        }

    if (
        day["trend"] == "bearish"
        and h4["trend"] == "bearish"
        and h1["trend"] == "bearish"
        and h1["rsi"] <= 45
    ):

        return {
            "signal": "SHORT",
            "confidence": 9
        }

    return {

        "signal": "SIN ENTRADA",

        "confidence": 3

    }
