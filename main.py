import time

from scanner import scan
from telegram_bot import send_telegram_message
from signals import should_send

PAIRS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "BNBUSDT",
    "XRPUSDT",
    "DOGEUSDT",
]


def build_message(result):

    return f"""
🚀 LENCHO SMC RADAR

━━━━━━━━━━━━━━━━━━━━━━

📌 Activo: {result["symbol"]}

💲 Precio: {result["price"]:.2f}

📅 1D: {result["day"]["trend"].upper()}
🕓 4H: {result["h4"]["trend"].upper()}
🕐 1H: {result["h1"]["trend"].upper()}

📈 RSI 1H: {result["h1"]["rsi"]:.2f}

📊 BOS: {"✅" if result["h1"]["bos"] else "❌"}
🔄 CHoCH: {"✅" if result["h1"]["choch"] else "❌"}

🎯 SEÑAL: {result["signal"]}

⭐ Convicción: {result["confidence"]}/10

━━━━━━━━━━━━━━━━━━━━━━
"""


def main():

    print("LENCHO SMC RADAR iniciado...")

    send_telegram_message(
        "🚀 LENCHO SMC RADAR\n\nBot iniciado correctamente."
    )

    while True:

        for symbol in PAIRS:

            try:

                result = scan(symbol)

                if not result["success"]:
                    continue

                if should_send(result["symbol"], result["signal"]):

                    send_telegram_message(
                        build_message(result)
                    )

            except Exception as e:

                print(f"{symbol}: {e}")

            time.sleep(2)

        print("Esperando próximo escaneo...")

        time.sleep(900)


if __name__ == "__main__":
    main()
