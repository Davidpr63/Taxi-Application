import os
from datetime import datetime, timedelta
from jose import jwt
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
ISSUER = os.getenv("JWT_ISSUER")
AUDIENCE = os.getenv("JWT_AUDIENCE")
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({
        "exp": expire,
        "iss": ISSUER,
        "aud": AUDIENCE
    })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_row_key_from_token(token: str) -> str:
    try:
        payload = decode_token(token)
        row_key = payload.get("sub")
        if row_key is None:
            return "invalid token"
        return row_key
    except Exception as e:
        print("An error was occurred while trying to get row_key from jwt : ", e)

def decode_token(token: str):
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
        audience=AUDIENCE,
        issuer=ISSUER
    )