import requests as rq


def get_token_prices():
    binance_url = "https://api.binance.com/api/v3/ticker/price"
    response = rq.get(binance_url)
    data = response.json()
    return {token['symbol'][:-4]: token['price'] for token in data if token['symbol'].endswith('USDT')}