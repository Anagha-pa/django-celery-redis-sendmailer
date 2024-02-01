from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'confi.settings')

app = Celery('confi')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.enable_utc = False

app.conf.update(timezone = 'Europe/Paris')

app.autodiscover_tasks()

# celery beat settings
app.conf.beat_schedule = {
    'send-ad-mail-every-day': {
        'task':'timedmailer.task.send_ad_mails',
        'schedule':crontab(hour=15, minute=56),
        'args': ("I am Anagha") 
    }
}