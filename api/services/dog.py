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

class ServiceDog:

    def get_dogs():
        dogs= db.session.query(Dog).all()
        return dogs

    def get_by_name(name: str):
        dogs_name= db.session.query(Dog).where(Dog.name==name).all()
        return dogs_name

    def dogs_adopted(name: str):
        dogs_adopted= db.session.query(Dog).where(Dog.is_adopted == True).all()
        return dogs_adopted

    def update_dogs(name:str, dog:SchemaDog):
        dog_to_updated= db.session.query(Dog).where(Dog.name==name).first()
        dog_to_updated.name= dog.name
        dog_to_updated.is_adopted= dog.is_adopted
        dog_to_updated.id_user= dog.id_user
        db.session.commit()
        return dog_to_updated

    def delete_dogs(name: str):
        dog_to_delete=db.session.query(Dog).where(Dog.name==name).first()
        db.session.delete(dog_to_delete)
        db.session.commit()
        return dog_to_delete

    def create_dogs(dog: SchemaDog)
        dog_created = Dog(name=dog.name, picture= picture_update , is_adopted= dog.is_adopted, id_user=dog.id_user)
        ##task = sum.delay(5,2,3)
        db.session.add(dog_created)
        db.session.commit()
        return dog_created
