import requests
import json
from config import keys

class APIException(Exception):  # обработка  ошибок
    pass


class CryptoConverter:
    @staticmethod

    def get_price(quote: str, base: str,amount: str):#amountd  в переводе сумма
        if quote == base:
            raise APIException(f'невозможно перевести одинаковые валюты {base}')  ##ловля ошибки если переводит конвертор на сомого себя

        try:# пробывать,попытка
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'не удалось обработать валюту1  "{quote}"')

        try:  # пробывать,попытка
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'не удалось обработать валюту2 "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]]

        return total_base
