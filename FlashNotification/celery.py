"""
    celery.py file
"""
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FlashNotification.settings')
app = Celery('FlashNotification')
# app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata")

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object(settings)
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """
        debug task
    """
    print(f'Request: {self.request}')
    