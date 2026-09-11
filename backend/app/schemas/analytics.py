from typing import Literal
from pydantic import BaseModel
class Metrics(BaseModel):
    total_revenue: float
    orders: int
    customers: int = 0
    average_order_value: float
    revenue_growth: float = 0
    order_growth: float = 0
class RevenuePoint(BaseModel):
    date: str
    revenue: float
    orders: int = 0
class ProductMetric(BaseModel):
    product: str
    revenue: float
    orders: int
class CustomerMetric(BaseModel):
    customer: str
    revenue: float
    orders: int
class NamedMetric(BaseModel):
    name: str
    revenue: float
    orders: int = 0
    share: float = 0
class Insight(BaseModel):
    tone: Literal["positive","neutral","warning"]
    title: str
    detail: str
class AnalyticsResponse(BaseModel):
    metrics: Metrics
    revenue_over_time: list[RevenuePoint]
    orders_over_time: list[RevenuePoint]
    top_products: list[ProductMetric]
    top_customers: list[CustomerMetric]
    categories: list[NamedMetric]
    regions: list[NamedMetric]
    insights: list[Insight]
    fallbacks: list[str] = []
