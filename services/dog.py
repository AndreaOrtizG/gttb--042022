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
from models.models import Dog
from dotenv import load_dotenv
from services.api_get_random_image import get_dog_picture
class ServiceDog:

    def get_dogs():
        dogs= db.session.query(Dog).all()
        return dogs

    def get_by_name(name: str):
        dogs_name= db.session.query(Dog).where(Dog.name==name).all()
        return dogs_name

    def get_dogs_adopted():
        dogs_adopted= db.session.query(Dog).where(Dog.is_adopted == True).all()
        print(dogs_adopted)
        return dogs_adopted

    
        

    def update_dogs(name:str, dog:SchemaDog):
        dog_to_updated= db.session.query(Dog).where(Dog.name==name).all()
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

    def create_dogs(dog: SchemaDog):
        picture_update= get_dog_picture()
        dog_created = Dog(name=dog.name, picture= picture_update , is_adopted= dog.is_adopted, id_user=dog.id_user)
        ##task = sum.delay(5,2,3)
        db.session.add(dog_created)
        db.session.commit()
        return dog_created
