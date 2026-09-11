from typing import Literal
from pydantic import BaseModel
class QualityIssue(BaseModel):
    code: str
    severity: Literal["low","medium","high"]
    title: str
    detail: str
    count: int
    deduction: int
class QualityResponse(BaseModel):
    score: int
    grade: str
    rows: int
    columns: int
    issues: list[QualityIssue]
    healthy_checks: list[str]
