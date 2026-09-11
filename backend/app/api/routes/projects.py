from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Project
from app.schemas.project import ProjectCreate, ProjectOut
router=APIRouter(prefix="/projects",tags=["projects"])
@router.get("",response_model=list[ProjectOut])
def list_projects(db:Session=Depends(get_db)): return list(db.scalars(select(Project).order_by(Project.updated_at.desc())).all())
@router.post("",response_model=ProjectOut,status_code=201)
def create_project(payload:ProjectCreate,db:Session=Depends(get_db)):
    item=Project(**payload.model_dump());db.add(item);db.commit();db.refresh(item);return item
