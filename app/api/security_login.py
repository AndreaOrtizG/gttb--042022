from fastapi import HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError

from app.core.config_fastapi import Settings, get_settings
from app.infra.postgres.models.user import User
from app.schemas.token import TokenPayload
from app.services.user import user_service

settings: Settings = get_settings()

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/api/users/login")


async def get_current_user(token: str = Security(oauth2_schema)) -> User:

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    user = await user_service.find_user_id(id=data.id)
    if user:
        return user
    raise HTTPException(status_code=404)


def get_current_active_user(current_user=Security(get_current_user)):
    return current_user
