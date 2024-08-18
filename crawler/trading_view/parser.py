import time
from .constant import COLUMN_NAMES
from .model import StockInfo

def transfer_stock_data(stock_data):
    stock_info = StockInfo(
        name = stock_data['name'],
        close = stock_data['close'],
        volume = stock_data['volume'],
        current_ratio_fq = stock_data['current_ratio_fq'],
        total_current_assets_fq = stock_data['total_current_assets_fq'],
        total_liabilities_fq = stock_data['total_liabilities_fq'],
        market_cap_basic = stock_data['market_cap_basic'] ,
        continuous_dividend_payout = stock_data['continuous_dividend_payout'],
        continuous_dividend_growth = stock_data['continuous_dividend_growth'],
        earnings_per_share_diluted_ttm = stock_data['earnings_per_share_diluted_ttm'],
        price_earnings_ttm = stock_data['price_earnings_ttm'],
        price_book_fq = stock_data['price_book_fq'],
        net_income_ttm = stock_data['net_income_ttm'],
        dps_common_stock_prim_issue_yoy_growth_fy = stock_data['dps_common_stock_prim_issue_yoy_growth_fy']
    )
    return stock_info
def parse_stock_data(resp_data: dict):
    stock_data_dict = {}
    for item in resp_data['data']:
        stock = {}
        stock_id = item['s']
        data = item['d']
        for i, column_name in enumerate(COLUMN_NAMES):
            stock[column_name] = data[i]
        stock_data_dict[stock_id] = transfer_stock_data(stock)

    return stock_data_dict
