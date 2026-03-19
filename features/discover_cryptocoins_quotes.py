from coinmarketcapapi import CoinMarketCapAPI

from main.config import coinmarketcap_api

def get_crypto_values(symbol="BTC"):

    cmc = CoinMarketCapAPI(coinmarketcap_api)

    data = cmc.tools_priceconversion(amount=1, symbol=symbol, convert="EUR")
    return data

if __name__ == "__main__":
    get_crypto_values()