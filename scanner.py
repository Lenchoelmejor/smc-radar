from market import get_candles
from indicators import calculate_rsi


def scan(symbol="BTCUSDT"):

    try:

        data = get_candles(
            symbol=symbol,
            interval="1H",
            limit=200,
        )

        # Ajustar al formato devuelto por Bitget
        candles = data["data"]

        closes = []

        for candle in candles:

            # El precio de cierre viene en la posición 4
            closes.append(float(candle[4]))

        rsi = calculate_rsi(closes)

        return {
            "symbol": symbol,
            "rsi": rsi,
            "candles": len(closes),
        }

    except Exception as e:

        return {
            "symbol": symbol,
            "error": str(e),
        }
