import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class MonetaryConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Так низя вообще-то!!! Как я буду {base} в {base} переводить???')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Чет не найду никаких {quote}!!!')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Чет не найду никаких {base}!!!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'{amount}??? Я таких цифер не знаю! Я бот приличный!!!')

        r = requests.get(f'https://currate.ru/api/?get=rates&pairs={quote_ticker}{base_ticker},EURRUB&key=1d1cff49e449258bff06e8e4b846540f')
        total_base_first = json.loads(r.content)
        crutch = total_base_first.get('data')
        crutch_2 = float(crutch.get(f'{keys[quote]}{keys[base]}'))
        total_base = crutch_2 * amount

        return total_base
