from enum import Enum
class ColumnRole(str, Enum):
    DATE = "date"
    REVENUE = "revenue"
    PRODUCT = "product"
    ORDER_ID = "order_id"
    CUSTOMER = "customer"
    CATEGORY = "category"
    REGION = "region"
    QUANTITY = "quantity"
    UNIT_PRICE = "unit_price"
