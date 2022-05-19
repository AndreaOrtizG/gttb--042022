from typing import Optional

from pydantic import BaseModel
from pydantic.networks import EmailStr


class DogBase(BaseModel):
    id: int
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


class UpdateDog(BaseModel):
    name: Optional[str]
    is_adopted: bool


class DogData(BaseModel):
    id: int
    name: Optional[str]


class DogInfo(CreateDog):
    is_adopted: bool
    pass
