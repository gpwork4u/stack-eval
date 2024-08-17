from .constant import COLUMN_NAMES

def parse_stock_data(resp_data: dict):
    stock_data_dict = {}
    for item in resp_data['data']:
        stock = {}
        stock_id = item['s']
        data = item['d']
        for i, column_name in enumerate(COLUMN_NAMES):
            stock[column_name] = data[i]
        stock_data_dict[stock_id] = stock
    return stock_data_dict

    