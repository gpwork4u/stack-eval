from .constant import (MARKET_VALUE_THRESHOLD, 
                       CURRENT_RATIO_THRESHOLD,
                       NET_INCOME_THRESHOLD,
                       CONTINUOUS_DIVIDEND_PAYOUT,
                       DPS_COMMON_STOCK_PRIM_ISSUE_YOY_GROWTH,
                       PRICE_EARNING_THRESHOLD,
                       PRICE_BOOK_THRESHOLD)

def is_market_value_over(value):
    if value is not None and value >= MARKET_VALUE_THRESHOLD:
        return True
    return False

def is_current_ratio_over(value):
    if value is not None and value >= CURRENT_RATIO_THRESHOLD:
        return True
    return False

def is_net_income_over(value):
    if value is not None and value >= NET_INCOME_THRESHOLD:
        return True
    return False

def is_continuous_dividend_payout(value):
    if value is not None and value > CONTINUOUS_DIVIDEND_PAYOUT:
        return True
    return False

def is_dps_common_stock_prim_issue_yoy_growth_fy(value):
    if value is not None and value > DPS_COMMON_STOCK_PRIM_ISSUE_YOY_GROWTH:
        return True
    return False

def is_price_earning_over(value):
    if value is not None and value >= PRICE_EARNING_THRESHOLD:
        return True
    return False

def is_price_book_over(value):
    if value is not None and value >= PRICE_BOOK_THRESHOLD:
        return True
    return False