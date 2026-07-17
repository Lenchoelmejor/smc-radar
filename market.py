import requests

BASE_URL = "https://api.bitget.com"


def get_candles(symbol="BTCUSDT", interval="1H", limit=200):

    url = BASE_URL + "/api/v2/mix/market/candles"

    params = {
        "symbol": symbol,
        "granularity": interval,
        "productType": "USDT-FUTURES",
        "limit": limit
    }

    response = requests.get(
        url,
        params=params,
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    if data["code"] != "00000":
        raise Exception(data["msg"])

    candles = []

    for c in reversed(data["data"]):

        candles.append({

            "time": int(c[0]),
            "open": float(c[1]),
            "high": float(c[2]),
            "low": float(c[3]),
            "close": float(c[4]),
            "volume": float(c[5])

        })

    return candles
