import requests as rq
from django.shortcuts import render

from wallet.utils import get_token_prices


def index(request):
    data = get_token_prices()

    return render(request, 'index.html', {'data': data})
