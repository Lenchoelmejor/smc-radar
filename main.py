import time

from telegram_bot import send_message
from bitget import get_server_time


def startup():

    print("=" * 60)
    print("LENCHO SMC RADAR")
    print("=" * 60)

    # -----------------------------------------
    # BITGET
    # -----------------------------------------

    try:

        server = get_server_time()

        print("✅ Bitget conectado")
        print(server)

    except Exception as e:

        print(f"❌ Error Bitget: {e}")

    # -----------------------------------------
    # TELEGRAM
    # -----------------------------------------

    try:

        send_message(
            "🚀 LENCHO SMC RADAR\n\n"
            "✅ Bot iniciado correctamente.\n"
            "✅ Bitget conectado.\n"
            "✅ Telegram conectado.\n\n"
            "Esperando próximo escaneo..."
        )

        print("✅ Telegram conectado")

    except Exception as e:

        print(f"❌ Error Telegram: {e}")


def main():

    startup()

    while True:

        print("Radar activo...")

        # Más adelante aquí irá:
        # scanner.scan()

        time.sleep(900)


if __name__ == "__main__":
    main()
    from market import get_candles
