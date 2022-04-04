"""
    mdoels.py file
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICE = (
    ('male', 'male'),
    ('female', 'female'),
)


class Profile(models.Model):
    """
        custom profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=12)
    dob = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
