def calculate_rsi(candles, period=14):

    closes = [c["close"] for c in candles]

    if len(closes) < period + 1:
        return None

    gains = []
    losses = []

    for i in range(1, period + 1):

        diff = closes[i] - closes[i - 1]

        gains.append(max(diff, 0))
        losses.append(max(-diff, 0))

    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    for i in range(period + 1, len(closes)):

        diff = closes[i] - closes[i - 1]

        gain = max(diff, 0)
        loss = max(-diff, 0)

        avg_gain = ((avg_gain * (period - 1)) + gain) / period
        avg_loss = ((avg_loss * (period - 1)) + loss) / period

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss

    return round(100 - (100 / (1 + rs)), 2)
