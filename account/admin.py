"""
    admin.py file
"""
from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
        model admim
    """
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone', 'gender', 'dob']


admin.site.register(Profile, ProfileAdmin)
