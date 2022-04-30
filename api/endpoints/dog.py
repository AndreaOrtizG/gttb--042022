from codecs import namereplace_errors
from pyexpat import model
from typing import List
from webbrowser import get
from auth.auth_bearer import JWTBearer
import requests
from rsa import sign
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from auth.auth_handler import signJWT
from schemas.dog_schema import Dog as SchemaDog
from models.dog_model import Dog 
from dotenv import load_dotenv
from fastapi import APIRouter
from services.dog import ServiceDog

router = APIRouter()

@router.get("/")
def get_all_dogs():
    dogs= get_dogs()
    if dogs:
        return dogs
    raise HTTPException(status_code=404, detail="Dogs not found")


@router.get("/{name}")
def get_dogs_name():
    dogs_name= ServiceDog.get_by_name()
    if dogs_name: 
        return dogs_name
    raise HTTPException(status_code=404, detail="Dog not found")


@router.get("/is_adopted")
def get_dogs_adopted():
    dogs_adopted= ServiceDog.dogs_adopted()
    if dogs_adopted:
        return dogs_adopted
    raise HTTPException(status_code=404, detail="Dogs adopted not found")


@router.put("/{name}")
def update_dogs(name:str, dog:SchemaDog):
    dog_to_updated= ServiceDog.update_dogs(name = name)
    if dog_to_updated:
        return dog_to_updated
    return none


@router.delete("/{name}")
def delete_dog(name:str):
    dog_to_delete = ServiceDog.delete_dogs(name = name)
    if dog_to_delete:
        return dog_to_delete
    return none


@router.post("/", response_model=SchemaDog, dependencies=[Depends(JWTBearer())])
def add_dog(dog: SchemaDog) :
    dog_created = ServiceDog.create_dogs()
    if dog_created:
        return dog_created
    return None 




