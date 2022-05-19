import os

from requests import post


def upload_file():
    url = "https://gttb.guane.dev/api/files"
    path = r"./app/services/files"
    files = {
        "file": ("upload.txt", open(os.path.join(path, "upload.txt"), "rb")),
    }
    response = post(url, files=files)
    return response.json()
