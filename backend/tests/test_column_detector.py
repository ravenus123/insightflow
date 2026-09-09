import pandas as pd
from app.services.column_detector import detect_columns


def test_detects_basic_sales_columns() -> None:
    df = pd.DataFrame({
        "order_date": ["2026-01-01", "2026-01-02"],
        "total_price": [10.0, 20.0],
        "product_name": ["A", "B"],
        "order_id": ["1", "2"],
    })
    result = detect_columns(df)
    assert result["date"]["column"] == "order_date"
    assert result["revenue"]["column"] == "total_price"
    assert result["product"]["column"] == "product_name"
    assert result["order_id"]["column"] == "order_id"
