import requests
from .constant import COLUMN_NAMES
from .parser import parse_stock_data

def get_current_stock_data():
    url = 'https://scanner.tradingview.com/america/scan'

    payload = {
        'columns': COLUMN_NAMES,
        'ignore_unknown_fields': False,
        'range': [0, 10000],
        'sort': {'sortBy': 'name', 'sortOrder': 'asc', 'nullsFirst': False},
        'preset': 'all_stocks'
    }

    resp = requests.post(url, json=payload)

    data = resp.json()

    return parse_stock_data(data)

data = get_current_stock_data()

