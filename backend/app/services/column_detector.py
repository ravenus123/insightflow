import re
import pandas as pd
from app.domain.column_roles import ColumnRole

ALIASES: dict[ColumnRole, set[str]] = {
    ColumnRole.DATE: {"date", "order_date", "created_at", "purchase_date", "transaction_date"},
    ColumnRole.REVENUE: {"revenue", "sales", "sales_amount", "total", "total_price", "amount", "order_total"},
    ColumnRole.PRODUCT: {"product", "product_name", "item", "item_name", "sku_name"},
    ColumnRole.ORDER_ID: {"order_id", "order", "transaction_id", "invoice_id", "receipt_id"},
}


def normalize(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower())
    return re.sub(r"_+", "_", value).strip("_")


def _type_bonus(series: pd.Series, role: ColumnRole) -> float:
    if role is ColumnRole.REVENUE and pd.api.types.is_numeric_dtype(series):
        return 0.12
    if role is ColumnRole.DATE:
        parsed = pd.to_datetime(series.head(50), errors="coerce", format="mixed")
        return 0.12 if parsed.notna().mean() >= 0.8 else 0.0
    if role in {ColumnRole.PRODUCT, ColumnRole.ORDER_ID} and not pd.api.types.is_numeric_dtype(series):
        return 0.05
    return 0.0


def detect_columns(df: pd.DataFrame) -> dict[str, dict[str, object]]:
    detections: dict[str, dict[str, object]] = {}
    for role, aliases in ALIASES.items():
        best_column: str | None = None
        best_score = 0.0
        for column in df.columns:
            normalized = normalize(str(column))
            score = 0.0
            if normalized in aliases:
                score = 0.86
            elif any(alias in normalized or normalized in alias for alias in aliases):
                score = 0.64
            score += _type_bonus(df[column], role)
            score = min(score, 0.98)
            if score > best_score:
                best_column, best_score = str(column), score
        if best_column and best_score >= 0.6:
            detections[role.value] = {"column": best_column, "confidence": round(best_score, 2)}
    return detections
