"""
    admin.py file
"""
from django.contrib import admin
from notification.models import Notification


class NotificationModelAdmin(admin.ModelAdmin):
    """
        Notificaiton Admin model
    """
    list_display = ['title', 'text', 'types', 'user',
                 'scheduled', 'is_read', 'link']


admin.site.register(Notification, NotificationModelAdmin)
