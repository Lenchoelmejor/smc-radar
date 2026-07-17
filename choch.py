def detect_choch(structure):

    trend = structure["trend"]

    if trend == "bullish" and structure["lh"]:
        return {
            "choch": True,
            "direction": "bearish"
        }

    if trend == "bearish" and structure["hh"]:
        return {
            "choch": True,
            "direction": "bullish"
        }

    return {
        "choch": False,
        "direction": "none"
    }
