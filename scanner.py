from market import get_candles
from indicators import calculate_rsi
from structure import detect_market_structure
from bos import detect_bos


def scan(symbol):

    candles = get_candles(symbol)

    rsi = calculate_rsi(candles)

    structure = detect_market_structure(candles)

    bos = detect_bos(structure)

    last = candles[-1]

    return {

        "success": True,

        "symbol": symbol,

        "price": last["close"],

        "rsi": round(rsi, 2),

        "trend": structure["trend"],

        "hh": structure["hh"],
        "hl": structure["hl"],
        "lh": structure["lh"],
        "ll": structure["ll"],

        "bos": bos["bos"],
        "direction": bos["direction"],
    }
