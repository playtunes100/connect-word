"""
ASGI config for connectword project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import django

django.setup()
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import connectapp.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectword.settings')

from connectapp.models import *

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            connectapp.routing.websocket_urlpatterns
        )
    ),
    
})
