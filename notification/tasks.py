
"""
    Task.py file
"""

from celery.utils.log import get_task_logger
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core import serializers
from notification.models import Notification

logger = get_task_logger(__name__)


@shared_task(name="send_notification")
def send_notification(notification_id):
    """
        send notification message to wqebsocket using celery
    """
    notification_obj = Notification.objects.get(id=int(notification_id))
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"notification_{notification_obj.user.id}",
        {
            'type': 'send_notification',
            'notification': serializers.serialize('json', [notification_obj])
        }
    )
