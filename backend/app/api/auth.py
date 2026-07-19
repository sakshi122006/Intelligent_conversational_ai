from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginIn(BaseModel):
    username: str
    password: str

@router.post('/login')
async def login(payload: LoginIn):
    # TODO: validate credentials and return JWT
    if payload.username == 'admin':
        return {"access_token": "fake-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
