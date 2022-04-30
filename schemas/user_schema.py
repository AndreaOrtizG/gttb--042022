import datetime
from lib2to3.pytree import Base
from typing import Optional
from unicodedata import name
from pydantic import BaseModel, EmailStr
import requests

class User(BaseModel):
    name: str
    last_name: str
    email: EmailStr

    class Config:
        orm_mode= True
