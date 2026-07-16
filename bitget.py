import requests

BASE_URL = "https://api.bitget.com"


def get_server_time():
    """Obtiene la hora del servidor de Bitget."""
    url = f"{BASE_URL}/api/v2/public/time"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    print(get_server_time())
