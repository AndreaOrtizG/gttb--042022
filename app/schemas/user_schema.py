from typing import Optional

from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    id: int
    name: str
    last_name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

    class Config:
        orm_mode = True


class UserInfo(UserBase):
    pass


class User(UserInfo):
    pass
