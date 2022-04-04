"""
    accoutn routes
"""
from django.urls import path
from account.views import (
        RegistrationView,
        LoginView,
        LogoutView
    )

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
