from codecs import namereplace_errors
from pyexpat import model
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schema import Dog as SchemaDog
from schema import User as SchemaUser
from models import Dog 
from models import User 
from dotenv import load_dotenv
import os


load_dotenv(".env")
app= FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/dogs/")
def get_dogs():
    dogs= db.session.query(Dog).all()

    return dogs

@app.get("/users/")
def get_users():
    users= db.session.query(User).all()

    return users

@app.get("/dogs/is_adopted")
def get_dogs_adopted():
    dogs_adopted= db.session.query(Dog).where(Dog.is_adopted == True).all()
    return dogs_adopted

@app.get("/dogs/{name}")
async def get_dogs_name(name: str):
    dogs_name= db.session.query(Dog).where(Dog.name==name).all()
    return dogs_name


@app.put("/dogs/{name}")
def update_dogs(name:str, dog:SchemaDog):
    dog_to_updated= db.session.query(Dog).where(Dog.name==name).first()
    dog_to_updated.name= dog.name
    dog_to_updated.picture= dog.picture
    dog_to_updated.is_adopted= dog.is_adopted
    dog_to_updated.id_user= dog.id_user

    db.session.commit()
    return dog_to_updated

@app.delete("/dogs/{name}")
def delete_dog(name:str):
    dog_to_delete=db.session.query(Dog).where(Dog.name==name).first()
    
    db.session.delete(dog_to_delete)
    db.session.commit()
    return dog_to_delete

@app.post("/dog/", response_model=SchemaDog)
def add_dog(dog: SchemaDog):
    admin = Dog(name=dog.name, picture=dog.picture, is_adopted= dog.is_adopted, id_user=dog.id_user)
    db.session.add(admin)
    db.session.commit()
    return admin

@app.post("/user/", response_model=SchemaUser)
def add_user(user: SchemaUser):
    admin = User(name=user.name,last_name=user.last_name, email= user.email )
    db.session.add(admin)
    db.session.commit()
    return admin

    