import time

from scanner import scan
from telegram_bot import send_telegram_message

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

━━━━━━━━━━━━━━━━━━━━

📌 {result["symbol"]}

💲 Precio: {result["price"]:.2f}

📅 1D : {result["day"]["trend"]}
🕓 4H : {result["h4"]["trend"]}
🕐 1H : {result["h1"]["trend"]}

📈 RSI 1H : {result["h1"]["rsi"]:.2f}

📊 BOS : {"✅" if result["h1"]["bos"] else "❌"}

🔄 CHoCH : {"✅" if result["h1"]["choch"] else "❌"}

🎯 SEÑAL : {result["signal"]}

⭐ Convicción : {result["confidence"]}/10
"""


def main():

    send_telegram_message("🚀 LENCHO SMC RADAR iniciado")

    while True:

        for symbol in PAIRS:

            try:

                result = scan(symbol)

                if result["success"]:

                    send_telegram_message(
                        build_message(result)
                    )

            except Exception as e:

                send_telegram_message(
                    f"❌ {symbol}\n{e}"
                )

            time.sleep(2)

        time.sleep(900)


if __name__ == "__main__":
    main()
