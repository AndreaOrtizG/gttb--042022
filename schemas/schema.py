import datetime
from lib2to3.pytree import Base
from typing import Optional
from unicodedata import name
from pydantic import BaseModel
import requests




class Dog(BaseModel):
    name: str
    is_adopted: bool
    id_user: int

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    last_name: str
    email: str

    class Config:
        orm_mode= True

