from http.client import HTTPException
from typing import List, Union
from venv import create
from app.infra.postgres.crud.base import CrudBase, crud
from app.infra.postgres.models.dog import Dog
from app.infra.postgres.models.user import User
from app.schemas.dog_schema import CreateDog, UpdateDog

class DogCrud(CrudBase[Dog, CreateDog, UpdateDog]):

    async def create_dog(self,*, obj_in: CreateDog) -> Union[dict,None]:
        info_dog = obj_in.dict()
        name_existed= await self.get_by_field(name=info_dog["name"])
        type_dog= type(info_dog["user_adopter_id"])
        if name_existed:
            raise HTTPException(status_code=409, detail= "Already exists dog with the same name")
    

        dog_created = await self.model.create(**info_dog)
        return dog_created


    async def update(self, *, name:str, dog_updated: UpdateDog, user: User) -> Union[dict, None]:
        dog_info= await self.get_by_field(name=name)
        if dog_info:
            if user.id == dog_info.user_adopter_id or user.id == dog_info.user_creator_id:
                dog_to_update= await self.model.filter(name=name).update(**dog_updated.dict())
                dog_to_update= await self.get_by_field(id= dog_info.id) 
                return dog_to_update
            else:
                raise HTTPException(status_code=401, detail= "User not Authorized")

        else:
            raise HTTPException(status_code=404,detail= "Dog not found")


    async def delete (self, *, name:str, user: User) -> Union[dict, None]:
        dog_to_delete = await self.get_by_field(name=name)
        if dog_to_delete:
            if user.id == dog_to_delete.user_adopter_id or user.id == dog_to_delete.user_creator_id:
                model = await self.model.filter(name=name).first().delete()
            else: 
                raise HTTPException(status_code=401, detail= "User not Authorized")
            return dog_to_delete
        else: 
            raise HTTPException(status_code=404, detail= "Dog not found")


   


dog_crud = DogCrud(model=Dog)