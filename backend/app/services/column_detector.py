import re
import pandas as pd
from app.domain.column_roles import ColumnRole

ALIASES: dict[ColumnRole, set[str]] = {
    ColumnRole.DATE: {"date","order_date","created_at","purchase_date","transaction_date","sale_date"},
    ColumnRole.REVENUE: {"revenue","sales","sales_amount","total","total_price","amount","order_total","line_total","net_sales"},
    ColumnRole.PRODUCT: {"product","product_name","item","item_name","sku_name","sku"},
    ColumnRole.ORDER_ID: {"order_id","order","transaction_id","invoice_id","receipt_id"},
    ColumnRole.CUSTOMER: {"customer","customer_id","client","client_id","account","account_id"},
    ColumnRole.CATEGORY: {"category","product_category","department","segment","family"},
    ColumnRole.REGION: {"region","market","territory","location","area","country"},
    ColumnRole.QUANTITY: {"quantity","qty","units","units_sold","count"},
    ColumnRole.UNIT_PRICE: {"unit_price","price","price_each","item_price","unit_cost"},
}

def normalize(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower())
    return re.sub(r"_+", "_", value).strip("_")

def _type_bonus(series: pd.Series, role: ColumnRole) -> float:
    if role in {ColumnRole.REVENUE, ColumnRole.QUANTITY, ColumnRole.UNIT_PRICE}:
        numeric = pd.to_numeric(series.head(100), errors="coerce").notna().mean()
        return 0.12 if numeric >= 0.8 else 0.0
    if role is ColumnRole.DATE:
        parsed = pd.to_datetime(series.head(100), errors="coerce", format="mixed")
        return 0.12 if parsed.notna().mean() >= 0.8 else 0.0
    if role in {ColumnRole.PRODUCT, ColumnRole.CUSTOMER, ColumnRole.CATEGORY, ColumnRole.REGION, ColumnRole.ORDER_ID}:
        return 0.04
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
            score = min(score + _type_bonus(df[column], role), 0.98)
            if score > best_score:
                best_column, best_score = str(column), score
        if best_column and best_score >= 0.6:
            detections[role.value] = {"column": best_column, "confidence": round(best_score, 2)}
    return detections
