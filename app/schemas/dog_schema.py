
from datetime import datetime
from lib2to3.pgen2.token import OP
from typing import Optional, List
from pydantic import BaseModel
from pydantic.networks import EmailStr

from app.schemas.user_schema import UserBase;

class DogBase(BaseModel):
    id:int
    user_adopter_email: Optional[EmailStr]
    is_adopted: bool
    
    
    class Config:
        orm_mode = True

class CreateDog(DogBase):
    id: int
    name: str
    user_adopter_id: Optional[int]
    user_creator_id: Optional[int]
    picture: str
    is_adopted: bool
    user_adopter_email: Optional[EmailStr]
    #created_date: datetime

class UpdateDog(BaseModel):
    name: Optional[str]
    is_adopted:bool

class DogData(BaseModel):
    id: int
    name: Optional[str]


    

class DogInfo(CreateDog):
    is_adopted: bool
    pass
    

