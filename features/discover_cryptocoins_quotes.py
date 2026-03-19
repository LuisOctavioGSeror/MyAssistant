import requests

from main.config import coinmarketcap_api


def get_crypto_values(symbol="BTC"):
    url = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": coinmarketcap_api or "",
    }
    params = {
        "amount": 1,
        "symbol": symbol,
        "convert": "EUR",
    }

    response = requests.get(url, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    get_crypto_values()