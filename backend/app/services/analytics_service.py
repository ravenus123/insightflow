import pandas as pd
from app.core.exceptions import InvalidDatasetError
from app.schemas.analytics import AnalyticsResponse, Metrics, ProductMetric, RevenuePoint


def analyze_sales(df: pd.DataFrame, mapping: dict[str, str]) -> AnalyticsResponse:
    revenue_col = mapping.get("revenue")
    if not revenue_col or revenue_col not in df.columns:
        raise InvalidDatasetError("A valid revenue column is required.")

    work = df.copy()
    work[revenue_col] = pd.to_numeric(work[revenue_col], errors="coerce")
    valid_revenue = work[revenue_col].dropna()
    if valid_revenue.empty:
        raise InvalidDatasetError("Revenue contains no valid numeric values.")

    total_revenue = float(valid_revenue.sum())
    fallbacks: list[str] = []

    order_col = mapping.get("order_id")
    if order_col and order_col in work.columns:
        orders = int(work[order_col].nunique(dropna=True))
    else:
        orders = int(len(work))
        fallbacks.append("Order count uses row count because no order ID was mapped.")

    aov = total_revenue / orders if orders else 0.0

    revenue_over_time: list[RevenuePoint] = []
    date_col = mapping.get("date")
    if date_col and date_col in work.columns:
        work["__date"] = pd.to_datetime(work[date_col], errors="coerce")
        dated = work.dropna(subset=["__date", revenue_col]).copy()
        if not dated.empty:
            grouped = dated.groupby(dated["__date"].dt.date)[revenue_col].sum().sort_index()
            revenue_over_time = [RevenuePoint(date=str(day), revenue=float(value)) for day, value in grouped.items()]

    top_products: list[ProductMetric] = []
    product_col = mapping.get("product")
    if product_col and product_col in work.columns:
        product_rows = work.dropna(subset=[product_col, revenue_col])
        grouped = product_rows.groupby(product_col).agg(revenue=(revenue_col, "sum"))
        if order_col and order_col in product_rows.columns:
            grouped["orders"] = product_rows.groupby(product_col)[order_col].nunique()
        else:
            grouped["orders"] = product_rows.groupby(product_col).size()
        grouped = grouped.sort_values("revenue", ascending=False).head(10)
        top_products = [
            ProductMetric(product=str(index), revenue=float(row.revenue), orders=int(row.orders))
            for index, row in grouped.iterrows()
        ]

    return AnalyticsResponse(
        metrics=Metrics(
            total_revenue=round(total_revenue, 2),
            orders=orders,
            average_order_value=round(aov, 2),
        ),
        revenue_over_time=revenue_over_time,
        top_products=top_products,
        fallbacks=fallbacks,
    )
