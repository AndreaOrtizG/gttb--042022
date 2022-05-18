
from distutils import ccompiler
from typing import List, Union, Optional
import uvicorn
from fastapi import  Depends, HTTPException,APIRouter
from app.infra.postgres.models.user import User
from app.schemas.dog_schema import  DogInfo,DogBase, UpdateDog, DogData
from app.services.dog import dog_service
from app.services.user import user_service
from app.celery_worker import task_time
import asyncio
from app.api import security_login


router = APIRouter()

@router.get("/", response_model= Union[List[DogInfo], None])
async def get_all_dogs() -> Optional[List[DogInfo]]:
    dogs= await dog_service.get_dogs()
    
    return dogs
    

@router.get("/is_adopted", response_model= Union[List[DogData], None])
async def get_dogs_adopted()-> Optional[List[DogData]]:
    dogs_adopted= await dog_service.get_by_element_list(is_adopted=True)
    if dogs_adopted:
        return dogs_adopted
    raise HTTPException(status_code=404, detail="Dogs adopted not found")



@router.get("/{name}", response_model=DogInfo)
async def get_dogs_name(name:str):
    dogs_name= await dog_service.find_dog_name(name=name)
    if dogs_name: 
        return dogs_name
    raise HTTPException(status_code=404, detail="Dog not found")



@router.put("/{name}" , response_model= Union[DogInfo,None])
async def update_dogs(dog_to_update: UpdateDog, name: str,current_user: User= Depends(security_login.get_current_active_user) ):
    
    dog_to_updated= await dog_service.update_dogs(update= dog_to_update, name=name, user= current_user)
    if dog_to_updated:
        return dog_to_updated
    return None


@router.delete("/{name}" , response_model= Union[DogInfo,None])
async def delete_dog(name:str, current_user: User= Depends(security_login.get_current_active_user)):
    dog= await dog_service.find_dog_name(name= name)
    if dog: 
        dog_to_delete = await dog_service.delete_dogs(name=name, user=current_user)
        if dog_to_delete:
            return dog_to_delete
        raise HTTPException(status_code=404, detail="Dog not found") 


@router.post("/{name}", response_model=Union[DogInfo, None])
async def add_dog(dog: DogBase, name: str, current_user: User = Depends(security_login.get_current_active_user)) -> Optional[DogInfo]:
    dog_created = await dog_service.create_dogs(dog_created=dog, name=name, user_creator= current_user)
    task = task_time.delay(10)
    if dog_created:
        print (task)
        return dog_created
    return None 




