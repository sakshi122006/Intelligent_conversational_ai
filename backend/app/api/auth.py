from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import os
import datetime

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post('/login')
async def login(req: LoginRequest):
    # TODO: replace with real authentication (MSSQL lookup, password hash)
    if req.username == 'admin' and req.password == 'admin':
        return {"access_token":"fake-jwt-token","token_type":"bearer"}
    raise HTTPException(status_code=401, detail='Invalid credentials')

@router.get('/me')
async def me():
    # TODO: decode JWT and fetch user profile
    return {"username":"admin","role":"Admin"}
