def build_trade(signal, candles):

    if signal == "SIN ENTRADA":
        return {
            "valid": False
        }

    last = candles[-1]

    entry = last["close"]

    if signal == "LONG":

        stop = min(c["low"] for c in candles[-5:])

        risk = entry - stop

        if risk <= 0:
            return {"valid": False}

        target = entry + risk * 2

    elif signal == "SHORT":

        stop = max(c["high"] for c in candles[-5:])

        risk = stop - entry

        if risk <= 0:
            return {"valid": False}

        target = entry - risk * 2

    else:

        return {"valid": False}

    return {

        "valid": True,

        "entry": round(entry, 2),

        "stop": round(stop, 2),

        "target": round(target, 2),

        "rr": 2.0

    }
