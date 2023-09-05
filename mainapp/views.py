from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
from django.template import RequestContext
from asgiref.sync import async_to_sync
import json


def home(request):
    return render(request, 'mainapp/index.html', {
        'room_name': "broadcast"
    })


def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification")
        }
    )
    return HttpResponse("Done")