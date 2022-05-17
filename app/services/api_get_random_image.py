import requests
import json

def get_dog_picture():
    dog_picture= requests.get("https://dog.ceo/api/breeds/image/random")
    return dog_picture.json().get("message")
