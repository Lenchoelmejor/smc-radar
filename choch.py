def detect_choch(structure):

    if structure["trend"] == "bullish" and structure["lh"]:

        return {

            "choch": True,

            "direction": "bearish"

        }

    if structure["trend"] == "bearish" and structure["hh"]:

        return {

            "choch": True,

            "direction": "bullish"

        }

    return {

        "choch": False,

        "direction": "none"

    }
