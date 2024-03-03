import requests as rq

from django.db import models
from django.core.validators import MinValueValidator


def get_token_name():
    binance_url = "https://api.binance.com/api/v3/ticker/price"
    response = rq.get(binance_url)
    data = response.json()
    tokens = {token['symbol'][:-4]: token['symbol'][:-4] for token in data if token['symbol'].endswith('USDT')}
    tokens['USDT'] = 'USDT'
    return tokens


class Storage(models.Model):
    TOKEN_NAME = get_token_name()
    token_name = models.CharField(max_length=100, choices=TOKEN_NAME, default='BTC', unique=True)
    value = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.token_name
