def detect_bos(structure):

    bullish = structure["hh"] and structure["hl"]

    bearish = structure["lh"] and structure["ll"]

    if bullish:

        return {

            "bos": True,

            "direction": "bullish"

        }

    if bearish:

        return {

            "bos": True,

            "direction": "bearish"

        }

    return {

        "bos": False,

        "direction": "none"

    }
