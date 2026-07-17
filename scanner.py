from market import get_candles
from indicators import calculate_rsi
from structure import detect_market_structure
from bos import detect_bos
from choch import detect_choch
from strategy import evaluate_strategy
from trade import build_trade


def analyze_timeframe(symbol, timeframe):

    candles = get_candles(symbol, timeframe)

    rsi = calculate_rsi(candles)

    structure = detect_market_structure(candles)

    bos = detect_bos(structure)

    choch = detect_choch(structure)

    return {
        "candles": candles,
        "trend": structure["trend"],
        "rsi": rsi,
        "bos": bos["bos"],
        "bos_direction": bos["direction"],
        "choch": choch["choch"],
        "choch_direction": choch["direction"],
        "price": candles[-1]["close"],
    }


def scan(symbol):

    day = analyze_timeframe(symbol, "1D")

    h4 = analyze_timeframe(symbol, "4H")

    h1 = analyze_timeframe(symbol, "1H")

    signal = evaluate_strategy(day, h4, h1)

    trade = build_trade(
        signal["signal"],
        h1["candles"]
    )

    return {

        "success": True,

        "symbol": symbol,

        "price": h1["price"],

        "day": day,

        "h4": h4,

        "h1": h1,

        "signal": signal["signal"],

        "confidence": signal["confidence"],

        "trade": trade,

    }
