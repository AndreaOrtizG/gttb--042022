from codecs import namereplace_errors
from curses.ascii import US
import email
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
from schemas.user_schema import User as SchemaUser
from models.models import User
from dotenv import load_dotenv
from services.upload_file import upload_file

class ServiceUser:

    def get_users():
        users= db.session.query(User).all()
        return users

    def upload_file():
        file_uploaded= upload_file()
        return file_uploaded
    
    def update_users(name:str, user:SchemaUser):
        user_to_updated= db.session.query(User).where(User.name==name).first()
        user_to_updated.name= user.name
        user_to_updated.last_name= user.last_name
        user_to_updated.email= user.email
        db.session.commit()
        return user_to_updated

    def delete_users(name: str):
        user_to_delete=db.session.query(User).where(User.name==name).first()
        db.session.delete(user_to_delete)
        db.session.commit()
        return user_to_delete

    def create_users(user: SchemaUser):
        user_created = User(name=user.name,last_name=user.last_name, email= user.email)
        db.session.add(user_created)
        db.session.commit()
        return signJWT(user_created.email)
