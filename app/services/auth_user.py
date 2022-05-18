from typing import Optional

from rsa import verify

from app.core.config_fastapi import Settings, get_settings
from app.schemas.user_schema import UserInfo
from app.services.user import user_service
from app.core.auth import password_verify
from app.infra.postgres.models.user import User

settings: Settings = get_settings()

class ServiceAuth:
    def __init__(self):
        return

    async def authenticate_email(self,*,email: str, password:str) -> Optional[User]:
        user_authenticate= await user_service.get_by_email(email=email)
        
        if not user_authenticate:
            return None
        if not password_verify(password, user_authenticate.password):
            return None
       # user_authenticate = User(**user_authenticate)
        return user_authenticate
          

auth_service = ServiceAuth()