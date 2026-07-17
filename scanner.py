from market import get_candles
from indicators import calculate_rsi
from structure import market_structure


def scan(symbol="BTCUSDT"):

    try:

        response = get_candles(
            symbol=symbol,
            interval="1H",
            limit=200,
        )

        candles = response["data"]

        closes = []

        for candle in candles:
            closes.append(float(candle[4]))

        rsi = calculate_rsi(closes)

        trend = market_structure(closes)

        return {
            "success": True,
            "symbol": symbol,
            "trend": trend,
            "rsi": rsi,
            "price": closes[-1],
        }

    except Exception as e:

        return {
            "success": False,
            "symbol": symbol,
            "error": str(e),
        }
