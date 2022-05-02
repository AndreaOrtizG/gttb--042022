import os
import time
from celery import Celery
from dotenv import load_dotenv
from requests import post

load_dotenv(".env")

celery = Celery("__name__ ")
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")



@celery.task(name="task_time")
def task_time(secs: int):
    url = "https://gttb.guane.dev/api/workers?task_complexity="+str(secs)
    response = post(url)
    return response.json()




