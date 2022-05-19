from typing import Any, Dict, List, Optional, TypeVar, Union

from passlib.hash import bcrypt

from app.infra.postgres.crud.user import UserCrud, user_crud
from app.schemas.user_schema import CreateUser, UserInfo, UserUpdate
from app.services.upload_file import upload_file

QueryType = TypeVar("QueryType", bound=UserCrud)


class ServiceUser:
    def __init__(self, query: QueryType):
        self.query = query

    async def get_users(self) -> Optional[List[UserInfo]]:
        users = await self.query.get_all()
        return users

    def upload_file(self):
        file_uploaded = upload_file()
        return file_uploaded

    async def update_user(self, *, id: int, update: UserUpdate) -> Union[dict, None]:
        if update.password:
            update.password = bcrypt.hash(update.password)
        user_to_update = await self.query.update(id=id, obj_in=update)
        return user_to_update

    async def delete_user(self, *, id: int) -> Union[dict, None]:
        deleted = await self.query.delete(id=id)
        return deleted

    async def create_users(self, user_created: CreateUser) -> Optional[UserInfo]:
        user_created.password = bcrypt.hash(user_created.password)
        user = await self.query.create(obj_in=user_created)
        return user

    async def find_user_email(self, *, email: str) -> Union[Dict, None]:
        user = await self.query.get_by_field(email=email)
        if user:
            return user
        return None

    async def find_user_id(self, *, id: int) -> Union[Dict, None]:
        user = await self.query.get_by_field(id=id)
        if user:
            return user
        return None

    async def get_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        user = await self.query.get_by_field(email=email)
        if user:
            return user
        return None

    async def get_by_element(self, **content) -> Union[dict, None]:
        user = await self.get_by_element(**content)
        if user:
            return user
        return None


user_service = ServiceUser(query=user_crud)
