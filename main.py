from fastapi import FastAPI, Depends
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from api.api import api_router

import os

load_dotenv(".env")
app= FastAPI()
app.include_router(api_router, prefix="/api")

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])








    