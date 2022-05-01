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
from schemas.user_schema import User as SchemaUser
from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi import APIRouter
from services.user import ServiceUser

router = APIRouter()


@router.get("/")
def get_all_user():
    users= ServiceUser.get_users()
    if users:
        return users
    raise HTTPException(status_code=404, detail="users not found")



@router.put("/{name}")
def update_user(name:str, user:SchemaUser):
    user_to_updated= ServiceUser.update_users(name=name, user=user)
    if user_to_updated:
        return user_to_updated
    return None


@router.delete("/{name}")
def delete_user(name:str):
    user_to_delete = ServiceUser.delete_users(name=name)
    if user_to_delete:
        return user_to_delete
    return None


@router.post("/")
def add_user(user: SchemaUser) :
    user_created = ServiceUser.create_users(user)
    if user_created:
        return user_created, user_created.id
    return None 




