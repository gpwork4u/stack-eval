from ..trading_view.model import StockInfo
from ..trading_view.api import get_current_stock_data
from ..common.filter import (is_market_value_over,
                             is_current_ratio_over,
                             is_net_income_over,
                             is_continuous_dividend_payout,
                             is_dps_common_stock_prim_issue_yoy_growth_fy,
                             is_price_earning_over,
                             is_price_book_over)


stock_data_dict = get_current_stock_data()


def filter_by_market_value(stock_data_dict: dict[str, StockInfo]) -> dict[str, StockInfo]:
    filtered_stock_data_dict = {}
    for stock_id, stock_info in stock_data_dict.items():
        if is_market_value_over(stock_info.market_cap_basic):
            filtered_stock_data_dict[stock_id] = stock_info
    return filtered_stock_data_dict

def filter_by_current_ratio(stock_data_dict):
    filtered_stock_data_dict = {}
    for stock_id, stock_info in stock_data_dict.items():
        if is_current_ratio_over(stock_info.current_ratio_fq):
            filtered_stock_data_dict[stock_id] = stock_info
    return filtered_stock_data_dict

def filter_by_net_income(stock_data_dict):
    filtered_stock_data_dict = {}
    for stock_id, stock_info in stock_data_dict.items():
        if is_net_income_over(stock_info.net_income_ttm):
            filtered_stock_data_dict[stock_id] = stock_info
    return filtered_stock_data_dict

def filter_by_continuous_dividend_payout(stock_data_dict):
    filtered_stock_data_dict = {}
    for stock_id, stock_info in stock_data_dict.items():
        if is_continuous_dividend_payout(stock_info.continuous_dividend_payout):
            filtered_stock_data_dict[stock_id] = stock_info
    return filtered_stock_data_dict

def filter_by_dps_common_stock_prim_issue_yoy_growth_fy(stock_data_dict):
    filtered_stock_data_dict = {}
    for stock_id, stock_info in stock_data_dict.items():
        if is_dps_common_stock_prim_issue_yoy_growth_fy(stock_info.dps_common_stock_prim_issue_yoy_growth_fy):
            filtered_stock_data_dict[stock_id] = stock_info
    return filtered_stock_data_dict

def filter_by_price_earning(stock_data_dict):
    filtered_stock_data_dict = {}
    for stock_id, stock_info in stock_data_dict.items():
        if is_price_earning_over(stock_info.price_earnings_ttm):
            filtered_stock_data_dict[stock_id] = stock_info
    return filtered_stock_data_dict

def filter_by_price_book(stock_data_dict):
    filtered_stock_data_dict = {}
    for stock_id, stock_info in stock_data_dict.items():
        if is_price_book_over(stock_info.price_book_fq):
            filtered_stock_data_dict[stock_id] = stock_info
    return filtered_stock_data_dict


filtered_stock_data_dict = filter_by_market_value(stock_data_dict)
filtered_stock_data_dict = filter_by_current_ratio(filtered_stock_data_dict)
filtered_stock_data_dict = filter_by_net_income(filtered_stock_data_dict)
filtered_stock_data_dict = filter_by_continuous_dividend_payout(filtered_stock_data_dict)
filtered_stock_data_dict = filter_by_dps_common_stock_prim_issue_yoy_growth_fy(filtered_stock_data_dict)
filtered_stock_data_dict = filter_by_price_earning(filtered_stock_data_dict)
filtered_stock_data_dict = filter_by_price_book(filtered_stock_data_dict)

print(len(filtered_stock_data_dict))