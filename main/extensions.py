from celery import Celery
from main.configs import Config

celery = Celery(broker=Config.CELERY_BROKER_URL, backend=Config.result_backend)