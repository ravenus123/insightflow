import base64, hashlib, hmac, os
from datetime import datetime, timedelta, timezone
import jwt
from app.core.config import settings

def hash_password(password:str)->str:
    salt=os.urandom(16); digest=hashlib.pbkdf2_hmac("sha256",password.encode(),salt,310_000)
    return f"pbkdf2_sha256$310000${base64.b64encode(salt).decode()}${base64.b64encode(digest).decode()}"
def verify_password(password:str,stored:str)->bool:
    try:
        _,rounds,salt_b64,digest_b64=stored.split("$"); salt=base64.b64decode(salt_b64); expected=base64.b64decode(digest_b64)
        actual=hashlib.pbkdf2_hmac("sha256",password.encode(),salt,int(rounds)); return hmac.compare_digest(actual,expected)
    except Exception: return False
def make_token(user_id:int,email:str)->str:
    exp=datetime.now(timezone.utc)+timedelta(minutes=settings.jwt_exp_minutes)
    return jwt.encode({"sub":str(user_id),"email":email,"exp":exp},settings.jwt_secret,algorithm="HS256")
