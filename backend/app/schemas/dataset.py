from typing import Any
from pydantic import BaseModel, Field

class ColumnDetection(BaseModel):
    column: str
    confidence: float = Field(ge=0, le=1)

class DatasetUploadResponse(BaseModel):
    dataset_id: str
    filename: str
    rows: int
    columns: list[str]
    preview: list[dict[str, Any]]
    detected_mapping: dict[str, ColumnDetection]

class AnalyzeRequest(BaseModel):
    mapping: dict[str, str]
