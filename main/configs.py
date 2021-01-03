class Config(object):
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'    #has been deprecated
    result_backend = 'redis://localhost:6379/1'
