"""
    notifiaction/apps.py
"""
from django.apps import AppConfig


class NotificationConfig(AppConfig):
    """
        app config class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notification'
    def ready(self):
        """
            ready method
        """
        import notification.signals
