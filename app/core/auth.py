from jose import jwt
from passlib.context import CryptContext

from app.core.config_fastapi import Settings, get_settings

settings: Settings = get_settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(id: int, email: str) -> str:
    data = {"email": email, "id": id}
    encoded_jwt = jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def password_verify(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
