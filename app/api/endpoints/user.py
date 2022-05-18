
from typing import List, Union, Optional, Any
from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth_user import auth_service
from app.services.user import user_service
from app.schemas.token import Token
from app.schemas.user_schema import CreateUser
from app.core import auth
from app.core.config_fastapi import Settings, get_settings
from app.services.auth_user import auth_service
from app.schemas.user_schema import CreateUser, UserUpdate, UserInfo
from app.services.user import user_service
import asyncio


router = APIRouter()


@router.get("/", response_model= Union[List[UserInfo], None])
async def get_all_users() -> Optional[List[UserInfo]]:
    users= await user_service.get_users()
    if users: 
        return users
    
    raise HTTPException(status_code=404, detail="Users not found")

@router.get("/upload_file")
async def upload_file():
    file_upload = user_service.upload_file()
    if file_upload:
        return file_upload
    return None

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm= Depends()) -> Any:
    user_authenticate= await auth_service.authenticate_email(email=form_data.username, password= form_data.password)
    if not user_authenticate:
        raise HTTPException(status_code=400, detail="incorrect email or password")
    return{
        "access_token": auth.create_access_token(id= user_authenticate.id, email= user_authenticate.email), "token_type":"bearer",
    }



@router.put("/{id}" , response_model= Union[UserInfo, None])
async def update_users(user_updated: UserUpdate, id:int):
    user= await user_service.update_user(id=id, update=user_updated)
    if user:
            return user
    return None


@router.delete("/{id}", response_model= Union[UserInfo,None])
async def delete_user(*, id:int) -> Optional[UserInfo]:
    user = await user_service.delete_user(id=id)
    if user: 
            return user
    else:
        raise HTTPException(status_code=404, detail="User not found") 

@router.post("/", response_model=Union[UserInfo, None])
async def add_user(*,user: CreateUser) -> Optional[UserInfo]:
    user_to_create = await user_service.create_users(user_created=user)
    ##task = task_time.delay(10)
    if user_to_create:
        ##print (task)
        return user_to_create
    return None 





