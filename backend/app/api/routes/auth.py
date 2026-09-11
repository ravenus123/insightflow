from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.services.auth_service import hash_password, make_token, verify_password
router=APIRouter(prefix="/auth",tags=["auth"])
@router.post("/register",response_model=TokenResponse)
def register(payload:RegisterRequest,db:Session=Depends(get_db)):
    if db.scalar(select(User).where(User.email==payload.email.lower())): raise HTTPException(409,"Email already registered.")
    user=User(email=payload.email.lower(),name=payload.name,password_hash=hash_password(payload.password));db.add(user);db.commit();db.refresh(user)
    return TokenResponse(access_token=make_token(user.id,user.email))
@router.post("/login",response_model=TokenResponse)
def login(payload:LoginRequest,db:Session=Depends(get_db)):
    user=db.scalar(select(User).where(User.email==payload.email.lower()))
    if not user or not verify_password(payload.password,user.password_hash): raise HTTPException(401,"Invalid email or password.")
    return TokenResponse(access_token=make_token(user.id,user.email))
