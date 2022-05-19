from typing import Any, Dict, List, Optional, TypeVar, Union

from app.infra.postgres.crud.dog import DogCrud, dog_crud
from app.schemas.dog_schema import CreateDog, DogBase, DogInfo, UpdateDog
from app.schemas.user_schema import User, UserInfo
from app.services.api_get_random_image import get_dog_picture
from app.services.user import user_service

QueryType = TypeVar("QueryType", bound=DogCrud)


class ServiceDog:
    def __init__(self, query: QueryType):
        self.query = query

    async def get_dogs(self) -> Optional[List[DogInfo]]:
        dogs = await self.query.get_all()
        return dogs

    async def get_by_name(self, *, name: str) -> Optional[Dict[str, Any]]:
        dogs_name = await self.query.get_by_field(name=name)
        if dogs_name:
            return dogs_name
        return None

    async def update_dogs(self, *, update: UpdateDog, name: str, user: User):
        picture_update = get_dog_picture()
        update.picture = picture_update
        dog_to_update = await self.query.update(
            name=name, dog_updated=update, user=user
        )
        return dog_to_update

    async def delete_dogs(self, *, name: str, user: User) -> Union[dict, None]:
        deleted = await self.query.delete(name=name, user=user)
        return deleted

    async def create_dogs(
        self, *, dog_created: DogBase, name: str, user_creator: UserInfo
    ) -> Union[dict, None]:
        picture_update = get_dog_picture()
        dog_to_create = CreateDog(
            id=dog_created.id,
            name=name,
            picture=picture_update,
            is_adopted=dog_created.is_adopted,
        )
        if dog_created.user_adopter_email:
            adopter = await user_service.find_user_email(
                email=dog_created.user_adopter_email
            )
            dog_to_create.user_adopter_id = adopter.id
            dog_to_create.user_creator_id = user_creator.id
            dog_to_create.user_adopter_email = dog_created.user_adopter_email
            print(dog_to_create.user_adopter_email)
            dog_create = await self.query.create_dog(obj_in=dog_to_create)
            return dog_create

    async def find_dog_name(self, *, name: str) -> Optional[Dict[str, Any]]:
        dog = await self.query.get_by_field(name=name)
        if dog:
            return dog
        return None

    async def get_by_element(self, **content) -> Union[dict, None]:
        dog = await self.query.get_by_field(**content)
        if dog:
            return dog
        return None

    async def get_by_element_list(self, **content) -> Union[dict, None]:
        dog = await self.query.get_by_field_list(**content)
        if dog:
            return dog
        return None


dog_service = ServiceDog(query=dog_crud)
