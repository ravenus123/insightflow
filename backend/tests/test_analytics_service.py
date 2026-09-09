import pandas as pd
from app.services.analytics_service import analyze_sales


def test_basic_sales_metrics() -> None:
    df = pd.DataFrame({
        "date": ["2026-01-01", "2026-01-01", "2026-01-02"],
        "order": ["A", "A", "B"],
        "product": ["One", "Two", "One"],
        "revenue": [10.0, 5.0, 20.0],
    })
    result = analyze_sales(df, {"date": "date", "order_id": "order", "product": "product", "revenue": "revenue"})
    assert result.metrics.total_revenue == 35.0
    assert result.metrics.orders == 2
    assert result.metrics.average_order_value == 17.5
