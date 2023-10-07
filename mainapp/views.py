from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
from django.template import RequestContext
from celery import shared_task
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


@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return 'Done'