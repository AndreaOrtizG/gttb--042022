import os
from urllib import response 
from requests import post
import json

def upload_file():
    url="https://gttb.guane.dev/api/files"
    path= r"./services/files"
    files = {
        "file": ("upload.txt",open(os.path.join(path, "upload.txt"), "rb")),
    }

    response = post(url, files=files)
    return response.json()
