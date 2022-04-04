"""
    views.py file
"""
from django.urls import path
from notification.views import (
        HomeView,
        send_notification_websocket,
        HideNotificationView

    )

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('test/', send_notification_websocket, name="send_notification_websocket"),
    path('notification/hide/<int:notification_id>/',
            HideNotificationView.as_view(), name="hide-notification"),
]
