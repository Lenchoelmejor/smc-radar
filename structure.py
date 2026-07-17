def market_structure(closes):
    """
    Detecta la estructura básica del mercado.

    Retorna:
        bullish
        bearish
        ranging
    """

    if len(closes) < 10:
        return "unknown"

    highs = []
    lows = []

    for i in range(1, len(closes) - 1):

        if closes[i] > closes[i - 1] and closes[i] > closes[i + 1]:
            highs.append(closes[i])

        if closes[i] < closes[i - 1] and closes[i] < closes[i + 1]:
            lows.append(closes[i])

    if len(highs) < 2 or len(lows) < 2:
        return "ranging"

    if highs[-1] > highs[-2] and lows[-1] > lows[-2]:
        return "bullish"

    if highs[-1] < highs[-2] and lows[-1] < lows[-2]:
        return "bearish"

    return "ranging"
