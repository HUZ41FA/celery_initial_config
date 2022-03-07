from __future__ import absolute_import, unicode_literals
import os 
from celery import Celery
from django.conf import settings
from pytz import timezone


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')

#Celery beat config
app.conf.beat_schedule = {

}

app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Karachi')

app.config_from_object(settings, namespace='celery')

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')