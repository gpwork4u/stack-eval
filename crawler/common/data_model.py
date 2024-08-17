from dataclasses import dataclass
from datetime import datetime


# reference: https://www.stockfeel.com.tw/%E5%AD%B8%E7%BF%92%E5%83%B9%E5%80%BC%E6%8A%95%E8%B3%87%E4%B9%8B%E7%88%B6%E8%91%9B%E6%8B%89%E6%BC%A2%E7%9A%84%E6%8A%95%E8%B3%87%E6%96%B9%E7%A8%8B%E5%BC%8F/# https://www.ycc.idv.tw/finance/finance_10.html
@dataclass
class financial_report_10k:
    company_id: str
    published_at: datetime
    current_assets: float # 流動性資產
    current_flow_liabilities: float # 流動性負債
    eps: float # 每股盈餘
    dividend: float # 股息
    net_income: float # 淨利
    # 本益比 = 股價 / 每股盈餘
    # 股價淨值比= 收盤價／每股參考淨值

@dataclass
class stock_price:
    company_id: str
    price: float
    volume: float
    timestamp: datetime