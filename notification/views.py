"""
    view.py file
"""
import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers

from notification.models import Notification
from account.models import Profile


# Create your views here.


class LoginRequiredMixin(View):
    """
        Custome LoginRequiredMixin
    """
    def dispatch(self, request, *args, **kwargs):
        """
            custom dispatch method for restricting unauthoprize users
        """
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)


class HomeView(LoginRequiredMixin):
    """
        Home page view class
    """

    template_name = "home.html"

    def get(self, requset, *args, **kwargs):
        """
            Get Method
        """
        context = {}
        user = Profile.objects.get(username=self.request.user.username)
        context["notifications"] = Notification.objects.filter(
            user=user, is_read=False, scheduled__lte=datetime.datetime.now()
        )
        context["room_name"] = f"notification_{user.id}"

        return render(self.request, self.template_name, context)


class HideNotificationView(LoginRequiredMixin):
    """
        Hide notification ajax view
    """

    def post(self, request, *args, **kwargs):
        """
            change is_read status of notifiaction object
        """
        notification_id = kwargs.get("notification_id")
        notification_object = Notification.objects.get(id=notification_id)
        notification_object.is_read = True
        notification_object.save()
        return JsonResponse({"status": 200})



def send_notification_websocket(request):
    """
        Take Notificaiton Id for testing perpose.
        I have take 39. you can take accourding to your database.
        this class is only for send message to websocket without celery run.
    """
    notification_obj = Notification.objects.get(id=1)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"notification_{notification_obj.user.id}",
        {
            "type": "send_notification",
            "notification": serializers.serialize("json", [notification_obj]),
        },
    )

    return HttpResponse("done")
