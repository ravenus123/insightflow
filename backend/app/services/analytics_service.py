import pandas as pd
from app.core.exceptions import InvalidDatasetError
from app.schemas.analytics import AnalyticsResponse, CustomerMetric, Insight, Metrics, NamedMetric, ProductMetric, RevenuePoint

def _growth(current: float, previous: float) -> float:
    if previous == 0: return 0.0
    return round((current-previous)/abs(previous)*100, 1)

def _named_breakdown(work: pd.DataFrame, name_col: str | None, revenue_col: str, order_col: str | None) -> list[NamedMetric]:
    if not name_col or name_col not in work.columns: return []
    subset = work.dropna(subset=[name_col, revenue_col])
    if subset.empty: return []
    grouped = subset.groupby(name_col)[revenue_col].sum().sort_values(ascending=False).head(8)
    total = float(work[revenue_col].sum()) or 1.0
    result=[]
    for name,revenue in grouped.items():
        if order_col and order_col in subset: orders=int(subset.loc[subset[name_col]==name,order_col].nunique())
        else: orders=int((subset[name_col]==name).sum())
        result.append(NamedMetric(name=str(name),revenue=round(float(revenue),2),orders=orders,share=round(float(revenue)/total*100,1)))
    return result

def analyze_sales(df: pd.DataFrame, mapping: dict[str, str]) -> AnalyticsResponse:
    revenue_col = mapping.get("revenue")
    if not revenue_col or revenue_col not in df.columns: raise InvalidDatasetError("A valid revenue column is required.")
    work = df.copy(); work[revenue_col]=pd.to_numeric(work[revenue_col],errors="coerce"); work=work.dropna(subset=[revenue_col])
    if work.empty: raise InvalidDatasetError("Revenue contains no valid numeric values.")
    total_revenue=float(work[revenue_col].sum()); fallbacks=[]
    order_col=mapping.get("order_id")
    orders=int(work[order_col].nunique(dropna=True)) if order_col and order_col in work else int(len(work))
    if not order_col or order_col not in work: fallbacks.append("Order count uses row count because no order ID was mapped.")
    customer_col=mapping.get("customer"); customers=int(work[customer_col].nunique(dropna=True)) if customer_col and customer_col in work else 0
    aov=total_revenue/orders if orders else 0.0
    date_col=mapping.get("date"); revenue_over_time=[]; revenue_growth=0.; order_growth=0.
    if date_col and date_col in work:
        work["__date"]=pd.to_datetime(work[date_col],errors="coerce",format="mixed"); dated=work.dropna(subset=["__date"]).copy()
        if not dated.empty:
            grouped_rev=dated.groupby(dated["__date"].dt.date)[revenue_col].sum().sort_index()
            if order_col and order_col in dated: grouped_ord=dated.groupby(dated["__date"].dt.date)[order_col].nunique()
            else: grouped_ord=dated.groupby(dated["__date"].dt.date).size()
            revenue_over_time=[RevenuePoint(date=str(day),revenue=round(float(value),2),orders=int(grouped_ord.get(day,0))) for day,value in grouped_rev.items()]
            split=dated["__date"].min()+(dated["__date"].max()-dated["__date"].min())/2
            prev=dated[dated["__date"]<=split]; curr=dated[dated["__date"]>split]
            revenue_growth=_growth(float(curr[revenue_col].sum()),float(prev[revenue_col].sum()))
            prev_orders=int(prev[order_col].nunique()) if order_col and order_col in prev else len(prev)
            curr_orders=int(curr[order_col].nunique()) if order_col and order_col in curr else len(curr)
            order_growth=_growth(curr_orders,prev_orders)
    product_col=mapping.get("product"); top_products=[]
    if product_col and product_col in work:
        subset=work.dropna(subset=[product_col]); grouped=subset.groupby(product_col)[revenue_col].sum().sort_values(ascending=False).head(10)
        for product,revenue in grouped.items():
            p=subset[subset[product_col]==product]; count=int(p[order_col].nunique()) if order_col and order_col in p else len(p)
            top_products.append(ProductMetric(product=str(product),revenue=round(float(revenue),2),orders=count))
    top_customers=[]
    if customer_col and customer_col in work:
        subset=work.dropna(subset=[customer_col]); grouped=subset.groupby(customer_col)[revenue_col].sum().sort_values(ascending=False).head(10)
        for customer,revenue in grouped.items():
            c=subset[subset[customer_col]==customer]; count=int(c[order_col].nunique()) if order_col and order_col in c else len(c)
            top_customers.append(CustomerMetric(customer=str(customer),revenue=round(float(revenue),2),orders=count))
    categories=_named_breakdown(work,mapping.get("category"),revenue_col,order_col)
    regions=_named_breakdown(work,mapping.get("region"),revenue_col,order_col)
    insights=[]
    if revenue_growth:
        direction="increased" if revenue_growth>0 else "decreased"
        insights.append(Insight(tone="positive" if revenue_growth>0 else "warning",title=f"Revenue {direction} {abs(revenue_growth):.1f}%",detail="Comparison uses the first and second half of the mapped date range, so the result remains deterministic and auditable."))
    if categories:
        c=categories[0]; insights.append(Insight(tone="neutral",title=f"{c.name} leads category mix",detail=f"It contributes {c.share:.1f}% of tracked revenue ({c.revenue:,.0f} in source currency)."))
    if regions:
        r=regions[0]; insights.append(Insight(tone="neutral",title=f"{r.name} is the strongest region",detail=f"It accounts for {r.share:.1f}% of revenue in the selected dataset."))
    if customer_col and customers:
        by_customer=work.groupby(customer_col)[revenue_col].sum().sort_values(ascending=False)
        top_n=max(1,int(len(by_customer)*.2)); concentration=float(by_customer.head(top_n).sum())/total_revenue*100 if total_revenue else 0
        insights.append(Insight(tone="warning" if concentration>70 else "neutral",title="Customer concentration is measurable",detail=f"The top 20% of customers contribute {concentration:.1f}% of revenue."))
    return AnalyticsResponse(metrics=Metrics(total_revenue=round(total_revenue,2),orders=orders,customers=customers,average_order_value=round(aov,2),revenue_growth=revenue_growth,order_growth=order_growth),revenue_over_time=revenue_over_time,orders_over_time=revenue_over_time,top_products=top_products,top_customers=top_customers,categories=categories,regions=regions,insights=insights, fallbacks=fallbacks)
