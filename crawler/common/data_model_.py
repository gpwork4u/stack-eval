from dataclasses import dataclass
from datetime import datetime

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
