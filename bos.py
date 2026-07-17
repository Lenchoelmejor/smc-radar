def detect_bos(structure):

    if structure["hh"] and structure["hl"]:
        return {
            "bos": True,
            "direction": "bullish"
        }

    if structure["lh"] and structure["ll"]:
        return {
            "bos": True,
            "direction": "bearish"
        }

    return {
        "bos": False,
        "direction": "none"
    }
