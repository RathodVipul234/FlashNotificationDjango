"""
    signal.py file
"""
import json

from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.db.models.signals import post_save
from django.dispatch import receiver

from notification.models import Notification


@receiver(post_save, sender=Notification)
def create_profile(sender, instance, created, **kwargs):
    """
        create new cron for notification object
    """
    if created:
        schedule, created = CrontabSchedule.objects.get_or_create(
            hour=instance.scheduled.hour,
            minute=instance.scheduled.minute,
            day_of_month=instance.scheduled.day,
            month_of_year=instance.scheduled.month,
            timezone="Asia/kolkata",
        )
        PeriodicTask.objects.create(crontab=schedule,
                                    name="TestTest Test" + str(instance.id),
                                    task="send_notification",
                                    args=json.dumps((instance.id,))
                                )
