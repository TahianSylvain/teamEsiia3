from django.urls import re_path
from base.consumers import  ChatSocket
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', ChatSocket.as_asgi()),
    re_path(r'ws/notification/(?P<room_name>\w+)/$', consumers.NotificationConsumer.as_asgi()),
]