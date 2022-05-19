from typing import Union

from fastapi import HTTPException

from app.infra.postgres.crud.base import CrudBase
from app.infra.postgres.models.user import User
from app.schemas.user_schema import CreateUser, UserUpdate


class UserCrud(CrudBase[User, CreateUser, UserUpdate]):
    async def create(self, *, obj_in: CreateUser) -> Union[dict, None]:
        user_created = obj_in.dict()
        user_existed = await self.get_by_field(email=user_created["email"])
        if user_existed:
            raise HTTPException(status_code=409, detail="User already exist")
        user = await self.model.create(**user_created)
        return user

    async def delete(self, *, id: str) -> Union[dict, None]:
        user_to_delete = await self.get_by_field(id=id)
        if user_to_delete:
            model = await self.model.filter(id=id).delete()
            return model
        else:
            raise HTTPException(status_code=404, detail="User not found")

    async def update(self, *, id: int, obj_in: UserUpdate) -> Union[dict, None]:
        user_info = await self.get_by_id(id=id)
        if user_info:
            user_to_update = await self.model.filter(id=id).update(**obj_in.dict())
            user_to_update = await self.get_by_id(id=user_info.id)
            return user_to_update
        else:
            raise HTTPException(status_code=404, detail="User not Found")


user_crud = UserCrud(model=User)
