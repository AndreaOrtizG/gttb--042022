from operator import index
from wsgiref.simple_server import server_version
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import requests

    
Base = declarative_base()

class User(Base):
    __tablename__ = "user" 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))