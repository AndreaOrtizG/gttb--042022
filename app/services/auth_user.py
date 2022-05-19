from typing import Optional

from app.core.auth import password_verify
from app.core.config_fastapi import Settings, get_settings
from app.infra.postgres.models.user import User
from app.services.user import user_service

settings: Settings = get_settings()


class ServiceAuth:
    def __init__(self):
        return

    async def authenticate_email(self, *, email: str, password: str) -> Optional[User]:
        user_authenticate = await user_service.get_by_email(email=email)
        if not user_authenticate:
            return None
        if not password_verify(password, user_authenticate.password):
            return None
        return user_authenticate


auth_service = ServiceAuth()
