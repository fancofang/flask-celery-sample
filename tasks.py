from main.extensions import celery

@celery.task(name='sum-of-two-numbers')
def add_together(a, b):
    return a + b