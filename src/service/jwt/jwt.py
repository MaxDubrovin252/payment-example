import jwt
from datetime import datetime, timedelta
from core.config import settings
from fastapi import HTTPException

def create_access_token(
    username:str,
    user_id:int,
    exp_time:int = 1,
        
)->str:
    payload = {
        "sub":username,
        "user_id":user_id,
        "ias":datetime.utcnow(),
        "exp":datetime.utcnow() + timedelta(hours=exp_time)
    }
    
    token = jwt.encode(
        payload=payload,
        key=settings.jwt.secret_key,
        algorithm=settings.jwt.algo,
    )
    return token

def verify_token(token:str)->bool:
    try:
        is_correct = jwt.decode(
        jwt=token,
        key=settings.jwt.secret_key,
        algorithms=[settings.jwt.algo]
        )
        return is_correct
    except jwt.InvalidTokenError as e :
        raise HTTPException(status_code=401,detail=e)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401,detail="time has expired")
    
    