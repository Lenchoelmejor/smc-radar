import time

from telegram_bot import send_message
from scanner import scan


def startup():

    print("=" * 60)
    print("LENCHO SMC RADAR")
    print("=" * 60)

    result = scan("BTCUSDT")

    if result["success"]:

        message = (
            "📊 BTCUSDT\n\n"
            f"💵 Precio: {result['price']}\n"
            f"📈 RSI (14): {result['rsi']}\n"
            f"📊 Tendencia: {result['trend']}"
        )

        print(message)

        send_message(message)

    else:

        print(result["error"])

        send_message(
            f"❌ Error:\n\n{result['error']}"
        )


def main():

    startup()

    while True:

        print("Esperando próximo escaneo...")

        time.sleep(900)

        startup()


if __name__ == "__main__":
    main()
