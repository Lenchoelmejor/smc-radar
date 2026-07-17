from market import get_candles
from indicators import calculate_rsi
from structure import detect_market_structure
from bos import detect_bos


def scan(symbol):

    try:

        df = get_candles(symbol)

        rsi = calculate_rsi(df)

        structure = detect_market_structure(df)

        bos = detect_bos(structure)

        return {
            "success": True,
            "symbol": symbol,
            "price": round(df["close"].iloc[-1], 2),
            "rsi": round(rsi, 2),

            "trend": structure["trend"],

            "hh": structure["hh"],
            "hl": structure["hl"],
            "lh": structure["lh"],
            "ll": structure["ll"],

            "bos": bos["bos"],
            "direction": bos["direction"],
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e),
        }
