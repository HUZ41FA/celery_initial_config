from celery import shared_task


@shared_task(bind=True)
def func(self):
    for i in range(100000000):
        print(i)
    return 'DONE'
