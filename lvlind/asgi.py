import os
import django
from channels.auth import AuthMiddlewareStack
from notifications_app.routing import websocket_urlpatterns
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault(  'DJANGO_SETTINGS_MODULE', 
                        'lvlind.settings'
                    )
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter( websocket_urlpatterns )
    )
})
