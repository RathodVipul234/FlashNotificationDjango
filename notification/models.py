"""
    models.py file
"""
from django.db import models

from account.models import Profile

# Create your models here.
TYPES_OF_NOTIFICATIONS = (
    ("ACTIVATE", "ACTIVATE"),
    ("SUSPENDED", "SUSPENDED"),
    ("CREDIT", "CREDIT"),
    ("DEBIT", "DEBIT"),
    ("OTHER", "OTHER"),
)


class Notification(models.Model):
    """
        Notificaiton
    """

    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    types = models.CharField(max_length=20, choices=TYPES_OF_NOTIFICATIONS, default="OTHER")
    user = models.ForeignKey(Profile, related_name="User", on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    link = models.URLField(null=True, blank=True)
    scheduled = models.DateTimeField(auto_created=True)

    def __str__(self):
        """
            return title
        """
        return str(self.title)
