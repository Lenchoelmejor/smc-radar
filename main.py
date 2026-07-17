import time

from telegram_bot import send_message
from scanner import scan


PAIRS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "BNBUSDT",
    "XRPUSDT",
    "DOGEUSDT",
]


def startup():

    print("=" * 60)
    print("LENCHO SMC RADAR")
    print("=" * 60)

    message = "📊 LENCHO SMC RADAR\n\n"

    for symbol in PAIRS:

        result = scan(symbol)

        if result["success"]:

            message += (
                f"📈 {symbol}\n"
                f"💰 Precio: {result['price']}\n"
                f"📊 RSI: {result['rsi']}\n"
                f"📉 Tendencia: {result['trend']}\n\n"
            )

        else:

            message += (
                f"❌ {symbol}\n"
                f"{result['error']}\n\n"
            )

    print(message)

    send_message(message)


def main():

    while True:

        startup()

        print("Esperando próximo escaneo...")

        time.sleep(900)


if __name__ == "__main__":
    main()
