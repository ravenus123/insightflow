from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, File, HTTPException, UploadFile

from app.core.config import settings
from app.core.exceptions import InvalidDatasetError
from app.schemas.analytics import AnalyticsResponse
from app.schemas.dataset import AnalyzeRequest, DatasetUploadResponse
from app.services.analytics_service import analyze_sales
from app.services.column_detector import detect_columns
from app.services.dataset_parser import read_csv_dataset

router = APIRouter(prefix="/datasets", tags=["datasets"])


def dataset_path(dataset_id: str) -> Path:
    return settings.temp_dir / f"{dataset_id}.csv"


@router.post("/upload", response_model=DatasetUploadResponse)
async def upload_dataset(file: UploadFile = File(...)) -> DatasetUploadResponse:
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=415, detail="V0.1 supports CSV files only.")

    content = await file.read()
    if len(content) > settings.max_upload_mb * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"Maximum upload size is {settings.max_upload_mb} MB.")

    dataset_id = str(uuid4())
    path = dataset_path(dataset_id)
    path.write_bytes(content)

    try:
        df = read_csv_dataset(path)
    except InvalidDatasetError as exc:
        path.unlink(missing_ok=True)
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    preview = df.head(20).where(df.head(20).notna(), None).to_dict(orient="records")
    return DatasetUploadResponse(
        dataset_id=dataset_id,
        filename=file.filename,
        rows=len(df),
        columns=[str(c) for c in df.columns],
        preview=preview,
        detected_mapping=detect_columns(df),
    )


@router.post("/{dataset_id}/analyze", response_model=AnalyticsResponse)
def analyze_dataset(dataset_id: str, payload: AnalyzeRequest) -> AnalyticsResponse:
    path = dataset_path(dataset_id)
    if not path.exists():
        raise HTTPException(status_code=404, detail="Dataset not found or expired.")
    try:
        df = read_csv_dataset(path)
        return analyze_sales(df, payload.mapping)
    except InvalidDatasetError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
