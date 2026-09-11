from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.auth import router as auth_router
from app.api.routes.datasets import router as datasets_router
from app.api.routes.health import router as health_router
from app.api.routes.projects import router as projects_router
from app.core.config import settings
from app.core.logging import configure_logging
from app.db import Base, engine
import app.models  # noqa: F401

configure_logging()
app=FastAPI(title=settings.app_name,version="1.0.0",description="Analytics ingestion, quality and deterministic insight API for InsightFlow.")
app.add_middleware(CORSMiddleware,allow_origins=[settings.frontend_origin],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
@app.on_event("startup")
def create_dev_schema(): Base.metadata.create_all(bind=engine)
app.include_router(health_router,prefix=settings.api_prefix)
app.include_router(auth_router,prefix=settings.api_prefix)
app.include_router(projects_router,prefix=settings.api_prefix)
app.include_router(datasets_router,prefix=settings.api_prefix)
