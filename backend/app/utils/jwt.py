# simple JWT util functions (placeholder)
from datetime import datetime, timedelta
from jose import jwt
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'change_me')
ALGORITHM = os.getenv('ALGORITHM', 'HS256')

def create_access_token(data: dict, expires_delta: int = 60):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded
