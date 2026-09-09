from pydantic import BaseModel


class Metrics(BaseModel):
    total_revenue: float
    orders: int
    average_order_value: float


class RevenuePoint(BaseModel):
    date: str
    revenue: float


class ProductMetric(BaseModel):
    product: str
    revenue: float
    orders: int


class AnalyticsResponse(BaseModel):
    metrics: Metrics
    revenue_over_time: list[RevenuePoint]
    top_products: list[ProductMetric]
    fallbacks: list[str] = []
