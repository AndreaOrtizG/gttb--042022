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

router = APIRouter()

@router.get("/")
def get_dogs():
    dogs= db.session.query(Dog).all()

    if dogs:
        return dogs
    raise HTTPException(status_code=404, detail="Dogs not found")


@router.get("/{name}")
async def get_dogs_name(name: str):
    dogs_name= db.session.query(Dog).where(Dog.name==name).all()

    if dogs_name: 
        return dogs_name
    raise HTTPException(status_code=404, detail="Dog not found")


@router.get("/is_adopted")
def get_dogs_adopted():
    dogs_adopted= db.session.query(Dog).where(Dog.is_adopted == True).all()

    if dogs_adopted:
        return dogs_adopted
    raise HTTPException(status_code=404, detail="Dogs adopted not found")


@router.put("/{name}")
def update_dogs(name:str, dog:SchemaDog):
    dog_to_updated= db.session.query(Dog).where(Dog.name==name).first()
    dog_to_updated.name= dog.name
    dog_to_updated.is_adopted= dog.is_adopted
    dog_to_updated.id_user= dog.id_user
    db.session.commit()

    if dog_to_updated:
        return dog_to_updated
    return none



@router.delete("/{name}")
def delete_dog(name:str):
    dog_to_delete=db.session.query(Dog).where(Dog.name==name).first()
    db.session.delete(dog_to_delete)
    db.session.commit()
    if dog_to_delete:
        return dog_to_delete
    return none


@router.post("/", response_model=SchemaDog, dependencies=[Depends(JWTBearer())])
def add_dog(dog: SchemaDog) :
    dog_created = Dog(name=dog.name, picture= picture_update , is_adopted= dog.is_adopted, id_user=dog.id_user)
    ##task = sum.delay(5,2,3)
    db.session.add(dog_created)
    db.session.commit()
    return dog_created
    if admin: 




