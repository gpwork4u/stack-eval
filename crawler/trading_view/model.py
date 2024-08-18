
from dataclasses import dataclass

@dataclass
class StockInfo:
    name: str
    close: float
    volume: float
    current_ratio_fq: float
    total_current_assets_fq: float
    total_liabilities_fq: float
    market_cap_basic: float
    continuous_dividend_payout: int
    continuous_dividend_growth: int
    earnings_per_share_diluted_ttm: float
    price_earnings_ttm: float
    price_book_fq: float
    net_income_ttm: float
    dps_common_stock_prim_issue_yoy_growth_fy: float