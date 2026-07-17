import requests

BASE_URL = "https://api.bitget.com"


def get_candles(symbol="BTCUSDT", interval="1H", limit=200):
    """
    Obtiene velas de Bitget.
    """

    url = f"{BASE_URL}/api/v2/mix/market/candles"

    params = {
        "symbol": symbol,
        "granularity": interval,
        "productType": "USDT-FUTURES",
        "limit": limit,
    }

    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()

    return r.json()
