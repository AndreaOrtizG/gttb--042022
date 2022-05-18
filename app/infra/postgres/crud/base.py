from typing import Any, Dict, List, Optional, Union, Generic

from app.schemas.general import CreateSchemaType, UpdateSchemaType, ModelType

class CrudBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model):
        self.model = model

    async def get_all(self, *, content: dict = None, skip: int = 0, limit: int = 50) -> List:
        if content:
            model = await self.model.all().filter(**content).offset(skip).limit(limit).all().values()
        else:
            model = await self.model.all().offset(skip).limit(limit).values()
        return model

    async def create(self, *, obj_in: CreateSchemaType) -> Union[dict, None]:
        model = self.model(**obj_in.dict())
        await model.save()
        return model

    async def update(self, *, id: int, obj_in: UpdateSchemaType) -> Union[dict,None]:
        model = await self.model.filter(id=id)
        if model:
            update_model = await self.model.filter(id=id).update(**obj_in.dict(exclude_unset=True))
            update_model= await self.get_by_id(id=id)
            return update_model[0]
        else: return None

    async def delete(self, *, id: int) -> int:
        delete = await self.model.filter(id=id).first().delete()
        return delete

    async def get_by_id(self, *, id: int) -> Optional[ModelType]:
        if id:
            model = await self.model.filter(id=id).first()
            if model:
                return model
            return None
        else:
            return None

    async def get_by_field(self, **kwargs: Union[str, int]) -> Optional[Dict[str, Any]]:
            model = await self.model.filter(**kwargs).first()
            if model:
                return model
            return None

    async def get_by_field_list (self, **kwargs: Union[str, int]) -> Optional[Dict[str, Any]]:
            model = await self.model.all().filter(**kwargs).values()
            if model:
                return model
            return None
    

crud=CrudBase(CrudBase)
    
   
