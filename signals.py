last_signals = {}


def should_send(symbol, signal):

    if signal == "SIN ENTRADA":
        return False

    previous = last_signals.get(symbol)

    if previous == signal:
        return False

    last_signals[symbol] = signal

    return True
