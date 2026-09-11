import pandas as pd
from app.services.quality_service import assess_quality

def test_quality_score_explains_issues():
    df=pd.DataFrame({"revenue":[10,20,-5,None],"date":["2026-01-01","bad","2026-01-03","2026-01-04"],"customer":["A","B",None,"D"]})
    result=assess_quality(df,{"revenue":"revenue","date":"date","customer":"customer"})
    assert result.score < 100
    assert any(i.code=="negative_revenue" for i in result.issues)
    assert any(i.code=="invalid_dates" for i in result.issues)
