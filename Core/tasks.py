import time
from celery import shared_task


@shared_task
def export():
    print('export start')
    time.sleep(10)
    print('export finish')
