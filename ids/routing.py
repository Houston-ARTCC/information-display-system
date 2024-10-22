from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url

from apps.flights import consumers


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            url('ws/flights/', consumers.FlightConsumer.as_asgi()),
        ])
    ),
})
