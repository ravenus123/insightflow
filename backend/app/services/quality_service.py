import numpy as np
import pandas as pd
from app.schemas.quality import QualityIssue, QualityResponse

def _issue(code: str, severity: str, title: str, detail: str, count: int, deduction: int) -> QualityIssue:
    return QualityIssue(code=code, severity=severity, title=title, detail=detail, count=int(count), deduction=int(deduction))

def assess_quality(df: pd.DataFrame, mapping: dict[str, str]) -> QualityResponse:
    issues: list[QualityIssue] = []
    healthy: list[str] = []
    rows = max(len(df), 1)
    duplicate_count = int(df.duplicated().sum())
    if duplicate_count:
        rate = duplicate_count / rows
        issues.append(_issue("duplicates", "medium" if rate > .02 else "low", "Potential duplicate rows", "Exact duplicate rows can inflate totals if they represent repeated imports.", duplicate_count, min(12, max(2, round(rate*100)))))
    else:
        healthy.append("No exact duplicate rows detected")

    revenue_col = mapping.get("revenue")
    if revenue_col and revenue_col in df:
        numeric = pd.to_numeric(df[revenue_col], errors="coerce")
        invalid = int(numeric.isna().sum() - df[revenue_col].isna().sum())
        missing = int(df[revenue_col].isna().sum())
        negative = int((numeric < 0).sum())
        valid_rate = numeric.notna().mean()
        if invalid or missing:
            count = invalid + missing
            issues.append(_issue("invalid_revenue", "high" if count/rows > .05 else "medium", "Invalid revenue values", "Revenue contains missing or non-numeric values that are excluded from aggregates.", count, min(18, max(3, round(count/rows*120)))))
        else:
            healthy.append(f"Revenue is {valid_rate*100:.1f}% numeric")
        if negative:
            issues.append(_issue("negative_revenue", "medium", "Negative revenue values", "Negative values may be legitimate refunds, but should be reviewed before reporting.", negative, min(8, max(2, round(negative/rows*100)))))
        else:
            healthy.append("No negative revenue values detected")
        clean = numeric.dropna()
        if len(clean) >= 8:
            q1, q3 = clean.quantile([.25,.75]); iqr = q3-q1
            if iqr > 0:
                outliers = int(((clean < q1-1.5*iqr)|(clean > q3+1.5*iqr)).sum())
                if outliers:
                    issues.append(_issue("revenue_outliers", "low", "Revenue outliers", "High or low values outside the IQR range are flagged for review, not removed automatically.", outliers, min(6, max(1, round(outliers/rows*60)))))
    else:
        issues.append(_issue("missing_revenue_mapping", "high", "Revenue is not mapped", "A revenue field is required for sales analytics.", rows, 35))

    date_col = mapping.get("date")
    if date_col and date_col in df:
        parsed = pd.to_datetime(df[date_col], errors="coerce", format="mixed")
        invalid_dates = int(parsed.isna().sum())
        if invalid_dates:
            issues.append(_issue("invalid_dates", "medium" if invalid_dates/rows > .02 else "low", "Invalid dates", "Rows with unparseable dates are excluded from time-series comparisons.", invalid_dates, min(10, max(1, round(invalid_dates/rows*100)))))
        else:
            healthy.append("All mapped dates parse successfully")

    customer_col = mapping.get("customer")
    if customer_col and customer_col in df:
        missing_customers = int(df[customer_col].isna().sum())
        if missing_customers:
            issues.append(_issue("missing_customer", "low", "Missing customer IDs", "Rows without customer IDs remain in revenue totals but cannot contribute to customer-level analysis.", missing_customers, min(5, max(1, round(missing_customers/rows*50)))))

    category_col = mapping.get("category")
    if category_col and category_col in df:
        series = df[category_col].dropna().astype(str).str.strip()
        if len(series):
            canonical = series.str.lower()
            if canonical.nunique() == series.nunique(): healthy.append("Category labels are consistent")

    score = max(0, 100 - sum(i.deduction for i in issues))
    grade = "Excellent" if score >= 90 else "Good" if score >= 80 else "Fair" if score >= 65 else "Needs attention"
    return QualityResponse(score=score, grade=grade, rows=len(df), columns=len(df.columns), issues=issues, healthy_checks=healthy[:6])
