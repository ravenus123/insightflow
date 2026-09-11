from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from app.core.config import settings
from app.core.exceptions import InvalidDatasetError
from app.schemas.analytics import AnalyticsResponse
from app.schemas.dataset import AnalyzeRequest, DatasetUploadResponse
from app.schemas.quality import QualityResponse
from app.services.analytics_service import analyze_sales
from app.services.column_detector import detect_columns
from app.services.dataset_parser import read_dataset
from app.services.quality_service import assess_quality

router=APIRouter(prefix="/datasets",tags=["datasets"])

def dataset_path(dataset_id: str) -> Path:
    matches=list(settings.data_dir.glob(f"{dataset_id}.*"))
    if not matches: raise HTTPException(status_code=404,detail="Dataset not found or expired.")
    return matches[0]

@router.post("/upload",response_model=DatasetUploadResponse)
async def upload_dataset(file: UploadFile=File(...))->DatasetUploadResponse:
    if not file.filename: raise HTTPException(status_code=400,detail="Filename is required.")
    ext=Path(file.filename).suffix.lower()
    if ext not in {".csv",".xlsx"}: raise HTTPException(status_code=415,detail="InsightFlow supports CSV and XLSX files.")
    content=await file.read()
    if not content: raise HTTPException(status_code=422,detail="The uploaded file is empty.")
    if len(content)>settings.max_upload_mb*1024*1024: raise HTTPException(status_code=413,detail=f"Maximum upload size is {settings.max_upload_mb} MB.")
    dataset_id=str(uuid4()); path=settings.data_dir/f"{dataset_id}{ext}"; path.write_bytes(content)
    try: df=read_dataset(path)
    except InvalidDatasetError as exc: path.unlink(missing_ok=True); raise HTTPException(status_code=422,detail=str(exc)) from exc
    preview=df.head(20).where(df.head(20).notna(),None).to_dict(orient="records")
    return DatasetUploadResponse(dataset_id=dataset_id,filename=file.filename,rows=len(df),columns=[str(c) for c in df.columns],preview=preview,detected_mapping=detect_columns(df))

@router.post("/{dataset_id}/quality",response_model=QualityResponse)
def quality_dataset(dataset_id:str,payload:AnalyzeRequest)->QualityResponse:
    try: return assess_quality(read_dataset(dataset_path(dataset_id)),payload.mapping)
    except InvalidDatasetError as exc: raise HTTPException(status_code=422,detail=str(exc)) from exc

@router.post("/{dataset_id}/analyze",response_model=AnalyticsResponse)
def analyze_dataset(dataset_id:str,payload:AnalyzeRequest)->AnalyticsResponse:
    try: return analyze_sales(read_dataset(dataset_path(dataset_id)),payload.mapping)
    except InvalidDatasetError as exc: raise HTTPException(status_code=422,detail=str(exc)) from exc

@router.get("/{dataset_id}/export")
def export_dataset(dataset_id:str):
    path=dataset_path(dataset_id)
    return FileResponse(path,filename=path.name,media_type="application/octet-stream")
