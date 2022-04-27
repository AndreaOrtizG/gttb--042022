from operator import index
from wsgiref.simple_server import server_version
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import requests

    
Base = declarative_base()


class Dog(Base):
    __tablename__ = "dog" 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    picture = Column(String(500))
    is_adopted = Column(Boolean)
    create_date = Column(DateTime, server_default=func.now())
    id_user = Column(Integer, ForeignKey("user.id"))

    user = relationship("User")

class User(Base):
    __tablename__ = "user" 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))