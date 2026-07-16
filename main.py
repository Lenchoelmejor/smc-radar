from telegram_bot import send_message
from bitget import get_server_time


def main():

    print("=" * 50)
    print("LENCHO SMC RADAR")
    print("=" * 50)

    print("Conectando con Bitget...")

    try:
        server = get_server_time()
        print("✅ Bitget conectado")
        print(server)

    except Exception as e:
        print(f"❌ Error Bitget: {e}")
        return

    try:

        send_message(
            "🚀 Lencho SMC Radar iniciado correctamente.\n\n"
            "✅ Conectado a Bitget\n"
            "✅ Conectado a Telegram\n\n"
            "Ahora comenzará el desarrollo del radar."
        )

        print("✅ Telegram conectado")

    except Exception as e:
        print(f"❌ Error Telegram: {e}")


if __name__ == "__main__":
    main()
